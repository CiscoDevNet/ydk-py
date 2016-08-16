


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Ipv4Acls.Ipv4Acl',
            False, 
            [
            _MetaInfoClassMember('acl-name', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                ACL name
                ''',
                'acl_name',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('acl-rate', ATTRIBUTE, 'int' , None, None, 
                [(0, 100000)], [], 
                '''                pre-ifib policer rate config commands
                ''',
                'acl_rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipv4acl',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Ipv4Acls' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Ipv4Acls',
            False, 
            [
            _MetaInfoClassMember('ipv4acl', REFERENCE_LIST, 'Ipv4Acl' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Ipv4Acls.Ipv4Acl', 
                [], [], 
                '''                ACL name
                ''',
                'ipv4acl',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipv4acls',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Flows.Flow.Precedences' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows.Flow.Precedences',
            False, 
            [
            _MetaInfoClassMember('precedence', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Precedence values
                ''',
                'precedence',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, [
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'LptsPreIFibPrecedenceNumberEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsPreIFibPrecedenceNumberEnum', 
                        [], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                    _MetaInfoClassMember('precedence', REFERENCE_LEAFLIST, 'int' , None, None, 
                        [(0, 7)], [], 
                        '''                        Precedence values
                        ''',
                        'precedence',
                        'Cisco-IOS-XR-lpts-pre-ifib-cfg', False, max_elements=8),
                ], max_elements=8),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'precedences',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Flows.Flow' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows.Flow',
            False, 
            [
            _MetaInfoClassMember('flow-type', REFERENCE_ENUM_CLASS, 'LptsFlowEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_pre_ifib_cfg', 'LptsFlowEnum', 
                [], [], 
                '''                LPTS Flow Type
                ''',
                'flow_type',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', True),
            _MetaInfoClassMember('precedences', REFERENCE_CLASS, 'Precedences' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows.Flow.Precedences', 
                [], [], 
                '''                TOS Precedence value(s)
                ''',
                'precedences',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Configured rate value
                ''',
                'rate',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flow',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer.Flows' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer.Flows',
            False, 
            [
            _MetaInfoClassMember('flow', REFERENCE_LIST, 'Flow' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows.Flow', 
                [], [], 
                '''                selected flow type
                ''',
                'flow',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'flows',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts.Ipolicer' : {
        'meta_info' : _MetaInfoClass('Lpts.Ipolicer',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Enabled
                ''',
                'enable',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('flows', REFERENCE_CLASS, 'Flows' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Flows', 
                [], [], 
                '''                Table for Flows
                ''',
                'flows',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            _MetaInfoClassMember('ipv4acls', REFERENCE_CLASS, 'Ipv4Acls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer.Ipv4Acls', 
                [], [], 
                '''                Table for ACLs
                ''',
                'ipv4acls',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-pre-ifib-cfg',
            'ipolicer',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-pre-ifib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
    'Lpts' : {
        'meta_info' : _MetaInfoClass('Lpts',
            False, 
            [
            _MetaInfoClassMember('ipolicer', REFERENCE_CLASS, 'Ipolicer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg', 'Lpts.Ipolicer', 
                [], [], 
                '''                Pre IFiB Configuration 
                ''',
                'ipolicer',
                'Cisco-IOS-XR-lpts-pre-ifib-cfg', False),
            ],
            'Cisco-IOS-XR-lpts-lib-cfg',
            'lpts',
            _yang_ns._namespaces['Cisco-IOS-XR-lpts-lib-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_lpts_lib_cfg'
        ),
    },
}
_meta_table['Lpts.Ipolicer.Ipv4Acls.Ipv4Acl']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Ipv4Acls']['meta_info']
_meta_table['Lpts.Ipolicer.Flows.Flow.Precedences']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info']
_meta_table['Lpts.Ipolicer.Flows.Flow']['meta_info'].parent =_meta_table['Lpts.Ipolicer.Flows']['meta_info']
_meta_table['Lpts.Ipolicer.Ipv4Acls']['meta_info'].parent =_meta_table['Lpts.Ipolicer']['meta_info']
_meta_table['Lpts.Ipolicer.Flows']['meta_info'].parent =_meta_table['Lpts.Ipolicer']['meta_info']
_meta_table['Lpts.Ipolicer']['meta_info'].parent =_meta_table['Lpts']['meta_info']
