


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'loc-rib',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-in-pre',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-in-post',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-out-pre',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-out-post',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the BGP neighbor or peer
                ''',
                'neighbor_address',
                'openconfig-rib-bgp', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the BGP neighbor or peer
                        ''',
                        'neighbor_address',
                        'openconfig-rib-bgp', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the BGP neighbor or peer
                        ''',
                        'neighbor_address',
                        'openconfig-rib-bgp', True),
                ]),
            _MetaInfoClassMember('adj-rib-in-post', REFERENCE_CLASS, 'AdjRibInPost' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost', 
                [], [], 
                '''                Per-neighbor table containing the paths received from
                the neighbor that are eligible for best-path selection
                after local input policy rules have been applied.
                ''',
                'adj_rib_in_post',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('adj-rib-in-pre', REFERENCE_CLASS, 'AdjRibInPre' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre', 
                [], [], 
                '''                Per-neighbor table containing the NLRI updates
                received from the neighbor before any local input
                policy rules or filters have been applied.  This can
                be considered the 'raw' updates from the neighbor.
                ''',
                'adj_rib_in_pre',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('adj-rib-out-post', REFERENCE_CLASS, 'AdjRibOutPost' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost', 
                [], [], 
                '''                Per-neighbor table containing paths eligble for
                sending (advertising) to the neighbor after output
                policy rules have been applied
                ''',
                'adj_rib_out_post',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('adj-rib-out-pre', REFERENCE_CLASS, 'AdjRibOutPre' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre', 
                [], [], 
                '''                Per-neighbor table containing paths eligble for
                sending (advertising) to the neighbor before output
                policy rules have been applied
                ''',
                'adj_rib_out_pre',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'neighbor',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor', 
                [], [], 
                '''                List of neighbors (peers) of the local BGP speaker
                ''',
                'neighbor',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'neighbors',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv4Unicast',
            False, 
            [
            _MetaInfoClassMember('loc-rib', REFERENCE_CLASS, 'LocRib' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib', 
                [], [], 
                '''                Main routing table on the router, containing best-path
                selections for each prefix.  The loc-rib may contain
                multiple routes for the same prefix (it is a read-only,
                unkeyed list).  The best-path leaf should be set to true
                for the route selected by the best-path selection process.
                Note that multiple paths may be used or advertised even if
                only one path is marked as best, e.g., when using BGP
                add-paths.  An implementation may choose to mark multiple
                paths in the RIB as best path by setting the flag to true for
                multiple entries.
                ''',
                'loc_rib',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors', 
                [], [], 
                '''                Enclosing container for neighbor list
                ''',
                'neighbors',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ipv4-unicast',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'loc-rib',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-in-pre',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-in-post',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-out-pre',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address of the router that performed the
                aggregation.
                ''',
                'address',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation (4-octet representation).  This value is
                populated if an upstream router is not 4-octet capable.
                Its semantics are similar to the AS4_PATH optional
                transitive attribute
                ''',
                'as4',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                AS number of the autnonomous system that performed the
                aggregation.
                ''',
                'as_',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'aggregator',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes',
            False, 
            [
            _MetaInfoClassMember('aggregator', REFERENCE_CLASS, 'Aggregator' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator', 
                [], [], 
                '''                BGP attribute indicating the prefix has been aggregated by
                the specified AS and router.
                ''',
                'aggregator',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as4-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This string represents the AS path encoded with 4-octet
                AS numbers in the optional transitive AS4_PATH attribute.
                This value is populated with the received or sent attribute
                in Adj-RIB-In or Adj-RIB-Out, respectively.  It should not
                be populated in Loc-RIB since the Loc-RIB is expected to
                store the effective AS-Path in the as-path leaf regardless
                of being 4-octet or 2-octet.
                ''',
                'as4_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('as-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                String representation of the BGP AS path attribute as
                concatenated AS path segments.  Each segment of the AS_PATH
                should be formatted as follows based on the segment type
                (#### denotes a single AS number):
                
                 AS_SEQ: #### #### #####
                 AS_SET: { #### #### }
                 AS_CONFED_SEQUENCE: ( #### #### )
                 AS_CONFED_SET: [ #### #### ]
                
                AS_PATH segment types are described in RFC 5065.
                
                In the Adj-RIB-In or Adj-RIB-Out, this leaf should show
                the received or sent AS_PATH value, respectively.  For
                example, if the local router is not 4-byte capable, this
                value should consist of 2-octet ASNs or the AS_TRANS
                (AS 23456) values received or sent in route updates.
                
                In the Loc-RIB, this leaf should reflect the effective
                AS path for the route, e.g., a 4-octet value if the
                local router is 4-octet capable.
                ''',
                'as_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('atomic-aggr', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BGP attribute indicating that the prefix is an atomic
                aggregate, i.e., the peer selected a less specific
                route without selecting a more specific route that is
                included in it.
                ''',
                'atomic_aggr',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of standard BGP community attributes.
                ''',
                'community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [('65536', '4294901759')], [], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'([0-9]+:[0-9]+)'], 
                        '''                        List of standard BGP community attributes.
                        ''',
                        'community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('local-pref', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP local preference attribute sent to internal peers to
                indicate
                ''',
                'local_pref',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('med', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BGP multi-exit discriminator attribute used in BGP route
                selection process
                ''',
                'med',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                BGP next hop attribute defining the IP address of the router
                that should be used as the next hop to the destination
                ''',
                'next_hop',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        BGP next hop attribute defining the IP address of the router
                        that should be used as the next hop to the destination
                        ''',
                        'next_hop',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('origin', REFERENCE_ENUM_CLASS, 'BgpOriginAttrTypeEnum' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'BgpOriginAttrTypeEnum', 
                [], [], 
                '''                BGP attribute defining the origin of the path information.
                ''',
                'origin',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute',
            False, 
            [
            _MetaInfoClassMember('attr-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                2-octet value encoding the attribute flags and the
                attribute type code
                ''',
                'attr_type',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('attr-len', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                One or two octet attribute length field indicating the
                length of the attribute data in octets.  If the Extended
                Length attribute flag in the attribute type field is set,
                the length field is 2 octets, otherwise it is 1 octet
                ''',
                'attr_len',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('attr-value', ATTRIBUTE, 'str' , None, None, 
                [(1, 65535)], [], 
                '''                Raw attribute value data, not to exceed the length
                indicated in the attr-len field.  The maximum length
                of the attribute data is 2^16-1 per the max value of the
                attr-len field (2 octets).
                ''',
                'attr_value',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'unknown-attribute',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes',
            False, 
            [
            _MetaInfoClassMember('aigp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                BGP path attribute representing the accumulated IGP metric
                for the path
                ''',
                'aigp',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('cluster-list', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Represents the reflection path that the route has passed.
                ''',
                'cluster_list',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-community', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                List of BGP extended community attributes
                ''',
                'ext_community',
                'openconfig-rib-bgp', False, [
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-target:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9]):(4[0-2][0-9][0-4][0-9][0-6][0-7][0-2][0-9][0-6]|[1-3][0-9]{9}|[1-9]([0-9]{1,7})?[0-9]|[1-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                    _MetaInfoClassMember('ext-community', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [b'route\\-origin:(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5]):(6[0-5][0-5][0-3][0-5]|[1-5][0-9]{4}|[1-9][0-9]{1,4}|[0-9])'], 
                        '''                        List of BGP extended community attributes
                        ''',
                        'ext_community',
                        'openconfig-rib-bgp', False),
                ]),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BGP attribute that provides the id as an IPv4 address
                of the route reflector that created the announcement
                ''',
                'originator_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('path-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the BGP speaker supports advertisement of multiple
                paths for a prefix, the path identifier is used to
                uniquely identify a route based on the combination of the
                prefix and path id.  In the Adj-RIB-In, the path-id value is
                the value received in the update message.   In the Loc-RIB,
                if used, it should represent a locally generated path-id
                value for the corresponding route.  In Adj-RIB-Out, it
                should be the value sent to a neighbor when add-paths is
                used, i.e., the capability has been negotiated.
                ''',
                'path_id',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('unknown-attribute', REFERENCE_LIST, 'UnknownAttribute' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute', 
                [], [], 
                '''                This list contains received attributes that are unrecognized
                or unsupported by the local router.  The list may be empty.
                ''',
                'unknown_attribute',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ext-attributes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('attributes', REFERENCE_CLASS, 'Attributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes', 
                [], [], 
                '''                Base BGP route attributes associated with this route
                ''',
                'attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('best-path', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Current path was selected as the best path.
                ''',
                'best_path',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ext-attributes', REFERENCE_CLASS, 'ExtAttributes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes', 
                [], [], 
                '''                Extended BGP route attributes associated with this
                route
                ''',
                'ext_attributes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('invalid-reason', REFERENCE_IDENTITY_CLASS, 'Invalid_Route_ReasonIdentity' , 'ydk.models.openconfig.openconfig_rib_bgp_types', 'Invalid_Route_ReasonIdentity', 
                [], [], 
                '''                If the route is rejected as invalid, this indicates the
                reason.
                ''',
                'invalid_reason',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-modified-date', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when this path was last changed
                ''',
                'last_modified_date',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('last-update-received', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Timestamp of when the last BGP update message was received
                for this path / prefix
                ''',
                'last_update_received',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Prefix for the route
                ''',
                'prefix',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('valid-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates that the route is considered valid by the
                local router
                ''',
                'valid_route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'route',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route', 
                [], [], 
                '''                List of routes in the table
                ''',
                'route',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'routes',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost',
            False, 
            [
            _MetaInfoClassMember('num-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of route entries in the table
                ''',
                'num_routes',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes', 
                [], [], 
                '''                Enclosing container for list of routes in the routing
                table.
                ''',
                'routes',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'adj-rib-out-post',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of the BGP neighbor or peer
                ''',
                'neighbor_address',
                'openconfig-rib-bgp', True, [
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the BGP neighbor or peer
                        ''',
                        'neighbor_address',
                        'openconfig-rib-bgp', True),
                    _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of the BGP neighbor or peer
                        ''',
                        'neighbor_address',
                        'openconfig-rib-bgp', True),
                ]),
            _MetaInfoClassMember('adj-rib-in-post', REFERENCE_CLASS, 'AdjRibInPost' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost', 
                [], [], 
                '''                Per-neighbor table containing the paths received from
                the neighbor that are eligible for best-path selection
                after local input policy rules have been applied.
                ''',
                'adj_rib_in_post',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('adj-rib-in-pre', REFERENCE_CLASS, 'AdjRibInPre' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre', 
                [], [], 
                '''                Per-neighbor table containing the NLRI updates
                received from the neighbor before any local input
                policy rules or filters have been applied.  This can
                be considered the 'raw' updates from the neighbor.
                ''',
                'adj_rib_in_pre',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('adj-rib-out-post', REFERENCE_CLASS, 'AdjRibOutPost' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost', 
                [], [], 
                '''                Per-neighbor table containing paths eligble for
                sending (advertising) to the neighbor after output
                policy rules have been applied
                ''',
                'adj_rib_out_post',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('adj-rib-out-pre', REFERENCE_CLASS, 'AdjRibOutPre' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre', 
                [], [], 
                '''                Per-neighbor table containing paths eligble for
                sending (advertising) to the neighbor before output
                policy rules have been applied
                ''',
                'adj_rib_out_pre',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'neighbor',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor', 
                [], [], 
                '''                List of neighbors (peers) of the local BGP speaker
                ''',
                'neighbor',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'neighbors',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi.Ipv6Unicast',
            False, 
            [
            _MetaInfoClassMember('loc-rib', REFERENCE_CLASS, 'LocRib' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib', 
                [], [], 
                '''                Main routing table on the router, containing best-path
                selections for each prefix.  The loc-rib may contain
                multiple routes for the same prefix (it is a read-only,
                unkeyed list).  The best-path leaf should be set to true
                for the route selected by the best-path selection process.
                Note that multiple paths may be used or advertised even if
                only one path is marked as best, e.g., when using BGP
                add-paths.  An implementation may choose to mark multiple
                paths in the RIB as best path by setting the flag to true for
                multiple entries.
                ''',
                'loc_rib',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors', 
                [], [], 
                '''                Enclosing container for neighbor list
                ''',
                'neighbors',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'ipv6-unicast',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis.AfiSafi' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis.AfiSafi',
            False, 
            [
            _MetaInfoClassMember('afi-safi-name', REFERENCE_IDENTITY_CLASS, 'Afi_Safi_TypeIdentity' , 'ydk.models.openconfig.cisco_xr_openconfig_bgp_types', 'Afi_Safi_TypeIdentity', 
                [], [], 
                '''                AFI,SAFI
                ''',
                'afi_safi_name',
                'openconfig-rib-bgp', True),
            _MetaInfoClassMember('ipv4-unicast', REFERENCE_CLASS, 'Ipv4Unicast' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv4Unicast', 
                [], [], 
                '''                Routing tables for IPv4 unicast -- active when the
                afi-safi name is ipv4-unicast
                ''',
                'ipv4_unicast',
                'openconfig-rib-bgp', False),
            _MetaInfoClassMember('ipv6-unicast', REFERENCE_CLASS, 'Ipv6Unicast' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi.Ipv6Unicast', 
                [], [], 
                '''                Routing tables for IPv6 unicast -- active when the
                afi-safi name is ipv6-unicast
                ''',
                'ipv6_unicast',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'afi-safi',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib.AfiSafis' : {
        'meta_info' : _MetaInfoClass('BgpRib.AfiSafis',
            False, 
            [
            _MetaInfoClassMember('afi-safi', REFERENCE_LIST, 'AfiSafi' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis.AfiSafi', 
                [], [], 
                '''                list of afi-safi types
                ''',
                'afi_safi',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'afi-safis',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
    'BgpRib' : {
        'meta_info' : _MetaInfoClass('BgpRib',
            False, 
            [
            _MetaInfoClassMember('afi-safis', REFERENCE_CLASS, 'AfiSafis' , 'ydk.models.openconfig.openconfig_rib_bgp', 'BgpRib.AfiSafis', 
                [], [], 
                '''                Enclosing container for address family list
                ''',
                'afi_safis',
                'openconfig-rib-bgp', False),
            ],
            'openconfig-rib-bgp',
            'bgp-rib',
            _yang_ns._namespaces['openconfig-rib-bgp'],
        'ydk.models.openconfig.openconfig_rib_bgp'
        ),
    },
}
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPre']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibInPost']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPre']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor.AdjRibOutPost']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors.Neighbor']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.LocRib']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast.Neighbors']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes.Aggregator']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes.UnknownAttribute']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.Attributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route.ExtAttributes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes.Route']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost.Routes']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPre']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibInPost']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPre']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor.AdjRibOutPost']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors.Neighbor']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.LocRib']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast.Neighbors']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv4Unicast']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi.Ipv6Unicast']['meta_info'].parent =_meta_table['BgpRib.AfiSafis.AfiSafi']['meta_info']
_meta_table['BgpRib.AfiSafis.AfiSafi']['meta_info'].parent =_meta_table['BgpRib.AfiSafis']['meta_info']
_meta_table['BgpRib.AfiSafis']['meta_info'].parent =_meta_table['BgpRib']['meta_info']
