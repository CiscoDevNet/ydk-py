


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Ieee8021PrioritycodepointEnum' : _MetaInfoEnum('Ieee8021PrioritycodepointEnum', 'ydk.models.cisco_ios_xe.IEEE8021_TC_MIB',
        {
            'codePoint8p0d':'codePoint8p0d',
            'codePoint7p1d':'codePoint7p1d',
            'codePoint6p2d':'codePoint6p2d',
            'codePoint5p3d':'codePoint5p3d',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
    'Ieee8021PortacceptableframetypesEnum' : _MetaInfoEnum('Ieee8021PortacceptableframetypesEnum', 'ydk.models.cisco_ios_xe.IEEE8021_TC_MIB',
        {
            'admitAll':'admitAll',
            'admitUntaggedAndPriority':'admitUntaggedAndPriority',
            'admitTagged':'admitTagged',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
    'Ieee8021ServiceselectortypeEnum' : _MetaInfoEnum('Ieee8021ServiceselectortypeEnum', 'ydk.models.cisco_ios_xe.IEEE8021_TC_MIB',
        {
            'vlanId':'vlanId',
            'isid':'isid',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
    'Ieee8021BridgeporttypeEnum' : _MetaInfoEnum('Ieee8021BridgeporttypeEnum', 'ydk.models.cisco_ios_xe.IEEE8021_TC_MIB',
        {
            'none':'none',
            'customerVlanPort':'customerVlanPort',
            'providerNetworkPort':'providerNetworkPort',
            'customerNetworkPort':'customerNetworkPort',
            'customerEdgePort':'customerEdgePort',
            'customerBackbonePort':'customerBackbonePort',
            'virtualInstancePort':'virtualInstancePort',
            'dBridgePort':'dBridgePort',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
}
