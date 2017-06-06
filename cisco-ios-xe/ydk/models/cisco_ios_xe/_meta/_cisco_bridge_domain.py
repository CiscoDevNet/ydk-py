


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'BridgeDomainStateTypeEnum' : _MetaInfoEnum('BridgeDomainStateTypeEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_domain',
        {
            'up':'up',
            'down':'down',
            'admin-down':'admin_down',
        }, 'cisco-bridge-domain', _yang_ns._namespaces['cisco-bridge-domain']),
    'BridgeDomainConfig.Global_.Pbb' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.Global_.Pbb',
            False, 
            [
            _MetaInfoClassMember('backbone-src-mac', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Backbone source mac address configuration for Provider
                Backbone Bridging (PBB)
                ''',
                'backbone_src_mac',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'pbb',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.Global_' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.Global_',
            False, 
            [
            _MetaInfoClassMember('bd-state-notification-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this leaf is set to true, then it enables the emission
                of 'bd-state-notification'; otherwise these notifications
                are not emitted.
                ''',
                'bd_state_notification_enabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('bd-state-notification-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This leaf defines the maximum number of 'bd-state-
                notification' that can be emitted from the device per
                second.
                ''',
                'bd_state_notification_rate',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('pbb', REFERENCE_CLASS, 'Pbb' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.Global_.Pbb', 
                [], [], 
                '''                Provider Backbone Bridging (PBB) related global
                configurations.
                ''',
                'pbb',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'global',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeGroups.BridgeGroup' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeGroups.BridgeGroup',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Bridge-group name
                ''',
                'name',
                'cisco-bridge-domain', True),
            ],
            'cisco-bridge-domain',
            'bridge-group',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeGroups' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeGroups',
            False, 
            [
            _MetaInfoClassMember('bridge-group', REFERENCE_LIST, 'BridgeGroup' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeGroups.BridgeGroup', 
                [], [], 
                '''                Bridge-group configuration.
                ''',
                'bridge_group',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-groups',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Split Horizon group number for bridge domain member.
                ''',
                'id',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'split-horizon-group',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacLimitActionEnum', 
                [], [], 
                '''                MAC limit violation actions.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of mac addresses that can be learnt
                ''',
                'maximum',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('notification', REFERENCE_IDENTITY_CLASS, 'MacLimitNotificationTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacLimitNotificationTypeIdentity', 
                [], [], 
                '''                MAC limit violation notifications.
                ''',
                'notification',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'limit',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging',
            False, 
            [
            _MetaInfoClassMember('time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The timeout period in seconds for aging out
                dynamically learned forwarding information
                ''',
                'time',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MacAgingTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacAgingTypeEnum', 
                [], [], 
                '''                MAC aging type.
                ''',
                'type',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'aging',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown',
            False, 
            [
            _MetaInfoClassMember('flush', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable mac table flush when port moves to down
                state.
                ''',
                'flush',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'port-down',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacSecureActionEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacSecureActionEnum', 
                [], [], 
                '''                MAC secure action for violating packets.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable mac secure feature
                ''',
                'enabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable logging.
                ''',
                'logging',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'secure',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac',
            False, 
            [
            _MetaInfoClassMember('aging', REFERENCE_CLASS, 'Aging' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging', 
                [], [], 
                '''                MAC aging configurations.
                ''',
                'aging',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('learning-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable disable mac learning
                ''',
                'learning_enabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('limit', REFERENCE_CLASS, 'Limit' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit', 
                [], [], 
                '''                MAC table learning limit.
                ''',
                'limit',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('port-down', REFERENCE_CLASS, 'PortDown' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown', 
                [], [], 
                '''                Port down event
                ''',
                'port_down',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('secure', REFERENCE_CLASS, 'Secure' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure', 
                [], [], 
                '''                MAC secure parameters.
                ''',
                'secure',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mac',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IGMP snooping profile name
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'igmp-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MLD snooping profile name.
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mld-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCPv4 snooping profile name
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'dhcp-ipv4-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding',
            False, 
            [
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable flooding
                ''',
                'disabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('disabled-unknown-unicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable unknown unicast flooding
                ''',
                'disabled_unknown_unicast',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'flooding',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds.UnitEnum' : _MetaInfoEnum('UnitEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_domain',
        {
            'bps':'bps',
            'kbps':'kbps',
            'pps':'pps',
        }, 'cisco-storm-control', _yang_ns._namespaces['cisco-storm-control']),
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds',
            False, 
            [
            _MetaInfoClassMember('traffic-class', REFERENCE_ENUM_CLASS, 'EthTrafficClassEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'EthTrafficClassEnum', 
                [], [], 
                '''                This leaf identifies a ethernet traffic type for
                which an administrator desires to configure storm
                control.
                ''',
                'traffic_class',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'UnitEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds.UnitEnum', 
                [], [], 
                '''                This enumeration define unit of the traffic threshold
                value.
                ''',
                'unit',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Traffic threshold value. Unit of the value is indicated by
                leaf 'unit'.
                ''',
                'value',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'thresholds',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_IDENTITY_CLASS, 'StormControlActionIdentity' , 'ydk.models.cisco_ios_xe.cisco_storm_control', 'StormControlActionIdentity', 
                [], [], 
                '''                This leaf represents the storm control action taken when
                the traffic of a particular type exceeds the configured
                threshold values.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('thresholds', REFERENCE_LIST, 'Thresholds' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds', 
                [], [], 
                '''                A collection of storm control threshold configuration
                entries.
                ''',
                'thresholds',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'storm-control',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation',
            False, 
            [
            _MetaInfoClassMember('dst-mac', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match Destination MAC Address
                ''',
                'dst_mac',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match IPv4 Address
                ''',
                'ipv4',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('src-mac', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match Source MAC Address
                ''',
                'src_mac',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'address-validation',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection',
            False, 
            [
            _MetaInfoClassMember('address-validation', REFERENCE_CLASS, 'AddressValidation' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation', 
                [], [], 
                '''                Enable address validation.
                ''',
                'address_validation',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable Dynamic ARP Inspection.
                ''',
                'enable',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable DAI logging
                ''',
                'logging',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'dynamic-arp-inspection',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable IP source guard feature.
                ''',
                'enable',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable IPSG logging
                ''',
                'logging',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'ip-source-guard',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an attchment circuit interface
                instance which is configured to be part of this
                bridge-domain.
                ''',
                'interface',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('dhcp-ipv4-snooping', REFERENCE_CLASS, 'DhcpIpv4Snooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping', 
                [], [], 
                '''                Enable DHCP IPv4 snooping.
                ''',
                'dhcp_ipv4_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('dynamic-arp-inspection', REFERENCE_CLASS, 'DynamicArpInspection' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection', 
                [], [], 
                '''                Dynamic ARP Inspection (DAI) configurations.
                ''',
                'dynamic_arp_inspection',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('flooding', REFERENCE_CLASS, 'Flooding' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding', 
                [], [], 
                '''                Flooding configurations.
                ''',
                'flooding',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('igmp-snooping', REFERENCE_CLASS, 'IgmpSnooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping', 
                [], [], 
                '''                Enable IGMP snooping.
                ''',
                'igmp_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('ip-source-guard', REFERENCE_CLASS, 'IpSourceGuard' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard', 
                [], [], 
                '''                IP source guard (IPSG) configurations.
                ''',
                'ip_source_guard',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac', 
                [], [], 
                '''                MAC features for bridge domain.
                ''',
                'mac',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mld-snooping', REFERENCE_CLASS, 'MldSnooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping', 
                [], [], 
                '''                Enable MLD snooping
                ''',
                'mld_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('split-horizon-group', REFERENCE_CLASS, 'SplitHorizonGroup' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup', 
                [], [], 
                '''                Bridge domain aggregates attachment circuits (ACs) and
                pseudowires (PWs) in one or more groups called Split Horizon
                Groups. When applied to bridge domains, Split Horizon refers
                to the flooding and forwarding behavior between members of a
                Split Horizon group. In general, frames received on one
                member of a split horizon group are not flooded out to the
                other members.
                ''',
                'split_horizon_group',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('storm-control', REFERENCE_CLASS, 'StormControl' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl', 
                [], [], 
                '''                A collection of storm control threshold and action
                configurations.
                ''',
                'storm_control',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'ac-member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an Virtual Forwarding Interface
                instance which is configured to be part of this
                bridge-domain
                ''',
                'interface',
                'cisco-bridge-domain', True),
            ],
            'cisco-bridge-domain',
            'vfi-member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an access pseudo-wire interface
                instance which is configured to be part of this
                bridge domain
                ''',
                'interface',
                'cisco-bridge-domain', True),
            ],
            'cisco-bridge-domain',
            'access-pw-if-member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel',
            False, 
            [
            _MetaInfoClassMember('local-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Local MPLS label ID
                ''',
                'local_label',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('remote-label', ATTRIBUTE, 'int' , None, None, 
                [('16', '1048575')], [], 
                '''                Remote MPLS label ID
                ''',
                'remote_label',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'static-label',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Split Horizon group number for bridge domain member.
                ''',
                'id',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'split-horizon-group',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacLimitActionEnum', 
                [], [], 
                '''                MAC limit violation actions.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of mac addresses that can be learnt
                ''',
                'maximum',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('notification', REFERENCE_IDENTITY_CLASS, 'MacLimitNotificationTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacLimitNotificationTypeIdentity', 
                [], [], 
                '''                MAC limit violation notifications.
                ''',
                'notification',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'limit',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging',
            False, 
            [
            _MetaInfoClassMember('time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The timeout period in seconds for aging out
                dynamically learned forwarding information
                ''',
                'time',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MacAgingTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacAgingTypeEnum', 
                [], [], 
                '''                MAC aging type.
                ''',
                'type',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'aging',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown',
            False, 
            [
            _MetaInfoClassMember('flush', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable mac table flush when port moves to down
                state.
                ''',
                'flush',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'port-down',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacSecureActionEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacSecureActionEnum', 
                [], [], 
                '''                MAC secure action for violating packets.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable or disable mac secure feature
                ''',
                'enabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable logging.
                ''',
                'logging',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'secure',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac',
            False, 
            [
            _MetaInfoClassMember('aging', REFERENCE_CLASS, 'Aging' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging', 
                [], [], 
                '''                MAC aging configurations.
                ''',
                'aging',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('learning-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable disable mac learning
                ''',
                'learning_enabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('limit', REFERENCE_CLASS, 'Limit' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit', 
                [], [], 
                '''                MAC table learning limit.
                ''',
                'limit',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('port-down', REFERENCE_CLASS, 'PortDown' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown', 
                [], [], 
                '''                Port down event
                ''',
                'port_down',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('secure', REFERENCE_CLASS, 'Secure' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure', 
                [], [], 
                '''                MAC secure parameters.
                ''',
                'secure',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mac',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IGMP snooping profile name
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'igmp-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MLD snooping profile name.
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mld-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCPv4 snooping profile name
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'dhcp-ipv4-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding',
            False, 
            [
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable flooding
                ''',
                'disabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('disabled-unknown-unicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable unknown unicast flooding
                ''',
                'disabled_unknown_unicast',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'flooding',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds.UnitEnum' : _MetaInfoEnum('UnitEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_domain',
        {
            'bps':'bps',
            'kbps':'kbps',
            'pps':'pps',
        }, 'cisco-storm-control', _yang_ns._namespaces['cisco-storm-control']),
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds',
            False, 
            [
            _MetaInfoClassMember('traffic-class', REFERENCE_ENUM_CLASS, 'EthTrafficClassEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'EthTrafficClassEnum', 
                [], [], 
                '''                This leaf identifies a ethernet traffic type for
                which an administrator desires to configure storm
                control.
                ''',
                'traffic_class',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'UnitEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds.UnitEnum', 
                [], [], 
                '''                This enumeration define unit of the traffic threshold
                value.
                ''',
                'unit',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Traffic threshold value. Unit of the value is indicated by
                leaf 'unit'.
                ''',
                'value',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'thresholds',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_IDENTITY_CLASS, 'StormControlActionIdentity' , 'ydk.models.cisco_ios_xe.cisco_storm_control', 'StormControlActionIdentity', 
                [], [], 
                '''                This leaf represents the storm control action taken when
                the traffic of a particular type exceeds the configured
                threshold values.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('thresholds', REFERENCE_LIST, 'Thresholds' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds', 
                [], [], 
                '''                A collection of storm control threshold configuration
                entries.
                ''',
                'thresholds',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'storm-control',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup',
            False, 
            [
            _MetaInfoClassMember('neighbor-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 or IPv6 address of the neighbor.
                ''',
                'neighbor_ip_address',
                'cisco-bridge-domain', False, [
                    _MetaInfoClassMember('neighbor-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 or IPv6 address of the neighbor.
                        ''',
                        'neighbor_ip_address',
                        'cisco-bridge-domain', False),
                    _MetaInfoClassMember('neighbor-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 or IPv6 address of the neighbor.
                        ''',
                        'neighbor_ip_address',
                        'cisco-bridge-domain', False),
                ]),
            _MetaInfoClassMember('pw-class-template', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to a pseudowire template
                ''',
                'pw_class_template',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('vc-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire VC ID
                ''',
                'vc_id',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'backup',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec',
            False, 
            [
            _MetaInfoClassMember('neighbor-ip-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                IPv4 or IPv6 address of the neighbor.
                ''',
                'neighbor_ip_address',
                'cisco-bridge-domain', True, [
                    _MetaInfoClassMember('neighbor-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 or IPv6 address of the neighbor.
                        ''',
                        'neighbor_ip_address',
                        'cisco-bridge-domain', True),
                    _MetaInfoClassMember('neighbor-ip-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        IPv4 or IPv6 address of the neighbor.
                        ''',
                        'neighbor_ip_address',
                        'cisco-bridge-domain', True),
                ]),
            _MetaInfoClassMember('vc-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Pseudowire VC ID
                ''',
                'vc_id',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('backup', REFERENCE_CLASS, 'Backup' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup', 
                [], [], 
                '''                Backup pseudo-wire.
                ''',
                'backup',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('dhcp-ipv4-snooping', REFERENCE_CLASS, 'DhcpIpv4Snooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping', 
                [], [], 
                '''                Enable DHCP IPv4 snooping.
                ''',
                'dhcp_ipv4_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('encap-type', REFERENCE_IDENTITY_CLASS, 'PwEncapsulationTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_pw', 'PwEncapsulationTypeIdentity', 
                [], [], 
                '''                Encapsulation configuration for this neighbor
                ''',
                'encap_type',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('flooding', REFERENCE_CLASS, 'Flooding' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding', 
                [], [], 
                '''                Flooding configurations.
                ''',
                'flooding',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('igmp-snooping', REFERENCE_CLASS, 'IgmpSnooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping', 
                [], [], 
                '''                Enable IGMP snooping.
                ''',
                'igmp_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac', 
                [], [], 
                '''                MAC features for bridge domain.
                ''',
                'mac',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mld-snooping', REFERENCE_CLASS, 'MldSnooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping', 
                [], [], 
                '''                Enable MLD snooping
                ''',
                'mld_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('pw-class-template', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to a pseudowire template
                ''',
                'pw_class_template',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('source-ipv6', ATTRIBUTE, 'str' , None, None, 
                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The local source IPv6 address. Note this should only be
                configured when neighbor address is IPv6 type
                ''',
                'source_ipv6',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('split-horizon-group', REFERENCE_CLASS, 'SplitHorizonGroup' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup', 
                [], [], 
                '''                Bridge domain aggregates attachment circuits (ACs) and
                pseudowires (PWs) in one or more groups called Split Horizon
                Groups. When applied to bridge domains, Split Horizon refers
                to the flooding and forwarding behavior between members of a
                Split Horizon group. In general, frames received on one
                member of a split horizon group are not flooded out to the
                other members.
                ''',
                'split_horizon_group',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('static-label', REFERENCE_CLASS, 'StaticLabel' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel', 
                [], [], 
                '''                Statically configured labels, signalling should be none
                ''',
                'static_label',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('storm-control', REFERENCE_CLASS, 'StormControl' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl', 
                [], [], 
                '''                A collection of storm control threshold and action
                configurations.
                ''',
                'storm_control',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('tag-impose-vlan', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                Specify a tag for a VLAN ID for the pseudowire
                ''',
                'tag_impose_vlan',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'pw-neighbor-spec',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember',
            False, 
            [
            _MetaInfoClassMember('access-pw-if-member', REFERENCE_LIST, 'AccessPwIfMember' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember', 
                [], [], 
                '''                List of interface based access pseudowires for
                current bridge-domain.
                ''',
                'access_pw_if_member',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('pw-neighbor-spec', REFERENCE_LIST, 'PwNeighborSpec' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec', 
                [], [], 
                '''                Collection of neighbor specification based
                pseudo-wires.
                ''',
                'pw_neighbor_spec',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'access-pw-member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Members',
            False, 
            [
            _MetaInfoClassMember('ac-member', REFERENCE_LIST, 'AcMember' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember', 
                [], [], 
                '''                List of Attachment circuits for current
                bridge-domain.
                ''',
                'ac_member',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('access-pw-member', REFERENCE_CLASS, 'AccessPwMember' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember', 
                [], [], 
                '''                Collection of access pseudowire members.
                
                A Pseudowires can be a regular interface with ifType
                'ifPwType' or it can represented as a non-interface
                context. This container provides model definition for
                both types of the pseudowires.
                ''',
                'access_pw_member',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('vfi-member', REFERENCE_LIST, 'VfiMember' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember', 
                [], [], 
                '''                List of Virtual Forrwarding Interfaces for current
                bridge-domain.
                ''',
                'vfi_member',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'members',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacLimitActionEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacLimitActionEnum', 
                [], [], 
                '''                MAC limit violation actions.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('maximum', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of mac addresses that can be learnt
                ''',
                'maximum',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('notification', REFERENCE_IDENTITY_CLASS, 'MacLimitNotificationTypeIdentity' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacLimitNotificationTypeIdentity', 
                [], [], 
                '''                MAC limit violation notifications.
                ''',
                'notification',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'limit',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging',
            False, 
            [
            _MetaInfoClassMember('time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The timeout period in seconds for aging out
                dynamically learned forwarding information
                ''',
                'time',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'MacAgingTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacAgingTypeEnum', 
                [], [], 
                '''                MAC aging type.
                ''',
                'type',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'aging',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown',
            False, 
            [
            _MetaInfoClassMember('flush', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable mac table flush when port moves to down
                state.
                ''',
                'flush',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'port-down',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding',
            False, 
            [
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable flooding
                ''',
                'disabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('disabled-unknown-unicast', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable unknown unicast flooding
                ''',
                'disabled_unknown_unicast',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'flooding',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_ENUM_CLASS, 'MacSecureActionEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'MacSecureActionEnum', 
                [], [], 
                '''                MAC secure action for violating packets.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/Disable logging.
                ''',
                'logging',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'secure',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses',
            False, 
            [
            _MetaInfoClassMember('mac-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Static MAC address.
                ''',
                'mac_addr',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('drop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Drop packet.
                ''',
                'drop',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mac-addresses',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static',
            False, 
            [
            _MetaInfoClassMember('mac-addresses', REFERENCE_LIST, 'MacAddresses' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses', 
                [], [], 
                '''                MAC address entry.
                ''',
                'mac_addresses',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'static',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac',
            False, 
            [
            _MetaInfoClassMember('aging', REFERENCE_CLASS, 'Aging' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging', 
                [], [], 
                '''                MAC aging configurations.
                ''',
                'aging',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('flooding', REFERENCE_CLASS, 'Flooding' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding', 
                [], [], 
                '''                Flooding configurations.
                ''',
                'flooding',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('learning-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable disable mac learning
                ''',
                'learning_enabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('limit', REFERENCE_CLASS, 'Limit' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit', 
                [], [], 
                '''                MAC table learning limit.
                ''',
                'limit',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('port-down', REFERENCE_CLASS, 'PortDown' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown', 
                [], [], 
                '''                Port down event
                ''',
                'port_down',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('secure', REFERENCE_CLASS, 'Secure' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure', 
                [], [], 
                '''                MAC secure parameters.
                ''',
                'secure',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('static', REFERENCE_CLASS, 'Static' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static', 
                [], [], 
                '''                Static mac address list parameters.
                ''',
                'static',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mac',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation',
            False, 
            [
            _MetaInfoClassMember('dst-mac', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match Destination MAC Address
                ''',
                'dst_mac',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('ipv4', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match IPv4 Address
                ''',
                'ipv4',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('src-mac', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Match Source MAC Address
                ''',
                'src_mac',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'address-validation',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection',
            False, 
            [
            _MetaInfoClassMember('address-validation', REFERENCE_CLASS, 'AddressValidation' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation', 
                [], [], 
                '''                Enable address validation.
                ''',
                'address_validation',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable DAI logging
                ''',
                'logging',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'dynamic-arp-inspection',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard',
            False, 
            [
            _MetaInfoClassMember('logging', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable IPSG logging
                ''',
                'logging',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'ip-source-guard',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds.UnitEnum' : _MetaInfoEnum('UnitEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_domain',
        {
            'bps':'bps',
            'kbps':'kbps',
            'pps':'pps',
        }, 'cisco-storm-control', _yang_ns._namespaces['cisco-storm-control']),
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds',
            False, 
            [
            _MetaInfoClassMember('traffic-class', REFERENCE_ENUM_CLASS, 'EthTrafficClassEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'EthTrafficClassEnum', 
                [], [], 
                '''                This leaf identifies a ethernet traffic type for
                which an administrator desires to configure storm
                control.
                ''',
                'traffic_class',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('unit', REFERENCE_ENUM_CLASS, 'UnitEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds.UnitEnum', 
                [], [], 
                '''                This enumeration define unit of the traffic threshold
                value.
                ''',
                'unit',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Traffic threshold value. Unit of the value is indicated by
                leaf 'unit'.
                ''',
                'value',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'thresholds',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl',
            False, 
            [
            _MetaInfoClassMember('action', REFERENCE_IDENTITY_CLASS, 'StormControlActionIdentity' , 'ydk.models.cisco_ios_xe.cisco_storm_control', 'StormControlActionIdentity', 
                [], [], 
                '''                This leaf represents the storm control action taken when
                the traffic of a particular type exceeds the configured
                threshold values.
                ''',
                'action',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('thresholds', REFERENCE_LIST, 'Thresholds' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds', 
                [], [], 
                '''                A collection of storm control threshold configuration
                entries.
                ''',
                'thresholds',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'storm-control',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping',
            False, 
            [
            _MetaInfoClassMember('disabled', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable IGMP snooping.
                ''',
                'disabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IGMP snooping profile name
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'igmp-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MLD snooping profile name.
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mld-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping',
            False, 
            [
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                DHCPv4 snooping profile name
                ''',
                'profile_name',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'dhcp-ipv4-snooping',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains.BridgeDomain.FloodingModeEnum' : _MetaInfoEnum('FloodingModeEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_domain',
        {
            'convergence-optimized':'convergence_optimized',
            'resilience-optimized':'resilience_optimized',
        }, 'cisco-bridge-domain', _yang_ns._namespaces['cisco-bridge-domain']),
    'BridgeDomainConfig.BridgeDomains.BridgeDomain' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains.BridgeDomain',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name or number
                ''',
                'id',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('bd-status-change-notification', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Enable/disable bridge-domain status change notification.
                
                If true, any change in bridge-domain operational status
                will be notified to client via 'bd-status-change'
                notification.
                ''',
                'bd_status_change_notification',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('bridge-group', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Reference to bridge-group name. If bridge-groups are
                supported, referred bridge-group MUST be created
                first.
                ''',
                'bridge_group',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('dhcp-ipv4-snooping', REFERENCE_CLASS, 'DhcpIpv4Snooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping', 
                [], [], 
                '''                Enable DHCP IPv4 snooping.
                ''',
                'dhcp_ipv4_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('dynamic-arp-inspection', REFERENCE_CLASS, 'DynamicArpInspection' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection', 
                [], [], 
                '''                Dynamic ARP Inspection (DAI) configurations.
                ''',
                'dynamic_arp_inspection',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf represents configured admin status of the
                bridge domain
                ''',
                'enabled',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('flooding-mode', REFERENCE_ENUM_CLASS, 'FloodingModeEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.FloodingModeEnum', 
                [], [], 
                '''                Flood modes for optimization.
                ''',
                'flooding_mode',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('igmp-snooping', REFERENCE_CLASS, 'IgmpSnooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping', 
                [], [], 
                '''                Enable IGMP snooping.
                ''',
                'igmp_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('ip-source-guard', REFERENCE_CLASS, 'IpSourceGuard' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard', 
                [], [], 
                '''                IP source guard (IPSG) configurations.
                ''',
                'ip_source_guard',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mac', REFERENCE_CLASS, 'Mac' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac', 
                [], [], 
                '''                MAC features for bridge domain.
                ''',
                'mac',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('members', REFERENCE_CLASS, 'Members' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.Members', 
                [], [], 
                '''                Collection of bridge-domain members.
                ''',
                'members',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mld-snooping', REFERENCE_CLASS, 'MldSnooping' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping', 
                [], [], 
                '''                Enable MLD snooping
                ''',
                'mld_snooping',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('46', '65535')], [], 
                '''                The MTU size for bridge domain. All bridge domain
                members must have same MTU size to be operational
                in the domain
                ''',
                'mtu',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('storm-control', REFERENCE_CLASS, 'StormControl' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl', 
                [], [], 
                '''                A collection of storm control threshold and action
                configurations.
                ''',
                'storm_control',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-domain',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig.BridgeDomains' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig.BridgeDomains',
            False, 
            [
            _MetaInfoClassMember('bridge-domain', REFERENCE_LIST, 'BridgeDomain' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains.BridgeDomain', 
                [], [], 
                '''                Definition of a bridge-domain.
                ''',
                'bridge_domain',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-domains',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainConfig' : {
        'meta_info' : _MetaInfoClass('BridgeDomainConfig',
            False, 
            [
            _MetaInfoClassMember('bridge-domains', REFERENCE_CLASS, 'BridgeDomains' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeDomains', 
                [], [], 
                '''                Collection of bridge domains.
                ''',
                'bridge_domains',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('bridge-groups', REFERENCE_CLASS, 'BridgeGroups' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.BridgeGroups', 
                [], [], 
                '''                Collection of bridge-groups.
                
                A Bridge-group is logical grouping construct for bridge
                domains. It defines grouping of bridge-domains under a
                named bridge-group. For example all bridge-domains
                belonging to a single customer can be grouped under a bridge
                -group
                ''',
                'bridge_groups',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('global', REFERENCE_CLASS, 'Global_' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainConfig.Global_', 
                [], [], 
                '''                Global configurations for bridge-domains.
                ''',
                'global_',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-domain-config',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.SystemCapabilities' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.SystemCapabilities',
            False, 
            [
            _MetaInfoClassMember('max-ac-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of attachment circuits per
                bridge-domains.
                ''',
                'max_ac_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of bridge-domains suported.
                ''',
                'max_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-interflex-if-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of Interflex interfaces per
                bridge-domains.
                ''',
                'max_interflex_if_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-pw-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of access pseudowires per
                bridge-domains
                ''',
                'max_pw_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-sh-group-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of Split Horizon groups per
                bridge-domains.
                ''',
                'max_sh_group_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-vfi-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of virtual forwarding instances per
                bridge-domains.
                ''',
                'max_vfi_per_bd',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'system-capabilities',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.ModuleCapabilities.Modules' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.ModuleCapabilities.Modules',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the hardware module such as linecards, for
                which capability is described.
                ''',
                'name',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('max-ac-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of attachment circuits per
                bridge-domains.
                ''',
                'max_ac_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of bridge-domains suported.
                ''',
                'max_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-mac-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of MAC addresses per bridge-domains
                supported by this module.
                ''',
                'max_mac_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-pdd-edge-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of PBB Edge type bridge-domains
                supported by this module.
                ''',
                'max_pdd_edge_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-pw-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of access pseudowires per
                bridge-domains
                ''',
                'max_pw_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-sh-group-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of Split Horizon groups per
                bridge-domains.
                ''',
                'max_sh_group_per_bd',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('max-vfi-per-bd', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum number of virtual forwarding instances per
                bridge-domains.
                ''',
                'max_vfi_per_bd',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'modules',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.ModuleCapabilities' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.ModuleCapabilities',
            False, 
            [
            _MetaInfoClassMember('modules', REFERENCE_LIST, 'Modules' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.ModuleCapabilities.Modules', 
                [], [], 
                '''                Collection of capabillity statements for hardware
                module in the system.
                ''',
                'modules',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'module-capabilities',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats',
            False, 
            [
            _MetaInfoClassMember('byte-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes dropped by interface due to DAI
                actions.
                ''',
                'byte_drops',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('packet-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets dropped by interface due to DAI
                actions.
                ''',
                'packet_drops',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'dai-stats',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats',
            False, 
            [
            _MetaInfoClassMember('byte-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes dropped by interface due to IPSG
                actions.
                ''',
                'byte_drops',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('packet-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets dropped by interface due to IPSG
                actions.
                ''',
                'packet_drops',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'ipsg-stats',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter',
            False, 
            [
            _MetaInfoClassMember('traffic-class', REFERENCE_ENUM_CLASS, 'EthTrafficClassEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'EthTrafficClassEnum', 
                [], [], 
                '''                Ethernet traffic class i.e. broadcast, multicast or
                unknown unicast.
                ''',
                'traffic_class',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('octate-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of bytes of traffic dropped due to
                storm control violations.
                ''',
                'octate_drops',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('packet-drops', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The total number of dropped packets due to storm
                control violations.
                ''',
                'packet_drops',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'drop-counter',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl',
            False, 
            [
            _MetaInfoClassMember('drop-counter', REFERENCE_LIST, 'DropCounter' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter', 
                [], [], 
                '''                Collection of packet drop statistics for ethernet traffic
                clasess.
                ''',
                'drop_counter',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'storm-control',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an instance of Bridge domain attachment
                circuit (AC) interface name.
                ''',
                'interface',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('dai-stats', REFERENCE_CLASS, 'DaiStats' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats', 
                [], [], 
                '''                Dynamic ARP Inspection (DAI) statistics.
                ''',
                'dai_stats',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('ipsg-stats', REFERENCE_CLASS, 'IpsgStats' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats', 
                [], [], 
                '''                IPSG stats.
                ''',
                'ipsg_stats',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('static-mac-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of static MAC address configured on this
                bridge-domain member interface.
                ''',
                'static_mac_count',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('storm-control', REFERENCE_CLASS, 'StormControl' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl', 
                [], [], 
                '''                Storm control statistics.
                ''',
                'storm_control',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'ac-member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status',
            False, 
            [
            _MetaInfoClassMember('traffic-class', REFERENCE_ENUM_CLASS, 'EthTrafficClassEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'EthTrafficClassEnum', 
                [], [], 
                '''                This leaf identifies a ethernet traffic type.
                ''',
                'traffic_class',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates if flooding is enabled for
                corresponding traffic class
                ''',
                'enabled',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'status',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding',
            False, 
            [
            _MetaInfoClassMember('status', REFERENCE_LIST, 'Status' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status', 
                [], [], 
                '''                A collection of storm control threshold configuration
                entries.
                ''',
                'status',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'flooding',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain memeber interface name.
                ''',
                'interface',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('flooding', REFERENCE_CLASS, 'Flooding' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding', 
                [], [], 
                '''                Flooding operational status
                ''',
                'flooding',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'vfi-member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status',
            False, 
            [
            _MetaInfoClassMember('traffic-class', REFERENCE_ENUM_CLASS, 'EthTrafficClassEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_common', 'EthTrafficClassEnum', 
                [], [], 
                '''                This leaf identifies a ethernet traffic type.
                ''',
                'traffic_class',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates if flooding is enabled for
                corresponding traffic class
                ''',
                'enabled',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'status',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding',
            False, 
            [
            _MetaInfoClassMember('status', REFERENCE_LIST, 'Status' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status', 
                [], [], 
                '''                A collection of storm control threshold configuration
                entries.
                ''',
                'status',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'flooding',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember',
            False, 
            [
            _MetaInfoClassMember('vc-peer-address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Reference to peer ip address of a pseudowire instance.
                ''',
                'vc_peer_address',
                'cisco-bridge-domain', True, [
                    _MetaInfoClassMember('vc-peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Reference to peer ip address of a pseudowire instance.
                        ''',
                        'vc_peer_address',
                        'cisco-bridge-domain', True),
                    _MetaInfoClassMember('vc-peer-address', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Reference to peer ip address of a pseudowire instance.
                        ''',
                        'vc_peer_address',
                        'cisco-bridge-domain', True),
                ]),
            _MetaInfoClassMember('vc-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reference to vc-id of a pseudowire instance.
                ''',
                'vc_id',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('flooding', REFERENCE_CLASS, 'Flooding' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding', 
                [], [], 
                '''                Flooding operational status
                ''',
                'flooding',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'access-pw-member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain.Members' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain.Members',
            False, 
            [
            _MetaInfoClassMember('ac-member', REFERENCE_LIST, 'AcMember' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember', 
                [], [], 
                '''                List of attachment circuits for this bridge domains
                ''',
                'ac_member',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('access-pw-member', REFERENCE_LIST, 'AccessPwMember' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember', 
                [], [], 
                '''                Collection of access pseudowire members of the bridge
                domain.
                ''',
                'access_pw_member',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('vfi-member', REFERENCE_LIST, 'VfiMember' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember', 
                [], [], 
                '''                Reference to an instance of Bridge domain Virtual
                Forwarding Instance (VFI) name.
                ''',
                'vfi_member',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'members',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains.BridgeDomain' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains.BridgeDomain',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge domain name or number
                ''',
                'id',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('bd-state', REFERENCE_ENUM_CLASS, 'BridgeDomainStateTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainStateTypeEnum', 
                [], [], 
                '''                Bridge domain operational/admin status.
                ''',
                'bd_state',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('create-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                System time when this bridge-domain was created
                ''',
                'create_time',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('last-status-change', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of consecutive ticks since bridge-domain status
                was changed last time.
                ''',
                'last_status_change',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mac-limit-reached', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This leaf indicates if MAC address limit has been
                reached.
                ''',
                'mac_limit_reached',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('members', REFERENCE_CLASS, 'Members' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain.Members', 
                [], [], 
                '''                Collection of bridge-domain members.
                ''',
                'members',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('p2mp-pw-disabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Point to Mutipoint pseudowire state
                ''',
                'p2mp_pw_disabled',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-domain',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.BridgeDomains' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.BridgeDomains',
            False, 
            [
            _MetaInfoClassMember('bridge-domain', REFERENCE_LIST, 'BridgeDomain' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains.BridgeDomain', 
                [], [], 
                '''                Collection of bridge-domain state data.
                ''',
                'bridge_domain',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-domains',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState.MacTable.MacTypeEnum' : _MetaInfoEnum('MacTypeEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_domain',
        {
            'static':'static',
            'dynamic':'dynamic',
        }, 'cisco-bridge-domain', _yang_ns._namespaces['cisco-bridge-domain']),
    'BridgeDomainState.MacTable' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState.MacTable',
            False, 
            [
            _MetaInfoClassMember('bd-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge-domain name where MAC entry is learnt.
                ''',
                'bd_id',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address.
                ''',
                'mac_address',
                'cisco-bridge-domain', True),
            _MetaInfoClassMember('age', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time since mac address was learnt on the interface.
                ''',
                'age',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an interface instance where MAC 
                address is learnt.
                ''',
                'interface',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard / Module where mac address was learnt.
                ''',
                'location',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mac-type', REFERENCE_ENUM_CLASS, 'MacTypeEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.MacTable.MacTypeEnum', 
                [], [], 
                '''                MAC address type.
                ''',
                'mac_type',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('ntfy-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TBD ?NTFY?
                ''',
                'ntfy_mac',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('secure-mac', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Secure MAC address.
                ''',
                'secure_mac',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'mac-table',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'BridgeDomainState' : {
        'meta_info' : _MetaInfoClass('BridgeDomainState',
            False, 
            [
            _MetaInfoClassMember('bridge-domains', REFERENCE_CLASS, 'BridgeDomains' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.BridgeDomains', 
                [], [], 
                '''                Bridge domain state data.
                ''',
                'bridge_domains',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mac-table', REFERENCE_LIST, 'MacTable' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.MacTable', 
                [], [], 
                '''                This list contains mac-address entries for bridge
                domains.
                ''',
                'mac_table',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('module-capabilities', REFERENCE_CLASS, 'ModuleCapabilities' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.ModuleCapabilities', 
                [], [], 
                '''                This container defines module capabilities for bridge
                domain.
                ''',
                'module_capabilities',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('system-capabilities', REFERENCE_CLASS, 'SystemCapabilities' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'BridgeDomainState.SystemCapabilities', 
                [], [], 
                '''                This container defines system capabilities for bridge
                domain.
                ''',
                'system_capabilities',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-domain-state',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'ClearBridgeDomainRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearBridgeDomainRpc.Input',
            False, 
            [
            _MetaInfoClassMember('all', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Clear all bridge-domains configured on the device.
                ''',
                'all',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('bd-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Clear a single bridge-domain
                ''',
                'bd_id',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('bg-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Clears all bridge-domains under this bridge-group.
                ''',
                'bg_id',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'input',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'ClearBridgeDomainRpc.Output' : {
        'meta_info' : _MetaInfoClass('ClearBridgeDomainRpc.Output',
            False, 
            [
            _MetaInfoClassMember('errstr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error message from the device if RPC failed.
                ''',
                'errstr',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'output',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'ClearBridgeDomainRpc' : {
        'meta_info' : _MetaInfoClass('ClearBridgeDomainRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'ClearBridgeDomainRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'ClearBridgeDomainRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'clear-bridge-domain',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'ClearMacAddressRpc.Input.BridgeDomain' : {
        'meta_info' : _MetaInfoClass('ClearMacAddressRpc.Input.BridgeDomain',
            False, 
            [
            _MetaInfoClassMember('bd-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge-domain identifier, clear all mac-address entries
                dynamically learnt on this bridge-domain
                ''',
                'bd_id',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('bg-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bridge-group identifier, clear all mac-address entries
                from all bridge-domains under this bridge-group.
                ''',
                'bg_id',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'bridge-domain',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'ClearMacAddressRpc.Input' : {
        'meta_info' : _MetaInfoClass('ClearMacAddressRpc.Input',
            False, 
            [
            _MetaInfoClassMember('bridge-domain', REFERENCE_CLASS, 'BridgeDomain' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'ClearMacAddressRpc.Input.BridgeDomain', 
                [], [], 
                '''                Clear mac-address entries for given bridge-domain(s).
                ''',
                'bridge_domain',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an interface. Clear mac-addesses learnt by
                by this interface.
                ''',
                'interface',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Clear a specific mac-address entry from the mac-table.
                ''',
                'mac_address',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'input',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'ClearMacAddressRpc.Output' : {
        'meta_info' : _MetaInfoClass('ClearMacAddressRpc.Output',
            False, 
            [
            _MetaInfoClassMember('errstr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error message from the device if RPC failed.
                ''',
                'errstr',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'output',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'ClearMacAddressRpc' : {
        'meta_info' : _MetaInfoClass('ClearMacAddressRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'ClearMacAddressRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'ClearMacAddressRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'clear-mac-address',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'CreateParameterizedBridgeDomainsRpc.Input.Member' : {
        'meta_info' : _MetaInfoClass('CreateParameterizedBridgeDomainsRpc.Input.Member',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an interface instance which is
                configured to be part of this bridge domain
                ''',
                'interface',
                'cisco-bridge-domain', True),
            ],
            'cisco-bridge-domain',
            'member',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'CreateParameterizedBridgeDomainsRpc.Input.ParameterEnum' : _MetaInfoEnum('ParameterEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_domain',
        {
            'vlan':'vlan',
        }, 'cisco-bridge-domain', _yang_ns._namespaces['cisco-bridge-domain']),
    'CreateParameterizedBridgeDomainsRpc.Input' : {
        'meta_info' : _MetaInfoClass('CreateParameterizedBridgeDomainsRpc.Input',
            False, 
            [
            _MetaInfoClassMember('parameter', REFERENCE_ENUM_CLASS, 'ParameterEnum' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'CreateParameterizedBridgeDomainsRpc.Input.ParameterEnum', 
                [], [], 
                '''                Parameter for automatic bridge domain creation.
                ''',
                'parameter',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('member', REFERENCE_LIST, 'Member' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'CreateParameterizedBridgeDomainsRpc.Input.Member', 
                [], [], 
                '''                Bridge-domain member interface.
                ''',
                'member',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'input',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'CreateParameterizedBridgeDomainsRpc.Output' : {
        'meta_info' : _MetaInfoClass('CreateParameterizedBridgeDomainsRpc.Output',
            False, 
            [
            _MetaInfoClassMember('errstr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Error message from the device if RPC failed.
                ''',
                'errstr',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'output',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
    'CreateParameterizedBridgeDomainsRpc' : {
        'meta_info' : _MetaInfoClass('CreateParameterizedBridgeDomainsRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'CreateParameterizedBridgeDomainsRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'cisco-bridge-domain', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.cisco_ios_xe.cisco_bridge_domain', 'CreateParameterizedBridgeDomainsRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'cisco-bridge-domain', False),
            ],
            'cisco-bridge-domain',
            'create-parameterized-bridge-domains',
            _yang_ns._namespaces['cisco-bridge-domain'],
        'ydk.models.cisco_ios_xe.cisco_bridge_domain'
        ),
    },
}
_meta_table['BridgeDomainConfig.Global_.Pbb']['meta_info'].parent =_meta_table['BridgeDomainConfig.Global_']['meta_info']
_meta_table['BridgeDomainConfig.BridgeGroups.BridgeGroup']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeGroups']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Limit']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Aging']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.PortDown']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac.Secure']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.Thresholds']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection.AddressValidation']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.SplitHorizonGroup']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Mac']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IgmpSnooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.MldSnooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DhcpIpv4Snooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.Flooding']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.StormControl']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.DynamicArpInspection']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember.IpSourceGuard']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Limit']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Aging']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.PortDown']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac.Secure']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl.Thresholds']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StaticLabel']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.SplitHorizonGroup']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Mac']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.IgmpSnooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.MldSnooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.DhcpIpv4Snooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Flooding']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.StormControl']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec.Backup']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.AccessPwIfMember']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember.PwNeighborSpec']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.VfiMember']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members.AccessPwMember']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static.MacAddresses']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Limit']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Aging']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.PortDown']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Flooding']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Secure']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac.Static']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection.AddressValidation']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl.Thresholds']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Members']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.Mac']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.DynamicArpInspection']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.IpSourceGuard']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.StormControl']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.IgmpSnooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.MldSnooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain.DhcpIpv4Snooping']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains.BridgeDomain']['meta_info'].parent =_meta_table['BridgeDomainConfig.BridgeDomains']['meta_info']
_meta_table['BridgeDomainConfig.Global_']['meta_info'].parent =_meta_table['BridgeDomainConfig']['meta_info']
_meta_table['BridgeDomainConfig.BridgeGroups']['meta_info'].parent =_meta_table['BridgeDomainConfig']['meta_info']
_meta_table['BridgeDomainConfig.BridgeDomains']['meta_info'].parent =_meta_table['BridgeDomainConfig']['meta_info']
_meta_table['BridgeDomainState.ModuleCapabilities.Modules']['meta_info'].parent =_meta_table['BridgeDomainState.ModuleCapabilities']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl.DropCounter']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.DaiStats']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.IpsgStats']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember.StormControl']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding.Status']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember.Flooding']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding.Status']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember.Flooding']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AcMember']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.VfiMember']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members.AccessPwMember']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain.Members']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains.BridgeDomain']['meta_info'].parent =_meta_table['BridgeDomainState.BridgeDomains']['meta_info']
_meta_table['BridgeDomainState.SystemCapabilities']['meta_info'].parent =_meta_table['BridgeDomainState']['meta_info']
_meta_table['BridgeDomainState.ModuleCapabilities']['meta_info'].parent =_meta_table['BridgeDomainState']['meta_info']
_meta_table['BridgeDomainState.BridgeDomains']['meta_info'].parent =_meta_table['BridgeDomainState']['meta_info']
_meta_table['BridgeDomainState.MacTable']['meta_info'].parent =_meta_table['BridgeDomainState']['meta_info']
_meta_table['ClearBridgeDomainRpc.Input']['meta_info'].parent =_meta_table['ClearBridgeDomainRpc']['meta_info']
_meta_table['ClearBridgeDomainRpc.Output']['meta_info'].parent =_meta_table['ClearBridgeDomainRpc']['meta_info']
_meta_table['ClearMacAddressRpc.Input.BridgeDomain']['meta_info'].parent =_meta_table['ClearMacAddressRpc.Input']['meta_info']
_meta_table['ClearMacAddressRpc.Input']['meta_info'].parent =_meta_table['ClearMacAddressRpc']['meta_info']
_meta_table['ClearMacAddressRpc.Output']['meta_info'].parent =_meta_table['ClearMacAddressRpc']['meta_info']
_meta_table['CreateParameterizedBridgeDomainsRpc.Input.Member']['meta_info'].parent =_meta_table['CreateParameterizedBridgeDomainsRpc.Input']['meta_info']
_meta_table['CreateParameterizedBridgeDomainsRpc.Input']['meta_info'].parent =_meta_table['CreateParameterizedBridgeDomainsRpc']['meta_info']
_meta_table['CreateParameterizedBridgeDomainsRpc.Output']['meta_info'].parent =_meta_table['CreateParameterizedBridgeDomainsRpc']['meta_info']
