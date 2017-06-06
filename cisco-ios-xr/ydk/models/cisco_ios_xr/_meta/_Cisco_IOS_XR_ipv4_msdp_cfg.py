


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'MsdpFilterTypeVrfEnum' : _MetaInfoEnum('MsdpFilterTypeVrfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg',
        {
            'incoming':'incoming',
            'outgoing':'outgoing',
        }, 'Cisco-IOS-XR-ipv4-msdp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg']),
    'MsdpListTypeVrfEnum' : _MetaInfoEnum('MsdpListTypeVrfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg',
        {
            'list':'list',
            'rp-list':'rp_list',
        }, 'Cisco-IOS-XR-ipv4-msdp-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg']),
    'Msdp.Vrfs.Vrf.CacheState' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.CacheState',
            False, 
            [
            _MetaInfoClassMember('list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list name
                ''',
                'list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('rp-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list for originating RP
                ''',
                'rp_list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('sa-holdtime', ATTRIBUTE, 'int' , None, None, 
                [('150', '3600')], [], 
                '''                SA State Holdtime period
                ''',
                'sa_holdtime',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'cache-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.KeepAlive' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.KeepAlive',
            False, 
            [
            _MetaInfoClassMember('keep-alive-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Keep alive period in seconds
                ''',
                'keep_alive_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peer-timeout-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '75')], [], 
                '''                Peer timeout period in seconds
                ''',
                'peer_timeout_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'keep-alive',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First half of ASN in asdot format or 0 in
                asplain
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Second half of ASN in asdot format or
                complete ASN in asplain
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive',
            False, 
            [
            _MetaInfoClassMember('keep-alive-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Keep alive period in seconds
                ''',
                'keep_alive_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peer-timeout-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '75')], [], 
                '''                Peer timeout period in seconds
                ''',
                'peer_timeout_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'keep-alive',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter',
            False, 
            [
            _MetaInfoClassMember('list', REFERENCE_ENUM_CLASS, 'MsdpListTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpListTypeVrfEnum', 
                [], [], 
                '''                Src List/RP List
                ''',
                'list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('filter-type', REFERENCE_ENUM_CLASS, 'MsdpFilterTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpFilterTypeVrfEnum', 
                [], [], 
                '''                Incoming/Outgoing ACL
                ''',
                'filter_type',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.Peers.Peer.SaFilters' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.Peers.Peer.SaFilters',
            False, 
            [
            _MetaInfoClassMember('sa-filter', REFERENCE_LIST, 'SaFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter', 
                [], [], 
                '''                SA-Filter incoming/outgoing list or RPlist
                ''',
                'sa_filter',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer address
                ''',
                'peer_address',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('connect-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure interface name used for MSDP
                connection
                ''',
                'connect_source',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 80)], [], 
                '''                Up to 80 characters describing this peer
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabling Peer Configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('keep-alive', REFERENCE_CLASS, 'KeepAlive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive', 
                [], [], 
                '''                MSDP keep alive period
                ''',
                'keep_alive',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('max-sa', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Maximum SA accepted from this peer
                ''',
                'max_sa',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('mesh-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Configure an MSDP mesh-group
                ''',
                'mesh_group',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('nsr-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable NSR for the peer
                ''',
                'nsr_down',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peer-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Configuration of password of peer
                ''',
                'peer_password',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs', 
                [], [], 
                '''                Configure the remote AS of this peer
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('sa-filters', REFERENCE_CLASS, 'SaFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.Peers.Peer.SaFilters', 
                [], [], 
                '''                Filter SA messages from peer
                ''',
                'sa_filters',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MSDP Peer Shutdown
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Configure TTL Threshold for MSDP Peer
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.Peers' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.Peers.Peer', 
                [], [], 
                '''                Peer address
                ''',
                'peer',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.SaFilters.SaFilter' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.SaFilters.SaFilter',
            False, 
            [
            _MetaInfoClassMember('list', REFERENCE_ENUM_CLASS, 'MsdpListTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpListTypeVrfEnum', 
                [], [], 
                '''                Src List/RP List
                ''',
                'list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('filter-type', REFERENCE_ENUM_CLASS, 'MsdpFilterTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpFilterTypeVrfEnum', 
                [], [], 
                '''                Incoming/Outgoing ACL
                ''',
                'filter_type',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf.SaFilters' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf.SaFilters',
            False, 
            [
            _MetaInfoClassMember('sa-filter', REFERENCE_LIST, 'SaFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.SaFilters.SaFilter', 
                [], [], 
                '''                SA-Filter incoming/outgoing list or RPlist
                ''',
                'sa_filter',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('cache-state', REFERENCE_CLASS, 'CacheState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.CacheState', 
                [], [], 
                '''                Configure this systems SA cache access-lists
                ''',
                'cache_state',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('connect-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure interface name used for MSDP
                connection
                ''',
                'connect_source',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('default-peer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure default peers for the box
                ''',
                'default_peer',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('keep-alive', REFERENCE_CLASS, 'KeepAlive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.KeepAlive', 
                [], [], 
                '''                MSDP keep alive period
                ''',
                'keep_alive',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('max-peer-sa', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure inheritable MAX SA state for peers
                ''',
                'max_peer_sa',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('max-sa', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure context's MAX SA state for the router
                ''',
                'max_sa',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure interface name used as originator ID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.Peers', 
                [], [], 
                '''                Entering Peer Configuration
                ''',
                'peers',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('sa-filters', REFERENCE_CLASS, 'SaFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf.SaFilters', 
                [], [], 
                '''                Filter SA messages from peer
                ''',
                'sa_filters',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Configure TTL Threshold for MSDP Peer
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.Vrfs' : {
        'meta_info' : _MetaInfoClass('Msdp.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs.Vrf', 
                [], [], 
                '''                VRF Name
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.CacheState' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.CacheState',
            False, 
            [
            _MetaInfoClassMember('list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list name
                ''',
                'list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('rp-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access-list for originating RP
                ''',
                'rp_list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('sa-holdtime', ATTRIBUTE, 'int' , None, None, 
                [('150', '3600')], [], 
                '''                SA State Holdtime period
                ''',
                'sa_holdtime',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'cache-state',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.KeepAlive' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.KeepAlive',
            False, 
            [
            _MetaInfoClassMember('keep-alive-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Keep alive period in seconds
                ''',
                'keep_alive_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peer-timeout-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '75')], [], 
                '''                Peer timeout period in seconds
                ''',
                'peer_timeout_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'keep-alive',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.Peers.Peer.RemoteAs' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.Peers.Peer.RemoteAs',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                First half of ASN in asdot format or 0 in
                asplain
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Second half of ASN in asdot format or
                complete ASN in asplain
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'remote-as',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.Peers.Peer.KeepAlive' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.Peers.Peer.KeepAlive',
            False, 
            [
            _MetaInfoClassMember('keep-alive-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '60')], [], 
                '''                Keep alive period in seconds
                ''',
                'keep_alive_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peer-timeout-period', ATTRIBUTE, 'int' , None, None, 
                [('1', '75')], [], 
                '''                Peer timeout period in seconds
                ''',
                'peer_timeout_period',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'keep-alive',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter',
            False, 
            [
            _MetaInfoClassMember('list', REFERENCE_ENUM_CLASS, 'MsdpListTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpListTypeVrfEnum', 
                [], [], 
                '''                Src List/RP List
                ''',
                'list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('filter-type', REFERENCE_ENUM_CLASS, 'MsdpFilterTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpFilterTypeVrfEnum', 
                [], [], 
                '''                Incoming/Outgoing ACL
                ''',
                'filter_type',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.Peers.Peer.SaFilters' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.Peers.Peer.SaFilters',
            False, 
            [
            _MetaInfoClassMember('sa-filter', REFERENCE_LIST, 'SaFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter', 
                [], [], 
                '''                SA-Filter incoming/outgoing list or RPlist
                ''',
                'sa_filter',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.Peers.Peer' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.Peers.Peer',
            False, 
            [
            _MetaInfoClassMember('peer-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Peer address
                ''',
                'peer_address',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('connect-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure interface name used for MSDP
                connection
                ''',
                'connect_source',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(1, 80)], [], 
                '''                Up to 80 characters describing this peer
                ''',
                'description',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabling Peer Configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('keep-alive', REFERENCE_CLASS, 'KeepAlive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.Peers.Peer.KeepAlive', 
                [], [], 
                '''                MSDP keep alive period
                ''',
                'keep_alive',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('max-sa', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Maximum SA accepted from this peer
                ''',
                'max_sa',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('mesh-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Configure an MSDP mesh-group
                ''',
                'mesh_group',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('nsr-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable NSR for the peer
                ''',
                'nsr_down',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peer-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Configuration of password of peer
                ''',
                'peer_password',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('remote-as', REFERENCE_CLASS, 'RemoteAs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.Peers.Peer.RemoteAs', 
                [], [], 
                '''                Configure the remote AS of this peer
                ''',
                'remote_as',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('sa-filters', REFERENCE_CLASS, 'SaFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.Peers.Peer.SaFilters', 
                [], [], 
                '''                Filter SA messages from peer
                ''',
                'sa_filters',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                MSDP Peer Shutdown
                ''',
                'shutdown',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Configure TTL Threshold for MSDP Peer
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'peer',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.Peers' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.Peers',
            False, 
            [
            _MetaInfoClassMember('peer', REFERENCE_LIST, 'Peer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.Peers.Peer', 
                [], [], 
                '''                Peer address
                ''',
                'peer',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'peers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.SaFilters.SaFilter' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.SaFilters.SaFilter',
            False, 
            [
            _MetaInfoClassMember('list', REFERENCE_ENUM_CLASS, 'MsdpListTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpListTypeVrfEnum', 
                [], [], 
                '''                Src List/RP List
                ''',
                'list',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('filter-type', REFERENCE_ENUM_CLASS, 'MsdpFilterTypeVrfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'MsdpFilterTypeVrfEnum', 
                [], [], 
                '''                Incoming/Outgoing ACL
                ''',
                'filter_type',
                'Cisco-IOS-XR-ipv4-msdp-cfg', True),
            _MetaInfoClassMember('access-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                Access list name
                ''',
                'access_list_name',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext.SaFilters' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext.SaFilters',
            False, 
            [
            _MetaInfoClassMember('sa-filter', REFERENCE_LIST, 'SaFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.SaFilters.SaFilter', 
                [], [], 
                '''                SA-Filter incoming/outgoing list or RPlist
                ''',
                'sa_filter',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'sa-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp.DefaultContext' : {
        'meta_info' : _MetaInfoClass('Msdp.DefaultContext',
            False, 
            [
            _MetaInfoClassMember('cache-state', REFERENCE_CLASS, 'CacheState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.CacheState', 
                [], [], 
                '''                Configure this systems SA cache access-lists
                ''',
                'cache_state',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('connect-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure interface name used for MSDP
                connection
                ''',
                'connect_source',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('default-peer', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Configure default peers for the box
                ''',
                'default_peer',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('keep-alive', REFERENCE_CLASS, 'KeepAlive' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.KeepAlive', 
                [], [], 
                '''                MSDP keep alive period
                ''',
                'keep_alive',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('max-peer-sa', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure inheritable MAX SA state for peers
                ''',
                'max_peer_sa',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('max-sa', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure context's MAX SA state for the router
                ''',
                'max_sa',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('originator-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Configure interface name used as originator ID
                ''',
                'originator_id',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('peers', REFERENCE_CLASS, 'Peers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.Peers', 
                [], [], 
                '''                Entering Peer Configuration
                ''',
                'peers',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('sa-filters', REFERENCE_CLASS, 'SaFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext.SaFilters', 
                [], [], 
                '''                Filter SA messages from peer
                ''',
                'sa_filters',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('ttl-threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Configure TTL Threshold for MSDP Peer
                ''',
                'ttl_threshold',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'default-context',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
    'Msdp' : {
        'meta_info' : _MetaInfoClass('Msdp',
            False, 
            [
            _MetaInfoClassMember('default-context', REFERENCE_CLASS, 'DefaultContext' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.DefaultContext', 
                [], [], 
                '''                Default Context
                ''',
                'default_context',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('global-max-sa', ATTRIBUTE, 'int' , None, None, 
                [('1', '75000')], [], 
                '''                Configure the global MAX SA state for the router
                ''',
                'global_max_sa',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('nsr-delay', ATTRIBUTE, 'int' , None, None, 
                [('5', '90')], [], 
                '''                NSR-Ready delay period for MSDP Peer
                ''',
                'nsr_delay',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg', 'Msdp.Vrfs', 
                [], [], 
                '''                VRF Table
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv4-msdp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-msdp-cfg',
            'msdp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-msdp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv4_msdp_cfg'
        ),
    },
}
_meta_table['Msdp.Vrfs.Vrf.Peers.Peer.SaFilters.SaFilter']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf.Peers.Peer.SaFilters']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.Peers.Peer.RemoteAs']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf.Peers.Peer']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.Peers.Peer.KeepAlive']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf.Peers.Peer']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.Peers.Peer.SaFilters']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf.Peers.Peer']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.Peers.Peer']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf.Peers']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.SaFilters.SaFilter']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf.SaFilters']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.CacheState']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.KeepAlive']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.Peers']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf']['meta_info']
_meta_table['Msdp.Vrfs.Vrf.SaFilters']['meta_info'].parent =_meta_table['Msdp.Vrfs.Vrf']['meta_info']
_meta_table['Msdp.Vrfs.Vrf']['meta_info'].parent =_meta_table['Msdp.Vrfs']['meta_info']
_meta_table['Msdp.DefaultContext.Peers.Peer.SaFilters.SaFilter']['meta_info'].parent =_meta_table['Msdp.DefaultContext.Peers.Peer.SaFilters']['meta_info']
_meta_table['Msdp.DefaultContext.Peers.Peer.RemoteAs']['meta_info'].parent =_meta_table['Msdp.DefaultContext.Peers.Peer']['meta_info']
_meta_table['Msdp.DefaultContext.Peers.Peer.KeepAlive']['meta_info'].parent =_meta_table['Msdp.DefaultContext.Peers.Peer']['meta_info']
_meta_table['Msdp.DefaultContext.Peers.Peer.SaFilters']['meta_info'].parent =_meta_table['Msdp.DefaultContext.Peers.Peer']['meta_info']
_meta_table['Msdp.DefaultContext.Peers.Peer']['meta_info'].parent =_meta_table['Msdp.DefaultContext.Peers']['meta_info']
_meta_table['Msdp.DefaultContext.SaFilters.SaFilter']['meta_info'].parent =_meta_table['Msdp.DefaultContext.SaFilters']['meta_info']
_meta_table['Msdp.DefaultContext.CacheState']['meta_info'].parent =_meta_table['Msdp.DefaultContext']['meta_info']
_meta_table['Msdp.DefaultContext.KeepAlive']['meta_info'].parent =_meta_table['Msdp.DefaultContext']['meta_info']
_meta_table['Msdp.DefaultContext.Peers']['meta_info'].parent =_meta_table['Msdp.DefaultContext']['meta_info']
_meta_table['Msdp.DefaultContext.SaFilters']['meta_info'].parent =_meta_table['Msdp.DefaultContext']['meta_info']
_meta_table['Msdp.Vrfs']['meta_info'].parent =_meta_table['Msdp']['meta_info']
_meta_table['Msdp.DefaultContext']['meta_info'].parent =_meta_table['Msdp']['meta_info']
