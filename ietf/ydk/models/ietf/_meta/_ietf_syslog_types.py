


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SeverityEnum' : _MetaInfoEnum('SeverityEnum', 'ydk.models.ietf.ietf_syslog_types',
        {
            'emergency':'emergency',
            'alert':'alert',
            'critical':'critical',
            'error':'error',
            'warning':'warning',
            'notice':'notice',
            'info':'info',
            'debug':'debug',
        }, 'ietf-syslog-types', _yang_ns._namespaces['ietf-syslog-types']),
    'SyslogFacilityIdentity' : {
        'meta_info' : _MetaInfoClass('SyslogFacilityIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'syslog-facility',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local3Identity' : {
        'meta_info' : _MetaInfoClass('Local3Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local3',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'DaemonIdentity' : {
        'meta_info' : _MetaInfoClass('DaemonIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'daemon',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local0Identity' : {
        'meta_info' : _MetaInfoClass('Local0Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local0',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'NtpIdentity' : {
        'meta_info' : _MetaInfoClass('NtpIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'ntp',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'CronIdentity' : {
        'meta_info' : _MetaInfoClass('CronIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'cron',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'AuditIdentity' : {
        'meta_info' : _MetaInfoClass('AuditIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'audit',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'KernIdentity' : {
        'meta_info' : _MetaInfoClass('KernIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'kern',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local4Identity' : {
        'meta_info' : _MetaInfoClass('Local4Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local4',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'MailIdentity' : {
        'meta_info' : _MetaInfoClass('MailIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'mail',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'UserIdentity' : {
        'meta_info' : _MetaInfoClass('UserIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'user',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'FtpIdentity' : {
        'meta_info' : _MetaInfoClass('FtpIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'ftp',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local6Identity' : {
        'meta_info' : _MetaInfoClass('Local6Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local6',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'ConsoleIdentity' : {
        'meta_info' : _MetaInfoClass('ConsoleIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'console',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'LprIdentity' : {
        'meta_info' : _MetaInfoClass('LprIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'lpr',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local1Identity' : {
        'meta_info' : _MetaInfoClass('Local1Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local1',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'AuthIdentity' : {
        'meta_info' : _MetaInfoClass('AuthIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'auth',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local2Identity' : {
        'meta_info' : _MetaInfoClass('Local2Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local2',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local5Identity' : {
        'meta_info' : _MetaInfoClass('Local5Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local5',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Local7Identity' : {
        'meta_info' : _MetaInfoClass('Local7Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'local7',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'UucpIdentity' : {
        'meta_info' : _MetaInfoClass('UucpIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'uucp',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'NewsIdentity' : {
        'meta_info' : _MetaInfoClass('NewsIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'news',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'AuthprivIdentity' : {
        'meta_info' : _MetaInfoClass('AuthprivIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'authpriv',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'Cron2Identity' : {
        'meta_info' : _MetaInfoClass('Cron2Identity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'cron2',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
    'SyslogIdentity' : {
        'meta_info' : _MetaInfoClass('SyslogIdentity',
            False, 
            [
            ],
            'ietf-syslog-types',
            'syslog',
            _yang_ns._namespaces['ietf-syslog-types'],
        'ydk.models.ietf.ietf_syslog_types'
        ),
    },
}
