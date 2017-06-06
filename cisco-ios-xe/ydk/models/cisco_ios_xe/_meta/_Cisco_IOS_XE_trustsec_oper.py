


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CtsOdmBindingSourceEnum' : _MetaInfoEnum('CtsOdmBindingSourceEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper',
        {
            'default':'default',
            'from-vlan':'from_vlan',
            'from-cli':'from_cli',
            'from-l3if':'from_l3if',
            'from-cfp':'from_cfp',
            'from-ip-arp':'from_ip_arp',
            'from-local':'from_local',
            'from-sgt-caching':'from_sgt_caching',
            'from-cli-hi':'from_cli_hi',
        }, 'Cisco-IOS-XE-trustsec-oper', _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper']),
    'SxpConModeEnum' : _MetaInfoEnum('SxpConModeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper',
        {
            'con-mode-invalid':'con_mode_invalid',
            'con-mode-speaker':'con_mode_speaker',
            'con-mode-listener':'con_mode_listener',
            'con-mode-both':'con_mode_both',
        }, 'Cisco-IOS-XE-trustsec-oper', _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper']),
    'SxpConStateEnum' : _MetaInfoEnum('SxpConStateEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper',
        {
            'state-off':'state_off',
            'state-pending-on':'state_pending_on',
            'state-on':'state_on',
            'state-delete-hold-down':'state_delete_hold_down',
            'state-not-applicable':'state_not_applicable',
        }, 'Cisco-IOS-XE-trustsec-oper', _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper']),
    'TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap' : {
        'meta_info' : _MetaInfoClass('TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap',
            False, 
            [
            _MetaInfoClassMember('ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP-Prefix information to find its corresponding
                Secure Group Tag. Only IPv4 prefix information is 
                supported currently to get the Security Group Tag
                binding in this device.
                ''',
                'ip',
                'Cisco-IOS-XE-trustsec-oper', True, [
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        IP-Prefix information to find its corresponding
                        Secure Group Tag. Only IPv4 prefix information is 
                        supported currently to get the Security Group Tag
                        binding in this device.
                        ''',
                        'ip',
                        'Cisco-IOS-XE-trustsec-oper', True),
                    _MetaInfoClassMember('ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        IP-Prefix information to find its corresponding
                        Secure Group Tag. Only IPv4 prefix information is 
                        supported currently to get the Security Group Tag
                        binding in this device.
                        ''',
                        'ip',
                        'Cisco-IOS-XE-trustsec-oper', True),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF-Name to find the Security Group Tag for the 
                corresponding IP-Address in
                this VRF instance. Only default VRF is supported 
                currently which is indicated by
                (empty string).
                ''',
                'vrf_name',
                'Cisco-IOS-XE-trustsec-oper', True),
            _MetaInfoClassMember('sgt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Security Group Tag value corresponding to the
                given IP-Address.
                ''',
                'sgt',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('source', REFERENCE_ENUM_CLASS, 'CtsOdmBindingSourceEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'CtsOdmBindingSourceEnum', 
                [], [], 
                '''                Source information via which the Security 
                Group Tag binding was
                learned in this device.
                ''',
                'source',
                'Cisco-IOS-XE-trustsec-oper', False),
            ],
            'Cisco-IOS-XE-trustsec-oper',
            'cts-rolebased-sgtmap',
            _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper'
        ),
    },
    'TrustsecState.CtsRolebasedSgtmaps' : {
        'meta_info' : _MetaInfoClass('TrustsecState.CtsRolebasedSgtmaps',
            False, 
            [
            _MetaInfoClassMember('cts-rolebased-sgtmap', REFERENCE_LIST, 'CtsRolebasedSgtmap' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap', 
                [], [], 
                '''                Security Group Tag is assigned for an IP-Address
                based on the user permissions and authorization 
                level as configured by the network administrator
                in Identity Service Engine server or in the
                device locally
                ''',
                'cts_rolebased_sgtmap',
                'Cisco-IOS-XE-trustsec-oper', False),
            ],
            'Cisco-IOS-XE-trustsec-oper',
            'cts-rolebased-sgtmaps',
            _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper'
        ),
    },
    'TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy' : {
        'meta_info' : _MetaInfoClass('TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy',
            False, 
            [
            _MetaInfoClassMember('src-sgt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Source Security Group Tag number.
                This value must be in the 
                inclusive range of -1 to 65519.
                ''',
                'src_sgt',
                'Cisco-IOS-XE-trustsec-oper', True),
            _MetaInfoClassMember('dst-sgt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Destination Security Tag number.
                This value must be in the 
                inclusive range of -1 to 65519.
                ''',
                'dst_sgt',
                'Cisco-IOS-XE-trustsec-oper', True),
            _MetaInfoClassMember('hardware-deny-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that have been denied in the
                hardware forwarding path of the device by
                the Role based permissions between a Source
                Security Group and a Destination Security
                Group.
                ''',
                'hardware_deny_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('hardware-monitor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that have been monitored in the
                hardware forwarding path of the device
                by the Role based permissions between a Source
                Security Group and a Destination Security
                Group.
                ''',
                'hardware_monitor_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('hardware-permit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that have been permitted in the
                hardware forwarding path of the device
                by the Role based permissions between a Source
                Security Group and a Destination Security
                Group.
                ''',
                'hardware_permit_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('last-updated-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Indicates the time when the Role based permissions
                 between a Source Security Group and a Destination
                 Security Group was modified or updated last. The
                 value will be represented as date and time 
                 corresponding to the local time zone of the
                 Identify Services Engine when the Role based 
                 permissions was modified or updated
                 last.
                ''',
                'last_updated_time',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('monitor-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the monitor mode status between the Source
                Security Group and Destination
                Security Group is currently enabled or disabled.
                This will be TRUE if monitor
                mode is enabled and FALSE if it is disabled.
                ''',
                'monitor_mode',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('num-of-sgacl', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Security Group Access Control Lists that
                are currently applied between
                the Source Security Group and the Destination
                Security Group. This should match
                the number of Security Group Access Control List
                names in sgacl-name.
                ''',
                'num_of_sgacl',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('policy-life-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Duration of the Role based permissions that are
                applied    between a Source Security Group
                and a Destination Security Group. The duration
                is represented in seconds.
                ''',
                'policy_life_time',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('sgacl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                List of Security Group Access Control List names
                separated by semi-colon(;).
                ''',
                'sgacl_name',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('software-deny-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that have been denied in the 
                software forwarding path of the device
                by the Role based permissions between a Source
                Security Group and a Destination
                Security Group.
                ''',
                'software_deny_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('software-monitor-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that have been monitored in the
                software forwarding path of the device
                by the Role based permissions between a Source
                Security Group and a Destination Security
                Group.
                ''',
                'software_monitor_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('software-permit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets that have been permitted in the
                software forwarding path of the device
                by the Role based permissions between a Source
                Security Group and a Destination Security
                Group.
                ''',
                'software_permit_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('total-deny-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets that have been denied by
                the Role based permissions
                between a Source Security Group and a Destination
                Security Group. This corresponds to
                total packets denied in both hardware and software
                forwarding paths of the device.
                ''',
                'total_deny_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('total-permit-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Total number of packets that have been permitted
                by the Role based permissions
                between a Source Security Group and a Destination
                Security Group. This corresponds to
                total packets allowed in both hardware and software
                forwarding paths of the device.
                ''',
                'total_permit_count',
                'Cisco-IOS-XE-trustsec-oper', False),
            ],
            'Cisco-IOS-XE-trustsec-oper',
            'cts-rolebased-policy',
            _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper'
        ),
    },
    'TrustsecState.CtsRolebasedPolicies' : {
        'meta_info' : _MetaInfoClass('TrustsecState.CtsRolebasedPolicies',
            False, 
            [
            _MetaInfoClassMember('cts-rolebased-policy', REFERENCE_LIST, 'CtsRolebasedPolicy' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy', 
                [], [], 
                '''                Role based permissions between a Source Security Group
                and a Destination Security Group can be retrieved from
                the device using a Security Group Tag and Destination
                Group Tag value.
                ''',
                'cts_rolebased_policy',
                'Cisco-IOS-XE-trustsec-oper', False),
            ],
            'Cisco-IOS-XE-trustsec-oper',
            'cts-rolebased-policies',
            _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper'
        ),
    },
    'TrustsecState.CtsSxpConnections.CtsSxpConnection' : {
        'meta_info' : _MetaInfoClass('TrustsecState.CtsSxpConnections.CtsSxpConnection',
            False, 
            [
            _MetaInfoClassMember('peer-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IP-Address information of the peer of an SXP
                connection in this device. Only IPv4
                address is currently supported.
                ''',
                'peer_ip',
                'Cisco-IOS-XE-trustsec-oper', True, [
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP-Address information of the peer of an SXP
                        connection in this device. Only IPv4
                        address is currently supported.
                        ''',
                        'peer_ip',
                        'Cisco-IOS-XE-trustsec-oper', True),
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IP-Address information of the peer of an SXP
                        connection in this device. Only IPv4
                        address is currently supported.
                        ''',
                        'peer_ip',
                        'Cisco-IOS-XE-trustsec-oper', True),
                ]),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                vrf-name string of the VRF instance in this device,
                to which the peer of an SXP connection
                Belongs to. Only default VRF is supported currently
                which is indicated by empty string.
                ''',
                'vrf_name',
                'Cisco-IOS-XE-trustsec-oper', True),
            _MetaInfoClassMember('listener-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Duration of the SXP listener of the SXP connection
                in this device. This information is valid
                Only if the local mode of the SXP connection
                is Listener.
                ''',
                'listener_duration',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('listener-state', REFERENCE_ENUM_CLASS, 'SxpConStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'SxpConStateEnum', 
                [], [], 
                '''                SXP listener state information of the SXP 
                connection in this device. This information is
                valid only if the local mode of the SXP
                connection in the device is Listener.
                ''',
                'listener_state',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('local-mode', REFERENCE_ENUM_CLASS, 'SxpConModeEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'SxpConModeEnum', 
                [], [], 
                '''                SXP connection mode of this device for the SXP
                connection with the given peer.
                ''',
                'local_mode',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('source-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Source IP-Address of the SXP connection in this
                device for the given peer IP-Address.
                ''',
                'source_ip',
                'Cisco-IOS-XE-trustsec-oper', False, [
                    _MetaInfoClassMember('source-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source IP-Address of the SXP connection in this
                        device for the given peer IP-Address.
                        ''',
                        'source_ip',
                        'Cisco-IOS-XE-trustsec-oper', False),
                    _MetaInfoClassMember('source-ip', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Source IP-Address of the SXP connection in this
                        device for the given peer IP-Address.
                        ''',
                        'source_ip',
                        'Cisco-IOS-XE-trustsec-oper', False),
                ]),
            _MetaInfoClassMember('speaker-duration', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Duration of the SXP speaker of the SXP connection
                in this device. This information is valid
                only if the local mode of the SXP connection
                is Speaker.
                ''',
                'speaker_duration',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('speaker-state', REFERENCE_ENUM_CLASS, 'SxpConStateEnum' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'SxpConStateEnum', 
                [], [], 
                '''                SXP speaker state information of the SXP
                connection in this device. This information is
                valid only if the local mode of the SXP
                connection in this device is Speaker.
                ''',
                'speaker_state',
                'Cisco-IOS-XE-trustsec-oper', False),
            ],
            'Cisco-IOS-XE-trustsec-oper',
            'cts-sxp-connection',
            _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper'
        ),
    },
    'TrustsecState.CtsSxpConnections' : {
        'meta_info' : _MetaInfoClass('TrustsecState.CtsSxpConnections',
            False, 
            [
            _MetaInfoClassMember('cts-sxp-connection', REFERENCE_LIST, 'CtsSxpConnection' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'TrustsecState.CtsSxpConnections.CtsSxpConnection', 
                [], [], 
                '''                Trustsec SXP connection information from a device
                can be retrieved with the SXP connection peer IP
                address. Only IPv4 address as Peer IP and default
                VRF instance in device is supported currently
                ''',
                'cts_sxp_connection',
                'Cisco-IOS-XE-trustsec-oper', False),
            ],
            'Cisco-IOS-XE-trustsec-oper',
            'cts-sxp-connections',
            _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper'
        ),
    },
    'TrustsecState' : {
        'meta_info' : _MetaInfoClass('TrustsecState',
            False, 
            [
            _MetaInfoClassMember('cts-rolebased-policies', REFERENCE_CLASS, 'CtsRolebasedPolicies' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'TrustsecState.CtsRolebasedPolicies', 
                [], [], 
                '''                Role based permissions between a Source Security Group
                and a Destination Security Group are configured by the
                administrator in the Identity Services Engine or in the
                Device
                ''',
                'cts_rolebased_policies',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('cts-rolebased-sgtmaps', REFERENCE_CLASS, 'CtsRolebasedSgtmaps' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'TrustsecState.CtsRolebasedSgtmaps', 
                [], [], 
                '''                Security Group Tag value corresponding to an IP-Address 
                in the given VRF instance in this device.
                ''',
                'cts_rolebased_sgtmaps',
                'Cisco-IOS-XE-trustsec-oper', False),
            _MetaInfoClassMember('cts-sxp-connections', REFERENCE_CLASS, 'CtsSxpConnections' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper', 'TrustsecState.CtsSxpConnections', 
                [], [], 
                '''                Trustsec SXP connection is used between Cisco devices
                to propagate Security Group Tags from one device to 
                another device. One of the device will be in Speaker 
                mode or Listener mode or both the devices can be in
                both the connection modes.
                ''',
                'cts_sxp_connections',
                'Cisco-IOS-XE-trustsec-oper', False),
            ],
            'Cisco-IOS-XE-trustsec-oper',
            'trustsec-state',
            _yang_ns._namespaces['Cisco-IOS-XE-trustsec-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_trustsec_oper'
        ),
    },
}
_meta_table['TrustsecState.CtsRolebasedSgtmaps.CtsRolebasedSgtmap']['meta_info'].parent =_meta_table['TrustsecState.CtsRolebasedSgtmaps']['meta_info']
_meta_table['TrustsecState.CtsRolebasedPolicies.CtsRolebasedPolicy']['meta_info'].parent =_meta_table['TrustsecState.CtsRolebasedPolicies']['meta_info']
_meta_table['TrustsecState.CtsSxpConnections.CtsSxpConnection']['meta_info'].parent =_meta_table['TrustsecState.CtsSxpConnections']['meta_info']
_meta_table['TrustsecState.CtsRolebasedSgtmaps']['meta_info'].parent =_meta_table['TrustsecState']['meta_info']
_meta_table['TrustsecState.CtsRolebasedPolicies']['meta_info'].parent =_meta_table['TrustsecState']['meta_info']
_meta_table['TrustsecState.CtsSxpConnections']['meta_info'].parent =_meta_table['TrustsecState']['meta_info']
