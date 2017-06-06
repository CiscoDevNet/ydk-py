


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NetconfTcpIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfTcpIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'netconf-tcp',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'RestHttpIdentity' : {
        'meta_info' : _MetaInfoClass('RestHttpIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'rest-http',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'CliSshIdentity' : {
        'meta_info' : _MetaInfoClass('CliSshIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'cli-ssh',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'WebuiHttpIdentity' : {
        'meta_info' : _MetaInfoClass('WebuiHttpIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'webui-http',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'CliConsoleIdentity' : {
        'meta_info' : _MetaInfoClass('CliConsoleIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'cli-console',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'CliTcpIdentity' : {
        'meta_info' : _MetaInfoClass('CliTcpIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'cli-tcp',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'RestHttpsIdentity' : {
        'meta_info' : _MetaInfoClass('RestHttpsIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'rest-https',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'SnmpUdpIdentity' : {
        'meta_info' : _MetaInfoClass('SnmpUdpIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'snmp-udp',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
    'WebuiHttpsIdentity' : {
        'meta_info' : _MetaInfoClass('WebuiHttpsIdentity',
            False, 
            [
            ],
            'tailf-netconf-monitoring',
            'webui-https',
            _yang_ns._namespaces['tailf-netconf-monitoring'],
        'ydk.models.cisco_ios_xe.tailf_netconf_monitoring'
        ),
    },
}
