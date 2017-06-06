


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AddressFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('AddressFamilyIdentity',
            False, 
            [
            ],
            'ietf-routing',
            'address-family',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingProtocolIdentity' : {
        'meta_info' : _MetaInfoClass('RoutingProtocolIdentity',
            False, 
            [
            ],
            'ietf-routing',
            'routing-protocol',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingInstanceIdentity' : {
        'meta_info' : _MetaInfoClass('RoutingInstanceIdentity',
            False, 
            [
            ],
            'ietf-routing',
            'routing-instance',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.Interfaces' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Each entry is a reference to the name of a configured
                network layer interface.
                ''',
                'interface',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'interfaces',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Interface cost for multi-area.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('multi-area-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Multi-area ID
                ''',
                'multi_area_id',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('multi-area-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Multi-area ID
                        ''',
                        'multi_area_id',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('multi-area-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Multi-area ID
                        ''',
                        'multi_area_id',
                        'ietf-ospf', False),
                ]),
            ],
            'ietf-ospf',
            'multi-area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP address.
                ''',
                'address',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP address.
                        ''',
                        'address',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP address.
                        ''',
                        'address',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Neighbor cost.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Neighbor poll interval.
                ''',
                'poll_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Neighbor priority for DR election.
                ''',
                'priority',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'neighbor',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor', 
                [], [], 
                '''                Specify a neighbor router.
                ''',
                'neighbor',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'static-neighbors',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Activates remote LFA.
                ''',
                'enabled',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'remote-lfa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa',
            False, 
            [
            _MetaInfoClassMember('candidate-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prevent the interface to be used as backup.
                ''',
                'candidate_disabled',
                'ietf-ospf', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Activates LFA.
                This model assumes activation of per-prefix LFA.
                ''',
                'enabled',
                'ietf-ospf', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration.
                ''',
                'remote_lfa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'lfa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute',
            False, 
            [
            _MetaInfoClassMember('lfa', REFERENCE_CLASS, 'Lfa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa', 
                [], [], 
                '''                LFA configuration.
                ''',
                'lfa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'fast-reroute',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable TTL security check.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('hops', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Maximum number of hops that a OSPF packet may
                have traveled.
                ''',
                'hops',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ttl-security',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm',
            False, 
            [
            _MetaInfoClassMember('hmac-sha1-12', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-12 algorithm.
                ''',
                'hmac_sha1_12',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha1-20', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-20 algorithm.
                ''',
                'hmac_sha1_20',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-1 authentication algorithm.
                ''',
                'hmac_sha_1',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-256', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-256 authentication algorithm.
                ''',
                'hmac_sha_256',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-384', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-384 authentication algorithm.
                ''',
                'hmac_sha_384',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-512', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-512 authentication algorithm.
                ''',
                'hmac_sha_512',
                'ietf-ospf', False),
            _MetaInfoClassMember('md5', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The MD5 algorithm.
                ''',
                'md5',
                'ietf-ospf', False),
            _MetaInfoClassMember('sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The SHA-1 algorithm.
                ''',
                'sha_1',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'crypto-algorithm',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication',
            False, 
            [
            _MetaInfoClassMember('crypto-algorithm', REFERENCE_CLASS, 'CryptoAlgorithm' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm', 
                [], [], 
                '''                Cryptographic algorithm associated with key.
                ''',
                'crypto_algorithm',
                'ietf-ospf', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key string in ASCII format.
                ''',
                'key',
                'ietf-ospf', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                key-chain name
                ''',
                'key_chain',
                'ietf-ospf', False),
            _MetaInfoClassMember('sa', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SA name
                ''',
                'sa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'authentication',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Neighbor ID.
                ''',
                'neighbor_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor address.
                ''',
                'address',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address.
                        ''',
                        'address',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor address.
                        ''',
                        'address',
                        'ietf-ospf', False),
                ]),
            _MetaInfoClassMember('bdr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Backup Designated Router.
                ''',
                'bdr',
                'ietf-ospf', False),
            _MetaInfoClassMember('dr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Designated Router.
                ''',
                'dr',
                'ietf-ospf', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'NbrStateTypeEnum' , 'ydk.models.ietf.ietf_ospf', 'NbrStateTypeEnum', 
                [], [], 
                '''                OSPF neighbor state.
                ''',
                'state',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'neighbor',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header',
            False, 
            [
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                LSA advertising router.
                ''',
                'adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA age.
                ''',
                'age',
                'ietf-ospf', False),
            _MetaInfoClassMember('checksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA checksum.
                ''',
                'checksum',
                'ietf-ospf', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Opaque id.
                ''',
                'opaque_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Opaque type.
                ''',
                'opaque_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header.Options', 
                [], [], 
                '''                LSA option.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('seq-num', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA sequence number.
                ''',
                'seq_num',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'header',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link',
            False, 
            [
            _MetaInfoClassMember('link-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link ID
                ''',
                'link_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link ID
                        ''',
                        'link_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Link ID
                        ''',
                        'link_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('link-data', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link data.
                ''',
                'link_data',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('link-data', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link data.
                        ''',
                        'link_data',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('link-data', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Link data.
                        ''',
                        'link_data',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Flags', 
                [], [], 
                '''                Flags
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link', 
                [], [], 
                '''                Router LSA link.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('num-of-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of links.
                ''',
                'num_of_links',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network',
            False, 
            [
            _MetaInfoClassMember('attached-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                List of the routers attached to the network.
                ''',
                'attached_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'network',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary',
            False, 
            [
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'summary',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External',
            False, 
            [
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'external',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV type.
                ''',
                'type',
                'ietf-ospf', True),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                TLV value.
                ''',
                'value',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'unknown-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv',
            False, 
            [
            _MetaInfoClassMember('router-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router address.
                ''',
                'router_address',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router-address-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV type.
                ''',
                'type',
                'ietf-ospf', True),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                TLV value.
                ''',
                'value',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'unknown-subtlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv',
            False, 
            [
            _MetaInfoClassMember('admin-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Administrative group/Resource class/Color.
                ''',
                'admin_group',
                'ietf-ospf', False),
            _MetaInfoClassMember('link-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link ID.
                ''',
                'link_id',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link ID.
                        ''',
                        'link_id',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Link ID.
                        ''',
                        'link_id',
                        'ietf-ospf', False),
                ]),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'link_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('local-if-ipv4-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                List of local interface IPv4 addresses.
                ''',
                'local_if_ipv4_addr',
                'ietf-ospf', False),
            _MetaInfoClassMember('local-remote-ipv4-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                List of remote interface IPv4 addresses.
                ''',
                'local_remote_ipv4_addr',
                'ietf-ospf', False),
            _MetaInfoClassMember('max-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Maximum bandwidth.
                ''',
                'max_bandwidth',
                'ietf-ospf', False),
            _MetaInfoClassMember('max-reservable-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Maximum reservable bandwidth.
                ''',
                'max_reservable_bandwidth',
                'ietf-ospf', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE metric.
                ''',
                'te_metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('unknown-subtlv', REFERENCE_LIST, 'UnknownSubtlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv', 
                [], [], 
                '''                Unknown sub-TLV.
                ''',
                'unknown_subtlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('unreserved-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Unreserved bandwidth.
                ''',
                'unreserved_bandwidth',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque',
            False, 
            [
            _MetaInfoClassMember('link-tlv', REFERENCE_CLASS, 'LinkTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv', 
                [], [], 
                '''                Link TLV.
                ''',
                'link_tlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('router-address-tlv', REFERENCE_CLASS, 'RouterAddressTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv', 
                [], [], 
                '''                Router address TLV.
                ''',
                'router_address_tlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv', 
                [], [], 
                '''                Unknown TLV.
                ''',
                'unknown_tlv',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'opaque',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body',
            False, 
            [
            _MetaInfoClassMember('external', REFERENCE_CLASS, 'External' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External', 
                [], [], 
                '''                External LSA.
                ''',
                'external',
                'ietf-ospf', False),
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network', 
                [], [], 
                '''                Network LSA.
                ''',
                'network',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque', REFERENCE_CLASS, 'Opaque' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque', 
                [], [], 
                '''                Opaque LSA.
                ''',
                'opaque',
                'ietf-ospf', False),
            _MetaInfoClassMember('router', REFERENCE_CLASS, 'Router' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router', 
                [], [], 
                '''                Router LSA.
                ''',
                'router',
                'ietf-ospf', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary', 
                [], [], 
                '''                Summary LSA.
                ''',
                'summary',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'body',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2',
            False, 
            [
            _MetaInfoClassMember('body', REFERENCE_CLASS, 'Body' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body', 
                [], [], 
                '''                Decoded OSPFv2 LSA body data.
                ''',
                'body',
                'ietf-ospf', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header', 
                [], [], 
                '''                Decoded OSPFv2 LSA header data.
                ''',
                'header',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospfv2',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header',
            False, 
            [
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                LSA advertising router.
                ''',
                'adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA age.
                ''',
                'age',
                'ietf-ospf', False),
            _MetaInfoClassMember('checksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA checksum.
                ''',
                'checksum',
                'ietf-ospf', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('seq-num', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA sequence number.
                ''',
                'seq_num',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'header',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link',
            False, 
            [
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface ID.
                ''',
                'interface_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('neighbor-interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Neighbor Interface ID.
                ''',
                'neighbor_interface_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('neighbor-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Neighbor Router ID
                ''',
                'neighbor_router_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric.
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Flags', 
                [], [], 
                '''                LSA option.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link', 
                [], [], 
                '''                Router LSA link.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network',
            False, 
            [
            _MetaInfoClassMember('attached-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                List of the routers attached to the network.
                ''',
                'attached_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'network',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'inter-area-prefix',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter',
            False, 
            [
            _MetaInfoClassMember('destination-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                The Router ID of the router being described by the LSA.
                ''',
                'destination_router_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'inter-area-router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal',
            False, 
            [
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'as-external',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa',
            False, 
            [
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'nssa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'prefix-list',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link',
            False, 
            [
            _MetaInfoClassMember('link-local-interface-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The originating router's link-local
                interface address on the link.
                ''',
                'link_local_interface_address',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('link-local-interface-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The originating router's link-local
                        interface address on the link.
                        ''',
                        'link_local_interface_address',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('link-local-interface-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The originating router's link-local
                        interface address on the link.
                        ''',
                        'link_local_interface_address',
                        'ietf-ospf', False),
                ]),
            _MetaInfoClassMember('num-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes.
                ''',
                'num_of_prefixes',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-list', REFERENCE_LIST, 'PrefixList' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList', 
                [], [], 
                '''                List of prefixes associated with the link.
                ''',
                'prefix_list',
                'ietf-ospf', False),
            _MetaInfoClassMember('rtr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Router Priority of the interface.
                ''',
                'rtr_priority',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'prefix-list',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix',
            False, 
            [
            _MetaInfoClassMember('num-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of prefixes.
                ''',
                'num_of_prefixes',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-list', REFERENCE_LIST, 'PrefixList' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList', 
                [], [], 
                '''                List of prefixes associated with the link.
                ''',
                'prefix_list',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Referenced Advertising Router.
                ''',
                'referenced_adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'intra-area-prefix',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body',
            False, 
            [
            _MetaInfoClassMember('as-external', REFERENCE_CLASS, 'AsExternal' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal', 
                [], [], 
                '''                AS-External LSA.
                ''',
                'as_external',
                'ietf-ospf', False),
            _MetaInfoClassMember('inter-area-prefix', REFERENCE_CLASS, 'InterAreaPrefix' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix', 
                [], [], 
                '''                Inter-Area-Prefix LSA.
                ''',
                'inter_area_prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('inter-area-router', REFERENCE_CLASS, 'InterAreaRouter' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter', 
                [], [], 
                '''                Inter-Area-Router LSA.
                ''',
                'inter_area_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('intra-area-prefix', REFERENCE_CLASS, 'IntraAreaPrefix' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix', 
                [], [], 
                '''                Intra-Area-Prefix LSA.
                ''',
                'intra_area_prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_CLASS, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link', 
                [], [], 
                '''                Link LSA.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network', 
                [], [], 
                '''                Network LSA.
                ''',
                'network',
                'ietf-ospf', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa', 
                [], [], 
                '''                NSSA LSA.
                ''',
                'nssa',
                'ietf-ospf', False),
            _MetaInfoClassMember('router', REFERENCE_CLASS, 'Router' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router', 
                [], [], 
                '''                Router LSA.
                ''',
                'router',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'body',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3',
            False, 
            [
            _MetaInfoClassMember('body', REFERENCE_CLASS, 'Body' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body', 
                [], [], 
                '''                Decoded OSPF LSA body data.
                ''',
                'body',
                'ietf-ospf', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header', 
                [], [], 
                '''                Decoded OSPFv3 LSA header data.
                ''',
                'header',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospfv3',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa',
            False, 
            [
            _MetaInfoClassMember('lsa-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSA ID.
                        ''',
                        'lsa_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        LSA ID.
                        ''',
                        'lsa_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Advertising router.
                ''',
                'adv_router',
                'ietf-ospf', True),
            _MetaInfoClassMember('decoded-completed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The OSPF LSA body is fully decoded.
                ''',
                'decoded_completed',
                'ietf-ospf', False),
            _MetaInfoClassMember('ospfv2', REFERENCE_CLASS, 'Ospfv2' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2', 
                [], [], 
                '''                OSPFv2 LSA
                ''',
                'ospfv2',
                'ietf-ospf', False),
            _MetaInfoClassMember('ospfv3', REFERENCE_CLASS, 'Ospfv3' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3', 
                [], [], 
                '''                OSPFv3 LSA
                ''',
                'ospfv3',
                'ietf-ospf', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The complete LSA in network byte
                order as received/sent over the wire.
                ''',
                'raw_data',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link-scope-lsa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas',
            False, 
            [
            _MetaInfoClassMember('lsa-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                OSPF link scope LSA type.
                ''',
                'lsa_type',
                'ietf-ospf', True),
            _MetaInfoClassMember('link-scope-lsa', REFERENCE_LIST, 'LinkScopeLsa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa', 
                [], [], 
                '''                List of OSPF link scope LSAs
                ''',
                'link_scope_lsa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link-scope-lsas',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                One of the topology enabled on this interface
                ''',
                'name',
                'ietf-ospf', True),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.NetworkTypeEnum' : _MetaInfoEnum('NetworkTypeEnum', 'ydk.models.ietf.ietf_routing',
        {
            'broadcast':'broadcast',
            'non-broadcast':'non_broadcast',
            'point-to-multipoint':'point_to_multipoint',
            'point-to-point':'point_to_point',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface.
                ''',
                'interface',
                'ietf-ospf', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication', 
                [], [], 
                '''                Authentication configuration.
                ''',
                'authentication',
                'ietf-ospf', False),
            _MetaInfoClassMember('bdr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                BDR.
                ''',
                'bdr',
                'ietf-ospf', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable bfd.
                ''',
                'bfd',
                'ietf-ospf', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared dead.
                ''',
                'dead_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable demand circuit.
                ''',
                'demand_circuit',
                'ietf-ospf', False),
            _MetaInfoClassMember('dr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                DR.
                ''',
                'dr',
                'ietf-ospf', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable protocol on the interface.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration.
                ''',
                'fast_reroute',
                'ietf-ospf', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between hello packets.
                ''',
                'hello_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('hello-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Hello timer.
                ''',
                'hello_timer',
                'ietf-ospf', False),
            _MetaInfoClassMember('link-scope-lsas', REFERENCE_LIST, 'LinkScopeLsas' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas', 
                [], [], 
                '''                List OSPF link scope LSA databases
                ''',
                'link_scope_lsas',
                'ietf-ospf', False),
            _MetaInfoClassMember('lls', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable link-local signaling (LLS) support.
                ''',
                'lls',
                'ietf-ospf', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets.
                ''',
                'mtu_ignore',
                'ietf-ospf', False),
            _MetaInfoClassMember('multi-area', REFERENCE_CLASS, 'MultiArea' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea', 
                [], [], 
                '''                Configure ospf multi-area.
                ''',
                'multi_area',
                'ietf-ospf', False),
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor', 
                [], [], 
                '''                List of OSPF neighbors.
                ''',
                'neighbor',
                'ietf-ospf', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'NetworkTypeEnum' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.NetworkTypeEnum', 
                [], [], 
                '''                Network type.
                ''',
                'network_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('node-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set prefix as a node representative prefix.
                ''',
                'node_flag',
                'ietf-ospf', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable passive.
                ''',
                'passive',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress advertisement of the prefixes.
                ''',
                'prefix_suppression',
                'ietf-ospf', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between retransmitting unacknowledged Link State
                Advertisements (LSAs).
                ''',
                'retransmit_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface state.
                ''',
                'state',
                'ietf-ospf', False),
            _MetaInfoClassMember('static-neighbors', REFERENCE_CLASS, 'StaticNeighbors' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors', 
                [], [], 
                '''                Static configured neighbors.
                ''',
                'static_neighbors',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology', 
                [], [], 
                '''                OSPF interface topology.
                ''',
                'topology',
                'ietf-ospf', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Estimated time needed to send link-state update.
                ''',
                'transmit_delay',
                'ietf-ospf', False),
            _MetaInfoClassMember('ttl-security', REFERENCE_CLASS, 'TtlSecurity' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity', 
                [], [], 
                '''                TTL security check.
                ''',
                'ttl_security',
                'ietf-ospf', False),
            _MetaInfoClassMember('wait-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wait timer.
                ''',
                'wait_timer',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'interfaces',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header',
            False, 
            [
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                LSA advertising router.
                ''',
                'adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA age.
                ''',
                'age',
                'ietf-ospf', False),
            _MetaInfoClassMember('checksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA checksum.
                ''',
                'checksum',
                'ietf-ospf', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Opaque id.
                ''',
                'opaque_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Opaque type.
                ''',
                'opaque_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header.Options', 
                [], [], 
                '''                LSA option.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('seq-num', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA sequence number.
                ''',
                'seq_num',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'header',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link',
            False, 
            [
            _MetaInfoClassMember('link-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link ID
                ''',
                'link_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link ID
                        ''',
                        'link_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Link ID
                        ''',
                        'link_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('link-data', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link data.
                ''',
                'link_data',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('link-data', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link data.
                        ''',
                        'link_data',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('link-data', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Link data.
                        ''',
                        'link_data',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Flags', 
                [], [], 
                '''                Flags
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link', 
                [], [], 
                '''                Router LSA link.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('num-of-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of links.
                ''',
                'num_of_links',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network',
            False, 
            [
            _MetaInfoClassMember('attached-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                List of the routers attached to the network.
                ''',
                'attached_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'network',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary',
            False, 
            [
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'summary',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External',
            False, 
            [
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'external',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV type.
                ''',
                'type',
                'ietf-ospf', True),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                TLV value.
                ''',
                'value',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'unknown-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv',
            False, 
            [
            _MetaInfoClassMember('router-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router address.
                ''',
                'router_address',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router-address-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV type.
                ''',
                'type',
                'ietf-ospf', True),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                TLV value.
                ''',
                'value',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'unknown-subtlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv',
            False, 
            [
            _MetaInfoClassMember('admin-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Administrative group/Resource class/Color.
                ''',
                'admin_group',
                'ietf-ospf', False),
            _MetaInfoClassMember('link-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link ID.
                ''',
                'link_id',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link ID.
                        ''',
                        'link_id',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Link ID.
                        ''',
                        'link_id',
                        'ietf-ospf', False),
                ]),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'link_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('local-if-ipv4-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                List of local interface IPv4 addresses.
                ''',
                'local_if_ipv4_addr',
                'ietf-ospf', False),
            _MetaInfoClassMember('local-remote-ipv4-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                List of remote interface IPv4 addresses.
                ''',
                'local_remote_ipv4_addr',
                'ietf-ospf', False),
            _MetaInfoClassMember('max-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Maximum bandwidth.
                ''',
                'max_bandwidth',
                'ietf-ospf', False),
            _MetaInfoClassMember('max-reservable-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Maximum reservable bandwidth.
                ''',
                'max_reservable_bandwidth',
                'ietf-ospf', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE metric.
                ''',
                'te_metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('unknown-subtlv', REFERENCE_LIST, 'UnknownSubtlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv', 
                [], [], 
                '''                Unknown sub-TLV.
                ''',
                'unknown_subtlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('unreserved-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Unreserved bandwidth.
                ''',
                'unreserved_bandwidth',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque',
            False, 
            [
            _MetaInfoClassMember('link-tlv', REFERENCE_CLASS, 'LinkTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv', 
                [], [], 
                '''                Link TLV.
                ''',
                'link_tlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('router-address-tlv', REFERENCE_CLASS, 'RouterAddressTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv', 
                [], [], 
                '''                Router address TLV.
                ''',
                'router_address_tlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv', 
                [], [], 
                '''                Unknown TLV.
                ''',
                'unknown_tlv',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'opaque',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body',
            False, 
            [
            _MetaInfoClassMember('external', REFERENCE_CLASS, 'External' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External', 
                [], [], 
                '''                External LSA.
                ''',
                'external',
                'ietf-ospf', False),
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network', 
                [], [], 
                '''                Network LSA.
                ''',
                'network',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque', REFERENCE_CLASS, 'Opaque' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque', 
                [], [], 
                '''                Opaque LSA.
                ''',
                'opaque',
                'ietf-ospf', False),
            _MetaInfoClassMember('router', REFERENCE_CLASS, 'Router' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router', 
                [], [], 
                '''                Router LSA.
                ''',
                'router',
                'ietf-ospf', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary', 
                [], [], 
                '''                Summary LSA.
                ''',
                'summary',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'body',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2',
            False, 
            [
            _MetaInfoClassMember('body', REFERENCE_CLASS, 'Body' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body', 
                [], [], 
                '''                Decoded OSPFv2 LSA body data.
                ''',
                'body',
                'ietf-ospf', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header', 
                [], [], 
                '''                Decoded OSPFv2 LSA header data.
                ''',
                'header',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospfv2',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header',
            False, 
            [
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                LSA advertising router.
                ''',
                'adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA age.
                ''',
                'age',
                'ietf-ospf', False),
            _MetaInfoClassMember('checksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA checksum.
                ''',
                'checksum',
                'ietf-ospf', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('seq-num', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA sequence number.
                ''',
                'seq_num',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'header',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link',
            False, 
            [
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface ID.
                ''',
                'interface_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('neighbor-interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Neighbor Interface ID.
                ''',
                'neighbor_interface_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('neighbor-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Neighbor Router ID
                ''',
                'neighbor_router_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric.
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Flags', 
                [], [], 
                '''                LSA option.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link', 
                [], [], 
                '''                Router LSA link.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network',
            False, 
            [
            _MetaInfoClassMember('attached-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                List of the routers attached to the network.
                ''',
                'attached_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'network',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'inter-area-prefix',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter',
            False, 
            [
            _MetaInfoClassMember('destination-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                The Router ID of the router being described by the LSA.
                ''',
                'destination_router_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'inter-area-router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal',
            False, 
            [
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'as-external',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa',
            False, 
            [
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'nssa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'prefix-list',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link',
            False, 
            [
            _MetaInfoClassMember('link-local-interface-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The originating router's link-local
                interface address on the link.
                ''',
                'link_local_interface_address',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('link-local-interface-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The originating router's link-local
                        interface address on the link.
                        ''',
                        'link_local_interface_address',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('link-local-interface-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The originating router's link-local
                        interface address on the link.
                        ''',
                        'link_local_interface_address',
                        'ietf-ospf', False),
                ]),
            _MetaInfoClassMember('num-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes.
                ''',
                'num_of_prefixes',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-list', REFERENCE_LIST, 'PrefixList' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList', 
                [], [], 
                '''                List of prefixes associated with the link.
                ''',
                'prefix_list',
                'ietf-ospf', False),
            _MetaInfoClassMember('rtr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Router Priority of the interface.
                ''',
                'rtr_priority',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'prefix-list',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix',
            False, 
            [
            _MetaInfoClassMember('num-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of prefixes.
                ''',
                'num_of_prefixes',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-list', REFERENCE_LIST, 'PrefixList' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList', 
                [], [], 
                '''                List of prefixes associated with the link.
                ''',
                'prefix_list',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Referenced Advertising Router.
                ''',
                'referenced_adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'intra-area-prefix',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body',
            False, 
            [
            _MetaInfoClassMember('as-external', REFERENCE_CLASS, 'AsExternal' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal', 
                [], [], 
                '''                AS-External LSA.
                ''',
                'as_external',
                'ietf-ospf', False),
            _MetaInfoClassMember('inter-area-prefix', REFERENCE_CLASS, 'InterAreaPrefix' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix', 
                [], [], 
                '''                Inter-Area-Prefix LSA.
                ''',
                'inter_area_prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('inter-area-router', REFERENCE_CLASS, 'InterAreaRouter' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter', 
                [], [], 
                '''                Inter-Area-Router LSA.
                ''',
                'inter_area_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('intra-area-prefix', REFERENCE_CLASS, 'IntraAreaPrefix' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix', 
                [], [], 
                '''                Intra-Area-Prefix LSA.
                ''',
                'intra_area_prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_CLASS, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link', 
                [], [], 
                '''                Link LSA.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network', 
                [], [], 
                '''                Network LSA.
                ''',
                'network',
                'ietf-ospf', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa', 
                [], [], 
                '''                NSSA LSA.
                ''',
                'nssa',
                'ietf-ospf', False),
            _MetaInfoClassMember('router', REFERENCE_CLASS, 'Router' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router', 
                [], [], 
                '''                Router LSA.
                ''',
                'router',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'body',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3',
            False, 
            [
            _MetaInfoClassMember('body', REFERENCE_CLASS, 'Body' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body', 
                [], [], 
                '''                Decoded OSPF LSA body data.
                ''',
                'body',
                'ietf-ospf', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header', 
                [], [], 
                '''                Decoded OSPFv3 LSA header data.
                ''',
                'header',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospfv3',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa',
            False, 
            [
            _MetaInfoClassMember('lsa-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSA ID.
                        ''',
                        'lsa_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        LSA ID.
                        ''',
                        'lsa_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Advertising router.
                ''',
                'adv_router',
                'ietf-ospf', True),
            _MetaInfoClassMember('decoded-completed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The OSPF LSA body is fully decoded.
                ''',
                'decoded_completed',
                'ietf-ospf', False),
            _MetaInfoClassMember('ospfv2', REFERENCE_CLASS, 'Ospfv2' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2', 
                [], [], 
                '''                OSPFv2 LSA
                ''',
                'ospfv2',
                'ietf-ospf', False),
            _MetaInfoClassMember('ospfv3', REFERENCE_CLASS, 'Ospfv3' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3', 
                [], [], 
                '''                OSPFv3 LSA
                ''',
                'ospfv3',
                'ietf-ospf', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The complete LSA in network byte
                order as received/sent over the wire.
                ''',
                'raw_data',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'area-scope-lsa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas',
            False, 
            [
            _MetaInfoClassMember('lsa-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                OSPF area scope LSA type.
                ''',
                'lsa_type',
                'ietf-ospf', True),
            _MetaInfoClassMember('area-scope-lsa', REFERENCE_LIST, 'AreaScopeLsa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa', 
                [], [], 
                '''                List of OSPF area scope LSAs
                ''',
                'area_scope_lsa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'area-scope-lsas',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area',
            False, 
            [
            _MetaInfoClassMember('area-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Area ID.
                ''',
                'area_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('area-scope-lsas', REFERENCE_LIST, 'AreaScopeLsas' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas', 
                [], [], 
                '''                List OSPF area scope LSA databases
                ''',
                'area_scope_lsas',
                'ietf-ospf', False),
            _MetaInfoClassMember('interfaces', REFERENCE_LIST, 'Interfaces' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces', 
                [], [], 
                '''                List of OSPF interfaces.
                ''',
                'interfaces',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header',
            False, 
            [
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                LSA advertising router.
                ''',
                'adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA age.
                ''',
                'age',
                'ietf-ospf', False),
            _MetaInfoClassMember('checksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA checksum.
                ''',
                'checksum',
                'ietf-ospf', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Opaque id.
                ''',
                'opaque_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Opaque type.
                ''',
                'opaque_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header.Options', 
                [], [], 
                '''                LSA option.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('seq-num', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA sequence number.
                ''',
                'seq_num',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'header',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link',
            False, 
            [
            _MetaInfoClassMember('link-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link ID
                ''',
                'link_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link ID
                        ''',
                        'link_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Link ID
                        ''',
                        'link_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('link-data', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link data.
                ''',
                'link_data',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('link-data', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link data.
                        ''',
                        'link_data',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('link-data', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Link data.
                        ''',
                        'link_data',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Flags', 
                [], [], 
                '''                Flags
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link', 
                [], [], 
                '''                Router LSA link.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('num-of-links', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of links.
                ''',
                'num_of_links',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network',
            False, 
            [
            _MetaInfoClassMember('attached-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                List of the routers attached to the network.
                ''',
                'attached_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'network',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary',
            False, 
            [
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'summary',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology',
            False, 
            [
            _MetaInfoClassMember('mt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The MT-ID for topology enabled on the link.
                ''',
                'mt_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric for the topology.
                ''',
                'metric',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External',
            False, 
            [
            _MetaInfoClassMember('network-mask', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address mask for the network
                ''',
                'network_mask',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology', 
                [], [], 
                '''                Topology specific information.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'external',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV type.
                ''',
                'type',
                'ietf-ospf', True),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                TLV value.
                ''',
                'value',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'unknown-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv',
            False, 
            [
            _MetaInfoClassMember('router-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router address.
                ''',
                'router_address',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router-address-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv',
            False, 
            [
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV type.
                ''',
                'type',
                'ietf-ospf', True),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                TLV length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                TLV value.
                ''',
                'value',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'unknown-subtlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv',
            False, 
            [
            _MetaInfoClassMember('admin-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Administrative group/Resource class/Color.
                ''',
                'admin_group',
                'ietf-ospf', False),
            _MetaInfoClassMember('link-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Link ID.
                ''',
                'link_id',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Link ID.
                        ''',
                        'link_id',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('link-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Link ID.
                        ''',
                        'link_id',
                        'ietf-ospf', False),
                ]),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'link_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('local-if-ipv4-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                List of local interface IPv4 addresses.
                ''',
                'local_if_ipv4_addr',
                'ietf-ospf', False),
            _MetaInfoClassMember('local-remote-ipv4-addr', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                List of remote interface IPv4 addresses.
                ''',
                'local_remote_ipv4_addr',
                'ietf-ospf', False),
            _MetaInfoClassMember('max-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Maximum bandwidth.
                ''',
                'max_bandwidth',
                'ietf-ospf', False),
            _MetaInfoClassMember('max-reservable-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Maximum reservable bandwidth.
                ''',
                'max_reservable_bandwidth',
                'ietf-ospf', False),
            _MetaInfoClassMember('te-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                TE metric.
                ''',
                'te_metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('unknown-subtlv', REFERENCE_LIST, 'UnknownSubtlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv', 
                [], [], 
                '''                Unknown sub-TLV.
                ''',
                'unknown_subtlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('unreserved-bandwidth', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Unreserved bandwidth.
                ''',
                'unreserved_bandwidth',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link-tlv',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque',
            False, 
            [
            _MetaInfoClassMember('link-tlv', REFERENCE_CLASS, 'LinkTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv', 
                [], [], 
                '''                Link TLV.
                ''',
                'link_tlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('router-address-tlv', REFERENCE_CLASS, 'RouterAddressTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv', 
                [], [], 
                '''                Router address TLV.
                ''',
                'router_address_tlv',
                'ietf-ospf', False),
            _MetaInfoClassMember('unknown-tlv', REFERENCE_LIST, 'UnknownTlv' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv', 
                [], [], 
                '''                Unknown TLV.
                ''',
                'unknown_tlv',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'opaque',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body',
            False, 
            [
            _MetaInfoClassMember('external', REFERENCE_CLASS, 'External' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External', 
                [], [], 
                '''                External LSA.
                ''',
                'external',
                'ietf-ospf', False),
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network', 
                [], [], 
                '''                Network LSA.
                ''',
                'network',
                'ietf-ospf', False),
            _MetaInfoClassMember('opaque', REFERENCE_CLASS, 'Opaque' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque', 
                [], [], 
                '''                Opaque LSA.
                ''',
                'opaque',
                'ietf-ospf', False),
            _MetaInfoClassMember('router', REFERENCE_CLASS, 'Router' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router', 
                [], [], 
                '''                Router LSA.
                ''',
                'router',
                'ietf-ospf', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary', 
                [], [], 
                '''                Summary LSA.
                ''',
                'summary',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'body',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2',
            False, 
            [
            _MetaInfoClassMember('body', REFERENCE_CLASS, 'Body' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body', 
                [], [], 
                '''                Decoded OSPFv2 LSA body data.
                ''',
                'body',
                'ietf-ospf', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header', 
                [], [], 
                '''                Decoded OSPFv2 LSA header data.
                ''',
                'header',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospfv2',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header',
            False, 
            [
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                LSA advertising router.
                ''',
                'adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA age.
                ''',
                'age',
                'ietf-ospf', False),
            _MetaInfoClassMember('checksum', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA checksum.
                ''',
                'checksum',
                'ietf-ospf', False),
            _MetaInfoClassMember('length', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA length.
                ''',
                'length',
                'ietf-ospf', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('seq-num', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSA sequence number.
                ''',
                'seq_num',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                LSA type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'header',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link',
            False, 
            [
            _MetaInfoClassMember('interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface ID.
                ''',
                'interface_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('neighbor-interface-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Neighbor Interface ID.
                ''',
                'neighbor_interface_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('neighbor-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Neighbor Router ID
                ''',
                'neighbor_router_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Metric.
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Link type.
                ''',
                'type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Flags', 
                [], [], 
                '''                LSA option.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_LIST, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link', 
                [], [], 
                '''                Router LSA link.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network',
            False, 
            [
            _MetaInfoClassMember('attached-router', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                List of the routers attached to the network.
                ''',
                'attached_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'network',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix',
            False, 
            [
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'inter-area-prefix',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter',
            False, 
            [
            _MetaInfoClassMember('destination-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                The Router ID of the router being described by the LSA.
                ''',
                'destination_router_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'inter-area-router',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal',
            False, 
            [
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'as-external',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa',
            False, 
            [
            _MetaInfoClassMember('external-route-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route tag.
                ''',
                'external_route_tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('flags', REFERENCE_BITS, 'Flags' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa.Flags', 
                [], [], 
                '''                Flags.
                ''',
                'flags',
                'ietf-ospf', False),
            _MetaInfoClassMember('forwarding-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Forwarding address.
                ''',
                'forwarding_address',
                'ietf-ospf', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'nssa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'prefix-list',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link',
            False, 
            [
            _MetaInfoClassMember('link-local-interface-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The originating router's link-local
                interface address on the link.
                ''',
                'link_local_interface_address',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('link-local-interface-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The originating router's link-local
                        interface address on the link.
                        ''',
                        'link_local_interface_address',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('link-local-interface-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        The originating router's link-local
                        interface address on the link.
                        ''',
                        'link_local_interface_address',
                        'ietf-ospf', False),
                ]),
            _MetaInfoClassMember('num-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of prefixes.
                ''',
                'num_of_prefixes',
                'ietf-ospf', False),
            _MetaInfoClassMember('options', REFERENCE_BITS, 'Options' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.Options', 
                [], [], 
                '''                OSPFv3 LSA options.
                ''',
                'options',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-list', REFERENCE_LIST, 'PrefixList' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList', 
                [], [], 
                '''                List of prefixes associated with the link.
                ''',
                'prefix_list',
                'ietf-ospf', False),
            _MetaInfoClassMember('rtr-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Router Priority of the interface.
                ''',
                'rtr_priority',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Metric
                ''',
                'metric',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-options', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix options.
                ''',
                'prefix_options',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'prefix-list',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix',
            False, 
            [
            _MetaInfoClassMember('num-of-prefixes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of prefixes.
                ''',
                'num_of_prefixes',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-list', REFERENCE_LIST, 'PrefixList' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList', 
                [], [], 
                '''                List of prefixes associated with the link.
                ''',
                'prefix_list',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Referenced Advertising Router.
                ''',
                'referenced_adv_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-link-state-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced Link State ID.
                ''',
                'referenced_link_state_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('referenced-ls-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Referenced Link State type.
                ''',
                'referenced_ls_type',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'intra-area-prefix',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body',
            False, 
            [
            _MetaInfoClassMember('as-external', REFERENCE_CLASS, 'AsExternal' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal', 
                [], [], 
                '''                AS-External LSA.
                ''',
                'as_external',
                'ietf-ospf', False),
            _MetaInfoClassMember('inter-area-prefix', REFERENCE_CLASS, 'InterAreaPrefix' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix', 
                [], [], 
                '''                Inter-Area-Prefix LSA.
                ''',
                'inter_area_prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('inter-area-router', REFERENCE_CLASS, 'InterAreaRouter' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter', 
                [], [], 
                '''                Inter-Area-Router LSA.
                ''',
                'inter_area_router',
                'ietf-ospf', False),
            _MetaInfoClassMember('intra-area-prefix', REFERENCE_CLASS, 'IntraAreaPrefix' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix', 
                [], [], 
                '''                Intra-Area-Prefix LSA.
                ''',
                'intra_area_prefix',
                'ietf-ospf', False),
            _MetaInfoClassMember('link', REFERENCE_CLASS, 'Link' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link', 
                [], [], 
                '''                Link LSA.
                ''',
                'link',
                'ietf-ospf', False),
            _MetaInfoClassMember('network', REFERENCE_CLASS, 'Network' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network', 
                [], [], 
                '''                Network LSA.
                ''',
                'network',
                'ietf-ospf', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa', 
                [], [], 
                '''                NSSA LSA.
                ''',
                'nssa',
                'ietf-ospf', False),
            _MetaInfoClassMember('router', REFERENCE_CLASS, 'Router' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router', 
                [], [], 
                '''                Router LSA.
                ''',
                'router',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'body',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3',
            False, 
            [
            _MetaInfoClassMember('body', REFERENCE_CLASS, 'Body' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body', 
                [], [], 
                '''                Decoded OSPF LSA body data.
                ''',
                'body',
                'ietf-ospf', False),
            _MetaInfoClassMember('header', REFERENCE_CLASS, 'Header' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header', 
                [], [], 
                '''                Decoded OSPFv3 LSA header data.
                ''',
                'header',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospfv3',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa',
            False, 
            [
            _MetaInfoClassMember('lsa-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                LSA ID.
                ''',
                'lsa_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        LSA ID.
                        ''',
                        'lsa_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        LSA ID.
                        ''',
                        'lsa_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('adv-router', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Advertising router.
                ''',
                'adv_router',
                'ietf-ospf', True),
            _MetaInfoClassMember('decoded-completed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The OSPF LSA body is fully decoded.
                ''',
                'decoded_completed',
                'ietf-ospf', False),
            _MetaInfoClassMember('ospfv2', REFERENCE_CLASS, 'Ospfv2' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2', 
                [], [], 
                '''                OSPFv2 LSA
                ''',
                'ospfv2',
                'ietf-ospf', False),
            _MetaInfoClassMember('ospfv3', REFERENCE_CLASS, 'Ospfv3' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3', 
                [], [], 
                '''                OSPFv3 LSA
                ''',
                'ospfv3',
                'ietf-ospf', False),
            _MetaInfoClassMember('raw-data', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                The complete LSA in network byte
                order as received/sent over the wire.
                ''',
                'raw_data',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'as-scope-lsa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas',
            False, 
            [
            _MetaInfoClassMember('lsa-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                OSPF AS scope LSA type.
                ''',
                'lsa_type',
                'ietf-ospf', True),
            _MetaInfoClassMember('as-scope-lsa', REFERENCE_LIST, 'AsScopeLsa' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa', 
                [], [], 
                '''                List of OSPF AS scope LSAs
                ''',
                'as_scope_lsa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'as-scope-lsas',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area',
            False, 
            [
            _MetaInfoClassMember('area-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Area ID.
                ''',
                'area_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                ]),
            ],
            'ietf-ospf',
            'area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RIB
                ''',
                'name',
                'ietf-ospf', True),
            _MetaInfoClassMember('area', REFERENCE_LIST, 'Area' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area', 
                [], [], 
                '''                List of ospf areas
                ''',
                'area',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_routing', 'AddressFamilyIdentity', 
                [], [], 
                '''                Address-family of the instance.
                ''',
                'af',
                'ietf-ospf', True),
            _MetaInfoClassMember('area', REFERENCE_LIST, 'Area' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area', 
                [], [], 
                '''                List of OSPF areas
                ''',
                'area',
                'ietf-ospf', False),
            _MetaInfoClassMember('as-scope-lsas', REFERENCE_LIST, 'AsScopeLsas' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas', 
                [], [], 
                '''                List OSPF AS scope LSA databases
                ''',
                'as_scope_lsas',
                'ietf-ospf', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Defined in RFC 2328. A 32-bit number
                that uniquely identifies the router.
                ''',
                'router_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology', 
                [], [], 
                '''                OSPF topology.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'instance',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance', 
                [], [], 
                '''                An OSPF routing protocol instance.
                ''',
                'instance',
                'ietf-ospf', False),
            _MetaInfoClassMember('operation-mode', REFERENCE_IDENTITY_CLASS, 'OperationModeIdentity' , 'ydk.models.ietf.ietf_ospf', 'OperationModeIdentity', 
                [], [], 
                '''                OSPF operation mode.
                ''',
                'operation_mode',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospf',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'RoutingProtocolIdentity' , 'ydk.models.ietf.ietf_routing', 'RoutingProtocolIdentity', 
                [], [], 
                '''                Type of the routing protocol.
                ''',
                'type',
                'ietf-routing', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the routing protocol instance.
                
                For system-controlled instances this name is
                persistent, i.e., it SHOULD NOT change across
                reboots.
                ''',
                'name',
                'ietf-routing', True),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf', 
                [], [], 
                '''                OSPF
                ''',
                'ospf',
                'ietf-ospf', False),
            ],
            'ietf-routing',
            'routing-protocol',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.RoutingProtocols' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.RoutingProtocols',
            False, 
            [
            _MetaInfoClassMember('routing-protocol', REFERENCE_LIST, 'RoutingProtocol' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol', 
                [], [], 
                '''                State data of a routing protocol instance.
                
                An implementation MUST provide exactly one
                system-controlled instance of the type 'direct'. Other
                instances MAY be created by configuration.
                ''',
                'routing_protocol',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'routing-protocols',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop.SpecialNextHopEnum' : _MetaInfoEnum('SpecialNextHopEnum', 'ydk.models.ietf.ietf_routing',
        {
            'blackhole':'blackhole',
            'unreachable':'unreachable',
            'prohibit':'prohibit',
            'receive':'receive',
        }, 'ietf-routing', _yang_ns._namespaces['ietf-routing']),
    'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop',
            False, 
            [
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address.
                ''',
                'next_hop_address',
                'ietf-routing', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-routing', False),
            _MetaInfoClassMember('special-next-hop', REFERENCE_ENUM_CLASS, 'SpecialNextHopEnum' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop.SpecialNextHopEnum', 
                [], [], 
                '''                Special next-hop options.
                ''',
                'special_next_hop',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'next-hop',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.RouteTypeEnum' : _MetaInfoEnum('RouteTypeEnum', 'ydk.models.ietf.ietf_routing',
        {
            'intra-area':'intra_area',
            'inter-area':'inter_area',
            'external-1':'external_1',
            'external-2':'external_2',
            'nssa-1':'nssa_1',
            'nssa-2':'nssa_2',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.Ribs.Rib.Routes.Route',
            False, 
            [
            _MetaInfoClassMember('destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Destination IP address with prefix
                ''',
                'destination_prefix',
                'ietf-routing', True),
            _MetaInfoClassMember('active', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Presence of this leaf indicates that the route is preferred
                among all routes in the same RIB that have the same
                destination prefix.
                ''',
                'active',
                'ietf-routing', False),
            _MetaInfoClassMember('last-updated', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Time stamp of the last modification of the route. If the
                route was never modified, it is the time when the route was
                inserted into the RIB.
                ''',
                'last_updated',
                'ietf-routing', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route metric.
                ''',
                'metric',
                'ietf-routing', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop', 
                [], [], 
                '''                Route's next-hop attribute.
                ''',
                'next_hop',
                'ietf-routing', False),
            _MetaInfoClassMember('route-preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This route attribute, also known as administrative
                distance, allows for selecting the preferred route
                among routes with the same destination prefix. A
                smaller value means a more preferred route.
                ''',
                'route_preference',
                'ietf-routing', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RouteTypeEnum' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.RouteTypeEnum', 
                [], [], 
                '''                OSPF route type
                ''',
                'route_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('source-protocol', REFERENCE_IDENTITY_CLASS, 'RoutingProtocolIdentity' , 'ydk.models.ietf.ietf_routing', 'RoutingProtocolIdentity', 
                [], [], 
                '''                Type of the routing protocol from which the route
                originated.
                ''',
                'source_protocol',
                'ietf-routing', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OSPF route tag.
                ''',
                'tag',
                'ietf-ospf', False),
            _MetaInfoClassMember('update-source', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Update source for the route.
                ''',
                'update_source',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'route',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.Ribs.Rib.Routes' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.Ribs.Rib.Routes',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Ribs.Rib.Routes.Route', 
                [], [], 
                '''                A RIB route entry. This data node MUST be augmented
                with information specific for routes of each address
                family.
                ''',
                'route',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'routes',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.Ribs.Rib' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.Ribs.Rib',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the RIB.
                ''',
                'name',
                'ietf-routing', True),
            _MetaInfoClassMember('address-family', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_routing', 'AddressFamilyIdentity', 
                [], [], 
                '''                Address family.
                ''',
                'address_family',
                'ietf-routing', False),
            _MetaInfoClassMember('default-rib', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This flag has the value of 'true' if and only if the
                RIB is the default RIB for the given address family.
                
                A default RIB always receives direct routes. By
                default it also receives routes from all routing
                protocols.
                ''',
                'default_rib',
                'ietf-routing', False),
            _MetaInfoClassMember('routes', REFERENCE_CLASS, 'Routes' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Ribs.Rib.Routes', 
                [], [], 
                '''                Current content of the RIB.
                ''',
                'routes',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'rib',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance.Ribs' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance.Ribs',
            False, 
            [
            _MetaInfoClassMember('rib', REFERENCE_LIST, 'Rib' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Ribs.Rib', 
                [], [], 
                '''                Each entry represents a RIB identified by the 'name'
                key. All routes in a RIB MUST belong to the same address
                family.
                
                For each routing instance, an implementation SHOULD
                provide one system-controlled default RIB for each
                supported address family.
                ''',
                'rib',
                'ietf-routing', False, min_elements=1),
            ],
            'ietf-routing',
            'ribs',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState.RoutingInstance' : {
        'meta_info' : _MetaInfoClass('RoutingState.RoutingInstance',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the routing instance.
                
                For system-controlled instances the name is persistent,
                i.e., it SHOULD NOT change across reboots.
                ''',
                'name',
                'ietf-routing', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Interfaces', 
                [], [], 
                '''                Network layer interfaces belonging to the routing
                instance.
                ''',
                'interfaces',
                'ietf-routing', False),
            _MetaInfoClassMember('ribs', REFERENCE_CLASS, 'Ribs' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.Ribs', 
                [], [], 
                '''                Container for RIBs.
                ''',
                'ribs',
                'ietf-routing', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                A 32-bit number in the form of a dotted quad that is used by
                some routing protocols identifying a router.
                ''',
                'router_id',
                'ietf-routing', False),
            _MetaInfoClassMember('routing-protocols', REFERENCE_CLASS, 'RoutingProtocols' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance.RoutingProtocols', 
                [], [], 
                '''                Container for the list of routing protocol instances.
                ''',
                'routing_protocols',
                'ietf-routing', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'RoutingInstanceIdentity' , 'ydk.models.ietf.ietf_routing', 'RoutingInstanceIdentity', 
                [], [], 
                '''                The routing instance type.
                ''',
                'type',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'routing-instance',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'RoutingState' : {
        'meta_info' : _MetaInfoClass('RoutingState',
            False, 
            [
            _MetaInfoClassMember('routing-instance', REFERENCE_LIST, 'RoutingInstance' , 'ydk.models.ietf.ietf_routing', 'RoutingState.RoutingInstance', 
                [], [], 
                '''                Each list entry is a container for state data of a routing
                instance.
                
                An implementation MUST support routing instance(s) of the
                type 'rt:default-routing-instance', and MAY support other
                types. An implementation MAY restrict the number of routing
                instances of each supported type.
                
                An implementation SHOULD create at least one
                system-controlled instance, and MAY allow the clients to
                create user-controlled routing instances in
                configuration.
                ''',
                'routing_instance',
                'ietf-routing', False, min_elements=1),
            ],
            'ietf-routing',
            'routing-state',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.Interfaces' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                The name of a configured network layer interface to be
                assigned to the routing-instance.
                ''',
                'interface',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'interfaces',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop.SpecialNextHopEnum' : _MetaInfoEnum('SpecialNextHopEnum', 'ydk.models.ietf.ietf_routing',
        {
            'blackhole':'blackhole',
            'unreachable':'unreachable',
            'prohibit':'prohibit',
            'receive':'receive',
        }, 'ietf-routing', _yang_ns._namespaces['ietf-routing']),
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop',
            False, 
            [
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the next-hop.
                ''',
                'next_hop_address',
                'ietf-ipv4-unicast-routing', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-ipv4-unicast-routing', False),
            _MetaInfoClassMember('special-next-hop', REFERENCE_ENUM_CLASS, 'SpecialNextHopEnum' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop.SpecialNextHopEnum', 
                [], [], 
                '''                Special next-hop options.
                ''',
                'special_next_hop',
                'ietf-ipv4-unicast-routing', False),
            ],
            'ietf-ipv4-unicast-routing',
            'next-hop',
            _yang_ns._namespaces['ietf-ipv4-unicast-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route',
            False, 
            [
            _MetaInfoClassMember('destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                IPv4 destination prefix.
                ''',
                'destination_prefix',
                'ietf-ipv4-unicast-routing', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Textual description of the route.
                ''',
                'description',
                'ietf-ipv4-unicast-routing', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop', 
                [], [], 
                '''                Configuration of next-hop.
                ''',
                'next_hop',
                'ietf-ipv4-unicast-routing', False),
            ],
            'ietf-ipv4-unicast-routing',
            'route',
            _yang_ns._namespaces['ietf-ipv4-unicast-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route', 
                [], [], 
                '''                A user-ordered list of static routes.
                ''',
                'route',
                'ietf-ipv4-unicast-routing', False),
            ],
            'ietf-ipv4-unicast-routing',
            'ipv4',
            _yang_ns._namespaces['ietf-ipv4-unicast-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop.SpecialNextHopEnum' : _MetaInfoEnum('SpecialNextHopEnum', 'ydk.models.ietf.ietf_routing',
        {
            'blackhole':'blackhole',
            'unreachable':'unreachable',
            'prohibit':'prohibit',
            'receive':'receive',
        }, 'ietf-routing', _yang_ns._namespaces['ietf-routing']),
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop',
            False, 
            [
            _MetaInfoClassMember('next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address of the next-hop.
                ''',
                'next_hop_address',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('special-next-hop', REFERENCE_ENUM_CLASS, 'SpecialNextHopEnum' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop.SpecialNextHopEnum', 
                [], [], 
                '''                Special next-hop options.
                ''',
                'special_next_hop',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-ipv6-unicast-routing',
            'next-hop',
            _yang_ns._namespaces['ietf-ipv6-unicast-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route',
            False, 
            [
            _MetaInfoClassMember('destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                IPv6 destination prefix.
                ''',
                'destination_prefix',
                'ietf-ipv6-unicast-routing', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Textual description of the route.
                ''',
                'description',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop', 
                [], [], 
                '''                Configuration of next-hop.
                ''',
                'next_hop',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-ipv6-unicast-routing',
            'route',
            _yang_ns._namespaces['ietf-ipv6-unicast-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_LIST, 'Route' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route', 
                [], [], 
                '''                A user-ordered list of static routes.
                ''',
                'route',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-ipv6-unicast-routing',
            'ipv6',
            _yang_ns._namespaces['ietf-ipv6-unicast-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4', 
                [], [], 
                '''                Configuration of a 'static' pseudo-protocol instance
                consists of a list of routes.
                ''',
                'ipv4',
                'ietf-ipv4-unicast-routing', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6', 
                [], [], 
                '''                Configuration of a 'static' pseudo-protocol instance
                consists of a list of routes.
                ''',
                'ipv6',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-routing',
            'static-routes',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area',
            False, 
            [
            ],
            'ietf-ospf',
            'area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface',
            False, 
            [
            ],
            'ietf-ospf',
            'interface',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit',
            False, 
            [
            _MetaInfoClassMember('area', REFERENCE_CLASS, 'Area' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area', 
                [], [], 
                '''                Area config to be inherited by all areas in
                all instances.
                ''',
                'area',
                'ietf-ospf', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface', 
                [], [], 
                '''                Interface config to be inherited by all interfaces
                in all instances.
                ''',
                'interface',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'all-instances-inherit',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance',
            False, 
            [
            _MetaInfoClassMember('external', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Admin distance for both external route.
                ''',
                'external',
                'ietf-ospf', False),
            _MetaInfoClassMember('inter-area', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Admin distance for inter-area route.
                ''',
                'inter_area',
                'ietf-ospf', False),
            _MetaInfoClassMember('internal', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Admin distance for both intra-area and
                inter-area route.
                ''',
                'internal',
                'ietf-ospf', False),
            _MetaInfoClassMember('intra-area', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Admin distance for intra-area route.
                ''',
                'intra_area',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'admin-distance',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable NSR.
                ''',
                'enable',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'nsr',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable graceful restart as defined in RFC 3623.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('helper-enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable RestartHelperSupport in RFC 3623 Section B.2.
                ''',
                'helper_enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('helper-strict-lsa-checking', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                RestartHelperStrictLSAChecking option in RFC 3623
                Section B.2.
                ''',
                'helper_strict_lsa_checking',
                'ietf-ospf', False),
            _MetaInfoClassMember('restart-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '1800')], [], 
                '''                RestartInterval option in RFC 3623 Section B.1.
                ''',
                'restart_interval',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'graceful-restart',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable auto cost.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('reference-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967')], [], 
                '''                Configure reference bandwidth in term of Mbits
                ''',
                'reference_bandwidth',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'auto-cost',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl',
            False, 
            [
            _MetaInfoClassMember('paths', ATTRIBUTE, 'int' , None, None, 
                [('1', '32')], [], 
                '''                Maximum number of ECMP paths.
                ''',
                'paths',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'spf-control',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl',
            False, 
            [
            _MetaInfoClassMember('max-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967294')], [], 
                '''                Maximum number of LSAs OSPF will receive.
                ''',
                'max_lsa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'database-control',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl',
            False, 
            [
            ],
            'ietf-ospf',
            'reload-control',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Take the interface's IPv4 address as TE
                router ID.
                ''',
                'interface',
                'ietf-ospf', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Explicitly configure the TE router ID.
                ''',
                'router_id',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'te-rid',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp',
            False, 
            [
            _MetaInfoClassMember('autoconfig', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable LDP IGP interface auto-configuration.
                ''',
                'autoconfig',
                'ietf-ospf', False),
            _MetaInfoClassMember('igp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable LDP IGP synchronization.
                ''',
                'igp_sync',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ldp',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls',
            False, 
            [
            _MetaInfoClassMember('ldp', REFERENCE_CLASS, 'Ldp' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp', 
                [], [], 
                '''                OSPF MPLS LDP config state.
                ''',
                'ldp',
                'ietf-ospf', False),
            _MetaInfoClassMember('te-rid', REFERENCE_CLASS, 'TeRid' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid', 
                [], [], 
                '''                Traffic Engineering stable IP address for system.
                ''',
                'te_rid',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'mpls',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa',
            False, 
            [
            ],
            'ietf-ospf',
            'lfa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute',
            False, 
            [
            _MetaInfoClassMember('lfa', REFERENCE_CLASS, 'Lfa' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa', 
                [], [], 
                '''                This container may be augmented with
                global parameters for LFA.
                Creating the container has no effect on
                LFA activation.
                ''',
                'lfa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'fast-reroute',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area',
            False, 
            [
            ],
            'ietf-ospf',
            'area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface',
            False, 
            [
            ],
            'ietf-ospf',
            'interface',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit',
            False, 
            [
            _MetaInfoClassMember('area', REFERENCE_CLASS, 'Area' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area', 
                [], [], 
                '''                Area config to be inherited by all areas.
                ''',
                'area',
                'ietf-ospf', False),
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface', 
                [], [], 
                '''                Interface config to be inherited by all interfaces
                in all areas.
                ''',
                'interface',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'all-areas-inherit',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 or IPv6 prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise or hide.
                ''',
                'advertise',
                'ietf-ospf', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                Cost of summary route.
                ''',
                'cost',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'range',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface',
            False, 
            [
            ],
            'ietf-ospf',
            'interface',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_CLASS, 'Interface' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface', 
                [], [], 
                '''                Interface config to be inherited by all
                interfaces.
                ''',
                'interface',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'all-interfaces-inherit',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable TTL security check.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('hops', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Maximum number of hops that a OSPF packet may
                have traveled.
                ''',
                'hops',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ttl-security',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm',
            False, 
            [
            _MetaInfoClassMember('hmac-sha1-12', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-12 algorithm.
                ''',
                'hmac_sha1_12',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha1-20', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-20 algorithm.
                ''',
                'hmac_sha1_20',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-1 authentication algorithm.
                ''',
                'hmac_sha_1',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-256', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-256 authentication algorithm.
                ''',
                'hmac_sha_256',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-384', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-384 authentication algorithm.
                ''',
                'hmac_sha_384',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-512', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-512 authentication algorithm.
                ''',
                'hmac_sha_512',
                'ietf-ospf', False),
            _MetaInfoClassMember('md5', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The MD5 algorithm.
                ''',
                'md5',
                'ietf-ospf', False),
            _MetaInfoClassMember('sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The SHA-1 algorithm.
                ''',
                'sha_1',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'crypto-algorithm',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('crypto-algorithm', REFERENCE_CLASS, 'CryptoAlgorithm' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm', 
                [], [], 
                '''                Cryptographic algorithm associated with key.
                ''',
                'crypto_algorithm',
                'ietf-ospf', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key string in ASCII format.
                ''',
                'key',
                'ietf-ospf', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                key-chain name
                ''',
                'key_chain',
                'ietf-ospf', False),
            _MetaInfoClassMember('sa', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SA name
                ''',
                'sa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'authentication',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink',
            False, 
            [
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Virtual link router ID.
                ''',
                'router_id',
                'ietf-ospf', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication', 
                [], [], 
                '''                Authentication configuration.
                ''',
                'authentication',
                'ietf-ospf', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable bfd.
                ''',
                'bfd',
                'ietf-ospf', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared dead.
                ''',
                'dead_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable protocol on the interface.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between hello packets.
                ''',
                'hello_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('lls', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable link-local signaling (LLS) support.
                ''',
                'lls',
                'ietf-ospf', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets.
                ''',
                'mtu_ignore',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress advertisement of the prefixes.
                ''',
                'prefix_suppression',
                'ietf-ospf', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between retransmitting unacknowledged Link State
                Advertisements (LSAs).
                ''',
                'retransmit_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Estimated time needed to send link-state update.
                ''',
                'transmit_delay',
                'ietf-ospf', False),
            _MetaInfoClassMember('ttl-security', REFERENCE_CLASS, 'TtlSecurity' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity', 
                [], [], 
                '''                TTL security check.
                ''',
                'ttl_security',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'virtual-link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable TTL security check.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('hops', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Maximum number of hops that a OSPF packet may
                have traveled.
                ''',
                'hops',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ttl-security',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm',
            False, 
            [
            _MetaInfoClassMember('hmac-sha1-12', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-12 algorithm.
                ''',
                'hmac_sha1_12',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha1-20', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-20 algorithm.
                ''',
                'hmac_sha1_20',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-1 authentication algorithm.
                ''',
                'hmac_sha_1',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-256', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-256 authentication algorithm.
                ''',
                'hmac_sha_256',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-384', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-384 authentication algorithm.
                ''',
                'hmac_sha_384',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-512', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-512 authentication algorithm.
                ''',
                'hmac_sha_512',
                'ietf-ospf', False),
            _MetaInfoClassMember('md5', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The MD5 algorithm.
                ''',
                'md5',
                'ietf-ospf', False),
            _MetaInfoClassMember('sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The SHA-1 algorithm.
                ''',
                'sha_1',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'crypto-algorithm',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('crypto-algorithm', REFERENCE_CLASS, 'CryptoAlgorithm' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm', 
                [], [], 
                '''                Cryptographic algorithm associated with key.
                ''',
                'crypto_algorithm',
                'ietf-ospf', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key string in ASCII format.
                ''',
                'key',
                'ietf-ospf', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                key-chain name
                ''',
                'key_chain',
                'ietf-ospf', False),
            _MetaInfoClassMember('sa', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SA name
                ''',
                'sa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'authentication',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink',
            False, 
            [
            _MetaInfoClassMember('local-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the local end-point.
                ''',
                'local_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('local-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the local end-point.
                        ''',
                        'local_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('local-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the local end-point.
                        ''',
                        'local_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('remote-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address of the remote end-point.
                ''',
                'remote_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the remote end-point.
                        ''',
                        'remote_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('remote-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address of the remote end-point.
                        ''',
                        'remote_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication', 
                [], [], 
                '''                Authentication configuration.
                ''',
                'authentication',
                'ietf-ospf', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable bfd.
                ''',
                'bfd',
                'ietf-ospf', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared dead.
                ''',
                'dead_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable protocol on the interface.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between hello packets.
                ''',
                'hello_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('lls', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable link-local signaling (LLS) support.
                ''',
                'lls',
                'ietf-ospf', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets.
                ''',
                'mtu_ignore',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress advertisement of the prefixes.
                ''',
                'prefix_suppression',
                'ietf-ospf', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between retransmitting unacknowledged Link State
                Advertisements (LSAs).
                ''',
                'retransmit_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Estimated time needed to send link-state update.
                ''',
                'transmit_delay',
                'ietf-ospf', False),
            _MetaInfoClassMember('ttl-security', REFERENCE_CLASS, 'TtlSecurity' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity', 
                [], [], 
                '''                TTL security check.
                ''',
                'ttl_security',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'sham-link',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea',
            False, 
            [
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Interface cost for multi-area.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('multi-area-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Multi-area ID
                ''',
                'multi_area_id',
                'ietf-ospf', False, [
                    _MetaInfoClassMember('multi-area-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Multi-area ID
                        ''',
                        'multi_area_id',
                        'ietf-ospf', False),
                    _MetaInfoClassMember('multi-area-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Multi-area ID
                        ''',
                        'multi_area_id',
                        'ietf-ospf', False),
                ]),
            ],
            'ietf-ospf',
            'multi-area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Neighbor IP address.
                ''',
                'address',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP address.
                        ''',
                        'address',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Neighbor IP address.
                        ''',
                        'address',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Neighbor cost.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Neighbor poll interval.
                ''',
                'poll_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Neighbor priority for DR election.
                ''',
                'priority',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'neighbor',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor', 
                [], [], 
                '''                Specify a neighbor router.
                ''',
                'neighbor',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'static-neighbors',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Activates remote LFA.
                ''',
                'enabled',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'remote-lfa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa',
            False, 
            [
            _MetaInfoClassMember('candidate-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Prevent the interface to be used as backup.
                ''',
                'candidate_disabled',
                'ietf-ospf', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Activates LFA.
                This model assumes activation of per-prefix LFA.
                ''',
                'enabled',
                'ietf-ospf', False),
            _MetaInfoClassMember('remote-lfa', REFERENCE_CLASS, 'RemoteLfa' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa', 
                [], [], 
                '''                Remote LFA configuration.
                ''',
                'remote_lfa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'lfa',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute',
            False, 
            [
            _MetaInfoClassMember('lfa', REFERENCE_CLASS, 'Lfa' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa', 
                [], [], 
                '''                LFA configuration.
                ''',
                'lfa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'fast-reroute',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable TTL security check.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('hops', ATTRIBUTE, 'int' , None, None, 
                [('1', '254')], [], 
                '''                Maximum number of hops that a OSPF packet may
                have traveled.
                ''',
                'hops',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ttl-security',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm',
            False, 
            [
            _MetaInfoClassMember('hmac-sha1-12', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-12 algorithm.
                ''',
                'hmac_sha1_12',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha1-20', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The HMAC-SHA1-20 algorithm.
                ''',
                'hmac_sha1_20',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-1 authentication algorithm.
                ''',
                'hmac_sha_1',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-256', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-256 authentication algorithm.
                ''',
                'hmac_sha_256',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-384', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-384 authentication algorithm.
                ''',
                'hmac_sha_384',
                'ietf-ospf', False),
            _MetaInfoClassMember('hmac-sha-512', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                HMAC-SHA-512 authentication algorithm.
                ''',
                'hmac_sha_512',
                'ietf-ospf', False),
            _MetaInfoClassMember('md5', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The MD5 algorithm.
                ''',
                'md5',
                'ietf-ospf', False),
            _MetaInfoClassMember('sha-1', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The SHA-1 algorithm.
                ''',
                'sha_1',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'crypto-algorithm',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('crypto-algorithm', REFERENCE_CLASS, 'CryptoAlgorithm' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm', 
                [], [], 
                '''                Cryptographic algorithm associated with key.
                ''',
                'crypto_algorithm',
                'ietf-ospf', False),
            _MetaInfoClassMember('key', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Key string in ASCII format.
                ''',
                'key',
                'ietf-ospf', False),
            _MetaInfoClassMember('key-chain', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                key-chain name
                ''',
                'key_chain',
                'ietf-ospf', False),
            _MetaInfoClassMember('sa', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SA name
                ''',
                'sa',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'authentication',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                One of the topology enabled on this interface
                ''',
                'name',
                'ietf-ospf', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface cost for this topology
                ''',
                'cost',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.NetworkTypeEnum' : _MetaInfoEnum('NetworkTypeEnum', 'ydk.models.ietf.ietf_routing',
        {
            'broadcast':'broadcast',
            'non-broadcast':'non_broadcast',
            'point-to-multipoint':'point_to_multipoint',
            'point-to-point':'point_to_point',
        }, 'ietf-ospf', _yang_ns._namespaces['ietf-ospf']),
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface.
                ''',
                'interface',
                'ietf-ospf', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication', 
                [], [], 
                '''                Authentication configuration.
                ''',
                'authentication',
                'ietf-ospf', False),
            _MetaInfoClassMember('bfd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable bfd.
                ''',
                'bfd',
                'ietf-ospf', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost.
                ''',
                'cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared dead.
                ''',
                'dead_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable demand circuit.
                ''',
                'demand_circuit',
                'ietf-ospf', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable protocol on the interface.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration.
                ''',
                'fast_reroute',
                'ietf-ospf', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between hello packets.
                ''',
                'hello_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('lls', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable link-local signaling (LLS) support.
                ''',
                'lls',
                'ietf-ospf', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable ignoring of MTU in DBD packets.
                ''',
                'mtu_ignore',
                'ietf-ospf', False),
            _MetaInfoClassMember('multi-area', REFERENCE_CLASS, 'MultiArea' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea', 
                [], [], 
                '''                Configure ospf multi-area.
                ''',
                'multi_area',
                'ietf-ospf', False),
            _MetaInfoClassMember('network-type', REFERENCE_ENUM_CLASS, 'NetworkTypeEnum' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.NetworkTypeEnum', 
                [], [], 
                '''                Network type.
                ''',
                'network_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('node-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set prefix as a node representative prefix.
                ''',
                'node_flag',
                'ietf-ospf', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable passive.
                ''',
                'passive',
                'ietf-ospf', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress advertisement of the prefixes.
                ''',
                'prefix_suppression',
                'ietf-ospf', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between retransmitting unacknowledged Link State
                Advertisements (LSAs).
                ''',
                'retransmit_interval',
                'ietf-ospf', False),
            _MetaInfoClassMember('static-neighbors', REFERENCE_CLASS, 'StaticNeighbors' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors', 
                [], [], 
                '''                Static configured neighbors.
                ''',
                'static_neighbors',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology', 
                [], [], 
                '''                OSPF interface topology.
                ''',
                'topology',
                'ietf-ospf', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Estimated time needed to send link-state update.
                ''',
                'transmit_delay',
                'ietf-ospf', False),
            _MetaInfoClassMember('ttl-security', REFERENCE_CLASS, 'TtlSecurity' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity', 
                [], [], 
                '''                TTL security check.
                ''',
                'ttl_security',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'interface',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area',
            False, 
            [
            _MetaInfoClassMember('area-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Area ID.
                ''',
                'area_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('all-interfaces-inherit', REFERENCE_CLASS, 'AllInterfacesInherit' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit', 
                [], [], 
                '''                Inheritance for all interfaces
                ''',
                'all_interfaces_inherit',
                'ietf-ospf', False),
            _MetaInfoClassMember('area-type', REFERENCE_IDENTITY_CLASS, 'AreaTypeIdentity' , 'ydk.models.ietf.ietf_ospf', 'AreaTypeIdentity', 
                [], [], 
                '''                Area type.
                ''',
                'area_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Set the summary default-cost for a stub or NSSA area.
                ''',
                'default_cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface', 
                [], [], 
                '''                List of OSPF interfaces.
                ''',
                'interface',
                'ietf-ospf', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range', 
                [], [], 
                '''                Summarize routes matching address/mask (border
                routers only)
                ''',
                'range',
                'ietf-ospf', False),
            _MetaInfoClassMember('sham-link', REFERENCE_LIST, 'ShamLink' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink', 
                [], [], 
                '''                OSPF sham link
                ''',
                'sham_link',
                'ietf-ospf', False),
            _MetaInfoClassMember('summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable summary generation to the stub or
                NSSA area.
                ''',
                'summary',
                'ietf-ospf', False),
            _MetaInfoClassMember('virtual-link', REFERENCE_LIST, 'VirtualLink' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink', 
                [], [], 
                '''                OSPF virtual link
                ''',
                'virtual_link',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 or IPv6 prefix
                ''',
                'prefix',
                'ietf-ospf', True),
            _MetaInfoClassMember('advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Advertise or hide.
                ''',
                'advertise',
                'ietf-ospf', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                Cost of summary route.
                ''',
                'cost',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'range',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area',
            False, 
            [
            _MetaInfoClassMember('area-id', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Area ID.
                ''',
                'area_id',
                'ietf-ospf', True, [
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                        [('0', '4294967295')], [], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                    _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                        '''                        Area ID.
                        ''',
                        'area_id',
                        'ietf-ospf', True),
                ]),
            _MetaInfoClassMember('area-type', REFERENCE_IDENTITY_CLASS, 'AreaTypeIdentity' , 'ydk.models.ietf.ietf_ospf', 'AreaTypeIdentity', 
                [], [], 
                '''                Area type.
                ''',
                'area_type',
                'ietf-ospf', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777215')], [], 
                '''                Set the summary default-cost for a stub or NSSA area.
                ''',
                'default_cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range', 
                [], [], 
                '''                Summarize routes matching address/mask (border
                routers only)
                ''',
                'range',
                'ietf-ospf', False),
            _MetaInfoClassMember('summary', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable summary generation to the stub or
                NSSA area.
                ''',
                'summary',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'area',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                RIB
                ''',
                'name',
                'ietf-ospf', True),
            _MetaInfoClassMember('area', REFERENCE_LIST, 'Area' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area', 
                [], [], 
                '''                List of ospf areas
                ''',
                'area',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'topology',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance',
            False, 
            [
            _MetaInfoClassMember('af', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_routing', 'AddressFamilyIdentity', 
                [], [], 
                '''                Address-family of the instance.
                ''',
                'af',
                'ietf-ospf', True),
            _MetaInfoClassMember('admin-distance', REFERENCE_CLASS, 'AdminDistance' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance', 
                [], [], 
                '''                Admin distance config state.
                ''',
                'admin_distance',
                'ietf-ospf', False),
            _MetaInfoClassMember('all-areas-inherit', REFERENCE_CLASS, 'AllAreasInherit' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit', 
                [], [], 
                '''                Inheritance for all areas.
                ''',
                'all_areas_inherit',
                'ietf-ospf', False),
            _MetaInfoClassMember('area', REFERENCE_LIST, 'Area' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area', 
                [], [], 
                '''                List of ospf areas
                ''',
                'area',
                'ietf-ospf', False),
            _MetaInfoClassMember('auto-cost', REFERENCE_CLASS, 'AutoCost' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost', 
                [], [], 
                '''                Auto cost config state.
                ''',
                'auto_cost',
                'ietf-ospf', False),
            _MetaInfoClassMember('database-control', REFERENCE_CLASS, 'DatabaseControl' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl', 
                [], [], 
                '''                Database maintenance control.
                ''',
                'database_control',
                'ietf-ospf', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable the protocol.
                ''',
                'enable',
                'ietf-ospf', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute', 
                [], [], 
                '''                This container may be augmented with global
                parameters for IPFRR.
                ''',
                'fast_reroute',
                'ietf-ospf', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart', 
                [], [], 
                '''                Graceful restart config state.
                ''',
                'graceful_restart',
                'ietf-ospf', False),
            _MetaInfoClassMember('mpls', REFERENCE_CLASS, 'Mpls' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls', 
                [], [], 
                '''                OSPF MPLS config state.
                ''',
                'mpls',
                'ietf-ospf', False),
            _MetaInfoClassMember('nsr', REFERENCE_CLASS, 'Nsr' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr', 
                [], [], 
                '''                NSR config state.
                ''',
                'nsr',
                'ietf-ospf', False),
            _MetaInfoClassMember('reload-control', REFERENCE_CLASS, 'ReloadControl' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl', 
                [], [], 
                '''                Protocol reload control.
                ''',
                'reload_control',
                'ietf-ospf', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                Defined in RFC 2328. A 32-bit number
                that uniquely identifies the router.
                ''',
                'router_id',
                'ietf-ospf', False),
            _MetaInfoClassMember('spf-control', REFERENCE_CLASS, 'SpfControl' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl', 
                [], [], 
                '''                SPF calculation control.
                ''',
                'spf_control',
                'ietf-ospf', False),
            _MetaInfoClassMember('topology', REFERENCE_LIST, 'Topology' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology', 
                [], [], 
                '''                OSPF topology.
                ''',
                'topology',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'instance',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf',
            False, 
            [
            _MetaInfoClassMember('all-instances-inherit', REFERENCE_CLASS, 'AllInstancesInherit' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit', 
                [], [], 
                '''                Inheritance support to all instances.
                ''',
                'all_instances_inherit',
                'ietf-ospf', False),
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance', 
                [], [], 
                '''                An OSPF routing protocol instance.
                ''',
                'instance',
                'ietf-ospf', False),
            _MetaInfoClassMember('operation-mode', REFERENCE_IDENTITY_CLASS, 'OperationModeIdentity' , 'ydk.models.ietf.ietf_ospf', 'OperationModeIdentity', 
                [], [], 
                '''                OSPF operation mode.
                ''',
                'operation_mode',
                'ietf-ospf', False),
            ],
            'ietf-ospf',
            'ospf',
            _yang_ns._namespaces['ietf-ospf'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols.RoutingProtocol',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'RoutingProtocolIdentity' , 'ydk.models.ietf.ietf_routing', 'RoutingProtocolIdentity', 
                [], [], 
                '''                Type of the routing protocol - an identity derived
                from the 'routing-protocol' base identity.
                ''',
                'type',
                'ietf-routing', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An arbitrary name of the routing protocol instance.
                ''',
                'name',
                'ietf-routing', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Textual description of the routing protocol
                instance.
                ''',
                'description',
                'ietf-routing', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf', 
                [], [], 
                '''                OSPF.
                ''',
                'ospf',
                'ietf-ospf', False),
            _MetaInfoClassMember('static-routes', REFERENCE_CLASS, 'StaticRoutes' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes', 
                [], [], 
                '''                Configuration of the 'static' pseudo-protocol.
                
                Address-family-specific modules augment this node with
                their lists of routes.
                ''',
                'static_routes',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'routing-protocol',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.RoutingProtocols' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.RoutingProtocols',
            False, 
            [
            _MetaInfoClassMember('routing-protocol', REFERENCE_LIST, 'RoutingProtocol' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols.RoutingProtocol', 
                [], [], 
                '''                Each entry contains configuration of a routing protocol
                instance.
                ''',
                'routing_protocol',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'routing-protocols',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.Ribs.Rib' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.Ribs.Rib',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the RIB.
                
                For system-controlled entries, the value of this leaf
                must be the same as the name of the corresponding
                entry in state data.
                
                For user-controlled entries, an arbitrary name can be
                used.
                ''',
                'name',
                'ietf-routing', True),
            _MetaInfoClassMember('address-family', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_routing', 'AddressFamilyIdentity', 
                [], [], 
                '''                Address family.
                ''',
                'address_family',
                'ietf-routing', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Textual description of the RIB.
                ''',
                'description',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'rib',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance.Ribs' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance.Ribs',
            False, 
            [
            _MetaInfoClassMember('rib', REFERENCE_LIST, 'Rib' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.Ribs.Rib', 
                [], [], 
                '''                Each entry contains configuration for a RIB identified
                by the 'name' key.
                
                Entries having the same key as a system-controlled entry
                of the list /routing-state/routing-instance/ribs/rib are
                used for configuring parameters of that entry. Other
                entries define additional user-controlled RIBs.
                ''',
                'rib',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'ribs',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing.RoutingInstance' : {
        'meta_info' : _MetaInfoClass('Routing.RoutingInstance',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the routing instance.
                
                For system-controlled entries, the value of this leaf must
                be the same as the name of the corresponding entry in
                state data.
                
                For user-controlled entries, an arbitrary name can be
                used.
                ''',
                'name',
                'ietf-routing', True),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Textual description of the routing instance.
                ''',
                'description',
                'ietf-routing', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable the routing instance.
                
                If this parameter is false, the parent routing instance is
                disabled and does not appear in state data, despite any
                other configuration that might be present.
                ''',
                'enabled',
                'ietf-routing', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.Interfaces', 
                [], [], 
                '''                Assignment of the routing instance's interfaces.
                ''',
                'interfaces',
                'ietf-routing', False),
            _MetaInfoClassMember('ribs', REFERENCE_CLASS, 'Ribs' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.Ribs', 
                [], [], 
                '''                Configuration of RIBs.
                ''',
                'ribs',
                'ietf-routing', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])'], 
                '''                A 32-bit number in the form of a dotted quad that is used by
                some routing protocols identifying a router.
                ''',
                'router_id',
                'ietf-routing', False),
            _MetaInfoClassMember('routing-protocols', REFERENCE_CLASS, 'RoutingProtocols' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance.RoutingProtocols', 
                [], [], 
                '''                Configuration of routing protocol instances.
                ''',
                'routing_protocols',
                'ietf-routing', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'RoutingInstanceIdentity' , 'ydk.models.ietf.ietf_routing', 'RoutingInstanceIdentity', 
                [], [], 
                '''                The type of the routing instance.
                ''',
                'type',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'routing-instance',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Routing' : {
        'meta_info' : _MetaInfoClass('Routing',
            False, 
            [
            _MetaInfoClassMember('routing-instance', REFERENCE_LIST, 'RoutingInstance' , 'ydk.models.ietf.ietf_routing', 'Routing.RoutingInstance', 
                [], [], 
                '''                Configuration of a routing instance.
                ''',
                'routing_instance',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'routing',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'FibRouteRpc.Input.DestinationAddress' : {
        'meta_info' : _MetaInfoClass('FibRouteRpc.Input.DestinationAddress',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_routing', 'AddressFamilyIdentity', 
                [], [], 
                '''                Address family.
                ''',
                'address_family',
                'ietf-routing', False),
            _MetaInfoClassMember('ietf-ipv4-unicast-routing_address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 destination address.
                ''',
                'ietf_ipv4_unicast_routing_address',
                'ietf-ipv4-unicast-routing', False),
            _MetaInfoClassMember('ietf-ipv6-unicast-routing_address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 destination address.
                ''',
                'ietf_ipv6_unicast_routing_address',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-routing',
            'destination-address',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'FibRouteRpc.Input' : {
        'meta_info' : _MetaInfoClass('FibRouteRpc.Input',
            False, 
            [
            _MetaInfoClassMember('routing-instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the routing instance whose forwarding information
                base is being queried.
                
                If the routing instance with name equal to the value of
                this parameter doesn't exist, then this operation SHALL
                fail with error-tag 'data-missing' and error-app-tag
                'routing-instance-not-found'.
                ''',
                'routing_instance_name',
                'ietf-routing', False),
            _MetaInfoClassMember('destination-address', REFERENCE_CLASS, 'DestinationAddress' , 'ydk.models.ietf.ietf_routing', 'FibRouteRpc.Input.DestinationAddress', 
                [], [], 
                '''                Network layer destination address.
                
                Address family specific modules MUST augment this
                container with a leaf named 'address'.
                ''',
                'destination_address',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'input',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'FibRouteRpc.Output.Route.NextHop.SpecialNextHopEnum' : _MetaInfoEnum('SpecialNextHopEnum', 'ydk.models.ietf.ietf_routing',
        {
            'blackhole':'blackhole',
            'unreachable':'unreachable',
            'prohibit':'prohibit',
            'receive':'receive',
        }, 'ietf-routing', _yang_ns._namespaces['ietf-routing']),
    'FibRouteRpc.Output.Route.NextHop' : {
        'meta_info' : _MetaInfoClass('FibRouteRpc.Output.Route.NextHop',
            False, 
            [
            _MetaInfoClassMember('outgoing-interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the outgoing interface.
                ''',
                'outgoing_interface',
                'ietf-routing', False),
            _MetaInfoClassMember('ietf-routing_next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address.
                ''',
                'ietf_routing_next_hop_address',
                'ietf-routing', False),
            _MetaInfoClassMember('ietf-ipv4-unicast-routing_next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the next-hop.
                ''',
                'ietf_ipv4_unicast_routing_next_hop_address',
                'ietf-ipv4-unicast-routing', False),
            _MetaInfoClassMember('ietf-ipv6-unicast-routing_next-hop-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address of the next-hop.
                ''',
                'ietf_ipv6_unicast_routing_next_hop_address',
                'ietf-ipv6-unicast-routing', False),
            _MetaInfoClassMember('special-next-hop', REFERENCE_ENUM_CLASS, 'SpecialNextHopEnum' , 'ydk.models.ietf.ietf_routing', 'FibRouteRpc.Output.Route.NextHop.SpecialNextHopEnum', 
                [], [], 
                '''                Special next-hop options.
                ''',
                'special_next_hop',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'next-hop',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'FibRouteRpc.Output.Route' : {
        'meta_info' : _MetaInfoClass('FibRouteRpc.Output.Route',
            False, 
            [
            _MetaInfoClassMember('address-family', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_routing', 'AddressFamilyIdentity', 
                [], [], 
                '''                Address family.
                ''',
                'address_family',
                'ietf-routing', False),
            _MetaInfoClassMember('next-hop', REFERENCE_CLASS, 'NextHop' , 'ydk.models.ietf.ietf_routing', 'FibRouteRpc.Output.Route.NextHop', 
                [], [], 
                '''                Route's next-hop attribute.
                ''',
                'next_hop',
                'ietf-routing', False),
            _MetaInfoClassMember('source-protocol', REFERENCE_IDENTITY_CLASS, 'RoutingProtocolIdentity' , 'ydk.models.ietf.ietf_routing', 'RoutingProtocolIdentity', 
                [], [], 
                '''                Type of the routing protocol from which the route
                originated.
                ''',
                'source_protocol',
                'ietf-routing', False),
            _MetaInfoClassMember('active', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Presence of this leaf indicates that the route is preferred
                among all routes in the same RIB that have the same
                destination prefix.
                ''',
                'active',
                'ietf-routing', False),
            _MetaInfoClassMember('last-updated', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Time stamp of the last modification of the route. If the
                route was never modified, it is the time when the route was
                inserted into the RIB.
                ''',
                'last_updated',
                'ietf-routing', False),
            _MetaInfoClassMember('ietf-ipv4-unicast-routing_destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                IPv4 destination prefix.
                ''',
                'ietf_ipv4_unicast_routing_destination_prefix',
                'ietf-ipv4-unicast-routing', False),
            _MetaInfoClassMember('ietf-ipv6-unicast-routing_destination-prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                IPv6 destination prefix.
                ''',
                'ietf_ipv6_unicast_routing_destination_prefix',
                'ietf-ipv6-unicast-routing', False),
            ],
            'ietf-routing',
            'route',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'FibRouteRpc.Output' : {
        'meta_info' : _MetaInfoClass('FibRouteRpc.Output',
            False, 
            [
            _MetaInfoClassMember('route', REFERENCE_CLASS, 'Route' , 'ydk.models.ietf.ietf_routing', 'FibRouteRpc.Output.Route', 
                [], [], 
                '''                The active FIB route for the specified destination.
                
                If the routing instance has no active FIB route for the
                destination address, no output is returned - the server
                SHALL send an <rpc-reply> containing a single element
                <ok>.
                
                Address family specific modules MUST augment this list
                with appropriate route contents.
                ''',
                'route',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'output',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'FibRouteRpc' : {
        'meta_info' : _MetaInfoClass('FibRouteRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_routing', 'FibRouteRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-routing', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_routing', 'FibRouteRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-routing', False),
            ],
            'ietf-routing',
            'fib-route',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'DefaultRoutingInstanceIdentity' : {
        'meta_info' : _MetaInfoClass('DefaultRoutingInstanceIdentity',
            False, 
            [
            ],
            'ietf-routing',
            'default-routing-instance',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'StaticIdentity' : {
        'meta_info' : _MetaInfoClass('StaticIdentity',
            False, 
            [
            ],
            'ietf-routing',
            'static',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'VrfRoutingInstanceIdentity' : {
        'meta_info' : _MetaInfoClass('VrfRoutingInstanceIdentity',
            False, 
            [
            ],
            'ietf-routing',
            'vrf-routing-instance',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Ipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6Identity',
            False, 
            [
            ],
            'ietf-routing',
            'ipv6',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'DirectIdentity' : {
        'meta_info' : _MetaInfoClass('DirectIdentity',
            False, 
            [
            ],
            'ietf-routing',
            'direct',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
    'Ipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4Identity',
            False, 
            [
            ],
            'ietf-routing',
            'ipv4',
            _yang_ns._namespaces['ietf-routing'],
        'ydk.models.ietf.ietf_routing'
        ),
    },
}
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors.Neighbor']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa.RemoteLfa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute.Lfa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication.CryptoAlgorithm']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.UnknownTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Router']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Network']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Summary']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.External']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body.Opaque']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Header']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2.Body']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link.PrefixList']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Router']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Network']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaPrefix']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.InterAreaRouter']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.AsExternal']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Nssa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Header']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3.Body']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv2']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa.Ospfv3']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas.LinkScopeLsa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.MultiArea']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.StaticNeighbors']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.FastReroute']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.TtlSecurity']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Authentication']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Neighbor']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.LinkScopeLsas']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.UnknownTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Router']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Network']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Summary']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.External']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body.Opaque']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Header']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2.Body']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link.PrefixList']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Router']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Network']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaPrefix']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.InterAreaRouter']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.AsExternal']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Nssa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Header']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3.Body']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv2']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa.Ospfv3']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas.AreaScopeLsa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interfaces']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AreaScopeLsas']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv.UnknownSubtlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.UnknownTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.RouterAddressTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque.LinkTlv']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Router']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Network']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Summary']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.External']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body.Opaque']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Header']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2.Body']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link.PrefixList']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix.PrefixList']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Router']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Network']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaPrefix']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.InterAreaRouter']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.AsExternal']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Nssa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.Link']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body.IntraAreaPrefix']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Header']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3.Body']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv2']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa.Ospfv3']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas.AsScopeLsa']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AsScopeLsas']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols.RoutingProtocol']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.RoutingProtocols']['meta_info']
_meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes.Route.NextHop']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes.Route']['meta_info']
_meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes.Route']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes']['meta_info']
_meta_table['RoutingState.RoutingInstance.Ribs.Rib.Routes']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.Ribs.Rib']['meta_info']
_meta_table['RoutingState.RoutingInstance.Ribs.Rib']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance.Ribs']['meta_info']
_meta_table['RoutingState.RoutingInstance.Interfaces']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance']['meta_info']
_meta_table['RoutingState.RoutingInstance.RoutingProtocols']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance']['meta_info']
_meta_table['RoutingState.RoutingInstance.Ribs']['meta_info'].parent =_meta_table['RoutingState.RoutingInstance']['meta_info']
_meta_table['RoutingState.RoutingInstance']['meta_info'].parent =_meta_table['RoutingState']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route.NextHop']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4.Route']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route.NextHop']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6.Route']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv4']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes.Ipv6']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Area']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit.Interface']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.TeRid']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls.Ldp']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute.Lfa']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Area']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit.Interface']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit.Interface']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication.CryptoAlgorithm']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.TtlSecurity']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink.Authentication']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication.CryptoAlgorithm']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.TtlSecurity']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink.Authentication']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors.Neighbor']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa.RemoteLfa']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute.Lfa']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication.CryptoAlgorithm']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.MultiArea']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.StaticNeighbors']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.FastReroute']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.TtlSecurity']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Authentication']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface.Topology']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Range']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.AllInterfacesInherit']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.VirtualLink']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.ShamLink']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area.Interface']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area.Range']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology.Area']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AdminDistance']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Nsr']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.GracefulRestart']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AutoCost']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.SpfControl']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.DatabaseControl']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.ReloadControl']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Mpls']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.FastReroute']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.AllAreasInherit']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Area']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance.Topology']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.AllInstancesInherit']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf.Instance']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.StaticRoutes']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol.Ospf']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols.RoutingProtocol']['meta_info'].parent =_meta_table['Routing.RoutingInstance.RoutingProtocols']['meta_info']
_meta_table['Routing.RoutingInstance.Ribs.Rib']['meta_info'].parent =_meta_table['Routing.RoutingInstance.Ribs']['meta_info']
_meta_table['Routing.RoutingInstance.Interfaces']['meta_info'].parent =_meta_table['Routing.RoutingInstance']['meta_info']
_meta_table['Routing.RoutingInstance.RoutingProtocols']['meta_info'].parent =_meta_table['Routing.RoutingInstance']['meta_info']
_meta_table['Routing.RoutingInstance.Ribs']['meta_info'].parent =_meta_table['Routing.RoutingInstance']['meta_info']
_meta_table['Routing.RoutingInstance']['meta_info'].parent =_meta_table['Routing']['meta_info']
_meta_table['FibRouteRpc.Input.DestinationAddress']['meta_info'].parent =_meta_table['FibRouteRpc.Input']['meta_info']
_meta_table['FibRouteRpc.Output.Route.NextHop']['meta_info'].parent =_meta_table['FibRouteRpc.Output.Route']['meta_info']
_meta_table['FibRouteRpc.Output.Route']['meta_info'].parent =_meta_table['FibRouteRpc.Output']['meta_info']
_meta_table['FibRouteRpc.Input']['meta_info'].parent =_meta_table['FibRouteRpc']['meta_info']
_meta_table['FibRouteRpc.Output']['meta_info'].parent =_meta_table['FibRouteRpc']['meta_info']
