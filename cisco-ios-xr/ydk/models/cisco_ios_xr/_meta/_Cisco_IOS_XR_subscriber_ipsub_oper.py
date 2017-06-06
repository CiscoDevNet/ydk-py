


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'IpsubMaParentIntfStateDataEnum' : _MetaInfoEnum('IpsubMaParentIntfStateDataEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper',
        {
            'deleted':'deleted',
            'down':'down',
            'up':'up',
        }, 'Cisco-IOS-XR-subscriber-ipsub-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper']),
    'IpsubMaIntfStateDataEnum' : _MetaInfoEnum('IpsubMaIntfStateDataEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper',
        {
            'invalid':'invalid',
            'initialized':'initialized',
            'session-creation-started':'session_creation_started',
            'control-policy-executing':'control_policy_executing',
            'control-policy-executed':'control_policy_executed',
            'session-features-applied':'session_features_applied',
            'vrf-configured':'vrf_configured',
            'adding-adjacency':'adding_adjacency',
            'adjacency-added':'adjacency_added',
            'up':'up',
            'down':'down',
            'address-family-down':'address_family_down',
            'address-family-down-complete':'address_family_down_complete',
            'disconnecting':'disconnecting',
            'disconnected':'disconnected',
            'error':'error',
        }, 'Cisco-IOS-XR-subscriber-ipsub-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper']),
    'IpsubMaParentIntfVlanEnum' : _MetaInfoEnum('IpsubMaParentIntfVlanEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper',
        {
            'plain':'plain',
            'ambiguous':'ambiguous',
        }, 'Cisco-IOS-XR-subscriber-ipsub-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper']),
    'IpsubMaIntfInitiatorDataEnum' : _MetaInfoEnum('IpsubMaIntfInitiatorDataEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper',
        {
            'dhcp':'dhcp',
            'packet-trigger':'packet_trigger',
            'invalid-trigger':'invalid_trigger',
        }, 'Cisco-IOS-XR-subscriber-ipsub-oper', _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper']),
    'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'packet-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators',
            False, 
            [
            _MetaInfoClassMember('dhcp', REFERENCE_CLASS, 'Dhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp', 
                [], [], 
                '''                DHCP summary statistics
                ''',
                'dhcp',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('packet-trigger', REFERENCE_CLASS, 'PacketTrigger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger', 
                [], [], 
                '''                Packet trigger summary statistics
                ''',
                'packet_trigger',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'initiators',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'packet-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators',
            False, 
            [
            _MetaInfoClassMember('dhcp', REFERENCE_CLASS, 'Dhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp', 
                [], [], 
                '''                DHCP summary statistics
                ''',
                'dhcp',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('packet-trigger', REFERENCE_CLASS, 'PacketTrigger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger', 
                [], [], 
                '''                Packet trigger summary statistics
                ''',
                'packet_trigger',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'ipv6-initiators',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary',
            False, 
            [
            _MetaInfoClassMember('initiators', REFERENCE_CLASS, 'Initiators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators', 
                [], [], 
                '''                Summary counts per initiator
                ''',
                'initiators',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of interfaces with subscriber
                configuration
                ''',
                'interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-initiators', REFERENCE_CLASS, 'Ipv6Initiators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators', 
                [], [], 
                '''                Summary counts per initiator for ipv6 session
                ''',
                'ipv6_initiators',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'access-interface-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp',
            False, 
            [
            _MetaInfoClassMember('adding-adjacency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adding adjacency
                ''',
                'adding_adjacency',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('adjacency-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjacency added
                ''',
                'adjacency_added',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executed
                ''',
                'control_policy_executed',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executing', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executing
                ''',
                'control_policy_executing',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnected
                ''',
                'disconnected',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnecting', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnecting
                ''',
                'disconnecting',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Down
                ''',
                'down',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Error
                ''',
                'error',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('initialized', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initialized
                ''',
                'initialized',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid
                ''',
                'invalid',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-creation-started', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session creation started
                ''',
                'session_creation_started',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-features-applied', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session features applied
                ''',
                'session_features_applied',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('total-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces in all states
                ''',
                'total_interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up
                ''',
                'up',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf-configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF configured
                ''',
                'vrf_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger',
            False, 
            [
            _MetaInfoClassMember('adding-adjacency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adding adjacency
                ''',
                'adding_adjacency',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('adjacency-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjacency added
                ''',
                'adjacency_added',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executed
                ''',
                'control_policy_executed',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executing', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executing
                ''',
                'control_policy_executing',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnected
                ''',
                'disconnected',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnecting', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnecting
                ''',
                'disconnecting',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Down
                ''',
                'down',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Error
                ''',
                'error',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('initialized', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initialized
                ''',
                'initialized',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid
                ''',
                'invalid',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-creation-started', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session creation started
                ''',
                'session_creation_started',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-features-applied', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session features applied
                ''',
                'session_features_applied',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('total-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces in all states
                ''',
                'total_interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up
                ''',
                'up',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf-configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF configured
                ''',
                'vrf_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'packet-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators',
            False, 
            [
            _MetaInfoClassMember('dhcp', REFERENCE_CLASS, 'Dhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp', 
                [], [], 
                '''                DHCP
                ''',
                'dhcp',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('packet-trigger', REFERENCE_CLASS, 'PacketTrigger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger', 
                [], [], 
                '''                Packet trigger
                ''',
                'packet_trigger',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'initiators',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp',
            False, 
            [
            _MetaInfoClassMember('adding-adjacency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adding adjacency
                ''',
                'adding_adjacency',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('adjacency-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjacency added
                ''',
                'adjacency_added',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executed
                ''',
                'control_policy_executed',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executing', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executing
                ''',
                'control_policy_executing',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnected
                ''',
                'disconnected',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnecting', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnecting
                ''',
                'disconnecting',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Down
                ''',
                'down',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Error
                ''',
                'error',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('initialized', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initialized
                ''',
                'initialized',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid
                ''',
                'invalid',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-creation-started', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session creation started
                ''',
                'session_creation_started',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-features-applied', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session features applied
                ''',
                'session_features_applied',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('total-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces in all states
                ''',
                'total_interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up
                ''',
                'up',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf-configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF configured
                ''',
                'vrf_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger',
            False, 
            [
            _MetaInfoClassMember('adding-adjacency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adding adjacency
                ''',
                'adding_adjacency',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('adjacency-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Adjacency added
                ''',
                'adjacency_added',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executed
                ''',
                'control_policy_executed',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('control-policy-executing', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Control policy executing
                ''',
                'control_policy_executing',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnected
                ''',
                'disconnected',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('disconnecting', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disconnecting
                ''',
                'disconnecting',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Down
                ''',
                'down',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('error', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Error
                ''',
                'error',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('initialized', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Initialized
                ''',
                'initialized',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('invalid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Invalid
                ''',
                'invalid',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-creation-started', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session creation started
                ''',
                'session_creation_started',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-features-applied', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Session features applied
                ''',
                'session_features_applied',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('total-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of interfaces in all states
                ''',
                'total_interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Up
                ''',
                'up',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf-configured', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VRF configured
                ''',
                'vrf_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'packet-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators',
            False, 
            [
            _MetaInfoClassMember('dhcp', REFERENCE_CLASS, 'Dhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp', 
                [], [], 
                '''                DHCP
                ''',
                'dhcp',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('packet-trigger', REFERENCE_CLASS, 'PacketTrigger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger', 
                [], [], 
                '''                Packet trigger
                ''',
                'packet_trigger',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'ipv6-initiators',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.InterfaceCounts' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.InterfaceCounts',
            False, 
            [
            _MetaInfoClassMember('initiators', REFERENCE_CLASS, 'Initiators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators', 
                [], [], 
                '''                Initiators
                ''',
                'initiators',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-initiators', REFERENCE_CLASS, 'Ipv6Initiators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators', 
                [], [], 
                '''                IPv6 Initiators
                ''',
                'ipv6_initiators',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'interface-counts',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary.Vrf' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary.Vrf',
            False, 
            [
            _MetaInfoClassMember('interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of IP subscriber interfaces in the VRF
                table
                ''',
                'interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-interfaces', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of IPv6 subscriber interfaces in the VRF
                table
                ''',
                'ipv6_interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv6 VRF
                ''',
                'ipv6vrf_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv4 VRF
                ''',
                'vrf_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('access-interface-summary', REFERENCE_CLASS, 'AccessInterfaceSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary', 
                [], [], 
                '''                Access interface summary statistics
                ''',
                'access_interface_summary',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('interface-counts', REFERENCE_CLASS, 'InterfaceCounts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.InterfaceCounts', 
                [], [], 
                '''                Initiator interface counts
                ''',
                'interface_counts',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf', REFERENCE_LIST, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary.Vrf', 
                [], [], 
                '''                Array of VRFs with IPSUB interfaces
                ''',
                'vrf',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf',
            False, 
            [
            _MetaInfoClassMember('table-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Table
                ''',
                'table_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf',
            False, 
            [
            _MetaInfoClassMember('table-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Table
                ''',
                'table_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VRF name
                ''',
                'vrf_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'ipv6vrf',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', True),
            _MetaInfoClassMember('access-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Access interface through which this subscriber
                is accessible
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('age', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Age in hh:mm:ss format
                ''',
                'age',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('current-change-age', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Current change age in hh:mm:ss format
                ''',
                'current_change_age',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('initiator', REFERENCE_ENUM_CLASS, 'IpsubMaIntfInitiatorDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaIntfInitiatorDataEnum', 
                [], [], 
                '''                Protocol trigger for creation of this subscriber
                session
                ''',
                'initiator',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('interface-creation-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface creation time in month day hh:mm:ss
                format
                ''',
                'interface_creation_time',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-current-change-age', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPV6 Current change age in hh:mm:ss format
                ''',
                'ipv6_current_change_age',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-initiator', REFERENCE_ENUM_CLASS, 'IpsubMaIntfInitiatorDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaIntfInitiatorDataEnum', 
                [], [], 
                '''                Protocol trigger for creation of this
                subscriber's IPv6 session
                ''',
                'ipv6_initiator',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-last-state-change-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface's IPV6 last state change time in month
                day hh:mm:ss format
                ''',
                'ipv6_last_state_change_time',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-old-state', REFERENCE_ENUM_CLASS, 'IpsubMaIntfStateDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaIntfStateDataEnum', 
                [], [], 
                '''                Previous state of the subscriber's IPv6 session
                ''',
                'ipv6_old_state',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-state', REFERENCE_ENUM_CLASS, 'IpsubMaIntfStateDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaIntfStateDataEnum', 
                [], [], 
                '''                State of the subscriber's IPv6 session
                ''',
                'ipv6_state',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6vrf', REFERENCE_CLASS, 'Ipv6Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf', 
                [], [], 
                '''                IPv6 VRF details
                ''',
                'ipv6vrf',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('is-l2-connected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if L2 connected
                ''',
                'is_l2_connected',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('last-state-change-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface's last state change time in month day
                hh:mm:ss format
                ''',
                'last_state_change_time',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('old-state', REFERENCE_ENUM_CLASS, 'IpsubMaIntfStateDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaIntfStateDataEnum', 
                [], [], 
                '''                Previous state of the subscriber session
                ''',
                'old_state',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Session Type
                ''',
                'session_type',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IpsubMaIntfStateDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaIntfStateDataEnum', 
                [], [], 
                '''                State of the subscriber session
                ''',
                'state',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('subscriber-ipv4-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 Address of the subscriber
                ''',
                'subscriber_ipv4_address',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('subscriber-ipv6-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IPv6 Address of the subscriber
                ''',
                'subscriber_ipv6_address',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('subscriber-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Subscriber label for this subscriber interface
                ''',
                'subscriber_label',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('subscriber-mac-addres', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address of the subscriber
                ''',
                'subscriber_mac_addres',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vrf', REFERENCE_CLASS, 'Vrf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf', 
                [], [], 
                '''                IPv4 VRF details
                ''',
                'vrf',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                IP subscriber interface entry
                ''',
                'interface',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface that were
                dropped
                ''',
                'fsol_dropped_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped
                ''',
                'fsol_dropped_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-dup-addr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to duplicate source address
                ''',
                'fsol_dropped_packets_dup_addr',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-flow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding creation rate
                ''',
                'fsol_dropped_packets_flow',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-session-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding one or more of the
                configured session limits
                ''',
                'fsol_dropped_packets_session_limit',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ture if the initiator is configred
                ''',
                'is_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions currently up for each
                initiator
                ''',
                'sessions',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('unique-ip-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if check for subscriber address
                uniquenessduring first sign of life is enabled
                ''',
                'unique_ip_check',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface that were
                dropped
                ''',
                'fsol_dropped_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped
                ''',
                'fsol_dropped_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-dup-addr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to duplicate source address
                ''',
                'fsol_dropped_packets_dup_addr',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-flow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding creation rate
                ''',
                'fsol_dropped_packets_flow',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-session-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding one or more of the
                configured session limits
                ''',
                'fsol_dropped_packets_session_limit',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ture if the initiator is configred
                ''',
                'is_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions currently up for each
                initiator
                ''',
                'sessions',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('unique-ip-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if check for subscriber address
                uniquenessduring first sign of life is enabled
                ''',
                'unique_ip_check',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'packet-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators',
            False, 
            [
            _MetaInfoClassMember('dhcp', REFERENCE_CLASS, 'Dhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp', 
                [], [], 
                '''                DHCP information
                ''',
                'dhcp',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('packet-trigger', REFERENCE_CLASS, 'PacketTrigger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger', 
                [], [], 
                '''                packet trigger information
                ''',
                'packet_trigger',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'initiators',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface that were
                dropped
                ''',
                'fsol_dropped_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped
                ''',
                'fsol_dropped_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-dup-addr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to duplicate source address
                ''',
                'fsol_dropped_packets_dup_addr',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-flow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding creation rate
                ''',
                'fsol_dropped_packets_flow',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-session-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding one or more of the
                configured session limits
                ''',
                'fsol_dropped_packets_session_limit',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ture if the initiator is configred
                ''',
                'is_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions currently up for each
                initiator
                ''',
                'sessions',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('unique-ip-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if check for subscriber address
                uniquenessduring first sign of life is enabled
                ''',
                'unique_ip_check',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'dhcp',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger',
            False, 
            [
            _MetaInfoClassMember('fsol-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface
                ''',
                'fsol_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life bytes received for
                initiating protocol on this interface that were
                dropped
                ''',
                'fsol_dropped_bytes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped
                ''',
                'fsol_dropped_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-dup-addr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to duplicate source address
                ''',
                'fsol_dropped_packets_dup_addr',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-flow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding creation rate
                ''',
                'fsol_dropped_packets_flow',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-dropped-packets-session-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface that
                were dropped due to exceeding one or more of the
                configured session limits
                ''',
                'fsol_dropped_packets_session_limit',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('fsol-packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of first sign of life packets received
                for initiating protocol on this interface
                ''',
                'fsol_packets',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('is-configured', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ture if the initiator is configred
                ''',
                'is_configured',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions currently up for each
                initiator
                ''',
                'sessions',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('unique-ip-check', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if check for subscriber address
                uniquenessduring first sign of life is enabled
                ''',
                'unique_ip_check',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'packet-trigger',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators',
            False, 
            [
            _MetaInfoClassMember('dhcp', REFERENCE_CLASS, 'Dhcp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp', 
                [], [], 
                '''                DHCP information
                ''',
                'dhcp',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('packet-trigger', REFERENCE_CLASS, 'PacketTrigger' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger', 
                [], [], 
                '''                packet trigger information
                ''',
                'packet_trigger',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'ipv6-initiators',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource',
            False, 
            [
            _MetaInfoClassMember('per-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per-VLAN limit category
                ''',
                'per_vlan',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'unclassified-source',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total',
            False, 
            [
            _MetaInfoClassMember('per-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Per-VLAN limit category
                ''',
                'per_vlan',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'total',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit',
            False, 
            [
            _MetaInfoClassMember('total', REFERENCE_CLASS, 'Total' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total', 
                [], [], 
                '''                All sources session limits
                ''',
                'total',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('unclassified-source', REFERENCE_CLASS, 'UnclassifiedSource' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource', 
                [], [], 
                '''                Unclassified source session limits
                ''',
                'unclassified_source',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'session-limit',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', True),
            _MetaInfoClassMember('age', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Age in HH:MM:SS format
                ''',
                'age',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('initiators', REFERENCE_CLASS, 'Initiators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators', 
                [], [], 
                '''                Configurational state-statistics for each
                initiating protocol enabled on this parent
                interface
                ''',
                'initiators',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('interface-creation-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface creation time in Month Date HH:MM:SS
                format
                ''',
                'interface_creation_time',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('interface-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Type
                ''',
                'interface_type',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-initiators', REFERENCE_CLASS, 'Ipv6Initiators' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators', 
                [], [], 
                '''                Configurational state-statistics for each
                initiating protocol enabled on this parent
                interface for IPv6 session
                ''',
                'ipv6_initiators',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('ipv6-state', REFERENCE_ENUM_CLASS, 'IpsubMaParentIntfStateDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaParentIntfStateDataEnum', 
                [], [], 
                '''                Operational ipv6 state of this interface
                ''',
                'ipv6_state',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('session-limit', REFERENCE_CLASS, 'SessionLimit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit', 
                [], [], 
                '''                Configuration session limits for each session
                limit source and type
                ''',
                'session_limit',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'IpsubMaParentIntfStateDataEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaParentIntfStateDataEnum', 
                [], [], 
                '''                Operational state of this interface
                ''',
                'state',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('vlan-type', REFERENCE_ENUM_CLASS, 'IpsubMaParentIntfVlanEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpsubMaParentIntfVlanEnum', 
                [], [], 
                '''                The VLAN type on the access interface
                ''',
                'vlan_type',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'access-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node.AccessInterfaces' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node.AccessInterfaces',
            False, 
            [
            _MetaInfoClassMember('access-interface', REFERENCE_LIST, 'AccessInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface', 
                [], [], 
                '''                IP subscriber access interface entry
                ''',
                'access_interface',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'access-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node ID to filter on. For eg., 0/1/CPU0
                ''',
                'node_name',
                'Cisco-IOS-XR-subscriber-ipsub-oper', True),
            _MetaInfoClassMember('access-interfaces', REFERENCE_CLASS, 'AccessInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.AccessInterfaces', 
                [], [], 
                '''                IP subscriber access interface table
                ''',
                'access_interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Interfaces', 
                [], [], 
                '''                IP subscriber interface table
                ''',
                'interfaces',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node.Summary', 
                [], [], 
                '''                IP subscriber interface summary
                ''',
                'summary',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber.Nodes' : {
        'meta_info' : _MetaInfoClass('IpSubscriber.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes.Node', 
                [], [], 
                '''                Location. For eg., 0/1/CPU0
                ''',
                'node',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
    'IpSubscriber' : {
        'meta_info' : _MetaInfoClass('IpSubscriber',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper', 'IpSubscriber.Nodes', 
                [], [], 
                '''                IP subscriber operational data for a particular
                location
                ''',
                'nodes',
                'Cisco-IOS-XR-subscriber-ipsub-oper', False),
            ],
            'Cisco-IOS-XR-subscriber-ipsub-oper',
            'ip-subscriber',
            _yang_ns._namespaces['Cisco-IOS-XR-subscriber-ipsub-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_subscriber_ipsub_oper'
        ),
    },
}
_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.Dhcp']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators.PacketTrigger']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.Dhcp']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators.PacketTrigger']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Initiators']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary.Ipv6Initiators']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.Dhcp']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators.PacketTrigger']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.Dhcp']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators.PacketTrigger']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Initiators']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts.Ipv6Initiators']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.AccessInterfaceSummary']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.InterfaceCounts']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary.Vrf']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Summary']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface.Vrf']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface.Ipv6Vrf']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.Interfaces']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.Dhcp']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators.PacketTrigger']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.Dhcp']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators.PacketTrigger']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.UnclassifiedSource']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit.Total']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Initiators']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.Ipv6Initiators']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface.SessionLimit']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces.AccessInterface']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Summary']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node']['meta_info']
_meta_table['IpSubscriber.Nodes.Node.AccessInterfaces']['meta_info'].parent =_meta_table['IpSubscriber.Nodes.Node']['meta_info']
_meta_table['IpSubscriber.Nodes.Node']['meta_info'].parent =_meta_table['IpSubscriber.Nodes']['meta_info']
_meta_table['IpSubscriber.Nodes']['meta_info'].parent =_meta_table['IpSubscriber']['meta_info']
