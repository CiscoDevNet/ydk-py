


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BgpEbgpSendDmzEnableModeEnum' : _MetaInfoEnum('BgpEbgpSendDmzEnableModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'disable':'disable',
            'default':'default',
            'cumulative':'cumulative',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpVrfRouteTargetEnum' : _MetaInfoEnum('BgpVrfRouteTargetEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'as':'as_',
            'ipv4-address':'ipv4_address',
            'four-byte-as':'four_byte_as',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BmpPolicySelectEnum' : _MetaInfoEnum('BmpPolicySelectEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'pre-policy':'pre_policy',
            'post-policy':'post_policy',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpAdvRtEnum' : _MetaInfoEnum('BgpAdvRtEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'bgp-regular-rt':'bgp_regular_rt',
            'bgp-stitching-rt':'bgp_stitching_rt',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpSignalEnum' : _MetaInfoEnum('BgpSignalEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'bgp-disable':'bgp_disable',
            'ldp-disable':'ldp_disable',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpAigpCfgPoiEnum' : _MetaInfoEnum('BgpAigpCfgPoiEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'pre-best-path':'pre_best_path',
            'igp-cost':'igp_cost',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpFlowspecValidationCfgEnum' : _MetaInfoEnum('BgpFlowspecValidationCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'enable':'enable',
            'disable':'disable',
            'redirect-nexhop-disable':'redirect_nexhop_disable',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpReorgOptEnum' : _MetaInfoEnum('BgpReorgOptEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'bgp-cfg-adv':'bgp_cfg_adv',
            'bgp-cfg-adv-reorg':'bgp_cfg_adv_reorg',
            'bgp-cfg-adv-disable':'bgp_cfg_adv_disable',
            'bgp-cfg-adv-local':'bgp_cfg_adv_local',
            'bgp-cfg-adv-def-vrf-imp-disable':'bgp_cfg_adv_def_vrf_imp_disable',
            'bgp-cfg-adv-vrf-re-imp-disable':'bgp_cfg_adv_vrf_re_imp_disable',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpMvpnSfsSelectEnum' : _MetaInfoEnum('BgpMvpnSfsSelectEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'all-paths':'all_paths',
            'highest-ip-address':'highest_ip_address',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpSendMcastAttrCfgEnum' : _MetaInfoEnum('BgpSendMcastAttrCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpAfEncapsulationEnum' : _MetaInfoEnum('BgpAfEncapsulationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'vx-lan':'vx_lan',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpSiteOfOriginEnum' : _MetaInfoEnum('BgpSiteOfOriginEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'as':'as_',
            'ipv4-address':'ipv4_address',
            'four-byte-as':'four_byte_as',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BmpRouteDirectionEnum' : _MetaInfoEnum('BmpRouteDirectionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'inbound':'inbound',
            'outbound':'outbound',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpTcpModeEnum' : _MetaInfoEnum('BgpTcpModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'either':'either',
            'active-only':'active_only',
            'passive-only':'passive_only',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpRouteDistinguisherEnum' : _MetaInfoEnum('BgpRouteDistinguisherEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'auto':'auto',
            'as':'as_',
            'four-byte-as':'four_byte_as',
            'ipv4-address':'ipv4_address',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpOrfEnum' : _MetaInfoEnum('BgpOrfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'none':'none',
            'receive':'receive',
            'send':'send',
            'both':'both',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpClusterIdEnum' : _MetaInfoEnum('BgpClusterIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'number':'number',
            'ipv4-address':'ipv4_address',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpRpkiTransportEnum' : _MetaInfoEnum('BgpRpkiTransportEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'tcp':'tcp',
            'ssh':'ssh',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpAigpCfgEnum' : _MetaInfoEnum('BgpAigpCfgEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'enable':'enable',
            'disable':'disable',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'BgpBfdEnableModeEnum' : _MetaInfoEnum('BgpBfdEnableModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg',
        {
            'disable':'disable',
            'default':'default',
            'strict':'strict',
        }, 'Cisco-IOS-XR-ipv4-bgp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg']),
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.RouteDistinguisher' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.RouteDistinguisher',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                IP address index
                ''',
                'address_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ASN Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpRouteDistinguisherEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpRouteDistinguisherEnum', 
                [], [], 
                '''                Type of RD
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'route-distinguisher',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Mvpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Mvpn',
            False, 
            [
            _MetaInfoClassMember('single-forwarder-selection', REFERENCE_ENUM_CLASS, 'BgpMvpnSfsSelectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpMvpnSfsSelectEnum', 
                [], [], 
                '''                Select MVPN single forwarder selection
                ''',
                'single_forwarder_selection',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'mvpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ebgp',
            False, 
            [
            _MetaInfoClassMember('order-by-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Order candidate multipaths by IGP
                metric
                ''',
                'order_by_igp_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('paths-value', ATTRIBUTE, 'int' , None, None, 
                [('2', '32')], [], 
                '''                Number of paths
                ''',
                'paths_value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selective', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths only from marked
                neighbors
                ''',
                'selective',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('unequal-cost', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                UNUSED
                ''',
                'unequal_cost',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Eibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Eibgp',
            False, 
            [
            _MetaInfoClassMember('order-by-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Order candidate multipaths by IGP
                metric
                ''',
                'order_by_igp_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('paths-value', ATTRIBUTE, 'int' , None, None, 
                [('2', '32')], [], 
                '''                Number of paths
                ''',
                'paths_value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selective', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths only from marked
                neighbors
                ''',
                'selective',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('unequal-cost', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                UNUSED
                ''',
                'unequal_cost',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'eibgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ibgp',
            False, 
            [
            _MetaInfoClassMember('order-by-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Order candidate multipaths by IGP
                metric
                ''',
                'order_by_igp_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('paths-value', ATTRIBUTE, 'int' , None, None, 
                [('2', '32')], [], 
                '''                Number of paths
                ''',
                'paths_value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selective', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths only from marked
                neighbors
                ''',
                'selective',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('unequal-cost', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths to have different IGP
                metrics
                ''',
                'unequal_cost',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ibgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses.AggregateAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses.AggregateAddress',
            False, 
            [
            _MetaInfoClassMember('aggregate-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Aggregate in prefix/length format (address
                part)
                ''',
                'aggregate_addr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('aggregate-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Aggregate in prefix/length format (address
                        part)
                        ''',
                        'aggregate_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('aggregate-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Aggregate in prefix/length format (address
                        part)
                        ''',
                        'aggregate_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('aggregate-prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Aggregate in prefix/length format (prefix
                part)
                ''',
                'aggregate_prefix',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('generate-confederation-set-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate AS confederation set path
                information, FALSE otherwise
                ''',
                'generate_confederation_set_info',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('generate-set-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate AS set path information,
                FALSE otherwise
                ''',
                'generate_set_info',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy on which to condition
                advertisement, suppression, and attributes
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('summary-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to filter more specific routes from
                updates, FALSEotherwise
                ''',
                'summary_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aggregate-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses',
            False, 
            [
            _MetaInfoClassMember('aggregate-address', REFERENCE_LIST, 'AggregateAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses.AggregateAddress', 
                [], [], 
                '''                Aggregate address configuration
                ''',
                'aggregate_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aggregate-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Dampening' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Dampening',
            False, 
            [
            _MetaInfoClassMember('half-life', ATTRIBUTE, 'int' , None, None, 
                [('1', '45')], [], 
                '''                Half-life time for the penalty (minutes).
                ''',
                'half_life',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reuse-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '20000')], [], 
                '''                Value to start reusing a route.
                ''',
                'reuse_threshold',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to specify criteria for dampening.
                This cannot be specified if any other
                parameters are specified.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '20000')], [], 
                '''                Value to start suppressing a route.
                ''',
                'suppress_threshold',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum duration to suppress a stable route
                (seconds).
                ''',
                'suppress_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.RipRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.RipRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'rip-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LispRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LispRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'lisp-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.StaticRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.StaticRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'static-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Distance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Distance',
            False, 
            [
            _MetaInfoClassMember('external-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for routes external to the AS
                ''',
                'external_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for routes internal to the AS
                ''',
                'internal_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for local routes
                ''',
                'local_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LabelMode' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LabelMode',
            False, 
            [
            _MetaInfoClassMember('label-allocation-mode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label allocation mode: per-ce  Set per CE label
                mode, per-vrf Set per VRF label mode,
                per-prefix Set per Prefix label mode (for
                MPLS-VPN only)
                ''',
                'label_allocation_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label mode route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'label-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes.EigrpRoute' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes.EigrpRoute',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                EIGRP router tag
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('redist-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Redistribution type: 01 for internal routes,
                02 for external routes, Logical combinations
                permitted.
                ''',
                'redist_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'eigrp-route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes',
            False, 
            [
            _MetaInfoClassMember('eigrp-route', REFERENCE_LIST, 'EigrpRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes.EigrpRoute', 
                [], [], 
                '''                Redistribute EIGRP routes
                ''',
                'eigrp_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'eigrp-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks.SourcedNetwork' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks.SourcedNetwork',
            False, 
            [
            _MetaInfoClassMember('network-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format (address part)
                ''',
                'network_addr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('network-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Network in prefix/length format (address part)
                        ''',
                        'network_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('network-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Network in prefix/length format (address part)
                        ''',
                        'network_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('network-prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Network in prefix/length format (prefix part)
                ''',
                'network_prefix',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('backdoor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify a BGP backdoor route, default is FALSE
                ''',
                'backdoor',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'sourced-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks',
            False, 
            [
            _MetaInfoClassMember('sourced-network', REFERENCE_LIST, 'SourcedNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks.SourcedNetwork', 
                [], [], 
                '''                Sourced network configuration
                ''',
                'sourced_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'sourced-networks',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.ConnectedRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.ConnectedRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'connected-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AllocateLabel' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AllocateLabel',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether all nets should be labeled, default is
                FALSE
                ''',
                'all',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'allocate-label',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AdditionalPathsSelection' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AdditionalPathsSelection',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for selection
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selection', REFERENCE_ENUM_CLASS, 'BgpafAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpafAdditionalPathsCfgEnum', 
                [], [], 
                '''                Enable/disable selection 
                ''',
                'selection',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'additional-paths-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes.OspfRoute' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes.OspfRoute',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF router tag
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('redist-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Redistribution type: 01 for internal routes,
                02 for external routes of type 1, 04 for
                external routes of type 2, 08 for NSSA
                external routes of type 1, 10 for NSSA
                external routes of type 2, 20 for external
                routes, 40 for NSSA external routes.  Logical
                combinations permitted.
                ''',
                'redist_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ospf-route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes',
            False, 
            [
            _MetaInfoClassMember('ospf-route', REFERENCE_LIST, 'OspfRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes.OspfRoute', 
                [], [], 
                '''                Redistribute OSPF routes
                ''',
                'ospf_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ospf-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.MobileRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.MobileRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'mobile-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SubscriberRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SubscriberRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'subscriber-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('additional-paths-receive', REFERENCE_ENUM_CLASS, 'BgpafAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpafAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-selection', REFERENCE_CLASS, 'AdditionalPathsSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AdditionalPathsSelection', 
                [], [], 
                '''                Configure additional paths selection
                ''',
                'additional_paths_selection',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send', REFERENCE_ENUM_CLASS, 'BgpafAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpafAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route-safi-unicast', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label via Unicast SAFI
                ''',
                'advertise_local_labeled_route_safi_unicast',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aggregate-addresses', REFERENCE_CLASS, 'AggregateAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses', 
                [], [], 
                '''                Configure BGP aggregate entries
                ''',
                'aggregate_addresses',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allocate-label', REFERENCE_CLASS, 'AllocateLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AllocateLabel', 
                [], [], 
                '''                Label allocation policy
                ''',
                'allocate_label',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allow-vpn-default-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send default orig route to VPN
                neighborFALSE to not send default
                originate route 
                ''',
                'allow_vpn_default_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('attribute-download', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute download configuration
                ''',
                'attribute_download',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-external', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BE FALSE to disable BE
                inheritance from a parent
                ''',
                'best_external',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('connected-routes', REFERENCE_CLASS, 'ConnectedRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.ConnectedRoutes', 
                [], [], 
                '''                Redistribute connected routes
                ''',
                'connected_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dampening', REFERENCE_CLASS, 'Dampening' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Dampening', 
                [], [], 
                '''                Enable route-flap dampening
                ''',
                'dampening',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-as-path-loop-check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable outbound AS Path loop check
                ''',
                'disable_as_path_loop_check',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('distance', REFERENCE_CLASS, 'Distance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Distance', 
                [], [], 
                '''                Define an administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dynamic-med-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Update generation delay (in minutes) after a MED
                change
                ''',
                'dynamic_med_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ebgp', 
                [], [], 
                '''                Use eBGP multipaths
                ''',
                'ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('eibgp', REFERENCE_CLASS, 'Eibgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Eibgp', 
                [], [], 
                '''                Use eiBGP multipaths
                ''',
                'eibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('eigrp-routes', REFERENCE_CLASS, 'EigrpRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes', 
                [], [], 
                '''                Redistribute information for EIGRP routes.
                ''',
                'eigrp_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the address family. Deletion of this
                object causes deletion of all the objects under
                GlobalAF/VRFGlobalAF associated with this object
                .
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ibgp', REFERENCE_CLASS, 'Ibgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ibgp', 
                [], [], 
                '''                Use iBGP multipaths
                ''',
                'ibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('label-mode', REFERENCE_CLASS, 'LabelMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LabelMode', 
                [], [], 
                '''                BGP 6PE/MPLS-VPN label allocation mode
                ''',
                'label_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('lisp-routes', REFERENCE_CLASS, 'LispRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LispRoutes', 
                [], [], 
                '''                Redistribute lisp routes
                ''',
                'lisp_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mobile-routes', REFERENCE_CLASS, 'MobileRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.MobileRoutes', 
                [], [], 
                '''                Redistribute mobile routes
                ''',
                'mobile_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mvpn', REFERENCE_CLASS, 'Mvpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Mvpn', 
                [], [], 
                '''                MVPN configurations
                ''',
                'mvpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-resolution-prefix-length-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Minimum prefix-length for nexthop resolution
                ''',
                'next_hop_resolution_prefix_length_minimum',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ospf-routes', REFERENCE_CLASS, 'OspfRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes', 
                [], [], 
                '''                Redistribute information for OSPF routes.
                ''',
                'ospf_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('permanent-network', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for permanent networks
                ''',
                'permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reset-weight-on-import', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to reset weight on import. FALSE to not
                reset and to prevent inheritance from a parent
                ''',
                'reset_weight_on_import',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rip-routes', REFERENCE_CLASS, 'RipRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.RipRoutes', 
                [], [], 
                '''                Redistribute RIP routes
                ''',
                'rip_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-download', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Route-Target download configuration
                ''',
                'rt_download',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('sourced-networks', REFERENCE_CLASS, 'SourcedNetworks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks', 
                [], [], 
                '''                Specify a network to announce via BGP
                ''',
                'sourced_networks',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('static-routes', REFERENCE_CLASS, 'StaticRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.StaticRoutes', 
                [], [], 
                '''                Redistribute static routes
                ''',
                'static_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('subscriber-routes', REFERENCE_CLASS, 'SubscriberRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SubscriberRoutes', 
                [], [], 
                '''                Redistribute subscriber routes
                ''',
                'subscriber_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('table-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure policy for installation of routes to
                RIB
                ''',
                'table_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-global-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs',
            False, 
            [
            _MetaInfoClassMember('vrf-global-af', REFERENCE_LIST, 'VrfGlobalAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf', 
                [], [], 
                '''                Global VRF AF-specific configuration
                ''',
                'vrf_global_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-global-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces.MplsActivatedInterface' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces.MplsActivatedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'mpls-activated-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces',
            False, 
            [
            _MetaInfoClassMember('mpls-activated-interface', REFERENCE_LIST, 'MplsActivatedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces.MplsActivatedInterface', 
                [], [], 
                '''                Configure a MPLS activated interface
                ''',
                'mpls_activated_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'mpls-activated-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.GlobalTimers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.GlobalTimers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time (seconds).  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval (seconds)
                ''',
                'keepalive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time (seconds). Specify
                0 to disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'global-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.Bfd' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created
                by BGP
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.SendSocketBufferSizes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.SendSocketBufferSizes',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP Write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-socket-buffer-sizes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.ReceiveSocketBufferSizes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.ReceiveSocketBufferSizes',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP Read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-socket-buffer-sizes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal',
            False, 
            [
            _MetaInfoClassMember('best-path-aigp-ignore', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria to
                ignore AIGP unless both paths whichare compared
                have AIGP attribute
                ''',
                'best_path_aigp_ignore',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-as-multipath-relax', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default multi-route selection criteria to
                relax as-path checking - only require same
                aspath length
                ''',
                'best_path_as_multipath_relax',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-as-path-length', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria to
                ignore AS path length
                ''',
                'best_path_as_path_length',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-confederation-paths', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria and
                allow the comparing of MED among confederation
                paths
                ''',
                'best_path_confederation_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-cost-community', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria to
                ignore cost community comparison
                ''',
                'best_path_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-med-always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria and
                allow comparing of MED from different neighbors
                ''',
                'best_path_med_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-med-missing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Treat missing MED as the least preferred one
                ''',
                'best_path_med_missing',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-router-id', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria and
                compare router-id for identical EBGP paths
                ''',
                'best_path_router_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Control distribution of default information
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Default redistributed metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-auto-soft-reset', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable automatic soft peer reset on policy
                reconfiguration
                ''',
                'disable_auto_soft_reset',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-enforce-first-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable enforce the first AS for EBGP routes
                ''',
                'disable_enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-fast-external-fallover', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable immediate reset session if a link to a
                directly connected external peer goes down
                ''',
                'disable_fast_external_fallover',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-msg-log', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound and outbound messagelogging for
                all neighbors under the vrf
                ''',
                'disable_msg_log',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-neighbor-logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable neighbor change logging
                ''',
                'disable_neighbor_logging',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('exists', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create this VRF. Deletion of this object
                causes deletion of all the objects under
                VRF associated with this object.
                ''',
                'exists',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global-timers', REFERENCE_CLASS, 'GlobalTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.GlobalTimers', 
                [], [], 
                '''                Adjust routing timers.
                ''',
                'global_timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('igp-redist-internal', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow redistribution of iBGP into IGPs
                (dangerous)
                ''',
                'igp_redist_internal',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configure default local preference
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-activated-interfaces', REFERENCE_CLASS, 'MplsActivatedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces', 
                [], [], 
                '''                Configure list of MPLS activated interfaces
                ''',
                'mpls_activated_interfaces',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multi-path-as-path-ignore-onwards', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default multi-route selection criteria to
                ignore everything onwards as-path check
                ''',
                'multi_path_as_path_ignore_onwards',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-socket-buffer-sizes', REFERENCE_CLASS, 'ReceiveSocketBufferSizes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.ReceiveSocketBufferSizes', 
                [], [], 
                '''                Set socket and BGP receive buffer sizes
                ''',
                'receive_socket_buffer_sizes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-distinguisher', REFERENCE_CLASS, 'RouteDistinguisher' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.RouteDistinguisher', 
                [], [], 
                '''                Route distinguisher
                ''',
                'route_distinguisher',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure Router-id
                ''',
                'router_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-socket-buffer-sizes', REFERENCE_CLASS, 'SendSocketBufferSizes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.SendSocketBufferSizes', 
                [], [], 
                '''                set socket parameters
                ''',
                'send_socket_buffer_sizes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf-global-afs', REFERENCE_CLASS, 'VrfGlobalAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs', 
                [], [], 
                '''                Global VRF-specific configuration
                ''',
                'vrf_global_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-global',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity',
            False, 
            [
            _MetaInfoClassMember('cost-community-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Cost Community ID
                ''',
                'cost_community_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cost-community-poi-type', REFERENCE_ENUM_CLASS, 'BgpAigpCfgPoiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgPoiEnum', 
                [], [], 
                '''                Cost Community POI
                ''',
                'cost_community_poi_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable sending cost community, FALSE
                otherwise 
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transitive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True to send transitive cost community FALSE
                otherwise
                ''',
                'transitive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aigp-cost-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-disable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes',
            False, 
            [
            _MetaInfoClassMember('discard-extra-paths', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discard extra paths when limit is exceeded
                ''',
                'discard_extra_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum prefixes limit
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Restart interval
                ''',
                'restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to only give a warning message when limit
                is exceeded.  FALSE to accept max prefix limit
                only.
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message.
                ''',
                'warning_percentage',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'maximum-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates.
                FALSE to prevent remove-private-AS from being
                inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path-inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime',
            False, 
            [
            _MetaInfoClassMember('stale-time-accept', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_accept',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('stale-time-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af-long-lived-graceful-restart-stale-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                IP address Index
                ''',
                'address_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpSiteOfOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSiteOfOriginEnum', 
                [], [], 
                '''                Type of Extended community
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'site-of-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.Import_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.Import_',
            False, 
            [
            _MetaInfoClassMember('import-reoriginate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes, FALSE to
                not Reoriginate imported routes - not supported
                ''',
                'import_reoriginate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-reoriginate-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes with
                Stitching RTs, FALSE to Reoriginate imported
                routes with normal RTs
                ''',
                'import_reoriginate_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Import with Stitching RTs, FALSE to
                Import with normal RTs
                ''',
                'import_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prevent default-originate from, being
                inherited from a parent. TRUE otherwise.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to specify criteria to
                originate default.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'default-originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration',
            False, 
            [
            _MetaInfoClassMember('inbound-soft', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prohibit inbound soft reconfiguration.
                TRUE otherwise.
                ''',
                'inbound_soft',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to always use soft reconfig, even if route
                refresh is supported.  FALSE otherwise.
                ''',
                'soft_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'soft-reconfiguration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                .  FALSE to prevent remove-private-AS from
                being inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                BGP neighbor address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('accept-own', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Handle self-originated routes with Accept-Own
                community. Valid for following neighbor
                address-families: VPNv4Unicast, VPNv6Unicast.
                ''',
                'accept_own',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('accept-route-legacy-rt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a accept-route-legacy-RT. 
                FALSE to prevent accept-route-legacy-RT from
                being inherited.
                ''',
                'accept_route_legacy_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('activate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Activate an address family for this neighbor.
                Deletion of this object causes deletion of all
                the objects under
                NeighborAF/VRFNeighborAF/NeighborGroupAF
                associated with this object.
                ''',
                'activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseDefImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseDefImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-disable', REFERENCE_CLASS, 'AdvertiseDisable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable', 
                [], [], 
                '''                Disable Advertise Of Routes to the peer
                ''',
                'advertise_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseLocalL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label
                ''',
                'advertise_local_labeled_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v4', REFERENCE_CLASS, 'AdvertiseLocalV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v6', REFERENCE_CLASS, 'AdvertiseLocalV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-orf', REFERENCE_ENUM_CLASS, 'BgpOrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpOrfEnum', 
                [], [], 
                '''                Advertise ORF capability to the peer
                ''',
                'advertise_orf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-permanent-network', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise Permanent Networks to the peer
                ''',
                'advertise_permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v4', REFERENCE_CLASS, 'AdvertiseV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v6', REFERENCE_CLASS, 'AdvertiseV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration for this address-family
                from an AF-group
                ''',
                'af_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable Accumulated IGP Metric for this neighbor.
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-cost-community', REFERENCE_CLASS, 'AigpCostCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity', 
                [], [], 
                '''                Send AIGP value in Cost Community. 
                ''',
                'aigp_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-send-med', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable/Disable sending AIGP in MED 
                ''',
                'aigp_send_med',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allow-as-in', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Allow as-path with my AS present in it
                ''',
                'allow_as_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to override matching AS-number while
                sending update. FALSE to prevent as-override
                from being inherited from the parent
                ''',
                'as_override',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-originate', REFERENCE_CLASS, 'DefaultOriginate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate', 
                [], [], 
                '''                Originate default route to this neighbor
                ''',
                'default_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set default weight for routes from this
                neighbor/neighbor-group/af-group
                ''',
                'default_weight',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'BgpAfEncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAfEncapsulationEnum', 
                [], [], 
                '''                Encapsulation type for this neighbor
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('flowspec-validation', REFERENCE_ENUM_CLASS, 'BgpFlowspecValidationCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpFlowspecValidationCfgEnum', 
                [], [], 
                '''                Config Flowspec validation for this neighbor
                ''',
                'flowspec_validation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import', REFERENCE_CLASS, 'Import_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.Import_', 
                [], [], 
                '''                Import Reorigination options for Routes from the
                peer
                ''',
                'import_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('maximum-prefixes', REFERENCE_CLASS, 'MaximumPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes', 
                [], [], 
                '''                Maximum number of prefixes to accept from this
                peer
                ''',
                'maximum_prefixes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multipath', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow paths from this neighbor to be eligible
                for selective multipath
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-capable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to treat neighbor as Long-lived
                Graceful-restart capable. FALSE to rely on
                capability negotiation.
                ''',
                'neighbor_af_long_lived_graceful_restart_capable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-stale-time', REFERENCE_CLASS, 'NeighborAfLongLivedGracefulRestartStaleTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime', 
                [], [], 
                '''                Maximum time to wait before purging long lived
                routes
                ''',
                'neighbor_af_long_lived_graceful_restart_stale_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-self', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable the next hop calculation and  insert
                your own address in the nexthop field of
                advertised routes you learned from the neighbor.
                ''',
                'next_hop_self',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop before
                advertising to eBGP peers. FALSE to prevent
                next-hop-unchanged from being inherited.
                ''',
                'next_hop_unchanged',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged-multipath', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop for
                multipaths. FALSE to prevent next-hop-unchanged
                for multipaths.
                ''',
                'next_hop_unchanged_multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-orf-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix ORF policy name for incoming updates
                ''',
                'prefix_orf_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath', 
                [], [], 
                '''                Remove private AS number from outbound updates
                ''',
                'remove_private_as_entire_as_path',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path-inbound', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPathInbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound', 
                [], [], 
                '''                Remove private AS number from inbound updates
                ''',
                'remove_private_as_entire_as_path_inbound',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to inbound routes
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to outbound routes
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a route-reflector-client. 
                FALSE to prevent route-reflector-client from
                being inherited.
                ''',
                'route_reflector_client',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp-graceful-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp_graceful_shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-ext-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send extended communities to the
                external neighbor/neighbor-group/af-group. 
                FALSE not to send and to prevent inheritance
                from a parent
                ''',
                'send_ext_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('site-of-origin', REFERENCE_CLASS, 'SiteOfOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin', 
                [], [], 
                '''                Site-of-Origin extended community associated
                with the neighbor
                ''',
                'site_of_origin',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-reconfiguration', REFERENCE_CLASS, 'SoftReconfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration', 
                [], [], 
                '''                Enable/disable inbound soft reconfiguration for
                this neighbor/neighbor-group/af-group
                ''',
                'soft_reconfiguration',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-neighbor-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs',
            False, 
            [
            _MetaInfoClassMember('vrf-neighbor-af', REFERENCE_LIST, 'VrfNeighborAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf', 
                [], [], 
                '''                Address family type of a VRF neighbor
                ''',
                'vrf_neighbor_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-neighbor-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('local-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a local
                address if the parent has one.FALSE to specify
                local ip address
                ''',
                'local_address_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Local ip address for neighbor
                ''',
                'local_ip_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates.BmpActivate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates.BmpActivate',
            False, 
            [
            _MetaInfoClassMember('server-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                BMP Server ID
                ''',
                'server_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates',
            False, 
            [
            _MetaInfoClassMember('bmp-activate', REFERENCE_LIST, 'BmpActivate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates.BmpActivate', 
                [], [], 
                '''                Enable BMP logging for this particular server
                ''',
                'bmp_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('max-hop-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum hop count
                ''',
                'max_hop_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-deactivation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to not enable MPLS and NULL rewrite.
                ''',
                'mpls_deactivation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp-multihop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Local AS and prevent it from being
                inherited from a parent
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dual-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dual-AS mode
                ''',
                'dual_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('no-prepend', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not prepend Local AS to announcements from
                this neighbor
                ''',
                'no_prepend',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('replace-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prepend only Local AS to announcements from
                this neighbor
                ''',
                'replace_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Password' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Password',
            False, 
            [
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password.  Leave unspecified when
                disabling the password.
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                password even if the parent has one.  FALSEto
                specify a password
                ''',
                'password_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.AdvertisementInterval' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.AdvertisementInterval',
            False, 
            [
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Minimum advertisement interval time, secs part
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('minimum-interval-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Minimum advertisement interval time, msecs part
                ''',
                'minimum_interval_msecs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertisement-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.NeighborClusterId' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.NeighborClusterId',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Route-Reflector Cluster ID in IPV4 address
                format
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Route-Reflector Cluster ID as 32 bit quantity
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-cluster-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tcpmss' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tcpmss',
            False, 
            [
            _MetaInfoClassMember('mss', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                Maximum Segment Size
                ''',
                'mss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance ofTCP MSS
                valuefrom its parents.FALSE, otherwise
                ''',
                'tcpmss_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tcpmss',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tos' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tos',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpTosEnum', 
                [], [], 
                '''                Set type of service
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TOS value to set
                ''',
                'value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'BgpPrecedenceDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpPrecedenceDscpEnum', 
                        [], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers',
            False, 
            [
            _MetaInfoClassMember('non-circular-buffer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure non-circular buffer
                ''',
                'non_circular_buffer',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('number-of-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                Number of message buffers
                ''',
                'number_of_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering-message-buffers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure inbound update filtering
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-attribute-filter-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Attribute-filter group name for update
                filtering
                ''',
                'update_in_filtering_attribute_filter_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-message-buffers', REFERENCE_CLASS, 'UpdateInFilteringMessageBuffers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers', 
                [], [], 
                '''                Message buffers to store filtered updates
                ''',
                'update_in_filtering_message_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-syslog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound update filtering syslog
                messages
                ''',
                'update_in_filtering_syslog_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogOut' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogOut',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Outbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                outbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.ReceiveBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.ReceiveBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogIn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogIn',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Inbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                inbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.SendBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.SendBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time.  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval
                ''',
                'keepalive_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time.  Specify 0 to
                disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Keychain' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Keychain',
            False, 
            [
            _MetaInfoClassMember('keychain-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                keychain based authentication even if the
                parent has one.FALSE to specify a keychain name
                ''',
                'keychain_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the keychain associated with neighbor
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference',
            False, 
            [
            _MetaInfoClassMember('gshut-loc-pref-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of Local Pref
                value from its parents.FALSE, otherwise
                ''',
                'gshut_loc_pref_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Preference Value
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-local-preference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends',
            False, 
            [
            _MetaInfoClassMember('as-prepends', ATTRIBUTE, 'int' , None, None, 
                [('0', '6')], [], 
                '''                number of times AS prepends
                ''',
                'as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('gshut-prepends-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of AS Prepends
                value from its parents.FALSE, otherwise
                ''',
                'gshut_prepends_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-as-prepends',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter Graceful Maintenance mode to configure
                parametrs
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-activate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initiate the graceful shutdown procedure
                ''',
                'graceful_maintenance_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-as-prepends', REFERENCE_CLASS, 'GracefulMaintenanceAsPrepends' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends', 
                [], [], 
                '''                Number of times to prepend local AS number to
                the AS path
                ''',
                'graceful_maintenance_as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-local-preference', REFERENCE_CLASS, 'GracefulMaintenanceLocalPreference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference', 
                [], [], 
                '''                Set Local Preference to advertise routes with
                ''',
                'graceful_maintenance_local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('additional-paths-receive-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertisement-interval', REFERENCE_CLASS, 'AdvertisementInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.AdvertisementInterval', 
                [], [], 
                '''                Minimum interval between sending BGP routing
                updates
                ''',
                'advertisement_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-enable-modes', REFERENCE_ENUM_CLASS, 'BgpBfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpBfdEnableModeEnum', 
                [], [], 
                '''                Strict mode, Default mode or Disable to prevent
                inheritance from a parent
                ''',
                'bfd_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'bfd_minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created by
                BGP
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bmp-activates', REFERENCE_CLASS, 'BmpActivates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates', 
                [], [], 
                '''                Enable BMP logging for this neighbor
                ''',
                'bmp_activates',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Up to 80 characters describing this neighbor
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.EbgpMultihop', 
                [], [], 
                '''                Allow EBGP neighbors not on directly connected
                networks
                ''',
                'ebgp_multihop',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-recv-dmz', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to receive DMZ link bandwidth from ebgp
                peer. FALSE to not receive from ebgp peer and to
                prevent inheritance from a parent
                ''',
                'ebgp_recv_dmz',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-send-dmz-enable-modes', REFERENCE_ENUM_CLASS, 'BgpEbgpSendDmzEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpEbgpSendDmzEnableModeEnum', 
                [], [], 
                '''                Default mode, Cumulative mode or Disable to
                prevent inheritance from a parent
                ''',
                'ebgp_send_dmz_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('egress-peer-engineering', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable egress peer engineering FALSE to
                disable egress peer engineering and to prevent
                inheritance from a parent
                ''',
                'egress_peer_engineering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enforce-first-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enforce first AS; FALSE to not enforce
                first AS.
                ''',
                'enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance', REFERENCE_CLASS, 'GracefulMaintenance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance', 
                [], [], 
                '''                Graceful Maintenance mode
                ''',
                'graceful_maintenance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('idle-watch-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '1800')], [], 
                '''                Time to wait for deleteing IDLE state Dynamic
                peer
                ''',
                'idle_watch_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ignore-connected-check-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable the connected nexthop check for
                this peer.FALSE to enable the connected nexthop
                check for this peer.
                ''',
                'ignore_connected_check_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-vpn-client-ibgpce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to preserve the CE path attributes.FALSE to
                override CE path attributes.
                ''',
                'internal_vpn_client_ibgpce',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain', REFERENCE_CLASS, 'Keychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Keychain', 
                [], [], 
                '''                Set or disable keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAddress', 
                [], [], 
                '''                Local ip address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-as', REFERENCE_CLASS, 'LocalAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAs', 
                [], [], 
                '''                Specify a local-as number
                ''',
                'local_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('max-peers', ATTRIBUTE, 'int' , None, None, 
                [('1', '4096')], [], 
                '''                Set Maximum Peers in Dynamic Range
                ''',
                'max_peers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-in', REFERENCE_CLASS, 'MsgLogIn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogIn', 
                [], [], 
                '''                Message log inbound
                ''',
                'msg_log_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-out', REFERENCE_CLASS, 'MsgLogOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogOut', 
                [], [], 
                '''                Message log outbound
                ''',
                'msg_log_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-cluster-id', REFERENCE_CLASS, 'NeighborClusterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.NeighborClusterId', 
                [], [], 
                '''                Neighbor Cluster-id
                ''',
                'neighbor_cluster_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Enable graceful restart support for
                neighbor.  FALSE to disable graceful restart
                support for neighbor.
                ''',
                'neighbor_graceful_restart',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-stalepath-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Maximum time to wait for restart of GR capable
                peer
                ''',
                'neighbor_graceful_restart_stalepath_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Restart time advertised to neighbor
                ''',
                'neighbor_graceful_restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration from a neighbor-group
                ''',
                'neighbor_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Password', 
                [], [], 
                '''                Set or disable a password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('propagate-dmz-link-bandwidth', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to propagate DMZ link bandwidth.  FALSE to
                not propagate and to prevent inheritance from a
                parent
                ''',
                'propagate_dmz_link_bandwidth',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-buffer-size', REFERENCE_CLASS, 'ReceiveBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.ReceiveBufferSize', 
                [], [], 
                '''                Set socket receive buffer size and BGP read
                buffer size
                ''',
                'receive_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.RemoteAs', 
                [], [], 
                '''                Set remote AS
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote-as-list group name
                ''',
                'remote_as_list',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-buffer-size', REFERENCE_CLASS, 'SendBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.SendBufferSize', 
                [], [], 
                '''                Set socket send buffer size and BGP write buffer
                size
                ''',
                'send_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit address-family independent config from a
                session-group
                ''',
                'session_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-open-mode', REFERENCE_ENUM_CLASS, 'BgpTcpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpTcpModeEnum', 
                [], [], 
                '''                TCP mode to be used to establish BGP session
                ''',
                'session_open_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to shutdown this entity, FALSE to prevent
                this entity from being shutdown even if the
                parent is.
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-all-capabilities', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress all capabilities. FALSE to not
                suppress and to prevent inheritance from a
                parent
                ''',
                'suppress_all_capabilities',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-four-byte-as-capability', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress BGP 4-byte-as capability. 
                FALSE to not suppress it and to prevent
                inheritance from a parent
                ''',
                'suppress_four_byte_as_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss', REFERENCE_CLASS, 'Tcpmss' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tcpmss', 
                [], [], 
                '''                TCP Maximum segment size
                ''',
                'tcpmss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Timers', 
                [], [], 
                '''                BGP per neighbor timers.
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tos', 
                [], [], 
                '''                TOS (Type Of Service)
                ''',
                'tos',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ttl-security', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BGP TTL Security.  FALSE to not
                enable it and to prevent inheritance from a
                parent
                ''',
                'ttl_security',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering', REFERENCE_CLASS, 'UpdateInFiltering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering', 
                [], [], 
                '''                Inbound update filtering
                ''',
                'update_in_filtering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Select an interface to configure
                ''',
                'update_source_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf-neighbor-afs', REFERENCE_CLASS, 'VrfNeighborAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs', 
                [], [], 
                '''                Address family type of a VRF neighbor
                ''',
                'vrf_neighbor_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity',
            False, 
            [
            _MetaInfoClassMember('cost-community-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Cost Community ID
                ''',
                'cost_community_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cost-community-poi-type', REFERENCE_ENUM_CLASS, 'BgpAigpCfgPoiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgPoiEnum', 
                [], [], 
                '''                Cost Community POI
                ''',
                'cost_community_poi_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable sending cost community, FALSE
                otherwise 
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transitive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True to send transitive cost community FALSE
                otherwise
                ''',
                'transitive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aigp-cost-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-disable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes',
            False, 
            [
            _MetaInfoClassMember('discard-extra-paths', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discard extra paths when limit is exceeded
                ''',
                'discard_extra_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum prefixes limit
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Restart interval
                ''',
                'restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to only give a warning message when limit
                is exceeded.  FALSE to accept max prefix limit
                only.
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message.
                ''',
                'warning_percentage',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'maximum-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates.
                FALSE to prevent remove-private-AS from being
                inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path-inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime',
            False, 
            [
            _MetaInfoClassMember('stale-time-accept', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_accept',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('stale-time-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af-long-lived-graceful-restart-stale-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                IP address Index
                ''',
                'address_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpSiteOfOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSiteOfOriginEnum', 
                [], [], 
                '''                Type of Extended community
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'site-of-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.Import_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.Import_',
            False, 
            [
            _MetaInfoClassMember('import-reoriginate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes, FALSE to
                not Reoriginate imported routes - not supported
                ''',
                'import_reoriginate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-reoriginate-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes with
                Stitching RTs, FALSE to Reoriginate imported
                routes with normal RTs
                ''',
                'import_reoriginate_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Import with Stitching RTs, FALSE to
                Import with normal RTs
                ''',
                'import_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prevent default-originate from, being
                inherited from a parent. TRUE otherwise.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to specify criteria to
                originate default.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'default-originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration',
            False, 
            [
            _MetaInfoClassMember('inbound-soft', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prohibit inbound soft reconfiguration.
                TRUE otherwise.
                ''',
                'inbound_soft',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to always use soft reconfig, even if route
                refresh is supported.  FALSE otherwise.
                ''',
                'soft_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'soft-reconfiguration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                .  FALSE to prevent remove-private-AS from
                being inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                BGP neighbor address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('accept-own', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Handle self-originated routes with Accept-Own
                community. Valid for following neighbor
                address-families: VPNv4Unicast, VPNv6Unicast.
                ''',
                'accept_own',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('accept-route-legacy-rt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a accept-route-legacy-RT. 
                FALSE to prevent accept-route-legacy-RT from
                being inherited.
                ''',
                'accept_route_legacy_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('activate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Activate an address family for this neighbor.
                Deletion of this object causes deletion of all
                the objects under
                NeighborAF/VRFNeighborAF/NeighborGroupAF
                associated with this object.
                ''',
                'activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseDefImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseDefImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-disable', REFERENCE_CLASS, 'AdvertiseDisable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable', 
                [], [], 
                '''                Disable Advertise Of Routes to the peer
                ''',
                'advertise_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseLocalL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label
                ''',
                'advertise_local_labeled_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v4', REFERENCE_CLASS, 'AdvertiseLocalV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v6', REFERENCE_CLASS, 'AdvertiseLocalV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-orf', REFERENCE_ENUM_CLASS, 'BgpOrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpOrfEnum', 
                [], [], 
                '''                Advertise ORF capability to the peer
                ''',
                'advertise_orf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-permanent-network', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise Permanent Networks to the peer
                ''',
                'advertise_permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v4', REFERENCE_CLASS, 'AdvertiseV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v6', REFERENCE_CLASS, 'AdvertiseV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration for this address-family
                from an AF-group
                ''',
                'af_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable Accumulated IGP Metric for this neighbor.
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-cost-community', REFERENCE_CLASS, 'AigpCostCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity', 
                [], [], 
                '''                Send AIGP value in Cost Community. 
                ''',
                'aigp_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-send-med', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable/Disable sending AIGP in MED 
                ''',
                'aigp_send_med',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allow-as-in', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Allow as-path with my AS present in it
                ''',
                'allow_as_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to override matching AS-number while
                sending update. FALSE to prevent as-override
                from being inherited from the parent
                ''',
                'as_override',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-originate', REFERENCE_CLASS, 'DefaultOriginate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate', 
                [], [], 
                '''                Originate default route to this neighbor
                ''',
                'default_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set default weight for routes from this
                neighbor/neighbor-group/af-group
                ''',
                'default_weight',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'BgpAfEncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAfEncapsulationEnum', 
                [], [], 
                '''                Encapsulation type for this neighbor
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('flowspec-validation', REFERENCE_ENUM_CLASS, 'BgpFlowspecValidationCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpFlowspecValidationCfgEnum', 
                [], [], 
                '''                Config Flowspec validation for this neighbor
                ''',
                'flowspec_validation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import', REFERENCE_CLASS, 'Import_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.Import_', 
                [], [], 
                '''                Import Reorigination options for Routes from the
                peer
                ''',
                'import_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('maximum-prefixes', REFERENCE_CLASS, 'MaximumPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes', 
                [], [], 
                '''                Maximum number of prefixes to accept from this
                peer
                ''',
                'maximum_prefixes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multipath', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow paths from this neighbor to be eligible
                for selective multipath
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-capable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to treat neighbor as Long-lived
                Graceful-restart capable. FALSE to rely on
                capability negotiation.
                ''',
                'neighbor_af_long_lived_graceful_restart_capable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-stale-time', REFERENCE_CLASS, 'NeighborAfLongLivedGracefulRestartStaleTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime', 
                [], [], 
                '''                Maximum time to wait before purging long lived
                routes
                ''',
                'neighbor_af_long_lived_graceful_restart_stale_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-self', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable the next hop calculation and  insert
                your own address in the nexthop field of
                advertised routes you learned from the neighbor.
                ''',
                'next_hop_self',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop before
                advertising to eBGP peers. FALSE to prevent
                next-hop-unchanged from being inherited.
                ''',
                'next_hop_unchanged',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged-multipath', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop for
                multipaths. FALSE to prevent next-hop-unchanged
                for multipaths.
                ''',
                'next_hop_unchanged_multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-orf-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix ORF policy name for incoming updates
                ''',
                'prefix_orf_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath', 
                [], [], 
                '''                Remove private AS number from outbound updates
                ''',
                'remove_private_as_entire_as_path',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path-inbound', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPathInbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound', 
                [], [], 
                '''                Remove private AS number from inbound updates
                ''',
                'remove_private_as_entire_as_path_inbound',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to inbound routes
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to outbound routes
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a route-reflector-client. 
                FALSE to prevent route-reflector-client from
                being inherited.
                ''',
                'route_reflector_client',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp-graceful-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp_graceful_shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-ext-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send extended communities to the
                external neighbor/neighbor-group/af-group. 
                FALSE not to send and to prevent inheritance
                from a parent
                ''',
                'send_ext_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('site-of-origin', REFERENCE_CLASS, 'SiteOfOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin', 
                [], [], 
                '''                Site-of-Origin extended community associated
                with the neighbor
                ''',
                'site_of_origin',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-reconfiguration', REFERENCE_CLASS, 'SoftReconfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration', 
                [], [], 
                '''                Enable/disable inbound soft reconfiguration for
                this neighbor/neighbor-group/af-group
                ''',
                'soft_reconfiguration',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-neighbor-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs',
            False, 
            [
            _MetaInfoClassMember('vrf-neighbor-af', REFERENCE_LIST, 'VrfNeighborAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf', 
                [], [], 
                '''                Address family type of a VRF neighbor
                ''',
                'vrf_neighbor_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-neighbor-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('local-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a local
                address if the parent has one.FALSE to specify
                local ip address
                ''',
                'local_address_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Local ip address for neighbor
                ''',
                'local_ip_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates.BmpActivate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates.BmpActivate',
            False, 
            [
            _MetaInfoClassMember('server-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                BMP Server ID
                ''',
                'server_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates',
            False, 
            [
            _MetaInfoClassMember('bmp-activate', REFERENCE_LIST, 'BmpActivate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates.BmpActivate', 
                [], [], 
                '''                Enable BMP logging for this particular server
                ''',
                'bmp_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('max-hop-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum hop count
                ''',
                'max_hop_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-deactivation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to not enable MPLS and NULL rewrite.
                ''',
                'mpls_deactivation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp-multihop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Local AS and prevent it from being
                inherited from a parent
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dual-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dual-AS mode
                ''',
                'dual_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('no-prepend', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not prepend Local AS to announcements from
                this neighbor
                ''',
                'no_prepend',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('replace-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prepend only Local AS to announcements from
                this neighbor
                ''',
                'replace_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Password' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Password',
            False, 
            [
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password.  Leave unspecified when
                disabling the password.
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                password even if the parent has one.  FALSEto
                specify a password
                ''',
                'password_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.AdvertisementInterval' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.AdvertisementInterval',
            False, 
            [
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Minimum advertisement interval time, secs part
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('minimum-interval-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Minimum advertisement interval time, msecs part
                ''',
                'minimum_interval_msecs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertisement-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.NeighborClusterId' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.NeighborClusterId',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Route-Reflector Cluster ID in IPV4 address
                format
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Route-Reflector Cluster ID as 32 bit quantity
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-cluster-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tcpmss' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tcpmss',
            False, 
            [
            _MetaInfoClassMember('mss', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                Maximum Segment Size
                ''',
                'mss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance ofTCP MSS
                valuefrom its parents.FALSE, otherwise
                ''',
                'tcpmss_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tcpmss',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tos' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tos',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpTosEnum', 
                [], [], 
                '''                Set type of service
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TOS value to set
                ''',
                'value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'BgpPrecedenceDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpPrecedenceDscpEnum', 
                        [], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers',
            False, 
            [
            _MetaInfoClassMember('non-circular-buffer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure non-circular buffer
                ''',
                'non_circular_buffer',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('number-of-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                Number of message buffers
                ''',
                'number_of_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering-message-buffers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure inbound update filtering
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-attribute-filter-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Attribute-filter group name for update
                filtering
                ''',
                'update_in_filtering_attribute_filter_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-message-buffers', REFERENCE_CLASS, 'UpdateInFilteringMessageBuffers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers', 
                [], [], 
                '''                Message buffers to store filtered updates
                ''',
                'update_in_filtering_message_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-syslog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound update filtering syslog
                messages
                ''',
                'update_in_filtering_syslog_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogOut' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogOut',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Outbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                outbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.ReceiveBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.ReceiveBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogIn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogIn',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Inbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                inbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.SendBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.SendBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time.  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval
                ''',
                'keepalive_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time.  Specify 0 to
                disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Keychain' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Keychain',
            False, 
            [
            _MetaInfoClassMember('keychain-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                keychain based authentication even if the
                parent has one.FALSE to specify a keychain name
                ''',
                'keychain_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the keychain associated with neighbor
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference',
            False, 
            [
            _MetaInfoClassMember('gshut-loc-pref-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of Local Pref
                value from its parents.FALSE, otherwise
                ''',
                'gshut_loc_pref_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Preference Value
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-local-preference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends',
            False, 
            [
            _MetaInfoClassMember('as-prepends', ATTRIBUTE, 'int' , None, None, 
                [('0', '6')], [], 
                '''                number of times AS prepends
                ''',
                'as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('gshut-prepends-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of AS Prepends
                value from its parents.FALSE, otherwise
                ''',
                'gshut_prepends_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-as-prepends',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter Graceful Maintenance mode to configure
                parametrs
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-activate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initiate the graceful shutdown procedure
                ''',
                'graceful_maintenance_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-as-prepends', REFERENCE_CLASS, 'GracefulMaintenanceAsPrepends' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends', 
                [], [], 
                '''                Number of times to prepend local AS number to
                the AS path
                ''',
                'graceful_maintenance_as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-local-preference', REFERENCE_CLASS, 'GracefulMaintenanceLocalPreference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference', 
                [], [], 
                '''                Set Local Preference to advertise routes with
                ''',
                'graceful_maintenance_local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength',
            False, 
            [
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('additional-paths-receive-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertisement-interval', REFERENCE_CLASS, 'AdvertisementInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.AdvertisementInterval', 
                [], [], 
                '''                Minimum interval between sending BGP routing
                updates
                ''',
                'advertisement_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-enable-modes', REFERENCE_ENUM_CLASS, 'BgpBfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpBfdEnableModeEnum', 
                [], [], 
                '''                Strict mode, Default mode or Disable to prevent
                inheritance from a parent
                ''',
                'bfd_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'bfd_minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created by
                BGP
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bmp-activates', REFERENCE_CLASS, 'BmpActivates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates', 
                [], [], 
                '''                Enable BMP logging for this neighbor
                ''',
                'bmp_activates',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Up to 80 characters describing this neighbor
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.EbgpMultihop', 
                [], [], 
                '''                Allow EBGP neighbors not on directly connected
                networks
                ''',
                'ebgp_multihop',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-recv-dmz', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to receive DMZ link bandwidth from ebgp
                peer. FALSE to not receive from ebgp peer and to
                prevent inheritance from a parent
                ''',
                'ebgp_recv_dmz',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-send-dmz-enable-modes', REFERENCE_ENUM_CLASS, 'BgpEbgpSendDmzEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpEbgpSendDmzEnableModeEnum', 
                [], [], 
                '''                Default mode, Cumulative mode or Disable to
                prevent inheritance from a parent
                ''',
                'ebgp_send_dmz_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('egress-peer-engineering', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable egress peer engineering FALSE to
                disable egress peer engineering and to prevent
                inheritance from a parent
                ''',
                'egress_peer_engineering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enforce-first-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enforce first AS; FALSE to not enforce
                first AS.
                ''',
                'enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance', REFERENCE_CLASS, 'GracefulMaintenance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance', 
                [], [], 
                '''                Graceful Maintenance mode
                ''',
                'graceful_maintenance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('idle-watch-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '1800')], [], 
                '''                Time to wait for deleteing IDLE state Dynamic
                peer
                ''',
                'idle_watch_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ignore-connected-check-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable the connected nexthop check for
                this peer.FALSE to enable the connected nexthop
                check for this peer.
                ''',
                'ignore_connected_check_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-vpn-client-ibgpce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to preserve the CE path attributes.FALSE to
                override CE path attributes.
                ''',
                'internal_vpn_client_ibgpce',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain', REFERENCE_CLASS, 'Keychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Keychain', 
                [], [], 
                '''                Set or disable keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAddress', 
                [], [], 
                '''                Local ip address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-as', REFERENCE_CLASS, 'LocalAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAs', 
                [], [], 
                '''                Specify a local-as number
                ''',
                'local_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('max-peers', ATTRIBUTE, 'int' , None, None, 
                [('1', '4096')], [], 
                '''                Set Maximum Peers in Dynamic Range
                ''',
                'max_peers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-in', REFERENCE_CLASS, 'MsgLogIn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogIn', 
                [], [], 
                '''                Message log inbound
                ''',
                'msg_log_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-out', REFERENCE_CLASS, 'MsgLogOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogOut', 
                [], [], 
                '''                Message log outbound
                ''',
                'msg_log_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-cluster-id', REFERENCE_CLASS, 'NeighborClusterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.NeighborClusterId', 
                [], [], 
                '''                Neighbor Cluster-id
                ''',
                'neighbor_cluster_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Enable graceful restart support for
                neighbor.  FALSE to disable graceful restart
                support for neighbor.
                ''',
                'neighbor_graceful_restart',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-stalepath-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Maximum time to wait for restart of GR capable
                peer
                ''',
                'neighbor_graceful_restart_stalepath_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Restart time advertised to neighbor
                ''',
                'neighbor_graceful_restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration from a neighbor-group
                ''',
                'neighbor_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Password', 
                [], [], 
                '''                Set or disable a password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('propagate-dmz-link-bandwidth', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to propagate DMZ link bandwidth.  FALSE to
                not propagate and to prevent inheritance from a
                parent
                ''',
                'propagate_dmz_link_bandwidth',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-buffer-size', REFERENCE_CLASS, 'ReceiveBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.ReceiveBufferSize', 
                [], [], 
                '''                Set socket receive buffer size and BGP read
                buffer size
                ''',
                'receive_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.RemoteAs', 
                [], [], 
                '''                Set remote AS
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote-as-list group name
                ''',
                'remote_as_list',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-buffer-size', REFERENCE_CLASS, 'SendBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.SendBufferSize', 
                [], [], 
                '''                Set socket send buffer size and BGP write buffer
                size
                ''',
                'send_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit address-family independent config from a
                session-group
                ''',
                'session_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-open-mode', REFERENCE_ENUM_CLASS, 'BgpTcpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpTcpModeEnum', 
                [], [], 
                '''                TCP mode to be used to establish BGP session
                ''',
                'session_open_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to shutdown this entity, FALSE to prevent
                this entity from being shutdown even if the
                parent is.
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-all-capabilities', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress all capabilities. FALSE to not
                suppress and to prevent inheritance from a
                parent
                ''',
                'suppress_all_capabilities',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-four-byte-as-capability', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress BGP 4-byte-as capability. 
                FALSE to not suppress it and to prevent
                inheritance from a parent
                ''',
                'suppress_four_byte_as_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss', REFERENCE_CLASS, 'Tcpmss' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tcpmss', 
                [], [], 
                '''                TCP Maximum segment size
                ''',
                'tcpmss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Timers', 
                [], [], 
                '''                BGP per neighbor timers.
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tos', 
                [], [], 
                '''                TOS (Type Of Service)
                ''',
                'tos',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ttl-security', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BGP TTL Security.  FALSE to not
                enable it and to prevent inheritance from a
                parent
                ''',
                'ttl_security',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering', REFERENCE_CLASS, 'UpdateInFiltering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering', 
                [], [], 
                '''                Inbound update filtering
                ''',
                'update_in_filtering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Select an interface to configure
                ''',
                'update_source_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf-neighbor-afs', REFERENCE_CLASS, 'VrfNeighborAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs', 
                [], [], 
                '''                Address family type of a VRF neighbor
                ''',
                'vrf_neighbor_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-neighbor-prefix-length',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors',
            False, 
            [
            _MetaInfoClassMember('vrf-neighbor', REFERENCE_LIST, 'VrfNeighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor', 
                [], [], 
                '''                A particular VRF peer
                ''',
                'vrf_neighbor',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf-neighbor-prefix-length', REFERENCE_LIST, 'VrfNeighborPrefixLength' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength', 
                [], [], 
                '''                A particular VRF peer
                ''',
                'vrf_neighbor_prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('vrf-global', REFERENCE_CLASS, 'VrfGlobal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal', 
                [], [], 
                '''                VRF attribute config
                ''',
                'vrf_global',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf-neighbors', REFERENCE_CLASS, 'VrfNeighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors', 
                [], [], 
                '''                BGP VRF peer
                ''',
                'vrf_neighbors',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.Vrfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf', 
                [], [], 
                '''                VRF config
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AigpCostCommunity' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AigpCostCommunity',
            False, 
            [
            _MetaInfoClassMember('cost-community-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Cost Community ID
                ''',
                'cost_community_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cost-community-poi-type', REFERENCE_ENUM_CLASS, 'BgpAigpCfgPoiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgPoiEnum', 
                [], [], 
                '''                Cost Community POI
                ''',
                'cost_community_poi_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable sending cost community, FALSE
                otherwise 
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transitive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True to send transitive cost community FALSE
                otherwise
                ''',
                'transitive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aigp-cost-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDisable' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDisable',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-disable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.MaximumPrefixes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.MaximumPrefixes',
            False, 
            [
            _MetaInfoClassMember('discard-extra-paths', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discard extra paths when limit is exceeded
                ''',
                'discard_extra_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum prefixes limit
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Restart interval
                ''',
                'restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to only give a warning message when limit
                is exceeded.  FALSE to accept max prefix limit
                only.
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message.
                ''',
                'warning_percentage',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'maximum-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates.
                FALSE to prevent remove-private-AS from being
                inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path-inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime',
            False, 
            [
            _MetaInfoClassMember('stale-time-accept', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_accept',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('stale-time-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af-long-lived-graceful-restart-stale-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.Import_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.Import_',
            False, 
            [
            _MetaInfoClassMember('import-reoriginate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes, FALSE to
                not Reoriginate imported routes - not supported
                ''',
                'import_reoriginate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-reoriginate-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes with
                Stitching RTs, FALSE to Reoriginate imported
                routes with normal RTs
                ''',
                'import_reoriginate_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Import with Stitching RTs, FALSE to
                Import with normal RTs
                ''',
                'import_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.DefaultOriginate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.DefaultOriginate',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prevent default-originate from, being
                inherited from a parent. TRUE otherwise.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to specify criteria to
                originate default.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'default-originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.SoftReconfiguration' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.SoftReconfiguration',
            False, 
            [
            _MetaInfoClassMember('inbound-soft', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prohibit inbound soft reconfiguration.
                TRUE otherwise.
                ''',
                'inbound_soft',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to always use soft reconfig, even if route
                refresh is supported.  FALSE otherwise.
                ''',
                'soft_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'soft-reconfiguration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                .  FALSE to prevent remove-private-AS from
                being inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                BGP neighbor address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('accept-own', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Handle self-originated routes with Accept-Own
                community. Valid for following neighbor
                address-families: VPNv4Unicast, VPNv6Unicast.
                ''',
                'accept_own',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('accept-route-legacy-rt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a accept-route-legacy-RT. 
                FALSE to prevent accept-route-legacy-RT from
                being inherited.
                ''',
                'accept_route_legacy_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('activate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Activate an address family for this neighbor.
                Deletion of this object causes deletion of all
                the objects under
                NeighborAF/VRFNeighborAF/NeighborGroupAF
                associated with this object.
                ''',
                'activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseDefImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseDefImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-disable', REFERENCE_CLASS, 'AdvertiseDisable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDisable', 
                [], [], 
                '''                Disable Advertise Of Routes to the peer
                ''',
                'advertise_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseLocalL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label
                ''',
                'advertise_local_labeled_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v4', REFERENCE_CLASS, 'AdvertiseLocalV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV4', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v6', REFERENCE_CLASS, 'AdvertiseLocalV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV6', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-orf', REFERENCE_ENUM_CLASS, 'BgpOrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpOrfEnum', 
                [], [], 
                '''                Advertise ORF capability to the peer
                ''',
                'advertise_orf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-permanent-network', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise Permanent Networks to the peer
                ''',
                'advertise_permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v4', REFERENCE_CLASS, 'AdvertiseV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV4', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v6', REFERENCE_CLASS, 'AdvertiseV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV6', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration for this address-family
                from an AF-group
                ''',
                'af_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable Accumulated IGP Metric for this neighbor.
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-cost-community', REFERENCE_CLASS, 'AigpCostCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AigpCostCommunity', 
                [], [], 
                '''                Send AIGP value in Cost Community. 
                ''',
                'aigp_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-send-med', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable/Disable sending AIGP in MED 
                ''',
                'aigp_send_med',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allow-as-in', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Allow as-path with my AS present in it
                ''',
                'allow_as_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to override matching AS-number while
                sending update. FALSE to prevent as-override
                from being inherited from the parent
                ''',
                'as_override',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-originate', REFERENCE_CLASS, 'DefaultOriginate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.DefaultOriginate', 
                [], [], 
                '''                Originate default route to this neighbor
                ''',
                'default_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set default weight for routes from this
                neighbor/neighbor-group/af-group
                ''',
                'default_weight',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'BgpAfEncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAfEncapsulationEnum', 
                [], [], 
                '''                Encapsulation type for this neighbor
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('flowspec-validation', REFERENCE_ENUM_CLASS, 'BgpFlowspecValidationCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpFlowspecValidationCfgEnum', 
                [], [], 
                '''                Config Flowspec validation for this neighbor
                ''',
                'flowspec_validation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import', REFERENCE_CLASS, 'Import_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.Import_', 
                [], [], 
                '''                Import Reorigination options for Routes from the
                peer
                ''',
                'import_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('l2vpn-signalling', REFERENCE_ENUM_CLASS, 'BgpSignalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSignalEnum', 
                [], [], 
                '''                Disable signalling type on the peer
                ''',
                'l2vpn_signalling',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('maximum-prefixes', REFERENCE_CLASS, 'MaximumPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.MaximumPrefixes', 
                [], [], 
                '''                Maximum number of prefixes to accept from this
                peer
                ''',
                'maximum_prefixes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multipath', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow paths from this neighbor to be eligible
                for selective multipath
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-capable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to treat neighbor as Long-lived
                Graceful-restart capable. FALSE to rely on
                capability negotiation.
                ''',
                'neighbor_af_long_lived_graceful_restart_capable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-stale-time', REFERENCE_CLASS, 'NeighborAfLongLivedGracefulRestartStaleTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime', 
                [], [], 
                '''                Maximum time to wait before purging long lived
                routes
                ''',
                'neighbor_af_long_lived_graceful_restart_stale_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-self', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable the next hop calculation and  insert
                your own address in the nexthop field of
                advertised routes you learned from the neighbor.
                ''',
                'next_hop_self',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop before
                advertising to eBGP peers. FALSE to prevent
                next-hop-unchanged from being inherited.
                ''',
                'next_hop_unchanged',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged-multipath', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop for
                multipaths. FALSE to prevent next-hop-unchanged
                for multipaths.
                ''',
                'next_hop_unchanged_multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-orf-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix ORF policy name for incoming updates
                ''',
                'prefix_orf_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath', 
                [], [], 
                '''                Remove private AS number from outbound updates
                ''',
                'remove_private_as_entire_as_path',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path-inbound', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPathInbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound', 
                [], [], 
                '''                Remove private AS number from inbound updates
                ''',
                'remove_private_as_entire_as_path_inbound',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to inbound routes
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to outbound routes
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a route-reflector-client. 
                FALSE to prevent route-reflector-client from
                being inherited.
                ''',
                'route_reflector_client',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp-graceful-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp_graceful_shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-ext-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send extended communities to the
                external neighbor/neighbor-group/af-group. 
                FALSE not to send and to prevent inheritance
                from a parent
                ''',
                'send_ext_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-multicast-attr', REFERENCE_ENUM_CLASS, 'BgpSendMcastAttrCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSendMcastAttrCfgEnum', 
                [], [], 
                '''                Config send multicast attribute for this
                neighbor
                ''',
                'send_multicast_attr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-reconfiguration', REFERENCE_CLASS, 'SoftReconfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.SoftReconfiguration', 
                [], [], 
                '''                Enable/disable inbound soft reconfiguration for
                this neighbor/neighbor-group/af-group
                ''',
                'soft_reconfiguration',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs',
            False, 
            [
            _MetaInfoClassMember('neighbor-af', REFERENCE_LIST, 'NeighborAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf', 
                [], [], 
                '''                Address family type of neighbor
                ''',
                'neighbor_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('local-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a local
                address if the parent has one.FALSE to specify
                local ip address
                ''',
                'local_address_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Local ip address for neighbor
                ''',
                'local_ip_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates.BmpActivate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates.BmpActivate',
            False, 
            [
            _MetaInfoClassMember('server-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                BMP Server ID
                ''',
                'server_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates',
            False, 
            [
            _MetaInfoClassMember('bmp-activate', REFERENCE_LIST, 'BmpActivate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates.BmpActivate', 
                [], [], 
                '''                Enable BMP logging for this particular server
                ''',
                'bmp_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('max-hop-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum hop count
                ''',
                'max_hop_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-deactivation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to not enable MPLS and NULL rewrite.
                ''',
                'mpls_deactivation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp-multihop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Local AS and prevent it from being
                inherited from a parent
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dual-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dual-AS mode
                ''',
                'dual_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('no-prepend', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not prepend Local AS to announcements from
                this neighbor
                ''',
                'no_prepend',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('replace-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prepend only Local AS to announcements from
                this neighbor
                ''',
                'replace_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Password' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Password',
            False, 
            [
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password.  Leave unspecified when
                disabling the password.
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                password even if the parent has one.  FALSEto
                specify a password
                ''',
                'password_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.AdvertisementInterval' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.AdvertisementInterval',
            False, 
            [
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Minimum advertisement interval time, secs part
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('minimum-interval-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Minimum advertisement interval time, msecs part
                ''',
                'minimum_interval_msecs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertisement-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborClusterId' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborClusterId',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Route-Reflector Cluster ID in IPV4 address
                format
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Route-Reflector Cluster ID as 32 bit quantity
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-cluster-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tcpmss' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tcpmss',
            False, 
            [
            _MetaInfoClassMember('mss', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                Maximum Segment Size
                ''',
                'mss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance ofTCP MSS
                valuefrom its parents.FALSE, otherwise
                ''',
                'tcpmss_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tcpmss',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tos' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tos',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpTosEnum', 
                [], [], 
                '''                Set type of service
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TOS value to set
                ''',
                'value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'BgpPrecedenceDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpPrecedenceDscpEnum', 
                        [], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers',
            False, 
            [
            _MetaInfoClassMember('non-circular-buffer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure non-circular buffer
                ''',
                'non_circular_buffer',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('number-of-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                Number of message buffers
                ''',
                'number_of_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering-message-buffers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure inbound update filtering
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-attribute-filter-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Attribute-filter group name for update
                filtering
                ''',
                'update_in_filtering_attribute_filter_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-message-buffers', REFERENCE_CLASS, 'UpdateInFilteringMessageBuffers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers', 
                [], [], 
                '''                Message buffers to store filtered updates
                ''',
                'update_in_filtering_message_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-syslog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound update filtering syslog
                messages
                ''',
                'update_in_filtering_syslog_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogOut' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogOut',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Outbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                outbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.ReceiveBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.ReceiveBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogIn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogIn',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Inbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                inbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.SendBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.SendBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time.  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval
                ''',
                'keepalive_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time.  Specify 0 to
                disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Keychain' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Keychain',
            False, 
            [
            _MetaInfoClassMember('keychain-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                keychain based authentication even if the
                parent has one.FALSE to specify a keychain name
                ''',
                'keychain_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the keychain associated with neighbor
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference',
            False, 
            [
            _MetaInfoClassMember('gshut-loc-pref-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of Local Pref
                value from its parents.FALSE, otherwise
                ''',
                'gshut_loc_pref_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Preference Value
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-local-preference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends',
            False, 
            [
            _MetaInfoClassMember('as-prepends', ATTRIBUTE, 'int' , None, None, 
                [('0', '6')], [], 
                '''                number of times AS prepends
                ''',
                'as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('gshut-prepends-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of AS Prepends
                value from its parents.FALSE, otherwise
                ''',
                'gshut_prepends_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-as-prepends',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter Graceful Maintenance mode to configure
                parametrs
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-activate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initiate the graceful shutdown procedure
                ''',
                'graceful_maintenance_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-as-prepends', REFERENCE_CLASS, 'GracefulMaintenanceAsPrepends' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends', 
                [], [], 
                '''                Number of times to prepend local AS number to
                the AS path
                ''',
                'graceful_maintenance_as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-local-preference', REFERENCE_CLASS, 'GracefulMaintenanceLocalPreference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference', 
                [], [], 
                '''                Set Local Preference to advertise routes with
                ''',
                'graceful_maintenance_local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('additional-paths-receive-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertisement-interval', REFERENCE_CLASS, 'AdvertisementInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.AdvertisementInterval', 
                [], [], 
                '''                Minimum interval between sending BGP routing
                updates
                ''',
                'advertisement_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-enable-modes', REFERENCE_ENUM_CLASS, 'BgpBfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpBfdEnableModeEnum', 
                [], [], 
                '''                Strict mode, Default mode or Disable to prevent
                inheritance from a parent
                ''',
                'bfd_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'bfd_minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created by
                BGP
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bmp-activates', REFERENCE_CLASS, 'BmpActivates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates', 
                [], [], 
                '''                Enable BMP logging for this neighbor
                ''',
                'bmp_activates',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Up to 80 characters describing this neighbor
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.EbgpMultihop', 
                [], [], 
                '''                Allow EBGP neighbors not on directly connected
                networks
                ''',
                'ebgp_multihop',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-recv-dmz', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to receive DMZ link bandwidth from ebgp
                peer. FALSE to not receive from ebgp peer and to
                prevent inheritance from a parent
                ''',
                'ebgp_recv_dmz',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-send-dmz-enable-modes', REFERENCE_ENUM_CLASS, 'BgpEbgpSendDmzEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpEbgpSendDmzEnableModeEnum', 
                [], [], 
                '''                Default mode, Cumulative mode or Disable to
                prevent inheritance from a parent
                ''',
                'ebgp_send_dmz_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('egress-peer-engineering', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable egress peer engineering FALSE to
                disable egress peer engineering and to prevent
                inheritance from a parent
                ''',
                'egress_peer_engineering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enforce-first-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enforce first AS; FALSE to not enforce
                first AS.
                ''',
                'enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance', REFERENCE_CLASS, 'GracefulMaintenance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance', 
                [], [], 
                '''                Graceful Maintenance mode
                ''',
                'graceful_maintenance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('idle-watch-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '1800')], [], 
                '''                Time to wait for deleteing IDLE state Dynamic
                peer
                ''',
                'idle_watch_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ignore-connected-check-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable the connected nexthop check for
                this peer.FALSE to enable the connected nexthop
                check for this peer.
                ''',
                'ignore_connected_check_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-vpn-client-ibgpce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to preserve the CE path attributes.FALSE to
                override CE path attributes.
                ''',
                'internal_vpn_client_ibgpce',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain', REFERENCE_CLASS, 'Keychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Keychain', 
                [], [], 
                '''                Set or disable keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAddress', 
                [], [], 
                '''                Local ip address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-as', REFERENCE_CLASS, 'LocalAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAs', 
                [], [], 
                '''                Specify a local-as number
                ''',
                'local_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('max-peers', ATTRIBUTE, 'int' , None, None, 
                [('1', '4096')], [], 
                '''                Set Maximum Peers in Dynamic Range
                ''',
                'max_peers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-in', REFERENCE_CLASS, 'MsgLogIn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogIn', 
                [], [], 
                '''                Message log inbound
                ''',
                'msg_log_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-out', REFERENCE_CLASS, 'MsgLogOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogOut', 
                [], [], 
                '''                Message log outbound
                ''',
                'msg_log_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-afs', REFERENCE_CLASS, 'NeighborAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs', 
                [], [], 
                '''                BGP neighbor AF configuration table
                ''',
                'neighbor_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-cluster-id', REFERENCE_CLASS, 'NeighborClusterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborClusterId', 
                [], [], 
                '''                Neighbor Cluster-id
                ''',
                'neighbor_cluster_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Enable graceful restart support for
                neighbor.  FALSE to disable graceful restart
                support for neighbor.
                ''',
                'neighbor_graceful_restart',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-stalepath-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Maximum time to wait for restart of GR capable
                peer
                ''',
                'neighbor_graceful_restart_stalepath_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Restart time advertised to neighbor
                ''',
                'neighbor_graceful_restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration from a neighbor-group
                ''',
                'neighbor_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Password', 
                [], [], 
                '''                Set or disable a password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('propagate-dmz-link-bandwidth', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to propagate DMZ link bandwidth.  FALSE to
                not propagate and to prevent inheritance from a
                parent
                ''',
                'propagate_dmz_link_bandwidth',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-buffer-size', REFERENCE_CLASS, 'ReceiveBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.ReceiveBufferSize', 
                [], [], 
                '''                Set socket receive buffer size and BGP read
                buffer size
                ''',
                'receive_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.RemoteAs', 
                [], [], 
                '''                Set remote AS
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote-as-list group name
                ''',
                'remote_as_list',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-buffer-size', REFERENCE_CLASS, 'SendBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.SendBufferSize', 
                [], [], 
                '''                Set socket send buffer size and BGP write buffer
                size
                ''',
                'send_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit address-family independent config from a
                session-group
                ''',
                'session_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-open-mode', REFERENCE_ENUM_CLASS, 'BgpTcpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpTcpModeEnum', 
                [], [], 
                '''                TCP mode to be used to establish BGP session
                ''',
                'session_open_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to shutdown this entity, FALSE to prevent
                this entity from being shutdown even if the
                parent is.
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-all-capabilities', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress all capabilities. FALSE to not
                suppress and to prevent inheritance from a
                parent
                ''',
                'suppress_all_capabilities',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-four-byte-as-capability', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress BGP 4-byte-as capability. 
                FALSE to not suppress it and to prevent
                inheritance from a parent
                ''',
                'suppress_four_byte_as_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss', REFERENCE_CLASS, 'Tcpmss' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tcpmss', 
                [], [], 
                '''                TCP Maximum segment size
                ''',
                'tcpmss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Timers', 
                [], [], 
                '''                BGP per neighbor timers.
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tos', 
                [], [], 
                '''                TOS (Type Of Service)
                ''',
                'tos',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ttl-security', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BGP TTL Security.  FALSE to not
                enable it and to prevent inheritance from a
                parent
                ''',
                'ttl_security',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering', REFERENCE_CLASS, 'UpdateInFiltering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering', 
                [], [], 
                '''                Inbound update filtering
                ''',
                'update_in_filtering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Select an interface to configure
                ''',
                'update_source_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AigpCostCommunity' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AigpCostCommunity',
            False, 
            [
            _MetaInfoClassMember('cost-community-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Cost Community ID
                ''',
                'cost_community_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cost-community-poi-type', REFERENCE_ENUM_CLASS, 'BgpAigpCfgPoiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgPoiEnum', 
                [], [], 
                '''                Cost Community POI
                ''',
                'cost_community_poi_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable sending cost community, FALSE
                otherwise 
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transitive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True to send transitive cost community FALSE
                otherwise
                ''',
                'transitive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aigp-cost-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDisable' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDisable',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-disable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.MaximumPrefixes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.MaximumPrefixes',
            False, 
            [
            _MetaInfoClassMember('discard-extra-paths', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discard extra paths when limit is exceeded
                ''',
                'discard_extra_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum prefixes limit
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Restart interval
                ''',
                'restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to only give a warning message when limit
                is exceeded.  FALSE to accept max prefix limit
                only.
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message.
                ''',
                'warning_percentage',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'maximum-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates.
                FALSE to prevent remove-private-AS from being
                inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path-inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime',
            False, 
            [
            _MetaInfoClassMember('stale-time-accept', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_accept',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('stale-time-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af-long-lived-graceful-restart-stale-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.Import_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.Import_',
            False, 
            [
            _MetaInfoClassMember('import-reoriginate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes, FALSE to
                not Reoriginate imported routes - not supported
                ''',
                'import_reoriginate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-reoriginate-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes with
                Stitching RTs, FALSE to Reoriginate imported
                routes with normal RTs
                ''',
                'import_reoriginate_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Import with Stitching RTs, FALSE to
                Import with normal RTs
                ''',
                'import_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.DefaultOriginate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.DefaultOriginate',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prevent default-originate from, being
                inherited from a parent. TRUE otherwise.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to specify criteria to
                originate default.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'default-originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.SoftReconfiguration' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.SoftReconfiguration',
            False, 
            [
            _MetaInfoClassMember('inbound-soft', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prohibit inbound soft reconfiguration.
                TRUE otherwise.
                ''',
                'inbound_soft',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to always use soft reconfig, even if route
                refresh is supported.  FALSE otherwise.
                ''',
                'soft_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'soft-reconfiguration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                .  FALSE to prevent remove-private-AS from
                being inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                BGP neighbor address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('accept-own', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Handle self-originated routes with Accept-Own
                community. Valid for following neighbor
                address-families: VPNv4Unicast, VPNv6Unicast.
                ''',
                'accept_own',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('accept-route-legacy-rt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a accept-route-legacy-RT. 
                FALSE to prevent accept-route-legacy-RT from
                being inherited.
                ''',
                'accept_route_legacy_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('activate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Activate an address family for this neighbor.
                Deletion of this object causes deletion of all
                the objects under
                NeighborAF/VRFNeighborAF/NeighborGroupAF
                associated with this object.
                ''',
                'activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseDefImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseDefImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-disable', REFERENCE_CLASS, 'AdvertiseDisable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDisable', 
                [], [], 
                '''                Disable Advertise Of Routes to the peer
                ''',
                'advertise_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseLocalL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label
                ''',
                'advertise_local_labeled_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v4', REFERENCE_CLASS, 'AdvertiseLocalV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV4', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v6', REFERENCE_CLASS, 'AdvertiseLocalV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV6', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-orf', REFERENCE_ENUM_CLASS, 'BgpOrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpOrfEnum', 
                [], [], 
                '''                Advertise ORF capability to the peer
                ''',
                'advertise_orf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-permanent-network', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise Permanent Networks to the peer
                ''',
                'advertise_permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v4', REFERENCE_CLASS, 'AdvertiseV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV4', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v6', REFERENCE_CLASS, 'AdvertiseV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV6', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration for this address-family
                from an AF-group
                ''',
                'af_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable Accumulated IGP Metric for this neighbor.
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-cost-community', REFERENCE_CLASS, 'AigpCostCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AigpCostCommunity', 
                [], [], 
                '''                Send AIGP value in Cost Community. 
                ''',
                'aigp_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-send-med', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable/Disable sending AIGP in MED 
                ''',
                'aigp_send_med',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allow-as-in', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Allow as-path with my AS present in it
                ''',
                'allow_as_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to override matching AS-number while
                sending update. FALSE to prevent as-override
                from being inherited from the parent
                ''',
                'as_override',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-originate', REFERENCE_CLASS, 'DefaultOriginate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.DefaultOriginate', 
                [], [], 
                '''                Originate default route to this neighbor
                ''',
                'default_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set default weight for routes from this
                neighbor/neighbor-group/af-group
                ''',
                'default_weight',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'BgpAfEncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAfEncapsulationEnum', 
                [], [], 
                '''                Encapsulation type for this neighbor
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('flowspec-validation', REFERENCE_ENUM_CLASS, 'BgpFlowspecValidationCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpFlowspecValidationCfgEnum', 
                [], [], 
                '''                Config Flowspec validation for this neighbor
                ''',
                'flowspec_validation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import', REFERENCE_CLASS, 'Import_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.Import_', 
                [], [], 
                '''                Import Reorigination options for Routes from the
                peer
                ''',
                'import_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('l2vpn-signalling', REFERENCE_ENUM_CLASS, 'BgpSignalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSignalEnum', 
                [], [], 
                '''                Disable signalling type on the peer
                ''',
                'l2vpn_signalling',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('maximum-prefixes', REFERENCE_CLASS, 'MaximumPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.MaximumPrefixes', 
                [], [], 
                '''                Maximum number of prefixes to accept from this
                peer
                ''',
                'maximum_prefixes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multipath', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow paths from this neighbor to be eligible
                for selective multipath
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-capable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to treat neighbor as Long-lived
                Graceful-restart capable. FALSE to rely on
                capability negotiation.
                ''',
                'neighbor_af_long_lived_graceful_restart_capable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-stale-time', REFERENCE_CLASS, 'NeighborAfLongLivedGracefulRestartStaleTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime', 
                [], [], 
                '''                Maximum time to wait before purging long lived
                routes
                ''',
                'neighbor_af_long_lived_graceful_restart_stale_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-self', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable the next hop calculation and  insert
                your own address in the nexthop field of
                advertised routes you learned from the neighbor.
                ''',
                'next_hop_self',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop before
                advertising to eBGP peers. FALSE to prevent
                next-hop-unchanged from being inherited.
                ''',
                'next_hop_unchanged',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged-multipath', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop for
                multipaths. FALSE to prevent next-hop-unchanged
                for multipaths.
                ''',
                'next_hop_unchanged_multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-orf-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix ORF policy name for incoming updates
                ''',
                'prefix_orf_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath', 
                [], [], 
                '''                Remove private AS number from outbound updates
                ''',
                'remove_private_as_entire_as_path',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path-inbound', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPathInbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound', 
                [], [], 
                '''                Remove private AS number from inbound updates
                ''',
                'remove_private_as_entire_as_path_inbound',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to inbound routes
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to outbound routes
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a route-reflector-client. 
                FALSE to prevent route-reflector-client from
                being inherited.
                ''',
                'route_reflector_client',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp-graceful-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp_graceful_shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-ext-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send extended communities to the
                external neighbor/neighbor-group/af-group. 
                FALSE not to send and to prevent inheritance
                from a parent
                ''',
                'send_ext_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-multicast-attr', REFERENCE_ENUM_CLASS, 'BgpSendMcastAttrCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSendMcastAttrCfgEnum', 
                [], [], 
                '''                Config send multicast attribute for this
                neighbor
                ''',
                'send_multicast_attr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-reconfiguration', REFERENCE_CLASS, 'SoftReconfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.SoftReconfiguration', 
                [], [], 
                '''                Enable/disable inbound soft reconfiguration for
                this neighbor/neighbor-group/af-group
                ''',
                'soft_reconfiguration',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs',
            False, 
            [
            _MetaInfoClassMember('neighbor-af', REFERENCE_LIST, 'NeighborAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf', 
                [], [], 
                '''                Address family type of neighbor
                ''',
                'neighbor_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('local-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a local
                address if the parent has one.FALSE to specify
                local ip address
                ''',
                'local_address_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Local ip address for neighbor
                ''',
                'local_ip_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates.BmpActivate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates.BmpActivate',
            False, 
            [
            _MetaInfoClassMember('server-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                BMP Server ID
                ''',
                'server_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates',
            False, 
            [
            _MetaInfoClassMember('bmp-activate', REFERENCE_LIST, 'BmpActivate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates.BmpActivate', 
                [], [], 
                '''                Enable BMP logging for this particular server
                ''',
                'bmp_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('max-hop-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum hop count
                ''',
                'max_hop_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-deactivation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to not enable MPLS and NULL rewrite.
                ''',
                'mpls_deactivation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp-multihop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Local AS and prevent it from being
                inherited from a parent
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dual-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dual-AS mode
                ''',
                'dual_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('no-prepend', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not prepend Local AS to announcements from
                this neighbor
                ''',
                'no_prepend',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('replace-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prepend only Local AS to announcements from
                this neighbor
                ''',
                'replace_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Password' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Password',
            False, 
            [
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password.  Leave unspecified when
                disabling the password.
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                password even if the parent has one.  FALSEto
                specify a password
                ''',
                'password_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.AdvertisementInterval' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.AdvertisementInterval',
            False, 
            [
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Minimum advertisement interval time, secs part
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('minimum-interval-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Minimum advertisement interval time, msecs part
                ''',
                'minimum_interval_msecs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertisement-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborClusterId' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborClusterId',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Route-Reflector Cluster ID in IPV4 address
                format
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Route-Reflector Cluster ID as 32 bit quantity
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-cluster-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tcpmss' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tcpmss',
            False, 
            [
            _MetaInfoClassMember('mss', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                Maximum Segment Size
                ''',
                'mss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance ofTCP MSS
                valuefrom its parents.FALSE, otherwise
                ''',
                'tcpmss_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tcpmss',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tos' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tos',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpTosEnum', 
                [], [], 
                '''                Set type of service
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TOS value to set
                ''',
                'value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'BgpPrecedenceDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpPrecedenceDscpEnum', 
                        [], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers',
            False, 
            [
            _MetaInfoClassMember('non-circular-buffer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure non-circular buffer
                ''',
                'non_circular_buffer',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('number-of-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                Number of message buffers
                ''',
                'number_of_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering-message-buffers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure inbound update filtering
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-attribute-filter-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Attribute-filter group name for update
                filtering
                ''',
                'update_in_filtering_attribute_filter_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-message-buffers', REFERENCE_CLASS, 'UpdateInFilteringMessageBuffers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers', 
                [], [], 
                '''                Message buffers to store filtered updates
                ''',
                'update_in_filtering_message_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-syslog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound update filtering syslog
                messages
                ''',
                'update_in_filtering_syslog_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogOut' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogOut',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Outbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                outbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.ReceiveBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.ReceiveBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogIn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogIn',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Inbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                inbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.SendBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.SendBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time.  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval
                ''',
                'keepalive_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time.  Specify 0 to
                disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Keychain' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Keychain',
            False, 
            [
            _MetaInfoClassMember('keychain-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                keychain based authentication even if the
                parent has one.FALSE to specify a keychain name
                ''',
                'keychain_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the keychain associated with neighbor
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference',
            False, 
            [
            _MetaInfoClassMember('gshut-loc-pref-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of Local Pref
                value from its parents.FALSE, otherwise
                ''',
                'gshut_loc_pref_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Preference Value
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-local-preference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends',
            False, 
            [
            _MetaInfoClassMember('as-prepends', ATTRIBUTE, 'int' , None, None, 
                [('0', '6')], [], 
                '''                number of times AS prepends
                ''',
                'as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('gshut-prepends-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of AS Prepends
                value from its parents.FALSE, otherwise
                ''',
                'gshut_prepends_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-as-prepends',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter Graceful Maintenance mode to configure
                parametrs
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-activate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initiate the graceful shutdown procedure
                ''',
                'graceful_maintenance_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-as-prepends', REFERENCE_CLASS, 'GracefulMaintenanceAsPrepends' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends', 
                [], [], 
                '''                Number of times to prepend local AS number to
                the AS path
                ''',
                'graceful_maintenance_as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-local-preference', REFERENCE_CLASS, 'GracefulMaintenanceLocalPreference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference', 
                [], [], 
                '''                Set Local Preference to advertise routes with
                ''',
                'graceful_maintenance_local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength',
            False, 
            [
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address
                        ''',
                        'neighbor_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('additional-paths-receive-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertisement-interval', REFERENCE_CLASS, 'AdvertisementInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.AdvertisementInterval', 
                [], [], 
                '''                Minimum interval between sending BGP routing
                updates
                ''',
                'advertisement_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-enable-modes', REFERENCE_ENUM_CLASS, 'BgpBfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpBfdEnableModeEnum', 
                [], [], 
                '''                Strict mode, Default mode or Disable to prevent
                inheritance from a parent
                ''',
                'bfd_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'bfd_minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created by
                BGP
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bmp-activates', REFERENCE_CLASS, 'BmpActivates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates', 
                [], [], 
                '''                Enable BMP logging for this neighbor
                ''',
                'bmp_activates',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Up to 80 characters describing this neighbor
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.EbgpMultihop', 
                [], [], 
                '''                Allow EBGP neighbors not on directly connected
                networks
                ''',
                'ebgp_multihop',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-recv-dmz', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to receive DMZ link bandwidth from ebgp
                peer. FALSE to not receive from ebgp peer and to
                prevent inheritance from a parent
                ''',
                'ebgp_recv_dmz',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-send-dmz-enable-modes', REFERENCE_ENUM_CLASS, 'BgpEbgpSendDmzEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpEbgpSendDmzEnableModeEnum', 
                [], [], 
                '''                Default mode, Cumulative mode or Disable to
                prevent inheritance from a parent
                ''',
                'ebgp_send_dmz_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('egress-peer-engineering', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable egress peer engineering FALSE to
                disable egress peer engineering and to prevent
                inheritance from a parent
                ''',
                'egress_peer_engineering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enforce-first-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enforce first AS; FALSE to not enforce
                first AS.
                ''',
                'enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance', REFERENCE_CLASS, 'GracefulMaintenance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance', 
                [], [], 
                '''                Graceful Maintenance mode
                ''',
                'graceful_maintenance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('idle-watch-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '1800')], [], 
                '''                Time to wait for deleteing IDLE state Dynamic
                peer
                ''',
                'idle_watch_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ignore-connected-check-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable the connected nexthop check for
                this peer.FALSE to enable the connected nexthop
                check for this peer.
                ''',
                'ignore_connected_check_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-vpn-client-ibgpce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to preserve the CE path attributes.FALSE to
                override CE path attributes.
                ''',
                'internal_vpn_client_ibgpce',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain', REFERENCE_CLASS, 'Keychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Keychain', 
                [], [], 
                '''                Set or disable keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAddress', 
                [], [], 
                '''                Local ip address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-as', REFERENCE_CLASS, 'LocalAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAs', 
                [], [], 
                '''                Specify a local-as number
                ''',
                'local_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('max-peers', ATTRIBUTE, 'int' , None, None, 
                [('1', '4096')], [], 
                '''                Set Maximum Peers in Dynamic Range
                ''',
                'max_peers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-in', REFERENCE_CLASS, 'MsgLogIn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogIn', 
                [], [], 
                '''                Message log inbound
                ''',
                'msg_log_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-out', REFERENCE_CLASS, 'MsgLogOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogOut', 
                [], [], 
                '''                Message log outbound
                ''',
                'msg_log_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-afs', REFERENCE_CLASS, 'NeighborAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs', 
                [], [], 
                '''                BGP neighbor AF configuration table
                ''',
                'neighbor_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-cluster-id', REFERENCE_CLASS, 'NeighborClusterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborClusterId', 
                [], [], 
                '''                Neighbor Cluster-id
                ''',
                'neighbor_cluster_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Enable graceful restart support for
                neighbor.  FALSE to disable graceful restart
                support for neighbor.
                ''',
                'neighbor_graceful_restart',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-stalepath-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Maximum time to wait for restart of GR capable
                peer
                ''',
                'neighbor_graceful_restart_stalepath_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Restart time advertised to neighbor
                ''',
                'neighbor_graceful_restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration from a neighbor-group
                ''',
                'neighbor_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Password', 
                [], [], 
                '''                Set or disable a password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('propagate-dmz-link-bandwidth', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to propagate DMZ link bandwidth.  FALSE to
                not propagate and to prevent inheritance from a
                parent
                ''',
                'propagate_dmz_link_bandwidth',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-buffer-size', REFERENCE_CLASS, 'ReceiveBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.ReceiveBufferSize', 
                [], [], 
                '''                Set socket receive buffer size and BGP read
                buffer size
                ''',
                'receive_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.RemoteAs', 
                [], [], 
                '''                Set remote AS
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote-as-list group name
                ''',
                'remote_as_list',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-buffer-size', REFERENCE_CLASS, 'SendBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.SendBufferSize', 
                [], [], 
                '''                Set socket send buffer size and BGP write buffer
                size
                ''',
                'send_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit address-family independent config from a
                session-group
                ''',
                'session_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-open-mode', REFERENCE_ENUM_CLASS, 'BgpTcpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpTcpModeEnum', 
                [], [], 
                '''                TCP mode to be used to establish BGP session
                ''',
                'session_open_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to shutdown this entity, FALSE to prevent
                this entity from being shutdown even if the
                parent is.
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-all-capabilities', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress all capabilities. FALSE to not
                suppress and to prevent inheritance from a
                parent
                ''',
                'suppress_all_capabilities',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-four-byte-as-capability', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress BGP 4-byte-as capability. 
                FALSE to not suppress it and to prevent
                inheritance from a parent
                ''',
                'suppress_four_byte_as_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss', REFERENCE_CLASS, 'Tcpmss' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tcpmss', 
                [], [], 
                '''                TCP Maximum segment size
                ''',
                'tcpmss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Timers', 
                [], [], 
                '''                BGP per neighbor timers.
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tos', 
                [], [], 
                '''                TOS (Type Of Service)
                ''',
                'tos',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ttl-security', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BGP TTL Security.  FALSE to not
                enable it and to prevent inheritance from a
                parent
                ''',
                'ttl_security',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering', REFERENCE_CLASS, 'UpdateInFiltering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering', 
                [], [], 
                '''                Inbound update filtering
                ''',
                'update_in_filtering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Select an interface to configure
                ''',
                'update_source_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-prefix-length',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor', 
                [], [], 
                '''                A particular BGP peer
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-prefix-length', REFERENCE_LIST, 'NeighborPrefixLength' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength', 
                [], [], 
                '''                A particular BGP peer
                ''',
                'neighbor_prefix_length',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AigpCostCommunity' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AigpCostCommunity',
            False, 
            [
            _MetaInfoClassMember('cost-community-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Cost Community ID
                ''',
                'cost_community_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cost-community-poi-type', REFERENCE_ENUM_CLASS, 'BgpAigpCfgPoiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgPoiEnum', 
                [], [], 
                '''                Cost Community POI
                ''',
                'cost_community_poi_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable sending cost community, FALSE
                otherwise 
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transitive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True to send transitive cost community FALSE
                otherwise
                ''',
                'transitive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aigp-cost-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDisable' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDisable',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-disable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.MaximumPrefixes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.MaximumPrefixes',
            False, 
            [
            _MetaInfoClassMember('discard-extra-paths', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discard extra paths when limit is exceeded
                ''',
                'discard_extra_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum prefixes limit
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Restart interval
                ''',
                'restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to only give a warning message when limit
                is exceeded.  FALSE to accept max prefix limit
                only.
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message.
                ''',
                'warning_percentage',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'maximum-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPathInbound' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPathInbound',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates.
                FALSE to prevent remove-private-AS from being
                inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path-inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.NeighborAfLongLivedGracefulRestartStaleTime' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.NeighborAfLongLivedGracefulRestartStaleTime',
            False, 
            [
            _MetaInfoClassMember('stale-time-accept', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_accept',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('stale-time-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af-long-lived-graceful-restart-stale-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SiteOfOrigin' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SiteOfOrigin',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                IP address Index
                ''',
                'address_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpSiteOfOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSiteOfOriginEnum', 
                [], [], 
                '''                Type of Extended community
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'site-of-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.Import_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.Import_',
            False, 
            [
            _MetaInfoClassMember('import-reoriginate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes, FALSE to
                not Reoriginate imported routes - not supported
                ''',
                'import_reoriginate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-reoriginate-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes with
                Stitching RTs, FALSE to Reoriginate imported
                routes with normal RTs
                ''',
                'import_reoriginate_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Import with Stitching RTs, FALSE to
                Import with normal RTs
                ''',
                'import_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.DefaultOriginate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.DefaultOriginate',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prevent default-originate from, being
                inherited from a parent. TRUE otherwise.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to specify criteria to
                originate default.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'default-originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SoftReconfiguration' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SoftReconfiguration',
            False, 
            [
            _MetaInfoClassMember('inbound-soft', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prohibit inbound soft reconfiguration.
                TRUE otherwise.
                ''',
                'inbound_soft',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to always use soft reconfig, even if route
                refresh is supported.  FALSE otherwise.
                ''',
                'soft_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'soft-reconfiguration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPath' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPath',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                .  FALSE to prevent remove-private-AS from
                being inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                BGP neighbor group address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('accept-own', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Handle self-originated routes with Accept-Own
                community. Valid for following neighbor
                address-families: VPNv4Unicast, VPNv6Unicast.
                ''',
                'accept_own',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('accept-route-legacy-rt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a accept-route-legacy-RT. 
                FALSE to prevent accept-route-legacy-RT from
                being inherited.
                ''',
                'accept_route_legacy_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('activate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Activate an address family for this neighbor.
                Deletion of this object causes deletion of all
                the objects under
                NeighborAF/VRFNeighborAF/NeighborGroupAF
                associated with this object.
                ''',
                'activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseDefImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseDefImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-disable', REFERENCE_CLASS, 'AdvertiseDisable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDisable', 
                [], [], 
                '''                Disable Advertise Of Routes to the peer
                ''',
                'advertise_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseL2Vpnevpn', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseLocalL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalL2Vpnevpn', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label
                ''',
                'advertise_local_labeled_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v4', REFERENCE_CLASS, 'AdvertiseLocalV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV4', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v6', REFERENCE_CLASS, 'AdvertiseLocalV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV6', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-orf', REFERENCE_ENUM_CLASS, 'BgpOrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpOrfEnum', 
                [], [], 
                '''                Advertise ORF capability to the peer
                ''',
                'advertise_orf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-permanent-network', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise Permanent Networks to the peer
                ''',
                'advertise_permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v4', REFERENCE_CLASS, 'AdvertiseV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV4', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v6', REFERENCE_CLASS, 'AdvertiseV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV6', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration for this address-family
                from an AF-group
                ''',
                'af_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable Accumulated IGP Metric for this neighbor.
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-cost-community', REFERENCE_CLASS, 'AigpCostCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AigpCostCommunity', 
                [], [], 
                '''                Send AIGP value in Cost Community. 
                ''',
                'aigp_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-send-med', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable/Disable sending AIGP in MED 
                ''',
                'aigp_send_med',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allow-as-in', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Allow as-path with my AS present in it
                ''',
                'allow_as_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to override matching AS-number while
                sending update. FALSE to prevent as-override
                from being inherited from the parent
                ''',
                'as_override',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-originate', REFERENCE_CLASS, 'DefaultOriginate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.DefaultOriginate', 
                [], [], 
                '''                Originate default route to this neighbor
                ''',
                'default_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set default weight for routes from this
                neighbor/neighbor-group/af-group
                ''',
                'default_weight',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'BgpAfEncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAfEncapsulationEnum', 
                [], [], 
                '''                Encapsulation type for this neighbor
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('flowspec-validation', REFERENCE_ENUM_CLASS, 'BgpFlowspecValidationCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpFlowspecValidationCfgEnum', 
                [], [], 
                '''                Config Flowspec validation for this neighbor
                ''',
                'flowspec_validation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import', REFERENCE_CLASS, 'Import_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.Import_', 
                [], [], 
                '''                Import Reorigination options for Routes from the
                peer
                ''',
                'import_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('l2vpn-signalling', REFERENCE_ENUM_CLASS, 'BgpSignalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSignalEnum', 
                [], [], 
                '''                Disable signalling type on the peer
                ''',
                'l2vpn_signalling',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('maximum-prefixes', REFERENCE_CLASS, 'MaximumPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.MaximumPrefixes', 
                [], [], 
                '''                Maximum number of prefixes to accept from this
                peer
                ''',
                'maximum_prefixes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multipath', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow paths from this neighbor to be eligible
                for selective multipath
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-capable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to treat neighbor as Long-lived
                Graceful-restart capable. FALSE to rely on
                capability negotiation.
                ''',
                'neighbor_af_long_lived_graceful_restart_capable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-stale-time', REFERENCE_CLASS, 'NeighborAfLongLivedGracefulRestartStaleTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.NeighborAfLongLivedGracefulRestartStaleTime', 
                [], [], 
                '''                Maximum time to wait before purging long lived
                routes
                ''',
                'neighbor_af_long_lived_graceful_restart_stale_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-self', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable the next hop calculation and  insert
                your own address in the nexthop field of
                advertised routes you learned from the neighbor.
                ''',
                'next_hop_self',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop before
                advertising to eBGP peers. FALSE to prevent
                next-hop-unchanged from being inherited.
                ''',
                'next_hop_unchanged',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged-multipath', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop for
                multipaths. FALSE to prevent next-hop-unchanged
                for multipaths.
                ''',
                'next_hop_unchanged_multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-orf-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix ORF policy name for incoming updates
                ''',
                'prefix_orf_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPath', 
                [], [], 
                '''                Remove private AS number from outbound updates
                ''',
                'remove_private_as_entire_as_path',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path-inbound', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPathInbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPathInbound', 
                [], [], 
                '''                Remove private AS number from inbound updates
                ''',
                'remove_private_as_entire_as_path_inbound',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to inbound routes
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to outbound routes
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a route-reflector-client. 
                FALSE to prevent route-reflector-client from
                being inherited.
                ''',
                'route_reflector_client',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp-graceful-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp_graceful_shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-ext-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send extended communities to the
                external neighbor/neighbor-group/af-group. 
                FALSE not to send and to prevent inheritance
                from a parent
                ''',
                'send_ext_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-multicast-attr', REFERENCE_ENUM_CLASS, 'BgpSendMcastAttrCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSendMcastAttrCfgEnum', 
                [], [], 
                '''                Config send multicast attribute for this
                neighbor
                ''',
                'send_multicast_attr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('site-of-origin', REFERENCE_CLASS, 'SiteOfOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SiteOfOrigin', 
                [], [], 
                '''                Site-of-Origin extended community associated
                with the neighbor
                ''',
                'site_of_origin',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-reconfiguration', REFERENCE_CLASS, 'SoftReconfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SoftReconfiguration', 
                [], [], 
                '''                Enable/disable inbound soft reconfiguration for
                this neighbor/neighbor-group/af-group
                ''',
                'soft_reconfiguration',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-group-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs',
            False, 
            [
            _MetaInfoClassMember('neighbor-group-af', REFERENCE_LIST, 'NeighborGroupAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf', 
                [], [], 
                '''                Address family type of neighbor group
                ''',
                'neighbor_group_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-group-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('local-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a local
                address if the parent has one.FALSE to specify
                local ip address
                ''',
                'local_address_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Local ip address for neighbor
                ''',
                'local_ip_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates.BmpActivate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates.BmpActivate',
            False, 
            [
            _MetaInfoClassMember('server-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                BMP Server ID
                ''',
                'server_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates',
            False, 
            [
            _MetaInfoClassMember('bmp-activate', REFERENCE_LIST, 'BmpActivate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates.BmpActivate', 
                [], [], 
                '''                Enable BMP logging for this particular server
                ''',
                'bmp_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('max-hop-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum hop count
                ''',
                'max_hop_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-deactivation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to not enable MPLS and NULL rewrite.
                ''',
                'mpls_deactivation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp-multihop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Local AS and prevent it from being
                inherited from a parent
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dual-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dual-AS mode
                ''',
                'dual_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('no-prepend', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not prepend Local AS to announcements from
                this neighbor
                ''',
                'no_prepend',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('replace-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prepend only Local AS to announcements from
                this neighbor
                ''',
                'replace_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Password' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Password',
            False, 
            [
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password.  Leave unspecified when
                disabling the password.
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                password even if the parent has one.  FALSEto
                specify a password
                ''',
                'password_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.AdvertisementInterval' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.AdvertisementInterval',
            False, 
            [
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Minimum advertisement interval time, secs part
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('minimum-interval-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Minimum advertisement interval time, msecs part
                ''',
                'minimum_interval_msecs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertisement-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborClusterId' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborClusterId',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Route-Reflector Cluster ID in IPV4 address
                format
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Route-Reflector Cluster ID as 32 bit quantity
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-cluster-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tcpmss' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tcpmss',
            False, 
            [
            _MetaInfoClassMember('mss', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                Maximum Segment Size
                ''',
                'mss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance ofTCP MSS
                valuefrom its parents.FALSE, otherwise
                ''',
                'tcpmss_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tcpmss',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tos' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tos',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpTosEnum', 
                [], [], 
                '''                Set type of service
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TOS value to set
                ''',
                'value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'BgpPrecedenceDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpPrecedenceDscpEnum', 
                        [], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers',
            False, 
            [
            _MetaInfoClassMember('non-circular-buffer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure non-circular buffer
                ''',
                'non_circular_buffer',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('number-of-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                Number of message buffers
                ''',
                'number_of_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering-message-buffers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure inbound update filtering
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-attribute-filter-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Attribute-filter group name for update
                filtering
                ''',
                'update_in_filtering_attribute_filter_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-message-buffers', REFERENCE_CLASS, 'UpdateInFilteringMessageBuffers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers', 
                [], [], 
                '''                Message buffers to store filtered updates
                ''',
                'update_in_filtering_message_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-syslog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound update filtering syslog
                messages
                ''',
                'update_in_filtering_syslog_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogOut' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogOut',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Outbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                outbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.ReceiveBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.ReceiveBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogIn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogIn',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Inbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                inbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.SendBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.SendBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time.  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval
                ''',
                'keepalive_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time.  Specify 0 to
                disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Keychain' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Keychain',
            False, 
            [
            _MetaInfoClassMember('keychain-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                keychain based authentication even if the
                parent has one.FALSE to specify a keychain name
                ''',
                'keychain_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the keychain associated with neighbor
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference',
            False, 
            [
            _MetaInfoClassMember('gshut-loc-pref-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of Local Pref
                value from its parents.FALSE, otherwise
                ''',
                'gshut_loc_pref_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Preference Value
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-local-preference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends',
            False, 
            [
            _MetaInfoClassMember('as-prepends', ATTRIBUTE, 'int' , None, None, 
                [('0', '6')], [], 
                '''                number of times AS prepends
                ''',
                'as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('gshut-prepends-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of AS Prepends
                value from its parents.FALSE, otherwise
                ''',
                'gshut_prepends_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-as-prepends',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter Graceful Maintenance mode to configure
                parametrs
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-activate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initiate the graceful shutdown procedure
                ''',
                'graceful_maintenance_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-as-prepends', REFERENCE_CLASS, 'GracefulMaintenanceAsPrepends' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends', 
                [], [], 
                '''                Number of times to prepend local AS number to
                the AS path
                ''',
                'graceful_maintenance_as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-local-preference', REFERENCE_CLASS, 'GracefulMaintenanceLocalPreference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference', 
                [], [], 
                '''                Set Local Preference to advertise routes with
                ''',
                'graceful_maintenance_local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup',
            False, 
            [
            _MetaInfoClassMember('neighbor-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                BGP neighbor group name
                ''',
                'neighbor_group_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('additional-paths-receive-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertisement-interval', REFERENCE_CLASS, 'AdvertisementInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.AdvertisementInterval', 
                [], [], 
                '''                Minimum interval between sending BGP routing
                updates
                ''',
                'advertisement_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-enable-modes', REFERENCE_ENUM_CLASS, 'BgpBfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpBfdEnableModeEnum', 
                [], [], 
                '''                Strict mode, Default mode or Disable to prevent
                inheritance from a parent
                ''',
                'bfd_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'bfd_minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created by
                BGP
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bmp-activates', REFERENCE_CLASS, 'BmpActivates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates', 
                [], [], 
                '''                Enable BMP logging for this neighbor
                ''',
                'bmp_activates',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create this group. Deletion of this object
                causes deletion of all the objects under
                NeighborGroup/SessionGroup associated with this
                object.
                ''',
                'create',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Up to 80 characters describing this neighbor
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.EbgpMultihop', 
                [], [], 
                '''                Allow EBGP neighbors not on directly connected
                networks
                ''',
                'ebgp_multihop',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-recv-dmz', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to receive DMZ link bandwidth from ebgp
                peer. FALSE to not receive from ebgp peer and to
                prevent inheritance from a parent
                ''',
                'ebgp_recv_dmz',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-send-dmz-enable-modes', REFERENCE_ENUM_CLASS, 'BgpEbgpSendDmzEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpEbgpSendDmzEnableModeEnum', 
                [], [], 
                '''                Default mode, Cumulative mode or Disable to
                prevent inheritance from a parent
                ''',
                'ebgp_send_dmz_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('egress-peer-engineering', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable egress peer engineering FALSE to
                disable egress peer engineering and to prevent
                inheritance from a parent
                ''',
                'egress_peer_engineering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enforce-first-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enforce first AS; FALSE to not enforce
                first AS.
                ''',
                'enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance', REFERENCE_CLASS, 'GracefulMaintenance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance', 
                [], [], 
                '''                Graceful Maintenance mode
                ''',
                'graceful_maintenance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('idle-watch-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '1800')], [], 
                '''                Time to wait for deleteing IDLE state Dynamic
                peer
                ''',
                'idle_watch_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ignore-connected-check-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable the connected nexthop check for
                this peer.FALSE to enable the connected nexthop
                check for this peer.
                ''',
                'ignore_connected_check_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-vpn-client-ibgpce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to preserve the CE path attributes.FALSE to
                override CE path attributes.
                ''',
                'internal_vpn_client_ibgpce',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain', REFERENCE_CLASS, 'Keychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Keychain', 
                [], [], 
                '''                Set or disable keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAddress', 
                [], [], 
                '''                Local ip address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-as', REFERENCE_CLASS, 'LocalAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAs', 
                [], [], 
                '''                Specify a local-as number
                ''',
                'local_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('max-peers', ATTRIBUTE, 'int' , None, None, 
                [('1', '4096')], [], 
                '''                Set Maximum Peers in Dynamic Range
                ''',
                'max_peers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-in', REFERENCE_CLASS, 'MsgLogIn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogIn', 
                [], [], 
                '''                Message log inbound
                ''',
                'msg_log_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-out', REFERENCE_CLASS, 'MsgLogOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogOut', 
                [], [], 
                '''                Message log outbound
                ''',
                'msg_log_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-cluster-id', REFERENCE_CLASS, 'NeighborClusterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborClusterId', 
                [], [], 
                '''                Neighbor Cluster-id
                ''',
                'neighbor_cluster_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Enable graceful restart support for
                neighbor.  FALSE to disable graceful restart
                support for neighbor.
                ''',
                'neighbor_graceful_restart',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-stalepath-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Maximum time to wait for restart of GR capable
                peer
                ''',
                'neighbor_graceful_restart_stalepath_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Restart time advertised to neighbor
                ''',
                'neighbor_graceful_restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration from a
                neighbor-group
                ''',
                'neighbor_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-group-afs', REFERENCE_CLASS, 'NeighborGroupAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs', 
                [], [], 
                '''                BGP neighbor-group AF configuration table
                ''',
                'neighbor_group_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Password', 
                [], [], 
                '''                Set or disable a password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('propagate-dmz-link-bandwidth', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to propagate DMZ link bandwidth.  FALSE to
                not propagate and to prevent inheritance from a
                parent
                ''',
                'propagate_dmz_link_bandwidth',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-buffer-size', REFERENCE_CLASS, 'ReceiveBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.ReceiveBufferSize', 
                [], [], 
                '''                Set socket receive buffer size and BGP read
                buffer size
                ''',
                'receive_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.RemoteAs', 
                [], [], 
                '''                Set remote AS
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote-as-list group name
                ''',
                'remote_as_list',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-buffer-size', REFERENCE_CLASS, 'SendBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.SendBufferSize', 
                [], [], 
                '''                Set socket send buffer size and BGP write buffer
                size
                ''',
                'send_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit address-family independent config from a
                session-group
                ''',
                'session_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-open-mode', REFERENCE_ENUM_CLASS, 'BgpTcpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpTcpModeEnum', 
                [], [], 
                '''                TCP mode to be used to establish BGP session
                ''',
                'session_open_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to shutdown this entity, FALSE to prevent
                this entity from being shutdown even if the
                parent is.
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-all-capabilities', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress all capabilities. FALSE to not
                suppress and to prevent inheritance from a
                parent
                ''',
                'suppress_all_capabilities',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-four-byte-as-capability', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress BGP 4-byte-as capability. 
                FALSE to not suppress it and to prevent
                inheritance from a parent
                ''',
                'suppress_four_byte_as_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss', REFERENCE_CLASS, 'Tcpmss' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tcpmss', 
                [], [], 
                '''                TCP Maximum segment size
                ''',
                'tcpmss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Timers', 
                [], [], 
                '''                BGP per neighbor timers.
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tos', 
                [], [], 
                '''                TOS (Type Of Service)
                ''',
                'tos',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ttl-security', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BGP TTL Security.  FALSE to not
                enable it and to prevent inheritance from a
                parent
                ''',
                'ttl_security',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering', REFERENCE_CLASS, 'UpdateInFiltering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering', 
                [], [], 
                '''                Inbound update filtering
                ''',
                'update_in_filtering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Select an interface to configure
                ''',
                'update_source_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups',
            False, 
            [
            _MetaInfoClassMember('neighbor-group', REFERENCE_LIST, 'NeighborGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup', 
                [], [], 
                '''                A particular BGP neighbor group
                ''',
                'neighbor_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AigpCostCommunity' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AigpCostCommunity',
            False, 
            [
            _MetaInfoClassMember('cost-community-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Cost Community ID
                ''',
                'cost_community_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cost-community-poi-type', REFERENCE_ENUM_CLASS, 'BgpAigpCfgPoiEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgPoiEnum', 
                [], [], 
                '''                Cost Community POI
                ''',
                'cost_community_poi_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable sending cost community, FALSE
                otherwise 
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transitive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True to send transitive cost community FALSE
                otherwise
                ''',
                'transitive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aigp-cost-community',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDisable' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDisable',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-disable',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.MaximumPrefixes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.MaximumPrefixes',
            False, 
            [
            _MetaInfoClassMember('discard-extra-paths', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Discard extra paths when limit is exceeded
                ''',
                'discard_extra_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-limit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum prefixes limit
                ''',
                'prefix_limit',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Restart interval
                ''',
                'restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to only give a warning message when limit
                is exceeded.  FALSE to accept max prefix limit
                only.
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('warning-percentage', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message.
                ''',
                'warning_percentage',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'maximum-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPathInbound' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPathInbound',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates.
                FALSE to prevent remove-private-AS from being
                inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from inbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path-inbound',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-def-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalL2Vpnevpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalL2Vpnevpn',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-l2vpnevpn',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.NeighborAfLongLivedGracefulRestartStaleTime' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.NeighborAfLongLivedGracefulRestartStaleTime',
            False, 
            [
            _MetaInfoClassMember('stale-time-accept', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_accept',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('stale-time-send', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Max time (seconds)
                ''',
                'stale_time_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-af-long-lived-graceful-restart-stale-time',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SiteOfOrigin' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SiteOfOrigin',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('address-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                IP address Index
                ''',
                'address_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number Index
                ''',
                'as_index',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpSiteOfOriginEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSiteOfOriginEnum', 
                [], [], 
                '''                Type of Extended community
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'site-of-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV6',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.Import_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.Import_',
            False, 
            [
            _MetaInfoClassMember('import-reoriginate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes, FALSE to
                not Reoriginate imported routes - not supported
                ''',
                'import_reoriginate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-reoriginate-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Reoriginate imported routes with
                Stitching RTs, FALSE to Reoriginate imported
                routes with normal RTs
                ''',
                'import_reoriginate_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-stitching', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Import with Stitching RTs, FALSE to
                Import with normal RTs
                ''',
                'import_stitching',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.DefaultOriginate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.DefaultOriginate',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prevent default-originate from, being
                inherited from a parent. TRUE otherwise.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to specify criteria to
                originate default.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'default-originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SoftReconfiguration' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SoftReconfiguration',
            False, 
            [
            _MetaInfoClassMember('inbound-soft', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                FALSE to prohibit inbound soft reconfiguration.
                TRUE otherwise.
                ''',
                'inbound_soft',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to always use soft reconfig, even if route
                refresh is supported.  FALSE otherwise.
                ''',
                'soft_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'soft-reconfiguration',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV6' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV6',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v6',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV4',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reorg-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Reorigination option
                ''',
                'reorg_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-local-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPath' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPath',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                .  FALSE to prevent remove-private-AS from
                being inherited.
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('entire', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to remove private AS from outbound updates
                if all ASes in aspath areprivate. FALSE to
                prevent remove-private-ASfrom being inherited.
                ''',
                'entire',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remove-private-as-entire-as-path',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV4' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV4',
            False, 
            [
            _MetaInfoClassMember('adv-option', REFERENCE_ENUM_CLASS, 'BgpReorgOptEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpReorgOptEnum', 
                [], [], 
                '''                Advertise option
                ''',
                'adv_option',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rt-type', REFERENCE_ENUM_CLASS, 'BgpAdvRtEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAdvRtEnum', 
                [], [], 
                '''                RT type
                ''',
                'rt_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertise-vrf-imp-disable-v4',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                BGP AF group address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('accept-own', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Handle self-originated routes with Accept-Own
                community. Valid for following neighbor
                address-families: VPNv4Unicast, VPNv6Unicast.
                ''',
                'accept_own',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('accept-route-legacy-rt', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a accept-route-legacy-RT. 
                FALSE to prevent accept-route-legacy-RT from
                being inherited.
                ''',
                'accept_route_legacy_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseDefImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-def-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseDefImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of Default VRF Imported Routes
                ''',
                'advertise_def_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-disable', REFERENCE_CLASS, 'AdvertiseDisable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDisable', 
                [], [], 
                '''                Disable Advertise Of Routes to the peer
                ''',
                'advertise_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseL2Vpnevpn', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-l2vpnevpn', REFERENCE_CLASS, 'AdvertiseLocalL2Vpnevpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalL2Vpnevpn', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_l2vpnevpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label
                ''',
                'advertise_local_labeled_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v4', REFERENCE_CLASS, 'AdvertiseLocalV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV4', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-v6', REFERENCE_CLASS, 'AdvertiseLocalV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV6', 
                [], [], 
                '''                Advertise Of Local Routes to the peer with
                different RT
                ''',
                'advertise_local_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-orf', REFERENCE_ENUM_CLASS, 'BgpOrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpOrfEnum', 
                [], [], 
                '''                Advertise ORF capability to the peer
                ''',
                'advertise_orf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-permanent-network', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise Permanent Networks to the peer
                ''',
                'advertise_permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v4', REFERENCE_CLASS, 'AdvertiseV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV4', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-v6', REFERENCE_CLASS, 'AdvertiseV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV6', 
                [], [], 
                '''                Advertise Translated Routes to the peer
                ''',
                'advertise_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v4', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV4', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v4',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-vrf-imp-disable-v6', REFERENCE_CLASS, 'AdvertiseVrfImpDisableV6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV6', 
                [], [], 
                '''                Disable Advertise Of VRF ReImported Routes
                ''',
                'advertise_vrf_imp_disable_v6',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('af-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit configuration for this
                address-family from an AF-group
                ''',
                'af_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable Accumulated IGP Metric for this neighbor.
                ''',
                'aigp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-cost-community', REFERENCE_CLASS, 'AigpCostCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AigpCostCommunity', 
                [], [], 
                '''                Send AIGP value in Cost Community. 
                ''',
                'aigp_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aigp-send-med', REFERENCE_ENUM_CLASS, 'BgpAigpCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAigpCfgEnum', 
                [], [], 
                '''                Enable/Disable sending AIGP in MED 
                ''',
                'aigp_send_med',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allow-as-in', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                Allow as-path with my AS present in it
                ''',
                'allow_as_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-override', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to override matching AS-number while
                sending update. FALSE to prevent as-override
                from being inherited from the parent
                ''',
                'as_override',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create this address family group.
                Deletion of this object causes deletion
                of all the objects under AFGroup
                associated with this object.
                ''',
                'create',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-originate', REFERENCE_CLASS, 'DefaultOriginate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.DefaultOriginate', 
                [], [], 
                '''                Originate default route to this neighbor
                ''',
                'default_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-weight', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Set default weight for routes from this
                neighbor/neighbor-group/af-group
                ''',
                'default_weight',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'BgpAfEncapsulationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpAfEncapsulationEnum', 
                [], [], 
                '''                Encapsulation type for this neighbor
                ''',
                'encapsulation_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('flowspec-validation', REFERENCE_ENUM_CLASS, 'BgpFlowspecValidationCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpFlowspecValidationCfgEnum', 
                [], [], 
                '''                Config Flowspec validation for this neighbor
                ''',
                'flowspec_validation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import', REFERENCE_CLASS, 'Import_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.Import_', 
                [], [], 
                '''                Import Reorigination options for Routes from the
                peer
                ''',
                'import_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('l2vpn-signalling', REFERENCE_ENUM_CLASS, 'BgpSignalEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSignalEnum', 
                [], [], 
                '''                Disable signalling type on the peer
                ''',
                'l2vpn_signalling',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('maximum-prefixes', REFERENCE_CLASS, 'MaximumPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.MaximumPrefixes', 
                [], [], 
                '''                Maximum number of prefixes to accept from this
                peer
                ''',
                'maximum_prefixes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multipath', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow paths from this neighbor to be eligible
                for selective multipath
                ''',
                'multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-capable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to treat neighbor as Long-lived
                Graceful-restart capable. FALSE to rely on
                capability negotiation.
                ''',
                'neighbor_af_long_lived_graceful_restart_capable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-af-long-lived-graceful-restart-stale-time', REFERENCE_CLASS, 'NeighborAfLongLivedGracefulRestartStaleTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.NeighborAfLongLivedGracefulRestartStaleTime', 
                [], [], 
                '''                Maximum time to wait before purging long lived
                routes
                ''',
                'neighbor_af_long_lived_graceful_restart_stale_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-self', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable the next hop calculation and  insert
                your own address in the nexthop field of
                advertised routes you learned from the neighbor.
                ''',
                'next_hop_self',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop before
                advertising to eBGP peers. FALSE to prevent
                next-hop-unchanged from being inherited.
                ''',
                'next_hop_unchanged',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-unchanged-multipath', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable overwriting of next hop for
                multipaths. FALSE to prevent next-hop-unchanged
                for multipaths.
                ''',
                'next_hop_unchanged_multipath',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('prefix-orf-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix ORF policy name for incoming updates
                ''',
                'prefix_orf_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPath', 
                [], [], 
                '''                Remove private AS number from outbound updates
                ''',
                'remove_private_as_entire_as_path',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remove-private-as-entire-as-path-inbound', REFERENCE_CLASS, 'RemovePrivateAsEntireAsPathInbound' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPathInbound', 
                [], [], 
                '''                Remove private AS number from inbound updates
                ''',
                'remove_private_as_entire_as_path_inbound',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-in', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to inbound routes
                ''',
                'route_policy_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-out', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name to apply to outbound routes
                ''',
                'route_policy_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure as a route-reflector-client. 
                FALSE to prevent route-reflector-client from
                being inherited.
                ''',
                'route_reflector_client',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-community-ebgp-graceful-shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send communities to the external
                neighbor/neighbor-group/af-group.  FALSE not to
                send and to prevent inheritance from a parent
                ''',
                'send_community_ebgp_graceful_shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-ext-community-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to send extended communities to the
                external neighbor/neighbor-group/af-group. 
                FALSE not to send and to prevent inheritance
                from a parent
                ''',
                'send_ext_community_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-multicast-attr', REFERENCE_ENUM_CLASS, 'BgpSendMcastAttrCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpSendMcastAttrCfgEnum', 
                [], [], 
                '''                Config send multicast attribute for this
                neighbor
                ''',
                'send_multicast_attr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('site-of-origin', REFERENCE_CLASS, 'SiteOfOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SiteOfOrigin', 
                [], [], 
                '''                Site-of-Origin extended community associated
                with the neighbor
                ''',
                'site_of_origin',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('soft-reconfiguration', REFERENCE_CLASS, 'SoftReconfiguration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SoftReconfiguration', 
                [], [], 
                '''                Enable/disable inbound soft reconfiguration for
                this neighbor/neighbor-group/af-group
                ''',
                'soft_reconfiguration',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'af-group-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs',
            False, 
            [
            _MetaInfoClassMember('af-group-af', REFERENCE_LIST, 'AfGroupAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf', 
                [], [], 
                '''                Address family type of an AF group
                ''',
                'af_group_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'af-group-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup',
            False, 
            [
            _MetaInfoClassMember('af-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                BGP AF group name
                ''',
                'af_group_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('af-group-afs', REFERENCE_CLASS, 'AfGroupAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs', 
                [], [], 
                '''                AF group configuration table
                ''',
                'af_group_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'af-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups',
            False, 
            [
            _MetaInfoClassMember('af-group', REFERENCE_LIST, 'AfGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup', 
                [], [], 
                '''                A particular BGP AF group
                ''',
                'af_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'af-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAddress',
            False, 
            [
            _MetaInfoClassMember('local-address-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a local
                address if the parent has one.FALSE to specify
                local ip address
                ''',
                'local_address_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Local ip address for neighbor
                ''',
                'local_ip_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('local-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Local ip address for neighbor
                        ''',
                        'local_ip_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates.BmpActivate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates.BmpActivate',
            False, 
            [
            _MetaInfoClassMember('server-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '8')], [], 
                '''                BMP Server ID
                ''',
                'server_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates',
            False, 
            [
            _MetaInfoClassMember('bmp-activate', REFERENCE_LIST, 'BmpActivate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates.BmpActivate', 
                [], [], 
                '''                Enable BMP logging for this particular server
                ''',
                'bmp_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-activates',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('max-hop-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum hop count
                ''',
                'max_hop_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-deactivation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to not enable MPLS and NULL rewrite.
                ''',
                'mpls_deactivation',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp-multihop',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable Local AS and prevent it from being
                inherited from a parent
                ''',
                'disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dual-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Dual-AS mode
                ''',
                'dual_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('no-prepend', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not prepend Local AS to announcements from
                this neighbor
                ''',
                'no_prepend',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('replace-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Prepend only Local AS to announcements from
                this neighbor
                ''',
                'replace_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'local-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Password' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Password',
            False, 
            [
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The neighbor password.  Leave unspecified when
                disabling the password.
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                password even if the parent has one.  FALSEto
                specify a password
                ''',
                'password_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'password',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.AdvertisementInterval' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.AdvertisementInterval',
            False, 
            [
            _MetaInfoClassMember('minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Minimum advertisement interval time, secs part
                ''',
                'minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('minimum-interval-msecs', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Minimum advertisement interval time, msecs part
                ''',
                'minimum_interval_msecs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'advertisement-interval',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.NeighborClusterId' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.NeighborClusterId',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Route-Reflector Cluster ID in IPV4 address
                format
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Route-Reflector Cluster ID as 32 bit quantity
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'neighbor-cluster-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tcpmss' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tcpmss',
            False, 
            [
            _MetaInfoClassMember('mss', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                Maximum Segment Size
                ''',
                'mss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance ofTCP MSS
                valuefrom its parents.FALSE, otherwise
                ''',
                'tcpmss_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tcpmss',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tos' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tos',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpTosEnum', 
                [], [], 
                '''                Set type of service
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TOS value to set
                ''',
                'value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'BgpPrecedenceDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpPrecedenceDscpEnum', 
                        [], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers',
            False, 
            [
            _MetaInfoClassMember('non-circular-buffer', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to configure non-circular buffer
                ''',
                'non_circular_buffer',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('number-of-buffers', ATTRIBUTE, 'int' , None, None, 
                [('0', '25')], [], 
                '''                Number of message buffers
                ''',
                'number_of_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering-message-buffers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure inbound update filtering
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-attribute-filter-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Attribute-filter group name for update
                filtering
                ''',
                'update_in_filtering_attribute_filter_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-message-buffers', REFERENCE_CLASS, 'UpdateInFilteringMessageBuffers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers', 
                [], [], 
                '''                Message buffers to store filtered updates
                ''',
                'update_in_filtering_message_buffers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering-syslog-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound update filtering syslog
                messages
                ''',
                'update_in_filtering_syslog_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-in-filtering',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogOut' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogOut',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Outbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                outbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.ReceiveBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.ReceiveBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogIn' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogIn',
            False, 
            [
            _MetaInfoClassMember('msg-buf-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Inbound message log buffer size
                ''',
                'msg_buf_count',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable inbound message logging
                ''',
                'msg_log_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-inherit-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent this entity from having a
                inbound message logging if parent has one
                ''',
                'msg_log_inherit_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'msg-log-in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.SendBufferSize' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.SendBufferSize',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-buffer-size',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Timers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time.  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval
                ''',
                'keepalive_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time.  Specify 0 to
                disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Keychain' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Keychain',
            False, 
            [
            _MetaInfoClassMember('keychain-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to prevent this entity from having a
                keychain based authentication even if the
                parent has one.FALSE to specify a keychain name
                ''',
                'keychain_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the keychain associated with neighbor
                ''',
                'keychain_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'keychain',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference',
            False, 
            [
            _MetaInfoClassMember('gshut-loc-pref-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of Local Pref
                value from its parents.FALSE, otherwise
                ''',
                'gshut_loc_pref_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local Preference Value
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-local-preference',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends',
            False, 
            [
            _MetaInfoClassMember('as-prepends', ATTRIBUTE, 'int' , None, None, 
                [('0', '6')], [], 
                '''                number of times AS prepends
                ''',
                'as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('gshut-prepends-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE, to prevent inheritance of AS Prepends
                value from its parents.FALSE, otherwise
                ''',
                'gshut_prepends_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance-as-prepends',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enter Graceful Maintenance mode to configure
                parametrs
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-activate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Initiate the graceful shutdown procedure
                ''',
                'graceful_maintenance_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-as-prepends', REFERENCE_CLASS, 'GracefulMaintenanceAsPrepends' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends', 
                [], [], 
                '''                Number of times to prepend local AS number to
                the AS path
                ''',
                'graceful_maintenance_as_prepends',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance-local-preference', REFERENCE_CLASS, 'GracefulMaintenanceLocalPreference' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference', 
                [], [], 
                '''                Set Local Preference to advertise routes with
                ''',
                'graceful_maintenance_local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'graceful-maintenance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup',
            False, 
            [
            _MetaInfoClassMember('session-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                BGP session group name
                ''',
                'session_group_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('additional-paths-receive-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send-capability', REFERENCE_ENUM_CLASS, 'BgpNbrCapAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpNbrCapAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertisement-interval', REFERENCE_CLASS, 'AdvertisementInterval' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.AdvertisementInterval', 
                [], [], 
                '''                Minimum interval between sending BGP routing
                updates
                ''',
                'advertisement_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-enable-modes', REFERENCE_ENUM_CLASS, 'BgpBfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpBfdEnableModeEnum', 
                [], [], 
                '''                Strict mode, Default mode or Disable to prevent
                inheritance from a parent
                ''',
                'bfd_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-minimum-interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'bfd_minimum_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created by
                BGP
                ''',
                'bfd_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bmp-activates', REFERENCE_CLASS, 'BmpActivates' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates', 
                [], [], 
                '''                Enable BMP logging for this neighbor
                ''',
                'bmp_activates',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create this group. Deletion of this object
                causes deletion of all the objects under
                NeighborGroup/SessionGroup associated with this
                object.
                ''',
                'create',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Up to 80 characters describing this neighbor
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.EbgpMultihop', 
                [], [], 
                '''                Allow EBGP neighbors not on directly connected
                networks
                ''',
                'ebgp_multihop',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-recv-dmz', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to receive DMZ link bandwidth from ebgp
                peer. FALSE to not receive from ebgp peer and to
                prevent inheritance from a parent
                ''',
                'ebgp_recv_dmz',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp-send-dmz-enable-modes', REFERENCE_ENUM_CLASS, 'BgpEbgpSendDmzEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpEbgpSendDmzEnableModeEnum', 
                [], [], 
                '''                Default mode, Cumulative mode or Disable to
                prevent inheritance from a parent
                ''',
                'ebgp_send_dmz_enable_modes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('egress-peer-engineering', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable egress peer engineering FALSE to
                disable egress peer engineering and to prevent
                inheritance from a parent
                ''',
                'egress_peer_engineering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enforce-first-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enforce first AS; FALSE to not enforce
                first AS.
                ''',
                'enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-maintenance', REFERENCE_CLASS, 'GracefulMaintenance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance', 
                [], [], 
                '''                Graceful Maintenance mode
                ''',
                'graceful_maintenance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('idle-watch-time', ATTRIBUTE, 'int' , None, None, 
                [('30', '1800')], [], 
                '''                Time to wait for deleteing IDLE state Dynamic
                peer
                ''',
                'idle_watch_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ignore-connected-check-ebgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to disable the connected nexthop check for
                this peer.FALSE to enable the connected nexthop
                check for this peer.
                ''',
                'ignore_connected_check_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-vpn-client-ibgpce', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to preserve the CE path attributes.FALSE to
                override CE path attributes.
                ''',
                'internal_vpn_client_ibgpce',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keychain', REFERENCE_CLASS, 'Keychain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Keychain', 
                [], [], 
                '''                Set or disable keychain based authentication
                ''',
                'keychain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-address', REFERENCE_CLASS, 'LocalAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAddress', 
                [], [], 
                '''                Local ip address
                ''',
                'local_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-as', REFERENCE_CLASS, 'LocalAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAs', 
                [], [], 
                '''                Specify a local-as number
                ''',
                'local_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('max-peers', ATTRIBUTE, 'int' , None, None, 
                [('1', '4096')], [], 
                '''                Set Maximum Peers in Dynamic Range
                ''',
                'max_peers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-in', REFERENCE_CLASS, 'MsgLogIn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogIn', 
                [], [], 
                '''                Message log inbound
                ''',
                'msg_log_in',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('msg-log-out', REFERENCE_CLASS, 'MsgLogOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogOut', 
                [], [], 
                '''                Message log outbound
                ''',
                'msg_log_out',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-cluster-id', REFERENCE_CLASS, 'NeighborClusterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.NeighborClusterId', 
                [], [], 
                '''                Neighbor Cluster-id
                ''',
                'neighbor_cluster_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Enable graceful restart support for
                neighbor.  FALSE to disable graceful restart
                support for neighbor.
                ''',
                'neighbor_graceful_restart',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-stalepath-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Maximum time to wait for restart of GR capable
                peer
                ''',
                'neighbor_graceful_restart_stalepath_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-graceful-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Restart time advertised to neighbor
                ''',
                'neighbor_graceful_restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password', REFERENCE_CLASS, 'Password' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Password', 
                [], [], 
                '''                Set or disable a password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('propagate-dmz-link-bandwidth', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to propagate DMZ link bandwidth.  FALSE to
                not propagate and to prevent inheritance from a
                parent
                ''',
                'propagate_dmz_link_bandwidth',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-buffer-size', REFERENCE_CLASS, 'ReceiveBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.ReceiveBufferSize', 
                [], [], 
                '''                Set socket receive buffer size and BGP read
                buffer size
                ''',
                'receive_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.RemoteAs', 
                [], [], 
                '''                Set remote AS
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('remote-as-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote-as-list group name
                ''',
                'remote_as_list',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-buffer-size', REFERENCE_CLASS, 'SendBufferSize' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.SendBufferSize', 
                [], [], 
                '''                Set socket send buffer size and BGP write buffer
                size
                ''',
                'send_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-group-add-member', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inherit address-family independent config
                from a session-group
                ''',
                'session_group_add_member',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-open-mode', REFERENCE_ENUM_CLASS, 'BgpTcpModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpTcpModeEnum', 
                [], [], 
                '''                TCP mode to be used to establish BGP session
                ''',
                'session_open_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to shutdown this entity, FALSE to prevent
                this entity from being shutdown even if the
                parent is.
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-all-capabilities', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress all capabilities. FALSE to not
                suppress and to prevent inheritance from a
                parent
                ''',
                'suppress_all_capabilities',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-four-byte-as-capability', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to suppress BGP 4-byte-as capability. 
                FALSE to not suppress it and to prevent
                inheritance from a parent
                ''',
                'suppress_four_byte_as_capability',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tcpmss', REFERENCE_CLASS, 'Tcpmss' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tcpmss', 
                [], [], 
                '''                TCP Maximum segment size
                ''',
                'tcpmss',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Timers', 
                [], [], 
                '''                BGP per neighbor timers.
                ''',
                'timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tos', 
                [], [], 
                '''                TOS (Type Of Service)
                ''',
                'tos',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ttl-security', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BGP TTL Security.  FALSE to not
                enable it and to prevent inheritance from a
                parent
                ''',
                'ttl_security',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-in-filtering', REFERENCE_CLASS, 'UpdateInFiltering' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering', 
                [], [], 
                '''                Inbound update filtering
                ''',
                'update_in_filtering',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Select an interface to configure
                ''',
                'update_source_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'session-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups',
            False, 
            [
            _MetaInfoClassMember('session-group', REFERENCE_LIST, 'SessionGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup', 
                [], [], 
                '''                A particular BGP session group
                ''',
                'session_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'session-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity',
            False, 
            [
            _MetaInfoClassMember('af-groups', REFERENCE_CLASS, 'AfGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups', 
                [], [], 
                '''                AF-group configuration
                ''',
                'af_groups',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-groups', REFERENCE_CLASS, 'NeighborGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups', 
                [], [], 
                '''                Neighbor-group configuration
                ''',
                'neighbor_groups',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors', 
                [], [], 
                '''                Neighbor configuration
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('session-groups', REFERENCE_CLASS, 'SessionGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups', 
                [], [], 
                '''                Session group configuration
                ''',
                'session_groups',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bgp-entity',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ClusterId' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ClusterId',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Route-Reflector Cluster ID in IPV4 address
                format
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Route-Reflector Cluster ID as 32 bit
                quantity
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'cluster-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.WriteLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.WriteLimit',
            False, 
            [
            _MetaInfoClassMember('desynchronize', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable desynchronization, FALSE
                otherwise.
                ''',
                'desynchronize',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enqueued-messages', ATTRIBUTE, 'int' , None, None, 
                [('500', '100000000')], [], 
                '''                Number of messages that can be enqueued in
                total
                ''',
                'enqueued_messages',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('formatted-messages', ATTRIBUTE, 'int' , None, None, 
                [('500', '100000000')], [], 
                '''                Number of messages to be formatted per
                update group
                ''',
                'formatted_messages',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'write-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.UpdateDelay' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.UpdateDelay',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to TRUE to disable keepalive trigger
                bestpath and delay is enforced.
                ''',
                'always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Delay value (seconds)
                ''',
                'delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'update-delay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of peer AS xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of peer AS xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers.Peer', 
                [], [], 
                '''                AS League Peer AS
                ''',
                'peer',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                AS League creation
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers', 
                [], [], 
                '''                AS League Peers
                ''',
                'peers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'as-league',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer.Transport' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer.Transport',
            False, 
            [
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                port
                ''',
                'port',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transport', REFERENCE_ENUM_CLASS, 'BgpRpkiTransportEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpRpkiTransportEnum', 
                [], [], 
                '''                RPKI server transport
                ''',
                'transport',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'transport',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer',
            False, 
            [
            _MetaInfoClassMember('server', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Server address (opaque string)
                ''',
                'server',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI server configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RPKI server password
                ''',
                'password',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('purge-time', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                RPKI server purge-time (seconds)
                ''',
                'purge_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('refresh-time', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                RPKI server refresh-time (seconds)
                ''',
                'refresh_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('response-time', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                RPKI server response-time (seconds)
                ''',
                'response_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI server shutdown
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('transport', REFERENCE_CLASS, 'Transport' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer.Transport', 
                [], [], 
                '''                RPKI server transport
                ''',
                'transport',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RPKI server username
                ''',
                'username',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'rpki-server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers',
            False, 
            [
            _MetaInfoClassMember('rpki-server', REFERENCE_LIST, 'RpkiServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer', 
                [], [], 
                '''                RPKI server configuration
                ''',
                'rpki_server',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'rpki-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases.As_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases.As_',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number/confed peer xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number/confed peer xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases',
            False, 
            [
            _MetaInfoClassMember('as', REFERENCE_LIST, 'As_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases.As_', 
                [], [], 
                '''                AS-List group
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ases',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup',
            False, 
            [
            _MetaInfoClassMember('as-list-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group name
                ''',
                'as_list_group_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('ases', REFERENCE_CLASS, 'Ases' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases', 
                [], [], 
                '''                AS list
                ''',
                'ases',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                AS-List group creation
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'as-list-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups',
            False, 
            [
            _MetaInfoClassMember('as-list-group', REFERENCE_LIST, 'AsListGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup', 
                [], [], 
                '''                AS-List group
                ''',
                'as_list_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'as-list-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Limits' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Limits',
            False, 
            [
            _MetaInfoClassMember('maximum-neighbors', ATTRIBUTE, 'int' , None, None, 
                [('1', '15000')], [], 
                '''                Maximum number of neighbors that can be
                configured
                ''',
                'maximum_neighbors',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'limits',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationDomain' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationDomain',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'confederation-domain',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses.ConfederationPeerAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses.ConfederationPeerAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                xx of AS number/confed peer xx.yy
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                yy of AS number/confed peer xx.yy
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'confederation-peer-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses',
            False, 
            [
            _MetaInfoClassMember('confederation-peer-as', REFERENCE_LIST, 'ConfederationPeerAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses.ConfederationPeerAs', 
                [], [], 
                '''                Confederation peer AS
                ''',
                'confederation_peer_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'confederation-peer-ases',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters.AttributeFilter' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters.AttributeFilter',
            False, 
            [
            _MetaInfoClassMember('attribute-start', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                Start of attribute range
                ''',
                'attribute_start',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('attribute-end', ATTRIBUTE, 'int' , None, None, 
                [('0', '256')], [], 
                '''                End of attribute range
                ''',
                'attribute_end',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('filter-action', REFERENCE_ENUM_CLASS, 'BgpUpdateFilterActionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpUpdateFilterActionEnum', 
                [], [], 
                '''                Filtering action
                ''',
                'filter_action',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'attribute-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters',
            False, 
            [
            _MetaInfoClassMember('attribute-filter', REFERENCE_LIST, 'AttributeFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters.AttributeFilter', 
                [], [], 
                '''                Attribute-filter group attribute
                ''',
                'attribute_filter',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'attribute-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup',
            False, 
            [
            _MetaInfoClassMember('attribute-filter-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group name
                ''',
                'attribute_filter_group_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('attribute-filters', REFERENCE_CLASS, 'AttributeFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters', 
                [], [], 
                '''                Attribute-filter group attributes list
                ''',
                'attribute_filters',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute-filter group creation
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'attribute-filter-group',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups',
            False, 
            [
            _MetaInfoClassMember('attribute-filter-group', REFERENCE_LIST, 'AttributeFilterGroup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup', 
                [], [], 
                '''                Attribute-filter group
                ''',
                'attribute_filter_group',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'attribute-filter-groups',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalGracefulMaintenanceActivate' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalGracefulMaintenanceActivate',
            False, 
            [
            _MetaInfoClassMember('all-neighbors', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Also for neighbors without graceful
                maintenance config
                ''',
                'all_neighbors',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('retain-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Keep routes in RIB once BGP stops
                ''',
                'retain_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'global-graceful-maintenance-activate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes.IsisRoute' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes.IsisRoute',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IS-IS instance name
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('redist-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Redistribution type: 01 for level 1
                routes, 02 for level 2 routes, 04 for
                level 1 inter-area routes. Logical
                combinations permitted.
                ''',
                'redist_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'isis-route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes',
            False, 
            [
            _MetaInfoClassMember('isis-route', REFERENCE_LIST, 'IsisRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes.IsisRoute', 
                [], [], 
                '''                Redistribute IS-IS routes
                ''',
                'isis_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'isis-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DomainDistinguisher' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DomainDistinguisher',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS Number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID
                ''',
                'router_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'domain-distinguisher',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll.LabelMode' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll.LabelMode',
            False, 
            [
            _MetaInfoClassMember('label-allocation-mode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label allocation mode: per-ce  Set per
                CE label mode, per-vrf Set per VRF
                label mode
                ''',
                'label_allocation_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label mode route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'label-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable vrf all configuration submode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('label-mode', REFERENCE_CLASS, 'LabelMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll.LabelMode', 
                [], [], 
                '''                MPLS-VPN label allocation mode
                ''',
                'label_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('source-rt-import-policy', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable sourcing of import route-targets 
                from import-policy
                ''',
                'source_rt_import_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('table-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure policy for installation of
                routes to RIB
                ''',
                'table_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'vrf-all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes.ApplicationRoute' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes.ApplicationRoute',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OnePK application name
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'application-route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes',
            False, 
            [
            _MetaInfoClassMember('application-route', REFERENCE_LIST, 'ApplicationRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes.ApplicationRoute', 
                [], [], 
                '''                Redistribute application routes
                ''',
                'application_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'application-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Number' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Number',
            False, 
            [
            _MetaInfoClassMember('cluster-id-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cluster ID: if configured as a number
                ''',
                'cluster_id_number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'number',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Ipv4Address' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Ipv4Address',
            False, 
            [
            _MetaInfoClassMember('cluster-id-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Cluster ID: if configured as an IP
                Address
                ''',
                'cluster_id_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Cluster ID: if configured as an IP
                        Address
                        ''',
                        'cluster_id_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('cluster-id-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Cluster ID: if configured as an IP
                        Address
                        ''',
                        'cluster_id_address',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ipv4-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr',
            False, 
            [
            _MetaInfoClassMember('cluster-type', REFERENCE_ENUM_CLASS, 'BgpClusterIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BgpClusterIdEnum', 
                [], [], 
                '''                Type of cluster-id
                ''',
                'cluster_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('ipv4-address', REFERENCE_LIST, 'Ipv4Address' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Ipv4Address', 
                [], [], 
                '''                ipv4 address
                ''',
                'ipv4_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('number', REFERENCE_LIST, 'Number' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Number', 
                [], [], 
                '''                number
                ''',
                'number',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'disable-cluster-client-to-client-rr',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs',
            False, 
            [
            _MetaInfoClassMember('disable-cluster-client-to-client-rr', REFERENCE_LIST, 'DisableClusterClientToClientRr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr', 
                [], [], 
                '''                Cluster ID for which reflection is to be
                disbled
                ''',
                'disable_cluster_client_to_client_rr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'disable-cluster-client-to-client-rrs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelDelay' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelDelay',
            False, 
            [
            _MetaInfoClassMember('milliseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Delay, milliseconds part
                ''',
                'milliseconds',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Delay, seconds part
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'label-delay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ebgp',
            False, 
            [
            _MetaInfoClassMember('order-by-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Order candidate multipaths by IGP metric
                ''',
                'order_by_igp_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('paths-value', ATTRIBUTE, 'int' , None, None, 
                [('2', '64')], [], 
                '''                Number of paths
                ''',
                'paths_value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selective', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths only from marked
                neighbors
                ''',
                'selective',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('unequal-cost', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                UNUSED
                ''',
                'unequal_cost',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ebgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Eibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Eibgp',
            False, 
            [
            _MetaInfoClassMember('order-by-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Order candidate multipaths by IGP metric
                ''',
                'order_by_igp_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('paths-value', ATTRIBUTE, 'int' , None, None, 
                [('2', '64')], [], 
                '''                Number of paths
                ''',
                'paths_value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selective', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths only from marked
                neighbors
                ''',
                'selective',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('unequal-cost', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                UNUSED
                ''',
                'unequal_cost',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'eibgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RetainRt' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RetainRt',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether all RTs are to be retained,
                default is FALSE
                ''',
                'all',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'retain-rt',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ibgp',
            False, 
            [
            _MetaInfoClassMember('order-by-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Order candidate multipaths by IGP metric
                ''',
                'order_by_igp_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('paths-value', ATTRIBUTE, 'int' , None, None, 
                [('2', '64')], [], 
                '''                Number of paths
                ''',
                'paths_value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selective', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths only from marked
                neighbors
                ''',
                'selective',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('unequal-cost', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipaths to have different IGP
                metrics
                ''',
                'unequal_cost',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ibgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ImportDelay' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ImportDelay',
            False, 
            [
            _MetaInfoClassMember('milliseconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '999')], [], 
                '''                Delay, milliseconds part
                ''',
                'milliseconds',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('seconds', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Delay, seconds part
                ''',
                'seconds',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'import-delay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses.AggregateAddress' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses.AggregateAddress',
            False, 
            [
            _MetaInfoClassMember('aggregate-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Aggregate in prefix/length format (address
                part)
                ''',
                'aggregate_addr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('aggregate-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Aggregate in prefix/length format (address
                        part)
                        ''',
                        'aggregate_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('aggregate-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Aggregate in prefix/length format (address
                        part)
                        ''',
                        'aggregate_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('aggregate-prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Aggregate in prefix/length format (prefix
                part)
                ''',
                'aggregate_prefix',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('generate-confederation-set-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate AS confederation set path
                information, FALSE otherwise
                ''',
                'generate_confederation_set_info',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('generate-set-info', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to generate AS set path information,
                FALSE otherwise
                ''',
                'generate_set_info',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy on which to condition
                advertisement, suppression, and attributes
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('summary-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to filter more specific routes from
                updates, FALSEotherwise
                ''',
                'summary_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aggregate-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses',
            False, 
            [
            _MetaInfoClassMember('aggregate-address', REFERENCE_LIST, 'AggregateAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses.AggregateAddress', 
                [], [], 
                '''                Aggregate address configuration
                ''',
                'aggregate_address',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'aggregate-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Dampening' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Dampening',
            False, 
            [
            _MetaInfoClassMember('half-life', ATTRIBUTE, 'int' , None, None, 
                [('1', '45')], [], 
                '''                Half-life time for the penalty (minutes).
                ''',
                'half_life',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reuse-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '20000')], [], 
                '''                Value to start reusing a route.
                ''',
                'reuse_threshold',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to specify criteria for dampening.
                This cannot be specified if any other
                parameters are specified.
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '20000')], [], 
                '''                Value to start suppressing a route.
                ''',
                'suppress_threshold',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('suppress-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Maximum duration to suppress a stable route
                (seconds).
                ''',
                'suppress_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RipRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RipRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'rip-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LispRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LispRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'lisp-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.StaticRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.StaticRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'static-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Distance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Distance',
            False, 
            [
            _MetaInfoClassMember('external-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for routes external to the AS
                ''',
                'external_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('internal-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for routes internal to the AS
                ''',
                'internal_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-routes', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for local routes
                ''',
                'local_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelMode' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelMode',
            False, 
            [
            _MetaInfoClassMember('label-allocation-mode', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label allocation mode: per-ce  Set per CE label
                mode, per-vrf Set per VRF label mode,
                per-prefix Set per Prefix label mode (for
                MPLS-VPN only)
                ''',
                'label_allocation_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Label mode route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'label-mode',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes.EigrpRoute' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes.EigrpRoute',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                EIGRP router tag
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('redist-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Redistribution type: 01 for internal routes,
                02 for external routes, Logical combinations
                permitted.
                ''',
                'redist_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'eigrp-route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes',
            False, 
            [
            _MetaInfoClassMember('eigrp-route', REFERENCE_LIST, 'EigrpRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes.EigrpRoute', 
                [], [], 
                '''                Redistribute EIGRP routes
                ''',
                'eigrp_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'eigrp-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks.SourcedNetwork' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks.SourcedNetwork',
            False, 
            [
            _MetaInfoClassMember('network-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Network in prefix/length format (address part)
                ''',
                'network_addr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('network-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Network in prefix/length format (address part)
                        ''',
                        'network_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('network-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Network in prefix/length format (address part)
                        ''',
                        'network_addr',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('network-prefix', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Network in prefix/length format (prefix part)
                ''',
                'network_prefix',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('backdoor', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify a BGP backdoor route, default is FALSE
                ''',
                'backdoor',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'sourced-network',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks',
            False, 
            [
            _MetaInfoClassMember('sourced-network', REFERENCE_LIST, 'SourcedNetwork' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks.SourcedNetwork', 
                [], [], 
                '''                Sourced network configuration
                ''',
                'sourced_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'sourced-networks',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ConnectedRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ConnectedRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'connected-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AllocateLabel' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AllocateLabel',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether all nets should be labeled, default is
                FALSE
                ''',
                'all',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'allocate-label',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AdditionalPathsSelection' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AdditionalPathsSelection',
            False, 
            [
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for selection
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('selection', REFERENCE_ENUM_CLASS, 'BgpafAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpafAdditionalPathsCfgEnum', 
                [], [], 
                '''                Enable/disable selection 
                ''',
                'selection',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'additional-paths-selection',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes.OspfRoute' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes.OspfRoute',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                OSPF router tag
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('redist-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                Redistribution type: 01 for internal routes,
                02 for external routes of type 1, 04 for
                external routes of type 2, 08 for NSSA
                external routes of type 1, 10 for NSSA
                external routes of type 2, 20 for external
                routes, 40 for NSSA external routes.  Logical
                combinations permitted.
                ''',
                'redist_type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ospf-route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes',
            False, 
            [
            _MetaInfoClassMember('ospf-route', REFERENCE_LIST, 'OspfRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes.OspfRoute', 
                [], [], 
                '''                Redistribute OSPF routes
                ''',
                'ospf_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'ospf-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.MobileRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.MobileRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'mobile-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SubscriberRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SubscriberRoutes',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('not-used', ATTRIBUTE, 'int' , None, None, 
                [('0', '127')], [], 
                '''                Not used
                ''',
                'not_used',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy name
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'subscriber-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'BgpAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAddressFamilyEnum', 
                [], [], 
                '''                Address family
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('additional-paths-receive', REFERENCE_ENUM_CLASS, 'BgpafAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpafAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Receive capability
                ''',
                'additional_paths_receive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-selection', REFERENCE_CLASS, 'AdditionalPathsSelection' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AdditionalPathsSelection', 
                [], [], 
                '''                Configure additional paths selection
                ''',
                'additional_paths_selection',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('additional-paths-send', REFERENCE_ENUM_CLASS, 'BgpafAdditionalPathsCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpafAdditionalPathsCfgEnum', 
                [], [], 
                '''                Advertise additional paths Send capability
                ''',
                'additional_paths_send',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('advertise-local-labeled-route-safi-unicast', REFERENCE_ENUM_CLASS, 'BgpAdvertiseLocalLabeledRouteCfgEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpAdvertiseLocalLabeledRouteCfgEnum', 
                [], [], 
                '''                Enable/disable advertisement of routes with
                local-label via Unicast SAFI
                ''',
                'advertise_local_labeled_route_safi_unicast',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('aggregate-addresses', REFERENCE_CLASS, 'AggregateAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses', 
                [], [], 
                '''                Configure BGP aggregate entries
                ''',
                'aggregate_addresses',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('allocate-label', REFERENCE_CLASS, 'AllocateLabel' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AllocateLabel', 
                [], [], 
                '''                Label allocation policy
                ''',
                'allocate_label',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('application-routes', REFERENCE_CLASS, 'ApplicationRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes', 
                [], [], 
                '''                Redistribute information for Application
                routes.
                ''',
                'application_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('attribute-download', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Attribute download configuration
                ''',
                'attribute_download',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-external', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to enable BE FALSE to disable BE
                inheritance from a parent
                ''',
                'best_external',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('connected-routes', REFERENCE_CLASS, 'ConnectedRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ConnectedRoutes', 
                [], [], 
                '''                Redistribute connected routes
                ''',
                'connected_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dampening', REFERENCE_CLASS, 'Dampening' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Dampening', 
                [], [], 
                '''                Enable route-flap dampening
                ''',
                'dampening',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-as-path-loop-check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable outbound AS Path loop check
                ''',
                'disable_as_path_loop_check',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-client-to-client-rr', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable client-to-client reflection
                ''',
                'disable_client_to_client_rr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-cluster-client-to-client-rrs', REFERENCE_CLASS, 'DisableClusterClientToClientRrs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs', 
                [], [], 
                '''                Disable client-to-client reflection for a
                cluster
                ''',
                'disable_cluster_client_to_client_rrs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-default-martian-check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable default Martian Check
                ''',
                'disable_default_martian_check',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('distance', REFERENCE_CLASS, 'Distance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Distance', 
                [], [], 
                '''                Define an administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('domain-distinguisher', REFERENCE_CLASS, 'DomainDistinguisher' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DomainDistinguisher', 
                [], [], 
                '''                <ASN, router-id> tuple to use to identify
                the link-state domain
                ''',
                'domain_distinguisher',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('dynamic-med-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '10')], [], 
                '''                Update generation delay (in minutes) after a MED
                change
                ''',
                'dynamic_med_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ebgp', 
                [], [], 
                '''                Use eBGP multipaths
                ''',
                'ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('eibgp', REFERENCE_CLASS, 'Eibgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Eibgp', 
                [], [], 
                '''                Use eiBGP multipaths
                ''',
                'eibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('eigrp-routes', REFERENCE_CLASS, 'EigrpRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes', 
                [], [], 
                '''                Redistribute information for EIGRP routes.
                ''',
                'eigrp_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable the address family. Deletion of this
                object causes deletion of all the objects under
                GlobalAF/VRFGlobalAF associated with this object
                .
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global-table-mcast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable global table multicast
                ''',
                'global_table_mcast',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ibgp', REFERENCE_CLASS, 'Ibgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ibgp', 
                [], [], 
                '''                Use iBGP multipaths
                ''',
                'ibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('import-delay', REFERENCE_CLASS, 'ImportDelay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ImportDelay', 
                [], [], 
                '''                Delay timer to batch import processing.
                ''',
                'import_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('inter-as-install', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable install remote MVPN routes to PIM
                in default VRF
                ''',
                'inter_as_install',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('isis-routes', REFERENCE_CLASS, 'IsisRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes', 
                [], [], 
                '''                Redistribute information for IS-IS routes
                .
                ''',
                'isis_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('label-delay', REFERENCE_CLASS, 'LabelDelay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelDelay', 
                [], [], 
                '''                Delay timer to batch label processing.
                ''',
                'label_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('label-mode', REFERENCE_CLASS, 'LabelMode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelMode', 
                [], [], 
                '''                BGP 6PE/MPLS-VPN label allocation mode
                ''',
                'label_mode',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('label-retain', ATTRIBUTE, 'int' , None, None, 
                [('3', '60')], [], 
                '''                Label retention time in minutes
                ''',
                'label_retain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('label-security-rpf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Calculate label-security RPF lists and
                install to RIB/LSD
                ''',
                'label_security_rpf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('lisp-routes', REFERENCE_CLASS, 'LispRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LispRoutes', 
                [], [], 
                '''                Redistribute lisp routes
                ''',
                'lisp_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mobile-routes', REFERENCE_CLASS, 'MobileRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.MobileRoutes', 
                [], [], 
                '''                Redistribute mobile routes
                ''',
                'mobile_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-critical-trigger-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next hop Critical Trigger Delay
                ''',
                'next_hop_critical_trigger_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-non-critical-trigger-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Next hop Non-critical Trigger Delay
                ''',
                'next_hop_non_critical_trigger_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-resolution-prefix-length-minimum', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                Minimum prefix-length for nexthop resolution
                ''',
                'next_hop_resolution_prefix_length_minimum',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-route-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Next hop policy to filter out nexthop
                notification
                ''',
                'next_hop_route_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('ospf-routes', REFERENCE_CLASS, 'OspfRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes', 
                [], [], 
                '''                Redistribute information for OSPF routes.
                ''',
                'ospf_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('permanent-network', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for permanent networks
                ''',
                'permanent_network',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('reset-weight-on-import', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to reset weight on import. FALSE to not
                reset and to prevent inheritance from a parent
                ''',
                'reset_weight_on_import',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('retain-rt', REFERENCE_CLASS, 'RetainRt' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RetainRt', 
                [], [], 
                '''                Accept received updates with the
                specified attributes
                ''',
                'retain_rt',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rip-routes', REFERENCE_CLASS, 'RipRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RipRoutes', 
                [], [], 
                '''                Redistribute RIP routes
                ''',
                'rip_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-use-origin-as-validity', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath use origin-AS validity
                ''',
                'rpki_bestpath_use_origin_as_validity',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validity-signal-ibgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validity signal ibgp
                ''',
                'rpki_origin_as_validity_signal_ibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('scan-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '3600')], [], 
                '''                Configure background scanner interval for
                this address family
                ''',
                'scan_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('segmented-mcast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable segmented multicast
                ''',
                'segmented_mcast',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('sourced-networks', REFERENCE_CLASS, 'SourcedNetworks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks', 
                [], [], 
                '''                Specify a network to announce via BGP
                ''',
                'sourced_networks',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('static-routes', REFERENCE_CLASS, 'StaticRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.StaticRoutes', 
                [], [], 
                '''                Redistribute static routes
                ''',
                'static_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('subscriber-routes', REFERENCE_CLASS, 'SubscriberRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SubscriberRoutes', 
                [], [], 
                '''                Redistribute subscriber routes
                ''',
                'subscriber_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('table-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configure policy for installation of routes to
                RIB
                ''',
                'table_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-limit-address-family', ATTRIBUTE, 'int' , None, None, 
                [('4', '2048')], [], 
                '''                Upper bound on update generation
                transient memory usage for the
                address-family
                ''',
                'update_limit_address_family',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-limit-sub-group-ebgp', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Upper bound on update generation
                transient memory usage for every EBGP
                Sub-group
                ''',
                'update_limit_sub_group_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-limit-sub-group-ibgp', ATTRIBUTE, 'int' , None, None, 
                [('1', '512')], [], 
                '''                Upper bound on update generation
                transient memory usage for every IBGP
                Sub-group
                ''',
                'update_limit_sub_group_ibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('use-igpsr-label', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Use IGP SR label for resolution
                configuration
                ''',
                'use_igpsr_label',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf-all', REFERENCE_CLASS, 'VrfAll' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll', 
                [], [], 
                '''                Configurations to be inherited to all
                vrfs
                ''',
                'vrf_all',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('wait-rib-install', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Wait for route install before sending
                updates to neighbors
                ''',
                'wait_rib_install',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'global-af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs',
            False, 
            [
            _MetaInfoClassMember('global-af', REFERENCE_LIST, 'GlobalAf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf', 
                [], [], 
                '''                Global AF-specific configuration
                ''',
                'global_af',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'global-afs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes.RpkiStaticRoute' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes.RpkiStaticRoute',
            False, 
            [
            _MetaInfoClassMember('addrress', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address
                ''',
                'addrress',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True, [
                    _MetaInfoClassMember('addrress', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address
                        ''',
                        'addrress',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                    _MetaInfoClassMember('addrress', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address
                        ''',
                        'addrress',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', True),
                ]),
            _MetaInfoClassMember('minimum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Minimum Prefix Length
                ''',
                'minimum',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Maximum Prefix Length
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                AS Number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'rpki-static-route',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes',
            False, 
            [
            _MetaInfoClassMember('rpki-static-route', REFERENCE_LIST, 'RpkiStaticRoute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes.RpkiStaticRoute', 
                [], [], 
                '''                RPKI static route
                ''',
                'rpki_static_route',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'rpki-static-routes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces.MplsActivatedInterface' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces.MplsActivatedInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'mpls-activated-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces',
            False, 
            [
            _MetaInfoClassMember('mpls-activated-interface', REFERENCE_LIST, 'MplsActivatedInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces.MplsActivatedInterface', 
                [], [], 
                '''                Configure a MPLS activated interface
                ''',
                'mpls_activated_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'mpls-activated-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalTimers' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalTimers',
            False, 
            [
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Hold time (seconds).  Specify 0 to disable
                keepalives/hold time
                ''',
                'hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('keepalive', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Keepalive interval (seconds)
                ''',
                'keepalive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('min-accept-hold-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Minimum acceptable hold time (seconds). Specify
                0 to disable keepalives/hold time
                ''',
                'min_accept_hold_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'global-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Bfd' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '16')], [], 
                '''                Detection multiplier for BFD sessions created
                by BGP
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval for BFD sessions created by BGP
                ''',
                'interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.SendSocketBufferSizes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.SendSocketBufferSizes',
            False, 
            [
            _MetaInfoClassMember('bgp-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                BGP Write buffer size in bytes
                ''',
                'bgp_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-send-size', ATTRIBUTE, 'int' , None, None, 
                [('4096', '131072')], [], 
                '''                Send socket buffer size in bytes
                ''',
                'socket_send_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'send-socket-buffer-sizes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ReceiveSocketBufferSizes' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ReceiveSocketBufferSizes',
            False, 
            [
            _MetaInfoClassMember('bgp-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                BGP Read buffer size in bytes
                ''',
                'bgp_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('socket-receive-size', ATTRIBUTE, 'int' , None, None, 
                [('512', '131072')], [], 
                '''                Receive socket buffer size in bytes
                ''',
                'socket_receive_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'receive-socket-buffer-sizes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_',
            False, 
            [
            _MetaInfoClassMember('as-league', REFERENCE_CLASS, 'AsLeague' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague', 
                [], [], 
                '''                AS League
                ''',
                'as_league',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('as-list-groups', REFERENCE_CLASS, 'AsListGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups', 
                [], [], 
                '''                AS-list group lists
                ''',
                'as_list_groups',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('attribute-filter-groups', REFERENCE_CLASS, 'AttributeFilterGroups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups', 
                [], [], 
                '''                Attribute-filter groups list
                ''',
                'attribute_filter_groups',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-aigp-ignore', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria to
                ignore AIGP unless both paths whichare compared
                have AIGP attribute
                ''',
                'best_path_aigp_ignore',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-as-multipath-relax', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default multi-route selection criteria to
                relax as-path checking - only require same
                aspath length
                ''',
                'best_path_as_multipath_relax',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-as-path-length', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria to
                ignore AS path length
                ''',
                'best_path_as_path_length',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-confederation-paths', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria and
                allow the comparing of MED among confederation
                paths
                ''',
                'best_path_confederation_paths',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-cost-community', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria to
                ignore cost community comparison
                ''',
                'best_path_cost_community',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-med-always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria and
                allow comparing of MED from different neighbors
                ''',
                'best_path_med_always',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-med-missing', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Treat missing MED as the least preferred one
                ''',
                'best_path_med_missing',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('best-path-router-id', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default route selection criteria and
                compare router-id for identical EBGP paths
                ''',
                'best_path_router_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Bfd', 
                [], [], 
                '''                BFD configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cluster-id', REFERENCE_CLASS, 'ClusterId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ClusterId', 
                [], [], 
                '''                Configure Route-Reflector Cluster-id
                ''',
                'cluster_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('confederation-domain', REFERENCE_CLASS, 'ConfederationDomain' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationDomain', 
                [], [], 
                '''                Set routing domain confederation AS
                ''',
                'confederation_domain',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('confederation-peer-ases', REFERENCE_CLASS, 'ConfederationPeerAses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses', 
                [], [], 
                '''                Define peer ASes in BGP confederation
                ''',
                'confederation_peer_ases',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Control distribution of default information
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Default redistributed metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-auto-soft-reset', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable automatic soft peer reset on policy
                reconfiguration
                ''',
                'disable_auto_soft_reset',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-enforce-first-as', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable enforce the first AS for EBGP routes
                ''',
                'disable_enforce_first_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-fast-external-fallover', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable immediate reset session if a link to a
                directly connected external peer goes down
                ''',
                'disable_fast_external_fallover',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-msg-log', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable inbound and outbound messagelogging for
                all neighbors under the vrf
                ''',
                'disable_msg_log',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('disable-neighbor-logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable neighbor change logging
                ''',
                'disable_neighbor_logging',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('enforce-ibgp-out-policy', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow all attributes to be modified by
                outbound policy for iBGP peers
                ''',
                'enforce_ibgp_out_policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global-afs', REFERENCE_CLASS, 'GlobalAfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs', 
                [], [], 
                '''                Global AF-specific configuration
                ''',
                'global_afs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global-graceful-maintenance-activate', REFERENCE_CLASS, 'GlobalGracefulMaintenanceActivate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalGracefulMaintenanceActivate', 
                [], [], 
                '''                Activate Graceful Maintenance Mode for all
                neighbors with graceful maintenance config
                ''',
                'global_graceful_maintenance_activate',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global-scan-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '3600')], [], 
                '''                Configure background scanner interval for
                generic scanner
                ''',
                'global_scan_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global-timers', REFERENCE_CLASS, 'GlobalTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalTimers', 
                [], [], 
                '''                Adjust routing timers.
                ''',
                'global_timers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-reset', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Reset gracefully if configuration change
                forces a peer reset
                ''',
                'graceful_reset',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-restart', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable graceful restart support
                ''',
                'graceful_restart',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-restart-purge-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '6000')], [], 
                '''                Time before stale routes are purged.
                ''',
                'graceful_restart_purge_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-restart-stalepath-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Maximum time to wait for restart of GR
                capable peers
                ''',
                'graceful_restart_stalepath_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('graceful-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Restart time advertised to neighbors
                ''',
                'graceful_restart_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('igp-loop-check', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable AS-path loop checking for iBGP peers
                ''',
                'igp_loop_check',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('igp-redist-internal', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow redistribution of iBGP into IGPs
                (dangerous)
                ''',
                'igp_redist_internal',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('install-diversion', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Install diversion path to RIB/CEF
                ''',
                'install_diversion',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('limits', REFERENCE_CLASS, 'Limits' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Limits', 
                [], [], 
                '''                Maximum number that can be configured
                ''',
                'limits',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('local-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configure default local preference
                ''',
                'local_preference',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mpls-activated-interfaces', REFERENCE_CLASS, 'MplsActivatedInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces', 
                [], [], 
                '''                Configure list of MPLS activated interfaces
                ''',
                'mpls_activated_interfaces',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('multi-path-as-path-ignore-onwards', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Change default multi-route selection criteria to
                ignore everything onwards as-path check
                ''',
                'multi_path_as_path_ignore_onwards',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('mvpn', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Connect to PIM/PIM6
                ''',
                'mvpn',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('neighbor-logging-detail', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Include extra detail in neighbor change
                messages
                ''',
                'neighbor_logging_detail',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('next-hop-trigger-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Set the delay for triggering nexthop
                recalculations
                ''',
                'next_hop_trigger_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('nsr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to Enable non-stop routing
                supportFALSE to Disable non-stop routing
                support
                ''',
                'nsr',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('read-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow duplicate table config and disable
                update generation
                ''',
                'read_only',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('receive-socket-buffer-sizes', REFERENCE_CLASS, 'ReceiveSocketBufferSizes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ReceiveSocketBufferSizes', 
                [], [], 
                '''                Set socket and BGP receive buffer sizes
                ''',
                'receive_socket_buffer_sizes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure Router-id
                ''',
                'router_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-origin-as-allow-invalid', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath origin-AS allow invalid
                ''',
                'rpki_bestpath_origin_as_allow_invalid',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-bestpath-use-origin-as-validity', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI bestpath use origin-AS validity
                ''',
                'rpki_bestpath_use_origin_as_validity',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validation disable
                ''',
                'rpki_origin_as_validation_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validation-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Prefix validation time (in seconds). Range 
                : 5 - 60. Specify 0 to disable the timer
                ''',
                'rpki_origin_as_validation_time',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-origin-as-validity-signal-ibgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                RPKI origin-AS validity signal ibgp
                ''',
                'rpki_origin_as_validity_signal_ibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-servers', REFERENCE_CLASS, 'RpkiServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers', 
                [], [], 
                '''                RPKI server configuration
                ''',
                'rpki_servers',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('rpki-static-routes', REFERENCE_CLASS, 'RpkiStaticRoutes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes', 
                [], [], 
                '''                RPKI static route configuration
                ''',
                'rpki_static_routes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('send-socket-buffer-sizes', REFERENCE_CLASS, 'SendSocketBufferSizes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.SendSocketBufferSizes', 
                [], [], 
                '''                set socket parameters
                ''',
                'send_socket_buffer_sizes',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-delay', REFERENCE_CLASS, 'UpdateDelay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.UpdateDelay', 
                [], [], 
                '''                Set the max initial delay for sending
                updates
                ''',
                'update_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-error-handling-basic-ebgp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Inbound update basic error-handling for
                EBGP neighbors
                ''',
                'update_error_handling_basic_ebgp_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-error-handling-basic-ibgp-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Inbound update basic error-handling for
                IBGP neighbors
                ''',
                'update_error_handling_basic_ibgp_disable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-error-handling-extended-ebgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Inbound update extended error-handling for
                EBGP neighbors
                ''',
                'update_error_handling_extended_ebgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-error-handling-extended-ibgp', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Inbound update extended error-handling for
                IBGP neighbors
                ''',
                'update_error_handling_extended_ibgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-limit-process', ATTRIBUTE, 'int' , None, None, 
                [('16', '2048')], [], 
                '''                Upper bound on update generation transient
                memory usage for the process
                ''',
                'update_limit_process',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-out-logging', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enables logging of update generation events
                ''',
                'update_out_logging',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('write-limit', REFERENCE_CLASS, 'WriteLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.WriteLimit', 
                [], [], 
                '''                Set write-queue limit for each update group
                ''',
                'write_limit',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'global',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('bgp-entity', REFERENCE_CLASS, 'BgpEntity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity', 
                [], [], 
                '''                Neighbor, neighbor-group, af-group and
                session-group configuration
                ''',
                'bgp_entity',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_', 
                [], [], 
                '''                Global default config
                ''',
                'global_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs.FourByteAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs.FourByteAs',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                2-byte or 4-byte Autonomous system number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('bgp-running', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BGP. Deletion of this object causes
                deletion of all the objects under FourByteAS
                associated with this object.
                ''',
                'bgp_running',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf', 
                [], [], 
                '''                Global default config
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs.Vrfs', 
                [], [], 
                '''                VRF config
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'four-byte-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance.InstanceAs' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance.InstanceAs',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Higher 16 bits of 4-byte Autonomous system
                number
                ''',
                'as_',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('four-byte-as', REFERENCE_LIST, 'FourByteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs.FourByteAs', 
                [], [], 
                '''                4-byte Autonomous system
                ''',
                'four_byte_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'instance-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp.Instance' : {
        'meta_info' : _MetaInfoClass('Bgp.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Instance Name. For Default instance use -
                default
                ''',
                'instance_name',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('instance-as', REFERENCE_LIST, 'InstanceAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance.InstanceAs', 
                [], [], 
                '''                Autonomous system
                ''',
                'instance_as',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'Bgp' : {
        'meta_info' : _MetaInfoClass('Bgp',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'Bgp.Instance', 
                [], [], 
                '''                BGP instance configuration commands
                ''',
                'instance',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'BmpServers.BmpServer.InitialRefreshDelay' : {
        'meta_info' : _MetaInfoClass('BmpServers.BmpServer.InitialRefreshDelay',
            False, 
            [
            _MetaInfoClassMember('delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Delay in seconds before sending Refresh
                request to Peers
                ''',
                'delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('spread', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Spread over which to send initial Refresh
                request to Peers
                ''',
                'spread',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'initial-refresh-delay',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'BmpServers.BmpServer.HostPort' : {
        'meta_info' : _MetaInfoClass('BmpServers.BmpServer.HostPort',
            False, 
            [
            _MetaInfoClassMember('host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the BMP server(accepts IPv4/IPv6
                Address format too)
                ''',
                'host',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Port Number of listening BMP server
                ''',
                'port',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'host-port',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'BmpServers.BmpServer.RouteMonitoring' : {
        'meta_info' : _MetaInfoClass('BmpServers.BmpServer.RouteMonitoring',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'BmpRouteDirectionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BmpRouteDirectionEnum', 
                [], [], 
                '''                Specify if the routes should be picked up at
                inbound
                or outbound direction
                ''',
                'direction',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('policy', REFERENCE_ENUM_CLASS, 'BmpPolicySelectEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BmpPolicySelectEnum', 
                [], [], 
                '''                Specify if the routes packed in update
                messages should be
                before or after the
                application of route-policy
                ''',
                'policy',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'route-monitoring',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'BmpServers.BmpServer.Tos' : {
        'meta_info' : _MetaInfoClass('BmpServers.BmpServer.Tos',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'BgpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpTosEnum', 
                [], [], 
                '''                Set type of service
                ''',
                'type',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('value', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TOS value to set
                ''',
                'value',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False, [
                    _MetaInfoClassMember('value', REFERENCE_ENUM_CLASS, 'BgpPrecedenceDscpEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_datatypes', 'BgpPrecedenceDscpEnum', 
                        [], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                    _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        TOS value to set
                        ''',
                        'value',
                        'Cisco-IOS-XR-ipv4-bgp-cfg', False),
                ]),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'BmpServers.BmpServer' : {
        'meta_info' : _MetaInfoClass('BmpServers.BmpServer',
            False, 
            [
            _MetaInfoClassMember('server-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '9')], [], 
                '''                BMP Server ID
                ''',
                'server_id',
                'Cisco-IOS-XR-ipv4-bgp-cfg', True),
            _MetaInfoClassMember('bmptcp-keep-alive', ATTRIBUTE, 'int' , None, None, 
                [('0', '7200')], [], 
                '''                configure TCP keep alives to be exchanged
                between client and server. Default=1000
                ''',
                'bmptcp_keep_alive',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('bmptcp-maximum-segment-size', ATTRIBUTE, 'int' , None, None, 
                [('68', '10000')], [], 
                '''                configure TCP maximum segment size.
                Default=16384.
                ''',
                'bmptcp_maximum_segment_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('create', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                BMP Server Creation
                ''',
                'create',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String to describe the BMP server
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('flapping-delay', ATTRIBUTE, 'int' , None, None, 
                [('60', '3600')], [], 
                '''                Delay in connecting to BMP Server after a flap
                had been detected.
                ''',
                'flapping_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('host-port', REFERENCE_CLASS, 'HostPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BmpServers.BmpServer.HostPort', 
                [], [], 
                '''                Configure Host Name/Address and Port for BMP
                Server
                ''',
                'host_port',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('initial-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Initial connect delay in seconds in sending
                updates
                ''',
                'initial_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('initial-refresh-delay', REFERENCE_CLASS, 'InitialRefreshDelay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BmpServers.BmpServer.InitialRefreshDelay', 
                [], [], 
                '''                Initial refresh to generate BGP updates
                ''',
                'initial_refresh_delay',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('maximum-buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Range in MegaBytes for the maximum buffer size
                of BMP message queue.
                The maximum buf-size is
                20% and default buf-size is 15% of the
                platform
                virtual memory max-limit (aka rlimit)
                . Please run show bgp process
                performance-statistics
                to see the individual
                values. Unit is in Megabytes
                ''',
                'maximum_buffer_size',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('route-monitoring', REFERENCE_CLASS, 'RouteMonitoring' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BmpServers.BmpServer.RouteMonitoring', 
                [], [], 
                '''                Enable Route Monitoring capability for the BMP
                servers.
                BGP update messages messages will be
                regenrated with a table walk
                
                ''',
                'route_monitoring',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE to shutdown the BMP Server ConnectionFALSE
                to bring back the BMP Server Connection
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('status-report-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '3600')], [], 
                '''                Stats reporting period for BMP server
                ''',
                'status_report_interval',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BmpServers.BmpServer.Tos', 
                [], [], 
                '''                TOS (Type Of Service)
                ''',
                'tos',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('update-source-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Select an interface to configure
                ''',
                'update_source_interface',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF for BMP Server
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-server',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
    'BmpServers' : {
        'meta_info' : _MetaInfoClass('BmpServers',
            False, 
            [
            _MetaInfoClassMember('bmp-server', REFERENCE_LIST, 'BmpServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg', 'BmpServers.BmpServer', 
                [], [], 
                '''                A particular BMP server
                ''',
                'bmp_server',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bmp-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_bgp_cfg'
        ),
    },
}
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses.AggregateAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes.EigrpRoute']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks.SourcedNetwork']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes.OspfRoute']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Mvpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ebgp']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Eibgp']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Ibgp']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AggregateAddresses']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Dampening']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.RipRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LispRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.StaticRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.Distance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.LabelMode']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.EigrpRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SourcedNetworks']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.ConnectedRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AllocateLabel']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.AdditionalPathsSelection']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.OspfRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.MobileRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf.SubscriberRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs.VrfGlobalAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces.MplsActivatedInterface']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.RouteDistinguisher']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.VrfGlobalAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.MplsActivatedInterfaces']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.GlobalTimers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.Bfd']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.SendSocketBufferSizes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal.ReceiveSocketBufferSizes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.Import_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs.VrfNeighborAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates.BmpActivate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.VrfNeighborAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.BmpActivates']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.RemoteAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.LocalAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Password']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.AdvertisementInterval']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.NeighborClusterId']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tcpmss']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Tos']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.UpdateInFiltering']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogOut']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.ReceiveBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.MsgLogIn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.SendBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Timers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.Keychain']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor.GracefulMaintenance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AigpCostCommunity']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDisable']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.MaximumPrefixes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPathInbound']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseDefImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.NeighborAfLongLivedGracefulRestartStaleTime']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SiteOfOrigin']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.Import_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.DefaultOriginate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.SoftReconfiguration']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseLocalV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.RemovePrivateAsEntireAsPath']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf.AdvertiseVrfImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs.VrfNeighborAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates.BmpActivate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.VrfNeighborAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.BmpActivates']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.RemoteAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.LocalAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Password']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.AdvertisementInterval']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.NeighborClusterId']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tcpmss']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Tos']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.UpdateInFiltering']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogOut']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.ReceiveBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.MsgLogIn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.SendBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Timers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.Keychain']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength.GracefulMaintenance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighbor']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors.VrfNeighborPrefixLength']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfGlobal']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf.VrfNeighbors']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs.Vrf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AigpCostCommunity']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDisable']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.MaximumPrefixes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.Import_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.DefaultOriginate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.SoftReconfiguration']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseLocalV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs.NeighborAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates.BmpActivate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering.UpdateInFilteringMessageBuffers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceLocalPreference']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance.GracefulMaintenanceAsPrepends']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.BmpActivates']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.RemoteAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.LocalAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Password']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.AdvertisementInterval']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.NeighborClusterId']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tcpmss']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Tos']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.UpdateInFiltering']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogOut']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.ReceiveBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.MsgLogIn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.SendBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Timers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.Keychain']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor.GracefulMaintenance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AigpCostCommunity']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDisable']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.MaximumPrefixes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPathInbound']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseDefImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.NeighborAfLongLivedGracefulRestartStaleTime']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.Import_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.DefaultOriginate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.SoftReconfiguration']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseLocalV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.RemovePrivateAsEntireAsPath']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf.AdvertiseVrfImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs.NeighborAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates.BmpActivate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering.UpdateInFilteringMessageBuffers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceLocalPreference']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance.GracefulMaintenanceAsPrepends']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.BmpActivates']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.RemoteAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.LocalAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Password']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.AdvertisementInterval']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.NeighborClusterId']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tcpmss']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Tos']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.UpdateInFiltering']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogOut']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.ReceiveBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.MsgLogIn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.SendBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Timers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.Keychain']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength.GracefulMaintenance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors.NeighborPrefixLength']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AigpCostCommunity']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDisable']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.MaximumPrefixes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPathInbound']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseDefImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.NeighborAfLongLivedGracefulRestartStaleTime']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SiteOfOrigin']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.Import_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.DefaultOriginate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.SoftReconfiguration']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseLocalV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.RemovePrivateAsEntireAsPath']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf.AdvertiseVrfImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs.NeighborGroupAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates.BmpActivate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborGroupAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.BmpActivates']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.RemoteAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.LocalAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Password']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.AdvertisementInterval']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.NeighborClusterId']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tcpmss']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Tos']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.UpdateInFiltering']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogOut']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.ReceiveBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.MsgLogIn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.SendBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Timers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.Keychain']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup.GracefulMaintenance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups.NeighborGroup']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AigpCostCommunity']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDisable']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.MaximumPrefixes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPathInbound']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseDefImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalL2Vpnevpn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.NeighborAfLongLivedGracefulRestartStaleTime']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SiteOfOrigin']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.Import_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.DefaultOriginate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.SoftReconfiguration']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV6']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseLocalV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.RemovePrivateAsEntireAsPath']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf.AdvertiseVrfImpDisableV4']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs.AfGroupAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup.AfGroupAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups.AfGroup']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates.BmpActivate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering.UpdateInFilteringMessageBuffers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceLocalPreference']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance.GracefulMaintenanceAsPrepends']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.BmpActivates']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.RemoteAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.LocalAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Password']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.AdvertisementInterval']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.NeighborClusterId']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tcpmss']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Tos']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.UpdateInFiltering']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogOut']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.ReceiveBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.MsgLogIn']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.SendBufferSize']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Timers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.Keychain']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup.GracefulMaintenance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups.SessionGroup']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.Neighbors']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.NeighborGroups']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.AfGroups']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity.SessionGroups']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers.Peer']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague.Peers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer.Transport']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers.RpkiServer']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases.As_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup.Ases']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups.AsListGroup']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses.ConfederationPeerAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters.AttributeFilter']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup.AttributeFilters']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups.AttributeFilterGroup']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes.IsisRoute']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll.LabelMode']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes.ApplicationRoute']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Number']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr.Ipv4Address']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs.DisableClusterClientToClientRr']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses.AggregateAddress']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes.EigrpRoute']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks.SourcedNetwork']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes.OspfRoute']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.IsisRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DomainDistinguisher']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.VrfAll']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ApplicationRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.DisableClusterClientToClientRrs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelDelay']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ebgp']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Eibgp']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RetainRt']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Ibgp']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ImportDelay']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AggregateAddresses']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Dampening']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.RipRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LispRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.StaticRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.Distance']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.LabelMode']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.EigrpRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SourcedNetworks']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.ConnectedRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AllocateLabel']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.AdditionalPathsSelection']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.OspfRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.MobileRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf.SubscriberRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs.GlobalAf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes.RpkiStaticRoute']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces.MplsActivatedInterface']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ClusterId']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.WriteLimit']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.UpdateDelay']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsLeague']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiServers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AsListGroups']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Limits']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationDomain']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ConfederationPeerAses']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.AttributeFilterGroups']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalGracefulMaintenanceActivate']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalAfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.RpkiStaticRoutes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.MplsActivatedInterfaces']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.GlobalTimers']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.Bfd']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.SendSocketBufferSizes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_.ReceiveSocketBufferSizes']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.BgpEntity']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf.Global_']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.Vrfs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs.DefaultVrf']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs.FourByteAs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs.FourByteAs']['meta_info'].parent =_meta_table['Bgp.Instance.InstanceAs']['meta_info']
_meta_table['Bgp.Instance.InstanceAs']['meta_info'].parent =_meta_table['Bgp.Instance']['meta_info']
_meta_table['Bgp.Instance']['meta_info'].parent =_meta_table['Bgp']['meta_info']
_meta_table['BmpServers.BmpServer.InitialRefreshDelay']['meta_info'].parent =_meta_table['BmpServers.BmpServer']['meta_info']
_meta_table['BmpServers.BmpServer.HostPort']['meta_info'].parent =_meta_table['BmpServers.BmpServer']['meta_info']
_meta_table['BmpServers.BmpServer.RouteMonitoring']['meta_info'].parent =_meta_table['BmpServers.BmpServer']['meta_info']
_meta_table['BmpServers.BmpServer.Tos']['meta_info'].parent =_meta_table['BmpServers.BmpServer']['meta_info']
_meta_table['BmpServers.BmpServer']['meta_info'].parent =_meta_table['BmpServers']['meta_info']
