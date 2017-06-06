


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CefccstatusEnum' : _MetaInfoEnum('CefccstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'ccStatusIdle':'ccStatusIdle',
            'ccStatusRunning':'ccStatusRunning',
            'ccStatusDone':'ccStatusDone',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CeffailurereasonEnum' : _MetaInfoEnum('CeffailurereasonEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'none':'none',
            'mallocFailure':'mallocFailure',
            'hwFailure':'hwFailure',
            'keepaliveFailure':'keepaliveFailure',
            'noMsgBuffer':'noMsgBuffer',
            'invalidMsgSize':'invalidMsgSize',
            'internalError':'internalError',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefprefixsearchstateEnum' : _MetaInfoEnum('CefprefixsearchstateEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'running':'running',
            'matchFound':'matchFound',
            'noMatchFound':'noMatchFound',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefadminstatusEnum' : _MetaInfoEnum('CefadminstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefipversionEnum' : _MetaInfoEnum('CefipversionEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefoperstatusEnum' : _MetaInfoEnum('CefoperstatusEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'up':'up',
            'down':'down',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefcctypeEnum' : _MetaInfoEnum('CefcctypeEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'lcDetect':'lcDetect',
            'scanFibLcRp':'scanFibLcRp',
            'scanFibRpLc':'scanFibRpLc',
            'scanRibFib':'scanRibFib',
            'scanFibRib':'scanFibRib',
            'scanFibHwSw':'scanFibHwSw',
            'scanFibSwHw':'scanFibSwHw',
            'fullScanRibFib':'fullScanRibFib',
            'fullScanFibRib':'fullScanFibRib',
            'fullScanFibRpLc':'fullScanFibRpLc',
            'fullScanFibLcRp':'fullScanFibLcRp',
            'fullScanFibHwSw':'fullScanFibHwSw',
            'fullScanFibSwHw':'fullScanFibSwHw',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefforwardingelementspecialtypeEnum' : _MetaInfoEnum('CefforwardingelementspecialtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'illegal':'illegal',
            'punt':'punt',
            'drop':'drop',
            'discard':'discard',
            'null':'null',
            'glean':'glean',
            'unresolved':'unresolved',
            'noRoute':'noRoute',
            'none':'none',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefpathtypeEnum' : _MetaInfoEnum('CefpathtypeEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'receive':'receive',
            'connectedPrefix':'connectedPrefix',
            'attachedPrefix':'attachedPrefix',
            'attachedHost':'attachedHost',
            'attachedNexthop':'attachedNexthop',
            'recursiveNexthop':'recursiveNexthop',
            'adjacencyPrefix':'adjacencyPrefix',
            'specialPrefix':'specialPrefix',
            'unknown':'unknown',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefccactionEnum' : _MetaInfoEnum('CefccactionEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'ccActionStart':'ccActionStart',
            'ccActionAbort':'ccActionAbort',
            'ccActionNone':'ccActionNone',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
    'CefadjlinktypeEnum' : _MetaInfoEnum('CefadjlinktypeEnum', 'ydk.models.cisco_ios_xe.CISCO_CEF_TC',
        {
            'ipv4':'ipv4',
            'ipv6':'ipv6',
            'mpls':'mpls',
            'raw':'raw',
            'unknown':'unknown',
        }, 'CISCO-CEF-TC', _yang_ns._namespaces['CISCO-CEF-TC']),
}
