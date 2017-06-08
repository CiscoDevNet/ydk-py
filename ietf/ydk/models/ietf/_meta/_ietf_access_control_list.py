


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'AclBaseIdentity' : {
        'meta_info' : _MetaInfoClass('AclBaseIdentity',
            False, 
            [
            ],
            'ietf-access-control-list',
            'acl-base',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AclOperData' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AclOperData',
            False, 
            [
            ],
            'ietf-access-control-list',
            'acl-oper-data',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AccessListEntries.Ace.Matches.SourcePortRange' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AccessListEntries.Ace.Matches.SourcePortRange',
            False, 
            [
            _MetaInfoClassMember('lower-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Lower boundary for port.
                ''',
                'lower_port',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('upper-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Upper boundary for port . If existing, the upper port
                must be greater or equal to lower-port.
                ''',
                'upper_port',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'source-port-range',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AccessListEntries.Ace.Matches.DestinationPortRange' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AccessListEntries.Ace.Matches.DestinationPortRange',
            False, 
            [
            _MetaInfoClassMember('lower-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Lower boundary for port.
                ''',
                'lower_port',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('upper-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Upper boundary for port. If existing, the upper port must
                be greater or equal to lower-port
                ''',
                'upper_port',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'destination-port-range',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AccessListEntries.Ace.Matches' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AccessListEntries.Ace.Matches',
            False, 
            [
            _MetaInfoClassMember('destination-ipv4-network', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                Destination IPv4 address prefix.
                ''',
                'destination_ipv4_network',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('destination-ipv6-network', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Destination IPv6 address prefix.
                ''',
                'destination_ipv6_network',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('destination-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Destination IEEE 802 MAC address.
                ''',
                'destination_mac_address',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('destination-mac-address-mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Destination IEEE 802 MAC address mask.
                ''',
                'destination_mac_address_mask',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('destination-port-range', REFERENCE_CLASS, 'DestinationPortRange' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AccessListEntries.Ace.Matches.DestinationPortRange', 
                [], [], 
                '''                Inclusive range representing destination ports to be used. When
                       only lower-port is present, it represents a single port.
                ''',
                'destination_port_range',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Value of dscp.
                ''',
                'dscp',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('flow-label', ATTRIBUTE, 'int' , None, None, 
                [('0', '1048575')], [], 
                '''                IPv6 Flow label.
                ''',
                'flow_label',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('protocol', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Internet Protocol number.
                ''',
                'protocol',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('source-ipv4-network', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                '''                Source IPv4 address prefix.
                ''',
                'source_ipv4_network',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('source-ipv6-network', ATTRIBUTE, 'str' , None, None, 
                [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                '''                Source IPv6 address prefix.
                ''',
                'source_ipv6_network',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('source-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source IEEE 802 MAC address.
                ''',
                'source_mac_address',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('source-mac-address-mask', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source IEEE 802 MAC address mask.
                ''',
                'source_mac_address_mask',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('source-port-range', REFERENCE_CLASS, 'SourcePortRange' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AccessListEntries.Ace.Matches.SourcePortRange', 
                [], [], 
                '''                Inclusive range representing source ports to be used.
                When only lower-port is present, it represents a single port.
                ''',
                'source_port_range',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'matches',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AccessListEntries.Ace.Actions' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AccessListEntries.Ace.Actions',
            False, 
            [
            _MetaInfoClassMember('deny', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Deny action.
                ''',
                'deny',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('permit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Permit action.
                ''',
                'permit',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'actions',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AccessListEntries.Ace.AceOperData' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AccessListEntries.Ace.AceOperData',
            False, 
            [
            _MetaInfoClassMember('match-counter', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Number of matches for this Access List Entry
                ''',
                'match_counter',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'ace-oper-data',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AccessListEntries.Ace' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AccessListEntries.Ace',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A unique name identifying this Access List
                Entry(ACE).
                ''',
                'rule_name',
                'ietf-access-control-list', True),
            _MetaInfoClassMember('ace-oper-data', REFERENCE_CLASS, 'AceOperData' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AccessListEntries.Ace.AceOperData', 
                [], [], 
                '''                Operational data for this Access List Entry.
                ''',
                'ace_oper_data',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('actions', REFERENCE_CLASS, 'Actions' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AccessListEntries.Ace.Actions', 
                [], [], 
                '''                Definitions of action criteria for this Access List
                Entry.
                ''',
                'actions',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('matches', REFERENCE_CLASS, 'Matches' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AccessListEntries.Ace.Matches', 
                [], [], 
                '''                Definitions for match criteria for this Access List
                Entry.
                ''',
                'matches',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'ace',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl.AccessListEntries' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl.AccessListEntries',
            False, 
            [
            _MetaInfoClassMember('ace', REFERENCE_LIST, 'Ace' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AccessListEntries.Ace', 
                [], [], 
                '''                List of access list entries(ACE)
                ''',
                'ace',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'access-list-entries',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists.Acl' : {
        'meta_info' : _MetaInfoClass('AccessLists.Acl',
            False, 
            [
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of access-list. A device MAY restrict the length
                and value of this name, possibly space and special
                characters are not allowed.
                ''',
                'acl_name',
                'ietf-access-control-list', True),
            _MetaInfoClassMember('acl-type', REFERENCE_IDENTITY_CLASS, 'AclBaseIdentity' , 'ydk.models.ietf.ietf_access_control_list', 'AclBaseIdentity', 
                [], [], 
                '''                Type of access control list. Indicates the primary intended
                type of match criteria (e.g. ethernet, IPv4, IPv6, mixed, etc)
                used in the list instance.
                ''',
                'acl_type',
                'ietf-access-control-list', True),
            _MetaInfoClassMember('access-list-entries', REFERENCE_CLASS, 'AccessListEntries' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AccessListEntries', 
                [], [], 
                '''                The access-list-entries container contains
                a list of access-list-entries(ACE).
                ''',
                'access_list_entries',
                'ietf-access-control-list', False),
            _MetaInfoClassMember('acl-oper-data', REFERENCE_CLASS, 'AclOperData' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl.AclOperData', 
                [], [], 
                '''                Overall Access Control List operational data
                ''',
                'acl_oper_data',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'acl',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'AccessLists' : {
        'meta_info' : _MetaInfoClass('AccessLists',
            False, 
            [
            _MetaInfoClassMember('acl', REFERENCE_LIST, 'Acl' , 'ydk.models.ietf.ietf_access_control_list', 'AccessLists.Acl', 
                [], [], 
                '''                An Access Control List(ACL) is an ordered list of
                Access List Entries (ACE). Each Access Control Entry has a
                list of match criteria and a list of actions.
                Since there are several kinds of Access Control Lists
                implemented with different attributes for
                different vendors, this
                model accommodates customizing Access Control Lists for
                each kind and for each vendor.
                ''',
                'acl',
                'ietf-access-control-list', False),
            ],
            'ietf-access-control-list',
            'access-lists',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'Ipv6AclIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv6AclIdentity',
            False, 
            [
            ],
            'ietf-access-control-list',
            'ipv6-acl',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'Ipv4AclIdentity' : {
        'meta_info' : _MetaInfoClass('Ipv4AclIdentity',
            False, 
            [
            ],
            'ietf-access-control-list',
            'ipv4-acl',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
    'EthAclIdentity' : {
        'meta_info' : _MetaInfoClass('EthAclIdentity',
            False, 
            [
            ],
            'ietf-access-control-list',
            'eth-acl',
            _yang_ns._namespaces['ietf-access-control-list'],
        'ydk.models.ietf.ietf_access_control_list'
        ),
    },
}
_meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches.SourcePortRange']['meta_info'].parent =_meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches']['meta_info']
_meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches.DestinationPortRange']['meta_info'].parent =_meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches']['meta_info']
_meta_table['AccessLists.Acl.AccessListEntries.Ace.Matches']['meta_info'].parent =_meta_table['AccessLists.Acl.AccessListEntries.Ace']['meta_info']
_meta_table['AccessLists.Acl.AccessListEntries.Ace.Actions']['meta_info'].parent =_meta_table['AccessLists.Acl.AccessListEntries.Ace']['meta_info']
_meta_table['AccessLists.Acl.AccessListEntries.Ace.AceOperData']['meta_info'].parent =_meta_table['AccessLists.Acl.AccessListEntries.Ace']['meta_info']
_meta_table['AccessLists.Acl.AccessListEntries.Ace']['meta_info'].parent =_meta_table['AccessLists.Acl.AccessListEntries']['meta_info']
_meta_table['AccessLists.Acl.AclOperData']['meta_info'].parent =_meta_table['AccessLists.Acl']['meta_info']
_meta_table['AccessLists.Acl.AccessListEntries']['meta_info'].parent =_meta_table['AccessLists.Acl']['meta_info']
_meta_table['AccessLists.Acl']['meta_info'].parent =_meta_table['AccessLists']['meta_info']
