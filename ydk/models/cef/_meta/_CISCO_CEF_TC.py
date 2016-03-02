


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CefFailureReason_Enum' : _MetaInfoEnum('CefFailureReason_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'none':'NONE',
            'mallocFailure':'MALLOCFAILURE',
            'hwFailure':'HWFAILURE',
            'keepaliveFailure':'KEEPALIVEFAILURE',
            'noMsgBuffer':'NOMSGBUFFER',
            'invalidMsgSize':'INVALIDMSGSIZE',
            'internalError':'INTERNALERROR',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefCCStatus_Enum' : _MetaInfoEnum('CefCCStatus_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'ccStatusIdle':'CCSTATUSIDLE',
            'ccStatusRunning':'CCSTATUSRUNNING',
            'ccStatusDone':'CCSTATUSDONE',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefForwardingElementSpecialType_Enum' : _MetaInfoEnum('CefForwardingElementSpecialType_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'illegal':'ILLEGAL',
            'punt':'PUNT',
            'drop':'DROP',
            'discard':'DISCARD',
            'null':'NULL',
            'glean':'GLEAN',
            'unresolved':'UNRESOLVED',
            'noRoute':'NOROUTE',
            'none':'NONE',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefPrefixSearchState_Enum' : _MetaInfoEnum('CefPrefixSearchState_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'running':'RUNNING',
            'matchFound':'MATCHFOUND',
            'noMatchFound':'NOMATCHFOUND',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefPathType_Enum' : _MetaInfoEnum('CefPathType_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'receive':'RECEIVE',
            'connectedPrefix':'CONNECTEDPREFIX',
            'attachedPrefix':'ATTACHEDPREFIX',
            'attachedHost':'ATTACHEDHOST',
            'attachedNexthop':'ATTACHEDNEXTHOP',
            'recursiveNexthop':'RECURSIVENEXTHOP',
            'adjacencyPrefix':'ADJACENCYPREFIX',
            'specialPrefix':'SPECIALPREFIX',
            'unknown':'UNKNOWN',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefCCType_Enum' : _MetaInfoEnum('CefCCType_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'lcDetect':'LCDETECT',
            'scanFibLcRp':'SCANFIBLCRP',
            'scanFibRpLc':'SCANFIBRPLC',
            'scanRibFib':'SCANRIBFIB',
            'scanFibRib':'SCANFIBRIB',
            'scanFibHwSw':'SCANFIBHWSW',
            'scanFibSwHw':'SCANFIBSWHW',
            'fullScanRibFib':'FULLSCANRIBFIB',
            'fullScanFibRib':'FULLSCANFIBRIB',
            'fullScanFibRpLc':'FULLSCANFIBRPLC',
            'fullScanFibLcRp':'FULLSCANFIBLCRP',
            'fullScanFibHwSw':'FULLSCANFIBHWSW',
            'fullScanFibSwHw':'FULLSCANFIBSWHW',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefOperStatus_Enum' : _MetaInfoEnum('CefOperStatus_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'up':'UP',
            'down':'DOWN',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefAdjLinkType_Enum' : _MetaInfoEnum('CefAdjLinkType_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'ipv4':'IPV4',
            'ipv6':'IPV6',
            'mpls':'MPLS',
            'raw':'RAW',
            'unknown':'UNKNOWN',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefCCAction_Enum' : _MetaInfoEnum('CefCCAction_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'ccActionStart':'CCACTIONSTART',
            'ccActionAbort':'CCACTIONABORT',
            'ccActionNone':'CCACTIONNONE',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefAdminStatus_Enum' : _MetaInfoEnum('CefAdminStatus_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'enabled':'ENABLED',
            'disabled':'DISABLED',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefIpVersion_Enum' : _MetaInfoEnum('CefIpVersion_Enum', 'ydk.models.cef.CISCO_CEF_TC',
        {
            'ipv4':'IPV4',
            'ipv6':'IPV6',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
}
