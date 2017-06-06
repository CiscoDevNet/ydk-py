


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'EtherLinkOamEventActionEnumEnum' : _MetaInfoEnum('EtherLinkOamEventActionEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'error-disable':'error_disable',
            'log':'log',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamHelloIntervalEnumEnum' : _MetaInfoEnum('EtherLinkOamHelloIntervalEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            '1s':'Y_1s',
            '100ms':'Y_100ms',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamWindowUnitsSymbolsEnumEnum' : _MetaInfoEnum('EtherLinkOamWindowUnitsSymbolsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'milliseconds':'milliseconds',
            'symbols':'symbols',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnumEfdEnum' : _MetaInfoEnum('EtherLinkOamEventActionEnumEfdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'error-disable':'error_disable',
            'log':'log',
            'efd':'efd',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamThresholdUnitsSymbolsEnumEnum' : _MetaInfoEnum('EtherLinkOamThresholdUnitsSymbolsEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'symbols':'symbols',
            'ppm':'ppm',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamModeEnumEnum' : _MetaInfoEnum('EtherLinkOamModeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'passive',
            'active':'active',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamThresholdWindowMultiplierEnumEnum' : _MetaInfoEnum('EtherLinkOamThresholdWindowMultiplierEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'none':'none',
            'thousand':'thousand',
            'million':'million',
            'billion':'billion',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionPrimEnumEnum' : _MetaInfoEnum('EtherLinkOamEventActionPrimEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'log':'log',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamWindowUnitsFramesEnumEnum' : _MetaInfoEnum('EtherLinkOamWindowUnitsFramesEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'milliseconds':'milliseconds',
            'frames':'frames',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamRequireModeEnumEnum' : _MetaInfoEnum('EtherLinkOamRequireModeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'passive',
            'active':'active',
            'dont-care':'dont_care',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamThresholdUnitsFramesEnumEnum' : _MetaInfoEnum('EtherLinkOamThresholdUnitsFramesEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'frames':'frames',
            'ppm':'ppm',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
}
