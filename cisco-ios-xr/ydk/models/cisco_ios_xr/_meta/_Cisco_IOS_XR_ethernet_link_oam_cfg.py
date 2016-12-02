


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'EtherLinkOamInterfaceModeEnumEnum' : _MetaInfoEnum('EtherLinkOamInterfaceModeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'passive',
            'active':'active',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileHelloIntervalEnumEnum' : _MetaInfoEnum('EtherLinkOamProfileHelloIntervalEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            '100ms':'Y_100ms',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnumEnum' : _MetaInfoEnum('EtherLinkOamEventActionEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'error-disable':'error_disable',
            'log':'log',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionPrimEnumEnum' : _MetaInfoEnum('EtherLinkOamEventActionPrimEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'log':'log',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileRequireModeEnumEnum' : _MetaInfoEnum('EtherLinkOamProfileRequireModeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'passive',
            'active':'active',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamInterfaceRequireModeEnumEnum' : _MetaInfoEnum('EtherLinkOamInterfaceRequireModeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'passive',
            'active':'active',
            'dont-care':'dont_care',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum2Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum2Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'error-disable':'error_disable',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum5Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum5Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'error-disable':'error_disable',
            'efd':'efd',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum4Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum4Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileModeEnumEnum' : _MetaInfoEnum('EtherLinkOamProfileModeEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'passive',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum6Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum6Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'log':'log',
            'efd':'efd',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnumEfdEnum' : _MetaInfoEnum('EtherLinkOamEventActionEnumEfdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'disable',
            'error-disable':'error_disable',
            'log':'log',
            'efd':'efd',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum1Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum1Enum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'error-disable':'error_disable',
            'log':'log',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamInterfaceHelloIntervalEnumEnum' : _MetaInfoEnum('EtherLinkOamInterfaceHelloIntervalEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            '1s':'Y_1s',
            '100ms':'Y_100ms',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
}
