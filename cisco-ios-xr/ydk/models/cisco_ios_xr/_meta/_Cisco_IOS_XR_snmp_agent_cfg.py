


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SnmpPrivAlgorithmEnum' : _MetaInfoEnum('SnmpPrivAlgorithmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'none':'none',
            'des':'des',
            '3des':'Y_3des',
            'aes128':'aes128',
            'aes192':'aes192',
            'aes256':'aes256',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpOwnerAccessEnum' : _MetaInfoEnum('SnmpOwnerAccessEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'sdr-owner':'sdr_owner',
            'system-owner':'system_owner',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpPrecedenceValue1Enum' : _MetaInfoEnum('SnmpPrecedenceValue1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'routine':'routine',
            'priority':'priority',
            'immediate':'immediate',
            'flash':'flash',
            'flash-override':'flash_override',
            'critical':'critical',
            'internet':'internet',
            'network':'network',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpAccessLevelEnum' : _MetaInfoEnum('SnmpAccessLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'read-only':'read_only',
            'read-write':'read_write',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpBulkstatFileFormatEnum' : _MetaInfoEnum('SnmpBulkstatFileFormatEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'schema-ascii':'schema_ascii',
            'bulk-ascii':'bulk_ascii',
            'bulk-binary':'bulk_binary',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpMibViewInclusionEnum' : _MetaInfoEnum('SnmpMibViewInclusionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'included':'included',
            'excluded':'excluded',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpContextEnum' : _MetaInfoEnum('SnmpContextEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'vrf':'vrf',
            'bridge':'bridge',
            'ospf':'ospf',
            'ospfv3':'ospfv3',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'GroupSnmpVersionEnum' : _MetaInfoEnum('GroupSnmpVersionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'v1':'v1',
            'v2c':'v2c',
            'v3':'v3',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpHashAlgorithmEnum' : _MetaInfoEnum('SnmpHashAlgorithmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'none':'none',
            'md5':'md5',
            'sha':'sha',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpaclEnum' : _MetaInfoEnum('SnmpaclEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpSecurityModelEnum' : _MetaInfoEnum('SnmpSecurityModelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'no-authentication':'no_authentication',
            'authentication':'authentication',
            'privacy':'privacy',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpDscpValueEnum' : _MetaInfoEnum('SnmpDscpValueEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'default':'default',
            'af11':'af11',
            'af12':'af12',
            'af13':'af13',
            'af21':'af21',
            'af22':'af22',
            'af23':'af23',
            'af31':'af31',
            'af32':'af32',
            'af33':'af33',
            'af41':'af41',
            'af42':'af42',
            'af43':'af43',
            'ef':'ef',
            'cs1':'cs1',
            'cs2':'cs2',
            'cs3':'cs3',
            'cs4':'cs4',
            'cs5':'cs5',
            'cs6':'cs6',
            'cs7':'cs7',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpTosEnum' : _MetaInfoEnum('SnmpTosEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'precedence':'precedence',
            'dscp':'dscp',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'UserSnmpVersionEnum' : _MetaInfoEnum('UserSnmpVersionEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'v1':'v1',
            'v2c':'v2c',
            'v3':'v3',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'SnmpBulkstatSchemaEnum' : _MetaInfoEnum('SnmpBulkstatSchemaEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg',
        {
            'exact-interface':'exact_interface',
            'exact-oid':'exact_oid',
            'wild-interface':'wild_interface',
            'wild-oid':'wild_oid',
            'range-oid':'range_oid',
            'repeat-oid':'repeat_oid',
        }, 'Cisco-IOS-XR-snmp-agent-cfg', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg']),
    'Snmp.EncryptedCommunityMaps.EncryptedCommunityMap' : {
        'meta_info' : _MetaInfoClass('Snmp.EncryptedCommunityMaps.EncryptedCommunityMap',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMP community map
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Context Name 
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Security Name 
                ''',
                'security',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('target-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                target list name 
                ''',
                'target_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-community-map',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.EncryptedCommunityMaps' : {
        'meta_info' : _MetaInfoClass('Snmp.EncryptedCommunityMaps',
            False, 
            [
            _MetaInfoClassMember('encrypted-community-map', REFERENCE_LIST, 'EncryptedCommunityMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.EncryptedCommunityMaps.EncryptedCommunityMap', 
                [], [], 
                '''                Clear/encrypted SNMP community map
                ''',
                'encrypted_community_map',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-community-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Views.View' : {
        'meta_info' : _MetaInfoClass('Snmp.Views.View',
            False, 
            [
            _MetaInfoClassMember('view-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the view
                ''',
                'view_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('family', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MIB view family name
                ''',
                'family',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('view-inclusion', REFERENCE_ENUM_CLASS, 'SnmpMibViewInclusionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpMibViewInclusionEnum', 
                [], [], 
                '''                MIB view to be included or excluded
                ''',
                'view_inclusion',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'view',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Views' : {
        'meta_info' : _MetaInfoClass('Snmp.Views',
            False, 
            [
            _MetaInfoClassMember('view', REFERENCE_LIST, 'View' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Views.View', 
                [], [], 
                '''                Name of the view
                ''',
                'view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'views',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Logging.Threshold' : {
        'meta_info' : _MetaInfoClass('Snmp.Logging.Threshold',
            False, 
            [
            _MetaInfoClassMember('oid-processing', ATTRIBUTE, 'int' , None, None, 
                [('0', '20000')], [], 
                '''                SNMP logging threshold for OID processing
                ''',
                'oid_processing',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('pdu-processing', ATTRIBUTE, 'int' , None, None, 
                [('0', '20000')], [], 
                '''                SNMP logging threshold for PDU processing
                ''',
                'pdu_processing',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'threshold',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Logging' : {
        'meta_info' : _MetaInfoClass('Snmp.Logging',
            False, 
            [
            _MetaInfoClassMember('threshold', REFERENCE_CLASS, 'Threshold' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Logging.Threshold', 
                [], [], 
                '''                SNMP logging threshold
                ''',
                'threshold',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'logging',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Administration.DefaultCommunities.DefaultCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.DefaultCommunities.DefaultCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                SNMP community string
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('owner', REFERENCE_ENUM_CLASS, 'SnmpOwnerAccessEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccessEnum', 
                [], [], 
                '''                Logical Router or System owner access
                ''',
                'owner',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('priviledge', REFERENCE_ENUM_CLASS, 'SnmpAccessLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpAccessLevelEnum', 
                [], [], 
                '''                Read/Write Access
                ''',
                'priviledge',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('view-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MIB view to which the community has access
                ''',
                'view_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Administration.DefaultCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.DefaultCommunities',
            False, 
            [
            _MetaInfoClassMember('default-community', REFERENCE_LIST, 'DefaultCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.DefaultCommunities.DefaultCommunity', 
                [], [], 
                '''                Unencrpted SNMP community string and access
                priviledges
                ''',
                'default_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Administration.EncryptedCommunities.EncryptedCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.EncryptedCommunities.EncryptedCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMP community string
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('owner', REFERENCE_ENUM_CLASS, 'SnmpOwnerAccessEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccessEnum', 
                [], [], 
                '''                Logical Router or System owner access
                ''',
                'owner',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('priviledge', REFERENCE_ENUM_CLASS, 'SnmpAccessLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpAccessLevelEnum', 
                [], [], 
                '''                Read/Write Access
                ''',
                'priviledge',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('view-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MIB view to which the community has access
                ''',
                'view_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Administration.EncryptedCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration.EncryptedCommunities',
            False, 
            [
            _MetaInfoClassMember('encrypted-community', REFERENCE_LIST, 'EncryptedCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.EncryptedCommunities.EncryptedCommunity', 
                [], [], 
                '''                Clear/encrypted SNMP community string and
                access priviledges
                ''',
                'encrypted_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Administration' : {
        'meta_info' : _MetaInfoClass('Snmp.Administration',
            False, 
            [
            _MetaInfoClassMember('default-communities', REFERENCE_CLASS, 'DefaultCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.DefaultCommunities', 
                [], [], 
                '''                Container class to hold unencrpted communities
                ''',
                'default_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('encrypted-communities', REFERENCE_CLASS, 'EncryptedCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration.EncryptedCommunities', 
                [], [], 
                '''                Container class to hold clear/encrypted
                communities
                ''',
                'encrypted_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'administration',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Agent.EngineId.Remotes.Remote' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent.EngineId.Remotes.Remote',
            False, 
            [
            _MetaInfoClassMember('remote-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of remote SNMP entity
                ''',
                'remote_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('remote-engine-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                engine ID octet string
                ''',
                'remote_engine_id',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'remote',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Agent.EngineId.Remotes' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent.EngineId.Remotes',
            False, 
            [
            _MetaInfoClassMember('remote', REFERENCE_LIST, 'Remote' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent.EngineId.Remotes.Remote', 
                [], [], 
                '''                engineID of the remote agent
                ''',
                'remote',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'remotes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Agent.EngineId' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent.EngineId',
            False, 
            [
            _MetaInfoClassMember('local', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                engineID of the local agent
                ''',
                'local',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('remotes', REFERENCE_CLASS, 'Remotes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent.EngineId.Remotes', 
                [], [], 
                '''                SNMPv3 remote SNMP Entity
                ''',
                'remotes',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'engine-id',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Agent' : {
        'meta_info' : _MetaInfoClass('Snmp.Agent',
            False, 
            [
            _MetaInfoClassMember('engine-id', REFERENCE_CLASS, 'EngineId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent.EngineId', 
                [], [], 
                '''                SNMPv3 engineID
                ''',
                'engine_id',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'agent',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Trap' : {
        'meta_info' : _MetaInfoClass('Snmp.Trap',
            False, 
            [
            _MetaInfoClassMember('queue-length', ATTRIBUTE, 'int' , None, None, 
                [('1', '5000')], [], 
                '''                Message queue length for each TRAP host
                ''',
                'queue_length',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('throttle-time', ATTRIBUTE, 'int' , None, None, 
                [('10', '500')], [], 
                '''                Set throttle time for handling traps
                ''',
                'throttle_time',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '1000')], [], 
                '''                Timeout for TRAP message retransmissions
                ''',
                'timeout',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Ipv6.Tos' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv6.Tos',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                SNMP DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'SnmpDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpDscpValueEnum', 
                        [], [], 
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                ]),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                SNMP Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'SnmpPrecedenceValue1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrecedenceValue1Enum', 
                        [], [], 
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'SnmpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpTosEnum', 
                [], [], 
                '''                SNMP TOS type DSCP or Precedence
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Ipv6' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv6',
            False, 
            [
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv6.Tos', 
                [], [], 
                '''                Type of TOS
                ''',
                'tos',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'ipv6',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Ipv4.Tos' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv4.Tos',
            False, 
            [
            _MetaInfoClassMember('dscp', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                SNMP DSCP value
                ''',
                'dscp',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('dscp', REFERENCE_ENUM_CLASS, 'SnmpDscpValueEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpDscpValueEnum', 
                        [], [], 
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                    _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                        [('0', '63')], [], 
                        '''                        SNMP DSCP value
                        ''',
                        'dscp',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                ]),
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                SNMP Precedence value
                ''',
                'precedence',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_ENUM_CLASS, 'SnmpPrecedenceValue1Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrecedenceValue1Enum', 
                        [], [], 
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                    _MetaInfoClassMember('precedence', ATTRIBUTE, 'int' , None, None, 
                        [('0', '7')], [], 
                        '''                        SNMP Precedence value
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                ]),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'SnmpTosEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpTosEnum', 
                [], [], 
                '''                SNMP TOS type DSCP or Precedence
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'tos',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Ipv4' : {
        'meta_info' : _MetaInfoClass('Snmp.Ipv4',
            False, 
            [
            _MetaInfoClassMember('tos', REFERENCE_CLASS, 'Tos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv4.Tos', 
                [], [], 
                '''                Type of TOS
                ''',
                'tos',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'ipv4',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.System' : {
        'meta_info' : _MetaInfoClass('Snmp.System',
            False, 
            [
            _MetaInfoClassMember('chassis-id', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                String to uniquely identify this chassis
                ''',
                'chassis_id',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('contact', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                identification of the contact person for this
                managed node
                ''',
                'contact',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [(1, 255)], [], 
                '''                The physical location of this node
                ''',
                'location',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'system',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Target.Targets.Target_.VrfNames.VrfName' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.VrfNames.VrfName',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF Name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrf-name',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Target.Targets.Target_.VrfNames' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.VrfNames',
            False, 
            [
            _MetaInfoClassMember('vrf-name', REFERENCE_LIST, 'VrfName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.VrfNames.VrfName', 
                [], [], 
                '''                VRF name of the target
                ''',
                'vrf_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrf-names',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4/Ipv6 address
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/Ipv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4/Ipv6 address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target-address',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Target.Targets.Target_.TargetAddresses' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_.TargetAddresses',
            False, 
            [
            _MetaInfoClassMember('target-address', REFERENCE_LIST, 'TargetAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress', 
                [], [], 
                '''                IP Address to be configured for the Target
                ''',
                'target_address',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Target.Targets.Target_' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets.Target_',
            False, 
            [
            _MetaInfoClassMember('target-list-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name of the target list
                ''',
                'target_list_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('target-addresses', REFERENCE_CLASS, 'TargetAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.TargetAddresses', 
                [], [], 
                '''                SNMP Target address configurations
                ''',
                'target_addresses',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrf-names', REFERENCE_CLASS, 'VrfNames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_.VrfNames', 
                [], [], 
                '''                List of VRF Name for a target list
                ''',
                'vrf_names',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Target.Targets' : {
        'meta_info' : _MetaInfoClass('Snmp.Target.Targets',
            False, 
            [
            _MetaInfoClassMember('target', REFERENCE_LIST, 'Target_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets.Target_', 
                [], [], 
                '''                Name of the target list
                ''',
                'target',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'targets',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Target' : {
        'meta_info' : _MetaInfoClass('Snmp.Target',
            False, 
            [
            _MetaInfoClassMember('targets', REFERENCE_CLASS, 'Targets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target.Targets', 
                [], [], 
                '''                List of targets
                ''',
                'targets',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'target',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Snmp_' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Snmp_',
            False, 
            [
            _MetaInfoClassMember('authentication', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable authentication notification
                ''',
                'authentication',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('cold-start', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cold start notification
                ''',
                'cold_start',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SNMP notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('link-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable link down notification
                ''',
                'link_down',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('link-up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable link up notification
                ''',
                'link_up',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('warm-start', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable warm start notification
                ''',
                'warm_start',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'snmp',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Vpls' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Vpls',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CISCO-IETF-VPLS-GENERIC-MIB
                notifications
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('full-clear', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cvplsFwdFullAlarmCleared notification
                ''',
                'full_clear',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('full-raise', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cvplsFwdFullAlarmRaised notification
                ''',
                'full_raise',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cvplsStatusChanged notification
                ''',
                'status',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'vpls',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.L2Vpn' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.L2Vpn',
            False, 
            [
            _MetaInfoClassMember('cisco', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Cisco format including extra varbinds
                ''',
                'cisco',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CISCO-IETF-PW-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vc-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cpwVcDown notification
                ''',
                'vc_down',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vc-up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cpwVcUp notification
                ''',
                'vc_up',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            ],
            'Cisco-IOS-XR-l2vpn-cfg',
            'l2vpn',
            _yang_ns._namespaces['Cisco-IOS-XR-l2vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Isis' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Isis',
            False, 
            [
            _MetaInfoClassMember('adjacency-change', REFERENCE_ENUM_CLASS, 'IsisMibAdjacencyChangeBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAdjacencyChangeBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'adjacency_change',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('all', REFERENCE_ENUM_CLASS, 'IsisMibAllBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAllBooleanEnum', 
                [], [], 
                '''                Enable all isisMIB notifications
                ''',
                'all',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('area-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibAreaMismatchBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAreaMismatchBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'area_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('attempt-to-exceed-max-sequence', REFERENCE_ENUM_CLASS, 'IsisMibAttemptToExceedMaxSequenceBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAttemptToExceedMaxSequenceBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'attempt_to_exceed_max_sequence',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('authentication-failure', REFERENCE_ENUM_CLASS, 'IsisMibAuthenticationFailureBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationFailureBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'authentication_failure',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('authentication-type-failure', REFERENCE_ENUM_CLASS, 'IsisMibAuthenticationTypeFailureBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibAuthenticationTypeFailureBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'authentication_type_failure',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('corrupted-lsp-detected', REFERENCE_ENUM_CLASS, 'IsisMibCorruptedLspDetectedBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibCorruptedLspDetectedBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'corrupted_lsp_detected',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('database-overflow', REFERENCE_ENUM_CLASS, 'IsisMibDatabaseOverFlowBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibDatabaseOverFlowBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'database_overflow',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('id-length-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibIdLengthMismatchBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibIdLengthMismatchBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'id_length_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-error-detected', REFERENCE_ENUM_CLASS, 'IsisMibLspErrorDetectedBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspErrorDetectedBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'lsp_error_detected',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('lsp-too-large-to-propagate', REFERENCE_ENUM_CLASS, 'IsisMibLspTooLargeToPropagateBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibLspTooLargeToPropagateBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'lsp_too_large_to_propagate',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('manual-address-drops', REFERENCE_ENUM_CLASS, 'IsisMibManualAddressDropsBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibManualAddressDropsBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'manual_address_drops',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('max-area-address-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibMaxAreaAddressMismatchBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibMaxAreaAddressMismatchBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'max_area_address_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('originated-lsp-buffer-size-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibOriginatedLspBufferSizeMismatchBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOriginatedLspBufferSizeMismatchBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'originated_lsp_buffer_size_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('own-lsp-purge', REFERENCE_ENUM_CLASS, 'IsisMibOwnLspPurgeBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibOwnLspPurgeBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'own_lsp_purge',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('protocols-supported-mismatch', REFERENCE_ENUM_CLASS, 'IsisMibProtocolsSupportedMismatchBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibProtocolsSupportedMismatchBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'protocols_supported_mismatch',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('rejected-adjacency', REFERENCE_ENUM_CLASS, 'IsisMibRejectedAdjacencyBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibRejectedAdjacencyBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'rejected_adjacency',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('sequence-number-skip', REFERENCE_ENUM_CLASS, 'IsisMibSequenceNumberSkipBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibSequenceNumberSkipBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'sequence_number_skip',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('version-skew', REFERENCE_ENUM_CLASS, 'IsisMibVersionSkewBooleanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_clns_isis_cfg', 'IsisMibVersionSkewBooleanEnum', 
                [], [], 
                '''                Enable or disable
                ''',
                'version_skew',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            ],
            'Cisco-IOS-XR-clns-isis-cfg',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-clns-isis-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.ConfigMan' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.ConfigMan',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoConfigManMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-config-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-config-mibs-cfg',
            'config-man',
            _yang_ns._namespaces['Cisco-IOS-XR-config-mibs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Cfm' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Cfm',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable 802.1ag Connectivity Fault Management
                MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-cfm-cfg',
            'cfm',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-cfm-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Oam' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Oam',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable 802.3 OAM MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-cfg',
            'oam',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Flash' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Flash',
            False, 
            [
            _MetaInfoClassMember('insertion', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoFlashDeviceInsertedNotif
                notification
                ''',
                'insertion',
                'Cisco-IOS-XR-flashmib-cfg', False),
            _MetaInfoClassMember('removal', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoFlashDeviceRemovedNotif
                notification
                ''',
                'removal',
                'Cisco-IOS-XR-flashmib-cfg', False),
            ],
            'Cisco-IOS-XR-flashmib-cfg',
            'flash',
            _yang_ns._namespaces['Cisco-IOS-XR-flashmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.EntityRedundancy' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.EntityRedundancy',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CISCO-ENTITY-REDUNDANCY-MIB notification
                ''',
                'enable',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable status change notification
                ''',
                'status',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            _MetaInfoClassMember('switchover', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable switchover notification
                ''',
                'switchover',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-ceredundancymib-cfg',
            'entity-redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-ceredundancymib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.ConfigCopy' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.ConfigCopy',
            False, 
            [
            _MetaInfoClassMember('completion', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ccCopyCompletion notification
                ''',
                'completion',
                'Cisco-IOS-XR-infra-confcopymib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-confcopymib-cfg',
            'config-copy',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-confcopymib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.SelectiveVrfDownload' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.SelectiveVrfDownload',
            False, 
            [
            _MetaInfoClassMember('role-change', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable csvdEntityRoleChangeNotification
                notification
                ''',
                'role_change',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            ],
            'Cisco-IOS-XR-infra-rsi-cfg',
            'selective-vrf-download',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rsi-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.System' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.System',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoSystemMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-infra-systemmib-cfg', False),
            ],
            'Cisco-IOS-XR-infra-systemmib-cfg',
            'system',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-systemmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Bfd' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bfd',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CISCO-IETF-BFD-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            ],
            'Cisco-IOS-XR-ip-bfd-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-bfd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ntp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ntp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoNtpMIB notification configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-ntp-cfg',
            'ntp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-ntp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Rsvp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Rsvp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable all RSVP notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('lost-flow', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable lostFlow notification
                ''',
                'lost_flow',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('new-flow', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable newFlow notification
                ''',
                'new_flow',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            ],
            'Cisco-IOS-XR-ip-rsvp-cfg',
            'rsvp',
            _yang_ns._namespaces['Cisco-IOS-XR-ip-rsvp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Bgp.Bgp4Mib' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bgp.Bgp4Mib',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BGP4-MIB and CISCO-BGP4-MIB IPv4-only
                notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('up-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable BGP4-MIB and CISCO-BGP4-MIB IPv4-only
                up/down notifications
                ''',
                'up_down',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bgp4mib',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Bgp.CiscoBgp4Mib' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bgp.CiscoBgp4Mib',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CISCO-BGP4-MIB v2 notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('up-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CISCO-BGP4-MIB v2 up/down notifications
                ''',
                'up_down',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'cisco-bgp4mib',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Bgp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Bgp',
            False, 
            [
            _MetaInfoClassMember('bgp4mib', REFERENCE_CLASS, 'Bgp4Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bgp.Bgp4Mib', 
                [], [], 
                '''                Enable BGP4-MIB and CISCO-BGP4-MIB IPv4-only
                notifications: bgpEstablishedNotification,
                bgpBackwardTransNotification,
                cbgpFsmStateChange, cbgpBackwardTransition,
                cbgpPrefixThresholdExceeded,
                cbgpPrefixThresholdClear.
                ''',
                'bgp4mib',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cisco-bgp4mib', REFERENCE_CLASS, 'CiscoBgp4Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bgp.CiscoBgp4Mib', 
                [], [], 
                '''                Enable CISCO-BGP4-MIB v2 notifications:
                cbgpPeer2EstablishedNotification,
                cbgpPeer2BackwardTransNotification,
                cbgpPeer2FsmStateChange,
                cbgpPeer2BackwardTransition,
                cbgpPeer2PrefixThresholdExceeded,
                cbgpPeer2PrefixThresholdClear.
                ''',
                'cisco_bgp4mib',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-bgp-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-bgp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Hsrp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Hsrp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CISCO-HSRP-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-hsrp-cfg',
            'hsrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-hsrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospf.Lsa' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.Lsa',
            False, 
            [
            _MetaInfoClassMember('max-age-lsa', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfMaxAgeLsa notification
                ''',
                'max_age_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('originate-lsa', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfOriginateLsa notification
                ''',
                'originate_lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospf.StateChange' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.StateChange',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfIfStateChange notification
                ''',
                'interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfNbrStateChange notification
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-interface', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfVirtIfStateChange notification
                ''',
                'virtual_interface',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-neighbor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfVirtNbrStateChange notification
                ''',
                'virtual_neighbor',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospf.Retransmit' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.Retransmit',
            False, 
            [
            _MetaInfoClassMember('packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfTxRetransmit notification
                ''',
                'packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfVirtIfTxRetransmit notification
                ''',
                'virtual_packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'retransmit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospf.Error' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf.Error',
            False, 
            [
            _MetaInfoClassMember('authentication-failure', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfIfAuthFailure notification
                ''',
                'authentication_failure',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('bad-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfIfRxBadPacket notification
                ''',
                'bad_packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('config-error', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfIfConfigError notification
                ''',
                'config_error',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-authentication-failure', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfVirtIfAuthFailure notification
                ''',
                'virtual_authentication_failure',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-bad-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfVirtIfRxBadPacket notification
                ''',
                'virtual_bad_packet',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('virtual-config-error', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfVirtIfConfigError notification
                ''',
                'virtual_config_error',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospf' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospf',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_CLASS, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.Error', 
                [], [], 
                '''                SNMP notifications for OSPF errors
                ''',
                'error',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('lsa', REFERENCE_CLASS, 'Lsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.Lsa', 
                [], [], 
                '''                SNMP notifications related to LSAs
                ''',
                'lsa',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('retransmit', REFERENCE_CLASS, 'Retransmit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.Retransmit', 
                [], [], 
                '''                SNMP notifications for packet retransmissions
                ''',
                'retransmit',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('state-change', REFERENCE_CLASS, 'StateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf.StateChange', 
                [], [], 
                '''                SNMP notifications for OSPF state change
                ''',
                'state_change',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-ospf-cfg',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-ospf-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Vrrp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Vrrp',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable VRRP-MIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-ipv4-vrrp-cfg',
            'vrrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv4-vrrp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospfv3.Error' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospfv3.Error',
            False, 
            [
            _MetaInfoClassMember('bad-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3IfRxBadPacket notification
                ''',
                'bad_packet',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('config-error', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3IfConfigError notification
                ''',
                'config_error',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-bad-packet', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3VirtIfRxBadPacket notification
                ''',
                'virtual_bad_packet',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-config-error', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3VirtIfConfigError notification
                ''',
                'virtual_config_error',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'error',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospfv3.StateChange' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospfv3.StateChange',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3IfStateChange notification
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('neighbor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3NbrStateChange notification
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-translator', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3NssaTranslatorStatusChange
                notification
                ''',
                'nssa_translator',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('restart', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3RestartStatusChange notification
                ''',
                'restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('restart-helper', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3NbrRestartHelperStatusChange
                notification
                ''',
                'restart_helper',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('restart-virtual-helper', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3VirtNbrRestartHelperStatusChange
                notification
                ''',
                'restart_virtual_helper',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-interface', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3VirtIfStateChange notification
                ''',
                'virtual_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-neighbor', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ospfv3VirtNbrStateChange notification
                ''',
                'virtual_neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'state-change',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Ospfv3' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Ospfv3',
            False, 
            [
            _MetaInfoClassMember('error', REFERENCE_CLASS, 'Error' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospfv3.Error', 
                [], [], 
                '''                SNMP notifications for OSPF errors
                ''',
                'error',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('state-change', REFERENCE_CLASS, 'StateChange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospfv3.StateChange', 
                [], [], 
                '''                SNMP notifications for OSPF state change
                ''',
                'state_change',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ospfv3',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.MplsLdp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsLdp',
            False, 
            [
            _MetaInfoClassMember('init-session-threshold-exceeded', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsLdpInitSessionThresholdExceeded
                notification
                ''',
                'init_session_threshold_exceeded',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('session-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsLdpSessionDown notification
                ''',
                'session_down',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('session-up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsLdpSessionUp notification
                ''',
                'session_up',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-ldp-cfg',
            'mpls-ldp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-ldp-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.MplsTeP2Mp' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsTeP2Mp',
            False, 
            [
            _MetaInfoClassMember('down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsTeP2mpTunnelDestDown notification
                ''',
                'down',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsTeP2mpTunnelDestUp notification
                ''',
                'up',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-p2mp',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.MplsTe.CiscoExtension' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsTe.CiscoExtension',
            False, 
            [
            _MetaInfoClassMember('bringup-fail', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsTunnelBringupFail notification
                ''',
                'bringup_fail',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('insufficient-bandwidth', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsTunnelInsuffBW notification
                ''',
                'insufficient_bandwidth',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('preempt', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsTunnelPreempt notification
                ''',
                'preempt',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('re-route-pending', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsTunnelReRoutePending notification
                ''',
                're_route_pending',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('re-route-pending-clear', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsTunnelReRoutePendingClear
                notification
                ''',
                're_route_pending_clear',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'cisco-extension',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.MplsTe' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsTe',
            False, 
            [
            _MetaInfoClassMember('cisco', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS TE tunnel Cisco format (default
                IETF) notification
                ''',
                'cisco',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('cisco-extension', REFERENCE_CLASS, 'CiscoExtension' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsTe.CiscoExtension', 
                [], [], 
                '''                CISCO-MPLS-TE-STD-EXT-MIB notification
                configuration
                ''',
                'cisco_extension',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsTunnelDown notification
                ''',
                'down',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reoptimize', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsTunnelReoptimized notification
                ''',
                'reoptimize',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('reroute', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsTunnelRerouted notification
                ''',
                'reroute',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsTunnelUp notification
                ''',
                'up',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.MplsFrr' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsFrr',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsFrrMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('protected', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsFrrProtected notification
                ''',
                'protected',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('unprotected', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cmplsFrrUnProtected notification
                ''',
                'unprotected',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-frr',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.MplsL3Vpn' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.MplsL3Vpn',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsL3VpnMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('max-threshold-cleared', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsL3VpnNumVrfRouteMaxThreshCleared
                notification
                ''',
                'max_threshold_cleared',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('max-threshold-exceeded', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsL3VpnVrfNumVrfRouteMaxThreshExceeded
                notification
                ''',
                'max_threshold_exceeded',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('max-threshold-reissue-notification-time', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Time interval (secs) for re-issuing
                max-threshold notification
                ''',
                'max_threshold_reissue_notification_time',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('mid-threshold-exceeded', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsL3VpnVrfRouteMidThreshExceeded
                notification
                ''',
                'mid_threshold_exceeded',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('vrf-down', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsL3VpnVrfDown notification
                ''',
                'vrf_down',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('vrf-up', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable mplsL3VpnVrfUp notification
                ''',
                'vrf_up',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-vpn-cfg',
            'mpls-l3vpn',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-vpn-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Otn' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Otn',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoOtnIfMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-otnifmib-cfg', False),
            ],
            'Cisco-IOS-XR-otnifmib-cfg',
            'otn',
            _yang_ns._namespaces['Cisco-IOS-XR-otnifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Sensor' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Sensor',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable entitySensorMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-ciscosensormib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ciscosensormib-cfg',
            'sensor',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ciscosensormib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Entity' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Entity',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable entityMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-entitymib-cfg',
            'entity',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-entitymib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.EntityState' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.EntityState',
            False, 
            [
            _MetaInfoClassMember('oper-status', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable entStateOperEnable and
                entStateOperDisable notifications
                ''',
                'oper_status',
                'Cisco-IOS-XR-snmp-entstatemib-cfg', False),
            _MetaInfoClassMember('switchover', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ceStateExtStandbySwitchover notification
                ''',
                'switchover',
                'Cisco-IOS-XR-snmp-entstatemib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-entstatemib-cfg',
            'entity-state',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-entstatemib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.FruControl' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.FruControl',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoEntityFRUControlMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-frucontrolmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-frucontrolmib-cfg',
            'fru-control',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-frucontrolmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Rf' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Rf',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoRFMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-mib-rfmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-mib-rfmib-cfg',
            'rf',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-mib-rfmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification.Syslog' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification.Syslog',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ciscoSyslogMIB notifications
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-syslogmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-syslogmib-cfg',
            'syslog',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-syslogmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Notification' : {
        'meta_info' : _MetaInfoClass('Snmp.Notification',
            False, 
            [
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bfd', 
                [], [], 
                '''                CISCO-IETF-BFD-MIB notification configuration
                ''',
                'bfd',
                'Cisco-IOS-XR-ip-bfd-cfg', False),
            _MetaInfoClassMember('bgp', REFERENCE_CLASS, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Bgp', 
                [], [], 
                '''                BGP4-MIB and CISCO-BGP4-MIB notification
                configuration
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv4-bgp-cfg', False),
            _MetaInfoClassMember('cfm', REFERENCE_CLASS, 'Cfm' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Cfm', 
                [], [], 
                '''                802.1ag Connectivity Fault Management MIB
                notification configuration
                ''',
                'cfm',
                'Cisco-IOS-XR-ethernet-cfm-cfg', False),
            _MetaInfoClassMember('config-copy', REFERENCE_CLASS, 'ConfigCopy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.ConfigCopy', 
                [], [], 
                '''                CISCO-CONFIG-COPY-MIB notification configuration
                ''',
                'config_copy',
                'Cisco-IOS-XR-infra-confcopymib-cfg', False),
            _MetaInfoClassMember('config-man', REFERENCE_CLASS, 'ConfigMan' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.ConfigMan', 
                [], [], 
                '''                CISCO-CONFIG-MAN-MIB notification configurations
                ''',
                'config_man',
                'Cisco-IOS-XR-config-mibs-cfg', False),
            _MetaInfoClassMember('entity', REFERENCE_CLASS, 'Entity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Entity', 
                [], [], 
                '''                Enable ENTITY-MIB notifications
                ''',
                'entity',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            _MetaInfoClassMember('entity-redundancy', REFERENCE_CLASS, 'EntityRedundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.EntityRedundancy', 
                [], [], 
                '''                CISCO-ENTITY-REDUNDANCY-MIB notification
                configuration
                ''',
                'entity_redundancy',
                'Cisco-IOS-XR-infra-ceredundancymib-cfg', False),
            _MetaInfoClassMember('entity-state', REFERENCE_CLASS, 'EntityState' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.EntityState', 
                [], [], 
                '''                ENTITY-STATE-MIB notification configuration
                ''',
                'entity_state',
                'Cisco-IOS-XR-snmp-entstatemib-cfg', False),
            _MetaInfoClassMember('flash', REFERENCE_CLASS, 'Flash' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Flash', 
                [], [], 
                '''                CISCO-FLASH-MIB notification configuration
                ''',
                'flash',
                'Cisco-IOS-XR-flashmib-cfg', False),
            _MetaInfoClassMember('fru-control', REFERENCE_CLASS, 'FruControl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.FruControl', 
                [], [], 
                '''                CISCO-ENTITY-FRU-CONTROL-MIB notification
                configuration
                ''',
                'fru_control',
                'Cisco-IOS-XR-snmp-frucontrolmib-cfg', False),
            _MetaInfoClassMember('hsrp', REFERENCE_CLASS, 'Hsrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Hsrp', 
                [], [], 
                '''                CISCO-HSRP-MIB notification configuration
                ''',
                'hsrp',
                'Cisco-IOS-XR-ipv4-hsrp-cfg', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Isis', 
                [], [], 
                '''                Enable ISIS-MIB notifications
                ''',
                'isis',
                'Cisco-IOS-XR-clns-isis-cfg', False),
            _MetaInfoClassMember('l2vpn', REFERENCE_CLASS, 'L2Vpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.L2Vpn', 
                [], [], 
                '''                CISCO-IETF-PW-MIB notification configuration
                ''',
                'l2vpn',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('mpls-frr', REFERENCE_CLASS, 'MplsFrr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsFrr', 
                [], [], 
                '''                CISCO-IETF-FRR-MIB notification configuration
                ''',
                'mpls_frr',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-l3vpn', REFERENCE_CLASS, 'MplsL3Vpn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsL3Vpn', 
                [], [], 
                '''                MPLS-L3VPN-STD-MIB notification configuration
                ''',
                'mpls_l3vpn',
                'Cisco-IOS-XR-mpls-vpn-cfg', False),
            _MetaInfoClassMember('mpls-ldp', REFERENCE_CLASS, 'MplsLdp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsLdp', 
                [], [], 
                '''                MPLS-LDP-STD-MIB notification configuration
                ''',
                'mpls_ldp',
                'Cisco-IOS-XR-mpls-ldp-cfg', False),
            _MetaInfoClassMember('mpls-te', REFERENCE_CLASS, 'MplsTe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsTe', 
                [], [], 
                '''                MPLS-TE-STD-MIB notification configuration
                ''',
                'mpls_te',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-te-p2mp', REFERENCE_CLASS, 'MplsTeP2Mp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.MplsTeP2Mp', 
                [], [], 
                '''                CISCO-MPLS-TE-P2MP-STD-MIB notification
                configuration
                ''',
                'mpls_te_p2mp',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('ntp', REFERENCE_CLASS, 'Ntp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ntp', 
                [], [], 
                '''                CISCO-NTP-MIB notification configuration
                ''',
                'ntp',
                'Cisco-IOS-XR-ip-ntp-cfg', False),
            _MetaInfoClassMember('oam', REFERENCE_CLASS, 'Oam' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Oam', 
                [], [], 
                '''                802.3 OAM MIB notification configuration
                ''',
                'oam',
                'Cisco-IOS-XR-ethernet-link-oam-cfg', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospf', 
                [], [], 
                '''                OSPF-MIB notification configuration
                ''',
                'ospf',
                'Cisco-IOS-XR-ipv4-ospf-cfg', False),
            _MetaInfoClassMember('ospfv3', REFERENCE_CLASS, 'Ospfv3' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Ospfv3', 
                [], [], 
                '''                OSPFv3-MIB notification configuration
                ''',
                'ospfv3',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('otn', REFERENCE_CLASS, 'Otn' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Otn', 
                [], [], 
                '''                CISCO-OTN-IF-MIB notification configuration
                ''',
                'otn',
                'Cisco-IOS-XR-otnifmib-cfg', False),
            _MetaInfoClassMember('rf', REFERENCE_CLASS, 'Rf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Rf', 
                [], [], 
                '''                CISCO-RF-MIB notification configuration
                ''',
                'rf',
                'Cisco-IOS-XR-snmp-mib-rfmib-cfg', False),
            _MetaInfoClassMember('rsvp', REFERENCE_CLASS, 'Rsvp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Rsvp', 
                [], [], 
                '''                Enable RSVP-MIB notifications
                ''',
                'rsvp',
                'Cisco-IOS-XR-ip-rsvp-cfg', False),
            _MetaInfoClassMember('selective-vrf-download', REFERENCE_CLASS, 'SelectiveVrfDownload' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.SelectiveVrfDownload', 
                [], [], 
                '''                CISCO-SELECTIVE-VRF-DOWNLOAD-MIB notification
                configuration
                ''',
                'selective_vrf_download',
                'Cisco-IOS-XR-infra-rsi-cfg', False),
            _MetaInfoClassMember('sensor', REFERENCE_CLASS, 'Sensor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Sensor', 
                [], [], 
                '''                CISCO-ENTITY-SENSOR-MIB notification
                configuration
                ''',
                'sensor',
                'Cisco-IOS-XR-snmp-ciscosensormib-cfg', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Snmp_', 
                [], [], 
                '''                SNMP notification configuration
                ''',
                'snmp',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('syslog', REFERENCE_CLASS, 'Syslog' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Syslog', 
                [], [], 
                '''                CISCO-SYSLOG-MIB notification configuration
                ''',
                'syslog',
                'Cisco-IOS-XR-snmp-syslogmib-cfg', False),
            _MetaInfoClassMember('system', REFERENCE_CLASS, 'System' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.System', 
                [], [], 
                '''                CISCO-SYSTEM-MIB notification configuration
                ''',
                'system',
                'Cisco-IOS-XR-infra-systemmib-cfg', False),
            _MetaInfoClassMember('vpls', REFERENCE_CLASS, 'Vpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Vpls', 
                [], [], 
                '''                CISCO-IETF-VPLS-GENERIC-MIB notification
                configuration
                ''',
                'vpls',
                'Cisco-IOS-XR-l2vpn-cfg', False),
            _MetaInfoClassMember('vrrp', REFERENCE_CLASS, 'Vrrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification.Vrrp', 
                [], [], 
                '''                VRRP-MIB notification configuration
                ''',
                'vrrp',
                'Cisco-IOS-XR-ipv4-vrrp-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'notification',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular Expression to match index
                ''',
                'index',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular Expression to match value
                ''',
                'value',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'match',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of varbind (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match', 
                [], [], 
                '''                VarBind match conditions
                ''',
                'match',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-bind',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds',
            False, 
            [
            _MetaInfoClassMember('var-bind', REFERENCE_LIST, 'VarBind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind', 
                [], [], 
                '''                Varbind match conditions
                ''',
                'var_bind',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-binds',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of rootcause trap (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('created', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create rootcause
                ''',
                'created',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('var-binds', REFERENCE_CLASS, 'VarBinds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds', 
                [], [], 
                '''                Varbinds to match
                ''',
                'var_binds',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'root-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.RootCauses',
            False, 
            [
            _MetaInfoClassMember('root-cause', REFERENCE_LIST, 'RootCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause', 
                [], [], 
                '''                The rootcause - maximum of one can be
                configured per rule
                ''',
                'root_cause',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'root-causes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular Expression to match index
                ''',
                'index',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular Expression to match value
                ''',
                'value',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'match',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of varbind (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('match', REFERENCE_CLASS, 'Match' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match', 
                [], [], 
                '''                VarBind match conditions
                ''',
                'match',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-bind',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds',
            False, 
            [
            _MetaInfoClassMember('var-bind', REFERENCE_LIST, 'VarBind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind', 
                [], [], 
                '''                Varbind match conditions
                ''',
                'var_bind',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'var-binds',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of nonrootcause trap (dotted decimal)
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('created', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Create nonrootcause
                ''',
                'created',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('var-binds', REFERENCE_CLASS, 'VarBinds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds', 
                [], [], 
                '''                Varbinds to match
                ''',
                'var_binds',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'non-root-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses',
            False, 
            [
            _MetaInfoClassMember('non-root-cause', REFERENCE_LIST, 'NonRootCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause', 
                [], [], 
                '''                A non-rootcause
                ''',
                'non_root_cause',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'non-root-causes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.NonStateful' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.NonStateful',
            False, 
            [
            _MetaInfoClassMember('non-root-causes', REFERENCE_CLASS, 'NonRootCauses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses', 
                [], [], 
                '''                Table of configured non-rootcause
                ''',
                'non_root_causes',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('root-causes', REFERENCE_CLASS, 'RootCauses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful.RootCauses', 
                [], [], 
                '''                Table of configured rootcause (only one
                entry allowed)
                ''',
                'root_causes',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Timeout (time to wait for active
                correlation) in milliseconds
                ''',
                'timeout',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'non-stateful',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Port (specify 162 for default)
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.AppliedTo.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host', 
                [], [], 
                '''                A destination host
                ''',
                'host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule.AppliedTo' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule.AppliedTo',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Apply to all of the device
                ''',
                'all',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.AppliedTo.Hosts', 
                [], [], 
                '''                Table of configured hosts to apply rules to
                ''',
                'hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'applied-to',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules.Rule' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules.Rule',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Rule name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('applied-to', REFERENCE_CLASS, 'AppliedTo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.AppliedTo', 
                [], [], 
                '''                Applied to the Rule or Ruleset
                ''',
                'applied_to',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('non-stateful', REFERENCE_CLASS, 'NonStateful' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule.NonStateful', 
                [], [], 
                '''                The Non-Stateful Rule Type
                ''',
                'non_stateful',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rule',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.Rules' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Rules',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules.Rule', 
                [], [], 
                '''                Rule name
                ''',
                'rule',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rules',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename',
            False, 
            [
            _MetaInfoClassMember('rulename', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Rule name
                ''',
                'rulename',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rulename',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.Rulenames' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.Rulenames',
            False, 
            [
            _MetaInfoClassMember('rulename', REFERENCE_LIST, 'Rulename' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename', 
                [], [], 
                '''                A rulename
                ''',
                'rulename',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rulenames',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Port (specify 162 for default)
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host', 
                [], [], 
                '''                A destination host
                ''',
                'host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet.AppliedTo' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet.AppliedTo',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Apply to all of the device
                ''',
                'all',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts', 
                [], [], 
                '''                Table of configured hosts to apply rules to
                ''',
                'hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'applied-to',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.RuleSets.RuleSet' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets.RuleSet',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Ruleset name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('applied-to', REFERENCE_CLASS, 'AppliedTo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.AppliedTo', 
                [], [], 
                '''                Applied to the Rule or Ruleset
                ''',
                'applied_to',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('rulenames', REFERENCE_CLASS, 'Rulenames' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet.Rulenames', 
                [], [], 
                '''                Table of configured rulenames
                ''',
                'rulenames',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rule-set',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator.RuleSets' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSets',
            False, 
            [
            _MetaInfoClassMember('rule-set', REFERENCE_LIST, 'RuleSet' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets.RuleSet', 
                [], [], 
                '''                Ruleset name
                ''',
                'rule_set',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'rule-sets',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Correlator' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator',
            False, 
            [
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('1024', '52428800')], [], 
                '''                Configure size of the correlator buffer
                ''',
                'buffer_size',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('rule-sets', REFERENCE_CLASS, 'RuleSets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.RuleSets', 
                [], [], 
                '''                Table of configured rulesets
                ''',
                'rule_sets',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('rules', REFERENCE_CLASS, 'Rules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator.Rules', 
                [], [], 
                '''                Table of configured rules
                ''',
                'rules',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'correlator',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Schemas.Schema.Instance' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Schemas.Schema.Instance',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                End Instance OID for repetition
                ''',
                'end',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Instance of the schema
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('max', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Max value of Instance repetition
                ''',
                'max',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start Instance OID for repetition
                ''',
                'start',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('sub-interface', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Include all the subinterface
                ''',
                'sub_interface',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'SnmpBulkstatSchemaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatSchemaEnum', 
                [], [], 
                '''                Type of the instance
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Schemas.Schema' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Schemas.Schema',
            False, 
            [
            _MetaInfoClassMember('schema-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The name of the schema
                ''',
                'schema_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('instance', REFERENCE_CLASS, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Schemas.Schema.Instance', 
                [], [], 
                '''                Object instance information
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '20000')], [], 
                '''                Periodicity for polling of objects in this
                schema in minutes
                ''',
                'poll_interval',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('schema-object-list', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of an object List
                ''',
                'schema_object_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure schema name
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'schema',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Schemas' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Schemas',
            False, 
            [
            _MetaInfoClassMember('schema', REFERENCE_LIST, 'Schema' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Schemas.Schema', 
                [], [], 
                '''                The name of the Schema
                ''',
                'schema',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'schemas',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Objects.Object.Objects_.Object_' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects.Object.Objects_.Object_',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Object name or OID 
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Objects.Object.Objects_' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects.Object.Objects_',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects.Object.Objects_.Object_', 
                [], [], 
                '''                Object name or OID
                ''',
                'object',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Objects.Object' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects.Object',
            False, 
            [
            _MetaInfoClassMember('object-list-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of the object List
                ''',
                'object_list_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects.Object.Objects_', 
                [], [], 
                '''                Configure an object List
                ''',
                'objects',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure object list name
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'object',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Objects' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Objects',
            False, 
            [
            _MetaInfoClassMember('object', REFERENCE_LIST, 'Object' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects.Object', 
                [], [], 
                '''                Name of the object List
                ''',
                'object',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'objects',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema',
            False, 
            [
            _MetaInfoClassMember('schema-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Schema that contains objects to be
                collected
                ''',
                'schema_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfer-schema',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Transfers.Transfer.TransferSchemas' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers.Transfer.TransferSchemas',
            False, 
            [
            _MetaInfoClassMember('transfer-schema', REFERENCE_LIST, 'TransferSchema' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema', 
                [], [], 
                '''                Schema that contains objects to be collected
                ''',
                'transfer_schema',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfer-schemas',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Transfers.Transfer' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers.Transfer',
            False, 
            [
            _MetaInfoClassMember('transfer-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Name of bulk transfer
                ''',
                'transfer_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('1024', '2147483647')], [], 
                '''                Bulkstat data file maximum size in bytes
                ''',
                'buffer_size',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Start Data Collection for this Configuration
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('format', REFERENCE_ENUM_CLASS, 'SnmpBulkstatFileFormatEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpBulkstatFileFormatEnum', 
                [], [], 
                '''                Format of the bulk data file
                ''',
                'format',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Periodicity for the transfer of bulk data in
                minutes
                ''',
                'interval',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('primary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                FTP or rcp or TFTP can be used for file
                transfer
                ''',
                'primary',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('retain', ATTRIBUTE, 'int' , None, None, 
                [('0', '20000')], [], 
                '''                Retention period in minutes
                ''',
                'retain',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('retry', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Number of transmission retries
                ''',
                'retry',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('secondary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                FTP or rcp or TFTP can be used for file
                transfer
                ''',
                'secondary',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('transfer-schemas', REFERENCE_CLASS, 'TransferSchemas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers.Transfer.TransferSchemas', 
                [], [], 
                '''                Schema that contains objects to be collected
                ''',
                'transfer_schemas',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Configure transfer list name
                ''',
                'type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfer',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats.Transfers' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats.Transfers',
            False, 
            [
            _MetaInfoClassMember('transfer', REFERENCE_LIST, 'Transfer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers.Transfer', 
                [], [], 
                '''                Name of bulk transfer
                ''',
                'transfer',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'transfers',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.BulkStats' : {
        'meta_info' : _MetaInfoClass('Snmp.BulkStats',
            False, 
            [
            _MetaInfoClassMember('memory', ATTRIBUTE, 'int' , None, None, 
                [('100', '200000')], [], 
                '''                per process memory limit in kilo bytes
                ''',
                'memory',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('objects', REFERENCE_CLASS, 'Objects' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Objects', 
                [], [], 
                '''                Configure an Object List 
                ''',
                'objects',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('schemas', REFERENCE_CLASS, 'Schemas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Schemas', 
                [], [], 
                '''                Configure schema definition
                ''',
                'schemas',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('transfers', REFERENCE_CLASS, 'Transfers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats.Transfers', 
                [], [], 
                '''                Periodicity for the transfer of bulk data in
                minutes
                ''',
                'transfers',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'bulk-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.DefaultCommunityMaps.DefaultCommunityMap' : {
        'meta_info' : _MetaInfoClass('Snmp.DefaultCommunityMaps.DefaultCommunityMap',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                SNMP community map
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Context Name 
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Security Name 
                ''',
                'security',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('target-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                target list name 
                ''',
                'target_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-community-map',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.DefaultCommunityMaps' : {
        'meta_info' : _MetaInfoClass('Snmp.DefaultCommunityMaps',
            False, 
            [
            _MetaInfoClassMember('default-community-map', REFERENCE_LIST, 'DefaultCommunityMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.DefaultCommunityMaps.DefaultCommunityMap', 
                [], [], 
                '''                Unencrpted SNMP community map name 
                ''',
                'default_community_map',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-community-maps',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.OverloadControl' : {
        'meta_info' : _MetaInfoClass('Snmp.OverloadControl',
            False, 
            [
            _MetaInfoClassMember('drop-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Drop time in seconds for incoming queue
                (default 1 sec)
                ''',
                'drop_time',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('throttle-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '1000')], [], 
                '''                Throttle time in milliseconds for incoming
                queue (default 500 msec)
                ''',
                'throttle_rate',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'overload-control',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Timeouts' : {
        'meta_info' : _MetaInfoClass('Snmp.Timeouts',
            False, 
            [
            _MetaInfoClassMember('duplicates', ATTRIBUTE, 'int' , None, None, 
                [('0', '20')], [], 
                '''                Duplicate request feature timeout
                ''',
                'duplicates',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('in-qdrop', ATTRIBUTE, 'int' , None, None, 
                [('0', '20')], [], 
                '''                incoming queue drop feature timeout
                ''',
                'in_qdrop',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('pdu-stats', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                SNMP pdu statistics timeout
                ''',
                'pdu_stats',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('subagent', ATTRIBUTE, 'int' , None, None, 
                [('1', '20')], [], 
                '''                Sub-Agent Request timeout
                ''',
                'subagent',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'timeouts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Users.User' : {
        'meta_info' : _MetaInfoClass('Snmp.Users.User',
            False, 
            [
            _MetaInfoClassMember('user-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the user
                ''',
                'user_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'SnmpHashAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpHashAlgorithmEnum', 
                [], [], 
                '''                The algorithm used md5 or sha
                ''',
                'algorithm',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The authentication password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('authentication-password-configured', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Flag to indicate that authentication password
                is configred for version 3
                ''',
                'authentication_password_configured',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('group-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group to which the user belongs
                ''',
                'group_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('owner', REFERENCE_ENUM_CLASS, 'SnmpOwnerAccessEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpOwnerAccessEnum', 
                [], [], 
                '''                The system access either SDROwner or
                SystemOwner
                ''',
                'owner',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('priv-algorithm', REFERENCE_ENUM_CLASS, 'SnmpPrivAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpPrivAlgorithmEnum', 
                [], [], 
                '''                The algorithm used des56 or aes128 or aes192or
                aes256 or 3des
                ''',
                'priv_algorithm',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('privacy-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                The privacy password
                ''',
                'privacy_password',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('privacy-password-configured', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Flag to indicate that the privacy password is
                configured for version 3
                ''',
                'privacy_password_configured',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('remote-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of remote SNMP entity
                ''',
                'remote_address',
                'Cisco-IOS-XR-snmp-agent-cfg', False, [
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                    _MetaInfoClassMember('remote-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of remote SNMP entity
                        ''',
                        'remote_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', False),
                ]),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', REFERENCE_ENUM_CLASS, 'UserSnmpVersionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'UserSnmpVersionEnum', 
                [], [], 
                '''                SNMP version to be used. v1,v2c or v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'user',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Users' : {
        'meta_info' : _MetaInfoClass('Snmp.Users',
            False, 
            [
            _MetaInfoClassMember('user', REFERENCE_LIST, 'User' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Users.User', 
                [], [], 
                '''                Name of the user
                ''',
                'user',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'users',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v1/v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities',
            False, 
            [
            _MetaInfoClassMember('encrypted-user-community', REFERENCE_LIST, 'EncryptedUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity', 
                [], [], 
                '''                Clear/Encrypt Community name associated with
                a trap host
                ''',
                'encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities',
            False, 
            [
            _MetaInfoClassMember('inform-user-community', REFERENCE_LIST, 'InformUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity', 
                [], [], 
                '''                Unencrpted Community name associated with a
                inform host
                ''',
                'inform_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities',
            False, 
            [
            _MetaInfoClassMember('inform-encrypted-user-community', REFERENCE_LIST, 'InformEncryptedUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity', 
                [], [], 
                '''                Clear/Encrypt Community name associated with
                a inform host
                ''',
                'inform_encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost',
            False, 
            [
            _MetaInfoClassMember('inform-encrypted-user-communities', REFERENCE_CLASS, 'InformEncryptedUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities', 
                [], [], 
                '''                Container class for defining Clear/encrypt
                communities for a inform host
                ''',
                'inform_encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-user-communities', REFERENCE_CLASS, 'InformUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities', 
                [], [], 
                '''                Container class for defining communities for
                a inform host
                ''',
                'inform_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v1/v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities',
            False, 
            [
            _MetaInfoClassMember('default-user-community', REFERENCE_LIST, 'DefaultUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity', 
                [], [], 
                '''                Unencrpted Community name associated with a
                trap host
                ''',
                'default_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts.TrapHost' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts.TrapHost',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of SNMP notification host
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('default-user-communities', REFERENCE_CLASS, 'DefaultUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities', 
                [], [], 
                '''                Container class for defining communities for a
                trap host
                ''',
                'default_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('encrypted-user-communities', REFERENCE_CLASS, 'EncryptedUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities', 
                [], [], 
                '''                Container class for defining Clear/encrypt
                communities for a trap host
                ''',
                'encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-host', REFERENCE_CLASS, 'InformHost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost', 
                [], [], 
                '''                Container class for defining notification type
                for a Inform host
                ''',
                'inform_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.TrapHosts' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.TrapHosts',
            False, 
            [
            _MetaInfoClassMember('trap-host', REFERENCE_LIST, 'TrapHost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts.TrapHost', 
                [], [], 
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.Contexts.Context' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.Contexts.Context',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Context Name
                ''',
                'context_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.Contexts' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.Contexts',
            False, 
            [
            _MetaInfoClassMember('context', REFERENCE_LIST, 'Context' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.Contexts.Context', 
                [], [], 
                '''                Context Name
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'contexts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.ContextMappings.ContextMapping' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.ContextMappings.ContextMapping',
            False, 
            [
            _MetaInfoClassMember('context-mapping-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Context mapping name
                ''',
                'context_mapping_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', REFERENCE_ENUM_CLASS, 'SnmpContextEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpContextEnum', 
                [], [], 
                '''                SNMP context feature type
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF protocol instance
                ''',
                'instance_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Topology name associated with the context
                ''',
                'topology_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name associated with the context
                ''',
                'vrf_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf.ContextMappings' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf.ContextMappings',
            False, 
            [
            _MetaInfoClassMember('context-mapping', REFERENCE_LIST, 'ContextMapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.ContextMappings.ContextMapping', 
                [], [], 
                '''                Context mapping name
                ''',
                'context_mapping',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                VRF name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context-mappings', REFERENCE_CLASS, 'ContextMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.ContextMappings', 
                [], [], 
                '''                List of context names
                ''',
                'context_mappings',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('contexts', REFERENCE_CLASS, 'Contexts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.Contexts', 
                [], [], 
                '''                List of Context Names
                ''',
                'contexts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-hosts', REFERENCE_CLASS, 'TrapHosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf.TrapHosts', 
                [], [], 
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Vrfs' : {
        'meta_info' : _MetaInfoClass('Snmp.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs.Vrf', 
                [], [], 
                '''                VRF name
                ''',
                'vrf',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Snmp.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                Name of the group
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Context name
                ''',
                'context_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('notify-view', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                notify view name
                ''',
                'notify_view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('read-view', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                read view name
                ''',
                'read_view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-model', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                security model like auth/noAuth/Priv
                applicable for v3
                ''',
                'security_model',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('snmp-version', REFERENCE_ENUM_CLASS, 'GroupSnmpVersionEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'GroupSnmpVersionEnum', 
                [], [], 
                '''                snmp version
                ''',
                'snmp_version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv4 Access-list name
                ''',
                'v4_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v4acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v4acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6-access-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ipv6 Access-list name
                ''',
                'v6_access_list',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('v6acl-type', REFERENCE_ENUM_CLASS, 'SnmpaclEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpaclEnum', 
                [], [], 
                '''                Access-list type
                ''',
                'v6acl_type',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('write-view', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                write view name
                ''',
                'write_view',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Groups' : {
        'meta_info' : _MetaInfoClass('Snmp.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Groups.Group', 
                [], [], 
                '''                Name of the group
                ''',
                'group',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v1/v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.EncryptedUserCommunities',
            False, 
            [
            _MetaInfoClassMember('encrypted-user-community', REFERENCE_LIST, 'EncryptedUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity', 
                [], [], 
                '''                Clear/Encrypt Community name associated with
                a trap host
                ''',
                'encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'encrypted-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities',
            False, 
            [
            _MetaInfoClassMember('inform-user-community', REFERENCE_LIST, 'InformUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity', 
                [], [], 
                '''                Unencrpted Community name associated with a
                inform host
                ''',
                'inform_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMPv2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set
                as 0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this
                value to an integer corresponding to the
                trapBGP 8192, CONFIG 4096,SYSLOG 131072
                ,SNMP_TRAP 1COPY_COMPLETE_TRAP 64To provide
                a combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities',
            False, 
            [
            _MetaInfoClassMember('inform-encrypted-user-community', REFERENCE_LIST, 'InformEncryptedUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity', 
                [], [], 
                '''                Clear/Encrypt Community name associated with
                a inform host
                ''',
                'inform_encrypted_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-encrypted-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.InformHost' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.InformHost',
            False, 
            [
            _MetaInfoClassMember('inform-encrypted-user-communities', REFERENCE_CLASS, 'InformEncryptedUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities', 
                [], [], 
                '''                Container class for defining Clear/encrypt
                communities for a inform host
                ''',
                'inform_encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-user-communities', REFERENCE_CLASS, 'InformUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities', 
                [], [], 
                '''                Container class for defining communities for
                a inform host
                ''',
                'inform_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'inform-host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity',
            False, 
            [
            _MetaInfoClassMember('community-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 128)], [], 
                '''                SNMPv1/v2c community string or SNMPv3 user
                ''',
                'community_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('advanced-trap-types1', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setUse this for providing
                copy-complete trapValue must be set to 0 if
                not used
                ''',
                'advanced_trap_types1',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('advanced-trap-types2', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setvalue should always to set as
                0
                ''',
                'advanced_trap_types2',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('basic-trap-types', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Number to signify the feature traps that
                needs to be setBasicTrapTypes is used for
                all traps except copy-completeSet this value
                to an integer corresponding to the trapBGP
                8192, CONFIG 4096,SYSLOG 131072,SNMP_TRAP
                1COPY_COMPLETE_TRAP 64To provide a
                combination of trap Add the respective
                numbersValue must be set to 0 for all traps
                ''',
                'basic_trap_types',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                UDP port number
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('security-level', REFERENCE_ENUM_CLASS, 'SnmpSecurityModelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpSecurityModelEnum', 
                [], [], 
                '''                Security level to be used noauth/auth/priv
                ''',
                'security_level',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP Version to be used v1/v2c/v3
                ''',
                'version',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-community',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost.DefaultUserCommunities' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost.DefaultUserCommunities',
            False, 
            [
            _MetaInfoClassMember('default-user-community', REFERENCE_LIST, 'DefaultUserCommunity' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity', 
                [], [], 
                '''                Unencrpted Community name associated with a
                trap host
                ''',
                'default_user_community',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'default-user-communities',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts.TrapHost' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts.TrapHost',
            False, 
            [
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP address of SNMP notification host
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-cfg', True, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP address of SNMP notification host
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-snmp-agent-cfg', True),
                ]),
            _MetaInfoClassMember('default-user-communities', REFERENCE_CLASS, 'DefaultUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.DefaultUserCommunities', 
                [], [], 
                '''                Container class for defining communities for a
                trap host
                ''',
                'default_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('encrypted-user-communities', REFERENCE_CLASS, 'EncryptedUserCommunities' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.EncryptedUserCommunities', 
                [], [], 
                '''                Container class for defining Clear/encrypt
                communities for a trap host
                ''',
                'encrypted_user_communities',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-host', REFERENCE_CLASS, 'InformHost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost.InformHost', 
                [], [], 
                '''                Container class for defining notification type
                for a Inform host
                ''',
                'inform_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.TrapHosts' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapHosts',
            False, 
            [
            _MetaInfoClassMember('trap-host', REFERENCE_LIST, 'TrapHost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts.TrapHost', 
                [], [], 
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_host',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'trap-hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Contexts.Context' : {
        'meta_info' : _MetaInfoClass('Snmp.Contexts.Context',
            False, 
            [
            _MetaInfoClassMember('context-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Context Name
                ''',
                'context_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.Contexts' : {
        'meta_info' : _MetaInfoClass('Snmp.Contexts',
            False, 
            [
            _MetaInfoClassMember('context', REFERENCE_LIST, 'Context' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Contexts.Context', 
                [], [], 
                '''                Context Name
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'contexts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.ContextMappings.ContextMapping' : {
        'meta_info' : _MetaInfoClass('Snmp.ContextMappings.ContextMapping',
            False, 
            [
            _MetaInfoClassMember('context-mapping-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Context mapping name
                ''',
                'context_mapping_name',
                'Cisco-IOS-XR-snmp-agent-cfg', True),
            _MetaInfoClassMember('context', REFERENCE_ENUM_CLASS, 'SnmpContextEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'SnmpContextEnum', 
                [], [], 
                '''                SNMP context feature type
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OSPF protocol instance
                ''',
                'instance_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('topology-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Topology name associated with the context
                ''',
                'topology_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name associated with the context
                ''',
                'vrf_name',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp.ContextMappings' : {
        'meta_info' : _MetaInfoClass('Snmp.ContextMappings',
            False, 
            [
            _MetaInfoClassMember('context-mapping', REFERENCE_LIST, 'ContextMapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.ContextMappings.ContextMapping', 
                [], [], 
                '''                Context mapping name
                ''',
                'context_mapping',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'context-mappings',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Snmp' : {
        'meta_info' : _MetaInfoClass('Snmp',
            False, 
            [
            _MetaInfoClassMember('administration', REFERENCE_CLASS, 'Administration' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Administration', 
                [], [], 
                '''                Container class for SNMP administration
                ''',
                'administration',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('agent', REFERENCE_CLASS, 'Agent' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Agent', 
                [], [], 
                '''                The heirarchy point for SNMP Agent
                configurations
                ''',
                'agent',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('bulk-stats', REFERENCE_CLASS, 'BulkStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.BulkStats', 
                [], [], 
                '''                SNMP bulk stats configuration commands
                ''',
                'bulk_stats',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('context-mappings', REFERENCE_CLASS, 'ContextMappings' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.ContextMappings', 
                [], [], 
                '''                List of context names
                ''',
                'context_mappings',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('contexts', REFERENCE_CLASS, 'Contexts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Contexts', 
                [], [], 
                '''                List of Context Names
                ''',
                'contexts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('correlator', REFERENCE_CLASS, 'Correlator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Correlator', 
                [], [], 
                '''                Configure properties of the trap correlator
                ''',
                'correlator',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('default-community-maps', REFERENCE_CLASS, 'DefaultCommunityMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.DefaultCommunityMaps', 
                [], [], 
                '''                Container class to hold unencrpted community map
                ''',
                'default_community_maps',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('encrypted-community-maps', REFERENCE_CLASS, 'EncryptedCommunityMaps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.EncryptedCommunityMaps', 
                [], [], 
                '''                Container class to hold clear/encrypted
                communitie maps
                ''',
                'encrypted_community_maps',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Groups', 
                [], [], 
                '''                Define a User Security Model group
                ''',
                'groups',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-pending', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max nmber of informs to hold in queue, (default
                25)
                ''',
                'inform_pending',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                Number of times to retry an Inform request
                (default 3)
                ''',
                'inform_retries',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('inform-timeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '42949671')], [], 
                '''                Timeout value in seconds for Inform request
                (default 15 sec)
                ''',
                'inform_timeout',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv4', 
                [], [], 
                '''                SNMP TOS bit for outgoing packets
                ''',
                'ipv4',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Ipv6', 
                [], [], 
                '''                SNMP TOS bit for outgoing packets
                ''',
                'ipv6',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('logging', REFERENCE_CLASS, 'Logging' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Logging', 
                [], [], 
                '''                SNMP logging
                ''',
                'logging',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('notification', REFERENCE_CLASS, 'Notification' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Notification', 
                [], [], 
                '''                Enable SNMP notifications
                ''',
                'notification',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('oid-poll-stats', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable Poll OID statistics
                ''',
                'oid_poll_stats',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('overload-control', REFERENCE_CLASS, 'OverloadControl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.OverloadControl', 
                [], [], 
                '''                Set overload control params for handling
                incoming messages
                ''',
                'overload_control',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('484', '65500')], [], 
                '''                Largest SNMP packet size
                ''',
                'packet_size',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('system', REFERENCE_CLASS, 'System' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.System', 
                [], [], 
                '''                container to hold system information
                ''',
                'system',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Target', 
                [], [], 
                '''                SNMP target configurations
                ''',
                'target',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('throttle-time', ATTRIBUTE, 'int' , None, None, 
                [('50', '1000')], [], 
                '''                Throttle time for incoming queue (default 0
                msec)
                ''',
                'throttle_time',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('timeouts', REFERENCE_CLASS, 'Timeouts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Timeouts', 
                [], [], 
                '''                SNMP timeouts
                ''',
                'timeouts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap', REFERENCE_CLASS, 'Trap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Trap', 
                [], [], 
                '''                Class to hold trap configurations
                ''',
                'trap',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-hosts', REFERENCE_CLASS, 'TrapHosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.TrapHosts', 
                [], [], 
                '''                Specify hosts to receive SNMP notifications
                ''',
                'trap_hosts',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-port', ATTRIBUTE, 'int' , None, None, 
                [('1024', '65535')], [], 
                '''                Change the source port of all traps
                ''',
                'trap_port',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-source', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Assign an interface for the source address of
                all traps
                ''',
                'trap_source',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-source-ipv4', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Assign an interface for the source address of
                all traps
                ''',
                'trap_source_ipv4',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('trap-source-ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Assign an interface for the source IPV6 address
                of all traps
                ''',
                'trap_source_ipv6',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('users', REFERENCE_CLASS, 'Users' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Users', 
                [], [], 
                '''                Define a user who can access the SNMP engine
                ''',
                'users',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('views', REFERENCE_CLASS, 'Views' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Views', 
                [], [], 
                '''                Class to configure a SNMPv2 MIB view
                ''',
                'views',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrf-authentication-trap-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable authentication traps for packets on a
                vrf
                ''',
                'vrf_authentication_trap_disable',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Snmp.Vrfs', 
                [], [], 
                '''                SNMP VRF configuration commands
                ''',
                'vrfs',
                'Cisco-IOS-XR-snmp-agent-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'snmp',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.MplsTeMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsTeMib',
            False, 
            [
            _MetaInfoClassMember('cache-garbage-collect-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600')], [], 
                '''                Configure the cache garbage collector time for
                the mib.
                ''',
                'cache_garbage_collect_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.MplsP2MpMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsP2MpMib',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-p2mp-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.MplsTeExtStdMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsTeExtStdMib',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-ext-std-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.MplsTeExtMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsTeExtMib',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-te-ext-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.MplsFrrMib' : {
        'meta_info' : _MetaInfoClass('Mib.MplsFrrMib',
            False, 
            [
            _MetaInfoClassMember('cache-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '600')], [], 
                '''                Configure the cache time for the mib.
                ''',
                'cache_timer',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-te-cfg',
            'mpls-frr-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-te-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.CbQosmib.Cache' : {
        'meta_info' : _MetaInfoClass('Mib.CbQosmib.Cache',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable CBQoSMIB statistics data caching
                ''',
                'enable',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('refresh-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '60')], [], 
                '''                Cache refresh time in seconds
                ''',
                'refresh_time',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('service-policy-count', ATTRIBUTE, 'int' , None, None, 
                [('1', '5000')], [], 
                '''                Maximum number of service policies to cache
                the statistics for
                ''',
                'service_policy_count',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-qos-mibs-cfg',
            'cache',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-mibs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.CbQosmib' : {
        'meta_info' : _MetaInfoClass('Mib.CbQosmib',
            False, 
            [
            _MetaInfoClassMember('cache', REFERENCE_CLASS, 'Cache' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.CbQosmib.Cache', 
                [], [], 
                '''                CBQoSMIB statistics data caching
                ''',
                'cache',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('member-interface-stats', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable bundle member interface statistics
                retrieval.
                ''',
                'member_interface_stats',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('persist', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Persist CBQoSMIB config, service-policy and
                object indices
                ''',
                'persist',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            ],
            'Cisco-IOS-XR-qos-mibs-cfg',
            'cb-qosmib',
            _yang_ns._namespaces['Cisco-IOS-XR-qos-mibs-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.EntityMib' : {
        'meta_info' : _MetaInfoClass('Mib.EntityMib',
            False, 
            [
            _MetaInfoClassMember('entity-index-persistence', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable entPhysicalIndex persistence
                ''',
                'entity_index_persistence',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-entitymib-cfg',
            'entity-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-entitymib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.InterfaceMib.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-ifmib-cfg', True),
            _MetaInfoClassMember('index-persistence', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable index persistence
                ''',
                'index_persistence',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('link-up-down', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable LinkUpDown notification
                ''',
                'link_up_down',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.InterfaceMib.Interfaces' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Interfaces.Interface', 
                [], [], 
                '''                Interface to configure
                ''',
                'interface',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.InterfaceMib.Notification' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Notification',
            False, 
            [
            _MetaInfoClassMember('link-ietf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Set the varbind of linkupdown trap to the RFC
                specified varbinds (default cisco)
                ''',
                'link_ietf',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'notification',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.InterfaceMib.Subsets.Subset.LinkUpDown' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Subsets.Subset.LinkUpDown',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable linkupdown notification
                ''',
                'enable',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('regular-expression', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular expression to match ifName
                ''',
                'regular_expression',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'link-up-down',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.InterfaceMib.Subsets.Subset' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Subsets.Subset',
            False, 
            [
            _MetaInfoClassMember('subset-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The interface subset PriorityID
                ''',
                'subset_id',
                'Cisco-IOS-XR-snmp-ifmib-cfg', True),
            _MetaInfoClassMember('link-up-down', REFERENCE_CLASS, 'LinkUpDown' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Subsets.Subset.LinkUpDown', 
                [], [], 
                '''                SNMP linkUp and linkDown notifications
                ''',
                'link_up_down',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'subset',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.InterfaceMib.Subsets' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib.Subsets',
            False, 
            [
            _MetaInfoClassMember('subset', REFERENCE_LIST, 'Subset' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Subsets.Subset', 
                [], [], 
                '''                Subset priorityID to group ifNames based on
                Regular Expression
                ''',
                'subset',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'subsets',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib.InterfaceMib' : {
        'meta_info' : _MetaInfoClass('Mib.InterfaceMib',
            False, 
            [
            _MetaInfoClassMember('interface-alias-long', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable support for ifAlias values longer than
                64 characters
                ''',
                'interface_alias_long',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('interface-index-persistence', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ifindex persistence
                ''',
                'interface_index_persistence',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Interfaces', 
                [], [], 
                '''                Enter the SNMP interface configuration commands
                ''',
                'interfaces',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('internal-cache', ATTRIBUTE, 'int' , None, None, 
                [('0', '60')], [], 
                '''                Get cached interface statistics
                ''',
                'internal_cache',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('ip-subscriber', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable IP subscriber interfaces in IFMIB
                ''',
                'ip_subscriber',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('notification', REFERENCE_CLASS, 'Notification' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Notification', 
                [], [], 
                '''                MIB notification configuration
                ''',
                'notification',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('statistics-cache', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable cached interface statistics
                ''',
                'statistics_cache',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('subsets', REFERENCE_CLASS, 'Subsets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib.Subsets', 
                [], [], 
                '''                Add configuration for an interface subset
                ''',
                'subsets',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-cfg',
            'interface-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
    'Mib' : {
        'meta_info' : _MetaInfoClass('Mib',
            False, 
            [
            _MetaInfoClassMember('cb-qosmib', REFERENCE_CLASS, 'CbQosmib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.CbQosmib', 
                [], [], 
                '''                CBQoSMIB configuration
                ''',
                'cb_qosmib',
                'Cisco-IOS-XR-qos-mibs-cfg', False),
            _MetaInfoClassMember('entity-mib', REFERENCE_CLASS, 'EntityMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.EntityMib', 
                [], [], 
                '''                Entity MIB
                ''',
                'entity_mib',
                'Cisco-IOS-XR-snmp-entitymib-cfg', False),
            _MetaInfoClassMember('interface-mib', REFERENCE_CLASS, 'InterfaceMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.InterfaceMib', 
                [], [], 
                '''                Interface MIB configuration
                ''',
                'interface_mib',
                'Cisco-IOS-XR-snmp-ifmib-cfg', False),
            _MetaInfoClassMember('mpls-frr-mib', REFERENCE_CLASS, 'MplsFrrMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsFrrMib', 
                [], [], 
                '''                FRR MIB configuration
                ''',
                'mpls_frr_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-p2mp-mib', REFERENCE_CLASS, 'MplsP2MpMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsP2MpMib', 
                [], [], 
                '''                MPLS P2MP MIB configuration
                ''',
                'mpls_p2mp_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-te-ext-mib', REFERENCE_CLASS, 'MplsTeExtMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsTeExtMib', 
                [], [], 
                '''                MPLS TE EXT MIB configuration
                ''',
                'mpls_te_ext_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-te-ext-std-mib', REFERENCE_CLASS, 'MplsTeExtStdMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsTeExtStdMib', 
                [], [], 
                '''                MPLS TE EXT STD MIB configuration
                ''',
                'mpls_te_ext_std_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('mpls-te-mib', REFERENCE_CLASS, 'MplsTeMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg', 'Mib.MplsTeMib', 
                [], [], 
                '''                MPLS TE MIB configuration
                ''',
                'mpls_te_mib',
                'Cisco-IOS-XR-mpls-te-cfg', False),
            _MetaInfoClassMember('sensor-mib-cache', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Get cached Sesnsor MIB statistics
                ''',
                'sensor_mib_cache',
                'Cisco-IOS-XR-snmp-ciscosensormib-cfg', False),
            ],
            'Cisco-IOS-XR-snmp-agent-cfg',
            'mib',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_cfg'
        ),
    },
}
_meta_table['Snmp.EncryptedCommunityMaps.EncryptedCommunityMap']['meta_info'].parent =_meta_table['Snmp.EncryptedCommunityMaps']['meta_info']
_meta_table['Snmp.Views.View']['meta_info'].parent =_meta_table['Snmp.Views']['meta_info']
_meta_table['Snmp.Logging.Threshold']['meta_info'].parent =_meta_table['Snmp.Logging']['meta_info']
_meta_table['Snmp.Administration.DefaultCommunities.DefaultCommunity']['meta_info'].parent =_meta_table['Snmp.Administration.DefaultCommunities']['meta_info']
_meta_table['Snmp.Administration.EncryptedCommunities.EncryptedCommunity']['meta_info'].parent =_meta_table['Snmp.Administration.EncryptedCommunities']['meta_info']
_meta_table['Snmp.Administration.DefaultCommunities']['meta_info'].parent =_meta_table['Snmp.Administration']['meta_info']
_meta_table['Snmp.Administration.EncryptedCommunities']['meta_info'].parent =_meta_table['Snmp.Administration']['meta_info']
_meta_table['Snmp.Agent.EngineId.Remotes.Remote']['meta_info'].parent =_meta_table['Snmp.Agent.EngineId.Remotes']['meta_info']
_meta_table['Snmp.Agent.EngineId.Remotes']['meta_info'].parent =_meta_table['Snmp.Agent.EngineId']['meta_info']
_meta_table['Snmp.Agent.EngineId']['meta_info'].parent =_meta_table['Snmp.Agent']['meta_info']
_meta_table['Snmp.Ipv6.Tos']['meta_info'].parent =_meta_table['Snmp.Ipv6']['meta_info']
_meta_table['Snmp.Ipv4.Tos']['meta_info'].parent =_meta_table['Snmp.Ipv4']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.VrfNames.VrfName']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_.VrfNames']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.TargetAddresses.TargetAddress']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_.TargetAddresses']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.VrfNames']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_']['meta_info']
_meta_table['Snmp.Target.Targets.Target_.TargetAddresses']['meta_info'].parent =_meta_table['Snmp.Target.Targets.Target_']['meta_info']
_meta_table['Snmp.Target.Targets.Target_']['meta_info'].parent =_meta_table['Snmp.Target.Targets']['meta_info']
_meta_table['Snmp.Target.Targets']['meta_info'].parent =_meta_table['Snmp.Target']['meta_info']
_meta_table['Snmp.Notification.Bgp.Bgp4Mib']['meta_info'].parent =_meta_table['Snmp.Notification.Bgp']['meta_info']
_meta_table['Snmp.Notification.Bgp.CiscoBgp4Mib']['meta_info'].parent =_meta_table['Snmp.Notification.Bgp']['meta_info']
_meta_table['Snmp.Notification.Ospf.Lsa']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Ospf.StateChange']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Ospf.Retransmit']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Ospf.Error']['meta_info'].parent =_meta_table['Snmp.Notification.Ospf']['meta_info']
_meta_table['Snmp.Notification.Ospfv3.Error']['meta_info'].parent =_meta_table['Snmp.Notification.Ospfv3']['meta_info']
_meta_table['Snmp.Notification.Ospfv3.StateChange']['meta_info'].parent =_meta_table['Snmp.Notification.Ospfv3']['meta_info']
_meta_table['Snmp.Notification.MplsTe.CiscoExtension']['meta_info'].parent =_meta_table['Snmp.Notification.MplsTe']['meta_info']
_meta_table['Snmp.Notification.Snmp_']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Vpls']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.L2Vpn']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Isis']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.ConfigMan']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Cfm']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Oam']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Flash']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.EntityRedundancy']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.ConfigCopy']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.SelectiveVrfDownload']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.System']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Bfd']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Ntp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Rsvp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Bgp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Hsrp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Ospf']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Vrrp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Ospfv3']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsLdp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsTeP2Mp']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsTe']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsFrr']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.MplsL3Vpn']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Otn']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Sensor']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Entity']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.EntityState']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.FruControl']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Rf']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Notification.Syslog']['meta_info'].parent =_meta_table['Snmp.Notification']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind.Match']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds.VarBind']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause.VarBinds']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses.RootCause']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind.Match']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds.VarBind']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause.VarBinds']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses.NonRootCause']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.RootCauses']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful.NonRootCauses']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.NonStateful']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts.Host']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo.Hosts']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.NonStateful']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule.AppliedTo']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules.Rule']['meta_info']
_meta_table['Snmp.Correlator.Rules.Rule']['meta_info'].parent =_meta_table['Snmp.Correlator.Rules']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames.Rulename']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts.Host']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo.Hosts']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.Rulenames']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet.AppliedTo']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info']
_meta_table['Snmp.Correlator.RuleSets.RuleSet']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSets']['meta_info']
_meta_table['Snmp.Correlator.Rules']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.Correlator.RuleSets']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.BulkStats.Schemas.Schema.Instance']['meta_info'].parent =_meta_table['Snmp.BulkStats.Schemas.Schema']['meta_info']
_meta_table['Snmp.BulkStats.Schemas.Schema']['meta_info'].parent =_meta_table['Snmp.BulkStats.Schemas']['meta_info']
_meta_table['Snmp.BulkStats.Objects.Object.Objects_.Object_']['meta_info'].parent =_meta_table['Snmp.BulkStats.Objects.Object.Objects_']['meta_info']
_meta_table['Snmp.BulkStats.Objects.Object.Objects_']['meta_info'].parent =_meta_table['Snmp.BulkStats.Objects.Object']['meta_info']
_meta_table['Snmp.BulkStats.Objects.Object']['meta_info'].parent =_meta_table['Snmp.BulkStats.Objects']['meta_info']
_meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas.TransferSchema']['meta_info'].parent =_meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas']['meta_info']
_meta_table['Snmp.BulkStats.Transfers.Transfer.TransferSchemas']['meta_info'].parent =_meta_table['Snmp.BulkStats.Transfers.Transfer']['meta_info']
_meta_table['Snmp.BulkStats.Transfers.Transfer']['meta_info'].parent =_meta_table['Snmp.BulkStats.Transfers']['meta_info']
_meta_table['Snmp.BulkStats.Schemas']['meta_info'].parent =_meta_table['Snmp.BulkStats']['meta_info']
_meta_table['Snmp.BulkStats.Objects']['meta_info'].parent =_meta_table['Snmp.BulkStats']['meta_info']
_meta_table['Snmp.BulkStats.Transfers']['meta_info'].parent =_meta_table['Snmp.BulkStats']['meta_info']
_meta_table['Snmp.DefaultCommunityMaps.DefaultCommunityMap']['meta_info'].parent =_meta_table['Snmp.DefaultCommunityMaps']['meta_info']
_meta_table['Snmp.Users.User']['meta_info'].parent =_meta_table['Snmp.Users']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.InformHost']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts.TrapHost']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.TrapHosts']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.Contexts.Context']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.Contexts']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.ContextMappings.ContextMapping']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf.ContextMappings']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.TrapHosts']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.Contexts']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf']['meta_info']
_meta_table['Snmp.Vrfs.Vrf.ContextMappings']['meta_info'].parent =_meta_table['Snmp.Vrfs.Vrf']['meta_info']
_meta_table['Snmp.Vrfs.Vrf']['meta_info'].parent =_meta_table['Snmp.Vrfs']['meta_info']
_meta_table['Snmp.Groups.Group']['meta_info'].parent =_meta_table['Snmp.Groups']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities.EncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities.InformUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities.InformEncryptedUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost.InformEncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities.DefaultUserCommunity']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.EncryptedUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.InformHost']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost.DefaultUserCommunities']['meta_info'].parent =_meta_table['Snmp.TrapHosts.TrapHost']['meta_info']
_meta_table['Snmp.TrapHosts.TrapHost']['meta_info'].parent =_meta_table['Snmp.TrapHosts']['meta_info']
_meta_table['Snmp.Contexts.Context']['meta_info'].parent =_meta_table['Snmp.Contexts']['meta_info']
_meta_table['Snmp.ContextMappings.ContextMapping']['meta_info'].parent =_meta_table['Snmp.ContextMappings']['meta_info']
_meta_table['Snmp.EncryptedCommunityMaps']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Views']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Logging']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Administration']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Agent']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Trap']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Ipv6']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Ipv4']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.System']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Target']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Notification']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Correlator']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.BulkStats']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.DefaultCommunityMaps']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.OverloadControl']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Timeouts']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Users']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Vrfs']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Groups']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.TrapHosts']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Contexts']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.ContextMappings']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Mib.CbQosmib.Cache']['meta_info'].parent =_meta_table['Mib.CbQosmib']['meta_info']
_meta_table['Mib.InterfaceMib.Interfaces.Interface']['meta_info'].parent =_meta_table['Mib.InterfaceMib.Interfaces']['meta_info']
_meta_table['Mib.InterfaceMib.Subsets.Subset.LinkUpDown']['meta_info'].parent =_meta_table['Mib.InterfaceMib.Subsets.Subset']['meta_info']
_meta_table['Mib.InterfaceMib.Subsets.Subset']['meta_info'].parent =_meta_table['Mib.InterfaceMib.Subsets']['meta_info']
_meta_table['Mib.InterfaceMib.Interfaces']['meta_info'].parent =_meta_table['Mib.InterfaceMib']['meta_info']
_meta_table['Mib.InterfaceMib.Notification']['meta_info'].parent =_meta_table['Mib.InterfaceMib']['meta_info']
_meta_table['Mib.InterfaceMib.Subsets']['meta_info'].parent =_meta_table['Mib.InterfaceMib']['meta_info']
_meta_table['Mib.MplsTeMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsP2MpMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsTeExtStdMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsTeExtMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.MplsFrrMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.CbQosmib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.EntityMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
_meta_table['Mib.InterfaceMib']['meta_info'].parent =_meta_table['Mib']['meta_info']
