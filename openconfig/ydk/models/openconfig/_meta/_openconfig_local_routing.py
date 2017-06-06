


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Local_Defined_Next_HopIdentity' : {
        'meta_info' : _MetaInfoClass('Local_Defined_Next_HopIdentity',
            False, 
            [
            ],
            'openconfig-local-routing',
            'LOCAL_DEFINED_NEXT_HOP',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.Config' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.Config',
            False, 
            [
            ],
            'openconfig-local-routing',
            'config',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.State' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.State',
            False, 
            [
            ],
            'openconfig-local-routing',
            'state',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.Config' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.Config',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination prefix for the static route, either IPv4 or
                IPv6.
                ''',
                'prefix',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Destination prefix for the static route, either IPv4 or
                        IPv6.
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Destination prefix for the static route, either IPv4 or
                        IPv6.
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                ]),
            _MetaInfoClassMember('set-tag', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set a generic tag value on the route. This tag can be
                used for filtering routes that are distributed to other
                routing protocols.
                ''',
                'set_tag',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'str' , None, None, 
                        [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                ]),
            ],
            'openconfig-local-routing',
            'config',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.State' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.State',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Destination prefix for the static route, either IPv4 or
                IPv6.
                ''',
                'prefix',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Destination prefix for the static route, either IPv4 or
                        IPv6.
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Destination prefix for the static route, either IPv4 or
                        IPv6.
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                ]),
            _MetaInfoClassMember('set-tag', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set a generic tag value on the route. This tag can be
                used for filtering routes that are distributed to other
                routing protocols.
                ''',
                'set_tag',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'str' , None, None, 
                        [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                ]),
            ],
            'openconfig-local-routing',
            'state',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An user-specified identifier utilised to uniquely reference
                the next-hop entry in the next-hop list. The value of this
                index has no semantic meaning other than for referencing
                the entry.
                ''',
                'index',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A metric which is utilised to specify the preference of
                the next-hop entry when it is injected into the RIB. The
                lower the metric, the more preferable the prefix is. When
                this value is not specified the metric is inherited from
                the default metric utilised for static routes within the
                network instance that the static routes are being
                instantiated. When multiple next-hops are specified for a
                static route, the metric is utilised to determine which of
                the next-hops is to be installed in the RIB. When multiple
                next-hops have the same metric (be it specified, or simply
                the default) then these next-hops should all be installed
                in the RIB
                ''',
                'metric',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The next-hop that is to be used for the static route
                - this may be specified as an IP address, an interface
                or a pre-defined next-hop type - for instance, DROP or
                LOCAL_LINK. When this leaf is not set, and the interface-ref
                value is specified for the next-hop, then the system should
                treat the prefix as though it is directly connected to the
                interface.
                ''',
                'next_hop',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        The next-hop that is to be used for the static route
                        - this may be specified as an IP address, an interface
                        or a pre-defined next-hop type - for instance, DROP or
                        LOCAL_LINK. When this leaf is not set, and the interface-ref
                        value is specified for the next-hop, then the system should
                        treat the prefix as though it is directly connected to the
                        interface.
                        ''',
                        'next_hop',
                        'openconfig-local-routing', False, [
                            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The next-hop that is to be used for the static route
                                - this may be specified as an IP address, an interface
                                or a pre-defined next-hop type - for instance, DROP or
                                LOCAL_LINK. When this leaf is not set, and the interface-ref
                                value is specified for the next-hop, then the system should
                                treat the prefix as though it is directly connected to the
                                interface.
                                ''',
                                'next_hop',
                                'openconfig-local-routing', False),
                            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The next-hop that is to be used for the static route
                                - this may be specified as an IP address, an interface
                                or a pre-defined next-hop type - for instance, DROP or
                                LOCAL_LINK. When this leaf is not set, and the interface-ref
                                value is specified for the next-hop, then the system should
                                treat the prefix as though it is directly connected to the
                                interface.
                                ''',
                                'next_hop',
                                'openconfig-local-routing', False),
                        ]),
                    _MetaInfoClassMember('next-hop', REFERENCE_IDENTITY_CLASS, 'Local_Defined_Next_HopIdentity' , 'ydk.models.openconfig.openconfig_local_routing', 'Local_Defined_Next_HopIdentity', 
                        [], [], 
                        '''                        The next-hop that is to be used for the static route
                        - this may be specified as an IP address, an interface
                        or a pre-defined next-hop type - for instance, DROP or
                        LOCAL_LINK. When this leaf is not set, and the interface-ref
                        value is specified for the next-hop, then the system should
                        treat the prefix as though it is directly connected to the
                        interface.
                        ''',
                        'next_hop',
                        'openconfig-local-routing', False),
                ]),
            _MetaInfoClassMember('recurse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Determines whether the next-hop should be allowed to
                be looked up recursively - i.e., via a RIB entry which has
                been installed by a routing protocol, or another static route
                - rather than needing to be connected directly to an
                interface of the local system within the current network
                instance. When the interface reference specified within the
                next-hop entry is set (i.e., is not null) then forwarding is
                restricted to being via the interface specified - and
                recursion is hence disabled.
                ''',
                'recurse',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'config',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An user-specified identifier utilised to uniquely reference
                the next-hop entry in the next-hop list. The value of this
                index has no semantic meaning other than for referencing
                the entry.
                ''',
                'index',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A metric which is utilised to specify the preference of
                the next-hop entry when it is injected into the RIB. The
                lower the metric, the more preferable the prefix is. When
                this value is not specified the metric is inherited from
                the default metric utilised for static routes within the
                network instance that the static routes are being
                instantiated. When multiple next-hops are specified for a
                static route, the metric is utilised to determine which of
                the next-hops is to be installed in the RIB. When multiple
                next-hops have the same metric (be it specified, or simply
                the default) then these next-hops should all be installed
                in the RIB
                ''',
                'metric',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The next-hop that is to be used for the static route
                - this may be specified as an IP address, an interface
                or a pre-defined next-hop type - for instance, DROP or
                LOCAL_LINK. When this leaf is not set, and the interface-ref
                value is specified for the next-hop, then the system should
                treat the prefix as though it is directly connected to the
                interface.
                ''',
                'next_hop',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('next-hop', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        The next-hop that is to be used for the static route
                        - this may be specified as an IP address, an interface
                        or a pre-defined next-hop type - for instance, DROP or
                        LOCAL_LINK. When this leaf is not set, and the interface-ref
                        value is specified for the next-hop, then the system should
                        treat the prefix as though it is directly connected to the
                        interface.
                        ''',
                        'next_hop',
                        'openconfig-local-routing', False, [
                            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The next-hop that is to be used for the static route
                                - this may be specified as an IP address, an interface
                                or a pre-defined next-hop type - for instance, DROP or
                                LOCAL_LINK. When this leaf is not set, and the interface-ref
                                value is specified for the next-hop, then the system should
                                treat the prefix as though it is directly connected to the
                                interface.
                                ''',
                                'next_hop',
                                'openconfig-local-routing', False),
                            _MetaInfoClassMember('next-hop', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                The next-hop that is to be used for the static route
                                - this may be specified as an IP address, an interface
                                or a pre-defined next-hop type - for instance, DROP or
                                LOCAL_LINK. When this leaf is not set, and the interface-ref
                                value is specified for the next-hop, then the system should
                                treat the prefix as though it is directly connected to the
                                interface.
                                ''',
                                'next_hop',
                                'openconfig-local-routing', False),
                        ]),
                    _MetaInfoClassMember('next-hop', REFERENCE_IDENTITY_CLASS, 'Local_Defined_Next_HopIdentity' , 'ydk.models.openconfig.openconfig_local_routing', 'Local_Defined_Next_HopIdentity', 
                        [], [], 
                        '''                        The next-hop that is to be used for the static route
                        - this may be specified as an IP address, an interface
                        or a pre-defined next-hop type - for instance, DROP or
                        LOCAL_LINK. When this leaf is not set, and the interface-ref
                        value is specified for the next-hop, then the system should
                        treat the prefix as though it is directly connected to the
                        interface.
                        ''',
                        'next_hop',
                        'openconfig-local-routing', False),
                ]),
            _MetaInfoClassMember('recurse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Determines whether the next-hop should be allowed to
                be looked up recursively - i.e., via a RIB entry which has
                been installed by a routing protocol, or another static route
                - rather than needing to be connected directly to an
                interface of the local system within the current network
                instance. When the interface reference specified within the
                next-hop entry is set (i.e., is not null) then forwarding is
                restricted to being via the interface specified - and
                recursion is hence disabled.
                ''',
                'recurse',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'state',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to a base interface.  If a reference to a
                subinterface is required, this leaf must be specified
                to indicate the base interface.
                ''',
                'interface',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('subinterface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference to a subinterface -- this requires the base
                interface to be specified using the interface leaf in
                this container.  If only a reference to a base interface
                is requuired, this leaf should not be set.
                ''',
                'subinterface',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'config',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to a base interface.  If a reference to a
                subinterface is required, this leaf must be specified
                to indicate the base interface.
                ''',
                'interface',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('subinterface', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference to a subinterface -- this requires the base
                interface to be specified using the interface leaf in
                this container.  If only a reference to a base interface
                is requuired, this leaf should not be set.
                ''',
                'subinterface',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'state',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config', 
                [], [], 
                '''                Configured reference to interface / subinterface
                ''',
                'config',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State', 
                [], [], 
                '''                Operational state for interface-ref
                ''',
                'state',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'interface-ref',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.NextHops.NextHop' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.NextHops.NextHop',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A reference to the index of the current next-hop.
                The index is intended to be a user-specified value
                which can be used to reference the next-hop in
                question, without any other semantics being
                assigned to it.
                ''',
                'index',
                'openconfig-local-routing', True),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config', 
                [], [], 
                '''                Configuration parameters relating to the next-hop
                entry
                ''',
                'config',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('interface-ref', REFERENCE_CLASS, 'InterfaceRef' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef', 
                [], [], 
                '''                Reference to an interface or subinterface
                ''',
                'interface_ref',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State', 
                [], [], 
                '''                Operational state parameters relating to the
                next-hop entry
                ''',
                'state',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'next-hop',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static.NextHops' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static.NextHops',
            False, 
            [
            _MetaInfoClassMember('next-hop', REFERENCE_LIST, 'NextHop' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.NextHops.NextHop', 
                [], [], 
                '''                A list of next-hops to be utilised for the static
                route being specified.
                ''',
                'next_hop',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'next-hops',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes.Static' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes.Static',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Reference to the destination prefix list key.
                ''',
                'prefix',
                'openconfig-local-routing', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Reference to the destination prefix list key.
                        ''',
                        'prefix',
                        'openconfig-local-routing', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Reference to the destination prefix list key.
                        ''',
                        'prefix',
                        'openconfig-local-routing', True),
                ]),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.Config', 
                [], [], 
                '''                Configuration data for static routes
                ''',
                'config',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('next-hops', REFERENCE_CLASS, 'NextHops' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.NextHops', 
                [], [], 
                '''                Configuration and state parameters relating to the
                next-hops that are to be utilised for the static
                route being specified
                ''',
                'next_hops',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static.State', 
                [], [], 
                '''                Operational state data for static routes
                ''',
                'state',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'static',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.StaticRoutes' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.StaticRoutes',
            False, 
            [
            _MetaInfoClassMember('static', REFERENCE_LIST, 'Static' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes.Static', 
                [], [], 
                '''                List of locally configured static routes
                ''',
                'static',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'static-routes',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.LocalAggregates.Aggregate.Config' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.LocalAggregates.Aggregate.Config',
            False, 
            [
            _MetaInfoClassMember('discard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When true, install the aggregate route with a discard
                next-hop -- traffic destined to the aggregate will be
                discarded with no ICMP message generated.  When false,
                traffic destined to an aggregate address when no
                constituent routes are present will generate an ICMP
                unreachable message.
                ''',
                'discard',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Aggregate prefix to be advertised
                ''',
                'prefix',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Aggregate prefix to be advertised
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Aggregate prefix to be advertised
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                ]),
            _MetaInfoClassMember('set-tag', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set a generic tag value on the route. This tag can be
                used for filtering routes that are distributed to other
                routing protocols.
                ''',
                'set_tag',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'str' , None, None, 
                        [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                ]),
            ],
            'openconfig-local-routing',
            'config',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.LocalAggregates.Aggregate.State' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.LocalAggregates.Aggregate.State',
            False, 
            [
            _MetaInfoClassMember('discard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When true, install the aggregate route with a discard
                next-hop -- traffic destined to the aggregate will be
                discarded with no ICMP message generated.  When false,
                traffic destined to an aggregate address when no
                constituent routes are present will generate an ICMP
                unreachable message.
                ''',
                'discard',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Aggregate prefix to be advertised
                ''',
                'prefix',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Aggregate prefix to be advertised
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Aggregate prefix to be advertised
                        ''',
                        'prefix',
                        'openconfig-local-routing', False),
                ]),
            _MetaInfoClassMember('set-tag', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Set a generic tag value on the route. This tag can be
                used for filtering routes that are distributed to other
                routing protocols.
                ''',
                'set_tag',
                'openconfig-local-routing', False, [
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                    _MetaInfoClassMember('set-tag', ATTRIBUTE, 'str' , None, None, 
                        [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                        '''                        Set a generic tag value on the route. This tag can be
                        used for filtering routes that are distributed to other
                        routing protocols.
                        ''',
                        'set_tag',
                        'openconfig-local-routing', False),
                ]),
            ],
            'openconfig-local-routing',
            'state',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.LocalAggregates.Aggregate' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.LocalAggregates.Aggregate',
            False, 
            [
            _MetaInfoClassMember('prefix', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Reference to the configured prefix for this aggregate
                ''',
                'prefix',
                'openconfig-local-routing', True, [
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Reference to the configured prefix for this aggregate
                        ''',
                        'prefix',
                        'openconfig-local-routing', True),
                    _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Reference to the configured prefix for this aggregate
                        ''',
                        'prefix',
                        'openconfig-local-routing', True),
                ]),
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.LocalAggregates.Aggregate.Config', 
                [], [], 
                '''                Configuration data for aggregate advertisements
                ''',
                'config',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.LocalAggregates.Aggregate.State', 
                [], [], 
                '''                Operational state data for aggregate
                advertisements
                ''',
                'state',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'aggregate',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes.LocalAggregates' : {
        'meta_info' : _MetaInfoClass('LocalRoutes.LocalAggregates',
            False, 
            [
            _MetaInfoClassMember('aggregate', REFERENCE_LIST, 'Aggregate' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.LocalAggregates.Aggregate', 
                [], [], 
                '''                List of aggregates
                ''',
                'aggregate',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'local-aggregates',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'LocalRoutes' : {
        'meta_info' : _MetaInfoClass('LocalRoutes',
            False, 
            [
            _MetaInfoClassMember('config', REFERENCE_CLASS, 'Config' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.Config', 
                [], [], 
                '''                Configuration data for locally defined routes
                ''',
                'config',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('local-aggregates', REFERENCE_CLASS, 'LocalAggregates' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.LocalAggregates', 
                [], [], 
                '''                Enclosing container for locally-defined aggregate
                routes
                ''',
                'local_aggregates',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.State', 
                [], [], 
                '''                Operational state data for locally defined routes
                ''',
                'state',
                'openconfig-local-routing', False),
            _MetaInfoClassMember('static-routes', REFERENCE_CLASS, 'StaticRoutes' , 'ydk.models.openconfig.openconfig_local_routing', 'LocalRoutes.StaticRoutes', 
                [], [], 
                '''                Enclosing container for the list of static routes
                ''',
                'static_routes',
                'openconfig-local-routing', False),
            ],
            'openconfig-local-routing',
            'local-routes',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'DropIdentity' : {
        'meta_info' : _MetaInfoClass('DropIdentity',
            False, 
            [
            ],
            'openconfig-local-routing',
            'DROP',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
    'Local_LinkIdentity' : {
        'meta_info' : _MetaInfoClass('Local_LinkIdentity',
            False, 
            [
            ],
            'openconfig-local-routing',
            'LOCAL_LINK',
            _yang_ns._namespaces['openconfig-local-routing'],
        'ydk.models.openconfig.openconfig_local_routing'
        ),
    },
}
_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.Config']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef.State']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.Config']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.State']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop.InterfaceRef']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.NextHops.NextHop']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static.NextHops']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.Config']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.State']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static.NextHops']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes.Static']['meta_info']
_meta_table['LocalRoutes.StaticRoutes.Static']['meta_info'].parent =_meta_table['LocalRoutes.StaticRoutes']['meta_info']
_meta_table['LocalRoutes.LocalAggregates.Aggregate.Config']['meta_info'].parent =_meta_table['LocalRoutes.LocalAggregates.Aggregate']['meta_info']
_meta_table['LocalRoutes.LocalAggregates.Aggregate.State']['meta_info'].parent =_meta_table['LocalRoutes.LocalAggregates.Aggregate']['meta_info']
_meta_table['LocalRoutes.LocalAggregates.Aggregate']['meta_info'].parent =_meta_table['LocalRoutes.LocalAggregates']['meta_info']
_meta_table['LocalRoutes.Config']['meta_info'].parent =_meta_table['LocalRoutes']['meta_info']
_meta_table['LocalRoutes.State']['meta_info'].parent =_meta_table['LocalRoutes']['meta_info']
_meta_table['LocalRoutes.StaticRoutes']['meta_info'].parent =_meta_table['LocalRoutes']['meta_info']
_meta_table['LocalRoutes.LocalAggregates']['meta_info'].parent =_meta_table['LocalRoutes']['meta_info']
