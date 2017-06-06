


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ActionTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ActionTypeIdentity',
            False, 
            [
            ],
            'ietf-diffserv-policy',
            'action-type',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg',
            False, 
            [
            _MetaInfoClassMember('dscp-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Minimum value of dscp range
                ''',
                'dscp_min',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('dscp-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                maximum value of dscp range
                ''',
                'dscp_max',
                'ietf-diffserv-policy', True),
            ],
            'ietf-diffserv-policy',
            'dscp-cfg',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg',
            False, 
            [
            _MetaInfoClassMember('source-ip-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                source ip prefix
                ''',
                'source_ip_addr',
                'ietf-diffserv-policy', True, [
                    _MetaInfoClassMember('source-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        source ip prefix
                        ''',
                        'source_ip_addr',
                        'ietf-diffserv-policy', True),
                    _MetaInfoClassMember('source-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        source ip prefix
                        ''',
                        'source_ip_addr',
                        'ietf-diffserv-policy', True),
                ]),
            ],
            'ietf-diffserv-policy',
            'source-ip-address-cfg',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg',
            False, 
            [
            _MetaInfoClassMember('destination-ip-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                destination ip prefix
                ''',
                'destination_ip_addr',
                'ietf-diffserv-policy', True, [
                    _MetaInfoClassMember('destination-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        destination ip prefix
                        ''',
                        'destination_ip_addr',
                        'ietf-diffserv-policy', True),
                    _MetaInfoClassMember('destination-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        destination ip prefix
                        ''',
                        'destination_ip_addr',
                        'ietf-diffserv-policy', True),
                ]),
            ],
            'ietf-diffserv-policy',
            'destination-ip-address-cfg',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg',
            False, 
            [
            _MetaInfoClassMember('source-port-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                minimum value of source port range
                ''',
                'source_port_min',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('source-port-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                maximum value of source port range
                ''',
                'source_port_max',
                'ietf-diffserv-policy', True),
            ],
            'ietf-diffserv-policy',
            'source-port-cfg',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg',
            False, 
            [
            _MetaInfoClassMember('destination-port-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                minimum value of destination port range
                ''',
                'destination_port_min',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('destination-port-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                maximum value of destination port range
                ''',
                'destination_port_max',
                'ietf-diffserv-policy', True),
            ],
            'ietf-diffserv-policy',
            'destination-port-cfg',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg',
            False, 
            [
            _MetaInfoClassMember('protocol-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                minimum value of protocol range
                ''',
                'protocol_min',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('protocol-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                maximum value of protocol range
                ''',
                'protocol_max',
                'ietf-diffserv-policy', True),
            ],
            'ietf-diffserv-policy',
            'protocol-cfg',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.FilterEntry' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.FilterEntry',
            False, 
            [
            _MetaInfoClassMember('filter-type', REFERENCE_IDENTITY_CLASS, 'FilterTypeIdentity' , 'ydk.models.ietf.ietf_diffserv_classifier', 'FilterTypeIdentity', 
                [], [], 
                '''                This leaf defines type of the filter
                ''',
                'filter_type',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('filter-logical-not', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                
                This is logical-not operator for a filter. When true, it 
                indicates filter looks for absence of a pattern defined 
                by the filter
                
                ''',
                'filter_logical_not',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('destination-ip-address-cfg', REFERENCE_LIST, 'DestinationIpAddressCfg' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg', 
                [], [], 
                '''                list of destination ip address
                ''',
                'destination_ip_address_cfg',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('destination-port-cfg', REFERENCE_LIST, 'DestinationPortCfg' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg', 
                [], [], 
                '''                list of ranges of destination port
                ''',
                'destination_port_cfg',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('dscp-cfg', REFERENCE_LIST, 'DscpCfg' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg', 
                [], [], 
                '''                list of dscp ranges
                ''',
                'dscp_cfg',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('protocol-cfg', REFERENCE_LIST, 'ProtocolCfg' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg', 
                [], [], 
                '''                list of ranges of protocol values
                ''',
                'protocol_cfg',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('source-ip-address-cfg', REFERENCE_LIST, 'SourceIpAddressCfg' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg', 
                [], [], 
                '''                list of source ip address
                ''',
                'source_ip_address_cfg',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('source-port-cfg', REFERENCE_LIST, 'SourcePortCfg' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg', 
                [], [], 
                '''                list of ranges of source port
                ''',
                'source_port_cfg',
                'ietf-diffserv-policy', False),
            ],
            'ietf-diffserv-policy',
            'filter-entry',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg',
            False, 
            [
            _MetaInfoClassMember('action-type', REFERENCE_IDENTITY_CLASS, 'ActionTypeIdentity' , 'ydk.models.ietf.ietf_diffserv_policy', 'ActionTypeIdentity', 
                [], [], 
                '''                This defines action type 
                ''',
                'action_type',
                'ietf-diffserv-policy', True),
            ],
            'ietf-diffserv-policy',
            'classifier-action-entry-cfg',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry.ClassifierEntry' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry.ClassifierEntry',
            False, 
            [
            _MetaInfoClassMember('classifier-entry-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diffserv classifier entry name
                ''',
                'classifier_entry_name',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('classifier-action-entry-cfg', REFERENCE_LIST, 'ClassifierActionEntryCfg' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg', 
                [], [], 
                '''                Configuration of classifier & associated actions
                ''',
                'classifier_action_entry_cfg',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('classifier-entry-filter-oper', REFERENCE_IDENTITY_CLASS, 'ClassifierEntryFilterOperationTypeIdentity' , 'ydk.models.ietf.ietf_diffserv_classifier', 'ClassifierEntryFilterOperationTypeIdentity', 
                [], [], 
                '''                Filters are applicable as any or all filters
                ''',
                'classifier_entry_filter_oper',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('classifier-entry-inline', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indication of inline classifier entry
                ''',
                'classifier_entry_inline',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('filter-entry', REFERENCE_LIST, 'FilterEntry' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry.FilterEntry', 
                [], [], 
                '''                Filters configured inline in a policy
                ''',
                'filter_entry',
                'ietf-diffserv-policy', False),
            ],
            'ietf-diffserv-policy',
            'classifier-entry',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies.PolicyEntry' : {
        'meta_info' : _MetaInfoClass('Policies.PolicyEntry',
            False, 
            [
            _MetaInfoClassMember('policy-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diffserv policy name
                ''',
                'policy_name',
                'ietf-diffserv-policy', True),
            _MetaInfoClassMember('classifier-entry', REFERENCE_LIST, 'ClassifierEntry' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry.ClassifierEntry', 
                [], [], 
                '''                Classifier entry configuration in a policy
                ''',
                'classifier_entry',
                'ietf-diffserv-policy', False),
            _MetaInfoClassMember('policy-descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diffserv policy description
                ''',
                'policy_descr',
                'ietf-diffserv-policy', False),
            ],
            'ietf-diffserv-policy',
            'policy-entry',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
    'Policies' : {
        'meta_info' : _MetaInfoClass('Policies',
            False, 
            [
            _MetaInfoClassMember('policy-entry', REFERENCE_LIST, 'PolicyEntry' , 'ydk.models.ietf.ietf_diffserv_policy', 'Policies.PolicyEntry', 
                [], [], 
                '''                policy template
                ''',
                'policy_entry',
                'ietf-diffserv-policy', False),
            ],
            'ietf-diffserv-policy',
            'policies',
            _yang_ns._namespaces['ietf-diffserv-policy'],
        'ydk.models.ietf.ietf_diffserv_policy'
        ),
    },
}
_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.DscpCfg']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourceIpAddressCfg']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationIpAddressCfg']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.SourcePortCfg']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.DestinationPortCfg']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry.ProtocolCfg']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry.FilterEntry']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry.ClassifierActionEntryCfg']['meta_info'].parent =_meta_table['Policies.PolicyEntry.ClassifierEntry']['meta_info']
_meta_table['Policies.PolicyEntry.ClassifierEntry']['meta_info'].parent =_meta_table['Policies.PolicyEntry']['meta_info']
_meta_table['Policies.PolicyEntry']['meta_info'].parent =_meta_table['Policies']['meta_info']
