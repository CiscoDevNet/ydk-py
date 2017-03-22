


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Statistics.Period.ServiceAccounting' : {
        'meta_info' : _MetaInfoClass('Statistics.Period.ServiceAccounting',
            False, 
            [
            _MetaInfoClassMember('polling-disable', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Disable periodic statistics polling for
                service accounting collectors
                ''',
                'polling_disable',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            _MetaInfoClassMember('polling-period', ATTRIBUTE, 'int' , None, None, 
                [('30', '3600')], [], 
                '''                Collection polling period for service
                accounting collectors
                ''',
                'polling_period',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-statsd-cfg',
            'service-accounting',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-statsd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg'
        ),
    },
    'Statistics.Period' : {
        'meta_info' : _MetaInfoClass('Statistics.Period',
            False, 
            [
            _MetaInfoClassMember('service-accounting', REFERENCE_CLASS, 'ServiceAccounting' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg', 'Statistics.Period.ServiceAccounting', 
                [], [], 
                '''                Collection polling period for service
                accounting collectors
                ''',
                'service_accounting',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-statsd-cfg',
            'period',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-statsd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg'
        ),
    },
    'Statistics' : {
        'meta_info' : _MetaInfoClass('Statistics',
            False, 
            [
            _MetaInfoClassMember('period', REFERENCE_CLASS, 'Period' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg', 'Statistics.Period', 
                [], [], 
                '''                Collection period for statistics polling
                ''',
                'period',
                'Cisco-IOS-XR-infra-statsd-cfg', False),
            ],
            'Cisco-IOS-XR-infra-statsd-cfg',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-statsd-cfg'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_statsd_cfg'
        ),
    },
}
_meta_table['Statistics.Period.ServiceAccounting']['meta_info'].parent =_meta_table['Statistics.Period']['meta_info']
_meta_table['Statistics.Period']['meta_info'].parent =_meta_table['Statistics']['meta_info']
