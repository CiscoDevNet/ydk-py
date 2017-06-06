


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EfpStats.EfpStat' : {
        'meta_info' : _MetaInfoClass('EfpStats.EfpStat',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'id',
                'Cisco-IOS-XE-efp-oper', True),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'interface',
                'Cisco-IOS-XE-efp-oper', True),
            _MetaInfoClassMember('in-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ''',
                'in_bytes',
                'Cisco-IOS-XE-efp-oper', False),
            _MetaInfoClassMember('in-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ''',
                'in_pkts',
                'Cisco-IOS-XE-efp-oper', False),
            _MetaInfoClassMember('out-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ''',
                'out_bytes',
                'Cisco-IOS-XE-efp-oper', False),
            _MetaInfoClassMember('out-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                ''',
                'out_pkts',
                'Cisco-IOS-XE-efp-oper', False),
            ],
            'Cisco-IOS-XE-efp-oper',
            'efp-stat',
            _yang_ns._namespaces['Cisco-IOS-XE-efp-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_efp_oper'
        ),
    },
    'EfpStats' : {
        'meta_info' : _MetaInfoClass('EfpStats',
            False, 
            [
            _MetaInfoClassMember('efp-stat', REFERENCE_LIST, 'EfpStat' , 'ydk.models.cisco_ios_xe.Cisco_IOS_XE_efp_oper', 'EfpStats.EfpStat', 
                [], [], 
                '''                ''',
                'efp_stat',
                'Cisco-IOS-XE-efp-oper', False),
            ],
            'Cisco-IOS-XE-efp-oper',
            'efp-stats',
            _yang_ns._namespaces['Cisco-IOS-XE-efp-oper'],
        'ydk.models.cisco_ios_xe.Cisco_IOS_XE_efp_oper'
        ),
    },
}
_meta_table['EfpStats.EfpStat']['meta_info'].parent =_meta_table['EfpStats']['meta_info']
