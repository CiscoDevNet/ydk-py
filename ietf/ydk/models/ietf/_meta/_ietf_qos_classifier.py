


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'FilterTypeIdentity' : {
        'meta_info' : _MetaInfoClass('FilterTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'filter-type',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'ClassifierEntryFilterOperationTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ClassifierEntryFilterOperationTypeIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'classifier-entry-filter-operation-type',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.DscpCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.DscpCfg',
            False, 
            [
            _MetaInfoClassMember('dscp-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                maximum value of dscp min-max range
                ''',
                'dscp_max',
                'ietf-diffserv', True),
            _MetaInfoClassMember('dscp-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Minimum value of dscp min-max range
                ''',
                'dscp_min',
                'ietf-diffserv', True),
            ],
            'ietf-diffserv',
            'dscp-cfg',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg',
            False, 
            [
            _MetaInfoClassMember('source-ip-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                source ipv4 or ipv6 prefix
                ''',
                'source_ip_addr',
                'ietf-diffserv', True, [
                    _MetaInfoClassMember('source-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        source ipv4 or ipv6 prefix
                        ''',
                        'source_ip_addr',
                        'ietf-diffserv', True),
                    _MetaInfoClassMember('source-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        source ipv4 or ipv6 prefix
                        ''',
                        'source_ip_addr',
                        'ietf-diffserv', True),
                ]),
            ],
            'ietf-diffserv',
            'source-ip-address-cfg',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg',
            False, 
            [
            _MetaInfoClassMember('destination-ip-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                destination ipv4 or ipv6 prefix
                ''',
                'destination_ip_addr',
                'ietf-diffserv', True, [
                    _MetaInfoClassMember('destination-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        destination ipv4 or ipv6 prefix
                        ''',
                        'destination_ip_addr',
                        'ietf-diffserv', True),
                    _MetaInfoClassMember('destination-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        destination ipv4 or ipv6 prefix
                        ''',
                        'destination_ip_addr',
                        'ietf-diffserv', True),
                ]),
            ],
            'ietf-diffserv',
            'destination-ip-address-cfg',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg',
            False, 
            [
            _MetaInfoClassMember('source-port-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                maximum value of source port range
                ''',
                'source_port_max',
                'ietf-diffserv', True),
            _MetaInfoClassMember('source-port-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                minimum value of source port range
                ''',
                'source_port_min',
                'ietf-diffserv', True),
            ],
            'ietf-diffserv',
            'source-port-cfg',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg',
            False, 
            [
            _MetaInfoClassMember('destination-port-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                maximum value of destination port range
                ''',
                'destination_port_max',
                'ietf-diffserv', True),
            _MetaInfoClassMember('destination-port-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                minimum value of destination port range
                ''',
                'destination_port_min',
                'ietf-diffserv', True),
            ],
            'ietf-diffserv',
            'destination-port-cfg',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg',
            False, 
            [
            _MetaInfoClassMember('protocol-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                maximum value of protocol range
                ''',
                'protocol_max',
                'ietf-diffserv', True),
            _MetaInfoClassMember('protocol-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                minimum value of protocol range
                ''',
                'protocol_min',
                'ietf-diffserv', True),
            ],
            'ietf-diffserv',
            'protocol-cfg',
            _yang_ns._namespaces['ietf-diffserv'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry',
            False, 
            [
            _MetaInfoClassMember('filter-logical-not', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                
                This is logical-not operator for a filter. When true, it
                indicates filter looks for absence of a pattern defined
                by the filter
                
                ''',
                'filter_logical_not',
                'ietf-qos-classifier', True),
            _MetaInfoClassMember('filter-type', REFERENCE_IDENTITY_CLASS, 'FilterTypeIdentity' , 'ydk.models.ietf.ietf_qos_classifier', 'FilterTypeIdentity', 
                [], [], 
                '''                This leaf defines type of the filter
                ''',
                'filter_type',
                'ietf-qos-classifier', True),
            _MetaInfoClassMember('destination-ip-address-cfg', REFERENCE_LIST, 'DestinationIpAddressCfg' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg', 
                [], [], 
                '''                list of destination ipv4 or ipv6 address
                ''',
                'destination_ip_address_cfg',
                'ietf-diffserv', False),
            _MetaInfoClassMember('destination-port-cfg', REFERENCE_LIST, 'DestinationPortCfg' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg', 
                [], [], 
                '''                list of ranges of destination port
                ''',
                'destination_port_cfg',
                'ietf-diffserv', False),
            _MetaInfoClassMember('dscp-cfg', REFERENCE_LIST, 'DscpCfg' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry.FilterEntry.DscpCfg', 
                [], [], 
                '''                list of dscp ranges
                ''',
                'dscp_cfg',
                'ietf-diffserv', False),
            _MetaInfoClassMember('protocol-cfg', REFERENCE_LIST, 'ProtocolCfg' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg', 
                [], [], 
                '''                list of ranges of protocol values
                ''',
                'protocol_cfg',
                'ietf-diffserv', False),
            _MetaInfoClassMember('source-ip-address-cfg', REFERENCE_LIST, 'SourceIpAddressCfg' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg', 
                [], [], 
                '''                list of source ipv4 or ipv6 address
                ''',
                'source_ip_address_cfg',
                'ietf-diffserv', False),
            _MetaInfoClassMember('source-port-cfg', REFERENCE_LIST, 'SourcePortCfg' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg', 
                [], [], 
                '''                list of ranges of source port
                ''',
                'source_port_cfg',
                'ietf-diffserv', False),
            ],
            'ietf-qos-classifier',
            'filter-entry',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers.ClassifierEntry' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry',
            False, 
            [
            _MetaInfoClassMember('classifier-entry-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                classifier entry name
                ''',
                'classifier_entry_name',
                'ietf-qos-classifier', True),
            _MetaInfoClassMember('classifier-entry-descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                classifier entry description statement
                ''',
                'classifier_entry_descr',
                'ietf-qos-classifier', False),
            _MetaInfoClassMember('classifier-entry-filter-operation', REFERENCE_IDENTITY_CLASS, 'ClassifierEntryFilterOperationTypeIdentity' , 'ydk.models.ietf.ietf_qos_classifier', 'ClassifierEntryFilterOperationTypeIdentity', 
                [], [], 
                '''                Filters are applicable as match-any or match-all filters
                ''',
                'classifier_entry_filter_operation',
                'ietf-qos-classifier', False),
            _MetaInfoClassMember('filter-entry', REFERENCE_LIST, 'FilterEntry' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry.FilterEntry', 
                [], [], 
                '''                Filter entry configuration
                ''',
                'filter_entry',
                'ietf-qos-classifier', False),
            ],
            'ietf-qos-classifier',
            'classifier-entry',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'Classifiers' : {
        'meta_info' : _MetaInfoClass('Classifiers',
            False, 
            [
            _MetaInfoClassMember('classifier-entry', REFERENCE_LIST, 'ClassifierEntry' , 'ydk.models.ietf.ietf_qos_classifier', 'Classifiers.ClassifierEntry', 
                [], [], 
                '''                each classifier entry contains a list of filters
                ''',
                'classifier_entry',
                'ietf-qos-classifier', False),
            ],
            'ietf-qos-classifier',
            'classifiers',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'DestinationPortIdentity' : {
        'meta_info' : _MetaInfoClass('DestinationPortIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'destination-port',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'ProtocolIdentity' : {
        'meta_info' : _MetaInfoClass('ProtocolIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'protocol',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'DestinationIpAddressIdentity' : {
        'meta_info' : _MetaInfoClass('DestinationIpAddressIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'destination-ip-address',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'DscpIdentity' : {
        'meta_info' : _MetaInfoClass('DscpIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'dscp',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'MatchAllFilterIdentity' : {
        'meta_info' : _MetaInfoClass('MatchAllFilterIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'match-all-filter',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'SourceIpAddressIdentity' : {
        'meta_info' : _MetaInfoClass('SourceIpAddressIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'source-ip-address',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'MatchAnyFilterIdentity' : {
        'meta_info' : _MetaInfoClass('MatchAnyFilterIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'match-any-filter',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
    'SourcePortIdentity' : {
        'meta_info' : _MetaInfoClass('SourcePortIdentity',
            False, 
            [
            ],
            'ietf-qos-classifier',
            'source-port',
            _yang_ns._namespaces['ietf-qos-classifier'],
        'ydk.models.ietf.ietf_qos_classifier'
        ),
    },
}
_meta_table['Classifiers.ClassifierEntry.FilterEntry.DscpCfg']['meta_info'].parent =_meta_table['Classifiers.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg']['meta_info'].parent =_meta_table['Classifiers.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg']['meta_info'].parent =_meta_table['Classifiers.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg']['meta_info'].parent =_meta_table['Classifiers.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg']['meta_info'].parent =_meta_table['Classifiers.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg']['meta_info'].parent =_meta_table['Classifiers.ClassifierEntry.FilterEntry']['meta_info']
_meta_table['Classifiers.ClassifierEntry.FilterEntry']['meta_info'].parent =_meta_table['Classifiers.ClassifierEntry']['meta_info']
_meta_table['Classifiers.ClassifierEntry']['meta_info'].parent =_meta_table['Classifiers']['meta_info']
