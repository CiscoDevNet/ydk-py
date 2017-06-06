


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'AaaAccountingEnum' : _MetaInfoEnum('AaaAccountingEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes',
        {
            'not-set':'not_set',
            'start-stop':'start_stop',
            'stop-only':'stop_only',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaMethodEnum' : _MetaInfoEnum('AaaMethodEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes',
        {
            'not-set':'not_set',
            'none':'none',
            'local':'local',
            'radius':'radius',
            'tacacs-plus':'tacacs_plus',
            'dsmd':'dsmd',
            'sgbp':'sgbp',
            'acct-d':'acct_d',
            'error':'error',
            'if-authenticated':'if_authenticated',
            'server-group':'server_group',
            'server-group-not-defined':'server_group_not_defined',
            'line':'line',
            'enable':'enable',
            'kerberos':'kerberos',
            'diameter':'diameter',
            'last':'last',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaAccountingBroadcastEnum' : _MetaInfoEnum('AaaAccountingBroadcastEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaAccountingUpdateEnum' : _MetaInfoEnum('AaaAccountingUpdateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes',
        {
            'none':'none',
            'newinfo':'newinfo',
            'periodic':'periodic',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-datatypes']),
    'AaaAccountingRpFailoverEnum' : _MetaInfoEnum('AaaAccountingRpFailoverEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_aaa_lib_datatypes',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-aaa-lib-datatypes', _yang_ns._namespaces['Cisco-IOS-XR-aaa-lib-datatypes']),
}
