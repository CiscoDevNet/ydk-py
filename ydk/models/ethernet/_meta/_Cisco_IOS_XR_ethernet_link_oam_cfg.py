


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'EtherLinkOamInterfaceModeEnumEnum' : _MetaInfoEnum('EtherLinkOamInterfaceModeEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
            'active':'ACTIVE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileHelloIntervalEnumEnum' : _MetaInfoEnum('EtherLinkOamProfileHelloIntervalEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            '100ms':'Y_100MS',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnumEnum' : _MetaInfoEnum('EtherLinkOamEventActionEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
            'log':'LOG',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionPrimEnumEnum' : _MetaInfoEnum('EtherLinkOamEventActionPrimEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'log':'LOG',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileRequireModeEnumEnum' : _MetaInfoEnum('EtherLinkOamProfileRequireModeEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
            'active':'ACTIVE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamInterfaceRequireModeEnumEnum' : _MetaInfoEnum('EtherLinkOamInterfaceRequireModeEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
            'active':'ACTIVE',
            'dont-care':'DONT_CARE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum2Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum2Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum5Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum5Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
            'efd':'EFD',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum4Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum4Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileModeEnumEnum' : _MetaInfoEnum('EtherLinkOamProfileModeEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum6Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum6Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'log':'LOG',
            'efd':'EFD',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnumEfdEnum' : _MetaInfoEnum('EtherLinkOamEventActionEnumEfdEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
            'log':'LOG',
            'efd':'EFD',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum1Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum1Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'error-disable':'ERROR_DISABLE',
            'log':'LOG',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamInterfaceHelloIntervalEnumEnum' : _MetaInfoEnum('EtherLinkOamInterfaceHelloIntervalEnumEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            '1s':'Y_1S',
            '100ms':'Y_100MS',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
}
