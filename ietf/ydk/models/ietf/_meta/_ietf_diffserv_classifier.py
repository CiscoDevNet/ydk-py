


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'FilterTypeIdentity' : {
        'meta_info' : _MetaInfoClass('FilterTypeIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'filter-type',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'ClassifierEntryFilterOperationTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ClassifierEntryFilterOperationTypeIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'classifier-entry-filter-operation-type',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.DscpCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.DscpCfg',
            False, 
            [
            _MetaInfoClassMember('dscp-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                Minimum value of dscp range
                ''',
                'dscp_min',
                'ietf-diffserv-classifier', True),
            _MetaInfoClassMember('dscp-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                maximum value of dscp range
                ''',
                'dscp_max',
                'ietf-diffserv-classifier', True),
            ],
            'ietf-diffserv-classifier',
            'dscp-cfg',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg',
            False, 
            [
            _MetaInfoClassMember('source-ip-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                source ip prefix
                ''',
                'source_ip_addr',
                'ietf-diffserv-classifier', True, [
                    _MetaInfoClassMember('source-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        source ip prefix
                        ''',
                        'source_ip_addr',
                        'ietf-diffserv-classifier', True),
                    _MetaInfoClassMember('source-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        source ip prefix
                        ''',
                        'source_ip_addr',
                        'ietf-diffserv-classifier', True),
                ]),
            ],
            'ietf-diffserv-classifier',
            'source-ip-address-cfg',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg',
            False, 
            [
            _MetaInfoClassMember('destination-ip-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                destination ip prefix
                ''',
                'destination_ip_addr',
                'ietf-diffserv-classifier', True, [
                    _MetaInfoClassMember('destination-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        destination ip prefix
                        ''',
                        'destination_ip_addr',
                        'ietf-diffserv-classifier', True),
                    _MetaInfoClassMember('destination-ip-addr', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        destination ip prefix
                        ''',
                        'destination_ip_addr',
                        'ietf-diffserv-classifier', True),
                ]),
            ],
            'ietf-diffserv-classifier',
            'destination-ip-address-cfg',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg',
            False, 
            [
            _MetaInfoClassMember('source-port-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                minimum value of source port range
                ''',
                'source_port_min',
                'ietf-diffserv-classifier', True),
            _MetaInfoClassMember('source-port-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                maximum value of source port range
                ''',
                'source_port_max',
                'ietf-diffserv-classifier', True),
            ],
            'ietf-diffserv-classifier',
            'source-port-cfg',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg',
            False, 
            [
            _MetaInfoClassMember('destination-port-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                minimum value of destination port range
                ''',
                'destination_port_min',
                'ietf-diffserv-classifier', True),
            _MetaInfoClassMember('destination-port-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                maximum value of destination port range
                ''',
                'destination_port_max',
                'ietf-diffserv-classifier', True),
            ],
            'ietf-diffserv-classifier',
            'destination-port-cfg',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg',
            False, 
            [
            _MetaInfoClassMember('protocol-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                minimum value of protocol range
                ''',
                'protocol_min',
                'ietf-diffserv-classifier', True),
            _MetaInfoClassMember('protocol-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                maximum value of protocol range
                ''',
                'protocol_max',
                'ietf-diffserv-classifier', True),
            ],
            'ietf-diffserv-classifier',
            'protocol-cfg',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry.FilterEntry' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry.FilterEntry',
            False, 
            [
            _MetaInfoClassMember('filter-type', REFERENCE_IDENTITY_CLASS, 'FilterTypeIdentity' , 'ydk.models.ietf.ietf_diffserv_classifier', 'FilterTypeIdentity', 
                [], [], 
                '''                This leaf defines type of the filter
                ''',
                'filter_type',
                'ietf-diffserv-classifier', True),
            _MetaInfoClassMember('filter-logical-not', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                
                This is logical-not operator for a filter. When true, it 
                indicates filter looks for absence of a pattern defined 
                by the filter
                
                ''',
                'filter_logical_not',
                'ietf-diffserv-classifier', True),
            _MetaInfoClassMember('destination-ip-address-cfg', REFERENCE_LIST, 'DestinationIpAddressCfg' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry.FilterEntry.DestinationIpAddressCfg', 
                [], [], 
                '''                list of destination ip address
                ''',
                'destination_ip_address_cfg',
                'ietf-diffserv-classifier', False),
            _MetaInfoClassMember('destination-port-cfg', REFERENCE_LIST, 'DestinationPortCfg' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry.FilterEntry.DestinationPortCfg', 
                [], [], 
                '''                list of ranges of destination port
                ''',
                'destination_port_cfg',
                'ietf-diffserv-classifier', False),
            _MetaInfoClassMember('dscp-cfg', REFERENCE_LIST, 'DscpCfg' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry.FilterEntry.DscpCfg', 
                [], [], 
                '''                list of dscp ranges
                ''',
                'dscp_cfg',
                'ietf-diffserv-classifier', False),
            _MetaInfoClassMember('protocol-cfg', REFERENCE_LIST, 'ProtocolCfg' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry.FilterEntry.ProtocolCfg', 
                [], [], 
                '''                list of ranges of protocol values
                ''',
                'protocol_cfg',
                'ietf-diffserv-classifier', False),
            _MetaInfoClassMember('source-ip-address-cfg', REFERENCE_LIST, 'SourceIpAddressCfg' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry.FilterEntry.SourceIpAddressCfg', 
                [], [], 
                '''                list of source ip address
                ''',
                'source_ip_address_cfg',
                'ietf-diffserv-classifier', False),
            _MetaInfoClassMember('source-port-cfg', REFERENCE_LIST, 'SourcePortCfg' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry.FilterEntry.SourcePortCfg', 
                [], [], 
                '''                list of ranges of source port
                ''',
                'source_port_cfg',
                'ietf-diffserv-classifier', False),
            ],
            'ietf-diffserv-classifier',
            'filter-entry',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers.ClassifierEntry' : {
        'meta_info' : _MetaInfoClass('Classifiers.ClassifierEntry',
            False, 
            [
            _MetaInfoClassMember('classifier-entry-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diffserv classifier name
                ''',
                'classifier_entry_name',
                'ietf-diffserv-classifier', True),
            _MetaInfoClassMember('classifier-entry-descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Description of the class template
                ''',
                'classifier_entry_descr',
                'ietf-diffserv-classifier', False),
            _MetaInfoClassMember('classifier-entry-filter-operation', REFERENCE_IDENTITY_CLASS, 'ClassifierEntryFilterOperationTypeIdentity' , 'ydk.models.ietf.ietf_diffserv_classifier', 'ClassifierEntryFilterOperationTypeIdentity', 
                [], [], 
                '''                Filters are applicable as any or all filters
                ''',
                'classifier_entry_filter_operation',
                'ietf-diffserv-classifier', False),
            _MetaInfoClassMember('filter-entry', REFERENCE_LIST, 'FilterEntry' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry.FilterEntry', 
                [], [], 
                '''                Filter configuration
                ''',
                'filter_entry',
                'ietf-diffserv-classifier', False),
            ],
            'ietf-diffserv-classifier',
            'classifier-entry',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'Classifiers' : {
        'meta_info' : _MetaInfoClass('Classifiers',
            False, 
            [
            _MetaInfoClassMember('classifier-entry', REFERENCE_LIST, 'ClassifierEntry' , 'ydk.models.ietf.ietf_diffserv_classifier', 'Classifiers.ClassifierEntry', 
                [], [], 
                '''                classifier entry template
                ''',
                'classifier_entry',
                'ietf-diffserv-classifier', False),
            ],
            'ietf-diffserv-classifier',
            'classifiers',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'ProtocolIdentity' : {
        'meta_info' : _MetaInfoClass('ProtocolIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'protocol',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'DestinationIpAddressIdentity' : {
        'meta_info' : _MetaInfoClass('DestinationIpAddressIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'destination-ip-address',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'MatchAnyFilterIdentity' : {
        'meta_info' : _MetaInfoClass('MatchAnyFilterIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'match-any-filter',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'SourcePortIdentity' : {
        'meta_info' : _MetaInfoClass('SourcePortIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'source-port',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'DscpIdentity' : {
        'meta_info' : _MetaInfoClass('DscpIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'dscp',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'DestinationPortIdentity' : {
        'meta_info' : _MetaInfoClass('DestinationPortIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'destination-port',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'SourceIpAddressIdentity' : {
        'meta_info' : _MetaInfoClass('SourceIpAddressIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'source-ip-address',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
        ),
    },
    'MatchAllFilterIdentity' : {
        'meta_info' : _MetaInfoClass('MatchAllFilterIdentity',
            False, 
            [
            ],
            'ietf-diffserv-classifier',
            'match-all-filter',
            _yang_ns._namespaces['ietf-diffserv-classifier'],
        'ydk.models.ietf.ietf_diffserv_classifier'
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
