


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ospfv3FastRerouteTiebreakersEnum' : _MetaInfoEnum('Ospfv3FastRerouteTiebreakersEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'downstream':'downstream',
            'line-card-disjoint':'line_card_disjoint',
            'lowest-metric':'lowest_metric',
            'node-protect':'node_protect',
            'primary-path':'primary_path',
            'secondary-path':'secondary_path',
            'srlg-disjoint':'srlg_disjoint',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3AuthenticationEnum' : _MetaInfoEnum('Ospfv3AuthenticationEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'md5':'md5',
            'sha1':'sha1',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3InternalRouteEnum' : _MetaInfoEnum('Ospfv3InternalRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'internal':'internal',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3NssaExternalRouteEnum' : _MetaInfoEnum('Ospfv3NssaExternalRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'external1':'external1',
            'external2':'external2',
            'external':'external',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3SubsequentAddressFamilyEnum' : _MetaInfoEnum('Ospfv3SubsequentAddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'unicast':'unicast',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3EigrpRouteEnum' : _MetaInfoEnum('Ospfv3EigrpRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'internal':'internal',
            'external':'external',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'TraceBufSizeEnum' : _MetaInfoEnum('TraceBufSizeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'disable':'disable',
            'one':'one',
            'two':'two',
            'three':'three',
            'four':'four',
            'five':'five',
            'six':'six',
            'seven':'seven',
            'eight':'eight',
            'nine':'nine',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3NsrEnum' : _MetaInfoEnum('Ospfv3NsrEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'true':'true',
            'false':'false',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3ProtocolEnum' : _MetaInfoEnum('Ospfv3ProtocolEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'all':'all',
            'connected':'connected',
            'static':'static',
            'bgp':'bgp',
            'isis':'isis',
            'ospfv3':'ospfv3',
            'eigrp':'eigrp',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3BfdEnableModeEnum' : _MetaInfoEnum('Ospfv3BfdEnableModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'disable':'disable',
            'default':'default',
            'strict':'strict',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3AddressFamilyEnum' : _MetaInfoEnum('Ospfv3AddressFamilyEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'ipv6':'ipv6',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3EncryptionAlgorithmEnum' : _MetaInfoEnum('Ospfv3EncryptionAlgorithmEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'null':'null',
            'des':'des',
            '3des':'Y_3des',
            'aes':'aes',
            'aes192':'aes192',
            'aes256':'aes256',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3NetworkEnum' : _MetaInfoEnum('Ospfv3NetworkEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'broadcast':'broadcast',
            'non-broadcast':'non_broadcast',
            'point-to-point':'point_to_point',
            'point-to-multipoint':'point_to_multipoint',
            'non-broadcast-point-to-multipoint':'non_broadcast_point_to_multipoint',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3ExternalRouteEnum' : _MetaInfoEnum('Ospfv3ExternalRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'external1':'external1',
            'external2':'external2',
            'external':'external',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3ProtocolType2Enum' : _MetaInfoEnum('Ospfv3ProtocolType2Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'connected':'connected',
            'static':'static',
            'bgp':'bgp',
            'isis':'isis',
            'ospfv3':'ospfv3',
            'eigrp':'eigrp',
            'subscriber':'subscriber',
            'application':'application',
            'mobile':'mobile',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3MetricEnum' : _MetaInfoEnum('Ospfv3MetricEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'type1':'type1',
            'type2':'type2',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3FastRerouteEnum' : _MetaInfoEnum('Ospfv3FastRerouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'none':'none',
            'per-link':'per_link',
            'per-prefix':'per_prefix',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3DomainIdEnum' : _MetaInfoEnum('Ospfv3DomainIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'type0005':'type0005',
            'type0105':'type0105',
            'type0205':'type0205',
            'type8005':'type8005',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3LogAdjEnum' : _MetaInfoEnum('Ospfv3LogAdjEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'suppress':'suppress',
            'brief':'brief',
            'detail':'detail',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3IsisRouteEnum' : _MetaInfoEnum('Ospfv3IsisRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'level1':'level1',
            'level2':'level2',
            'level1-and2':'level1_and2',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3AuthenticationType2Enum' : _MetaInfoEnum('Ospfv3AuthenticationType2Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'null':'null',
            'md5':'md5',
            'sha1':'sha1',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3FastReroutePriorityEnum' : _MetaInfoEnum('Ospfv3FastReroutePriorityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg',
        {
            'critical':'critical',
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'Cisco-IOS-XR-ipv6-ospfv3-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg']),
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges.Range' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges.Range',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix format
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPV6 prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Specified metric for this range
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise address range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges',
            False, 
            [
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges.Range', 
                [], [], 
                '''                Summarize inter-area routes matching
                prefix/length
                ''',
                'range',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6 prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IPV6 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                OSPFv3 cost for point-to-multipoint
                neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPFv3 LSA during synchronization
                and flooding for point-to-multipoint
                neighbor
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                OSPFv3 dead-router polling interval (in
                seconds)
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                OSPFv3 priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor', 
                [], [], 
                '''                IPv6 address
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6
                prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 interface
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD
                packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors', 
                [], [], 
                '''                Specify a neighbor router
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an
                interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface', 
                [], [], 
                '''                OSPFv3 interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope',
            False, 
            [
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable sham link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks',
            False, 
            [
            _MetaInfoClassMember('sham-link', REFERENCE_LIST, 'ShamLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink', 
                [], [], 
                '''                ShamLink local and remote endpoints
                ''',
                'sham_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink',
            False, 
            [
            _MetaInfoClassMember('virtual-link-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled virtual link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks',
            False, 
            [
            _MetaInfoClassMember('virtual-link', REFERENCE_LIST, 'VirtualLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink', 
                [], [], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID if in IP address format
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope', 
                [], [], 
                '''                Area Scope Configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 area
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces', 
                [], [], 
                '''                OSPFv3 interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area.  Allowed only in
                non-backbone areas
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ranges', REFERENCE_CLASS, 'Ranges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges', 
                [], [], 
                '''                Range configuration
                ''',
                'ranges',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('sham-links', REFERENCE_CLASS, 'ShamLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks', 
                [], [], 
                '''                Sham Link sub-mode
                ''',
                'sham_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify area as a stub area.  Allowed only in
                non-backbone areas
                ''',
                'stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-links', REFERENCE_CLASS, 'VirtualLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks', 
                [], [], 
                '''                Virtual link sub-mode
                ''',
                'virtual_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges.Range' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges.Range',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix format
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPV6 prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Specified metric for this range
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise address range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges',
            False, 
            [
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges.Range', 
                [], [], 
                '''                Summarize inter-area routes matching
                prefix/length
                ''',
                'range',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6 prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IPV6 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                OSPFv3 cost for point-to-multipoint
                neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPFv3 LSA during synchronization
                and flooding for point-to-multipoint
                neighbor
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                OSPFv3 dead-router polling interval (in
                seconds)
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                OSPFv3 priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor', 
                [], [], 
                '''                IPv6 address
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6
                prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 interface
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD
                packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors', 
                [], [], 
                '''                Specify a neighbor router
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an
                interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface', 
                [], [], 
                '''                OSPFv3 interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope',
            False, 
            [
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable sham link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks',
            False, 
            [
            _MetaInfoClassMember('sham-link', REFERENCE_LIST, 'ShamLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink', 
                [], [], 
                '''                ShamLink local and remote endpoints
                ''',
                'sham_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink',
            False, 
            [
            _MetaInfoClassMember('virtual-link-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled virtual link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks',
            False, 
            [
            _MetaInfoClassMember('virtual-link', REFERENCE_LIST, 'VirtualLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink', 
                [], [], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId',
            False, 
            [
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Area ID if in integer format
                ''',
                'area_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope', 
                [], [], 
                '''                Area Scope Configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 area
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces', 
                [], [], 
                '''                OSPFv3 interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area.  Allowed only in
                non-backbone areas
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ranges', REFERENCE_CLASS, 'Ranges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges', 
                [], [], 
                '''                Range configuration
                ''',
                'ranges',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('sham-links', REFERENCE_CLASS, 'ShamLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks', 
                [], [], 
                '''                Sham Link sub-mode
                ''',
                'sham_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify area as a stub area.  Allowed only in
                non-backbone areas
                ''',
                'stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-links', REFERENCE_CLASS, 'VirtualLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks', 
                [], [], 
                '''                Virtual link sub-mode
                ''',
                'virtual_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-area-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AreaAddresses',
            False, 
            [
            _MetaInfoClassMember('area-address', REFERENCE_LIST, 'AreaAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('area-area-id', REFERENCE_LIST, 'AreaAreaId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_area_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Timers.Pacing' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Timers.Pacing',
            False, 
            [
            _MetaInfoClassMember('flood', ATTRIBUTE, 'int' , None, None, 
                [('5', '100')], [], 
                '''                The minimum interval in milliseconds to pace
                limit flooding on interface
                ''',
                'flood',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('lsa-group', ATTRIBUTE, 'int' , None, None, 
                [('10', '1800')], [], 
                '''                Interval in seconds at which LSAs are grouped
                and refreshed, checksummed, or aged
                ''',
                'lsa_group',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmission', ATTRIBUTE, 'int' , None, None, 
                [('5', '100')], [], 
                '''                The minimum interval in msec between neighbor
                retransmissions
                ''',
                'retransmission',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'pacing',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Timers.LsaTimers' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Timers.LsaTimers',
            False, 
            [
            _MetaInfoClassMember('arrival', ATTRIBUTE, 'int' , None, None, 
                [('0', '60000')], [], 
                '''                The minimum interval in milliseconds between
                accepting the same LSA
                ''',
                'arrival',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'lsa-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Lsa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Lsa',
            False, 
            [
            _MetaInfoClassMember('first-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '600000')], [], 
                '''                Delay to generate first occurrence of LSA in
                milliseconds
                ''',
                'first_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('maximum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Maximum delay between originating the same
                LSA in milliseconds
                ''',
                'maximum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('minimum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Minimum delay between originating the same
                LSA in milliseconds
                ''',
                'minimum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Spf' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Spf',
            False, 
            [
            _MetaInfoClassMember('first-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Initial delay between receiving a change and
                starting SPF in ms
                ''',
                'first_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('maximum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Maximum wait time between consecutive SPF
                calculations in ms
                ''',
                'maximum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('minimum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Minimum hold time between consecutive SPF
                calculations in ms
                ''',
                'minimum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'spf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle',
            False, 
            [
            _MetaInfoClassMember('lsa', REFERENCE_CLASS, 'Lsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Lsa', 
                [], [], 
                '''                LSA throttle timers for all types of OSPF LSAs
                ''',
                'lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spf', REFERENCE_CLASS, 'Spf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Spf', 
                [], [], 
                '''                SPF throttle timers
                ''',
                'spf',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Timers' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Timers',
            False, 
            [
            _MetaInfoClassMember('lsa-timers', REFERENCE_CLASS, 'LsaTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Timers.LsaTimers', 
                [], [], 
                '''                LSA timers
                ''',
                'lsa_timers',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('pacing', REFERENCE_CLASS, 'Pacing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Timers.Pacing', 
                [], [], 
                '''                Pacing timers
                ''',
                'pacing',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle', 
                [], [], 
                '''                Throttle timers
                ''',
                'throttle',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IPv6 prefix string format
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPV6 prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress routes matching prefix/length
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tag
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'summary-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes',
            False, 
            [
            _MetaInfoClassMember('summary-prefix', REFERENCE_LIST, 'SummaryPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefix', 
                [], [], 
                '''                IPv6 address
                ''',
                'summary_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'summary-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Snmp.TrapRateLimit' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Snmp.TrapRateLimit',
            False, 
            [
            _MetaInfoClassMember('max-window-traps', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Max number of traps sent in window time
                ''',
                'max_window_traps',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('2', '60')], [], 
                '''                Trap rate limit sliding window size
                ''',
                'window_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'trap-rate-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Snmp' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Snmp',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP context configuration
                ''',
                'context',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('trap-rate-limit', REFERENCE_CLASS, 'TrapRateLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Snmp.TrapRateLimit', 
                [], [], 
                '''                SNMP trap rate configuration
                ''',
                'trap_rate_limit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'snmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'Ospfv3FastReroutePriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker',
            False, 
            [
            _MetaInfoClassMember('tiebreaker-type', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteTiebreakersEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteTiebreakersEnum', 
                [], [], 
                '''                Tiebreaker type
                ''',
                'tiebreaker_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('tiebreaker-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Index value for a tiebreaker
                ''',
                'tiebreaker_index',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers',
            False, 
            [
            _MetaInfoClassMember('tiebreaker', REFERENCE_LIST, 'Tiebreaker' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker', 
                [], [], 
                '''                Fast-reroute tiebreakers configuration
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('load-sharing-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable load sharing between multiple backups
                ''',
                'load_sharing_disable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'Ospfv3FastReroutePriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tiebreakers', REFERENCE_CLASS, 'Tiebreakers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers', 
                [], [], 
                '''                Fast-reroute tiebreakers configurations
                ''',
                'tiebreakers',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.FastReroute',
            False, 
            [
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link global configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix global configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Distance.Ospfv3_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Distance.Ospfv3_',
            False, 
            [
            _MetaInfoClassMember('external', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for external type 5 and type 7 routes
                ''',
                'external',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('inter-area', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for inter-area routes
                ''',
                'inter_area',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('intra-area', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for intra-area routes
                ''',
                'intra_area',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ospfv3',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Distance' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Distance',
            False, 
            [
            _MetaInfoClassMember('administrative', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Define an administrative distance
                ''',
                'administrative',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ospfv3', REFERENCE_CLASS, 'Ospfv3_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Distance.Ospfv3_', 
                [], [], 
                '''                OSPFv3 administrative distance
                ''',
                'ospfv3',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Maximum.RedistributedPrefixes' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Maximum.RedistributedPrefixes',
            False, 
            [
            _MetaInfoClassMember('prefixes', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum number of prefixes redistributed to
                protocol
                ''',
                'prefixes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only give warning message when limit is
                exceeded
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'redistributed-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Maximum' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Maximum',
            False, 
            [
            _MetaInfoClassMember('interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Specify maximum number of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('paths', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Specify maximum number of paths per route
                ''',
                'paths',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistributed-prefixes', REFERENCE_CLASS, 'RedistributedPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Maximum.RedistributedPrefixes', 
                [], [], 
                '''                Limit number of redistributed prefixes
                ''',
                'redistributed_prefixes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'connected-or-static-or-subscriber-or-mobile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Bgp' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Bgp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                first half (X)
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                second half (Y), or 2-byte AS number, or
                4-byte AS number in asplain format
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                ISIS process name if protocol is ISIS, or
                OSPFv3 process name if protocol is OSPFv3
                ''',
                'process_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ospfv3-or-isis-or-application',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Eigrp' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                first half (X)
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'Ospfv3ProtocolType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ProtocolType2Enum', 
                [], [], 
                '''                Protocol
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Bgp', 
                [], [], 
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('connected-or-static-or-subscriber-or-mobile', REFERENCE_CLASS, 'ConnectedOrStaticOrSubscriberOrMobile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile', 
                [], [], 
                '''                connected or static or subscriber or mobile
                ''',
                'connected_or_static_or_subscriber_or_mobile',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Eigrp', 
                [], [], 
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ospfv3-or-isis-or-application', REFERENCE_LIST, 'Ospfv3OrIsisOrApplication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication', 
                [], [], 
                '''                ospfv3 or isis or application
                ''',
                'ospfv3_or_isis_or_application',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Redistributes' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Redistributes',
            False, 
            [
            _MetaInfoClassMember('redistribute', REFERENCE_LIST, 'Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistribute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'redistributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Ignore.Lsa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Ignore.Lsa',
            False, 
            [
            _MetaInfoClassMember('mospf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ignore of MOSPF type 6 LSA
                ''',
                'mospf',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Ignore' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Ignore',
            False, 
            [
            _MetaInfoClassMember('lsa', REFERENCE_CLASS, 'Lsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Ignore.Lsa', 
                [], [], 
                '''                Do not complain upon receiving LSA of the
                specified type
                ''',
                'lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ignore',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName',
            False, 
            [
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                second half (Y), or 2-byte AS number, or
                4-byte AS number in asplain format
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                first half (X)
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                If ISIS or OSPFv3, specify the instance name
                ''',
                'process_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix-list name
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'as-yy-and-as-xx-and-process-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'Ospfv3ProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ProtocolEnum', 
                [], [], 
                '''                none
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('as-yy-and-as-xx-and-process-name', REFERENCE_LIST, 'AsYyAndAsXxAndProcessName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName', 
                [], [], 
                '''                keys: as-yy, as-xx, process-name
                ''',
                'as_yy_and_as_xx_and_process_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts',
            False, 
            [
            _MetaInfoClassMember('distribute-out', REFERENCE_LIST, 'DistributeOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut', 
                [], [], 
                '''                Filter generated type-5 LSAs
                ''',
                'distribute_out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-outs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DistributeListOut',
            False, 
            [
            _MetaInfoClassMember('distribute-outs', REFERENCE_CLASS, 'DistributeOuts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts', 
                [], [], 
                '''                Filter generated type-5 LSAs
                ''',
                'distribute_outs',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6 prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit.OnStartup' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit.OnStartup',
            False, 
            [
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait until BGP converges (only applicable to
                default VRF)
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'wait_time',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Unconditionally enter stub router operational
                state
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled stub router configuration mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise external LSAs with modified metric in
                stub router mode
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise stub links with maximum metric in stub
                router mode
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-migration', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_migration',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-restart', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-startup', REFERENCE_CLASS, 'OnStartup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit.OnStartup', 
                [], [], 
                '''                Enter stub router operational state on startup
                ''',
                'on_startup',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-switchover', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_switchover',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise summary LSAs with modified metric in
                stub router mode
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'rbit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit.OnStartup' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit.OnStartup',
            False, 
            [
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait until BGP converges (only applicable to
                default VRF)
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'wait_time',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Unconditionally enter stub router operational
                state
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled stub router configuration mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise external LSAs with modified metric in
                stub router mode
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise stub links with maximum metric in stub
                router mode
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-migration', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_migration',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-restart', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-startup', REFERENCE_CLASS, 'OnStartup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit.OnStartup', 
                [], [], 
                '''                Enter stub router operational state on startup
                ''',
                'on_startup',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-switchover', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_switchover',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise summary LSAs with modified metric in
                stub router mode
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'v6bit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric.OnStartup' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric.OnStartup',
            False, 
            [
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait until BGP converges (only applicable to
                default VRF)
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'wait_time',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Unconditionally enter stub router operational
                state
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled stub router configuration mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise external LSAs with modified metric in
                stub router mode
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise stub links with maximum metric in stub
                router mode
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-migration', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_migration',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-restart', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-startup', REFERENCE_CLASS, 'OnStartup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric.OnStartup', 
                [], [], 
                '''                Enter stub router operational state on startup
                ''',
                'on_startup',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-switchover', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_switchover',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise summary LSAs with modified metric in
                stub router mode
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'max-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.StubRouter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.StubRouter',
            False, 
            [
            _MetaInfoClassMember('max-metric', REFERENCE_CLASS, 'MaxMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric', 
                [], [], 
                '''                Stub router max-metric configuration
                ''',
                'max_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('rbit', REFERENCE_CLASS, 'Rbit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit', 
                [], [], 
                '''                Stub router R-bit configuration
                ''',
                'rbit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('v6bit', REFERENCE_CLASS, 'V6Bit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit', 
                [], [], 
                '''                Stub router V6-bit configuration
                ''',
                'v6bit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'stub-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable out
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable graceful restart
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('helper', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable router's helper support
                ''',
                'helper',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('90', '3600')], [], 
                '''                Minimum interval between graceful restarts
                (seconds)
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('90', '1800')], [], 
                '''                Maximum route lifetime following restart
                (seconds)
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('strict-lsa-checking', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Terminate graceful restart helper mode if LSA
                changed
                ''',
                'strict_lsa_checking',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DefaultInformation.Originate' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DefaultInformation.Originate',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Always advertise default route
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                OSPFv3 metric type for default routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to default-information
                origination
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for default route
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('originate', REFERENCE_CLASS, 'Originate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DefaultInformation.Originate', 
                [], [], 
                '''                Distribute a default route
                ''',
                'originate',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.ProcessScope' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.ProcessScope',
            False, 
            [
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'process-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf.AutoCost' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf.AutoCost',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify 'true' to assign cost based on
                interface type
                ''',
                'disable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('reference-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967')], [], 
                '''                Specify reference bandwidth for cost
                computations in terms of Mbits per second
                ''',
                'reference_bandwidth',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'auto-cost',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.DefaultVrf' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.DefaultVrf',
            False, 
            [
            _MetaInfoClassMember('area-addresses', REFERENCE_CLASS, 'AreaAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AreaAddresses', 
                [], [], 
                '''                Area configuration
                ''',
                'area_addresses',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('auto-cost', REFERENCE_CLASS, 'AutoCost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.AutoCost', 
                [], [], 
                '''                Calculate interface cost according to bandwidth
                ''',
                'auto_cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared dead
                (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DefaultInformation', 
                [], [], 
                '''                Control distribution of default information
                ''',
                'default_information',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Set metric of redistributed routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distance', REFERENCE_CLASS, 'Distance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Distance', 
                [], [], 
                '''                Define an administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list-out', REFERENCE_CLASS, 'DistributeListOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.DistributeListOut', 
                [], [], 
                '''                Filter prefixes from RIB 
                ''',
                'distribute_list_out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.FastReroute', 
                [], [], 
                '''                Fast-reroute instance scoped parameters
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.GracefulRestart', 
                [], [], 
                '''                Graceful restart configuration
                ''',
                'graceful_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ignore', REFERENCE_CLASS, 'Ignore' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Ignore', 
                [], [], 
                '''                Do not complain about a specified event
                ''',
                'ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('log-adjacency-changes', REFERENCE_ENUM_CLASS, 'Ospfv3LogAdjEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3LogAdjEnum', 
                [], [], 
                '''                Log changes in adjacency state
                ''',
                'log_adjacency_changes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Maximum', 
                [], [], 
                '''                Set OSPFv3 limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('process-scope', REFERENCE_CLASS, 'ProcessScope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.ProcessScope', 
                [], [], 
                '''                Process scope configuration
                ''',
                'process_scope',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistributes', REFERENCE_CLASS, 'Redistributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Redistributes', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistributes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Specify the router ID for this OSPFv3 process in
                IPv4 address format
                ''',
                'router_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Snmp', 
                [], [], 
                '''                SNMP configuration
                ''',
                'snmp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spf-prefix-priority-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                SPF prefix prioritization disabled
                ''',
                'spf_prefix_priority_disable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spf-prefix-priority-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for SPF prefix prioritization
                ''',
                'spf_prefix_priority_policy',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('stub-router', REFERENCE_CLASS, 'StubRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.StubRouter', 
                [], [], 
                '''                Stub router configuration
                ''',
                'stub_router',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes', 
                [], [], 
                '''                Summarize redistributed routes matching
                prefix/length
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf.Timers', 
                [], [], 
                '''                Adjust routing timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'default-vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Capability' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Capability',
            False, 
            [
            _MetaInfoClassMember('vrf-lite', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable VRF Lite
                ''',
                'vrf_lite',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'capability',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId',
            False, 
            [
            _MetaInfoClassMember('domain-id-type', REFERENCE_ENUM_CLASS, 'Ospfv3DomainIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3DomainIdEnum', 
                [], [], 
                '''                Secondary domain ID type
                ''',
                'domain_id_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('domain-id-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Secondary domain ID value
                ''',
                'domain_id_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'secondary-domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds',
            False, 
            [
            _MetaInfoClassMember('secondary-domain-id', REFERENCE_LIST, 'SecondaryDomainId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId', 
                [], [], 
                '''                OSPF Secondary domain ID
                ''',
                'secondary_domain_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'secondary-domain-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId',
            False, 
            [
            _MetaInfoClassMember('domain-id-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Primary domain ID value
                ''',
                'domain_id_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('domain-id-type', REFERENCE_ENUM_CLASS, 'Ospfv3DomainIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3DomainIdEnum', 
                [], [], 
                '''                Primary domain ID type
                ''',
                'domain_id_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'primary-domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DomainId',
            False, 
            [
            _MetaInfoClassMember('primary-domain-id', REFERENCE_CLASS, 'PrimaryDomainId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId', 
                [], [], 
                '''                OSPF Primary domain ID
                ''',
                'primary_domain_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('secondary-domain-ids', REFERENCE_CLASS, 'SecondaryDomainIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds', 
                [], [], 
                '''                Secondary domain ID Table
                ''',
                'secondary_domain_ids',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'domain-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges.Range' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges.Range',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix format
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPV6 prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Specified metric for this range
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise address range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges',
            False, 
            [
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges.Range', 
                [], [], 
                '''                Summarize inter-area routes matching
                prefix/length
                ''',
                'range',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6 prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IPV6 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                OSPFv3 cost for point-to-multipoint
                neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPFv3 LSA during synchronization
                and flooding for point-to-multipoint
                neighbor
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                OSPFv3 dead-router polling interval (in
                seconds)
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                OSPFv3 priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor', 
                [], [], 
                '''                IPv6 address
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6
                prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 interface
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD
                packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors', 
                [], [], 
                '''                Specify a neighbor router
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an
                interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface', 
                [], [], 
                '''                OSPFv3 interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope',
            False, 
            [
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable sham link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks',
            False, 
            [
            _MetaInfoClassMember('sham-link', REFERENCE_LIST, 'ShamLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink', 
                [], [], 
                '''                ShamLink local and remote endpoints
                ''',
                'sham_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink',
            False, 
            [
            _MetaInfoClassMember('virtual-link-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled virtual link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks',
            False, 
            [
            _MetaInfoClassMember('virtual-link', REFERENCE_LIST, 'VirtualLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink', 
                [], [], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID if in IP address format
                ''',
                'address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope', 
                [], [], 
                '''                Area Scope Configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 area
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces', 
                [], [], 
                '''                OSPFv3 interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area.  Allowed only in
                non-backbone areas
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ranges', REFERENCE_CLASS, 'Ranges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges', 
                [], [], 
                '''                Range configuration
                ''',
                'ranges',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('sham-links', REFERENCE_CLASS, 'ShamLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks', 
                [], [], 
                '''                Sham Link sub-mode
                ''',
                'sham_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify area as a stub area.  Allowed only in
                non-backbone areas
                ''',
                'stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-links', REFERENCE_CLASS, 'VirtualLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks', 
                [], [], 
                '''                Virtual link sub-mode
                ''',
                'virtual_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-address',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges.Range' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges.Range',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 prefix format
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPV6 prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Specified metric for this range
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not advertise address range
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'range',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges',
            False, 
            [
            _MetaInfoClassMember('range', REFERENCE_LIST, 'Range' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges.Range', 
                [], [], 
                '''                Summarize inter-area routes matching
                prefix/length
                ''',
                'range',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ranges',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa',
            False, 
            [
            _MetaInfoClassMember('default-info-originate', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Originate Type 7 default into NSSA area
                ''',
                'default_info_originate',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                Only valid with DefaultInfoOriginate
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-redistribution', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                No redistribution into this NSSA area
                ''',
                'no_redistribution',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('no-summary', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Do not send summary LSA into NSSA
                ''',
                'no_summary',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'nssa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6 prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor',
            False, 
            [
            _MetaInfoClassMember('neighbor-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IPV6 address
                ''',
                'neighbor_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                OSPFv3 cost for point-to-multipoint
                neighbor
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Filter OSPFv3 LSA during synchronization
                and flooding for point-to-multipoint
                neighbor
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('poll-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                OSPFv3 dead-router polling interval (in
                seconds)
                ''',
                'poll_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                OSPFv3 priority of non-broadcast neighbor
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('zone', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Zone
                ''',
                'zone',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbor',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors',
            False, 
            [
            _MetaInfoClassMember('neighbor', REFERENCE_LIST, 'Neighbor' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor', 
                [], [], 
                '''                IPv6 address
                ''',
                'neighbor',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'neighbors',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable database-filter
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6
                prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface to configure
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 interface
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD
                packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('neighbors', REFERENCE_CLASS, 'Neighbors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors', 
                [], [], 
                '''                Specify a neighbor router
                ''',
                'neighbors',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an
                interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface', 
                [], [], 
                '''                OSPFv3 interface
                ''',
                'interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope',
            False, 
            [
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink',
            False, 
            [
            _MetaInfoClassMember('source-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Local sham-link endpoint
                ''',
                'source_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('destination-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote sham-link endpoint
                ''',
                'destination_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable sham link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks',
            False, 
            [
            _MetaInfoClassMember('sham-link', REFERENCE_LIST, 'ShamLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink', 
                [], [], 
                '''                ShamLink local and remote endpoints
                ''',
                'sham_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'sham-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink',
            False, 
            [
            _MetaInfoClassMember('virtual-link-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled virtual link
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks',
            False, 
            [
            _MetaInfoClassMember('virtual-link', REFERENCE_LIST, 'VirtualLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink', 
                [], [], 
                '''                Router ID of virtual link neighbor
                ''',
                'virtual_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'virtual-links',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId',
            False, 
            [
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Area ID if in integer format
                ''',
                'area_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('area-scope', REFERENCE_CLASS, 'AreaScope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope', 
                [], [], 
                '''                Area Scope Configuration
                ''',
                'area_scope',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared
                dead (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                Set the summary default-cost of a NSSA/stub
                area
                ''',
                'default_cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 area
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces', 
                [], [], 
                '''                OSPFv3 interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ldp-sync', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable MPLS LDP sync
                ''',
                'ldp_sync',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa', REFERENCE_CLASS, 'Nssa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa', 
                [], [], 
                '''                Specify area as a NSSA area.  Allowed only in
                non-backbone areas
                ''',
                'nssa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ranges', REFERENCE_CLASS, 'Ranges' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges', 
                [], [], 
                '''                Range configuration
                ''',
                'ranges',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('sham-links', REFERENCE_CLASS, 'ShamLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks', 
                [], [], 
                '''                Sham Link sub-mode
                ''',
                'sham_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('stub', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specify area as a stub area.  Allowed only in
                non-backbone areas
                ''',
                'stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('virtual-links', REFERENCE_CLASS, 'VirtualLinks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks', 
                [], [], 
                '''                Virtual link sub-mode
                ''',
                'virtual_links',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-area-id',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses',
            False, 
            [
            _MetaInfoClassMember('area-address', REFERENCE_LIST, 'AreaAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_address',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('area-area-id', REFERENCE_LIST, 'AreaAreaId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId', 
                [], [], 
                '''                Configuration for a particular area
                ''',
                'area_area_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'area-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Pacing' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Pacing',
            False, 
            [
            _MetaInfoClassMember('flood', ATTRIBUTE, 'int' , None, None, 
                [('5', '100')], [], 
                '''                The minimum interval in milliseconds to pace
                limit flooding on interface
                ''',
                'flood',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('lsa-group', ATTRIBUTE, 'int' , None, None, 
                [('10', '1800')], [], 
                '''                Interval in seconds at which LSAs are grouped
                and refreshed, checksummed, or aged
                ''',
                'lsa_group',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmission', ATTRIBUTE, 'int' , None, None, 
                [('5', '100')], [], 
                '''                The minimum interval in msec between neighbor
                retransmissions
                ''',
                'retransmission',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'pacing',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.LsaTimers' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Timers.LsaTimers',
            False, 
            [
            _MetaInfoClassMember('arrival', ATTRIBUTE, 'int' , None, None, 
                [('0', '60000')], [], 
                '''                The minimum interval in milliseconds between
                accepting the same LSA
                ''',
                'arrival',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'lsa-timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Lsa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Lsa',
            False, 
            [
            _MetaInfoClassMember('first-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '600000')], [], 
                '''                Delay to generate first occurrence of LSA in
                milliseconds
                ''',
                'first_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('maximum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Maximum delay between originating the same
                LSA in milliseconds
                ''',
                'maximum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('minimum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Minimum delay between originating the same
                LSA in milliseconds
                ''',
                'minimum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Spf' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Spf',
            False, 
            [
            _MetaInfoClassMember('first-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Initial delay between receiving a change and
                starting SPF in ms
                ''',
                'first_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('maximum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Maximum wait time between consecutive SPF
                calculations in ms
                ''',
                'maximum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('minimum-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '600000')], [], 
                '''                Minimum hold time between consecutive SPF
                calculations in ms
                ''',
                'minimum_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'spf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle',
            False, 
            [
            _MetaInfoClassMember('lsa', REFERENCE_CLASS, 'Lsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Lsa', 
                [], [], 
                '''                LSA throttle timers for all types of OSPF LSAs
                ''',
                'lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spf', REFERENCE_CLASS, 'Spf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Spf', 
                [], [], 
                '''                SPF throttle timers
                ''',
                'spf',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'throttle',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Timers' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Timers',
            False, 
            [
            _MetaInfoClassMember('lsa-timers', REFERENCE_CLASS, 'LsaTimers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.LsaTimers', 
                [], [], 
                '''                LSA timers
                ''',
                'lsa_timers',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('pacing', REFERENCE_CLASS, 'Pacing' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Pacing', 
                [], [], 
                '''                Pacing timers
                ''',
                'pacing',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('throttle', REFERENCE_CLASS, 'Throttle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle', 
                [], [], 
                '''                Throttle timers
                ''',
                'throttle',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'timers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefix',
            False, 
            [
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                IPv6 prefix string format
                ''',
                'prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-length', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                IPV6 prefix length
                ''',
                'prefix_length',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('not-advertise', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Suppress routes matching prefix/length
                ''',
                'not_advertise',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Tag
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'summary-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes',
            False, 
            [
            _MetaInfoClassMember('summary-prefix', REFERENCE_LIST, 'SummaryPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefix', 
                [], [], 
                '''                IPv6 address
                ''',
                'summary_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'summary-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Snmp.TrapRateLimit' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Snmp.TrapRateLimit',
            False, 
            [
            _MetaInfoClassMember('max-window-traps', ATTRIBUTE, 'int' , None, None, 
                [('0', '300')], [], 
                '''                Max number of traps sent in window time
                ''',
                'max_window_traps',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('window-size', ATTRIBUTE, 'int' , None, None, 
                [('2', '60')], [], 
                '''                Trap rate limit sliding window size
                ''',
                'window_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'trap-rate-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Snmp' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Snmp',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMP context configuration
                ''',
                'context',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('trap-rate-limit', REFERENCE_CLASS, 'TrapRateLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Snmp.TrapRateLimit', 
                [], [], 
                '''                SNMP trap rate configuration
                ''',
                'trap_rate_limit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'snmp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'Ospfv3FastReroutePriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker',
            False, 
            [
            _MetaInfoClassMember('tiebreaker-type', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteTiebreakersEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteTiebreakersEnum', 
                [], [], 
                '''                Tiebreaker type
                ''',
                'tiebreaker_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('tiebreaker-index', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Index value for a tiebreaker
                ''',
                'tiebreaker_index',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'tiebreaker',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers',
            False, 
            [
            _MetaInfoClassMember('tiebreaker', REFERENCE_LIST, 'Tiebreaker' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker', 
                [], [], 
                '''                Fast-reroute tiebreakers configuration
                ''',
                'tiebreaker',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'tiebreakers',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('load-sharing-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable load sharing between multiple backups
                ''',
                'load_sharing_disable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'Ospfv3FastReroutePriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastReroutePriorityEnum', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix priority-limit
                command
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tiebreakers', REFERENCE_CLASS, 'Tiebreakers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers', 
                [], [], 
                '''                Fast-reroute tiebreakers configurations
                ''',
                'tiebreakers',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute',
            False, 
            [
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link global configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-prefix global configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Distance.Ospfv3_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Distance.Ospfv3_',
            False, 
            [
            _MetaInfoClassMember('external', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for external type 5 and type 7 routes
                ''',
                'external',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('inter-area', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for inter-area routes
                ''',
                'inter_area',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('intra-area', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Distance for intra-area routes
                ''',
                'intra_area',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ospfv3',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Distance' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Distance',
            False, 
            [
            _MetaInfoClassMember('administrative', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Define an administrative distance
                ''',
                'administrative',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ospfv3', REFERENCE_CLASS, 'Ospfv3_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Distance.Ospfv3_', 
                [], [], 
                '''                OSPFv3 administrative distance
                ''',
                'ospfv3',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distance',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Maximum.RedistributedPrefixes' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Maximum.RedistributedPrefixes',
            False, 
            [
            _MetaInfoClassMember('prefixes', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Maximum number of prefixes redistributed to
                protocol
                ''',
                'prefixes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '100')], [], 
                '''                Threshold value (%) at which to generate a
                warning message
                ''',
                'threshold',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('warning-only', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Only give warning message when limit is
                exceeded
                ''',
                'warning_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'redistributed-prefixes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Maximum' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Maximum',
            False, 
            [
            _MetaInfoClassMember('interfaces', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Specify maximum number of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('paths', ATTRIBUTE, 'int' , None, None, 
                [('1', '64')], [], 
                '''                Specify maximum number of paths per route
                ''',
                'paths',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistributed-prefixes', REFERENCE_CLASS, 'RedistributedPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Maximum.RedistributedPrefixes', 
                [], [], 
                '''                Limit number of redistributed prefixes
                ''',
                'redistributed_prefixes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'maximum',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile',
            False, 
            [
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'connected-or-static-or-subscriber-or-mobile',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Bgp' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Bgp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                first half (X)
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                second half (Y), or 2-byte AS number, or
                4-byte AS number in asplain format
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bgp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                ISIS process name if protocol is ISIS, or
                OSPFv3 process name if protocol is OSPFv3
                ''',
                'process_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ospfv3-or-isis-or-application',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Eigrp' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Eigrp',
            False, 
            [
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                first half (X)
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3EigrpRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EigrpRouteEnum', 
                [], [], 
                '''                EIGRP route type
                ''',
                'eigrp_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3ExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 external routes
                ''',
                'external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('internal-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3InternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3InternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 routes
                ''',
                'internal_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('isis-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3IsisRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3IsisRouteEnum', 
                [], [], 
                '''                ISIS route type
                ''',
                'isis_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', REFERENCE_ENUM_CLASS, 'Ospfv3MetricEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3MetricEnum', 
                [], [], 
                '''                OSPFv3 exterior metric type for redistributed
                routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nssa-external-route-type', REFERENCE_ENUM_CLASS, 'Ospfv3NssaExternalRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NssaExternalRouteEnum', 
                [], [], 
                '''                Redistribute OSPFv3 NSSA external routes
                ''',
                'nssa_external_route_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve (Multi-Exit Discriminator) of BGP
                routes
                ''',
                'preserve_med',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('preserve-med-info', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Preserve Information (Multi-Exit
                Discriminator) of BGP routes
                ''',
                'preserve_med_info',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistribute-route', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Redistribution of OSPFv3 routes
                ''',
                'redistribute_route',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to redistribution
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for routes redistributed into OSPFv3
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'eigrp',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'Ospfv3ProtocolType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ProtocolType2Enum', 
                [], [], 
                '''                Protocol
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('bgp', REFERENCE_LIST, 'Bgp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Bgp', 
                [], [], 
                '''                bgp
                ''',
                'bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('connected-or-static-or-subscriber-or-mobile', REFERENCE_CLASS, 'ConnectedOrStaticOrSubscriberOrMobile' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile', 
                [], [], 
                '''                connected or static or subscriber or mobile
                ''',
                'connected_or_static_or_subscriber_or_mobile',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('eigrp', REFERENCE_LIST, 'Eigrp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Eigrp', 
                [], [], 
                '''                eigrp
                ''',
                'eigrp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ospfv3-or-isis-or-application', REFERENCE_LIST, 'Ospfv3OrIsisOrApplication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication', 
                [], [], 
                '''                ospfv3 or isis or application
                ''',
                'ospfv3_or_isis_or_application',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes',
            False, 
            [
            _MetaInfoClassMember('redistribute', REFERENCE_LIST, 'Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistribute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'redistributes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Ignore.Lsa' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Ignore.Lsa',
            False, 
            [
            _MetaInfoClassMember('mospf', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable ignore of MOSPF type 6 LSA
                ''',
                'mospf',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Ignore' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Ignore',
            False, 
            [
            _MetaInfoClassMember('lsa', REFERENCE_CLASS, 'Lsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Ignore.Lsa', 
                [], [], 
                '''                Do not complain upon receiving LSA of the
                specified type
                ''',
                'lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ignore',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName',
            False, 
            [
            _MetaInfoClassMember('as-yy', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                second half (Y), or 2-byte AS number, or
                4-byte AS number in asplain format
                ''',
                'as_yy',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('as-xx', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                4-byte AS number in asdot (X.Y) format -
                first half (X)
                ''',
                'as_xx',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                If ISIS or OSPFv3, specify the instance name
                ''',
                'process_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Prefix-list name
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'as-yy-and-as-xx-and-process-name',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut',
            False, 
            [
            _MetaInfoClassMember('protocol-name', REFERENCE_ENUM_CLASS, 'Ospfv3ProtocolEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3ProtocolEnum', 
                [], [], 
                '''                none
                ''',
                'protocol_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('as-yy-and-as-xx-and-process-name', REFERENCE_LIST, 'AsYyAndAsXxAndProcessName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName', 
                [], [], 
                '''                keys: as-yy, as-xx, process-name
                ''',
                'as_yy_and_as_xx_and_process_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts',
            False, 
            [
            _MetaInfoClassMember('distribute-out', REFERENCE_LIST, 'DistributeOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut', 
                [], [], 
                '''                Filter generated type-5 LSAs
                ''',
                'distribute_out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-outs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut',
            False, 
            [
            _MetaInfoClassMember('distribute-outs', REFERENCE_CLASS, 'DistributeOuts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts', 
                [], [], 
                '''                Filter generated type-5 LSAs
                ''',
                'distribute_outs',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list-out',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList.In_' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList.In_',
            False, 
            [
            _MetaInfoClassMember('prefix-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Filter prefixes based on an IPv6 prefix-list
                ''',
                'prefix_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'in',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList',
            False, 
            [
            _MetaInfoClassMember('in', REFERENCE_CLASS, 'In_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList.In_', 
                [], [], 
                '''                Filter prefixes installed to RIB
                ''',
                'in_',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'distribute-list',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit.OnStartup' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit.OnStartup',
            False, 
            [
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait until BGP converges (only applicable to
                default VRF)
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'wait_time',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Unconditionally enter stub router operational
                state
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled stub router configuration mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise external LSAs with modified metric in
                stub router mode
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise stub links with maximum metric in stub
                router mode
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-migration', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_migration',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-restart', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-startup', REFERENCE_CLASS, 'OnStartup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit.OnStartup', 
                [], [], 
                '''                Enter stub router operational state on startup
                ''',
                'on_startup',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-switchover', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_switchover',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise summary LSAs with modified metric in
                stub router mode
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'rbit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit.OnStartup' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit.OnStartup',
            False, 
            [
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait until BGP converges (only applicable to
                default VRF)
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'wait_time',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Unconditionally enter stub router operational
                state
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled stub router configuration mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise external LSAs with modified metric in
                stub router mode
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise stub links with maximum metric in stub
                router mode
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-migration', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_migration',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-restart', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-startup', REFERENCE_CLASS, 'OnStartup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit.OnStartup', 
                [], [], 
                '''                Enter stub router operational state on startup
                ''',
                'on_startup',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-switchover', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_switchover',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise summary LSAs with modified metric in
                stub router mode
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'v6bit',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric.OnStartup' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric.OnStartup',
            False, 
            [
            _MetaInfoClassMember('wait-for-bgp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Wait until BGP converges (only applicable to
                default VRF)
                ''',
                'wait_for_bgp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'wait_time',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'on-startup',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Unconditionally enter stub router operational
                state
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled stub router configuration mode
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('external-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise external LSAs with modified metric in
                stub router mode
                ''',
                'external_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('include-stub', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Advertise stub links with maximum metric in stub
                router mode
                ''',
                'include_stub',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-migration', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_migration',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-proc-restart', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_proc_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-startup', REFERENCE_CLASS, 'OnStartup' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric.OnStartup', 
                [], [], 
                '''                Enter stub router operational state on startup
                ''',
                'on_startup',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('on-switchover', ATTRIBUTE, 'int' , None, None, 
                [('5', '86400')], [], 
                '''                Time (in seconds) to stay in stub router
                operational state
                ''',
                'on_switchover',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-lsa', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Advertise summary LSAs with modified metric in
                stub router mode
                ''',
                'summary_lsa',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'max-metric',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter',
            False, 
            [
            _MetaInfoClassMember('max-metric', REFERENCE_CLASS, 'MaxMetric' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric', 
                [], [], 
                '''                Stub router max-metric configuration
                ''',
                'max_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('rbit', REFERENCE_CLASS, 'Rbit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit', 
                [], [], 
                '''                Stub router R-bit configuration
                ''',
                'rbit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('v6bit', REFERENCE_CLASS, 'V6Bit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit', 
                [], [], 
                '''                Stub router V6-bit configuration
                ''',
                'v6bit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'stub-router',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Bfd' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Bfd',
            False, 
            [
            _MetaInfoClassMember('detection-multiplier', ATTRIBUTE, 'int' , None, None, 
                [('2', '50')], [], 
                '''                Detect multiplier
                ''',
                'detection_multiplier',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-detect-mode', REFERENCE_ENUM_CLASS, 'Ospfv3BfdEnableModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3BfdEnableModeEnum', 
                [], [], 
                '''                Enable or disable BFD fast detection
                ''',
                'fast_detect_mode',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('3', '30000')], [], 
                '''                Hello interval in milli-seconds
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'bfd',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter.All' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter.All',
            False, 
            [
            _MetaInfoClassMember('out', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable out
                ''',
                'out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'all',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter',
            False, 
            [
            _MetaInfoClassMember('all', REFERENCE_CLASS, 'All' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter.All', 
                [], [], 
                '''                All
                ''',
                'all',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'database-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Authentication' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Authentication',
            False, 
            [
            _MetaInfoClassMember('algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationEnum', 
                [], [], 
                '''                Use the MD5 or SHA1 algorithm
                ''',
                'algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec AH authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'authentication',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.GracefulRestart' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.GracefulRestart',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable graceful restart
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('helper', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable router's helper support
                ''',
                'helper',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('interval', ATTRIBUTE, 'int' , None, None, 
                [('90', '3600')], [], 
                '''                Minimum interval between graceful restarts
                (seconds)
                ''',
                'interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('90', '1800')], [], 
                '''                Maximum route lifetime following restart
                (seconds)
                ''',
                'lifetime',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('strict-lsa-checking', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Terminate graceful restart helper mode if LSA
                changed
                ''',
                'strict_lsa_checking',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'graceful-restart',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation.Originate' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation.Originate',
            False, 
            [
            _MetaInfoClassMember('always', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Always advertise default route
                ''',
                'always',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777214')], [], 
                '''                OSPFv3 default metric
                ''',
                'metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('metric-type', ATTRIBUTE, 'int' , None, None, 
                [('1', '2')], [], 
                '''                OSPFv3 metric type for default routes
                ''',
                'metric_type',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('route-policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy to default-information
                origination
                ''',
                'route_policy_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Tag for default route
                ''',
                'tag',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'originate',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation',
            False, 
            [
            _MetaInfoClassMember('originate', REFERENCE_CLASS, 'Originate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation.Originate', 
                [], [], 
                '''                Distribute a default route
                ''',
                'originate',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'default-information',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-link',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces',
            False, 
            [
            _MetaInfoClassMember('candidate-interface', REFERENCE_LIST, 'CandidateInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface', 
                [], [], 
                '''                Candidate backup interface
                ''',
                'candidate_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'candidate-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces',
            False, 
            [
            _MetaInfoClassMember('exclude-interface', REFERENCE_LIST, 'ExcludeInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface', 
                [], [], 
                '''                Exclude an interface from becoming a backup
                ''',
                'exclude_interface',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'exclude-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix',
            False, 
            [
            _MetaInfoClassMember('candidate-interfaces', REFERENCE_CLASS, 'CandidateInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix candidate
                interface configuration
                ''',
                'candidate_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('exclude-interfaces', REFERENCE_CLASS, 'ExcludeInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces', 
                [], [], 
                '''                Fast-reroute per-link/per-prefix exclude
                interface configuration
                ''',
                'exclude_interfaces',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute-use-candidate-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use only interfaces on the candidate list as a
                backup path
                ''',
                'fast_reroute_use_candidate_only',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'per-prefix',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute',
            False, 
            [
            _MetaInfoClassMember('fast-reroute-enable', REFERENCE_ENUM_CLASS, 'Ospfv3FastRerouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3FastRerouteEnum', 
                [], [], 
                '''                Enable/Disable Fast-reroute per-link or
                per-prefix
                ''',
                'fast_reroute_enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-link', REFERENCE_CLASS, 'PerLink' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_link',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('per-prefix', REFERENCE_CLASS, 'PerPrefix' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix', 
                [], [], 
                '''                Fast-reroute per-link configuration
                ''',
                'per_prefix',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'fast-reroute',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope',
            False, 
            [
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute', 
                [], [], 
                '''                Fast-reroute configuration
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'process-scope',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.Encryption' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.Encryption',
            False, 
            [
            _MetaInfoClassMember('authentication-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3AuthenticationType2Enum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AuthenticationType2Enum', 
                [], [], 
                '''                Use the NULL, MD5 or SHA1 algorithm
                ''',
                'authentication_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Specify MD5 or SHA1 password
                ''',
                'authentication_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Authenticate packets
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-algorithm', REFERENCE_ENUM_CLASS, 'Ospfv3EncryptionAlgorithmEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3EncryptionAlgorithmEnum', 
                [], [], 
                '''                Specify the encryption algorithm
                ''',
                'encryption_algorithm',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption-password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encryption password
                ''',
                'encryption_password',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spi', ATTRIBUTE, 'int' , None, None, 
                [('256', '4294967295')], [], 
                '''                Use IPSec ESP authentication. Specify the
                Security Parameter Index (SPI) value
                ''',
                'spi',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'encryption',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf.AutoCost' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf.AutoCost',
            False, 
            [
            _MetaInfoClassMember('disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Specify 'true' to assign cost based on
                interface type
                ''',
                'disable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('reference-bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967')], [], 
                '''                Specify reference bandwidth for cost
                computations in terms of Mbits per second
                ''',
                'reference_bandwidth',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'auto-cost',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs.Vrf' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs.Vrf',
            False, 
            [
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name for this VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('area-addresses', REFERENCE_CLASS, 'AreaAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses', 
                [], [], 
                '''                Area configuration
                ''',
                'area_addresses',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('authentication', REFERENCE_CLASS, 'Authentication' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Authentication', 
                [], [], 
                '''                Authenticate OSPFv3 packets
                ''',
                'authentication',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('auto-cost', REFERENCE_CLASS, 'AutoCost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.AutoCost', 
                [], [], 
                '''                Calculate interface cost according to bandwidth
                ''',
                'auto_cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Bfd', 
                [], [], 
                '''                Configure BFD parameters
                ''',
                'bfd',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('capability', REFERENCE_CLASS, 'Capability' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Capability', 
                [], [], 
                '''                OSPFv3 Capability
                ''',
                'capability',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interface cost
                ''',
                'cost',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('database-filter', REFERENCE_CLASS, 'DatabaseFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter', 
                [], [], 
                '''                Database filter
                ''',
                'database_filter',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('dead-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Interval after which a neighbor is declared dead
                (in seconds)
                ''',
                'dead_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-information', REFERENCE_CLASS, 'DefaultInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation', 
                [], [], 
                '''                Control distribution of default information
                ''',
                'default_information',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-metric', ATTRIBUTE, 'int' , None, None, 
                [('1', '16777214')], [], 
                '''                Set metric of redistributed routes
                ''',
                'default_metric',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('demand-circuit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable demand circuit operation
                ''',
                'demand_circuit',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distance', REFERENCE_CLASS, 'Distance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Distance', 
                [], [], 
                '''                Define an administrative distance
                ''',
                'distance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list', REFERENCE_CLASS, 'DistributeList' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList', 
                [], [], 
                '''                Filter prefixes to/from RIB
                ''',
                'distribute_list',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('distribute-list-out', REFERENCE_CLASS, 'DistributeListOut' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut', 
                [], [], 
                '''                Filter prefixes from RIB 
                ''',
                'distribute_list_out',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('domain-id', REFERENCE_CLASS, 'DomainId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.DomainId', 
                [], [], 
                '''                OSPFv3 Domain ID
                ''',
                'domain_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 VRF configuration
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('encryption', REFERENCE_CLASS, 'Encryption' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Encryption', 
                [], [], 
                '''                Encrypt and authenticate OSPFv3 packets
                ''',
                'encryption',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('fast-reroute', REFERENCE_CLASS, 'FastReroute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute', 
                [], [], 
                '''                Fast-reroute instance scoped parameters
                ''',
                'fast_reroute',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('flood-reduction', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable flood reduction
                ''',
                'flood_reduction',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('graceful-restart', REFERENCE_CLASS, 'GracefulRestart' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.GracefulRestart', 
                [], [], 
                '''                Graceful restart configuration
                ''',
                'graceful_restart',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('hello-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Time between HELLO packets
                ''',
                'hello_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('ignore', REFERENCE_CLASS, 'Ignore' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Ignore', 
                [], [], 
                '''                Do not complain about a specified event
                ''',
                'ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Instance ID
                ''',
                'instance',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('log-adjacency-changes', REFERENCE_ENUM_CLASS, 'Ospfv3LogAdjEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3LogAdjEnum', 
                [], [], 
                '''                Log changes in adjacency state
                ''',
                'log_adjacency_changes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('maximum', REFERENCE_CLASS, 'Maximum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Maximum', 
                [], [], 
                '''                Set OSPFv3 limits
                ''',
                'maximum',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('mtu-ignore', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable ignoring of MTU in DBD packets
                ''',
                'mtu_ignore',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('network', REFERENCE_ENUM_CLASS, 'Ospfv3NetworkEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NetworkEnum', 
                [], [], 
                '''                Specify network type
                ''',
                'network',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('packet-size', ATTRIBUTE, 'int' , None, None, 
                [('256', '10000')], [], 
                '''                Limit size of OSPFv3 packets
                ''',
                'packet_size',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('passive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable routing updates on an interface
                ''',
                'passive',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('prefix-suppression', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable prefix suppression on an
                interface
                ''',
                'prefix_suppression',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Specify router priority
                ''',
                'priority',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('process-scope', REFERENCE_CLASS, 'ProcessScope' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope', 
                [], [], 
                '''                Process scope configuration
                ''',
                'process_scope',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('redistributes', REFERENCE_CLASS, 'Redistributes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes', 
                [], [], 
                '''                Redistribute information from another routing
                protocol
                ''',
                'redistributes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('retransmit-interval', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit interval in seconds
                ''',
                'retransmit_interval',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Specify the router ID for this OSPFv3 process in
                IPv4 address format
                ''',
                'router_id',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('snmp', REFERENCE_CLASS, 'Snmp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Snmp', 
                [], [], 
                '''                SNMP configuration
                ''',
                'snmp',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('snmpvrf-trap', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable SNMP trap configuration in a VRF
                ''',
                'snmpvrf_trap',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('spf-prefix-priority-policy', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route policy for SPF prefix prioritization
                ''',
                'spf_prefix_priority_policy',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('stub-router', REFERENCE_CLASS, 'StubRouter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter', 
                [], [], 
                '''                Stub router configuration
                ''',
                'stub_router',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('summary-prefixes', REFERENCE_CLASS, 'SummaryPrefixes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes', 
                [], [], 
                '''                Summarize redistributed routes matching
                prefix/length
                ''',
                'summary_prefixes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('timers', REFERENCE_CLASS, 'Timers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf.Timers', 
                [], [], 
                '''                Adjust routing timers
                ''',
                'timers',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('transmit-delay', ATTRIBUTE, 'int' , None, None, 
                [('1', '65535')], [], 
                '''                Specify the transmit delay in seconds
                ''',
                'transmit_delay',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Vrfs' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Vrfs',
            False, 
            [
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs.Vrf', 
                [], [], 
                '''                Configuration for a particular OSPF VRF
                ''',
                'vrf',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'vrfs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.Af' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.Af',
            False, 
            [
            _MetaInfoClassMember('af-name', REFERENCE_ENUM_CLASS, 'Ospfv3AddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3AddressFamilyEnum', 
                [], [], 
                '''                Address Family (AF) identifier
                ''',
                'af_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('saf-name', REFERENCE_ENUM_CLASS, 'Ospfv3SubsequentAddressFamilyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3SubsequentAddressFamilyEnum', 
                [], [], 
                '''                Subsequent Address Family (SAF) identifier
                ''',
                'saf_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'af',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.TraceBufs.TraceBuf' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.TraceBufs.TraceBuf',
            False, 
            [
            _MetaInfoClassMember('trace-buf-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Name for this VRF
                ''',
                'trace_buf_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('bufsize', REFERENCE_ENUM_CLASS, 'TraceBufSizeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'TraceBufSizeEnum', 
                [], [], 
                '''                Buffer size
                ''',
                'bufsize',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'trace-buf',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process.TraceBufs' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process.TraceBufs',
            False, 
            [
            _MetaInfoClassMember('trace-buf', REFERENCE_LIST, 'TraceBuf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.TraceBufs.TraceBuf', 
                [], [], 
                '''                Changes the size of the specified trace
                buffer
                ''',
                'trace_buf',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'trace-bufs',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes.Process' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes.Process',
            False, 
            [
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                OSPFv3 process name
                ''',
                'process_name',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', True),
            _MetaInfoClassMember('af', REFERENCE_CLASS, 'Af' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Af', 
                [], [], 
                '''                Address Family (AF)
                ''',
                'af',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('default-vrf', REFERENCE_CLASS, 'DefaultVrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.DefaultVrf', 
                [], [], 
                '''                Default VRF related configuration
                ''',
                'default_vrf',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3
                ''',
                'enable',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('nsr', REFERENCE_ENUM_CLASS, 'Ospfv3NsrEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3NsrEnum', 
                [], [], 
                '''                Enable non-stop routing
                ''',
                'nsr',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('protocol-shutdown', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable protocol shutdown
                ''',
                'protocol_shutdown',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('trace-bufs', REFERENCE_CLASS, 'TraceBufs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.TraceBufs', 
                [], [], 
                '''                Configuration to change size of trace buffer
                ''',
                'trace_bufs',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('vrfs', REFERENCE_CLASS, 'Vrfs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process.Vrfs', 
                [], [], 
                '''                VRF related configuration
                ''',
                'vrfs',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3.Processes' : {
        'meta_info' : _MetaInfoClass('Ospfv3.Processes',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes.Process', 
                [], [], 
                '''                An OSPFv3 process
                ''',
                'process',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'processes',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
    'Ospfv3' : {
        'meta_info' : _MetaInfoClass('Ospfv3',
            False, 
            [
            _MetaInfoClassMember('dns-name-lookup', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable OSPFv3 router IDs as DNS names
                ''',
                'dns_name_lookup',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            _MetaInfoClassMember('processes', REFERENCE_CLASS, 'Processes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg', 'Ospfv3.Processes', 
                [], [], 
                '''                OSPFv3 processes
                ''',
                'processes',
                'Cisco-IOS-XR-ipv6-ospfv3-cfg', False),
            ],
            'Cisco-IOS-XR-ipv6-ospfv3-cfg',
            'ospfv3',
            _yang_ns._namespaces['Cisco-IOS-XR-ipv6-ospfv3-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ipv6_ospfv3_cfg'
        ),
    },
}
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges.Range']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Ranges']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Nssa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.Interfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.AreaScope']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.ShamLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress.VirtualLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges.Range']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Ranges']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Nssa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.Interfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.ShamLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId.VirtualLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAddress']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses.AreaAreaId']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Lsa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle.Spf']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers.Pacing']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers.LsaTimers']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers.Throttle']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes.SummaryPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Snmp.TrapRateLimit']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Snmp']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix.Tiebreakers']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Distance.Ospfv3_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Distance']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Maximum.RedistributedPrefixes']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Maximum']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Bgp']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute.Eigrp']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes.Redistribute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Ignore.Lsa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.Ignore']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts.DistributeOut']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeListOut.DistributeOuts']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeListOut']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit.OnStartup']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit.OnStartup']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric.OnStartup']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.Rbit']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.V6Bit']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter.MaxMetric']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DefaultInformation.Originate']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.DefaultInformation']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AreaAddresses']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Timers']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.SummaryPrefixes']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Snmp']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Distance']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Maximum']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Redistributes']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Ignore']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeListOut']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.StubRouter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.GracefulRestart']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.DefaultInformation']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.ProcessScope']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf.AutoCost']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds.SecondaryDomainId']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.SecondaryDomainIds']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DomainId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DomainId.PrimaryDomainId']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DomainId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges.Range']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Neighbors']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces.Interface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks.ShamLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks.VirtualLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Ranges']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Nssa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.Interfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.AreaScope']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.ShamLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress.VirtualLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges.Range']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors.Neighbor']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Neighbors']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces.Interface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks.ShamLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks.VirtualLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Ranges']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Nssa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.Interfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.AreaScope']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.ShamLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId.VirtualLinks']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAddress']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses.AreaAreaId']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Lsa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle.Spf']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Pacing']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers.LsaTimers']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers.Throttle']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes.SummaryPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Snmp.TrapRateLimit']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Snmp']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers.Tiebreaker']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix.Tiebreakers']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Distance.Ospfv3_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Distance']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Maximum.RedistributedPrefixes']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Maximum']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.ConnectedOrStaticOrSubscriberOrMobile']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Bgp']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Ospfv3OrIsisOrApplication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute.Eigrp']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes.Redistribute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Ignore.Lsa']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Ignore']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut.AsYyAndAsXxAndProcessName']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts.DistributeOut']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut.DistributeOuts']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList.In_']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit.OnStartup']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit.OnStartup']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric.OnStartup']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.Rbit']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.V6Bit']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter.MaxMetric']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter.All']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation.Originate']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces.CandidateInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces.ExcludeInterface']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.CandidateInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix.ExcludeInterfaces']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerLink']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute.PerPrefix']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Capability']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DomainId']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AreaAddresses']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Timers']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.SummaryPrefixes']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Snmp']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.FastReroute']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Distance']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Maximum']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Redistributes']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Ignore']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeListOut']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DistributeList']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.StubRouter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Bfd']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DatabaseFilter']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Authentication']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.GracefulRestart']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.DefaultInformation']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.ProcessScope']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.Encryption']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf.AutoCost']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs.Vrf']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.Vrfs']['meta_info']
_meta_table['Ospfv3.Processes.Process.TraceBufs.TraceBuf']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process.TraceBufs']['meta_info']
_meta_table['Ospfv3.Processes.Process.DefaultVrf']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process']['meta_info']
_meta_table['Ospfv3.Processes.Process.Vrfs']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process']['meta_info']
_meta_table['Ospfv3.Processes.Process.Af']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process']['meta_info']
_meta_table['Ospfv3.Processes.Process.TraceBufs']['meta_info'].parent =_meta_table['Ospfv3.Processes.Process']['meta_info']
_meta_table['Ospfv3.Processes.Process']['meta_info'].parent =_meta_table['Ospfv3.Processes']['meta_info']
_meta_table['Ospfv3.Processes']['meta_info'].parent =_meta_table['Ospfv3']['meta_info']
