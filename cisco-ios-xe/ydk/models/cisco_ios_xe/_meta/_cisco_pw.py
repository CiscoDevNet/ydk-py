


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'PwOperStateTypeEnum' : _MetaInfoEnum('PwOperStateTypeEnum', 'ydk.models.cisco_ios_xe.cisco_pw',
        {
            'up':'up',
            'down':'down',
            'cold-standby':'cold_standby',
            'hot-standby':'hot_standby',
            'recovering':'recovering',
            'no-hardware':'no_hardware',
            'unresolved':'unresolved',
            'provisioned':'provisioned',
            'remote-standby':'remote_standby',
            'local-ready':'local_ready',
            'all-ready':'all_ready',
        }, 'cisco-pw', _yang_ns._namespaces['cisco-pw']),
    'PwLoadBalanceTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PwLoadBalanceTypeIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-load-balance-type',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSignalingProtocolTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PwSignalingProtocolTypeIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-signaling-protocol-type',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSequencingTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PwSequencingTypeIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-sequencing-type',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwVcTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PwVcTypeIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-vc-type',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwEncapsulationTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PwEncapsulationTypeIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-encapsulation-type',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.Global_' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.Global_',
            False, 
            [
            _MetaInfoClassMember('predictive-redundancy', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable predictive redundancy
                ''',
                'predictive_redundancy',
                'cisco-pw', False),
            _MetaInfoClassMember('pw-grouping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable pw-grouping.
                
                When pseudowires (PW) are established, each PW is assigned
                a group ID that is common for all PWs created from the
                same physical port. Hence, when the physical port becomes
                non-functional or is deleted, L2VPN sends a single message
                to advertise the status change of all PWs belonging to the
                group. A single L2VPN signal thus avoids a lot of
                processing and loss in reactivity.
                ''',
                'pw_grouping',
                'cisco-pw', False),
            _MetaInfoClassMember('pw-oam-refresh-transmit', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Set pseudowire oam transmit refresh time (in seconds)
                ''',
                'pw_oam_refresh_transmit',
                'cisco-pw', False),
            _MetaInfoClassMember('pw-status', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable pw-status
                ''',
                'pw_status',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-state-notification-batch-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                'vc-state-notification' allows batching of pseudowires in
                order to reduce number of notifications generated from the
                device. All pseudowires in a batched notification MUST
                share same state at the same time.
                
                This leaf defines the maximum number of VCs that can be
                batched in vc-state-notification.
                ''',
                'vc_state_notification_batch_size',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-state-notification-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this leaf is set to true, then it enables the emission
                of 'vc-state-notification'; otherwise these notifications
                are not emitted.
                ''',
                'vc_state_notification_enabled',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-state-notification-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This leaf defines the maximum number of VC state change
                notifications that can be emitted from the device per
                second.
                ''',
                'vc_state_notification_rate',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'global',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel.DirectionEnum' : _MetaInfoEnum('DirectionEnum', 'ydk.models.cisco_ios_xe.cisco_pw',
        {
            'transmit':'transmit',
            'receive':'receive',
            'both':'both',
        }, 'cisco-pw', _yang_ns._namespaces['cisco-pw']),
    'PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_ENUM_CLASS, 'DirectionEnum' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel.DirectionEnum', 
                [], [], 
                '''                Directions to enable Flow Aware Label PW
                ''',
                'direction',
                'cisco-pw', False),
            _MetaInfoClassMember('static', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use statically configured flow label on traffic
                flowing on the PW
                ''',
                'static',
                'cisco-pw', False),
            _MetaInfoClassMember('tlv-code-17', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Carry code 0x17 as Flow Aware Label (FAT) PW signalled
                sub-tlv id
                ''',
                'tlv_code_17',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'flow-label',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.LoadBalance' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.LoadBalance',
            False, 
            [
            _MetaInfoClassMember('ethernet', REFERENCE_IDENTITY_CLASS, 'PwLbEthernetTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwLbEthernetTypeIdentity', 
                [], [], 
                '''                Ethernet mac address based load balancing
                ''',
                'ethernet',
                'cisco-pw', False),
            _MetaInfoClassMember('flow-label', REFERENCE_CLASS, 'FlowLabel' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel', 
                [], [], 
                '''                Enable Flow Aware Label (FAT) PW - the capability to
                carry flow label on PW
                ''',
                'flow_label',
                'cisco-pw', False),
            _MetaInfoClassMember('ip', REFERENCE_IDENTITY_CLASS, 'PwLbIpTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwLbIpTypeIdentity', 
                [], [], 
                '''                IP address based load balancing
                ''',
                'ip',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'load-balance',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.PreferredPath' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.PreferredPath',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                TODO
                ''',
                'address',
                'cisco-pw', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        TODO
                        ''',
                        'address',
                        'cisco-pw', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        TODO
                        ''',
                        'address',
                        'cisco-pw', False),
                ]),
            _MetaInfoClassMember('disable-fallback', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable fall back to alternative route
                ''',
                'disable_fallback',
                'cisco-pw', False),
            _MetaInfoClassMember('hostname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TODO
                ''',
                'hostname',
                'cisco-pw', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to a tunnel interface.
                ''',
                'interface',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'preferred-path',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.Sequencing' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.Sequencing',
            False, 
            [
            _MetaInfoClassMember('direction', REFERENCE_IDENTITY_CLASS, 'PwSequencingTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwSequencingTypeIdentity', 
                [], [], 
                '''                TODO
                ''',
                'direction',
                'cisco-pw', False),
            _MetaInfoClassMember('resync', ATTRIBUTE, 'int' , None, None, 
                [('5', '65535')], [], 
                '''                TODO
                ''',
                'resync',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'sequencing',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.Vccv' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.Vccv',
            False, 
            [
            _MetaInfoClassMember('control-word', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable VCCV verification type
                ''',
                'control_word',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'vccv',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay',
            False, 
            [
            _MetaInfoClassMember('never', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The primary pseudowire never takes over for the backup
                ''',
                'never',
                'cisco-pw', False),
            _MetaInfoClassMember('switchover-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '120')], [], 
                '''                Specifies how long the backup pseudowire should wait before
                taking over
                ''',
                'switchover_timer',
                'cisco-pw', False),
            _MetaInfoClassMember('timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '180')], [], 
                '''                Specifies how long the primary pseudowire should wait
                after it becomes active to take over for the backup
                pseudowire
                ''',
                'timer',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'switchover-delay',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.Status' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.Status',
            False, 
            [
            _MetaInfoClassMember('decoupled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Reflect standby status of the attachment circuit as up on
                the pseudowire.
                ''',
                'decoupled',
                'cisco-pw', False),
            _MetaInfoClassMember('disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Do not send pseudowire status to peer.
                ''',
                'disable',
                'cisco-pw', False),
            _MetaInfoClassMember('peer-topo-dual-homed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Our peer(s) are participating in a redundant solution with
                some form of redundancy protocol running between the peer
                routers. Only one of the remote peers will advertise a
                status of UP at a time. The other will advertise standby.
                Change our configuration so we can send a status of UP on
                both active and redundant pseudowires.
                ''',
                'peer_topo_dual_homed',
                'cisco-pw', False),
            _MetaInfoClassMember('redundancy-master', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Make the PE as master to enables Pseudowire Preferential
                Forwarding feature to display the status of  the active
                and backup pseudowires.
                ''',
                'redundancy_master',
                'cisco-pw', False),
            _MetaInfoClassMember('route-watch-disable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Disable listening for routing events to trigger redundancy
                status changes
                ''',
                'route_watch_disable',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'status',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec',
            False, 
            [
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description string for the port profile
                ''',
                'description',
                'cisco-pw', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable this port profile
                ''',
                'enabled',
                'cisco-pw', False),
            _MetaInfoClassMember('max-ports', ATTRIBUTE, 'int' , None, None, 
                [('1', '16384')], [], 
                '''                Maximum number of ports
                ''',
                'max_ports',
                'cisco-pw', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MTU of the port
                ''',
                'mtu',
                'cisco-pw', False),
            _MetaInfoClassMember('shut-force', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Force shut down this port profile
                ''',
                'shut_force',
                'cisco-pw', False),
            _MetaInfoClassMember('shutdown', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Shut down this template
                ''',
                'shutdown',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'port-profile-spec',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates.PwTemplate' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates.PwTemplate',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                PW Template name.
                ''',
                'name',
                'cisco-pw', True),
            _MetaInfoClassMember('control-word', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Use control word in the MPLS PW header.
                ''',
                'control_word',
                'cisco-pw', False),
            _MetaInfoClassMember('encapsulation', REFERENCE_IDENTITY_CLASS, 'PwEncapsulationTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwEncapsulationTypeIdentity', 
                [], [], 
                '''                Encapsulation used for PW
                ''',
                'encapsulation',
                'cisco-pw', False),
            _MetaInfoClassMember('load-balance', REFERENCE_CLASS, 'LoadBalance' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.LoadBalance', 
                [], [], 
                '''                Load balancing mechanism.
                ''',
                'load_balance',
                'cisco-pw', False),
            _MetaInfoClassMember('mac-withdraw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Send Mac-withdraw message when PW becomes active.
                ''',
                'mac_withdraw',
                'cisco-pw', False),
            _MetaInfoClassMember('port-profile-spec', REFERENCE_CLASS, 'PortProfileSpec' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec', 
                [], [], 
                '''                Pseudowire port profile configurations.
                ''',
                'port_profile_spec',
                'cisco-pw', False),
            _MetaInfoClassMember('preferred-path', REFERENCE_CLASS, 'PreferredPath' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.PreferredPath', 
                [], [], 
                '''                Preferred path for the PW
                ''',
                'preferred_path',
                'cisco-pw', False),
            _MetaInfoClassMember('sequencing', REFERENCE_CLASS, 'Sequencing' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.Sequencing', 
                [], [], 
                '''                Sequencing options
                ''',
                'sequencing',
                'cisco-pw', False),
            _MetaInfoClassMember('signaling-protocol', REFERENCE_IDENTITY_CLASS, 'PwSignalingProtocolTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwSignalingProtocolTypeIdentity', 
                [], [], 
                '''                Signaling protocol to use.
                ''',
                'signaling_protocol',
                'cisco-pw', False),
            _MetaInfoClassMember('source-ip', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The local source IPv4 address
                ''',
                'source_ip',
                'cisco-pw', False),
            _MetaInfoClassMember('status', REFERENCE_CLASS, 'Status' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.Status', 
                [], [], 
                '''                TODO
                ''',
                'status',
                'cisco-pw', False),
            _MetaInfoClassMember('switching-tlv', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Send switching TLV
                ''',
                'switching_tlv',
                'cisco-pw', False),
            _MetaInfoClassMember('switchover-delay', REFERENCE_CLASS, 'SwitchoverDelay' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay', 
                [], [], 
                '''                Timer configuration related to pseudowire redundancy
                switchover and restoring to primary
                ''',
                'switchover_delay',
                'cisco-pw', False),
            _MetaInfoClassMember('tag-rewrite-ingress-vlan', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Configure ingress tag rewrite vlan.
                ''',
                'tag_rewrite_ingress_vlan',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-type', REFERENCE_IDENTITY_CLASS, 'PwVcTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwVcTypeIdentity', 
                [], [], 
                '''                Type of VC in the PW.
                ''',
                'vc_type',
                'cisco-pw', False),
            _MetaInfoClassMember('vccv', REFERENCE_CLASS, 'Vccv' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate.Vccv', 
                [], [], 
                '''                VCCV configuration
                ''',
                'vccv',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'pw-template',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwTemplates' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwTemplates',
            False, 
            [
            _MetaInfoClassMember('pw-template', REFERENCE_LIST, 'PwTemplate' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates.PwTemplate', 
                [], [], 
                '''                Pseudowire template list.
                ''',
                'pw_template',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'pw-templates',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwStaticOamClasses.PwStaticOamClass' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwStaticOamClasses.PwStaticOamClass',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OAM class name
                ''',
                'name',
                'cisco-pw', True),
            _MetaInfoClassMember('ack', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable ack
                ''',
                'ack',
                'cisco-pw', False),
            _MetaInfoClassMember('keepalive', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Keepalive in seconds
                ''',
                'keepalive',
                'cisco-pw', False),
            _MetaInfoClassMember('timeout-refresh-ack', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Ack timeout in seconds
                ''',
                'timeout_refresh_ack',
                'cisco-pw', False),
            _MetaInfoClassMember('timeout-refresh-send', ATTRIBUTE, 'int' , None, None, 
                [('1', '4095')], [], 
                '''                Refresh timeout in seconds
                ''',
                'timeout_refresh_send',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'pw-static-oam-class',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig.PwStaticOamClasses' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig.PwStaticOamClasses',
            False, 
            [
            _MetaInfoClassMember('pw-static-oam-class', REFERENCE_LIST, 'PwStaticOamClass' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwStaticOamClasses.PwStaticOamClass', 
                [], [], 
                '''                Pseudowire static oam class configuration
                ''',
                'pw_static_oam_class',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'pw-static-oam-classes',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireConfig' : {
        'meta_info' : _MetaInfoClass('PseudowireConfig',
            False, 
            [
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.Global_', 
                [], [], 
                '''                Global configurations related to pseudowires.
                ''',
                'global_',
                'cisco-pw', False),
            _MetaInfoClassMember('pw-static-oam-classes', REFERENCE_CLASS, 'PwStaticOamClasses' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwStaticOamClasses', 
                [], [], 
                '''                List of pseudowire static oam classes.
                ''',
                'pw_static_oam_classes',
                'cisco-pw', False),
            _MetaInfoClassMember('pw-templates', REFERENCE_CLASS, 'PwTemplates' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireConfig.PwTemplates', 
                [], [], 
                '''                Contains list of all pw-template definitions.
                Also called PW Class (XR) and Port Profile (NX-OS)
                ''',
                'pw_templates',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'pseudowire-config',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireState.Pseudowires.Statistics' : {
        'meta_info' : _MetaInfoClass('PseudowireState.Pseudowires.Statistics',
            False, 
            [
            _MetaInfoClassMember('discontinuity-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The time on the most recent occasion at which any of
                this pseudowire's counters sufferred discontinuity.
                If no such discontinuities have occurred since the
                last re-initialization of the local management
                subsystem, then this node contains the time the
                local management subsystem re-initialized itself.
                ''',
                'discontinuity_time',
                'cisco-pw', False),
            _MetaInfoClassMember('in-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of inbound packets that contained
                errors.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system
                and at other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_errors',
                'cisco-pw', False),
            _MetaInfoClassMember('in-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets received on this
                pseudowire.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system
                and at other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_octets',
                'cisco-pw', False),
            _MetaInfoClassMember('in-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets received on this
                pseudowire.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system
                and at other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'in_pkts',
                'cisco-pw', False),
            _MetaInfoClassMember('out-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of outbound packets that could not
                be sent on this pseudowire.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system
                and at other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_errors',
                'cisco-pw', False),
            _MetaInfoClassMember('out-octets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of octets sent on this pseudowire.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system
                and at other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_octets',
                'cisco-pw', False),
            _MetaInfoClassMember('out-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of packets sent on this pseudowire.
                
                Discontinuities in the value of this counter can
                occur at re-initialization of the management system
                and at other times as indicated by the value of
                'discontinuity-time'.
                ''',
                'out_pkts',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-create-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                System time when this VC was created
                ''',
                'vc_create_time',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-up-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of consecutive ticks this VC has been 'up' in
                both directions together
                ''',
                'vc_up_time',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'statistics',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireState.Pseudowires.VcOwnerTypeEnum' : _MetaInfoEnum('VcOwnerTypeEnum', 'ydk.models.cisco_ios_xe.cisco_pw',
        {
            'vpws':'vpws',
            'vpls-vfi':'vpls_vfi',
            'vpls-bridge-domain':'vpls_bridge_domain',
            'interface':'interface',
        }, 'cisco-pw', _yang_ns._namespaces['cisco-pw']),
    'PseudowireState.Pseudowires.VcPsnTypeEnum' : _MetaInfoEnum('VcPsnTypeEnum', 'ydk.models.cisco_ios_xe.cisco_pw',
        {
            'mpls':'mpls',
            'l2tp':'l2tp',
            'ip':'ip',
            'mpls-over-ip':'mpls_over_ip',
            'gre':'gre',
            'other':'other',
        }, 'cisco-pw', _yang_ns._namespaces['cisco-pw']),
    'PseudowireState.Pseudowires.VcRemoteControlWordEnum' : _MetaInfoEnum('VcRemoteControlWordEnum', 'ydk.models.cisco_ios_xe.cisco_pw',
        {
            'noControlWord':'noControlWord',
            'withControlWord':'withControlWord',
            'notYetKnown':'notYetKnown',
        }, 'cisco-pw', _yang_ns._namespaces['cisco-pw']),
    'PseudowireState.Pseudowires' : {
        'meta_info' : _MetaInfoClass('PseudowireState.Pseudowires',
            False, 
            [
            _MetaInfoClassMember('vc-peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                This object contains the value of the peer node address
                of the PW/PE protocol entity
                ''',
                'vc_peer_address',
                'cisco-pw', True, [
                    _MetaInfoClassMember('vc-peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This object contains the value of the peer node address
                        of the PW/PE protocol entity
                        ''',
                        'vc_peer_address',
                        'cisco-pw', True),
                    _MetaInfoClassMember('vc-peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        This object contains the value of the peer node address
                        of the PW/PE protocol entity
                        ''',
                        'vc_peer_address',
                        'cisco-pw', True),
                ]),
            _MetaInfoClassMember('vc-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used to distinguish between pseudowires going to the
                same peer node
                ''',
                'vc_id',
                'cisco-pw', True),
            _MetaInfoClassMember('vc-owner-type', REFERENCE_ENUM_CLASS, 'VcOwnerTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireState.Pseudowires.VcOwnerTypeEnum', 
                [], [], 
                '''                Indicates the service responsible for establishing
                this VC
                ''',
                'vc_owner_type',
                'cisco-pw', True),
            _MetaInfoClassMember('vc-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The canonical name assigned to the VC. The name may be
                autogenerated by the device; this Yang model does not
                currently support direct configuration of this name.
                ''',
                'vc_name',
                'cisco-pw', True),
            _MetaInfoClassMember('vc-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Locally-unique ID within the device for this
                pseudowire
                ''',
                'vc_index',
                'cisco-pw', True),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireState.Pseudowires.Statistics', 
                [], [], 
                '''                A collection of pseudowire-related statistics objects
                ''',
                'statistics',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-control-word', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates if the control word is sent with each packet
                by the local node
                ''',
                'vc_control_word',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-inbound-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VC label used in the inbound direction (i.e. packets
                received from the PSN). Example: for MPLS PSN, it
                represents the 20 bits of VC tag, for L2TP it represents
                the 32 bits Session ID. If the label is not yet known
                (signaling in process), the object should return a value
                of 0xFFFFFFFF.
                ''',
                'vc_inbound_label',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-inbound-oper-status', REFERENCE_ENUM_CLASS, 'PwOperStateTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwOperStateTypeEnum', 
                [], [], 
                '''                Indicates the actual operational status of this VC in
                the  inbound direction
                ''',
                'vc_inbound_oper_status',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-local-group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Used to identify which local pseudowire group this
                pseudowire belongs to
                ''',
                'vc_local_group_id',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-local-if-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If not zero, this represents the locally supported MTU
                size over the interface (or the virtual interface)
                associated with the VC
                ''',
                'vc_local_if_mtu',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-oper-status', REFERENCE_ENUM_CLASS, 'PwOperStateTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwOperStateTypeEnum', 
                [], [], 
                '''                Indicates the actual combined operational status of this
                VC. It is 'up' if both vc-inbound-oper-status and
                vc-outbound-oper-status are in 'up' state. For all other
                values, if the VCs in both directions are of the same
                value it reflects that value, otherwise it is set to the
                most severe status out of the two statuses. The order of
                severance from most severe to less severe is: unknown,
                notPresent, down, lowerLayerDown, dormant, testing, up.
                The operator may consult the per direction oper-status
                for fault isolation per direction.
                ''',
                'vc_oper_status',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-outbound-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The VC label used in the outbound direction (i.e. toward
                the PSN). Example: for MPLS PSN, it represents the 20 bits
                of VC tag, for L2TP it represent the 32 bits Session ID.
                If the label is not yet known (signaling in procesS), the
                object should return a value of 0xFFFFFFFF.
                ''',
                'vc_outbound_label',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-outbound-oper-status', REFERENCE_ENUM_CLASS, 'PwOperStateTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwOperStateTypeEnum', 
                [], [], 
                '''                Indicates the actual operational status of this VC in
                the outbound direction
                ''',
                'vc_outbound_oper_status',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-owner-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the L2VPN service instance that created
                the pseudowire VC
                ''',
                'vc_owner_name',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-psn-type', REFERENCE_ENUM_CLASS, 'VcPsnTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireState.Pseudowires.VcPsnTypeEnum', 
                [], [], 
                '''                Indicates the type of packet-switched network
                that carries this VC
                ''',
                'vc_psn_type',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-remote-control-word', REFERENCE_ENUM_CLASS, 'VcRemoteControlWordEnum' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireState.Pseudowires.VcRemoteControlWordEnum', 
                [], [], 
                '''                Indicates whether MPLS control words are used by the
                pseudowire PSN service
                ''',
                'vc_remote_control_word',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-remote-group-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                If not zero, indicates the pseudowire group to which
                this pseudowire belongs on the peer node
                ''',
                'vc_remote_group_id',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-remote-if-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remote interface MTU as (optionally) received
                from the remote node via the signaling protocol.
                Should be zero if this parameter is not available
                or not used
                ''',
                'vc_remote_if_mtu',
                'cisco-pw', False),
            _MetaInfoClassMember('vc-type', REFERENCE_IDENTITY_CLASS, 'PwVcTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwVcTypeIdentity', 
                [], [], 
                '''                Indicates the service to be carried over this VC
                ''',
                'vc_type',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'pseudowires',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PseudowireState' : {
        'meta_info' : _MetaInfoClass('PseudowireState',
            False, 
            [
            _MetaInfoClassMember('pseudowires', REFERENCE_LIST, 'Pseudowires' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PseudowireState.Pseudowires', 
                [], [], 
                '''                Each list element contains the state for a pseudowire
                instance. The list can be optionally keyed by any
                combination of vc-id, peer-address, etc.
                Additional filtering of the list by the agent may be
                performed upon request by the client using subtree
                filtering as described in RFC 6020 Section 6.
                ''',
                'pseudowires',
                'cisco-pw', False),
            ],
            'cisco-pw',
            'pseudowire-state',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSequencingTransmitIdentity' : {
        'meta_info' : _MetaInfoClass('PwSequencingTransmitIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-sequencing-transmit',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSignalingProtocolNoneIdentity' : {
        'meta_info' : _MetaInfoClass('PwSignalingProtocolNoneIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-signaling-protocol-none',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwVcTypeVlanPassthroughIdentity' : {
        'meta_info' : _MetaInfoClass('PwVcTypeVlanPassthroughIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-vc-type-vlan-passthrough',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwVcTypeVlanIdentity' : {
        'meta_info' : _MetaInfoClass('PwVcTypeVlanIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-vc-type-vlan',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSequencingReceiveIdentity' : {
        'meta_info' : _MetaInfoClass('PwSequencingReceiveIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-sequencing-receive',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSignalingProtocolLdpIdentity' : {
        'meta_info' : _MetaInfoClass('PwSignalingProtocolLdpIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-signaling-protocol-ldp',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbEthernetTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbEthernetTypeIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-ethernet-type',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSequencingBothIdentity' : {
        'meta_info' : _MetaInfoClass('PwSequencingBothIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-sequencing-both',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwVcTypeEtherIdentity' : {
        'meta_info' : _MetaInfoClass('PwVcTypeEtherIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-vc-type-ether',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbIpTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbIpTypeIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-ip-type',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbIpDstIpIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbIpDstIpIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-ip-dst-ip',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwEncapMplsIdentity' : {
        'meta_info' : _MetaInfoClass('PwEncapMplsIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-encap-mpls',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwSignalingProtocolBgpIdentity' : {
        'meta_info' : _MetaInfoClass('PwSignalingProtocolBgpIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-signaling-protocol-bgp',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbIpSrcDstIpIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbIpSrcDstIpIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-ip-src-dst-ip',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbEthSrcDstMacIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbEthSrcDstMacIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-eth-src-dst-mac',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbEthSrcMacIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbEthSrcMacIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-eth-src-mac',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbEthDstMacIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbEthDstMacIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-eth-dst-mac',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
    'PwLbIpSrcIpIdentity' : {
        'meta_info' : _MetaInfoClass('PwLbIpSrcIpIdentity',
            False, 
            [
            ],
            'cisco-pw',
            'pw-lb-ip-src-ip',
            _yang_ns._namespaces['cisco-pw'],
        'ydk.models.cisco_ios_xe.cisco_pw'
        ),
    },
}
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.LoadBalance.FlowLabel']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate.LoadBalance']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.LoadBalance']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.PreferredPath']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.Sequencing']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.Vccv']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.SwitchoverDelay']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.Status']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate.PortProfileSpec']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info']
_meta_table['PseudowireConfig.PwTemplates.PwTemplate']['meta_info'].parent =_meta_table['PseudowireConfig.PwTemplates']['meta_info']
_meta_table['PseudowireConfig.PwStaticOamClasses.PwStaticOamClass']['meta_info'].parent =_meta_table['PseudowireConfig.PwStaticOamClasses']['meta_info']
_meta_table['PseudowireConfig.Global_']['meta_info'].parent =_meta_table['PseudowireConfig']['meta_info']
_meta_table['PseudowireConfig.PwTemplates']['meta_info'].parent =_meta_table['PseudowireConfig']['meta_info']
_meta_table['PseudowireConfig.PwStaticOamClasses']['meta_info'].parent =_meta_table['PseudowireConfig']['meta_info']
_meta_table['PseudowireState.Pseudowires.Statistics']['meta_info'].parent =_meta_table['PseudowireState.Pseudowires']['meta_info']
_meta_table['PseudowireState.Pseudowires']['meta_info'].parent =_meta_table['PseudowireState']['meta_info']
