


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CfmLastClearedTypeEnum' : _MetaInfoEnum('CfmLastClearedTypeEnum', 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper',
        {
            'never-cleared':'never_cleared',
            'cleared-before':'cleared_before',
        }, 'Cisco-IOS-XE-cfm-oper', _yang_ns._namespaces['Cisco-IOS-XE-cfm-oper']),
    'CfmStatistics.CfmMeps.CfmMep.LastCleared' : {
        'meta_info' : _MetaInfoClass('CfmStatistics.CfmMeps.CfmMep.LastCleared',
            False, 
            [
            _MetaInfoClassMember('never', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                ''',
                'never',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'time',
                'Cisco-IOS-XE-cfm-oper', False),
            ],
            'Cisco-IOS-XE-cfm-oper',
            'last-cleared',
            _yang_ns._namespaces['Cisco-IOS-XE-cfm-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper'
        ),
    },
    'CfmStatistics.CfmMeps.CfmMep' : {
        'meta_info' : _MetaInfoClass('CfmStatistics.CfmMeps.CfmMep',
            False, 
            [
            _MetaInfoClassMember('domain-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the Domain corresponding the the MEP.
                ''',
                'domain_name',
                'Cisco-IOS-XE-cfm-oper', True),
            _MetaInfoClassMember('ma-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The name of the MA corresponding the the MEP.
                ''',
                'ma_name',
                'Cisco-IOS-XE-cfm-oper', True),
            _MetaInfoClassMember('mpid', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ID of the MEP
                ''',
                'mpid',
                'Cisco-IOS-XE-cfm-oper', True),
            _MetaInfoClassMember('ccm-seq-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of CCM sequence number errors detected.
                ''',
                'ccm_seq_errors',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('ccm-transmitted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of CCMs transmitted from the local MEP.
                ''',
                'ccm_transmitted',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('last-cleared', REFERENCE_CLASS, 'LastCleared' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper', 'CfmStatistics.CfmMeps.CfmMep.LastCleared', 
                [], [], 
                '''                ''',
                'last_cleared',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('lbr-received-bad', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of loopback reply packets received 
                with corrupted data pattern
                ''',
                'lbr_received_bad',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('lbr-received-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of valid loopback reply packets received.
                ''',
                'lbr_received_ok',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('lbr-seq-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of loopback reply packets received 
                with sequence number errors.
                ''',
                'lbr_seq_errors',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('lbr-transmitted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of loopback reply packets transmitted
                from the local MEP.
                ''',
                'lbr_transmitted',
                'Cisco-IOS-XE-cfm-oper', False),
            _MetaInfoClassMember('ltr-unexpected', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The number of unexpected linktrace reply packets 
                received at this MEP.
                ''',
                'ltr_unexpected',
                'Cisco-IOS-XE-cfm-oper', False),
            ],
            'Cisco-IOS-XE-cfm-oper',
            'cfm-mep',
            _yang_ns._namespaces['Cisco-IOS-XE-cfm-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper'
        ),
    },
    'CfmStatistics.CfmMeps' : {
        'meta_info' : _MetaInfoClass('CfmStatistics.CfmMeps',
            False, 
            [
            _MetaInfoClassMember('cfm-mep', REFERENCE_LIST, 'CfmMep' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper', 'CfmStatistics.CfmMeps.CfmMep', 
                [], [], 
                '''                The list of MEP entries in the system.
                ''',
                'cfm_mep',
                'Cisco-IOS-XE-cfm-oper', False),
            ],
            'Cisco-IOS-XE-cfm-oper',
            'cfm-meps',
            _yang_ns._namespaces['Cisco-IOS-XE-cfm-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper'
        ),
    },
    'CfmStatistics' : {
        'meta_info' : _MetaInfoClass('CfmStatistics',
            False, 
            [
            _MetaInfoClassMember('cfm-meps', REFERENCE_CLASS, 'CfmMeps' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper', 'CfmStatistics.CfmMeps', 
                [], [], 
                '''                ''',
                'cfm_meps',
                'Cisco-IOS-XE-cfm-oper', False),
            ],
            'Cisco-IOS-XE-cfm-oper',
            'cfm-statistics',
            _yang_ns._namespaces['Cisco-IOS-XE-cfm-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_cfm_oper'
        ),
    },
}
_meta_table['CfmStatistics.CfmMeps.CfmMep.LastCleared']['meta_info'].parent =_meta_table['CfmStatistics.CfmMeps.CfmMep']['meta_info']
_meta_table['CfmStatistics.CfmMeps.CfmMep']['meta_info'].parent =_meta_table['CfmStatistics.CfmMeps']['meta_info']
_meta_table['CfmStatistics.CfmMeps']['meta_info'].parent =_meta_table['CfmStatistics']['meta_info']
