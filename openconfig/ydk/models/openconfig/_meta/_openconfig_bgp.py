


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Bgp.Global_.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.Config',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local autonomous system number of the router.  Uses
                the 32-bit as-number type from the model in RFC 6991.
                ''',
                'as_',
                'openconfig-bgp', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router id of the router, expressed as an
                32-bit value, IPv4 address.
                ''',
                'router_id',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.State',
            False, 
            [
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local autonomous system number of the router.  Uses
                the 32-bit as-number type from the model in RFC 6991.
                ''',
                'as_',
                'openconfig-bgp', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router id of the router, expressed as an
                32-bit value, IPv4 address.
                ''',
                'router_id',
                'openconfig-bgp', False),
            _MetaInfoClassMember('total-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of BGP paths within the context
                ''',
                'total_paths',
                'openconfig-bgp', False),
            _MetaInfoClassMember('total-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                
                ''',
                'total_prefixes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.RouteSelectionOptions.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.RouteSelectionOptions.Config',
            False, 
            [
            _MetaInfoClassMember('advertise-inactive-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise inactive routes to external peers.  The
                default is to only advertise active routes.
                ''',
                'advertise_inactive_routes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('always-compare-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Compare multi-exit discriminator (MED) value from
                different ASes when selecting the best route.  The
                default behavior is to only compare MEDs for paths
                received from the same AS.
                ''',
                'always_compare_med',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enable-aigp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable sending / receiving accumulated IGP
                attribute in routing updates
                ''',
                'enable_aigp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('external-compare-router-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When comparing similar routes received from external
                BGP peers, use the router-id as a criterion to select
                the active path.
                ''',
                'external_compare_router_id',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-as-path-length', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the AS path length when selecting the best path.
                The default is to use the AS path length and prefer paths
                with shorter length.
                ''',
                'ignore_as_path_length',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-next-hop-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the IGP metric to the next-hop when calculating
                BGP best-path. The default is to select the route for
                which the metric to the next-hop is lowest
                ''',
                'ignore_next_hop_igp_metric',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.RouteSelectionOptions.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.RouteSelectionOptions.State',
            False, 
            [
            _MetaInfoClassMember('advertise-inactive-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise inactive routes to external peers.  The
                default is to only advertise active routes.
                ''',
                'advertise_inactive_routes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('always-compare-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Compare multi-exit discriminator (MED) value from
                different ASes when selecting the best route.  The
                default behavior is to only compare MEDs for paths
                received from the same AS.
                ''',
                'always_compare_med',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enable-aigp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable sending / receiving accumulated IGP
                attribute in routing updates
                ''',
                'enable_aigp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('external-compare-router-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When comparing similar routes received from external
                BGP peers, use the router-id as a criterion to select
                the active path.
                ''',
                'external_compare_router_id',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-as-path-length', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the AS path length when selecting the best path.
                The default is to use the AS path length and prefer paths
                with shorter length.
                ''',
                'ignore_as_path_length',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-next-hop-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the IGP metric to the next-hop when calculating
                BGP best-path. The default is to select the route for
                which the metric to the next-hop is lowest
                ''',
                'ignore_next_hop_igp_metric',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.RouteSelectionOptions' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.RouteSelectionOptions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.RouteSelectionOptions.Config', 
                [], [], 
                '''                Configuration parameters relating to route selection
                options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.RouteSelectionOptions.State', 
                [], [], 
                '''                State information for the route selection options
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'route-selection-options',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.DefaultRouteDistance.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.DefaultRouteDistance.Config',
            False, 
            [
            _MetaInfoClassMember('external-route-distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Administrative distance for routes learned from external
                BGP (eBGP).
                ''',
                'external_route_distance',
                'openconfig-bgp', False),
            _MetaInfoClassMember('internal-route-distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Administrative distance for routes learned from internal
                BGP (iBGP).
                ''',
                'internal_route_distance',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.DefaultRouteDistance.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.DefaultRouteDistance.State',
            False, 
            [
            _MetaInfoClassMember('external-route-distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Administrative distance for routes learned from external
                BGP (eBGP).
                ''',
                'external_route_distance',
                'openconfig-bgp', False),
            _MetaInfoClassMember('internal-route-distance', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Administrative distance for routes learned from internal
                BGP (iBGP).
                ''',
                'internal_route_distance',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.DefaultRouteDistance' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.DefaultRouteDistance',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.DefaultRouteDistance.Config', 
                [], [], 
                '''                Configuration parameters relating to the default route
                distance
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.DefaultRouteDistance.State', 
                [], [], 
                '''                State information relating to the default route distance
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'default-route-distance',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.Confederation.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.Confederation.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When this leaf is set to true it indicates that
                the local-AS is part of a BGP confederation
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Confederation identifier for the autonomous system.
                ''',
                'identifier',
                'openconfig-bgp', False),
            _MetaInfoClassMember('member-as', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote autonomous systems that are to be treated
                as part of the local confederation.
                ''',
                'member_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.Confederation.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.Confederation.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When this leaf is set to true it indicates that
                the local-AS is part of a BGP confederation
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Confederation identifier for the autonomous system.
                ''',
                'identifier',
                'openconfig-bgp', False),
            _MetaInfoClassMember('member-as', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote autonomous systems that are to be treated
                as part of the local confederation.
                ''',
                'member_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.Confederation' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.Confederation',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.Confederation.Config', 
                [], [], 
                '''                Configuration parameters relating to BGP confederations
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.Confederation.State', 
                [], [], 
                '''                State information relating to the BGP confederations
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'confederation',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.Ebgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.Ebgp.Config',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.Ebgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.Ebgp.State',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.Ebgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.Ebgp.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.Ebgp.State', 
                [], [], 
                '''                State information relating to eBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.Ibgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.Ibgp.Config',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.Ibgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.Ibgp.State',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths.Ibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths.Ibgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.Ibgp.Config', 
                [], [], 
                '''                Configuration parameters relating to iBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.Ibgp.State', 
                [], [], 
                '''                State information relating to iBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ibgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.UseMultiplePaths' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.UseMultiplePaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.Config', 
                [], [], 
                '''                Configuration parameters relating to multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.Ebgp', 
                [], [], 
                '''                Multipath parameters for eBGP
                ''',
                'ebgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ibgp', REFERENCE_CLASS, 'Ibgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.Ibgp', 
                [], [], 
                '''                Multipath parameters for iBGP
                ''',
                'ibgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths.State', 
                [], [], 
                '''                State parameters relating to multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'use-multiple-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.GracefulRestart.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.GracefulRestart.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable the graceful-restart capability.
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('helper-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable graceful-restart in helper mode only. When this
                leaf is set, the local system does not retain forwarding
                its own state during a restart, but supports procedures
                for the receiving speaker, as defined in RFC4724.
                ''',
                'helper_only',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                Estimated time (in seconds) for the local BGP speaker to
                restart a session. This value is advertise in the graceful
                restart BGP capability.  This is a 12-bit value, referred to
                as Restart Time in RFC4724.  Per RFC4724, the suggested
                default value is <= the hold-time value.
                ''',
                'restart_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('stale-routes-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                An upper-bound on the time thate stale routes will be
                retained by a router after a session is restarted. If an
                End-of-RIB (EOR) marker is received prior to this timer
                expiring stale-routes will be flushed upon its receipt - if
                no EOR is received, then when this timer expires stale paths
                will be purged. This timer is referred to as the
                Selection_Deferral_Timer in RFC4724
                ''',
                'stale_routes_time',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.GracefulRestart.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.GracefulRestart.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable the graceful-restart capability.
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('helper-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable graceful-restart in helper mode only. When this
                leaf is set, the local system does not retain forwarding
                its own state during a restart, but supports procedures
                for the receiving speaker, as defined in RFC4724.
                ''',
                'helper_only',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                Estimated time (in seconds) for the local BGP speaker to
                restart a session. This value is advertise in the graceful
                restart BGP capability.  This is a 12-bit value, referred to
                as Restart Time in RFC4724.  Per RFC4724, the suggested
                default value is <= the hold-time value.
                ''',
                'restart_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('stale-routes-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                An upper-bound on the time thate stale routes will be
                retained by a router after a session is restarted. If an
                End-of-RIB (EOR) marker is received prior to this timer
                expiring stale-routes will be flushed upon its receipt - if
                no EOR is received, then when this timer expires stale paths
                will be purged. This timer is referred to as the
                Selection_Deferral_Timer in RFC4724
                ''',
                'stale_routes_time',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.GracefulRestart.Config', 
                [], [], 
                '''                Configuration parameters relating to graceful-restart
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.GracefulRestart.State', 
                [], [], 
                '''                State information associated with graceful-restart
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'graceful-restart',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether graceful-restart is enabled for
                this AFI-SAFI
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether graceful-restart is enabled for
                this AFI-SAFI
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.Config', 
                [], [], 
                '''                Configuration options for BGP graceful-restart
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.State', 
                [], [], 
                '''                State information for BGP graceful-restart
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'graceful-restart',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Config',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                AFI,SAFI
                ''',
                'afi_safi_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the IPv4 Unicast AFI,SAFI is
                enabled for the neighbour or group
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.State',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                AFI,SAFI
                ''',
                'afi_safi_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the IPv4 Unicast AFI,SAFI is
                enabled for the neighbour or group
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('total-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of BGP paths within the context
                ''',
                'total_paths',
                'openconfig-bgp', False),
            _MetaInfoClassMember('total-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                
                ''',
                'total_prefixes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.Config',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.State',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.Config', 
                [], [], 
                '''                Policy configuration data.
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.State', 
                [], [], 
                '''                Operational state for routing policy
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'apply-policy',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.Config',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.State',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.Config', 
                [], [], 
                '''                Configuration parameters for common IPv4 and IPv6 unicast
                AFI-SAFI options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.State', 
                [], [], 
                '''                State information for common IPv4 and IPv6 unicast
                parameters
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.Config',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.State',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.Config', 
                [], [], 
                '''                Configuration parameters for common IPv4 and IPv6 unicast
                AFI-SAFI options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.State', 
                [], [], 
                '''                State information for common IPv4 and IPv6 unicast
                parameters
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv4-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv6-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv4-multicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv6-multicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l2vpn-vpls',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l2vpn-evpn',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config',
            False, 
            [
            _MetaInfoClassMember('advertise-inactive-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise inactive routes to external peers.  The
                default is to only advertise active routes.
                ''',
                'advertise_inactive_routes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('always-compare-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Compare multi-exit discriminator (MED) value from
                different ASes when selecting the best route.  The
                default behavior is to only compare MEDs for paths
                received from the same AS.
                ''',
                'always_compare_med',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enable-aigp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable sending / receiving accumulated IGP
                attribute in routing updates
                ''',
                'enable_aigp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('external-compare-router-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When comparing similar routes received from external
                BGP peers, use the router-id as a criterion to select
                the active path.
                ''',
                'external_compare_router_id',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-as-path-length', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the AS path length when selecting the best path.
                The default is to use the AS path length and prefer paths
                with shorter length.
                ''',
                'ignore_as_path_length',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-next-hop-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the IGP metric to the next-hop when calculating
                BGP best-path. The default is to select the route for
                which the metric to the next-hop is lowest
                ''',
                'ignore_next_hop_igp_metric',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State',
            False, 
            [
            _MetaInfoClassMember('advertise-inactive-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise inactive routes to external peers.  The
                default is to only advertise active routes.
                ''',
                'advertise_inactive_routes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('always-compare-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Compare multi-exit discriminator (MED) value from
                different ASes when selecting the best route.  The
                default behavior is to only compare MEDs for paths
                received from the same AS.
                ''',
                'always_compare_med',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enable-aigp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable sending / receiving accumulated IGP
                attribute in routing updates
                ''',
                'enable_aigp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('external-compare-router-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When comparing similar routes received from external
                BGP peers, use the router-id as a criterion to select
                the active path.
                ''',
                'external_compare_router_id',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-as-path-length', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the AS path length when selecting the best path.
                The default is to use the AS path length and prefer paths
                with shorter length.
                ''',
                'ignore_as_path_length',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-next-hop-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the IGP metric to the next-hop when calculating
                BGP best-path. The default is to select the route for
                which the metric to the next-hop is lowest
                ''',
                'ignore_next_hop_igp_metric',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config', 
                [], [], 
                '''                Configuration parameters relating to route selection
                options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State', 
                [], [], 
                '''                State information for the route selection options
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'route-selection-options',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State', 
                [], [], 
                '''                State information relating to eBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config', 
                [], [], 
                '''                Configuration parameters relating to iBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State', 
                [], [], 
                '''                State information relating to iBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ibgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Config', 
                [], [], 
                '''                Configuration parameters relating to multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp', 
                [], [], 
                '''                Multipath parameters for eBGP
                ''',
                'ebgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ibgp', REFERENCE_CLASS, 'Ibgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp', 
                [], [], 
                '''                Multipath parameters for iBGP
                ''',
                'ibgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.State', 
                [], [], 
                '''                State parameters relating to multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'use-multiple-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis.AfiSafi' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis.AfiSafi',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                Reference to the AFI-SAFI name used as a key
                for the AFI-SAFI list
                ''',
                'afi_safi_name',
                'openconfig-bgp', True),
            _MetaInfoClassMember('apply-policy', REFERENCE_CLASS, 'ApplyPolicy' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy', 
                [], [], 
                '''                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                ''',
                'apply_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Config', 
                [], [], 
                '''                Configuration parameters for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart', 
                [], [], 
                '''                Parameters relating to BGP graceful-restart
                ''',
                'graceful_restart',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv4-labelled-unicast', REFERENCE_CLASS, 'Ipv4LabelledUnicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast', 
                [], [], 
                '''                IPv4 Labelled Unicast configuration options
                ''',
                'ipv4_labelled_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv4-unicast', REFERENCE_CLASS, 'Ipv4Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast', 
                [], [], 
                '''                IPv4 unicast configuration options
                ''',
                'ipv4_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv6-labelled-unicast', REFERENCE_CLASS, 'Ipv6LabelledUnicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast', 
                [], [], 
                '''                IPv6 Labelled Unicast configuration options
                ''',
                'ipv6_labelled_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv6-unicast', REFERENCE_CLASS, 'Ipv6Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast', 
                [], [], 
                '''                IPv6 unicast configuration options
                ''',
                'ipv6_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l2vpn-evpn', REFERENCE_CLASS, 'L2VpnEvpn' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn', 
                [], [], 
                '''                BGP EVPN configuration options
                ''',
                'l2vpn_evpn',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l2vpn-vpls', REFERENCE_CLASS, 'L2VpnVpls' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls', 
                [], [], 
                '''                BGP-signalled VPLS configuration options
                ''',
                'l2vpn_vpls',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv4-multicast', REFERENCE_CLASS, 'L3VpnIpv4Multicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast', 
                [], [], 
                '''                Multicast IPv4 L3VPN configuration options
                ''',
                'l3vpn_ipv4_multicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv4-unicast', REFERENCE_CLASS, 'L3VpnIpv4Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast', 
                [], [], 
                '''                Unicast IPv4 L3VPN configuration options
                ''',
                'l3vpn_ipv4_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv6-multicast', REFERENCE_CLASS, 'L3VpnIpv6Multicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast', 
                [], [], 
                '''                Multicast IPv6 L3VPN configuration options
                ''',
                'l3vpn_ipv6_multicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv6-unicast', REFERENCE_CLASS, 'L3VpnIpv6Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast', 
                [], [], 
                '''                Unicast IPv6 L3VPN configuration options
                ''',
                'l3vpn_ipv6_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-selection-options', REFERENCE_CLASS, 'RouteSelectionOptions' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions', 
                [], [], 
                '''                Parameters relating to options for route selection
                ''',
                'route_selection_options',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.State', 
                [], [], 
                '''                State information relating to the AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            _MetaInfoClassMember('use-multiple-paths', REFERENCE_CLASS, 'UseMultiplePaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths', 
                [], [], 
                '''                Parameters related to the use of multiple paths for the
                same NLRI
                ''',
                'use_multiple_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'afi-safi',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.AfiSafis' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.AfiSafis',
            False, 
            [
            _MetaInfoClassMember('afi-safi', REFERENCE_LIST, 'AfiSafi' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis.AfiSafi', 
                [], [], 
                '''                AFI,SAFI configuration available for the
                neighbour or group
                ''',
                'afi_safi',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'afi-safis',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.ApplyPolicy.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.ApplyPolicy.Config',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.ApplyPolicy.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.ApplyPolicy.State',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_.ApplyPolicy' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_.ApplyPolicy',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.ApplyPolicy.Config', 
                [], [], 
                '''                Policy configuration data.
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.ApplyPolicy.State', 
                [], [], 
                '''                Operational state for routing policy
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'apply-policy',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Global_' : {
        'meta_info' : _MetaInfoClass('Bgp.Global_',
            False, 
            [
            _MetaInfoClassMember('afi-safis', REFERENCE_CLASS, 'AfiSafis' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.AfiSafis', 
                [], [], 
                '''                Address family specific configuration
                ''',
                'afi_safis',
                'openconfig-bgp', False),
            _MetaInfoClassMember('apply-policy', REFERENCE_CLASS, 'ApplyPolicy' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.ApplyPolicy', 
                [], [], 
                '''                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                ''',
                'apply_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('confederation', REFERENCE_CLASS, 'Confederation' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.Confederation', 
                [], [], 
                '''                Parameters indicating whether the local system acts as part
                of a BGP confederation
                ''',
                'confederation',
                'openconfig-bgp', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.Config', 
                [], [], 
                '''                Configuration parameters relating to the global BGP router
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-route-distance', REFERENCE_CLASS, 'DefaultRouteDistance' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.DefaultRouteDistance', 
                [], [], 
                '''                Administrative distance (or preference) assigned to
                routes received from different sources
                (external, internal, and local).
                ''',
                'default_route_distance',
                'openconfig-bgp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.GracefulRestart', 
                [], [], 
                '''                Parameters relating the graceful restart mechanism for BGP
                ''',
                'graceful_restart',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-selection-options', REFERENCE_CLASS, 'RouteSelectionOptions' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.RouteSelectionOptions', 
                [], [], 
                '''                Parameters relating to options for route selection
                ''',
                'route_selection_options',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.State', 
                [], [], 
                '''                State information relating to the global BGP router
                ''',
                'state',
                'openconfig-bgp', False),
            _MetaInfoClassMember('use-multiple-paths', REFERENCE_CLASS, 'UseMultiplePaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_.UseMultiplePaths', 
                [], [], 
                '''                Parameters related to the use of multiple paths for the
                same NLRI
                ''',
                'use_multiple_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'global',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.Config',
            False, 
            [
            _MetaInfoClassMember('auth-password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configures an MD5 authentication password for use with
                neighboring devices.
                ''',
                'auth_password',
                'openconfig-bgp', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An optional textual description (intended primarily for use
                with a peer or group
                ''',
                'description',
                'openconfig-bgp', False),
            _MetaInfoClassMember('local-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local autonomous system number that is to be used
                when establishing sessions with the remote peer or peer
                group, if this differs from the global BGP router
                autonomous system number.
                ''',
                'local_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the BGP peer, either in IPv4 or IPv6
                ''',
                'neighbor_address',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the BGP peer, either in IPv4 or IPv6
                        ''',
                        'neighbor_address',
                        'openconfig-bgp', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the BGP peer, either in IPv4 or IPv6
                        ''',
                        'neighbor_address',
                        'openconfig-bgp', False),
                ]),
            _MetaInfoClassMember('peer-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the peer.
                ''',
                'peer_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The peer-group with which this neighbor is associated
                ''',
                'peer_group',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-type', REFERENCE_ENUM_CLASS, 'PeerTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'PeerTypeEnum', 
                [], [], 
                '''                Explicitly designate the peer or peer group as internal
                (iBGP) or external (eBGP).
                ''',
                'peer_type',
                'openconfig-bgp', False),
            _MetaInfoClassMember('remove-private-as', REFERENCE_ENUM_CLASS, 'RemovePrivateAsOptionEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'RemovePrivateAsOptionEnum', 
                [], [], 
                '''                Remove private AS numbers from updates sent to peers.
                ''',
                'remove_private_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-flap-damping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable route flap damping.
                ''',
                'route_flap_damping',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-community', REFERENCE_ENUM_CLASS, 'CommunityTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'CommunityTypeEnum', 
                [], [], 
                '''                Specify which types of community should be sent to the
                neighbor or group. The default is to not send the
                community attribute
                ''',
                'send_community',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.State.Messages.Sent' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.State.Messages.Sent',
            False, 
            [
            _MetaInfoClassMember('NOTIFICATION', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of BGP NOTIFICATION messages indicating an
                error condition has occurred exchanged.
                ''',
                'notification',
                'openconfig-bgp', False),
            _MetaInfoClassMember('UPDATE', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of BGP UPDATE messages announcing, withdrawing
                or modifying paths exchanged.
                ''',
                'update',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'sent',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.State.Messages.Received' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.State.Messages.Received',
            False, 
            [
            _MetaInfoClassMember('NOTIFICATION', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of BGP NOTIFICATION messages indicating an
                error condition has occurred exchanged.
                ''',
                'notification',
                'openconfig-bgp', False),
            _MetaInfoClassMember('UPDATE', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of BGP UPDATE messages announcing, withdrawing
                or modifying paths exchanged.
                ''',
                'update',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'received',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.State.Messages' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.State.Messages',
            False, 
            [
            _MetaInfoClassMember('received', REFERENCE_CLASS, 'Received' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.State.Messages.Received', 
                [], [], 
                '''                Counters for BGP messages received from the neighbor
                ''',
                'received',
                'openconfig-bgp', False),
            _MetaInfoClassMember('sent', REFERENCE_CLASS, 'Sent' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.State.Messages.Sent', 
                [], [], 
                '''                Counters relating to BGP messages sent to the neighbor
                ''',
                'sent',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'messages',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.State.Queues' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.State.Queues',
            False, 
            [
            _MetaInfoClassMember('input', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of messages received from the peer currently
                queued
                ''',
                'input',
                'openconfig-bgp', False),
            _MetaInfoClassMember('output', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of messages queued to be sent to the peer
                ''',
                'output',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'queues',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.State.SessionStateEnum' : _MetaInfoEnum('SessionStateEnum', 'ydk.models.openconfig.openconfig_bgp',
        {
            'IDLE':'IDLE',
            'CONNECT':'CONNECT',
            'ACTIVE':'ACTIVE',
            'OPENSENT':'OPENSENT',
            'OPENCONFIRM':'OPENCONFIRM',
            'ESTABLISHED':'ESTABLISHED',
        }, 'openconfig-bgp-operational', _yang_ns._namespaces['openconfig-bgp-operational']),
    'Bgp.Neighbors.Neighbor.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.State',
            False, 
            [
            _MetaInfoClassMember('auth-password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configures an MD5 authentication password for use with
                neighboring devices.
                ''',
                'auth_password',
                'openconfig-bgp', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An optional textual description (intended primarily for use
                with a peer or group
                ''',
                'description',
                'openconfig-bgp', False),
            _MetaInfoClassMember('local-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local autonomous system number that is to be used
                when establishing sessions with the remote peer or peer
                group, if this differs from the global BGP router
                autonomous system number.
                ''',
                'local_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('messages', REFERENCE_CLASS, 'Messages' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.State.Messages', 
                [], [], 
                '''                Counters for BGP messages sent and received from the
                neighbor
                ''',
                'messages',
                'openconfig-bgp', False),
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the BGP peer, either in IPv4 or IPv6
                ''',
                'neighbor_address',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the BGP peer, either in IPv4 or IPv6
                        ''',
                        'neighbor_address',
                        'openconfig-bgp', False),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the BGP peer, either in IPv4 or IPv6
                        ''',
                        'neighbor_address',
                        'openconfig-bgp', False),
                ]),
            _MetaInfoClassMember('peer-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the peer.
                ''',
                'peer_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-group', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The peer-group with which this neighbor is associated
                ''',
                'peer_group',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-type', REFERENCE_ENUM_CLASS, 'PeerTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'PeerTypeEnum', 
                [], [], 
                '''                Explicitly designate the peer or peer group as internal
                (iBGP) or external (eBGP).
                ''',
                'peer_type',
                'openconfig-bgp', False),
            _MetaInfoClassMember('queues', REFERENCE_CLASS, 'Queues' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.State.Queues', 
                [], [], 
                '''                Counters related to queued messages associated with the
                BGP neighbor
                ''',
                'queues',
                'openconfig-bgp', False),
            _MetaInfoClassMember('remove-private-as', REFERENCE_ENUM_CLASS, 'RemovePrivateAsOptionEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'RemovePrivateAsOptionEnum', 
                [], [], 
                '''                Remove private AS numbers from updates sent to peers.
                ''',
                'remove_private_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-flap-damping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable route flap damping.
                ''',
                'route_flap_damping',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-community', REFERENCE_ENUM_CLASS, 'CommunityTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'CommunityTypeEnum', 
                [], [], 
                '''                Specify which types of community should be sent to the
                neighbor or group. The default is to not send the
                community attribute
                ''',
                'send_community',
                'openconfig-bgp', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'SessionStateEnum' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.State.SessionStateEnum', 
                [], [], 
                '''                Operational state of the BGP peer
                ''',
                'session_state',
                'openconfig-bgp', False),
            _MetaInfoClassMember('supported-capabilities', REFERENCE_LEAFLIST, 'BgpCapabilityIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'BgpCapabilityIdentity', 
                [], [], 
                '''                BGP capabilities negotiated as supported with the peer
                ''',
                'supported_capabilities',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.Timers.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.Timers.Config',
            False, 
            [
            _MetaInfoClassMember('connect-retry', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between attempts to establish a
                session with the peer.
                ''',
                'connect_retry',
                'openconfig-bgp', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds that a BGP session will be
                considered active in the absence of keepalive or other
                messages from the peer.  The hold-time is typically
                set to 3x the keepalive-interval.
                ''',
                'hold_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between transmission of keepalive
                messages to the neighbor.  Typically set to 1/3 the
                hold-time.
                ''',
                'keepalive_interval',
                'openconfig-bgp', False),
            _MetaInfoClassMember('minimum-advertisement-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Minimum time which must elapse between subsequent UPDATE
                messages relating to a common set of NLRI being transmitted
                to a peer. This timer is referred to as
                MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
                reduce the number of UPDATE messages transmitted when a
                particular set of NLRI exhibit instability.
                ''',
                'minimum_advertisement_interval',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.Timers.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.Timers.State',
            False, 
            [
            _MetaInfoClassMember('connect-retry', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between attempts to establish a
                session with the peer.
                ''',
                'connect_retry',
                'openconfig-bgp', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds that a BGP session will be
                considered active in the absence of keepalive or other
                messages from the peer.  The hold-time is typically
                set to 3x the keepalive-interval.
                ''',
                'hold_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between transmission of keepalive
                messages to the neighbor.  Typically set to 1/3 the
                hold-time.
                ''',
                'keepalive_interval',
                'openconfig-bgp', False),
            _MetaInfoClassMember('minimum-advertisement-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Minimum time which must elapse between subsequent UPDATE
                messages relating to a common set of NLRI being transmitted
                to a peer. This timer is referred to as
                MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
                reduce the number of UPDATE messages transmitted when a
                particular set of NLRI exhibit instability.
                ''',
                'minimum_advertisement_interval',
                'openconfig-bgp', False),
            _MetaInfoClassMember('negotiated-hold-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                The negotiated hold-time for the BGP session
                ''',
                'negotiated_hold_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('uptime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This timer determines the amount of time since the
                BGP last transitioned in or out of the Established
                state
                ''',
                'uptime',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.Timers',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.Timers.Config', 
                [], [], 
                '''                Configuration parameters relating to timers used for the
                BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.Timers.State', 
                [], [], 
                '''                State information relating to the timers used for the BGP
                neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'timers',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.Transport.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.Transport.Config',
            False, 
            [
            _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the local IP (either IPv4 or IPv6) address to use
                for the session when sending BGP update messages.  This
                may be expressed as either an IP address or reference
                to the name of an interface.
                ''',
                'local_address',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False, [
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                        ]),
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False),
                ]),
            _MetaInfoClassMember('mtu-discovery', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Turns path mtu discovery for BGP TCP sessions on (true)
                or off (false)
                ''',
                'mtu_discovery',
                'openconfig-bgp', False),
            _MetaInfoClassMember('passive-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait for peers to issue requests to open a BGP session,
                rather than initiating sessions from the local router.
                ''',
                'passive_mode',
                'openconfig-bgp', False),
            _MetaInfoClassMember('tcp-mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sets the max segment size for BGP TCP sessions.
                ''',
                'tcp_mss',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.Transport.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.Transport.State',
            False, 
            [
            _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the local IP (either IPv4 or IPv6) address to use
                for the session when sending BGP update messages.  This
                may be expressed as either an IP address or reference
                to the name of an interface.
                ''',
                'local_address',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False, [
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                        ]),
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False),
                ]),
            _MetaInfoClassMember('local-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Local TCP port being used for the TCP session supporting
                the BGP session
                ''',
                'local_port',
                'openconfig-bgp', False),
            _MetaInfoClassMember('mtu-discovery', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Turns path mtu discovery for BGP TCP sessions on (true)
                or off (false)
                ''',
                'mtu_discovery',
                'openconfig-bgp', False),
            _MetaInfoClassMember('passive-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait for peers to issue requests to open a BGP session,
                rather than initiating sessions from the local router.
                ''',
                'passive_mode',
                'openconfig-bgp', False),
            _MetaInfoClassMember('remote-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Remote address to which the BGP session has been
                established
                ''',
                'remote_address',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Remote address to which the BGP session has been
                        established
                        ''',
                        'remote_address',
                        'openconfig-bgp', False),
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Remote address to which the BGP session has been
                        established
                        ''',
                        'remote_address',
                        'openconfig-bgp', False),
                ]),
            _MetaInfoClassMember('remote-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Remote port being used by the peer for the TCP session
                supporting the BGP session
                ''',
                'remote_port',
                'openconfig-bgp', False),
            _MetaInfoClassMember('tcp-mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sets the max segment size for BGP TCP sessions.
                ''',
                'tcp_mss',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.Transport' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.Transport',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.Transport.Config', 
                [], [], 
                '''                Configuration parameters relating to the transport
                session(s) used for the BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.Transport.State', 
                [], [], 
                '''                State information relating to the transport session(s)
                used for the BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'transport',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.ErrorHandling.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.ErrorHandling.Config',
            False, 
            [
            _MetaInfoClassMember('treat-as-withdraw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify whether erroneous UPDATE messages for which the
                NLRI can be extracted are reated as though the NLRI is
                withdrawn - avoiding session reset
                ''',
                'treat_as_withdraw',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.ErrorHandling.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.ErrorHandling.State',
            False, 
            [
            _MetaInfoClassMember('erroneous-update-messages', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of BGP UPDATE messages for which the
                treat-as-withdraw mechanism has been applied based
                on erroneous message contents
                ''',
                'erroneous_update_messages',
                'openconfig-bgp', False),
            _MetaInfoClassMember('treat-as-withdraw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify whether erroneous UPDATE messages for which the
                NLRI can be extracted are reated as though the NLRI is
                withdrawn - avoiding session reset
                ''',
                'treat_as_withdraw',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.ErrorHandling' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.ErrorHandling',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.ErrorHandling.Config', 
                [], [], 
                '''                Configuration parameters enabling or modifying the
                behavior or enhanced error handling mechanisms for the BGP
                neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.ErrorHandling.State', 
                [], [], 
                '''                State information relating to enhanced error handling
                mechanisms for the BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'error-handling',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.LoggingOptions.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.LoggingOptions.Config',
            False, 
            [
            _MetaInfoClassMember('log-neighbor-state-changes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure logging of peer state changes.  Default is
                to enable logging of peer state changes.
                ''',
                'log_neighbor_state_changes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.LoggingOptions.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.LoggingOptions.State',
            False, 
            [
            _MetaInfoClassMember('log-neighbor-state-changes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure logging of peer state changes.  Default is
                to enable logging of peer state changes.
                ''',
                'log_neighbor_state_changes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.LoggingOptions' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.LoggingOptions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.LoggingOptions.Config', 
                [], [], 
                '''                Configuration parameters enabling or modifying logging
                for events relating to the BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.LoggingOptions.State', 
                [], [], 
                '''                State information relating to logging for the BGP neighbor
                or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'logging-options',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.EbgpMultihop.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.EbgpMultihop.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled the referenced group or neighbors are permitted
                to be indirectly connected - including cases where the TTL
                can be decremented between the BGP peers
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('multihop-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time-to-live value to use when packets are sent to the
                referenced group or neighbors and ebgp-multihop is enabled
                ''',
                'multihop_ttl',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.EbgpMultihop.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.EbgpMultihop.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled the referenced group or neighbors are permitted
                to be indirectly connected - including cases where the TTL
                can be decremented between the BGP peers
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('multihop-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time-to-live value to use when packets are sent to the
                referenced group or neighbors and ebgp-multihop is enabled
                ''',
                'multihop_ttl',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.EbgpMultihop.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multihop for the
                BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.EbgpMultihop.State', 
                [], [], 
                '''                State information for eBGP multihop, for the BGP neighbor
                or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp-multihop',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.RouteReflector.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.RouteReflector.Config',
            False, 
            [
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure the neighbor as a route reflector client.
                ''',
                'route_reflector_client',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-reflector-cluster-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                route-reflector cluster id to use when local router is
                configured as a route reflector.  Commonly set at the group
                level, but allows a different cluster
                id to be set for each neighbor.
                ''',
                'route_reflector_cluster_id',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                ]),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.RouteReflector.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.RouteReflector.State',
            False, 
            [
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure the neighbor as a route reflector client.
                ''',
                'route_reflector_client',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-reflector-cluster-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                route-reflector cluster id to use when local router is
                configured as a route reflector.  Commonly set at the group
                level, but allows a different cluster
                id to be set for each neighbor.
                ''',
                'route_reflector_cluster_id',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                ]),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.RouteReflector' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.RouteReflector',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.RouteReflector.Config', 
                [], [], 
                '''                Configuraton parameters relating to route reflection
                for the BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.RouteReflector.State', 
                [], [], 
                '''                State information relating to route reflection for the
                BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'route-reflector',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AsPathOptions.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AsPathOptions.Config',
            False, 
            [
            _MetaInfoClassMember('allow-own-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify the number of occurrences of the local BGP speaker's
                AS that can occur within the AS_PATH before it is rejected.
                ''',
                'allow_own_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('replace-peer-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Replace occurrences of the peer's AS in the AS_PATH
                with the local autonomous system number
                ''',
                'replace_peer_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AsPathOptions.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AsPathOptions.State',
            False, 
            [
            _MetaInfoClassMember('allow-own-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify the number of occurrences of the local BGP speaker's
                AS that can occur within the AS_PATH before it is rejected.
                ''',
                'allow_own_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('replace-peer-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Replace occurrences of the peer's AS in the AS_PATH
                with the local autonomous system number
                ''',
                'replace_peer_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AsPathOptions' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AsPathOptions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AsPathOptions.Config', 
                [], [], 
                '''                Configuration parameters relating to AS_PATH manipulation
                for the BGP peer or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AsPathOptions.State', 
                [], [], 
                '''                State information relating to the AS_PATH manipulation
                mechanisms for the BGP peer or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'as-path-options',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AddPaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AddPaths.Config',
            False, 
            [
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable ability to receive multiple path advertisements
                for an NLRI from the neighbor or group
                ''',
                'receive',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The maximum number of paths to advertise to neighbors
                for a single NLRI
                ''',
                'send_max',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AddPaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AddPaths.State',
            False, 
            [
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable ability to receive multiple path advertisements
                for an NLRI from the neighbor or group
                ''',
                'receive',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The maximum number of paths to advertise to neighbors
                for a single NLRI
                ''',
                'send_max',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AddPaths' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AddPaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AddPaths.Config', 
                [], [], 
                '''                Configuration parameters relating to ADD_PATHS
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AddPaths.State', 
                [], [], 
                '''                State information associated with ADD_PATHS
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'add-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether graceful-restart is enabled for
                this AFI-SAFI
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State',
            False, 
            [
            _MetaInfoClassMember('advertised', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the ability to support
                graceful-restart has been advertised to the peer
                ''',
                'advertised',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether graceful-restart is enabled for
                this AFI-SAFI
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the neighbor advertised the
                ability to support graceful-restart for this AFI-SAFI
                ''',
                'received',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config', 
                [], [], 
                '''                Configuration options for BGP graceful-restart
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State', 
                [], [], 
                '''                State information for BGP graceful-restart
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'graceful-restart',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                AFI,SAFI
                ''',
                'afi_safi_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the IPv4 Unicast AFI,SAFI is
                enabled for the neighbour or group
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes',
            False, 
            [
            _MetaInfoClassMember('installed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of advertised prefixes installed in the
                Loc-RIB
                ''',
                'installed',
                'openconfig-bgp', False),
            _MetaInfoClassMember('received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of prefixes received from the neighbor
                ''',
                'received',
                'openconfig-bgp', False),
            _MetaInfoClassMember('sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of prefixes advertised to the neighbor
                ''',
                'sent',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefixes',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State',
            False, 
            [
            _MetaInfoClassMember('active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This value indicates whether a particular AFI-SAFI has
                been succesfully negotiated with the peer. An AFI-SAFI
                may be enabled in the current running configuration, but a
                session restart may be required in order to negotiate the new
                capability.
                ''',
                'active',
                'openconfig-bgp', False),
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                AFI,SAFI
                ''',
                'afi_safi_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the IPv4 Unicast AFI,SAFI is
                enabled for the neighbour or group
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('prefixes', REFERENCE_CLASS, 'Prefixes' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes', 
                [], [], 
                '''                Prefix counters for the BGP session
                ''',
                'prefixes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config', 
                [], [], 
                '''                Policy configuration data.
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State', 
                [], [], 
                '''                Operational state for routing policy
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'apply-policy',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config', 
                [], [], 
                '''                Configuration parameters for common IPv4 and IPv6 unicast
                AFI-SAFI options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State', 
                [], [], 
                '''                State information for common IPv4 and IPv6 unicast
                parameters
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config', 
                [], [], 
                '''                Configuration parameters for common IPv4 and IPv6 unicast
                AFI-SAFI options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State', 
                [], [], 
                '''                State information for common IPv4 and IPv6 unicast
                parameters
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv4-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv6-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv4-multicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv6-multicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l2vpn-vpls',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l2vpn-evpn',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State', 
                [], [], 
                '''                State information relating to eBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config', 
                [], [], 
                '''                Configuration parameters relating to multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp', 
                [], [], 
                '''                Multipath configuration for eBGP
                ''',
                'ebgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State', 
                [], [], 
                '''                State parameters relating to multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'use-multiple-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                Reference to the AFI-SAFI name used as a key
                for the AFI-SAFI list
                ''',
                'afi_safi_name',
                'openconfig-bgp', True),
            _MetaInfoClassMember('apply-policy', REFERENCE_CLASS, 'ApplyPolicy' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy', 
                [], [], 
                '''                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                ''',
                'apply_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config', 
                [], [], 
                '''                Configuration parameters for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart', 
                [], [], 
                '''                Parameters relating to BGP graceful-restart
                ''',
                'graceful_restart',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv4-labelled-unicast', REFERENCE_CLASS, 'Ipv4LabelledUnicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast', 
                [], [], 
                '''                IPv4 Labelled Unicast configuration options
                ''',
                'ipv4_labelled_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv4-unicast', REFERENCE_CLASS, 'Ipv4Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast', 
                [], [], 
                '''                IPv4 unicast configuration options
                ''',
                'ipv4_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv6-labelled-unicast', REFERENCE_CLASS, 'Ipv6LabelledUnicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast', 
                [], [], 
                '''                IPv6 Labelled Unicast configuration options
                ''',
                'ipv6_labelled_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv6-unicast', REFERENCE_CLASS, 'Ipv6Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast', 
                [], [], 
                '''                IPv6 unicast configuration options
                ''',
                'ipv6_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l2vpn-evpn', REFERENCE_CLASS, 'L2VpnEvpn' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn', 
                [], [], 
                '''                BGP EVPN configuration options
                ''',
                'l2vpn_evpn',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l2vpn-vpls', REFERENCE_CLASS, 'L2VpnVpls' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls', 
                [], [], 
                '''                BGP-signalled VPLS configuration options
                ''',
                'l2vpn_vpls',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv4-multicast', REFERENCE_CLASS, 'L3VpnIpv4Multicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast', 
                [], [], 
                '''                Multicast IPv4 L3VPN configuration options
                ''',
                'l3vpn_ipv4_multicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv4-unicast', REFERENCE_CLASS, 'L3VpnIpv4Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast', 
                [], [], 
                '''                Unicast IPv4 L3VPN configuration options
                ''',
                'l3vpn_ipv4_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv6-multicast', REFERENCE_CLASS, 'L3VpnIpv6Multicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast', 
                [], [], 
                '''                Multicast IPv6 L3VPN configuration options
                ''',
                'l3vpn_ipv6_multicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv6-unicast', REFERENCE_CLASS, 'L3VpnIpv6Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast', 
                [], [], 
                '''                Unicast IPv6 L3VPN configuration options
                ''',
                'l3vpn_ipv6_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State', 
                [], [], 
                '''                State information relating to the AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            _MetaInfoClassMember('use-multiple-paths', REFERENCE_CLASS, 'UseMultiplePaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths', 
                [], [], 
                '''                Parameters related to the use of multiple-paths for the same
                NLRI when they are received only from this neighbor
                ''',
                'use_multiple_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'afi-safi',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.AfiSafis' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.AfiSafis',
            False, 
            [
            _MetaInfoClassMember('afi-safi', REFERENCE_LIST, 'AfiSafi' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi', 
                [], [], 
                '''                AFI,SAFI configuration available for the
                neighbour or group
                ''',
                'afi_safi',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'afi-safis',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.GracefulRestart.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable the graceful-restart capability.
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('helper-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable graceful-restart in helper mode only. When this
                leaf is set, the local system does not retain forwarding
                its own state during a restart, but supports procedures
                for the receiving speaker, as defined in RFC4724.
                ''',
                'helper_only',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                Estimated time (in seconds) for the local BGP speaker to
                restart a session. This value is advertise in the graceful
                restart BGP capability.  This is a 12-bit value, referred to
                as Restart Time in RFC4724.  Per RFC4724, the suggested
                default value is <= the hold-time value.
                ''',
                'restart_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('stale-routes-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                An upper-bound on the time thate stale routes will be
                retained by a router after a session is restarted. If an
                End-of-RIB (EOR) marker is received prior to this timer
                expiring stale-routes will be flushed upon its receipt - if
                no EOR is received, then when this timer expires stale paths
                will be purged. This timer is referred to as the
                Selection_Deferral_Timer in RFC4724
                ''',
                'stale_routes_time',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart.State.ModeEnum' : _MetaInfoEnum('ModeEnum', 'ydk.models.openconfig.openconfig_bgp',
        {
            'HELPER-ONLY':'HELPER_ONLY',
            'BILATERAL':'BILATERAL',
            'REMOTE-HELPER':'REMOTE_HELPER',
        }, 'openconfig-bgp-operational', _yang_ns._namespaces['openconfig-bgp-operational']),
    'Bgp.Neighbors.Neighbor.GracefulRestart.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.GracefulRestart.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable the graceful-restart capability.
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('helper-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable graceful-restart in helper mode only. When this
                leaf is set, the local system does not retain forwarding
                its own state during a restart, but supports procedures
                for the receiving speaker, as defined in RFC4724.
                ''',
                'helper_only',
                'openconfig-bgp', False),
            _MetaInfoClassMember('local-restarting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This flag indicates whether the local neighbor is currently
                restarting. The flag is unset after all NLRI have been
                advertised to the peer, and the End-of-RIB (EOR) marker has
                been unset
                ''',
                'local_restarting',
                'openconfig-bgp', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'ModeEnum' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.GracefulRestart.State.ModeEnum', 
                [], [], 
                '''                Ths leaf indicates the mode of operation of BGP graceful
                restart with the peer
                ''',
                'mode',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                The period of time (advertised by the peer) that
                the peer expects a restart of a BGP session to
                take
                ''',
                'peer_restart_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-restarting', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This flag indicates whether the remote neighbor is currently
                in the process of restarting, and hence received routes are
                currently stale
                ''',
                'peer_restarting',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                Estimated time (in seconds) for the local BGP speaker to
                restart a session. This value is advertise in the graceful
                restart BGP capability.  This is a 12-bit value, referred to
                as Restart Time in RFC4724.  Per RFC4724, the suggested
                default value is <= the hold-time value.
                ''',
                'restart_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('stale-routes-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                An upper-bound on the time thate stale routes will be
                retained by a router after a session is restarted. If an
                End-of-RIB (EOR) marker is received prior to this timer
                expiring stale-routes will be flushed upon its receipt - if
                no EOR is received, then when this timer expires stale paths
                will be purged. This timer is referred to as the
                Selection_Deferral_Timer in RFC4724
                ''',
                'stale_routes_time',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.GracefulRestart.Config', 
                [], [], 
                '''                Configuration parameters relating to graceful-restart
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.GracefulRestart.State', 
                [], [], 
                '''                State information associated with graceful-restart
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'graceful-restart',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.ApplyPolicy.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.ApplyPolicy.Config',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.ApplyPolicy.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.ApplyPolicy.State',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.ApplyPolicy' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.ApplyPolicy',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.ApplyPolicy.Config', 
                [], [], 
                '''                Policy configuration data.
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.ApplyPolicy.State', 
                [], [], 
                '''                Operational state for routing policy
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'apply-policy',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.UseMultiplePaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.UseMultiplePaths.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.UseMultiplePaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.UseMultiplePaths.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State', 
                [], [], 
                '''                State information relating to eBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor.UseMultiplePaths' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor.UseMultiplePaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.UseMultiplePaths.Config', 
                [], [], 
                '''                Configuration parameters relating to multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp', 
                [], [], 
                '''                Multipath configuration for eBGP
                ''',
                'ebgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.UseMultiplePaths.State', 
                [], [], 
                '''                State parameters relating to multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'use-multiple-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Reference to the address of the BGP neighbor used as
                a key in the neighbor list
                ''',
                'neighbor_address',
                'openconfig-bgp', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Reference to the address of the BGP neighbor used as
                        a key in the neighbor list
                        ''',
                        'neighbor_address',
                        'openconfig-bgp', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Reference to the address of the BGP neighbor used as
                        a key in the neighbor list
                        ''',
                        'neighbor_address',
                        'openconfig-bgp', True),
                ]),
            _MetaInfoClassMember('add-paths', REFERENCE_CLASS, 'AddPaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AddPaths', 
                [], [], 
                '''                Parameters relating to the advertisement and receipt of
                multiple paths for a single NLRI (add-paths)
                ''',
                'add_paths',
                'openconfig-bgp', False),
            _MetaInfoClassMember('afi-safis', REFERENCE_CLASS, 'AfiSafis' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AfiSafis', 
                [], [], 
                '''                Per-address-family configuration parameters associated with
                the neighbor or group
                ''',
                'afi_safis',
                'openconfig-bgp', False),
            _MetaInfoClassMember('apply-policy', REFERENCE_CLASS, 'ApplyPolicy' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.ApplyPolicy', 
                [], [], 
                '''                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                ''',
                'apply_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('as-path-options', REFERENCE_CLASS, 'AsPathOptions' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.AsPathOptions', 
                [], [], 
                '''                AS_PATH manipulation parameters for the BGP neighbor or
                group
                ''',
                'as_path_options',
                'openconfig-bgp', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.Config', 
                [], [], 
                '''                Configuration parameters relating to the BGP neighbor or
                group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.EbgpMultihop', 
                [], [], 
                '''                eBGP multi-hop parameters for the BGP neighbor or group
                ''',
                'ebgp_multihop',
                'openconfig-bgp', False),
            _MetaInfoClassMember('error-handling', REFERENCE_CLASS, 'ErrorHandling' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.ErrorHandling', 
                [], [], 
                '''                Error handling parameters used for the BGP neighbor or
                group
                ''',
                'error_handling',
                'openconfig-bgp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.GracefulRestart', 
                [], [], 
                '''                Parameters relating the graceful restart mechanism for BGP
                ''',
                'graceful_restart',
                'openconfig-bgp', False),
            _MetaInfoClassMember('logging-options', REFERENCE_CLASS, 'LoggingOptions' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.LoggingOptions', 
                [], [], 
                '''                Logging options for events related to the BGP neighbor or
                group
                ''',
                'logging_options',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-reflector', REFERENCE_CLASS, 'RouteReflector' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.RouteReflector', 
                [], [], 
                '''                Route reflector parameters for the BGP neighbor or group
                ''',
                'route_reflector',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.State', 
                [], [], 
                '''                State information relating to the BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.Timers', 
                [], [], 
                '''                Timers related to a BGP neighbor or group
                ''',
                'timers',
                'openconfig-bgp', False),
            _MetaInfoClassMember('transport', REFERENCE_CLASS, 'Transport' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.Transport', 
                [], [], 
                '''                Transport session parameters for the BGP neighbor or group
                ''',
                'transport',
                'openconfig-bgp', False),
            _MetaInfoClassMember('use-multiple-paths', REFERENCE_CLASS, 'UseMultiplePaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor.UseMultiplePaths', 
                [], [], 
                '''                Parameters related to the use of multiple-paths for the same
                NLRI when they are received only from this neighbor
                ''',
                'use_multiple_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'neighbor',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.Neighbors' : {
        'meta_info' : _MetaInfoClass('Bgp.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors.Neighbor', 
                [], [], 
                '''                List of BGP neighbors configured on the local system,
                uniquely identified by peer IPv[46] address
                ''',
                'neighbor',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'neighbors',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.Config',
            False, 
            [
            _MetaInfoClassMember('auth-password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configures an MD5 authentication password for use with
                neighboring devices.
                ''',
                'auth_password',
                'openconfig-bgp', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An optional textual description (intended primarily for use
                with a peer or group
                ''',
                'description',
                'openconfig-bgp', False),
            _MetaInfoClassMember('local-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local autonomous system number that is to be used
                when establishing sessions with the remote peer or peer
                group, if this differs from the global BGP router
                autonomous system number.
                ''',
                'local_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the peer.
                ''',
                'peer_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the BGP peer-group
                ''',
                'peer_group_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-type', REFERENCE_ENUM_CLASS, 'PeerTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'PeerTypeEnum', 
                [], [], 
                '''                Explicitly designate the peer or peer group as internal
                (iBGP) or external (eBGP).
                ''',
                'peer_type',
                'openconfig-bgp', False),
            _MetaInfoClassMember('remove-private-as', REFERENCE_ENUM_CLASS, 'RemovePrivateAsOptionEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'RemovePrivateAsOptionEnum', 
                [], [], 
                '''                Remove private AS numbers from updates sent to peers.
                ''',
                'remove_private_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-flap-damping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable route flap damping.
                ''',
                'route_flap_damping',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-community', REFERENCE_ENUM_CLASS, 'CommunityTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'CommunityTypeEnum', 
                [], [], 
                '''                Specify which types of community should be sent to the
                neighbor or group. The default is to not send the
                community attribute
                ''',
                'send_community',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.State',
            False, 
            [
            _MetaInfoClassMember('auth-password', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configures an MD5 authentication password for use with
                neighboring devices.
                ''',
                'auth_password',
                'openconfig-bgp', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An optional textual description (intended primarily for use
                with a peer or group
                ''',
                'description',
                'openconfig-bgp', False),
            _MetaInfoClassMember('local-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The local autonomous system number that is to be used
                when establishing sessions with the remote peer or peer
                group, if this differs from the global BGP router
                autonomous system number.
                ''',
                'local_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the peer.
                ''',
                'peer_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the BGP peer-group
                ''',
                'peer_group_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-type', REFERENCE_ENUM_CLASS, 'PeerTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'PeerTypeEnum', 
                [], [], 
                '''                Explicitly designate the peer or peer group as internal
                (iBGP) or external (eBGP).
                ''',
                'peer_type',
                'openconfig-bgp', False),
            _MetaInfoClassMember('remove-private-as', REFERENCE_ENUM_CLASS, 'RemovePrivateAsOptionEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'RemovePrivateAsOptionEnum', 
                [], [], 
                '''                Remove private AS numbers from updates sent to peers.
                ''',
                'remove_private_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-flap-damping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable route flap damping.
                ''',
                'route_flap_damping',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-community', REFERENCE_ENUM_CLASS, 'CommunityTypeEnum' , 'ydk.models.openconfig.openconfig_bgp_types', 'CommunityTypeEnum', 
                [], [], 
                '''                Specify which types of community should be sent to the
                neighbor or group. The default is to not send the
                community attribute
                ''',
                'send_community',
                'openconfig-bgp', False),
            _MetaInfoClassMember('total-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of BGP paths within the context
                ''',
                'total_paths',
                'openconfig-bgp', False),
            _MetaInfoClassMember('total-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                
                ''',
                'total_prefixes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.Timers.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.Timers.Config',
            False, 
            [
            _MetaInfoClassMember('connect-retry', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between attempts to establish a
                session with the peer.
                ''',
                'connect_retry',
                'openconfig-bgp', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds that a BGP session will be
                considered active in the absence of keepalive or other
                messages from the peer.  The hold-time is typically
                set to 3x the keepalive-interval.
                ''',
                'hold_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between transmission of keepalive
                messages to the neighbor.  Typically set to 1/3 the
                hold-time.
                ''',
                'keepalive_interval',
                'openconfig-bgp', False),
            _MetaInfoClassMember('minimum-advertisement-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Minimum time which must elapse between subsequent UPDATE
                messages relating to a common set of NLRI being transmitted
                to a peer. This timer is referred to as
                MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
                reduce the number of UPDATE messages transmitted when a
                particular set of NLRI exhibit instability.
                ''',
                'minimum_advertisement_interval',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.Timers.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.Timers.State',
            False, 
            [
            _MetaInfoClassMember('connect-retry', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between attempts to establish a
                session with the peer.
                ''',
                'connect_retry',
                'openconfig-bgp', False),
            _MetaInfoClassMember('hold-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds that a BGP session will be
                considered active in the absence of keepalive or other
                messages from the peer.  The hold-time is typically
                set to 3x the keepalive-interval.
                ''',
                'hold_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('keepalive-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds between transmission of keepalive
                messages to the neighbor.  Typically set to 1/3 the
                hold-time.
                ''',
                'keepalive_interval',
                'openconfig-bgp', False),
            _MetaInfoClassMember('minimum-advertisement-interval', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Minimum time which must elapse between subsequent UPDATE
                messages relating to a common set of NLRI being transmitted
                to a peer. This timer is referred to as
                MinRouteAdvertisementIntervalTimer by RFC 4721 and serves to
                reduce the number of UPDATE messages transmitted when a
                particular set of NLRI exhibit instability.
                ''',
                'minimum_advertisement_interval',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.Timers' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.Timers',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.Timers.Config', 
                [], [], 
                '''                Configuration parameters relating to timers used for the
                BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.Timers.State', 
                [], [], 
                '''                State information relating to the timers used for the BGP
                neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'timers',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.Transport.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.Transport.Config',
            False, 
            [
            _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the local IP (either IPv4 or IPv6) address to use
                for the session when sending BGP update messages.  This
                may be expressed as either an IP address or reference
                to the name of an interface.
                ''',
                'local_address',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False, [
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                        ]),
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False),
                ]),
            _MetaInfoClassMember('mtu-discovery', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Turns path mtu discovery for BGP TCP sessions on (true)
                or off (false)
                ''',
                'mtu_discovery',
                'openconfig-bgp', False),
            _MetaInfoClassMember('passive-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait for peers to issue requests to open a BGP session,
                rather than initiating sessions from the local router.
                ''',
                'passive_mode',
                'openconfig-bgp', False),
            _MetaInfoClassMember('tcp-mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sets the max segment size for BGP TCP sessions.
                ''',
                'tcp_mss',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.Transport.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.Transport.State',
            False, 
            [
            _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set the local IP (either IPv4 or IPv6) address to use
                for the session when sending BGP update messages.  This
                may be expressed as either an IP address or reference
                to the name of an interface.
                ''',
                'local_address',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('local-address', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False, [
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                            _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Set the local IP (either IPv4 or IPv6) address to use
                                for the session when sending BGP update messages.  This
                                may be expressed as either an IP address or reference
                                to the name of an interface.
                                ''',
                                'local_address',
                                'openconfig-bgp', False),
                        ]),
                    _MetaInfoClassMember('local-address', ATTRIBUTE, 'str' , None, None, 
                        [], [], 
                        '''                        Set the local IP (either IPv4 or IPv6) address to use
                        for the session when sending BGP update messages.  This
                        may be expressed as either an IP address or reference
                        to the name of an interface.
                        ''',
                        'local_address',
                        'openconfig-bgp', False),
                ]),
            _MetaInfoClassMember('mtu-discovery', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Turns path mtu discovery for BGP TCP sessions on (true)
                or off (false)
                ''',
                'mtu_discovery',
                'openconfig-bgp', False),
            _MetaInfoClassMember('passive-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait for peers to issue requests to open a BGP session,
                rather than initiating sessions from the local router.
                ''',
                'passive_mode',
                'openconfig-bgp', False),
            _MetaInfoClassMember('tcp-mss', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Sets the max segment size for BGP TCP sessions.
                ''',
                'tcp_mss',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.Transport' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.Transport',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.Transport.Config', 
                [], [], 
                '''                Configuration parameters relating to the transport
                session(s) used for the BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.Transport.State', 
                [], [], 
                '''                State information relating to the transport session(s)
                used for the BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'transport',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.ErrorHandling.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.ErrorHandling.Config',
            False, 
            [
            _MetaInfoClassMember('treat-as-withdraw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify whether erroneous UPDATE messages for which the
                NLRI can be extracted are reated as though the NLRI is
                withdrawn - avoiding session reset
                ''',
                'treat_as_withdraw',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.ErrorHandling.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.ErrorHandling.State',
            False, 
            [
            _MetaInfoClassMember('treat-as-withdraw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify whether erroneous UPDATE messages for which the
                NLRI can be extracted are reated as though the NLRI is
                withdrawn - avoiding session reset
                ''',
                'treat_as_withdraw',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.ErrorHandling' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.ErrorHandling',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.ErrorHandling.Config', 
                [], [], 
                '''                Configuration parameters enabling or modifying the
                behavior or enhanced error handling mechanisms for the BGP
                neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.ErrorHandling.State', 
                [], [], 
                '''                State information relating to enhanced error handling
                mechanisms for the BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'error-handling',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.LoggingOptions.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.LoggingOptions.Config',
            False, 
            [
            _MetaInfoClassMember('log-neighbor-state-changes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure logging of peer state changes.  Default is
                to enable logging of peer state changes.
                ''',
                'log_neighbor_state_changes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.LoggingOptions.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.LoggingOptions.State',
            False, 
            [
            _MetaInfoClassMember('log-neighbor-state-changes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure logging of peer state changes.  Default is
                to enable logging of peer state changes.
                ''',
                'log_neighbor_state_changes',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.LoggingOptions' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.LoggingOptions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.LoggingOptions.Config', 
                [], [], 
                '''                Configuration parameters enabling or modifying logging
                for events relating to the BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.LoggingOptions.State', 
                [], [], 
                '''                State information relating to logging for the BGP neighbor
                or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'logging-options',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled the referenced group or neighbors are permitted
                to be indirectly connected - including cases where the TTL
                can be decremented between the BGP peers
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('multihop-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time-to-live value to use when packets are sent to the
                referenced group or neighbors and ebgp-multihop is enabled
                ''',
                'multihop_ttl',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.EbgpMultihop.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.EbgpMultihop.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When enabled the referenced group or neighbors are permitted
                to be indirectly connected - including cases where the TTL
                can be decremented between the BGP peers
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('multihop-ttl', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Time-to-live value to use when packets are sent to the
                referenced group or neighbors and ebgp-multihop is enabled
                ''',
                'multihop_ttl',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.EbgpMultihop' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.EbgpMultihop',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multihop for the
                BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.EbgpMultihop.State', 
                [], [], 
                '''                State information for eBGP multihop, for the BGP neighbor
                or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp-multihop',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.RouteReflector.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.RouteReflector.Config',
            False, 
            [
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure the neighbor as a route reflector client.
                ''',
                'route_reflector_client',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-reflector-cluster-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                route-reflector cluster id to use when local router is
                configured as a route reflector.  Commonly set at the group
                level, but allows a different cluster
                id to be set for each neighbor.
                ''',
                'route_reflector_cluster_id',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                ]),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.RouteReflector.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.RouteReflector.State',
            False, 
            [
            _MetaInfoClassMember('route-reflector-client', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Configure the neighbor as a route reflector client.
                ''',
                'route_reflector_client',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-reflector-cluster-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                route-reflector cluster id to use when local router is
                configured as a route reflector.  Commonly set at the group
                level, but allows a different cluster
                id to be set for each neighbor.
                ''',
                'route_reflector_cluster_id',
                'openconfig-bgp', False, [
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                    _MetaInfoClassMember('route-reflector-cluster-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        route-reflector cluster id to use when local router is
                        configured as a route reflector.  Commonly set at the group
                        level, but allows a different cluster
                        id to be set for each neighbor.
                        ''',
                        'route_reflector_cluster_id',
                        'openconfig-bgp', False),
                ]),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.RouteReflector' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.RouteReflector',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.RouteReflector.Config', 
                [], [], 
                '''                Configuraton parameters relating to route reflection
                for the BGP neighbor or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.RouteReflector.State', 
                [], [], 
                '''                State information relating to route reflection for the
                BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'route-reflector',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AsPathOptions.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AsPathOptions.Config',
            False, 
            [
            _MetaInfoClassMember('allow-own-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify the number of occurrences of the local BGP speaker's
                AS that can occur within the AS_PATH before it is rejected.
                ''',
                'allow_own_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('replace-peer-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Replace occurrences of the peer's AS in the AS_PATH
                with the local autonomous system number
                ''',
                'replace_peer_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AsPathOptions.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AsPathOptions.State',
            False, 
            [
            _MetaInfoClassMember('allow-own-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify the number of occurrences of the local BGP speaker's
                AS that can occur within the AS_PATH before it is rejected.
                ''',
                'allow_own_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('replace-peer-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Replace occurrences of the peer's AS in the AS_PATH
                with the local autonomous system number
                ''',
                'replace_peer_as',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AsPathOptions' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AsPathOptions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AsPathOptions.Config', 
                [], [], 
                '''                Configuration parameters relating to AS_PATH manipulation
                for the BGP peer or group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AsPathOptions.State', 
                [], [], 
                '''                State information relating to the AS_PATH manipulation
                mechanisms for the BGP peer or group
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'as-path-options',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AddPaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AddPaths.Config',
            False, 
            [
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable ability to receive multiple path advertisements
                for an NLRI from the neighbor or group
                ''',
                'receive',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The maximum number of paths to advertise to neighbors
                for a single NLRI
                ''',
                'send_max',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AddPaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AddPaths.State',
            False, 
            [
            _MetaInfoClassMember('receive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable ability to receive multiple path advertisements
                for an NLRI from the neighbor or group
                ''',
                'receive',
                'openconfig-bgp', False),
            _MetaInfoClassMember('send-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The maximum number of paths to advertise to neighbors
                for a single NLRI
                ''',
                'send_max',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AddPaths' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AddPaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AddPaths.Config', 
                [], [], 
                '''                Configuration parameters relating to ADD_PATHS
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AddPaths.State', 
                [], [], 
                '''                State information associated with ADD_PATHS
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'add-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether graceful-restart is enabled for
                this AFI-SAFI
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether graceful-restart is enabled for
                this AFI-SAFI
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config', 
                [], [], 
                '''                Configuration options for BGP graceful-restart
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State', 
                [], [], 
                '''                State information for BGP graceful-restart
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'graceful-restart',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                AFI,SAFI
                ''',
                'afi_safi_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the IPv4 Unicast AFI,SAFI is
                enabled for the neighbour or group
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                AFI,SAFI
                ''',
                'afi_safi_name',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates whether the IPv4 Unicast AFI,SAFI is
                enabled for the neighbour or group
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config', 
                [], [], 
                '''                Policy configuration data.
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State', 
                [], [], 
                '''                Operational state for routing policy
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'apply-policy',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config', 
                [], [], 
                '''                Configuration parameters for common IPv4 and IPv6 unicast
                AFI-SAFI options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State', 
                [], [], 
                '''                State information for common IPv4 and IPv6 unicast
                parameters
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State',
            False, 
            [
            _MetaInfoClassMember('send-default-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If set to true, send the default-route to the neighbour(s)
                ''',
                'send_default_route',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config', 
                [], [], 
                '''                Configuration parameters for common IPv4 and IPv6 unicast
                AFI-SAFI options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State', 
                [], [], 
                '''                State information for common IPv4 and IPv6 unicast
                parameters
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv4-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ipv6-labelled-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv4-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv6-unicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv4-multicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l3vpn-ipv6-multicast',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l2vpn-vpls',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State',
            False, 
            [
            _MetaInfoClassMember('max-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of prefixes that will be accepted
                from the neighbour
                ''',
                'max_prefixes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-timer', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Time interval in seconds after which the BGP session
                is re-established after being torn down due to exceeding
                the max-prefix limit.
                ''',
                'restart_timer',
                'openconfig-bgp', False),
            _MetaInfoClassMember('shutdown-threshold-pct', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Threshold on number of prefixes that can be received
                from a neighbour before generation of warning messages
                or log entries. Expressed as a percentage of
                max-prefixes
                ''',
                'shutdown_threshold_pct',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config', 
                [], [], 
                '''                Configuration parameters relating to the prefix
                limit for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State', 
                [], [], 
                '''                State information relating to the prefix-limit for the
                AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'prefix-limit',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn',
            False, 
            [
            _MetaInfoClassMember('prefix-limit', REFERENCE_CLASS, 'PrefixLimit' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit', 
                [], [], 
                '''                Configure the maximum number of prefixes that will be
                accepted from a peer
                ''',
                'prefix_limit',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'l2vpn-evpn',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State', 
                [], [], 
                '''                State information relating to eBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config', 
                [], [], 
                '''                Configuration parameters relating to iBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State', 
                [], [], 
                '''                State information relating to iBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ibgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config', 
                [], [], 
                '''                Configuration parameters relating to multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp', 
                [], [], 
                '''                Multipath parameters for eBGP
                ''',
                'ebgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ibgp', REFERENCE_CLASS, 'Ibgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp', 
                [], [], 
                '''                Multipath parameters for iBGP
                ''',
                'ibgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State', 
                [], [], 
                '''                State parameters relating to multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'use-multiple-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config',
            False, 
            [
            _MetaInfoClassMember('advertise-inactive-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise inactive routes to external peers.  The
                default is to only advertise active routes.
                ''',
                'advertise_inactive_routes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('always-compare-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Compare multi-exit discriminator (MED) value from
                different ASes when selecting the best route.  The
                default behavior is to only compare MEDs for paths
                received from the same AS.
                ''',
                'always_compare_med',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enable-aigp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable sending / receiving accumulated IGP
                attribute in routing updates
                ''',
                'enable_aigp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('external-compare-router-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When comparing similar routes received from external
                BGP peers, use the router-id as a criterion to select
                the active path.
                ''',
                'external_compare_router_id',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-as-path-length', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the AS path length when selecting the best path.
                The default is to use the AS path length and prefer paths
                with shorter length.
                ''',
                'ignore_as_path_length',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-next-hop-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the IGP metric to the next-hop when calculating
                BGP best-path. The default is to select the route for
                which the metric to the next-hop is lowest
                ''',
                'ignore_next_hop_igp_metric',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State',
            False, 
            [
            _MetaInfoClassMember('advertise-inactive-routes', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise inactive routes to external peers.  The
                default is to only advertise active routes.
                ''',
                'advertise_inactive_routes',
                'openconfig-bgp', False),
            _MetaInfoClassMember('always-compare-med', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Compare multi-exit discriminator (MED) value from
                different ASes when selecting the best route.  The
                default behavior is to only compare MEDs for paths
                received from the same AS.
                ''',
                'always_compare_med',
                'openconfig-bgp', False),
            _MetaInfoClassMember('enable-aigp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag to enable sending / receiving accumulated IGP
                attribute in routing updates
                ''',
                'enable_aigp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('external-compare-router-id', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When comparing similar routes received from external
                BGP peers, use the router-id as a criterion to select
                the active path.
                ''',
                'external_compare_router_id',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-as-path-length', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the AS path length when selecting the best path.
                The default is to use the AS path length and prefer paths
                with shorter length.
                ''',
                'ignore_as_path_length',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ignore-next-hop-igp-metric', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ignore the IGP metric to the next-hop when calculating
                BGP best-path. The default is to select the route for
                which the metric to the next-hop is lowest
                ''',
                'ignore_next_hop_igp_metric',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config', 
                [], [], 
                '''                Configuration parameters relating to route selection
                options
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State', 
                [], [], 
                '''                State information for the route selection options
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'route-selection-options',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'AfiSafiTypeIdentity' , 'ydk.models.openconfig.openconfig_bgp_types', 'AfiSafiTypeIdentity', 
                [], [], 
                '''                Reference to the AFI-SAFI name used as a key
                for the AFI-SAFI list
                ''',
                'afi_safi_name',
                'openconfig-bgp', True),
            _MetaInfoClassMember('apply-policy', REFERENCE_CLASS, 'ApplyPolicy' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy', 
                [], [], 
                '''                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                ''',
                'apply_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config', 
                [], [], 
                '''                Configuration parameters for the AFI-SAFI
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart', 
                [], [], 
                '''                Parameters relating to BGP graceful-restart
                ''',
                'graceful_restart',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv4-labelled-unicast', REFERENCE_CLASS, 'Ipv4LabelledUnicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast', 
                [], [], 
                '''                IPv4 Labelled Unicast configuration options
                ''',
                'ipv4_labelled_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv4-unicast', REFERENCE_CLASS, 'Ipv4Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast', 
                [], [], 
                '''                IPv4 unicast configuration options
                ''',
                'ipv4_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv6-labelled-unicast', REFERENCE_CLASS, 'Ipv6LabelledUnicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast', 
                [], [], 
                '''                IPv6 Labelled Unicast configuration options
                ''',
                'ipv6_labelled_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ipv6-unicast', REFERENCE_CLASS, 'Ipv6Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast', 
                [], [], 
                '''                IPv6 unicast configuration options
                ''',
                'ipv6_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l2vpn-evpn', REFERENCE_CLASS, 'L2VpnEvpn' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn', 
                [], [], 
                '''                BGP EVPN configuration options
                ''',
                'l2vpn_evpn',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l2vpn-vpls', REFERENCE_CLASS, 'L2VpnVpls' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls', 
                [], [], 
                '''                BGP-signalled VPLS configuration options
                ''',
                'l2vpn_vpls',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv4-multicast', REFERENCE_CLASS, 'L3VpnIpv4Multicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast', 
                [], [], 
                '''                Multicast IPv4 L3VPN configuration options
                ''',
                'l3vpn_ipv4_multicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv4-unicast', REFERENCE_CLASS, 'L3VpnIpv4Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast', 
                [], [], 
                '''                Unicast IPv4 L3VPN configuration options
                ''',
                'l3vpn_ipv4_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv6-multicast', REFERENCE_CLASS, 'L3VpnIpv6Multicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast', 
                [], [], 
                '''                Multicast IPv6 L3VPN configuration options
                ''',
                'l3vpn_ipv6_multicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('l3vpn-ipv6-unicast', REFERENCE_CLASS, 'L3VpnIpv6Unicast' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast', 
                [], [], 
                '''                Unicast IPv6 L3VPN configuration options
                ''',
                'l3vpn_ipv6_unicast',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-selection-options', REFERENCE_CLASS, 'RouteSelectionOptions' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions', 
                [], [], 
                '''                Parameters relating to options for route selection
                ''',
                'route_selection_options',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State', 
                [], [], 
                '''                State information relating to the AFI-SAFI
                ''',
                'state',
                'openconfig-bgp', False),
            _MetaInfoClassMember('use-multiple-paths', REFERENCE_CLASS, 'UseMultiplePaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths', 
                [], [], 
                '''                Parameters related to the use of multiple paths for the
                same NLRI
                ''',
                'use_multiple_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'afi-safi',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.AfiSafis' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.AfiSafis',
            False, 
            [
            _MetaInfoClassMember('afi-safi', REFERENCE_LIST, 'AfiSafi' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi', 
                [], [], 
                '''                AFI,SAFI configuration available for the
                neighbour or group
                ''',
                'afi_safi',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'afi-safis',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.GracefulRestart.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.GracefulRestart.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable the graceful-restart capability.
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('helper-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable graceful-restart in helper mode only. When this
                leaf is set, the local system does not retain forwarding
                its own state during a restart, but supports procedures
                for the receiving speaker, as defined in RFC4724.
                ''',
                'helper_only',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                Estimated time (in seconds) for the local BGP speaker to
                restart a session. This value is advertise in the graceful
                restart BGP capability.  This is a 12-bit value, referred to
                as Restart Time in RFC4724.  Per RFC4724, the suggested
                default value is <= the hold-time value.
                ''',
                'restart_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('stale-routes-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                An upper-bound on the time thate stale routes will be
                retained by a router after a session is restarted. If an
                End-of-RIB (EOR) marker is received prior to this timer
                expiring stale-routes will be flushed upon its receipt - if
                no EOR is received, then when this timer expires stale paths
                will be purged. This timer is referred to as the
                Selection_Deferral_Timer in RFC4724
                ''',
                'stale_routes_time',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.GracefulRestart.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.GracefulRestart.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable the graceful-restart capability.
                ''',
                'enabled',
                'openconfig-bgp', False),
            _MetaInfoClassMember('helper-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable graceful-restart in helper mode only. When this
                leaf is set, the local system does not retain forwarding
                its own state during a restart, but supports procedures
                for the receiving speaker, as defined in RFC4724.
                ''',
                'helper_only',
                'openconfig-bgp', False),
            _MetaInfoClassMember('restart-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4096')], [], 
                '''                Estimated time (in seconds) for the local BGP speaker to
                restart a session. This value is advertise in the graceful
                restart BGP capability.  This is a 12-bit value, referred to
                as Restart Time in RFC4724.  Per RFC4724, the suggested
                default value is <= the hold-time value.
                ''',
                'restart_time',
                'openconfig-bgp', False),
            _MetaInfoClassMember('stale-routes-time', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                An upper-bound on the time thate stale routes will be
                retained by a router after a session is restarted. If an
                End-of-RIB (EOR) marker is received prior to this timer
                expiring stale-routes will be flushed upon its receipt - if
                no EOR is received, then when this timer expires stale paths
                will be purged. This timer is referred to as the
                Selection_Deferral_Timer in RFC4724
                ''',
                'stale_routes_time',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.GracefulRestart.Config', 
                [], [], 
                '''                Configuration parameters relating to graceful-restart
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.GracefulRestart.State', 
                [], [], 
                '''                State information associated with graceful-restart
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'graceful-restart',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.ApplyPolicy.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.ApplyPolicy.State',
            False, 
            [
            _MetaInfoClassMember('default-export-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the export policy chain is satisfied.
                ''',
                'default_export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('default-import-policy', REFERENCE_ENUM_CLASS, 'DefaultPolicyTypeEnum' , 'ydk.models.openconfig.openconfig_routing_policy', 'DefaultPolicyTypeEnum', 
                [], [], 
                '''                explicitly set a default policy if no policy definition
                in the import policy chain is satisfied.
                ''',
                'default_import_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('export-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                sending a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'export_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('import-policy', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                list of policy names in sequence to be applied on
                receiving a routing update in the current context, e.g.,
                for the current peer group, neighbor, address family,
                etc.
                ''',
                'import_policy',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.ApplyPolicy' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.ApplyPolicy',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config', 
                [], [], 
                '''                Policy configuration data.
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.ApplyPolicy.State', 
                [], [], 
                '''                Operational state for routing policy
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'apply-policy',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the use of multiple paths for the same NLRI is
                enabled for the neighbor. This value is overridden by
                any more specific configuration value.
                ''',
                'enabled',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State',
            False, 
            [
            _MetaInfoClassMember('allow-multiple-as', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow multipath to use paths from different neighbouring
                ASes.  The default is to only consider multiple paths from
                the same neighbouring AS.
                ''',
                'allow_multiple_as',
                'openconfig-bgp', False),
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                BGP multipath. The default is use a single path.
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config', 
                [], [], 
                '''                Configuration parameters relating to eBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State', 
                [], [], 
                '''                State information relating to eBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ebgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'config',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State',
            False, 
            [
            _MetaInfoClassMember('maximum-paths', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of parallel paths to consider when using
                iBGP multipath. The default is to use a single path
                ''',
                'maximum_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'state',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config', 
                [], [], 
                '''                Configuration parameters relating to iBGP multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State', 
                [], [], 
                '''                State information relating to iBGP multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'ibgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup.UseMultiplePaths' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup.UseMultiplePaths',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config', 
                [], [], 
                '''                Configuration parameters relating to multipath
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp', REFERENCE_CLASS, 'Ebgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp', 
                [], [], 
                '''                Multipath parameters for eBGP
                ''',
                'ebgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ibgp', REFERENCE_CLASS, 'Ibgp' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp', 
                [], [], 
                '''                Multipath parameters for iBGP
                ''',
                'ibgp',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State', 
                [], [], 
                '''                State parameters relating to multipath
                ''',
                'state',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'use-multiple-paths',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups.PeerGroup' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups.PeerGroup',
            False, 
            [
            _MetaInfoClassMember('peer-group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to the name of the BGP peer-group used as a
                key in the peer-group list
                ''',
                'peer_group_name',
                'openconfig-bgp', True),
            _MetaInfoClassMember('add-paths', REFERENCE_CLASS, 'AddPaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AddPaths', 
                [], [], 
                '''                Parameters relating to the advertisement and receipt of
                multiple paths for a single NLRI (add-paths)
                ''',
                'add_paths',
                'openconfig-bgp', False),
            _MetaInfoClassMember('afi-safis', REFERENCE_CLASS, 'AfiSafis' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AfiSafis', 
                [], [], 
                '''                Per-address-family configuration parameters associated with
                the neighbor or group
                ''',
                'afi_safis',
                'openconfig-bgp', False),
            _MetaInfoClassMember('apply-policy', REFERENCE_CLASS, 'ApplyPolicy' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.ApplyPolicy', 
                [], [], 
                '''                Anchor point for routing policies in the model.
                Import and export policies are with respect to the local
                routing table, i.e., export (send) and import (receive),
                depending on the context.
                ''',
                'apply_policy',
                'openconfig-bgp', False),
            _MetaInfoClassMember('as-path-options', REFERENCE_CLASS, 'AsPathOptions' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.AsPathOptions', 
                [], [], 
                '''                AS_PATH manipulation parameters for the BGP neighbor or
                group
                ''',
                'as_path_options',
                'openconfig-bgp', False),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.Config', 
                [], [], 
                '''                Configuration parameters relating to the BGP neighbor or
                group
                ''',
                'config',
                'openconfig-bgp', False),
            _MetaInfoClassMember('ebgp-multihop', REFERENCE_CLASS, 'EbgpMultihop' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.EbgpMultihop', 
                [], [], 
                '''                eBGP multi-hop parameters for the BGP neighbor or group
                ''',
                'ebgp_multihop',
                'openconfig-bgp', False),
            _MetaInfoClassMember('error-handling', REFERENCE_CLASS, 'ErrorHandling' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.ErrorHandling', 
                [], [], 
                '''                Error handling parameters used for the BGP neighbor or
                group
                ''',
                'error_handling',
                'openconfig-bgp', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.GracefulRestart', 
                [], [], 
                '''                Parameters relating the graceful restart mechanism for BGP
                ''',
                'graceful_restart',
                'openconfig-bgp', False),
            _MetaInfoClassMember('logging-options', REFERENCE_CLASS, 'LoggingOptions' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.LoggingOptions', 
                [], [], 
                '''                Logging options for events related to the BGP neighbor or
                group
                ''',
                'logging_options',
                'openconfig-bgp', False),
            _MetaInfoClassMember('route-reflector', REFERENCE_CLASS, 'RouteReflector' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.RouteReflector', 
                [], [], 
                '''                Route reflector parameters for the BGP neighbor or group
                ''',
                'route_reflector',
                'openconfig-bgp', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.State', 
                [], [], 
                '''                State information relating to the BGP neighbor or group
                ''',
                'state',
                'openconfig-bgp', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.Timers', 
                [], [], 
                '''                Timers related to a BGP neighbor or group
                ''',
                'timers',
                'openconfig-bgp', False),
            _MetaInfoClassMember('transport', REFERENCE_CLASS, 'Transport' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.Transport', 
                [], [], 
                '''                Transport session parameters for the BGP neighbor or group
                ''',
                'transport',
                'openconfig-bgp', False),
            _MetaInfoClassMember('use-multiple-paths', REFERENCE_CLASS, 'UseMultiplePaths' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup.UseMultiplePaths', 
                [], [], 
                '''                Parameters related to the use of multiple paths for the
                same NLRI
                ''',
                'use_multiple_paths',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'peer-group',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp.PeerGroups' : {
        'meta_info' : _MetaInfoClass('Bgp.PeerGroups',
            False, 
            [
            _MetaInfoClassMember('peer-group', REFERENCE_LIST, 'PeerGroup' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups.PeerGroup', 
                [], [], 
                '''                List of BGP peer-groups configured on the local system -
                uniquely identified by peer-group name
                ''',
                'peer_group',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'peer-groups',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
    'Bgp' : {
        'meta_info' : _MetaInfoClass('Bgp',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Global_', 
                [], [], 
                '''                Global configuration for the BGP router
                ''',
                'global_',
                'openconfig-bgp', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.Neighbors', 
                [], [], 
                '''                Configuration for BGP neighbors
                ''',
                'neighbors',
                'openconfig-bgp', False),
            _MetaInfoClassMember('peer-groups', REFERENCE_CLASS, 'PeerGroups' , 'ydk.models.openconfig.openconfig_bgp', 'Bgp.PeerGroups', 
                [], [], 
                '''                Configuration for BGP peer-groups
                ''',
                'peer_groups',
                'openconfig-bgp', False),
            ],
            'openconfig-bgp',
            'bgp',
            _yang_ns._namespaces['openconfig-bgp'],
        'ydk.models.openconfig.openconfig_bgp'
        ),
    },
}
_meta_table['Bgp.Global_.RouteSelectionOptions.Config']['meta_info'].parent =_meta_table['Bgp.Global_.RouteSelectionOptions']['meta_info']
_meta_table['Bgp.Global_.RouteSelectionOptions.State']['meta_info'].parent =_meta_table['Bgp.Global_.RouteSelectionOptions']['meta_info']
_meta_table['Bgp.Global_.DefaultRouteDistance.Config']['meta_info'].parent =_meta_table['Bgp.Global_.DefaultRouteDistance']['meta_info']
_meta_table['Bgp.Global_.DefaultRouteDistance.State']['meta_info'].parent =_meta_table['Bgp.Global_.DefaultRouteDistance']['meta_info']
_meta_table['Bgp.Global_.Confederation.Config']['meta_info'].parent =_meta_table['Bgp.Global_.Confederation']['meta_info']
_meta_table['Bgp.Global_.Confederation.State']['meta_info'].parent =_meta_table['Bgp.Global_.Confederation']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.Ebgp.Config']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.Ebgp.State']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.Ibgp.Config']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.Ibgp.State']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.Config']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.State']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.Ebgp']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths.Ibgp']['meta_info'].parent =_meta_table['Bgp.Global_.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.GracefulRestart.Config']['meta_info'].parent =_meta_table['Bgp.Global_.GracefulRestart']['meta_info']
_meta_table['Bgp.Global_.GracefulRestart.State']['meta_info'].parent =_meta_table['Bgp.Global_.GracefulRestart']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.GracefulRestart']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Config']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.State']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.ApplyPolicy']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnVpls']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Global_.AfiSafis.AfiSafi']['meta_info'].parent =_meta_table['Bgp.Global_.AfiSafis']['meta_info']
_meta_table['Bgp.Global_.ApplyPolicy.Config']['meta_info'].parent =_meta_table['Bgp.Global_.ApplyPolicy']['meta_info']
_meta_table['Bgp.Global_.ApplyPolicy.State']['meta_info'].parent =_meta_table['Bgp.Global_.ApplyPolicy']['meta_info']
_meta_table['Bgp.Global_.Config']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.State']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.RouteSelectionOptions']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.DefaultRouteDistance']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.Confederation']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.UseMultiplePaths']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.GracefulRestart']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.AfiSafis']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Global_.ApplyPolicy']['meta_info'].parent =_meta_table['Bgp.Global_']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.State.Messages.Sent']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.State.Messages']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.State.Messages.Received']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.State.Messages']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.State.Messages']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.State']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.State.Queues']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.State']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.Timers.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.Timers']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.Timers.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.Timers']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.Transport.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.Transport']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.Transport.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.Transport']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.ErrorHandling.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.ErrorHandling']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.ErrorHandling.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.ErrorHandling']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.LoggingOptions.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.LoggingOptions']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.LoggingOptions.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.LoggingOptions']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.RouteReflector.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.RouteReflector']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.RouteReflector.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.RouteReflector']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AsPathOptions.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AsPathOptions']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AsPathOptions.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AsPathOptions']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AddPaths.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AddPaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AddPaths.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AddPaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State.Prefixes']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.GracefulRestart']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.ApplyPolicy']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnVpls']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis.AfiSafi']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.AfiSafis']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.GracefulRestart.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.GracefulRestart']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.GracefulRestart.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.GracefulRestart']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths.Ebgp']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.Config']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.State']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.Timers']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.Transport']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.ErrorHandling']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.LoggingOptions']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.RouteReflector']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AsPathOptions']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AddPaths']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.AfiSafis']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.GracefulRestart']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.ApplyPolicy']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor.UseMultiplePaths']['meta_info'].parent =_meta_table['Bgp.Neighbors.Neighbor']['meta_info']
_meta_table['Bgp.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Bgp.Neighbors']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.Timers.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.Timers']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.Timers.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.Timers']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.Transport.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.Transport']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.Transport.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.Transport']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AddPaths.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AddPaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AddPaths.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AddPaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn.PrefixLimit']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ebgp']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths.Ibgp']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.GracefulRestart']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.ApplyPolicy']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv4LabelledUnicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.Ipv6LabelledUnicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Unicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Unicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv4Multicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L3VpnIpv6Multicast']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnVpls']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.L2VpnEvpn']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.UseMultiplePaths']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi.RouteSelectionOptions']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis.AfiSafi']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ebgp']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths.Ibgp']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.Config']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.State']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.Timers']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.Transport']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.ErrorHandling']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.LoggingOptions']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.EbgpMultihop']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.RouteReflector']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AsPathOptions']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AddPaths']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.AfiSafis']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.GracefulRestart']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.ApplyPolicy']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup.UseMultiplePaths']['meta_info'].parent =_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info']
_meta_table['Bgp.PeerGroups.PeerGroup']['meta_info'].parent =_meta_table['Bgp.PeerGroups']['meta_info']
_meta_table['Bgp.Global_']['meta_info'].parent =_meta_table['Bgp']['meta_info']
_meta_table['Bgp.Neighbors']['meta_info'].parent =_meta_table['Bgp']['meta_info']
_meta_table['Bgp.PeerGroups']['meta_info'].parent =_meta_table['Bgp']['meta_info']
