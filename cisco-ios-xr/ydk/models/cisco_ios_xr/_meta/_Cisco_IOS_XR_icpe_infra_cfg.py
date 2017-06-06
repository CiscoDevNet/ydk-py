


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NvSatelliteGlobal.ChassisMac' : {
        'meta_info' : _MetaInfoClass('NvSatelliteGlobal.ChassisMac',
            False, 
            [
            _MetaInfoClassMember('mac1', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                First two bytes of MAC address
                ''',
                'mac1',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('mac2', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Second two bytes of MAC address
                ''',
                'mac2',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('mac3', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Third two bytes of MAC address
                ''',
                'mac3',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'chassis-mac',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatelliteGlobal' : {
        'meta_info' : _MetaInfoClass('NvSatelliteGlobal',
            False, 
            [
            _MetaInfoClassMember('chassis-mac', REFERENCE_CLASS, 'ChassisMac' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatelliteGlobal.ChassisMac', 
                [], [], 
                '''                Chassis MAC address
                ''',
                'chassis_mac',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite-global',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatellites.NvSatellite.UpgradeOnConnect' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.UpgradeOnConnect',
            False, 
            [
            _MetaInfoClassMember('connect-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When to upgrade the satellite
                ''',
                'connect_type',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference name
                ''',
                'reference',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'upgrade-on-connect',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort',
            False, 
            [
            _MetaInfoClassMember('port-type', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Port type
                ''',
                'port_type',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [('0', '8')], [], 
                '''                Slot
                ''',
                'slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('sub-slot', ATTRIBUTE, 'int' , None, None, 
                [('0', '8')], [], 
                '''                Sub slot
                ''',
                'sub_slot',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('port-range', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Port range
                ''',
                'port_range',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'candidate-fabric-port',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatellites.NvSatellite.CandidateFabricPorts' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.CandidateFabricPorts',
            False, 
            [
            _MetaInfoClassMember('candidate-fabric-port', REFERENCE_LIST, 'CandidateFabricPort' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort', 
                [], [], 
                '''                Enable interfaces on the satellite to be used
                as fabric ports
                ''',
                'candidate_fabric_port',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'candidate-fabric-ports',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatellites.NvSatellite.ConnectionInfo' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.ConnectionInfo',
            False, 
            [
            _MetaInfoClassMember('password', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encrypted password for the user
                ''',
                'password',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite Username
                ''',
                'username',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'connection-info',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatellites.NvSatellite.Redundancy' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite.Redundancy',
            False, 
            [
            _MetaInfoClassMember('host-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority for this host for the given satellite
                ''',
                'host_priority',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'redundancy',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatellites.NvSatellite' : {
        'meta_info' : _MetaInfoClass('NvSatellites.NvSatellite',
            False, 
            [
            _MetaInfoClassMember('satellite-id', ATTRIBUTE, 'int' , None, None, 
                [('100', '65534')], [], 
                '''                Satellite ID
                ''',
                'satellite_id',
                'Cisco-IOS-XR-icpe-infra-cfg', True),
            _MetaInfoClassMember('candidate-fabric-ports', REFERENCE_CLASS, 'CandidateFabricPorts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.CandidateFabricPorts', 
                [], [], 
                '''                Enable interfaces on the satellite to be used
                as fabric ports table
                ''',
                'candidate_fabric_ports',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('connection-info', REFERENCE_CLASS, 'ConnectionInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.ConnectionInfo', 
                [], [], 
                '''                Satellite User
                ''',
                'connection_info',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('delayed-switchback', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Timer (in seconds) for delaying switchback in a
                dual home setup
                ''',
                'delayed_switchback',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite Description
                ''',
                'description',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('device-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite Name
                ''',
                'device_name',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('disc-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discovery timeout for the satellite
                ''',
                'disc_timeout',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable
                ''',
                'enable',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Satellite IP Address
                ''',
                'ip_address',
                'Cisco-IOS-XR-icpe-infra-cfg', False, [
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Satellite IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-icpe-infra-cfg', False),
                    _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Satellite IP Address
                        ''',
                        'ip_address',
                        'Cisco-IOS-XR-icpe-infra-cfg', False),
                ]),
            _MetaInfoClassMember('redundancy', REFERENCE_CLASS, 'Redundancy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.Redundancy', 
                [], [], 
                '''                Redundancy submode
                ''',
                'redundancy',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('secret', ATTRIBUTE, 'str' , None, None, 
                [], [b'(!.+)|([^!].+)'], 
                '''                Encrypted password for the Satellite
                ''',
                'secret',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite Serial Number
                ''',
                'serial_number',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('timeout-warning', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Discovery timeout warning for the satellite
                ''',
                'timeout_warning',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Satellite Type
                ''',
                'type',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('upgrade-on-connect', REFERENCE_CLASS, 'UpgradeOnConnect' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite.UpgradeOnConnect', 
                [], [], 
                '''                Satellite auto-upgrade capability
                ''',
                'upgrade_on_connect',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            _MetaInfoClassMember('vrf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF for Satellite IP Address
                ''',
                'vrf',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellite',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
    'NvSatellites' : {
        'meta_info' : _MetaInfoClass('NvSatellites',
            False, 
            [
            _MetaInfoClassMember('nv-satellite', REFERENCE_LIST, 'NvSatellite' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg', 'NvSatellites.NvSatellite', 
                [], [], 
                '''                Satellite Configuration
                ''',
                'nv_satellite',
                'Cisco-IOS-XR-icpe-infra-cfg', False),
            ],
            'Cisco-IOS-XR-icpe-infra-cfg',
            'nv-satellites',
            _yang_ns._namespaces['Cisco-IOS-XR-icpe-infra-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_icpe_infra_cfg'
        ),
    },
}
_meta_table['NvSatelliteGlobal.ChassisMac']['meta_info'].parent =_meta_table['NvSatelliteGlobal']['meta_info']
_meta_table['NvSatellites.NvSatellite.CandidateFabricPorts.CandidateFabricPort']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite.CandidateFabricPorts']['meta_info']
_meta_table['NvSatellites.NvSatellite.UpgradeOnConnect']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite.CandidateFabricPorts']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite.ConnectionInfo']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite.Redundancy']['meta_info'].parent =_meta_table['NvSatellites.NvSatellite']['meta_info']
_meta_table['NvSatellites.NvSatellite']['meta_info'].parent =_meta_table['NvSatellites']['meta_info']
