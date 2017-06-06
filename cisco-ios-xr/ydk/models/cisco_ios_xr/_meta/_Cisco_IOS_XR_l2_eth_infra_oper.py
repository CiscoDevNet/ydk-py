


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'VlanEncapsEnum' : _MetaInfoEnum('VlanEncapsEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'no-encapsulation':'no_encapsulation',
            'dot1q':'dot1q',
            'qinq':'qinq',
            'qin-any':'qin_any',
            'dot1q-native':'dot1q_native',
            'dot1ad':'dot1ad',
            'dot1ad-native':'dot1ad_native',
            'service-instance':'service_instance',
            'dot1ad-dot1q':'dot1ad_dot1q',
            'dot1ad-any':'dot1ad_any',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'EfpTagPriorityEnum' : _MetaInfoEnum('EfpTagPriorityEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'priority0':'priority0',
            'priority1':'priority1',
            'priority2':'priority2',
            'priority3':'priority3',
            'priority4':'priority4',
            'priority5':'priority5',
            'priority6':'priority6',
            'priority7':'priority7',
            'priority-any':'priority_any',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'EthFilteringEnum' : _MetaInfoEnum('EthFilteringEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'no-filtering':'no_filtering',
            'dot1q-filtering':'dot1q_filtering',
            'dot1ad-filtering':'dot1ad_filtering',
            'two-port-mac-relay-filtering':'two_port_mac_relay_filtering',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'EfpPayloadEtypeEnum' : _MetaInfoEnum('EfpPayloadEtypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'payload-ethertype-any':'payload_ethertype_any',
            'payload-ethertype-ip':'payload_ethertype_ip',
            'payload-ethertype-pppoe':'payload_ethertype_pppoe',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'EfpTagEtypeEnum' : _MetaInfoEnum('EfpTagEtypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'untagged':'untagged',
            'dot1q':'dot1q',
            'dot1ad':'dot1ad',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'VlanQinqOuterEtypeEnum' : _MetaInfoEnum('VlanQinqOuterEtypeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'ether-type8100':'ether_type8100',
            'ether-type9100':'ether_type9100',
            'ether-type9200':'ether_type9200',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'EthCapsUcastMacModeEnum' : _MetaInfoEnum('EthCapsUcastMacModeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'reserved':'reserved',
            'permit':'permit',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'ImStateEnumEnum' : _MetaInfoEnum('ImStateEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'im-state-not-ready':'im_state_not_ready',
            'im-state-admin-down':'im_state_admin_down',
            'im-state-down':'im_state_down',
            'im-state-up':'im_state_up',
            'im-state-shutdown':'im_state_shutdown',
            'im-state-err-disable':'im_state_err_disable',
            'im-state-down-immediate':'im_state_down_immediate',
            'im-state-down-immediate-admin':'im_state_down_immediate_admin',
            'im-state-down-graceful':'im_state_down_graceful',
            'im-state-begin-shutdown':'im_state_begin_shutdown',
            'im-state-end-shutdown':'im_state_end_shutdown',
            'im-state-begin-error-disable':'im_state_begin_error_disable',
            'im-state-end-error-disable':'im_state_end_error_disable',
            'im-state-begin-down-graceful':'im_state_begin_down_graceful',
            'im-state-reset':'im_state_reset',
            'im-state-operational':'im_state_operational',
            'im-state-not-operational':'im_state_not_operational',
            'im-state-unknown':'im_state_unknown',
            'im-state-last':'im_state_last',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'VlanServiceEnum' : _MetaInfoEnum('VlanServiceEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper',
        {
            'vlan-service-l2':'vlan_service_l2',
            'vlan-service-l3':'vlan_service_l3',
        }, 'Cisco-IOS-XR-l2-eth-infra-oper', _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper']),
    'MacAccounting.Interfaces.Interface.State' : {
        'meta_info' : _MetaInfoClass('MacAccounting.Interfaces.Interface.State',
            False, 
            [
            _MetaInfoClassMember('is-egress-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAC accounting on on egress
                ''',
                'is_egress_enabled',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('is-ingress-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                MAC accounting on on ingress
                ''',
                'is_ingress_enabled',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('number-available-egress', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MAC accounting entries available on egress
                ''',
                'number_available_egress',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('number-available-ingress', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MAC accounting entries available on ingress
                ''',
                'number_available_ingress',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('number-available-on-node', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MAC accountng entries available across the node
                ''',
                'number_available_on_node',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'state',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'MacAccounting.Interfaces.Interface.IngressStatistic' : {
        'meta_info' : _MetaInfoClass('MacAccounting.Interfaces.Interface.IngressStatistic',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes counted
                ''',
                'bytes',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                48bit MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets counted
                ''',
                'packets',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'ingress-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'MacAccounting.Interfaces.Interface.EgressStatistic' : {
        'meta_info' : _MetaInfoClass('MacAccounting.Interfaces.Interface.EgressStatistic',
            False, 
            [
            _MetaInfoClassMember('bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of bytes counted
                ''',
                'bytes',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                48bit MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('packets', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of packets counted
                ''',
                'packets',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'egress-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'MacAccounting.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('MacAccounting.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2-eth-infra-oper', True),
            _MetaInfoClassMember('egress-statistic', REFERENCE_LIST, 'EgressStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'MacAccounting.Interfaces.Interface.EgressStatistic', 
                [], [], 
                '''                Egress MAC accounting statistics
                ''',
                'egress_statistic',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('ingress-statistic', REFERENCE_LIST, 'IngressStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'MacAccounting.Interfaces.Interface.IngressStatistic', 
                [], [], 
                '''                Ingress MAC accounting statistics
                ''',
                'ingress_statistic',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('state', REFERENCE_CLASS, 'State' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'MacAccounting.Interfaces.Interface.State', 
                [], [], 
                '''                MAC accounting state for the interface
                ''',
                'state',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'MacAccounting.Interfaces' : {
        'meta_info' : _MetaInfoClass('MacAccounting.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'MacAccounting.Interfaces.Interface', 
                [], [], 
                '''                Operational data and statistics for an
                interface configured with MAC accounting
                enabled
                ''',
                'interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'MacAccounting' : {
        'meta_info' : _MetaInfoClass('MacAccounting',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'MacAccounting.Interfaces', 
                [], [], 
                '''                MAC accounting interface table in MIB
                lexicographic order
                ''',
                'interfaces',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'mac-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters',
            False, 
            [
            _MetaInfoClassMember('admin-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces which are
                administrativelyshutdown
                ''',
                'admin_down',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces which are down
                ''',
                'down',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces which are up
                ''',
                'up',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'state-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces',
            False, 
            [
            _MetaInfoClassMember('dot1q-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of single tagged subinterfaces
                ''',
                'dot1q_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('qin-any-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of double tagged subinterfaces with
                wildcarded inner tag
                ''',
                'qin_any_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('qin-q-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of double tagged subinterfaces with
                explicit inner tag
                ''',
                'qin_q_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('state-counters', REFERENCE_CLASS, 'StateCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters', 
                [], [], 
                '''                Numbers of subinterfaces up, down or
                administratively shut down
                ''',
                'state_counters',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of Layer 2 subinterfaces configured
                ''',
                'total_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('untagged-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces without VLAN tag
                configuration
                ''',
                'untagged_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'layer2-sub-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters',
            False, 
            [
            _MetaInfoClassMember('admin-down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces which are
                administrativelyshutdown
                ''',
                'admin_down',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('down', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces which are down
                ''',
                'down',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('up', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces which are up
                ''',
                'up',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'state-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces',
            False, 
            [
            _MetaInfoClassMember('dot1q-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of single tagged subinterfaces
                ''',
                'dot1q_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('native-vlan', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Native VLAN ID configured on trunk
                ''',
                'native_vlan',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('qin-q-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of double tagged subinterfaces
                ''',
                'qin_q_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('state-counters', REFERENCE_CLASS, 'StateCounters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters', 
                [], [], 
                '''                Numbers of subinterfaces up, down or
                administratively shut down
                ''',
                'state_counters',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of Layer 3 subinterfaces configured
                ''',
                'total_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('untagged-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces without VLAN tag
                configuration
                ''',
                'untagged_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'layer3-sub-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Trunks.Trunk' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Trunks.Trunk',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', True),
            _MetaInfoClassMember('dot1ad-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of subinterfaces with 802.1ad outer tag
                ''',
                'dot1ad_count',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface name
                ''',
                'interface_xr',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('layer2-sub-interfaces', REFERENCE_CLASS, 'Layer2SubInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces', 
                [], [], 
                '''                Layer 2 Transport Subinterfaces
                ''',
                'layer2_sub_interfaces',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('layer3-sub-interfaces', REFERENCE_CLASS, 'Layer3SubInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces', 
                [], [], 
                '''                Layer 3 Terminated Subinterfaces
                ''',
                'layer3_sub_interfaces',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('mac-filtering', REFERENCE_ENUM_CLASS, 'EthFilteringEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthFilteringEnum', 
                [], [], 
                '''                IEEE 802.1Q/802.1ad multicast MAC address
                filtering
                ''',
                'mac_filtering',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2 MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('qinq-outer-ether-type', REFERENCE_ENUM_CLASS, 'VlanQinqOuterEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanQinqOuterEtypeEnum', 
                [], [], 
                '''                QinQ Outer Tag Ether Type
                ''',
                'qinq_outer_ether_type',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('untagged-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface/Sub-interface handling untagged frames
                ''',
                'untagged_interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'trunk',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Trunks' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Trunks',
            False, 
            [
            _MetaInfoClassMember('trunk', REFERENCE_LIST, 'Trunk' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Trunks.Trunk', 
                [], [], 
                '''                Operational data for trunk interfaces
                configured with VLANs
                ''',
                'trunk',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'trunks',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack',
            False, 
            [
            _MetaInfoClassMember('outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer tag value
                ''',
                'outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('second-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Second tag value
                ''',
                'second_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'stack',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag',
            False, 
            [
            _MetaInfoClassMember('ethertype', REFERENCE_ENUM_CLASS, 'EfpTagEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtypeEnum', 
                [], [], 
                '''                Ethertype of tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN Id
                ''',
                'vlan_id',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'local-traffic-tag',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack',
            False, 
            [
            _MetaInfoClassMember('local-traffic-tag', REFERENCE_LIST, 'LocalTrafficTag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag', 
                [], [], 
                '''                VLAN tags for locally-sourced traffic
                ''',
                'local_traffic_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'local-traffic-stack',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange',
            False, 
            [
            _MetaInfoClassMember('vlan-id-high', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID High
                ''',
                'vlan_id_high',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-id-low', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID Low
                ''',
                'vlan_id_low',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'vlan-range',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch',
            False, 
            [
            _MetaInfoClassMember('ethertype', REFERENCE_ENUM_CLASS, 'EfpTagEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtypeEnum', 
                [], [], 
                '''                Ethertype of tag to match
                ''',
                'ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'EfpTagPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagPriorityEnum', 
                [], [], 
                '''                Priority to match
                ''',
                'priority',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-range', REFERENCE_LIST, 'VlanRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange', 
                [], [], 
                '''                VLAN Ids to match
                ''',
                'vlan_range',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'tags-to-match',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe',
            False, 
            [
            _MetaInfoClassMember('ethertype', REFERENCE_ENUM_CLASS, 'EfpTagEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtypeEnum', 
                [], [], 
                '''                Ethertype of tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN Id
                ''',
                'vlan_id',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'pushe',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails',
            False, 
            [
            _MetaInfoClassMember('destination-mac-match', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination MAC address to match on ingress
                ''',
                'destination_mac_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('is-exact-match', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the packet must match the encapsulation
                exactly, with no further inner tags
                ''',
                'is_exact_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('is-native-preserving', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the native VLAN is customer-tag
                preserving
                ''',
                'is_native_preserving',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('is-native-vlan', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether this represents the native VLAN on the
                port
                ''',
                'is_native_vlan',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('local-traffic-stack', REFERENCE_CLASS, 'LocalTrafficStack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack', 
                [], [], 
                '''                VLAN tags for locally-sourced traffic
                ''',
                'local_traffic_stack',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('payload-ethertype', REFERENCE_ENUM_CLASS, 'EfpPayloadEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpPayloadEtypeEnum', 
                [], [], 
                '''                Payload Ethertype to match
                ''',
                'payload_ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('pushe', REFERENCE_LIST, 'Pushe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe', 
                [], [], 
                '''                VLAN tags pushed on egress
                ''',
                'pushe',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('source-mac-match', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The source MAC address to match on ingress
                ''',
                'source_mac_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('tags-popped', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of tags popped on ingress
                ''',
                'tags_popped',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('tags-to-match', REFERENCE_LIST, 'TagsToMatch' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch', 
                [], [], 
                '''                Tags to match on ingress packets
                ''',
                'tags_to_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'service-instance-details',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack',
            False, 
            [
            _MetaInfoClassMember('outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer tag value
                ''',
                'outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('second-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Second tag value
                ''',
                'second_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'dot1ad-dot1q-stack',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails',
            False, 
            [
            _MetaInfoClassMember('dot1ad-dot1q-stack', REFERENCE_CLASS, 'Dot1AdDot1QStack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack', 
                [], [], 
                '''                802.1ad 802.1Q stack value
                ''',
                'dot1ad_dot1q_stack',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('dot1ad-native-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                802.1ad native tag value
                ''',
                'dot1ad_native_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('dot1ad-outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                802.1ad Outer tag value
                ''',
                'dot1ad_outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('dot1ad-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                802.1ad tag value
                ''',
                'dot1ad_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('native-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Native tag value
                ''',
                'native_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer tag value
                ''',
                'outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('service-instance-details', REFERENCE_CLASS, 'ServiceInstanceDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails', 
                [], [], 
                '''                Service Instance encapsulation
                ''',
                'service_instance_details',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack', 
                [], [], 
                '''                Stack value
                ''',
                'stack',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tag value
                ''',
                'tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-encapsulation', REFERENCE_ENUM_CLASS, 'VlanEncapsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanEncapsEnum', 
                [], [], 
                '''                VLANEncapsulation
                ''',
                'vlan_encapsulation',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'encapsulation-details',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', True),
            _MetaInfoClassMember('encapsulation-details', REFERENCE_CLASS, 'EncapsulationDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails', 
                [], [], 
                '''                Encapsulation type and tag stack
                ''',
                'encapsulation_details',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2 MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('parent-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent interface
                ''',
                'parent_interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('service', REFERENCE_ENUM_CLASS, 'VlanServiceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanServiceEnum', 
                [], [], 
                '''                Service type
                ''',
                'service',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('switched-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2 switched MTU
                ''',
                'switched_mtu',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.Interfaces' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces.Interface', 
                [], [], 
                '''                Operational data for a sub-interface
                configured with VLANs
                ''',
                'interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack',
            False, 
            [
            _MetaInfoClassMember('outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer tag value
                ''',
                'outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('second-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Second tag value
                ''',
                'second_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'stack',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag',
            False, 
            [
            _MetaInfoClassMember('ethertype', REFERENCE_ENUM_CLASS, 'EfpTagEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtypeEnum', 
                [], [], 
                '''                Ethertype of tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN Id
                ''',
                'vlan_id',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'local-traffic-tag',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack',
            False, 
            [
            _MetaInfoClassMember('local-traffic-tag', REFERENCE_LIST, 'LocalTrafficTag' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag', 
                [], [], 
                '''                VLAN tags for locally-sourced traffic
                ''',
                'local_traffic_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'local-traffic-stack',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange',
            False, 
            [
            _MetaInfoClassMember('vlan-id-high', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID High
                ''',
                'vlan_id_high',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-id-low', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID Low
                ''',
                'vlan_id_low',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'vlan-range',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch',
            False, 
            [
            _MetaInfoClassMember('ethertype', REFERENCE_ENUM_CLASS, 'EfpTagEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtypeEnum', 
                [], [], 
                '''                Ethertype of tag to match
                ''',
                'ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'EfpTagPriorityEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagPriorityEnum', 
                [], [], 
                '''                Priority to match
                ''',
                'priority',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-range', REFERENCE_LIST, 'VlanRange' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange', 
                [], [], 
                '''                VLAN Ids to match
                ''',
                'vlan_range',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'tags-to-match',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe',
            False, 
            [
            _MetaInfoClassMember('ethertype', REFERENCE_ENUM_CLASS, 'EfpTagEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpTagEtypeEnum', 
                [], [], 
                '''                Ethertype of tag
                ''',
                'ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN Id
                ''',
                'vlan_id',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'pushe',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails',
            False, 
            [
            _MetaInfoClassMember('destination-mac-match', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The destination MAC address to match on ingress
                ''',
                'destination_mac_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('is-exact-match', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the packet must match the encapsulation
                exactly, with no further inner tags
                ''',
                'is_exact_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('is-native-preserving', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the native VLAN is customer-tag
                preserving
                ''',
                'is_native_preserving',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('is-native-vlan', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether this represents the native VLAN on the
                port
                ''',
                'is_native_vlan',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('local-traffic-stack', REFERENCE_CLASS, 'LocalTrafficStack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack', 
                [], [], 
                '''                VLAN tags for locally-sourced traffic
                ''',
                'local_traffic_stack',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('payload-ethertype', REFERENCE_ENUM_CLASS, 'EfpPayloadEtypeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EfpPayloadEtypeEnum', 
                [], [], 
                '''                Payload Ethertype to match
                ''',
                'payload_ethertype',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('pushe', REFERENCE_LIST, 'Pushe' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe', 
                [], [], 
                '''                VLAN tags pushed on egress
                ''',
                'pushe',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('source-mac-match', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The source MAC address to match on ingress
                ''',
                'source_mac_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('tags-popped', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Number of tags popped on ingress
                ''',
                'tags_popped',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('tags-to-match', REFERENCE_LIST, 'TagsToMatch' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch', 
                [], [], 
                '''                Tags to match on ingress packets
                ''',
                'tags_to_match',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'service-instance-details',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack',
            False, 
            [
            _MetaInfoClassMember('outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer tag value
                ''',
                'outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('second-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Second tag value
                ''',
                'second_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'dot1ad-dot1q-stack',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails',
            False, 
            [
            _MetaInfoClassMember('dot1ad-dot1q-stack', REFERENCE_CLASS, 'Dot1AdDot1QStack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack', 
                [], [], 
                '''                802.1ad 802.1Q stack value
                ''',
                'dot1ad_dot1q_stack',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('dot1ad-native-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                802.1ad native tag value
                ''',
                'dot1ad_native_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('dot1ad-outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                802.1ad Outer tag value
                ''',
                'dot1ad_outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('dot1ad-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                802.1ad tag value
                ''',
                'dot1ad_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('native-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Native tag value
                ''',
                'native_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('outer-tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Outer tag value
                ''',
                'outer_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('service-instance-details', REFERENCE_CLASS, 'ServiceInstanceDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails', 
                [], [], 
                '''                Service Instance encapsulation
                ''',
                'service_instance_details',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('stack', REFERENCE_CLASS, 'Stack' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack', 
                [], [], 
                '''                Stack value
                ''',
                'stack',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('tag', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Tag value
                ''',
                'tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('vlan-encapsulation', REFERENCE_ENUM_CLASS, 'VlanEncapsEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanEncapsEnum', 
                [], [], 
                '''                VLANEncapsulation
                ''',
                'vlan_encapsulation',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'encapsulation-details',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations.TagAllocation' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations.TagAllocation',
            False, 
            [
            _MetaInfoClassMember('encapsulation-details', REFERENCE_CLASS, 'EncapsulationDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails', 
                [], [], 
                '''                Encapsulation type and tag stack
                ''',
                'encapsulation_details',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('first-tag', ATTRIBUTE, 'int' , None, None, 
                [('1', '4094')], [], 
                '''                The first (outermost) tag
                ''',
                'first_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('interface-xr', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface_xr',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2 MTU
                ''',
                'mtu',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('parent-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent interface
                ''',
                'parent_interface',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('second-tag', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                The second tag
                ''',
                'second_tag',
                'Cisco-IOS-XR-l2-eth-infra-oper', False, [
                    _MetaInfoClassMember('second-tag', REFERENCE_ENUM_CLASS, 'VlanTagOrAnyEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_datatypes', 'VlanTagOrAnyEnum', 
                        [], [], 
                        '''                        The second tag
                        ''',
                        'second_tag',
                        'Cisco-IOS-XR-l2-eth-infra-oper', False),
                    _MetaInfoClassMember('second-tag', ATTRIBUTE, 'int' , None, None, 
                        [('1', '4096')], [], 
                        '''                        The second tag
                        ''',
                        'second_tag',
                        'Cisco-IOS-XR-l2-eth-infra-oper', False),
                ]),
            _MetaInfoClassMember('service', REFERENCE_ENUM_CLASS, 'VlanServiceEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'VlanServiceEnum', 
                [], [], 
                '''                Service type
                ''',
                'service',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Interface state
                ''',
                'state',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('switched-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                L2 switched MTU
                ''',
                'switched_mtu',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'tag-allocation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node.TagAllocations' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node.TagAllocations',
            False, 
            [
            _MetaInfoClassMember('tag-allocation', REFERENCE_LIST, 'TagAllocation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations.TagAllocation', 
                [], [], 
                '''                Operational data for a sub-interface
                configured with VLANs
                ''',
                'tag_allocation',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'tag-allocations',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The identifier for the node
                ''',
                'node_id',
                'Cisco-IOS-XR-l2-eth-infra-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Interfaces', 
                [], [], 
                '''                VLAN interface table (specific to this node)
                ''',
                'interfaces',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('tag-allocations', REFERENCE_CLASS, 'TagAllocations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.TagAllocations', 
                [], [], 
                '''                VLAN tag allocation table (specific to this
                node)
                ''',
                'tag_allocations',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('trunks', REFERENCE_CLASS, 'Trunks' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node.Trunks', 
                [], [], 
                '''                VLAN trunk table (specific to this node)
                ''',
                'trunks',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan.Nodes' : {
        'meta_info' : _MetaInfoClass('Vlan.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes.Node', 
                [], [], 
                '''                The VLAN operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'Vlan' : {
        'meta_info' : _MetaInfoClass('Vlan',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'Vlan.Nodes', 
                [], [], 
                '''                Per node VLAN operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'vlan',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter' : {
        'meta_info' : _MetaInfoClass('EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'EthCapsUcastMacModeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthCapsUcastMacModeEnum', 
                [], [], 
                '''                Unicast MAC mode
                ''',
                'mode',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'unicast-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter' : {
        'meta_info' : _MetaInfoClass('EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The interface name
                ''',
                'interface_name',
                'Cisco-IOS-XR-l2-eth-infra-oper', True),
            _MetaInfoClassMember('unicast-filter', REFERENCE_LIST, 'UnicastFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter', 
                [], [], 
                '''                Unicast MAC filter information
                ''',
                'unicast_filter',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'unicast-mac-filter',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'EthernetEncapsulation.Nodes.Node.UnicastMacFilters' : {
        'meta_info' : _MetaInfoClass('EthernetEncapsulation.Nodes.Node.UnicastMacFilters',
            False, 
            [
            _MetaInfoClassMember('unicast-mac-filter', REFERENCE_LIST, 'UnicastMacFilter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter', 
                [], [], 
                '''                Operational data for interface with MAC
                filters configured
                ''',
                'unicast_mac_filter',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'unicast-mac-filters',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'EthernetEncapsulation.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('EthernetEncapsulation.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The identifier for the node
                ''',
                'node_name',
                'Cisco-IOS-XR-l2-eth-infra-oper', True),
            _MetaInfoClassMember('unicast-mac-filters', REFERENCE_CLASS, 'UnicastMacFilters' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthernetEncapsulation.Nodes.Node.UnicastMacFilters', 
                [], [], 
                '''                Unicast MAC filter table (specific to this
                node)
                ''',
                'unicast_mac_filters',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'EthernetEncapsulation.Nodes' : {
        'meta_info' : _MetaInfoClass('EthernetEncapsulation.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthernetEncapsulation.Nodes.Node', 
                [], [], 
                '''                The Ethernet encaps operational data for a
                particular node
                ''',
                'node',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
    'EthernetEncapsulation' : {
        'meta_info' : _MetaInfoClass('EthernetEncapsulation',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper', 'EthernetEncapsulation.Nodes', 
                [], [], 
                '''                Per node Ethernet encapsulation operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-l2-eth-infra-oper', False),
            ],
            'Cisco-IOS-XR-l2-eth-infra-oper',
            'ethernet-encapsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-l2-eth-infra-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_l2_eth_infra_oper'
        ),
    },
}
_meta_table['MacAccounting.Interfaces.Interface.State']['meta_info'].parent =_meta_table['MacAccounting.Interfaces.Interface']['meta_info']
_meta_table['MacAccounting.Interfaces.Interface.IngressStatistic']['meta_info'].parent =_meta_table['MacAccounting.Interfaces.Interface']['meta_info']
_meta_table['MacAccounting.Interfaces.Interface.EgressStatistic']['meta_info'].parent =_meta_table['MacAccounting.Interfaces.Interface']['meta_info']
_meta_table['MacAccounting.Interfaces.Interface']['meta_info'].parent =_meta_table['MacAccounting.Interfaces']['meta_info']
_meta_table['MacAccounting.Interfaces']['meta_info'].parent =_meta_table['MacAccounting']['meta_info']
_meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces.StateCounters']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces']['meta_info']
_meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces.StateCounters']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces']['meta_info']
_meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer2SubInterfaces']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Trunks.Trunk']['meta_info']
_meta_table['Vlan.Nodes.Node.Trunks.Trunk.Layer3SubInterfaces']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Trunks.Trunk']['meta_info']
_meta_table['Vlan.Nodes.Node.Trunks.Trunk']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Trunks']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails.Pushe']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Stack']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.ServiceInstanceDetails']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails.Dot1AdDot1QStack']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface.EncapsulationDetails']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces.Interface']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces.Interface']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.Interfaces']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack.LocalTrafficTag']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch.VlanRange']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.LocalTrafficStack']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.TagsToMatch']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails.Pushe']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Stack']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.ServiceInstanceDetails']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails.Dot1AdDot1QStack']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation.EncapsulationDetails']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations.TagAllocation']['meta_info'].parent =_meta_table['Vlan.Nodes.Node.TagAllocations']['meta_info']
_meta_table['Vlan.Nodes.Node.Trunks']['meta_info'].parent =_meta_table['Vlan.Nodes.Node']['meta_info']
_meta_table['Vlan.Nodes.Node.Interfaces']['meta_info'].parent =_meta_table['Vlan.Nodes.Node']['meta_info']
_meta_table['Vlan.Nodes.Node.TagAllocations']['meta_info'].parent =_meta_table['Vlan.Nodes.Node']['meta_info']
_meta_table['Vlan.Nodes.Node']['meta_info'].parent =_meta_table['Vlan.Nodes']['meta_info']
_meta_table['Vlan.Nodes']['meta_info'].parent =_meta_table['Vlan']['meta_info']
_meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter.UnicastFilter']['meta_info'].parent =_meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter']['meta_info']
_meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters.UnicastMacFilter']['meta_info'].parent =_meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters']['meta_info']
_meta_table['EthernetEncapsulation.Nodes.Node.UnicastMacFilters']['meta_info'].parent =_meta_table['EthernetEncapsulation.Nodes.Node']['meta_info']
_meta_table['EthernetEncapsulation.Nodes.Node']['meta_info'].parent =_meta_table['EthernetEncapsulation.Nodes']['meta_info']
_meta_table['EthernetEncapsulation.Nodes']['meta_info'].parent =_meta_table['EthernetEncapsulation']['meta_info']
