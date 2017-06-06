


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EthTrafficClassEnum' : _MetaInfoEnum('EthTrafficClassEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_common',
        {
            'broadcast':'broadcast',
            'multicast':'multicast',
            'unknown-unicast':'unknown_unicast',
        }, 'cisco-bridge-common', _yang_ns._namespaces['cisco-bridge-common']),
    'MacAgingTypeEnum' : _MetaInfoEnum('MacAgingTypeEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_common',
        {
            'inactivity':'inactivity',
            'absolute':'absolute',
        }, 'cisco-bridge-common', _yang_ns._namespaces['cisco-bridge-common']),
    'MacSecureActionEnum' : _MetaInfoEnum('MacSecureActionEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_common',
        {
            'none':'none',
            'restrict':'restrict',
            'shutdown':'shutdown',
        }, 'cisco-bridge-common', _yang_ns._namespaces['cisco-bridge-common']),
    'MacLimitActionEnum' : _MetaInfoEnum('MacLimitActionEnum', 'ydk.models.cisco_ios_xe.cisco_bridge_common',
        {
            'none':'none',
            'flood':'flood',
            'drop':'drop',
            'shutdown':'shutdown',
        }, 'cisco-bridge-common', _yang_ns._namespaces['cisco-bridge-common']),
    'MacLimitNotificationTypeIdentity' : {
        'meta_info' : _MetaInfoClass('MacLimitNotificationTypeIdentity',
            False, 
            [
            ],
            'cisco-bridge-common',
            'mac-limit-notification-type',
            _yang_ns._namespaces['cisco-bridge-common'],
        'ydk.models.cisco_ios_xe.cisco_bridge_common'
        ),
    },
    'NotifSyslogIdentity' : {
        'meta_info' : _MetaInfoClass('NotifSyslogIdentity',
            False, 
            [
            ],
            'cisco-bridge-common',
            'notif-syslog',
            _yang_ns._namespaces['cisco-bridge-common'],
        'ydk.models.cisco_ios_xe.cisco_bridge_common'
        ),
    },
    'NotifSyslogAndSnmpTrapIdentity' : {
        'meta_info' : _MetaInfoClass('NotifSyslogAndSnmpTrapIdentity',
            False, 
            [
            ],
            'cisco-bridge-common',
            'notif-syslog-and-snmp-trap',
            _yang_ns._namespaces['cisco-bridge-common'],
        'ydk.models.cisco_ios_xe.cisco_bridge_common'
        ),
    },
    'NotifNoneIdentity' : {
        'meta_info' : _MetaInfoClass('NotifNoneIdentity',
            False, 
            [
            ],
            'cisco-bridge-common',
            'notif-none',
            _yang_ns._namespaces['cisco-bridge-common'],
        'ydk.models.cisco_ios_xe.cisco_bridge_common'
        ),
    },
    'NotifSnmpTrapIdentity' : {
        'meta_info' : _MetaInfoClass('NotifSnmpTrapIdentity',
            False, 
            [
            ],
            'cisco-bridge-common',
            'notif-snmp-trap',
            _yang_ns._namespaces['cisco-bridge-common'],
        'ydk.models.cisco_ios_xe.cisco_bridge_common'
        ),
    },
}
