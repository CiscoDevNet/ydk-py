


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'IEEE8021PriorityCodePoint_Enum' : _MetaInfoEnum('IEEE8021PriorityCodePoint_Enum', 'ydk.models.ieee8021.IEEE8021_TC_MIB',
        {
            'codePoint8p0d':'CODEPOINT8P0D',
            'codePoint7p1d':'CODEPOINT7P1D',
            'codePoint6p2d':'CODEPOINT6P2D',
            'codePoint5p3d':'CODEPOINT5P3D',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
    'IEEE8021ServiceSelectorType_Enum' : _MetaInfoEnum('IEEE8021ServiceSelectorType_Enum', 'ydk.models.ieee8021.IEEE8021_TC_MIB',
        {
            'vlanId':'VLANID',
            'isid':'ISID',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
    'IEEE8021PortAcceptableFrameTypes_Enum' : _MetaInfoEnum('IEEE8021PortAcceptableFrameTypes_Enum', 'ydk.models.ieee8021.IEEE8021_TC_MIB',
        {
            'admitAll':'ADMITALL',
            'admitUntaggedAndPriority':'ADMITUNTAGGEDANDPRIORITY',
            'admitTagged':'ADMITTAGGED',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
    'IEEE8021BridgePortType_Enum' : _MetaInfoEnum('IEEE8021BridgePortType_Enum', 'ydk.models.ieee8021.IEEE8021_TC_MIB',
        {
            'none':'NONE',
            'customerVlanPort':'CUSTOMERVLANPORT',
            'providerNetworkPort':'PROVIDERNETWORKPORT',
            'customerNetworkPort':'CUSTOMERNETWORKPORT',
            'customerEdgePort':'CUSTOMEREDGEPORT',
            'customerBackbonePort':'CUSTOMERBACKBONEPORT',
            'virtualInstancePort':'VIRTUALINSTANCEPORT',
            'dBridgePort':'DBRIDGEPORT',
        }, 'IEEE8021-TC-MIB', _yang_ns._namespaces['IEEE8021-TC-MIB']),
}
