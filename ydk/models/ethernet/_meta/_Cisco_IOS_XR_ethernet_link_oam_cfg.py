


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'EtherLinkOamInterfaceModeEnum_Enum' : _MetaInfoEnum('EtherLinkOamInterfaceModeEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
            'active':'ACTIVE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileHelloIntervalEnum_Enum' : _MetaInfoEnum('EtherLinkOamProfileHelloIntervalEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            '100ms':'Y_100MS',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum_Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
            'log':'LOG',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionPrimEnum_Enum' : _MetaInfoEnum('EtherLinkOamEventActionPrimEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'log':'LOG',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileRequireModeEnum_Enum' : _MetaInfoEnum('EtherLinkOamProfileRequireModeEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
            'active':'ACTIVE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamInterfaceRequireModeEnum_Enum' : _MetaInfoEnum('EtherLinkOamInterfaceRequireModeEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
            'active':'ACTIVE',
            'dont-care':'DONT_CARE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum2_Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum2_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum5_Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum5_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
            'efd':'EFD',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum4_Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum4_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamProfileModeEnum_Enum' : _MetaInfoEnum('EtherLinkOamProfileModeEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'passive':'PASSIVE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum6_Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum6_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'log':'LOG',
            'efd':'EFD',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnumEfd_Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnumEfd_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'disable':'DISABLE',
            'error-disable':'ERROR_DISABLE',
            'log':'LOG',
            'efd':'EFD',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamEventActionEnum1_Enum' : _MetaInfoEnum('EtherLinkOamEventActionEnum1_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            'error-disable':'ERROR_DISABLE',
            'log':'LOG',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
    'EtherLinkOamInterfaceHelloIntervalEnum_Enum' : _MetaInfoEnum('EtherLinkOamInterfaceHelloIntervalEnum_Enum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_cfg',
        {
            '1s':'Y_1S',
            '100ms':'Y_100MS',
        }, 'Cisco-IOS-XR-ethernet-link-oam-cfg', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-cfg']),
}
