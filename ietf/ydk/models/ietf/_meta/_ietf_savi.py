


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'BindingStateIdentity' : {
        'meta_info' : _MetaInfoClass('BindingStateIdentity',
            False, 
            [
            ],
            'ietf-savi',
            'binding-state',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable.BindingStateEntry' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable.BindingStateEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The binding source IP address.
                ''',
                'address',
                'ietf-savi-dhcpv4', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-dhcpv4', True),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('state', REFERENCE_IDENTITY_CLASS, 'SaviDhcpStateIdentity' , 'ydk.models.ietf.ietf_savi_dhcpv4', 'SaviDhcpStateIdentity', 
                [], [], 
                '''                State of the entry as defined in SAVI DHCP: NO_BIND, INIT_BIND, BOUND, DETECTION , RECOVERY, VERIFY.
                ''',
                'state',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('tid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Transaction ID of the corresponding DHCP transaction.
                ''',
                'tid',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                the number of timeouts that expired in the current state
                ''',
                'timeouts',
                'ietf-savi-dhcpv4', False),
            ],
            'ietf-savi-dhcpv4',
            'binding-state-entry',
            _yang_ns._namespaces['ietf-savi-dhcpv4'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable',
            False, 
            [
            _MetaInfoClassMember('binding-state-entry', REFERENCE_LIST, 'BindingStateEntry' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable.BindingStateEntry', 
                [], [], 
                '''                A binding state entry specific for SAVI DHCPv4.
                ''',
                'binding_state_entry',
                'ietf-savi-dhcpv4', False),
            ],
            'ietf-savi-dhcpv4',
            'ietf-savi-dhcpv4_binding-state-table',
            _yang_ns._namespaces['ietf-savi-dhcpv4'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable.BindingStateEntry' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable.BindingStateEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The binding source IP address.
                ''',
                'address',
                'ietf-savi-dhcpv6', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-dhcpv6', True),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('state', REFERENCE_IDENTITY_CLASS, 'SaviDhcpStateIdentity' , 'ydk.models.ietf.ietf_savi_dhcpv6', 'SaviDhcpStateIdentity', 
                [], [], 
                '''                State of the entry as defined in SAVI DHCP: NO_BIND, INIT_BIND, BOUND, DETECTION , RECOVERY, VERIFY.
                ''',
                'state',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('tid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Transaction ID of the corresponding DHCP transaction.
                ''',
                'tid',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('timeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of timeouts that expired in the current state.
                ''',
                'timeouts',
                'ietf-savi-dhcpv6', False),
            ],
            'ietf-savi-dhcpv6',
            'binding-state-entry',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable',
            False, 
            [
            _MetaInfoClassMember('binding-state-entry', REFERENCE_LIST, 'BindingStateEntry' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable.BindingStateEntry', 
                [], [], 
                '''                A binding state entry specific for SAVI DHCPv6.
                ''',
                'binding_state_entry',
                'ietf-savi-dhcpv6', False),
            ],
            'ietf-savi-dhcpv6',
            'ietf-savi-dhcpv6_binding-state-table',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable.BindingStateEntry' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable.BindingStateEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The binding source IP address.
                ''',
                'address',
                'ietf-savi-fcfs', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-fcfs', True),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('state', REFERENCE_IDENTITY_CLASS, 'SaviFcfsStateIdentity' , 'ydk.models.ietf.ietf_savi_fcfs', 'SaviFcfsStateIdentity', 
                [], [], 
                '''                State of the entry as defined in SAVI FCFS: NO_BIND, TENTATIVE, VALID, TESTING_VP, TESTING_TP-LT
                ''',
                'state',
                'ietf-savi-fcfs', False),
            ],
            'ietf-savi-fcfs',
            'binding-state-entry',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable',
            False, 
            [
            _MetaInfoClassMember('binding-state-entry', REFERENCE_LIST, 'BindingStateEntry' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable.BindingStateEntry', 
                [], [], 
                '''                A binding status entry specific for SAVI FCFS.
                ''',
                'binding_state_entry',
                'ietf-savi-fcfs', False),
            ],
            'ietf-savi-fcfs',
            'ietf-savi-fcfs_binding-state-table',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable.BindingStateEntry' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable.BindingStateEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                The binding source IP address.
                ''',
                'address',
                'ietf-savi-send', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-send', True),
            _MetaInfoClassMember('alternative-if', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Alternative interface is a parameter defined in SAVI SEND.
                ''',
                'alternative_if',
                'ietf-savi-send', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi-send', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi-send', False),
            _MetaInfoClassMember('state', REFERENCE_IDENTITY_CLASS, 'SaviSendStateIdentity' , 'ydk.models.ietf.ietf_savi_send', 'SaviSendStateIdentity', 
                [], [], 
                '''                State of the entry as defined in SAVI SEND: TENTATIVE_DAD, TENTATIVE_NUD, VALID, TESTING_VP, TESTING_VP'
                ''',
                'state',
                'ietf-savi-send', False),
            ],
            'ietf-savi-send',
            'binding-state-entry',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable',
            False, 
            [
            _MetaInfoClassMember('binding-state-entry', REFERENCE_LIST, 'BindingStateEntry' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable.BindingStateEntry', 
                [], [], 
                '''                A binding state entry specific for SAVI SEND.
                ''',
                'binding_state_entry',
                'ietf-savi-send', False),
            ],
            'ietf-savi-send',
            'ietf-savi-send_binding-state-table',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances.SaviInstance' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances.SaviInstance',
            False, 
            [
            _MetaInfoClassMember('savi-method', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address assignment methods.
                ''',
                'savi_method',
                'ietf-savi', True),
            _MetaInfoClassMember('ietf-savi-dhcpv4_binding-state-table', REFERENCE_CLASS, 'IetfSaviDhcpv4_BindingStateTable' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable', 
                [], [], 
                '''                Binding state table specific for SAVI DHCPv4.
                ''',
                'ietf_savi_dhcpv4_binding_state_table',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('ietf-savi-dhcpv6_binding-state-table', REFERENCE_CLASS, 'IetfSaviDhcpv6_BindingStateTable' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable', 
                [], [], 
                '''                Binding state table specific for SAVI DHCPv6.
                ''',
                'ietf_savi_dhcpv6_binding_state_table',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('ietf-savi-fcfs_binding-state-table', REFERENCE_CLASS, 'IetfSaviFcfs_BindingStateTable' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable', 
                [], [], 
                '''                Binding state table specific for SAVI FCFS.
                ''',
                'ietf_savi_fcfs_binding_state_table',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('ietf-savi-send_binding-state-table', REFERENCE_CLASS, 'IetfSaviSend_BindingStateTable' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable', 
                [], [], 
                '''                Binding state table specific for SAVI SEND.
                ''',
                'ietf_savi_send_binding_state_table',
                'ietf-savi-send', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Preference of the savi method.
                ''',
                'preference',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'savi-instance',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.SaviInstances' : {
        'meta_info' : _MetaInfoClass('SaviState.SaviInstances',
            False, 
            [
            _MetaInfoClassMember('savi-instance', REFERENCE_LIST, 'SaviInstance' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances.SaviInstance', 
                [], [], 
                '''                A list of parameters for each savi method.
                ''',
                'savi_instance',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'savi-instances',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.BindingTable.Ipv4.BindingEntry' : {
        'meta_info' : _MetaInfoClass('SaviState.BindingTable.Ipv4.BindingEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the binding host.
                ''',
                'address',
                'ietf-savi', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi', True),
            _MetaInfoClassMember('binding-method', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address assignment methods.
                ''',
                'binding_method',
                'ietf-savi', False),
            _MetaInfoClassMember('creationtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the local clock when the entry was firstly created.
                ''',
                'creationtime',
                'ietf-savi', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'binding-entry',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.BindingTable.Ipv4' : {
        'meta_info' : _MetaInfoClass('SaviState.BindingTable.Ipv4',
            False, 
            [
            _MetaInfoClassMember('binding-entry', REFERENCE_LIST, 'BindingEntry' , 'ydk.models.ietf.ietf_savi', 'SaviState.BindingTable.Ipv4.BindingEntry', 
                [], [], 
                '''                Definition of a binding entry
                ''',
                'binding_entry',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'ipv4',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.BindingTable.Ipv6.BindingEntry' : {
        'meta_info' : _MetaInfoClass('SaviState.BindingTable.Ipv6.BindingEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address of the binding host.
                ''',
                'address',
                'ietf-savi', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi', True),
            _MetaInfoClassMember('binding-method', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address assignment methods.
                ''',
                'binding_method',
                'ietf-savi', False),
            _MetaInfoClassMember('creationtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the local clock when the entry was firstly created.
                ''',
                'creationtime',
                'ietf-savi', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'binding-entry',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.BindingTable.Ipv6' : {
        'meta_info' : _MetaInfoClass('SaviState.BindingTable.Ipv6',
            False, 
            [
            _MetaInfoClassMember('binding-entry', REFERENCE_LIST, 'BindingEntry' , 'ydk.models.ietf.ietf_savi', 'SaviState.BindingTable.Ipv6.BindingEntry', 
                [], [], 
                '''                Definition of a binding entry
                ''',
                'binding_entry',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'ipv6',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.BindingTable' : {
        'meta_info' : _MetaInfoClass('SaviState.BindingTable',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_savi', 'SaviState.BindingTable.Ipv4', 
                [], [], 
                '''                Container for binding table for IPv4 protocol.
                ''',
                'ipv4',
                'ietf-savi', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_savi', 'SaviState.BindingTable.Ipv6', 
                [], [], 
                '''                Container for binding table for IPv4 protocol.
                ''',
                'ipv6',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'binding-table',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.Statistics.FilteringPks.IfFilteringPks' : {
        'meta_info' : _MetaInfoClass('SaviState.Statistics.FilteringPks.IfFilteringPks',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi', True),
            _MetaInfoClassMember('filtering-pks', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of filtering packets.
                ''',
                'filtering_pks',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'if-filtering-pks',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.Statistics.FilteringPks' : {
        'meta_info' : _MetaInfoClass('SaviState.Statistics.FilteringPks',
            False, 
            [
            _MetaInfoClassMember('if-filtering-pks', REFERENCE_LIST, 'IfFilteringPks' , 'ydk.models.ietf.ietf_savi', 'SaviState.Statistics.FilteringPks.IfFilteringPks', 
                [], [], 
                '''                A list of parameters for counting filtering packets.
                ''',
                'if_filtering_pks',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'filtering-pks',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState.Statistics' : {
        'meta_info' : _MetaInfoClass('SaviState.Statistics',
            False, 
            [
            _MetaInfoClassMember('bst-entry-counts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The count of the binding state table.
                ''',
                'bst_entry_counts',
                'ietf-savi', False),
            _MetaInfoClassMember('bst-entry-volume', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The volume of the the binding state table.
                ''',
                'bst_entry_volume',
                'ietf-savi', False),
            _MetaInfoClassMember('filtering-pks', REFERENCE_CLASS, 'FilteringPks' , 'ydk.models.ietf.ietf_savi', 'SaviState.Statistics.FilteringPks', 
                [], [], 
                '''                Container of parameters for counting filtering packets.
                ''',
                'filtering_pks',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'statistics',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'SaviState' : {
        'meta_info' : _MetaInfoClass('SaviState',
            False, 
            [
            _MetaInfoClassMember('binding-table', REFERENCE_CLASS, 'BindingTable' , 'ydk.models.ietf.ietf_savi', 'SaviState.BindingTable', 
                [], [], 
                '''                Container for binding table.
                ''',
                'binding_table',
                'ietf-savi', False),
            _MetaInfoClassMember('savi-instances', REFERENCE_CLASS, 'SaviInstances' , 'ydk.models.ietf.ietf_savi', 'SaviState.SaviInstances', 
                [], [], 
                '''                Container of parameters for each savi method.
                ''',
                'savi_instances',
                'ietf-savi', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ietf.ietf_savi', 'SaviState.Statistics', 
                [], [], 
                '''                Container of statistics parameters for savi subsystem.
                ''',
                'statistics',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'savi-state',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes.IfAttribute' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes.IfAttribute',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-dhcpv4', True),
            _MetaInfoClassMember('data-snooping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'data_snooping',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('dhcp-snooping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'dhcp_snooping',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('dhcp-trust', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'dhcp_trust',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('trust-attribute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'trust_attribute',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('validating', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'validating',
                'ietf-savi-dhcpv4', False),
            ],
            'ietf-savi-dhcpv4',
            'if-attribute',
            _yang_ns._namespaces['ietf-savi-dhcpv4'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes',
            False, 
            [
            _MetaInfoClassMember('if-attribute', REFERENCE_LIST, 'IfAttribute' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes.IfAttribute', 
                [], [], 
                '''                A list of attributes for each interface.
                ''',
                'if_attribute',
                'ietf-savi-dhcpv4', False),
            ],
            'ietf-savi-dhcpv4',
            'if-attributes',
            _yang_ns._namespaces['ietf-savi-dhcpv4'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params',
            False, 
            [
            _MetaInfoClassMember('datasnooping-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum interval between two successive EVE_DATA_UNMATCH
                events triggered by an attachment. Recommended interval:
                60s and configurable.
                ''',
                'datasnooping_interval',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('detection-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum duration of a hardware address verification step
                in the VERIFY state.
                ''',
                'detection_timeout',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('if-attributes', REFERENCE_CLASS, 'IfAttributes' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes', 
                [], [], 
                '''                Interface attributes specific to SAVI DHCPv4.
                ''',
                'if_attributes',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('max-dhcp-responsetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Solicit timeout value. Default is 120s.
                ''',
                'max_dhcp_responsetime',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('max-leasequery-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum LEASEQUERY timeout value. Default is 10s.
                ''',
                'max_leasequery_delay',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('offlink-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Period after a client is last detected before the binding
                anchor is being removed.  Recommended delay: 30s.
                ''',
                'offlink_delay',
                'ietf-savi-dhcpv4', False),
            ],
            'ietf-savi-dhcpv4',
            'ietf-savi-dhcpv4_params',
            _yang_ns._namespaces['ietf-savi-dhcpv4'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes.IfAttribute' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes.IfAttribute',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-dhcpv6', True),
            _MetaInfoClassMember('data-snooping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'data_snooping',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('dhcp-snooping', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'dhcp_snooping',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('dhcp-trust', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'dhcp_trust',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('trust-attribute', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'trust_attribute',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('validating', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An attribute defined in SAVI DHCP.
                ''',
                'validating',
                'ietf-savi-dhcpv6', False),
            ],
            'ietf-savi-dhcpv6',
            'if-attribute',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes',
            False, 
            [
            _MetaInfoClassMember('if-attribute', REFERENCE_LIST, 'IfAttribute' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes.IfAttribute', 
                [], [], 
                '''                A list of attributes for each interface.
                ''',
                'if_attribute',
                'ietf-savi-dhcpv6', False),
            ],
            'ietf-savi-dhcpv6',
            'if-attributes',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params',
            False, 
            [
            _MetaInfoClassMember('datasnooping-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Minimum interval between two successive EVE_DATA_UNMATCH
                events triggered by an attachment. Recommended interval:
                60s and configurable.
                ''',
                'datasnooping_interval',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('detection-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum duration of a hardware address verification step
                in the VERIFY state.
                ''',
                'detection_timeout',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('if-attributes', REFERENCE_CLASS, 'IfAttributes' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes', 
                [], [], 
                '''                Interface attributes specific to SAVI DHCPv6.
                ''',
                'if_attributes',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('max-dhcp-responsetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Solicit timeout value. Default is 120s.
                ''',
                'max_dhcp_responsetime',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('max-leasequery-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum LEASEQUERY timeout value. Default is 10s.
                ''',
                'max_leasequery_delay',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('offlink-delay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Period after a client is last detected before the binding
                anchor is being removed.  Recommended delay: 30s.
                ''',
                'offlink_delay',
                'ietf-savi-dhcpv6', False),
            ],
            'ietf-savi-dhcpv6',
            'ietf-savi-dhcpv6_params',
            _yang_ns._namespaces['ietf-savi-dhcpv6'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes.IfAttribute' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes.IfAttribute',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-fcfs', True),
            _MetaInfoClassMember('trust', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SAVI FCFS processing is not performed in the port.
                ''',
                'trust',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('validating', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SAVI FCFS processing is performed in the port.
                ''',
                'validating',
                'ietf-savi-fcfs', False),
            ],
            'ietf-savi-fcfs',
            'if-attribute',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes',
            False, 
            [
            _MetaInfoClassMember('if-attribute', REFERENCE_LIST, 'IfAttribute' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes.IfAttribute', 
                [], [], 
                '''                A list of attributes for each interface.
                ''',
                'if_attribute',
                'ietf-savi-fcfs', False),
            ],
            'ietf-savi-fcfs',
            'if-attributes',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params',
            False, 
            [
            _MetaInfoClassMember('default_lt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A default value defined in SAVI FCFS.
                ''',
                'default_lt',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('if-attributes', REFERENCE_CLASS, 'IfAttributes' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes', 
                [], [], 
                '''                Interface attributes specific to SAVI SEND.
                ''',
                'if_attributes',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('tent_lt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A default value defined in SAVI FCFS.
                ''',
                'tent_lt',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('twait', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A default value defined in SAVI FCFS
                ''',
                'twait',
                'ietf-savi-fcfs', False),
            ],
            'ietf-savi-fcfs',
            'ietf-savi-fcfs_params',
            _yang_ns._namespaces['ietf-savi-fcfs'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes.IfAttribute' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes.IfAttribute',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi-send', True),
            _MetaInfoClassMember('trust', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SAVI SEND processing is not performed in the port.
                ''',
                'trust',
                'ietf-savi-send', False),
            _MetaInfoClassMember('validating', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                SAVI SEND processing is performed in the port.
                ''',
                'validating',
                'ietf-savi-send', False),
            ],
            'ietf-savi-send',
            'if-attribute',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes',
            False, 
            [
            _MetaInfoClassMember('if-attribute', REFERENCE_LIST, 'IfAttribute' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes.IfAttribute', 
                [], [], 
                '''                A list of attributes for each interface.
                ''',
                'if_attribute',
                'ietf-savi-send', False),
            ],
            'ietf-savi-send',
            'if-attributes',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance.IetfSaviSend_Params' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance.IetfSaviSend_Params',
            False, 
            [
            _MetaInfoClassMember('default_lt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A default value defined in SAVI SEND.
                ''',
                'default_lt',
                'ietf-savi-send', False),
            _MetaInfoClassMember('if-attributes', REFERENCE_CLASS, 'IfAttributes' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes', 
                [], [], 
                '''                Interface attributes specific to SAVI SEND.
                ''',
                'if_attributes',
                'ietf-savi-send', False),
            _MetaInfoClassMember('tent_lt', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                A default value defined in SAVI SEND.
                ''',
                'tent_lt',
                'ietf-savi-send', False),
            ],
            'ietf-savi-send',
            'ietf-savi-send_params',
            _yang_ns._namespaces['ietf-savi-send'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances.SaviInstance' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances.SaviInstance',
            False, 
            [
            _MetaInfoClassMember('savi-method', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address assignment methods.
                ''',
                'savi_method',
                'ietf-savi', True),
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the savi method is enabled?
                ''',
                'enable',
                'ietf-savi', False),
            _MetaInfoClassMember('ietf-savi-dhcpv4_params', REFERENCE_CLASS, 'IetfSaviDhcpv4_Params' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params', 
                [], [], 
                '''                Parameters specific to SAVI DHCPv4
                ''',
                'ietf_savi_dhcpv4_params',
                'ietf-savi-dhcpv4', False),
            _MetaInfoClassMember('ietf-savi-dhcpv6_params', REFERENCE_CLASS, 'IetfSaviDhcpv6_Params' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params', 
                [], [], 
                '''                Parameters specific to SAVI DHCPv6
                ''',
                'ietf_savi_dhcpv6_params',
                'ietf-savi-dhcpv6', False),
            _MetaInfoClassMember('ietf-savi-fcfs_params', REFERENCE_CLASS, 'IetfSaviFcfs_Params' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params', 
                [], [], 
                '''                Parameters specific to SAVI FCFS.
                ''',
                'ietf_savi_fcfs_params',
                'ietf-savi-fcfs', False),
            _MetaInfoClassMember('ietf-savi-send_params', REFERENCE_CLASS, 'IetfSaviSend_Params' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance.IetfSaviSend_Params', 
                [], [], 
                '''                Parameters specific to SAVI SEND.
                ''',
                'ietf_savi_send_params',
                'ietf-savi-send', False),
            _MetaInfoClassMember('preference', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Preference of the savi method.
                ''',
                'preference',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'savi-instance',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.SaviInstances' : {
        'meta_info' : _MetaInfoClass('Savi.SaviInstances',
            False, 
            [
            _MetaInfoClassMember('savi-instance', REFERENCE_LIST, 'SaviInstance' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances.SaviInstance', 
                [], [], 
                '''                A list of parameters for each savi method.
                ''',
                'savi_instance',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'savi-instances',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.IfFilteringAttributes.IfFilteringAttribute' : {
        'meta_info' : _MetaInfoClass('Savi.IfFilteringAttributes.IfFilteringAttribute',
            False, 
            [
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi', True),
            _MetaInfoClassMember('filtering-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If the filtering attribute is enabled? 
                ''',
                'filtering_enabled',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'if-filtering-attribute',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.IfFilteringAttributes' : {
        'meta_info' : _MetaInfoClass('Savi.IfFilteringAttributes',
            False, 
            [
            _MetaInfoClassMember('if-filtering-attribute', REFERENCE_LIST, 'IfFilteringAttribute' , 'ydk.models.ietf.ietf_savi', 'Savi.IfFilteringAttributes.IfFilteringAttribute', 
                [], [], 
                '''                A list of filtering attributes for each interface.
                ''',
                'if_filtering_attribute',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'if-filtering-attributes',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.BindingTable.Ipv4.BindingEntry' : {
        'meta_info' : _MetaInfoClass('Savi.BindingTable.Ipv4.BindingEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv4 address of the binding host.
                ''',
                'address',
                'ietf-savi', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi', True),
            _MetaInfoClassMember('binding-method', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address assignment methods.
                ''',
                'binding_method',
                'ietf-savi', False),
            _MetaInfoClassMember('creationtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the local clock when the entry was firstly created.
                ''',
                'creationtime',
                'ietf-savi', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'binding-entry',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.BindingTable.Ipv4' : {
        'meta_info' : _MetaInfoClass('Savi.BindingTable.Ipv4',
            False, 
            [
            _MetaInfoClassMember('binding-entry', REFERENCE_LIST, 'BindingEntry' , 'ydk.models.ietf.ietf_savi', 'Savi.BindingTable.Ipv4.BindingEntry', 
                [], [], 
                '''                Definition of a binding entry
                ''',
                'binding_entry',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'ipv4',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.BindingTable.Ipv6.BindingEntry' : {
        'meta_info' : _MetaInfoClass('Savi.BindingTable.Ipv6.BindingEntry',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                '''                IPv6 address of the binding host.
                ''',
                'address',
                'ietf-savi', True),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the interface.
                ''',
                'ifname',
                'ietf-savi', True),
            _MetaInfoClassMember('binding-method', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address assignment methods.
                ''',
                'binding_method',
                'ietf-savi', False),
            _MetaInfoClassMember('creationtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of the local clock when the entry was firstly created.
                ''',
                'creationtime',
                'ietf-savi', False),
            _MetaInfoClassMember('lifetime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The remaining lifetime of the entry.
                ''',
                'lifetime',
                'ietf-savi', False),
            _MetaInfoClassMember('mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                The binding source mac address.
                ''',
                'mac',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'binding-entry',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.BindingTable.Ipv6' : {
        'meta_info' : _MetaInfoClass('Savi.BindingTable.Ipv6',
            False, 
            [
            _MetaInfoClassMember('binding-entry', REFERENCE_LIST, 'BindingEntry' , 'ydk.models.ietf.ietf_savi', 'Savi.BindingTable.Ipv6.BindingEntry', 
                [], [], 
                '''                Definition of a binding entry
                ''',
                'binding_entry',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'ipv6',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi.BindingTable' : {
        'meta_info' : _MetaInfoClass('Savi.BindingTable',
            False, 
            [
            _MetaInfoClassMember('ipv4', REFERENCE_CLASS, 'Ipv4' , 'ydk.models.ietf.ietf_savi', 'Savi.BindingTable.Ipv4', 
                [], [], 
                '''                Container for binding table for IPv4 protocol.
                ''',
                'ipv4',
                'ietf-savi', False),
            _MetaInfoClassMember('ipv6', REFERENCE_CLASS, 'Ipv6' , 'ydk.models.ietf.ietf_savi', 'Savi.BindingTable.Ipv6', 
                [], [], 
                '''                Container for binding table for IPv4 protocol.
                ''',
                'ipv6',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'binding-table',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
    'Savi' : {
        'meta_info' : _MetaInfoClass('Savi',
            False, 
            [
            _MetaInfoClassMember('binding-table', REFERENCE_CLASS, 'BindingTable' , 'ydk.models.ietf.ietf_savi', 'Savi.BindingTable', 
                [], [], 
                '''                Container for binding table.
                ''',
                'binding_table',
                'ietf-savi', False),
            _MetaInfoClassMember('if-filtering-attributes', REFERENCE_CLASS, 'IfFilteringAttributes' , 'ydk.models.ietf.ietf_savi', 'Savi.IfFilteringAttributes', 
                [], [], 
                '''                Container for defining filtering attributes of each interface, common for every savi instance.
                ''',
                'if_filtering_attributes',
                'ietf-savi', False),
            _MetaInfoClassMember('savi-instances', REFERENCE_CLASS, 'SaviInstances' , 'ydk.models.ietf.ietf_savi', 'Savi.SaviInstances', 
                [], [], 
                '''                Container of parameters for each savi method.
                ''',
                'savi_instances',
                'ietf-savi', False),
            ],
            'ietf-savi',
            'savi',
            _yang_ns._namespaces['ietf-savi'],
        'ydk.models.ietf.ietf_savi'
        ),
    },
}
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable.BindingStateEntry']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable.BindingStateEntry']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable.BindingStateEntry']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable.BindingStateEntry']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv4_BindingStateTable']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviDhcpv6_BindingStateTable']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviFcfs_BindingStateTable']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance.IetfSaviSend_BindingStateTable']['meta_info'].parent =_meta_table['SaviState.SaviInstances.SaviInstance']['meta_info']
_meta_table['SaviState.SaviInstances.SaviInstance']['meta_info'].parent =_meta_table['SaviState.SaviInstances']['meta_info']
_meta_table['SaviState.BindingTable.Ipv4.BindingEntry']['meta_info'].parent =_meta_table['SaviState.BindingTable.Ipv4']['meta_info']
_meta_table['SaviState.BindingTable.Ipv6.BindingEntry']['meta_info'].parent =_meta_table['SaviState.BindingTable.Ipv6']['meta_info']
_meta_table['SaviState.BindingTable.Ipv4']['meta_info'].parent =_meta_table['SaviState.BindingTable']['meta_info']
_meta_table['SaviState.BindingTable.Ipv6']['meta_info'].parent =_meta_table['SaviState.BindingTable']['meta_info']
_meta_table['SaviState.Statistics.FilteringPks.IfFilteringPks']['meta_info'].parent =_meta_table['SaviState.Statistics.FilteringPks']['meta_info']
_meta_table['SaviState.Statistics.FilteringPks']['meta_info'].parent =_meta_table['SaviState.Statistics']['meta_info']
_meta_table['SaviState.SaviInstances']['meta_info'].parent =_meta_table['SaviState']['meta_info']
_meta_table['SaviState.BindingTable']['meta_info'].parent =_meta_table['SaviState']['meta_info']
_meta_table['SaviState.Statistics']['meta_info'].parent =_meta_table['SaviState']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes.IfAttribute']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params.IfAttributes']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes.IfAttribute']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params.IfAttributes']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes.IfAttribute']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params.IfAttributes']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes.IfAttribute']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params.IfAttributes']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv4_Params']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviDhcpv6_Params']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviFcfs_Params']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance.IetfSaviSend_Params']['meta_info'].parent =_meta_table['Savi.SaviInstances.SaviInstance']['meta_info']
_meta_table['Savi.SaviInstances.SaviInstance']['meta_info'].parent =_meta_table['Savi.SaviInstances']['meta_info']
_meta_table['Savi.IfFilteringAttributes.IfFilteringAttribute']['meta_info'].parent =_meta_table['Savi.IfFilteringAttributes']['meta_info']
_meta_table['Savi.BindingTable.Ipv4.BindingEntry']['meta_info'].parent =_meta_table['Savi.BindingTable.Ipv4']['meta_info']
_meta_table['Savi.BindingTable.Ipv6.BindingEntry']['meta_info'].parent =_meta_table['Savi.BindingTable.Ipv6']['meta_info']
_meta_table['Savi.BindingTable.Ipv4']['meta_info'].parent =_meta_table['Savi.BindingTable']['meta_info']
_meta_table['Savi.BindingTable.Ipv6']['meta_info'].parent =_meta_table['Savi.BindingTable']['meta_info']
_meta_table['Savi.SaviInstances']['meta_info'].parent =_meta_table['Savi']['meta_info']
_meta_table['Savi.IfFilteringAttributes']['meta_info'].parent =_meta_table['Savi']['meta_info']
_meta_table['Savi.BindingTable']['meta_info'].parent =_meta_table['Savi']['meta_info']
