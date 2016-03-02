


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'MplsIpTtlPropagateDisable_Enum' : _MetaInfoEnum('MplsIpTtlPropagateDisable_Enum', 'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg',
        {
            'all':'ALL',
            'forward':'FORWARD',
            'local':'LOCAL',
        }, 'Cisco-IOS-XR-mpls-lsd-cfg', _yang_ns._namespaces['Cisco-IOS-XR-mpls-lsd-cfg']),
    'MplsLsd.LabelDatabases.LabelDatabase.LabelRange' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases.LabelDatabase.LabelRange',
            False, 
            [
            _MetaInfoClassMember('max-static-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 1048575)], [], 
                '''                Maximum static label value
                ''',
                'max_static_value',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('max-value', ATTRIBUTE, 'int' , None, None, 
                [(16000, 1048575)], [], 
                '''                Maximum label value
                ''',
                'max_value',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('min-static-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 1048575)], [], 
                '''                Minimum static label value
                ''',
                'min_static_value',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('minvalue', ATTRIBUTE, 'int' , None, None, 
                [(16000, 1048575)], [], 
                '''                Minimum label value
                ''',
                'minvalue',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-range',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-lsd-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg'
        ),
    },
    'MplsLsd.LabelDatabases.LabelDatabase' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases.LabelDatabase',
            False, 
            [
            _MetaInfoClassMember('label-database-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Label database identifier
                ''',
                'label_database_id',
                'Cisco-IOS-XR-mpls-lsd-cfg', True),
            _MetaInfoClassMember('label-range', REFERENCE_CLASS, 'LabelRange' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases.LabelDatabase.LabelRange', 
                [], [], 
                '''                Label range
                ''',
                'label_range',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-database',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-lsd-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg'
        ),
    },
    'MplsLsd.LabelDatabases' : {
        'meta_info' : _MetaInfoClass('MplsLsd.LabelDatabases',
            False, 
            [
            _MetaInfoClassMember('label-database', REFERENCE_LIST, 'LabelDatabase' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases.LabelDatabase', 
                [], [], 
                '''                A label database
                ''',
                'label_database',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'label-databases',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-lsd-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg'
        ),
    },
    'MplsLsd' : {
        'meta_info' : _MetaInfoClass('MplsLsd',
            False, 
            [
            _MetaInfoClassMember('app-reg-delay-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable LSD application reg delay
                ''',
                'app_reg_delay_disable',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('label-databases', REFERENCE_CLASS, 'LabelDatabases' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsLsd.LabelDatabases', 
                [], [], 
                '''                Table of label databases
                ''',
                'label_databases',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('mpls-entropy-label', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enable MPLS Entropy Label
                ''',
                'mpls_entropy_label',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('mpls-ip-ttl-expiration-pop', ATTRIBUTE, 'int' , None, None, 
                [(1, 10)], [], 
                '''                Number of labels to pop upon MPLS TTL expiry
                ''',
                'mpls_ip_ttl_expiration_pop',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            _MetaInfoClassMember('mpls-ip-ttl-propagate-disable', REFERENCE_ENUM_CLASS, 'MplsIpTtlPropagateDisable_Enum' , 'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg', 'MplsIpTtlPropagateDisable_Enum', 
                [], [], 
                '''                Disable Propagation of IP TTL onto the label
                stack
                ''',
                'mpls_ip_ttl_propagate_disable',
                'Cisco-IOS-XR-mpls-lsd-cfg', False),
            ],
            'Cisco-IOS-XR-mpls-lsd-cfg',
            'mpls-lsd',
            _yang_ns._namespaces['Cisco-IOS-XR-mpls-lsd-cfg'],
        'ydk.models.mpls.Cisco_IOS_XR_mpls_lsd_cfg'
        ),
    },
}
_meta_table['MplsLsd.LabelDatabases.LabelDatabase.LabelRange']['meta_info'].parent =_meta_table['MplsLsd.LabelDatabases.LabelDatabase']['meta_info']
_meta_table['MplsLsd.LabelDatabases.LabelDatabase']['meta_info'].parent =_meta_table['MplsLsd.LabelDatabases']['meta_info']
_meta_table['MplsLsd.LabelDatabases']['meta_info'].parent =_meta_table['MplsLsd']['meta_info']
