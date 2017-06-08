


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'ControlModeEnum' : _MetaInfoEnum('ControlModeEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'peer':'peer',
            'tunnel':'tunnel',
            'discard':'discard',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'NegModeEnum' : _MetaInfoEnum('NegModeEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'full-duplex':'full_duplex',
            'auto-neg':'auto_neg',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'BwTypeIdentity' : {
        'meta_info' : _MetaInfoClass('BwTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'bw-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpModeIdentity' : {
        'meta_info' : _MetaInfoClass('LacpModeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-mode',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpStateIdentity' : {
        'meta_info' : _MetaInfoClass('LacpStateIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-state',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'MacLearningModeIdentity' : {
        'meta_info' : _MetaInfoClass('MacLearningModeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'mac-learning-mode',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PolicingIdentity' : {
        'meta_info' : _MetaInfoClass('PolicingIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'policing',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'BumTypeIdentity' : {
        'meta_info' : _MetaInfoClass('BumTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'BUM-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ColorTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ColorTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'color-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PlacementDiversityIdentity' : {
        'meta_info' : _MetaInfoClass('PlacementDiversityIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'placement-diversity',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PerfTierOptIdentity' : {
        'meta_info' : _MetaInfoClass('PerfTierOptIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'perf-tier-opt',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'SiteTypeIdentity' : {
        'meta_info' : _MetaInfoClass('SiteTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'site-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'AddressFamilyIdentity' : {
        'meta_info' : _MetaInfoClass('AddressFamilyIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'address-family',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'DataSvcFrameDeliveryIdentity' : {
        'meta_info' : _MetaInfoClass('DataSvcFrameDeliveryIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'data-svc-frame-delivery',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LoopPreventionTypeIdentity' : {
        'meta_info' : _MetaInfoClass('LoopPreventionTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'loop-prevention-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ColorIdIdentity' : {
        'meta_info' : _MetaInfoClass('ColorIdIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'color-id',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'FaultAlarmDefectTypeIdentity' : {
        'meta_info' : _MetaInfoClass('FaultAlarmDefectTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'fault-alarm-defect-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ManagementIdentity' : {
        'meta_info' : _MetaInfoClass('ManagementIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'management',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'SvcTopoTypeIdentity' : {
        'meta_info' : _MetaInfoClass('SvcTopoTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'svc-topo-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CosIdIdentity' : {
        'meta_info' : _MetaInfoClass('CosIdIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'cos-id',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnTypeIdentity' : {
        'meta_info' : _MetaInfoClass('L2VpnTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'l2vpn-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'BundlingTypeIdentity' : {
        'meta_info' : _MetaInfoClass('BundlingTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'bundling-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'VpnTopologyIdentity' : {
        'meta_info' : _MetaInfoClass('VpnTopologyIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'vpn-topology',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'SiteRoleIdentity' : {
        'meta_info' : _MetaInfoClass('SiteRoleIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'site-role',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PmTypeIdentity' : {
        'meta_info' : _MetaInfoClass('PmTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'pm-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2AccessTypeIdentity' : {
        'meta_info' : _MetaInfoClass('L2AccessTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'l2-access-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'VpnSignalingTypeIdentity' : {
        'meta_info' : _MetaInfoClass('VpnSignalingTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'vpn-signaling-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpSpeedIdentity' : {
        'meta_info' : _MetaInfoClass('LacpSpeedIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-speed',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ServiceTypeIdentity' : {
        'meta_info' : _MetaInfoClass('ServiceTypeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'service-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter.CustomerNocPhoneNumber' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter.CustomerNocPhoneNumber',
            False, 
            [
            _MetaInfoClassMember('extension-options', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Extension or options
                ''',
                'extension_options',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('main-phone-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Main phone number.
                ''',
                'main_phone_num',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'customer-noc-phone-number',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter',
            False, 
            [
            _MetaInfoClassMember('customer-noc-phone-number', REFERENCE_CLASS, 'CustomerNocPhoneNumber' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter.CustomerNocPhoneNumber', 
                [], [], 
                '''                Configuration of customer NOCc phone number
                ''',
                'customer_noc_phone_number',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('customer-noc-street-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Customer NOC street Address.
                ''',
                'customer_noc_street_address',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'customer-operation-center',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.CustomerInfo.CustomerInfo_' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.CustomerInfo.CustomerInfo_',
            False, 
            [
            _MetaInfoClassMember('customer-account-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Customer account number
                ''',
                'customer_account_number',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('customer-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Customer name
                ''',
                'customer_name',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('customer-operation-center', REFERENCE_CLASS, 'CustomerOperationCenter' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter', 
                [], [], 
                '''                Configuration of customer operation center
                ''',
                'customer_operation_center',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'customer-info',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.CustomerInfo' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.CustomerInfo',
            False, 
            [
            _MetaInfoClassMember('customer-info', REFERENCE_LIST, 'CustomerInfo_' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.CustomerInfo.CustomerInfo_', 
                [], [], 
                '''                List of customer information
                ''',
                'customer_info',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'customer-info',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList.UniList_' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList.UniList_',
            False, 
            [
            _MetaInfoClassMember('network-access-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Network Access Identifier
                ''',
                'network_access_id',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'uni-list',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList',
            False, 
            [
            _MetaInfoClassMember('uni-list', REFERENCE_LIST, 'UniList_' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList.UniList_', 
                [], [], 
                '''                List for UNIs
                ''',
                'uni_list',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'uni-list',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.EvcType' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.EvcType',
            False, 
            [
            _MetaInfoClassMember('evc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ethernet Virtual Connection identifier
                ''',
                'evc_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('number-of-pe', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of PE
                ''',
                'number_of_pe',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('number-of-site', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Sites
                ''',
                'number_of_site',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('uni-list', REFERENCE_CLASS, 'UniList' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList', 
                [], [], 
                '''                Container for UNI List
                ''',
                'uni_list',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'evc-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.OvcType.OvcList' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.OvcType.OvcList',
            False, 
            [
            _MetaInfoClassMember('ovc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OVC ID type
                ''',
                'ovc_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('off-net', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Off net
                ''',
                'off_net',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('on-net', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                On net
                ''',
                'on_net',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'ovc-list',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.OvcType' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.OvcType',
            False, 
            [
            _MetaInfoClassMember('ovc-list', REFERENCE_LIST, 'OvcList' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.OvcType.OvcList', 
                [], [], 
                '''                List for OVC
                ''',
                'ovc_list',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'ovc-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.EthernetSvcType' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.EthernetSvcType',
            False, 
            [
            _MetaInfoClassMember('access-epl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Access Ethernet virtual private line
                ''',
                'access_epl',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('access-evpl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Access Ethernet virtual private line
                ''',
                'access_evpl',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ep-lan', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet private LAN
                ''',
                'ep_lan',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('epl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet private line
                ''',
                'epl',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('evp-lan', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet virtual private LAN
                ''',
                'evp_lan',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('evpl', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet virtual private line
                ''',
                'evpl',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'ethernet-svc-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites.AuthorizedSite' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites.AuthorizedSite',
            False, 
            [
            _MetaInfoClassMember('site-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Site ID.
                ''',
                'site_id',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'authorized-site',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites',
            False, 
            [
            _MetaInfoClassMember('authorized-site', REFERENCE_LIST, 'AuthorizedSite' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites.AuthorizedSite', 
                [], [], 
                '''                List of authorized sites.
                ''',
                'authorized_site',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'authorized-sites',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites.DeniedSite' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites.DeniedSite',
            False, 
            [
            _MetaInfoClassMember('site-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Site ID.
                ''',
                'site_id',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'denied-site',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites',
            False, 
            [
            _MetaInfoClassMember('denied-site', REFERENCE_LIST, 'DeniedSite' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites.DeniedSite', 
                [], [], 
                '''                List of denied sites.
                ''',
                'denied_site',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'denied-sites',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess',
            False, 
            [
            _MetaInfoClassMember('cloud-identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identification of cloud service. Local
                admin meaning.
                ''',
                'cloud_identifier',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('authorized-sites', REFERENCE_CLASS, 'AuthorizedSites' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites', 
                [], [], 
                '''                Configuration of authorized sites
                ''',
                'authorized_sites',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('denied-sites', REFERENCE_CLASS, 'DeniedSites' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites', 
                [], [], 
                '''                Configuration of denied sites
                ''',
                'denied_sites',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('deny-site', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Site ID to be denied.
                ''',
                'deny_site',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('permit-any', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                Allow all sites.
                ''',
                'permit_any',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('permit-site', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Site ID to be authorized.
                ''',
                'permit_site',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'cloud-access',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CloudAccesses',
            False, 
            [
            _MetaInfoClassMember('cloud-access', REFERENCE_LIST, 'CloudAccess' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess', 
                [], [], 
                '''                Cloud access configuration.
                ''',
                'cloud_access',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'cloud-accesses',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CeVlanPreservation' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CeVlanPreservation',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'ce-vlan-preservation',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId.IntraMkt' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId.IntraMkt',
            False, 
            [
            _MetaInfoClassMember('metro-mkt-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Metro MKT ID
                ''',
                'metro_mkt_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('mkt-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MKT Name
                ''',
                'mkt_name',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('ovc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OVC identifier
                ''',
                'ovc_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'intra-mkt',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId',
            False, 
            [
            _MetaInfoClassMember('inter-mkt-service', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether service is inter market service.
                ''',
                'inter_mkt_service',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('intra-mkt', REFERENCE_LIST, 'IntraMkt' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId.IntraMkt', 
                [], [], 
                '''                List of intra-MKT
                ''',
                'intra_mkt',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'metro-network-id',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.L2CpControl' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.L2CpControl',
            False, 
            [
            _MetaInfoClassMember('lldp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LLDP
                ''',
                'lldp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('pause', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                Pause
                ''',
                'pause',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('stp-rstp-mstp', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                STP/RSTP/MSTP
                ''',
                'stp_rstp_mstp',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'L2CP-control',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.LoadBalanceOptions' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.LoadBalanceOptions',
            False, 
            [
            _MetaInfoClassMember('entropy-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Entropy label is applied to IP forwarding,
                L2VPN or L3VPN across MPLS network
                ''',
                'entropy_label',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('fat-pw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Fat label is applied to Pseudowires across MPLS
                network
                ''',
                'fat_pw',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vxlan-source-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vxlan source port
                ''',
                'vxlan_source_port',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'load-balance-options',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap.CvlanId' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap.CvlanId',
            False, 
            [
            _MetaInfoClassMember('vid', REFERENCE_IDENTITY_CLASS, 'IanaInterfaceTypeIdentity' , 'ydk.models.ietf.iana_if_type', 'IanaInterfaceTypeIdentity', 
                [], [], 
                '''                CVLAN ID
                ''',
                'vid',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'cvlan-id',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap',
            False, 
            [
            _MetaInfoClassMember('evc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EVC ID
                ''',
                'evc_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'BundlingTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'BundlingTypeIdentity', 
                [], [], 
                '''                Bundling type
                ''',
                'type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('cvlan-id', REFERENCE_LIST, 'CvlanId' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap.CvlanId', 
                [], [], 
                '''                List of CVLAN-ID to EVC Map configurations
                ''',
                'cvlan_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'cvlan-id-to-evc-map',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.ProtectionModel' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.ProtectionModel',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'protection-model',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.PeerEvcId' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.PeerEvcId',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'peer-evc-id',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.ServiceProtection' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.ServiceProtection',
            False, 
            [
            _MetaInfoClassMember('peer-evc-id', REFERENCE_CLASS, 'PeerEvcId' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.PeerEvcId', 
                [], [], 
                '''                Container of peer EVC ID configurations
                ''',
                'peer_evc_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('protection-model', REFERENCE_CLASS, 'ProtectionModel' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.ProtectionModel', 
                [], [], 
                '''                Container of protection model configurations
                ''',
                'protection_model',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'service-protection',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc.SlaTargets' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc.SlaTargets',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'sla-targets',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices.VpnSvc' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices.VpnSvc',
            False, 
            [
            _MetaInfoClassMember('vpn-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Defining a service id.
                ''',
                'vpn_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('ce-vlan-preservation', REFERENCE_CLASS, 'CeVlanPreservation' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CeVlanPreservation', 
                [], [], 
                '''                CE vlan preservation
                ''',
                'ce_vlan_preservation',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('cloud-accesses', REFERENCE_CLASS, 'CloudAccesses' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CloudAccesses', 
                [], [], 
                '''                Container for cloud access configurations
                ''',
                'cloud_accesses',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('cvlan-id-to-evc-map', REFERENCE_LIST, 'CvlanIdToEvcMap' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap', 
                [], [], 
                '''                List for cvlan-id to evc map configurations
                ''',
                'cvlan_id_to_evc_map',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ethernet-svc-type', REFERENCE_CLASS, 'EthernetSvcType' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.EthernetSvcType', 
                [], [], 
                '''                Container of Ethernet service type
                ''',
                'ethernet_svc_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('evc-type', REFERENCE_CLASS, 'EvcType' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.EvcType', 
                [], [], 
                '''                Container for Ethernet virtual connection.
                ''',
                'evc_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('L2CP-control', REFERENCE_CLASS, 'L2CpControl' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.L2CpControl', 
                [], [], 
                '''                Container of L2CP control configurations
                ''',
                'l2cp_control',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('load-balance-options', REFERENCE_CLASS, 'LoadBalanceOptions' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.LoadBalanceOptions', 
                [], [], 
                '''                Container for load balance options
                ''',
                'load_balance_options',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('metro-network-id', REFERENCE_CLASS, 'MetroNetworkId' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId', 
                [], [], 
                '''                Container of Metro-Network ID configurations
                ''',
                'metro_network_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ovc-type', REFERENCE_CLASS, 'OvcType' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.OvcType', 
                [], [], 
                '''                Container for OVC
                ''',
                'ovc_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('service-level-mac-limit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service-level MAC-limit (E-LAN only)
                ''',
                'service_level_mac_limit',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('service-protection', REFERENCE_CLASS, 'ServiceProtection' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.ServiceProtection', 
                [], [], 
                '''                Container of End-to-end Service Protection
                configurations
                ''',
                'service_protection',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('sla-targets', REFERENCE_CLASS, 'SlaTargets' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc.SlaTargets', 
                [], [], 
                '''                Container for SLA targets
                ''',
                'sla_targets',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('svc-topo', REFERENCE_IDENTITY_CLASS, 'SvcTopoTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'SvcTopoTypeIdentity', 
                [], [], 
                '''                Defining service topology, such as
                point to point, multipoint to multipoint,
                rooted multipoint, etc.
                ''',
                'svc_topo',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('svc-type', REFERENCE_IDENTITY_CLASS, 'ServiceTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ServiceTypeIdentity', 
                [], [], 
                '''                Service type
                ''',
                'svc_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('svlan-id-ethernet-tag', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SVLAN-ID/Ethernet Tag configurations
                ''',
                'svlan_id_ethernet_tag',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vpn-svc',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.VpnServices' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.VpnServices',
            False, 
            [
            _MetaInfoClassMember('vpn-svc', REFERENCE_LIST, 'VpnSvc' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices.VpnSvc', 
                [], [], 
                '''                List of vpn-svc
                ''',
                'vpn_svc',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vpn-services',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Device.Devices.Management' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Device.Devices.Management',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Address
                ''',
                'address',
                'ietf-l2vpn-svc', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address
                        ''',
                        'address',
                        'ietf-l2vpn-svc', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Address
                        ''',
                        'address',
                        'ietf-l2vpn-svc', False),
                ]),
            _MetaInfoClassMember('management-transport', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'AddressFamilyIdentity', 
                [], [], 
                '''                Transport protocol used for management.
                ''',
                'management_transport',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'management',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Device.Devices' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Device.Devices',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device ID
                ''',
                'device_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('management', REFERENCE_CLASS, 'Management' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Device.Devices.Management', 
                [], [], 
                '''                Container for management
                ''',
                'management',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('site-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Site name
                ''',
                'site_name',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'devices',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Device' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Device',
            False, 
            [
            _MetaInfoClassMember('devices', REFERENCE_LIST, 'Devices' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Device.Devices', 
                [], [], 
                '''                List of devices
                ''',
                'devices',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'device',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Managemnt' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Managemnt',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'ManagementIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ManagementIdentity', 
                [], [], 
                '''                Management type of the connection.
                ''',
                'type',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'managemnt',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Location' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Location',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Address (number and street) of the site.
                ''',
                'address',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('city', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                City of the site.
                ''',
                'city',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('country-code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Country of the site.
                ''',
                'country_code',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('state', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                State of the site. This leaf can also be used to
                describe a region for country who does not have
                states.
                ''',
                'state',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('zip-code', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ZIP code of the site.
                ''',
                'zip_code',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'location',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SiteDiversity.Groups.Group' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SiteDiversity.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group-id the site is belonging to
                ''',
                'group_id',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'group',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SiteDiversity.Groups' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SiteDiversity.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SiteDiversity.Groups.Group', 
                [], [], 
                '''                List of group-id
                ''',
                'group',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'groups',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SiteDiversity' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SiteDiversity',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SiteDiversity.Groups', 
                [], [], 
                '''                Groups the site is belonging to.
                All site network accesses will inherit those group
                values.
                ''',
                'groups',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'site-diversity',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Filter' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Filter',
            False, 
            [
            _MetaInfoClassMember('lan-tag', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of lan-tags to be matched.
                ''',
                'lan_tag',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'filter',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Vpn' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Vpn',
            False, 
            [
            _MetaInfoClassMember('site-role', REFERENCE_IDENTITY_CLASS, 'SiteRoleIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'SiteRoleIdentity', 
                [], [], 
                '''                Role of the site in the IPVPN.
                ''',
                'site_role',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to an IPVPN.
                ''',
                'vpn_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vpn',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier for the policy entry.
                ''',
                'id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('filter', REFERENCE_CLASS, 'Filter' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Filter', 
                [], [], 
                '''                If used, it permit to split site LANs
                among multiple VPNs.
                If no filter used, all the LANs will be
                part of the same VPNs with the same
                role.
                ''',
                'filter',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn', REFERENCE_CLASS, 'Vpn' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Vpn', 
                [], [], 
                '''                List of VPNs the LAN is associated to.
                ''',
                'vpn',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'entries',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy',
            False, 
            [
            _MetaInfoClassMember('vpn-policy-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Unique identifier for the VPN policy.
                ''',
                'vpn_policy_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('entries', REFERENCE_LIST, 'Entries' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries', 
                [], [], 
                '''                List of entries for export policy.
                ''',
                'entries',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vpn-policy',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.VpnPolicies' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.VpnPolicies',
            False, 
            [
            _MetaInfoClassMember('vpn-policy', REFERENCE_LIST, 'VpnPolicy' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy', 
                [], [], 
                '''                List of VPN policies.
                ''',
                'vpn_policy',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vpn-policies',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpL2Vpn' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpL2Vpn',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'L2VpnTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnTypeIdentity', 
                [], [], 
                '''                L2VPN types
                ''',
                'type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifies the target VPN
                ''',
                'vpn_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'mp-bgp-l2vpn',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpEvpn' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpEvpn',
            False, 
            [
            _MetaInfoClassMember('arp-suppress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether to suppress ARP broadcast.
                ''',
                'arp_suppress',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mac-learning-mode', REFERENCE_IDENTITY_CLASS, 'MacLearningModeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'MacLearningModeIdentity', 
                [], [], 
                '''                Indicates through which plane MAC addresses are
                advertised.
                ''',
                'mac_learning_mode',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'L2VpnTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnTypeIdentity', 
                [], [], 
                '''                L2VPN types
                ''',
                'type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifies the target VPN
                ''',
                'vpn_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'mp-bgp-evpn',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe.PeEgList' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe.PeEgList',
            False, 
            [
            _MetaInfoClassMember('service-ip-lo-addr', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Service ip lo address
                ''',
                'service_ip_lo_addr',
                'ietf-l2vpn-svc', True, [
                    _MetaInfoClassMember('service-ip-lo-addr', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Service ip lo address
                        ''',
                        'service_ip_lo_addr',
                        'ietf-l2vpn-svc', True),
                    _MetaInfoClassMember('service-ip-lo-addr', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Service ip lo address
                        ''',
                        'service_ip_lo_addr',
                        'ietf-l2vpn-svc', True),
                ]),
            _MetaInfoClassMember('vc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                VC id
                ''',
                'vc_id',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'PE-EG-list',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe',
            False, 
            [
            _MetaInfoClassMember('PE-EG-list', REFERENCE_LIST, 'PeEgList' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe.PeEgList', 
                [], [], 
                '''                List of PE/EG
                ''',
                'pe_eg_list',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            't-ldp-pwe',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweEncapsulationType' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweEncapsulationType',
            False, 
            [
            _MetaInfoClassMember('ethernet', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Ethernet
                ''',
                'ethernet',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vlan', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                VLAN
                ''',
                'vlan',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'pwe-encapsulation-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweMtu' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweMtu',
            False, 
            [
            _MetaInfoClassMember('allow-mtu-mismatch', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Allow MTU mismatch
                ''',
                'allow_mtu_mismatch',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'pwe-mtu',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.ControlWord' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.ControlWord',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'control-word',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'VpnSignalingTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'VpnSignalingTypeIdentity', 
                [], [], 
                '''                VPN signaling types
                ''',
                'type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('control-word', REFERENCE_CLASS, 'ControlWord' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.ControlWord', 
                [], [], 
                '''                Container of control word configurations
                ''',
                'control_word',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mp-bgp-evpn', REFERENCE_CLASS, 'MpBgpEvpn' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpEvpn', 
                [], [], 
                '''                Container for MP BGP L2VPN
                ''',
                'mp_bgp_evpn',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mp-bgp-l2vpn', REFERENCE_CLASS, 'MpBgpL2Vpn' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpL2Vpn', 
                [], [], 
                '''                Container for MP BGP L2VPN
                ''',
                'mp_bgp_l2vpn',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('pwe-encapsulation-type', REFERENCE_CLASS, 'PweEncapsulationType' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweEncapsulationType', 
                [], [], 
                '''                Container of PWE Encapsulation Type configurations
                ''',
                'pwe_encapsulation_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('pwe-mtu', REFERENCE_CLASS, 'PweMtu' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweMtu', 
                [], [], 
                '''                Container of PWE MTU configurations
                ''',
                'pwe_mtu',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('t-ldp-pwe', REFERENCE_CLASS, 'TLdpPwe' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe', 
                [], [], 
                '''                Container of T-LDP PWE configurations
                ''',
                't_ldp_pwe',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'signaling-option',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.SignalingOption' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.SignalingOption',
            False, 
            [
            _MetaInfoClassMember('signaling-option', REFERENCE_LIST, 'SignalingOption_' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_', 
                [], [], 
                '''                List of VPN Signaling Option.
                ''',
                'signaling_option',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'signaling-option',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.LoadBalanceOptions' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.LoadBalanceOptions',
            False, 
            [
            _MetaInfoClassMember('entropy-label', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Entropy label is applied to IP forwarding,
                L2VPN or L3VPN across MPLS network
                ''',
                'entropy_label',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('fat-pw', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Fat label is applied to Pseudowires across MPLS
                network
                ''',
                'fat_pw',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vxlan-source-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Vxlan source port
                ''',
                'vxlan_source_port',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'load-balance-options',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups.Group' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Group-id the site network access
                is belonging to
                ''',
                'group_id',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'group',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups',
            False, 
            [
            _MetaInfoClassMember('fate-sharing-group-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Fate sharing group size.
                ''',
                'fate_sharing_group_size',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups.Group', 
                [], [], 
                '''                List of group-id
                ''',
                'group',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'groups',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target.Group' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target.Group',
            False, 
            [
            _MetaInfoClassMember('group-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The constraint will apply
                against this particular
                group-id
                ''',
                'group_id',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'group',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target',
            False, 
            [
            _MetaInfoClassMember('all-other-accesses', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The constraint will apply
                against all other site network
                access of this site
                ''',
                'all_other_accesses',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('all-other-groups', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The constraint will apply
                against all other groups the
                customer is managing
                ''',
                'all_other_groups',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target.Group', 
                [], [], 
                '''                List of groups
                ''',
                'group',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'target',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint',
            False, 
            [
            _MetaInfoClassMember('constraint-type', REFERENCE_IDENTITY_CLASS, 'PlacementDiversityIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'PlacementDiversityIdentity', 
                [], [], 
                '''                Diversity constraint type.
                ''',
                'constraint_type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('target', REFERENCE_CLASS, 'Target' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target', 
                [], [], 
                '''                The constraint will apply against
                this list of groups
                ''',
                'target',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'constraint',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints',
            False, 
            [
            _MetaInfoClassMember('constraint', REFERENCE_LIST, 'Constraint' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint', 
                [], [], 
                '''                List of constraints
                ''',
                'constraint',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'constraints',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity',
            False, 
            [
            _MetaInfoClassMember('constraints', REFERENCE_CLASS, 'Constraints' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints', 
                [], [], 
                '''                Constraints for placing this site
                 network access
                ''',
                'constraints',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups', 
                [], [], 
                '''                Groups the fate sharing group member
                is belonging to
                ''',
                'groups',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'access-diversity',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile.Dot1Q' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile.Dot1Q',
            False, 
            [
            _MetaInfoClassMember('physical-if', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Physical interface
                ''',
                'physical_if',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                VLAN ID
                ''',
                'vlan_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'dot1q',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile',
            False, 
            [
            _MetaInfoClassMember('circuit-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Circuit ID
                ''',
                'circuit_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('dot1q', REFERENCE_CLASS, 'Dot1Q' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile.Dot1Q', 
                [], [], 
                '''                Container for dot1q.
                ''',
                'dot1q',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('physical-if', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Physical interface
                ''',
                'physical_if',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'request-type-profile',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType',
            False, 
            [
            _MetaInfoClassMember('request-type-profile', REFERENCE_CLASS, 'RequestTypeProfile' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile', 
                [], [], 
                '''                Container for request type profile.
                ''',
                'request_type_profile',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('requested-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Type of requested bearer Ethernet, DSL,
                Wireless ... Operator specific.
                ''',
                'requested_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('strict', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Define if the requested-type is a preference
                or a strict requirement.
                ''',
                'strict',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'requested-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Bearer' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Bearer',
            False, 
            [
            _MetaInfoClassMember('always-on', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Request for an always on access type.
                This means no Dial access type for
                example.
                ''',
                'always_on',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('bearer-reference', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This is an internal reference for the
                service provider.
                ''',
                'bearer_reference',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('requested-type', REFERENCE_CLASS, 'RequestedType' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType', 
                [], [], 
                '''                Container for requested type.
                ''',
                'requested_type',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'bearer',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vlan' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vlan',
            False, 
            [
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VLAN-ID/Ethernet Tag configurations
                ''',
                'vlan_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vlan',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Dot1Q' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Dot1Q',
            False, 
            [
            _MetaInfoClassMember('physical-inf', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Physical Interface
                ''',
                'physical_inf',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VLAN identifier
                ''',
                'vlan_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'dot1q',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Qinq' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Qinq',
            False, 
            [
            _MetaInfoClassMember('c-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                C-VLAN Identifier
                ''',
                'c_vlan_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('s-vlan-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                S-VLAN Identifier
                ''',
                's_vlan_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'qinq',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan.PeerList' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan.PeerList',
            False, 
            [
            _MetaInfoClassMember('peer-ip', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Peer IP
                ''',
                'peer_ip',
                'ietf-l2vpn-svc', True, [
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer IP
                        ''',
                        'peer_ip',
                        'ietf-l2vpn-svc', True),
                    _MetaInfoClassMember('peer-ip', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Peer IP
                        ''',
                        'peer_ip',
                        'ietf-l2vpn-svc', True),
                ]),
            ],
            'ietf-l2vpn-svc',
            'peer-list',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan',
            False, 
            [
            _MetaInfoClassMember('peer-list', REFERENCE_LIST, 'PeerList' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan.PeerList', 
                [], [], 
                '''                List for peer IP
                ''',
                'peer_list',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vni-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                VNI Identifier
                ''',
                'vni_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vxlan',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.Oam802__Dot__3AhLink' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.Oam802__Dot__3AhLink',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether support oam 802.3 ah link
                ''',
                'enable',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'oam-802.3AH-link',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.EncapsulationTypeEnum' : _MetaInfoEnum('EncapsulationTypeEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'VLAN':'VLAN',
            'Ethernet':'Ethernet',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface',
            False, 
            [
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'EncapsulationTypeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.EncapsulationTypeEnum', 
                [], [], 
                '''                Encapsulation-type
                ''',
                'encapsulation_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ethertype
                ''',
                'ethertype',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('flow-control', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Flow control
                ''',
                'flow_control',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('lldp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LLDP
                ''',
                'lldp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'NegModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'NegModeEnum', 
                [], [], 
                '''                Negotiation mode
                ''',
                'mode',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('oam-802.3AH-link', REFERENCE_CLASS, 'Oam802__Dot__3AhLink' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.Oam802__Dot__3AhLink', 
                [], [], 
                '''                Container for oam 802.3 ah link.
                ''',
                'oam_802_3ah_link',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('phy-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                PHY MTU
                ''',
                'phy_mtu',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port number
                ''',
                'port_number',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('port-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port speed
                ''',
                'port_speed',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('uni-loop-prevention', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If this leaf set to truth that the port automatically
                goes down when a physical loopback is detect.
                ''',
                'uni_loop_prevention',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'phy-interface',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd.MicroBfdOnOffEnum' : _MetaInfoEnum('MicroBfdOnOffEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'on':'on',
            'off':'off',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd',
            False, 
            [
            _MetaInfoClassMember('bfd-hold-timer', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD hold timer
                ''',
                'bfd_hold_timer',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('bfd-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                BFD interval
                ''',
                'bfd_interval',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('Micro-BFD-on-off', REFERENCE_ENUM_CLASS, 'MicroBfdOnOffEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd.MicroBfdOnOffEnum', 
                [], [], 
                '''                Micro BFD ON/OFF
                ''',
                'micro_bfd_on_off',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'Micro-BFD',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.Bfd' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.Bfd',
            False, 
            [
            _MetaInfoClassMember('bfd-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                BFD activation
                ''',
                'bfd_enabled',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('fixed-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Expected hold time expressed in msec.
                ''',
                'fixed_value',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('profile-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service provider well known profile.
                ''',
                'profile_name',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'bfd',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink.Oam802__Dot__3AhLink' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink.Oam802__Dot__3AhLink',
            False, 
            [
            _MetaInfoClassMember('enable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether support oam 802.3 ah link
                ''',
                'enable',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'oam-802.3AH-link',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Member link name
                ''',
                'name',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'NegModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'NegModeEnum', 
                [], [], 
                '''                Negotiation mode
                ''',
                'mode',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MTU
                ''',
                'mtu',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('oam-802.3AH-link', REFERENCE_CLASS, 'Oam802__Dot__3AhLink' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink.Oam802__Dot__3AhLink', 
                [], [], 
                '''                Container for oam 802.3 ah link.
                ''',
                'oam_802_3ah_link',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('port-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Port speed
                ''',
                'port_speed',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'member-link',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList',
            False, 
            [
            _MetaInfoClassMember('member-link', REFERENCE_LIST, 'MemberLink' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink', 
                [], [], 
                '''                Member link
                ''',
                'member_link',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'Member-link-list',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.EncapsulationTypeEnum' : _MetaInfoEnum('EncapsulationTypeEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'VLAN':'VLAN',
            'ether':'ether',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp',
            False, 
            [
            _MetaInfoClassMember('bfd', REFERENCE_CLASS, 'Bfd' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.Bfd', 
                [], [], 
                '''                Container for BFD.
                ''',
                'bfd',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('encapsulation-type', REFERENCE_ENUM_CLASS, 'EncapsulationTypeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.EncapsulationTypeEnum', 
                [], [], 
                '''                Encapsulation type
                ''',
                'encapsulation_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ethertype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ether type
                ''',
                'ethertype',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('flow-control', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Flow control
                ''',
                'flow_control',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('LACP-mode', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LACP mode
                ''',
                'lacp_mode',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('LACP-speed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LACP speed
                ''',
                'lacp_speed',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('LACP-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LACP on/off
                ''',
                'lacp_state',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('lldp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LLDP
                ''',
                'lldp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('Member-link-list', REFERENCE_CLASS, 'MemberLinkList' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList', 
                [], [], 
                '''                Container of Member link list
                ''',
                'member_link_list',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('Micro-BFD', REFERENCE_CLASS, 'MicroBfd' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd', 
                [], [], 
                '''                Container of Micro-BFD configurations
                ''',
                'micro_bfd',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mini-link', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Mini link
                ''',
                'mini_link',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('system-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Indicates the LACP priority for the system.
                The range is from 0 to 65535.
                The default is 32768.
                ''',
                'system_priority',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'LACP',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_',
            False, 
            [
            _MetaInfoClassMember('LAG-interface-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LAG interface number
                ''',
                'lag_interface_number',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('LACP', REFERENCE_CLASS, 'Lacp' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp', 
                [], [], 
                '''                LACP
                ''',
                'lacp',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'LAG-interface',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface',
            False, 
            [
            _MetaInfoClassMember('LAG-interface', REFERENCE_LIST, 'LagInterface_' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_', 
                [], [], 
                '''                List of LAG interfaces
                ''',
                'lag_interface',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'LAG-interface',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection',
            False, 
            [
            _MetaInfoClassMember('dot1q', REFERENCE_CLASS, 'Dot1Q' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Dot1Q', 
                [], [], 
                '''                Qot1q
                ''',
                'dot1q',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ESI', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ethernet segment id
                ''',
                'esi',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('interface-description', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface description
                ''',
                'interface_description',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('LAG-interface', REFERENCE_CLASS, 'LagInterface' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface', 
                [], [], 
                '''                Container of LAG interface attributes configuration
                ''',
                'lag_interface',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('phy-interface', REFERENCE_CLASS, 'PhyInterface' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface', 
                [], [], 
                '''                Container of PHY Interface Attributes configurations
                ''',
                'phy_interface',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('qinq', REFERENCE_CLASS, 'Qinq' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Qinq', 
                [], [], 
                '''                QinQ
                ''',
                'qinq',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('sub-if-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sub interface ID
                ''',
                'sub_if_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vlan', REFERENCE_CLASS, 'Vlan' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vlan', 
                [], [], 
                '''                Abstract container for VLAN
                ''',
                'vlan',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vxlan', REFERENCE_CLASS, 'Vxlan' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan', 
                [], [], 
                '''                QinQ
                ''',
                'vxlan',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'ethernet-connection',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.L2CpControl' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.L2CpControl',
            False, 
            [
            _MetaInfoClassMember('e-lmi', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                E-LMI
                ''',
                'e_lmi',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('esmc', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                ESMC
                ''',
                'esmc',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('garp-mrp', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                GARP/MRP
                ''',
                'garp_mrp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('l2cp-802.1x', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                802.x
                ''',
                'l2cp_802_1x',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('lacp-lamp', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                LACP/LAMP
                ''',
                'lacp_lamp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('link-oam', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                Link OAM
                ''',
                'link_oam',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('lldp', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                LLDP
                ''',
                'lldp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('pause', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                Pause
                ''',
                'pause',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('provider-bridge-group', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                Provider bridge group reserved MAC address
                01-80-C2-00-00-08
                ''',
                'provider_bridge_group',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('provider-bridge-mvrp', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                Provider bridge MVRP reserved MAC address
                01-80-C2-00-00-0D
                ''',
                'provider_bridge_mvrp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ptp-peer-delay', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                PTP peer delay
                ''',
                'ptp_peer_delay',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('stp-rstp-mstp', REFERENCE_ENUM_CLASS, 'ControlModeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ControlModeEnum', 
                [], [], 
                '''                STP/RSTP/MSTP
                ''',
                'stp_rstp_mstp',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'L2CP-control',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Availability' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Availability',
            False, 
            [
            _MetaInfoClassMember('all-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                All active
                ''',
                'all_active',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('single-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Single active
                ''',
                'single_active',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'availability',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment.Management' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment.Management',
            False, 
            [
            _MetaInfoClassMember('address', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Management address
                ''',
                'address',
                'ietf-l2vpn-svc', False, [
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Management address
                        ''',
                        'address',
                        'ietf-l2vpn-svc', False),
                    _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                        [], ['((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                        '''                        Management address
                        ''',
                        'address',
                        'ietf-l2vpn-svc', False),
                ]),
            _MetaInfoClassMember('address-family', REFERENCE_IDENTITY_CLASS, 'AddressFamilyIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'AddressFamilyIdentity', 
                [], [], 
                '''                Address family used for management.
                ''',
                'address_family',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'management',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment',
            False, 
            [
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device ID
                ''',
                'device_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('management', REFERENCE_CLASS, 'Management' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment.Management', 
                [], [], 
                '''                Management configuration..
                ''',
                'management',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('site-role', REFERENCE_IDENTITY_CLASS, 'SiteRoleIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'SiteRoleIdentity', 
                [], [], 
                '''                Role of the site in the IPVPN.
                ''',
                'site_role',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reference to a VPN.
                ''',
                'vpn_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'vpn-attachment',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth.InputBandwidth' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth.InputBandwidth',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ID
                ''',
                'id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'BwTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'BwTypeIdentity', 
                [], [], 
                '''                Bandwidth Type
                ''',
                'type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('CBS', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed Burst Size
                ''',
                'cbs',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('CIR', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed Information Rate
                ''',
                'cir',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('CM', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Color Mode
                ''',
                'cm',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('EBS', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Burst Size
                ''',
                'ebs',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('EIR', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Information Rate
                ''',
                'eir',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('evc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EVC ID
                ''',
                'evc_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'input-bandwidth',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth',
            False, 
            [
            _MetaInfoClassMember('input-bandwidth', REFERENCE_LIST, 'InputBandwidth' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth.InputBandwidth', 
                [], [], 
                '''                List for input bandwidth
                ''',
                'input_bandwidth',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'svc-input-bandwidth',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth.OutputBandwidth' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth.OutputBandwidth',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ID
                ''',
                'id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'BwTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'BwTypeIdentity', 
                [], [], 
                '''                Bandwidth Type
                ''',
                'type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('CBS', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed Burst Size
                ''',
                'cbs',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('CIR', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Committed Information Rate
                ''',
                'cir',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('CM', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Color Mode
                ''',
                'cm',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('EBS', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Burst Size
                ''',
                'ebs',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('EIR', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Excess Information Rate
                ''',
                'eir',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('evc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EVC ID
                ''',
                'evc_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'output-bandwidth',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth',
            False, 
            [
            _MetaInfoClassMember('output-bandwidth', REFERENCE_LIST, 'OutputBandwidth' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth.OutputBandwidth', 
                [], [], 
                '''                List for output bandwidth
                ''',
                'output_bandwidth',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'svc-output-bandwidth',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap.CvlanId' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap.CvlanId',
            False, 
            [
            _MetaInfoClassMember('vid', REFERENCE_IDENTITY_CLASS, 'IanaInterfaceTypeIdentity' , 'ydk.models.ietf.iana_if_type', 'IanaInterfaceTypeIdentity', 
                [], [], 
                '''                CVLAN ID
                ''',
                'vid',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'cvlan-id',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap',
            False, 
            [
            _MetaInfoClassMember('evc-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EVC ID
                ''',
                'evc_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'BundlingTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'BundlingTypeIdentity', 
                [], [], 
                '''                Bundling type
                ''',
                'type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('cvlan-id', REFERENCE_LIST, 'CvlanId' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap.CvlanId', 
                [], [], 
                '''                List of CVLAN-ID to EVC Map configurations
                ''',
                'cvlan_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'cvlan-id-to-evc-map',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow.CosColorId' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow.CosColorId',
            False, 
            [
            _MetaInfoClassMember('cos-label', REFERENCE_IDENTITY_CLASS, 'CosIdIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'CosIdIdentity', 
                [], [], 
                '''                COS label
                ''',
                'cos_label',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Device ID
                ''',
                'device_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                DSCP value.
                ''',
                'dscp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCP value
                ''',
                'pcp',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'cos-color-id',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow',
            False, 
            [
            _MetaInfoClassMember('color-type', REFERENCE_IDENTITY_CLASS, 'ColorTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'ColorTypeIdentity', 
                [], [], 
                '''                Color Types
                ''',
                'color_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('cos-color-id', REFERENCE_CLASS, 'CosColorId' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow.CosColorId', 
                [], [], 
                '''                Container for cos color id
                ''',
                'cos_color_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('dot1p', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                802.1p matching.
                ''',
                'dot1p',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('dscp', ATTRIBUTE, 'int' , None, None, 
                [('0', '63')], [], 
                '''                DSCP value.
                ''',
                'dscp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('dst-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Destination MAC
                ''',
                'dst_mac',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('pcp', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                PCP value
                ''',
                'pcp',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('src-mac', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Source MAC
                ''',
                'src_mac',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('target-sites', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Identify a site as traffic destination.
                ''',
                'target_sites',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'match-flow',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule',
            False, 
            [
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                ID of the rule.
                ''',
                'id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('match-flow', REFERENCE_CLASS, 'MatchFlow' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow', 
                [], [], 
                '''                Describe flow matching criterions.
                ''',
                'match_flow',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('match-phy-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Defines the physical port
                to match.
                ''',
                'match_phy_port',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('target-class-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identification of the class of service.
                This identifier is internal to the
                administration.
                ''',
                'target_class_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'rule',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy',
            False, 
            [
            _MetaInfoClassMember('rule', REFERENCE_LIST, 'Rule' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule', 
                [], [], 
                '''                List of marking rules.
                ''',
                'rule',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'qos-classification-policy',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameDelay' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameDelay',
            False, 
            [
            _MetaInfoClassMember('delay-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The traffic class should use
                a path with a defined maximum
                delay.
                ''',
                'delay_bound',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('use-low-del', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The traffic class should use
                the lowest delay path
                ''',
                'use_low_del',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'frame-delay',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameJitter' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameJitter',
            False, 
            [
            _MetaInfoClassMember('delay-bound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The traffic class should use
                a path with a defined maximum
                jitter.
                ''',
                'delay_bound',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('use-low-jit', ATTRIBUTE, 'Empty' , None, None, 
                [], [], 
                '''                The traffic class should use
                the lowest jitter path
                ''',
                'use_low_jit',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'frame-jitter',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameLoss' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameLoss',
            False, 
            [
            _MetaInfoClassMember('fr-loss-rate', ATTRIBUTE, 'Decimal64' , None, None, 
                [('-92233720368547758.08', '92233720368547758.07')], [], 
                '''                Loss constraint on the traffic class
                ''',
                'fr_loss_rate',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'frame-loss',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_',
            False, 
            [
            _MetaInfoClassMember('class-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identification of the class of
                service. This identifier is internal
                to the administration.
                ''',
                'class_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('byte-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                For not including extra VLAN tags in the QoS
                calculation
                ''',
                'byte_offset',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('direction', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Direction type
                ''',
                'direction',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('discard-percentage', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The value of the discard-percentage,
                Expressed as pecentage of the svc-bw 
                ''',
                'discard_percentage',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('frame-delay', REFERENCE_CLASS, 'FrameDelay' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameDelay', 
                [], [], 
                '''                Delay constraint on the traffic
                class
                ''',
                'frame_delay',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('frame-jitter', REFERENCE_CLASS, 'FrameJitter' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameJitter', 
                [], [], 
                '''                Jitter constraint on the traffic
                class
                ''',
                'frame_jitter',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('frame-loss', REFERENCE_CLASS, 'FrameLoss' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameLoss', 
                [], [], 
                '''                Container for frame loss
                ''',
                'frame_loss',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('perf-tier-opt', REFERENCE_IDENTITY_CLASS, 'PerfTierOptIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'PerfTierOptIdentity', 
                [], [], 
                '''                Performance tier option
                ''',
                'perf_tier_opt',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('policing', REFERENCE_IDENTITY_CLASS, 'PolicingIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'PolicingIdentity', 
                [], [], 
                '''                The policing can be either one-rate,
                two-color (1R2C) or two-rate, three-color
                (2R3C)
                ''',
                'policing',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('rate-limit', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                To be used if class must be rate limited.
                Expressed as percentage of the svc-bw.
                ''',
                'rate_limit',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'class',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes',
            False, 
            [
            _MetaInfoClassMember('class', REFERENCE_LIST, 'Class_' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_', 
                [], [], 
                '''                List of class of services.
                ''',
                'class_',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'classes',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile',
            False, 
            [
            _MetaInfoClassMember('classes', REFERENCE_CLASS, 'Classes' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes', 
                [], [], 
                '''                Container for list of class of services.
                ''',
                'classes',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('egress-profile', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Egress QoS Profile to be used
                ''',
                'egress_profile',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ingress-profile', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ingress QoS Profile to be used
                ''',
                'ingress_profile',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'qos-profile',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service.Qos',
            False, 
            [
            _MetaInfoClassMember('qos-classification-policy', REFERENCE_CLASS, 'QosClassificationPolicy' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy', 
                [], [], 
                '''                Need to express marking rules ...
                ''',
                'qos_classification_policy',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('qos-profile', REFERENCE_CLASS, 'QosProfile' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile', 
                [], [], 
                '''                Qos profile configuration.
                ''',
                'qos_profile',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'qos',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.Service' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.Service',
            False, 
            [
            _MetaInfoClassMember('cvlan-id-to-evc-map', REFERENCE_LIST, 'CvlanIdToEvcMap' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap', 
                [], [], 
                '''                List for cvlan-id to evc map configurations
                ''',
                'cvlan_id_to_evc_map',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('qos', REFERENCE_CLASS, 'Qos' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.Qos', 
                [], [], 
                '''                QoS configuration.
                ''',
                'qos',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('service-level-mac-limit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Service-level MAC-limit (E-LAN only)
                ''',
                'service_level_mac_limit',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('service-multiplexing', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Service multiplexing
                ''',
                'service_multiplexing',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('svc-input-bandwidth', REFERENCE_CLASS, 'SvcInputBandwidth' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth', 
                [], [], 
                '''                From the PE perspective, the service input
                bandwidth of the connection.
                ''',
                'svc_input_bandwidth',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('svc-output-bandwidth', REFERENCE_CLASS, 'SvcOutputBandwidth' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth', 
                [], [], 
                '''                From the PE perspective, the service output
                bandwidth of the connection.
                ''',
                'svc_output_bandwidth',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('svlan-id-ethernet-tag', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SVLAN-ID/Ethernet Tag configurations
                ''',
                'svlan_id_ethernet_tag',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'service',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC.MepUpDownEnum' : _MetaInfoEnum('MepUpDownEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'up':'up',
            'down':'down',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC',
            False, 
            [
            _MetaInfoClassMember('MAID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MA ID
                ''',
                'maid',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('alarm-priority-defect', REFERENCE_IDENTITY_CLASS, 'FaultAlarmDefectTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'FaultAlarmDefectTypeIdentity', 
                [], [], 
                '''                The lowest priority defect that is
                allowed to generate a Fault Alarm.
                The non-existence of this leaf means
                that no defects are to be reported
                ''',
                'alarm_priority_defect',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ccm-holdtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCM hold time
                ''',
                'ccm_holdtime',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ccm-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCM interval
                ''',
                'ccm_interval',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ccm-p-bits-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                The priority parameter for CCMs transmitted by the MEP
                ''',
                'ccm_p_bits_pri',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('cos-for-cfm-pdus', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COS for CFM PDUs
                ''',
                'cos_for_cfm_pdus',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local MEP ID
                ''',
                'mep_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mep-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MEP level
                ''',
                'mep_level',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mep-up-down', REFERENCE_ENUM_CLASS, 'MepUpDownEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC.MepUpDownEnum', 
                [], [], 
                '''                MEP up/down
                ''',
                'mep_up_down',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('remote-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote MEP ID
                ''',
                'remote_mep_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'n2-uni-c',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN.MepUpDownEnum' : _MetaInfoEnum('MepUpDownEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'up':'up',
            'down':'down',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN',
            False, 
            [
            _MetaInfoClassMember('MAID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MA ID
                ''',
                'maid',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('alarm-priority-defect', REFERENCE_IDENTITY_CLASS, 'FaultAlarmDefectTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'FaultAlarmDefectTypeIdentity', 
                [], [], 
                '''                The lowest priority defect that is
                allowed to generate a Fault Alarm.
                The non-existence of this leaf means
                that no defects are to be reported
                ''',
                'alarm_priority_defect',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ccm-holdtime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCM hold time
                ''',
                'ccm_holdtime',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ccm-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                CCM interval
                ''',
                'ccm_interval',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ccm-p-bits-pri', ATTRIBUTE, 'int' , None, None, 
                [('0', '7')], [], 
                '''                The priority parameter for CCMs transmitted by the MEP
                ''',
                'ccm_p_bits_pri',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('cos-for-cfm-pdus', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                COS for CFM PDUs
                ''',
                'cos_for_cfm_pdus',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local MEP ID
                ''',
                'mep_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mep-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MEP level
                ''',
                'mep_level',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mep-up-down', REFERENCE_ENUM_CLASS, 'MepUpDownEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN.MepUpDownEnum', 
                [], [], 
                '''                MEP up/down
                ''',
                'mep_up_down',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('remote-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote MEP ID
                ''',
                'remote_mep_id',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'n2-uni-n',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag',
            False, 
            [
            _MetaInfoClassMember('n2-uni-c', REFERENCE_LIST, 'N2UniC' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC', 
                [], [], 
                '''                List of UNI-N to UNI-C
                ''',
                'n2_uni_c',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('n2-uni-n', REFERENCE_LIST, 'N2UniN' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN', 
                [], [], 
                '''                List of UNI-N to UNI-N
                ''',
                'n2_uni_n',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'cfm-802.1-ag',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.DelayMeasurement' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.DelayMeasurement',
            False, 
            [
            _MetaInfoClassMember('enable-dm', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether to enable delay measurement
                ''',
                'enable_dm',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('two-way', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether delay measurement is two-way (true) of one-
                way (false)
                ''',
                'two_way',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'delay-measurement',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.SessionTypeEnum' : _MetaInfoEnum('SessionTypeEnum', 'ydk.models.ietf.ietf_l2vpn_svc',
        {
            'proactive':'proactive',
            'on-demand':'on_demand',
        }, 'ietf-l2vpn-svc', _yang_ns._namespaces['ietf-l2vpn-svc']),
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731',
            False, 
            [
            _MetaInfoClassMember('MAID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MA ID 
                ''',
                'maid',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('cos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Class of service
                ''',
                'cos',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('delay-measurement', REFERENCE_CLASS, 'DelayMeasurement' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.DelayMeasurement', 
                [], [], 
                '''                Container for delay measurement
                ''',
                'delay_measurement',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('frame-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Frame size
                ''',
                'frame_size',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('loss-measurement', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether enable loss measurement
                ''',
                'loss_measurement',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('measurement-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Specifies the measurement interval for statistics. The
                measurement interval is expressed in seconds
                ''',
                'measurement_interval',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Local MEP ID
                ''',
                'mep_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('message-period', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Defines the interval between OAM messages. The message
                period is expressed in milliseconds
                ''',
                'message_period',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('remote-mep-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote MEP ID
                ''',
                'remote_mep_id',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('session-type', REFERENCE_ENUM_CLASS, 'SessionTypeEnum' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.SessionTypeEnum', 
                [], [], 
                '''                Session type
                ''',
                'session_type',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('synthethic-loss-measurement', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicate whether enable synthetic loss measurement
                ''',
                'synthethic_loss_measurement',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'PmTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'PmTypeIdentity', 
                [], [], 
                '''                Performance monitor types
                ''',
                'type',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'y-1731',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam',
            False, 
            [
            _MetaInfoClassMember('cfm-802.1-ag', REFERENCE_CLASS, 'Cfm802__Dot__1Ag' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag', 
                [], [], 
                '''                Container of 802.1ag CFM configurations.
                ''',
                'cfm_802_1_ag',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('MD-level', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Maintenance domain level
                ''',
                'md_level',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('MD-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maintenance domain name
                ''',
                'md_name',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('y-1731', REFERENCE_LIST, 'Y1731' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731', 
                [], [], 
                '''                List for y-1731.
                ''',
                'y_1731',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'Ethernet-Service-OAM',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacLoopPrevention' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacLoopPrevention',
            False, 
            [
            _MetaInfoClassMember('frequency', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Frequency
                ''',
                'frequency',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('number-retries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retries
                ''',
                'number_retries',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('protection-type', REFERENCE_IDENTITY_CLASS, 'LoopPreventionTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'LoopPreventionTypeIdentity', 
                [], [], 
                '''                Protection type
                ''',
                'protection_type',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'mac-loop-prevention',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList.Mac' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList.Mac',
            False, 
            [
            _MetaInfoClassMember('mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                MAC address
                ''',
                'mac_address',
                'ietf-l2vpn-svc', True),
            ],
            'ietf-l2vpn-svc',
            'mac',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList',
            False, 
            [
            _MetaInfoClassMember('mac', REFERENCE_LIST, 'Mac' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList.Mac', 
                [], [], 
                '''                List for MAC
                ''',
                'mac',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'access-control-list',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacAddrLimit' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacAddrLimit',
            False, 
            [
            _MetaInfoClassMember('exceeding-option', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Exceeding option
                ''',
                'exceeding_option',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'mac-addr-limit',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl.BumRatePerType' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl.BumRatePerType',
            False, 
            [
            _MetaInfoClassMember('type', REFERENCE_IDENTITY_CLASS, 'BumTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'BumTypeIdentity', 
                [], [], 
                '''                BUM type
                ''',
                'type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                rate for BUM
                ''',
                'rate',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'BUM-rate-per-type',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl',
            False, 
            [
            _MetaInfoClassMember('BUM-overall-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                overall rate for BUM
                ''',
                'bum_overall_rate',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('BUM-rate-per-type', REFERENCE_LIST, 'BumRatePerType' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl.BumRatePerType', 
                [], [], 
                '''                List of rate per type
                ''',
                'bum_rate_per_type',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'B-U-M-storm-control',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering',
            False, 
            [
            _MetaInfoClassMember('access-control-list', REFERENCE_CLASS, 'AccessControlList' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList', 
                [], [], 
                '''                Container for access control
                ''',
                'access_control_list',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('B-U-M-storm-control', REFERENCE_CLASS, 'BUMStormControl' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl', 
                [], [], 
                '''                Container of B-U-M-strom-control configurations
                ''',
                'b_u_m_storm_control',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mac-addr-limit', REFERENCE_CLASS, 'MacAddrLimit' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacAddrLimit', 
                [], [], 
                '''                Container of MAC-Addr limit configurations
                ''',
                'mac_addr_limit',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('mac-loop-prevention', REFERENCE_CLASS, 'MacLoopPrevention' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacLoopPrevention', 
                [], [], 
                '''                Container of MAC loop prevention.
                ''',
                'mac_loop_prevention',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'security-filtering',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports.Port' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports.Port',
            False, 
            [
            _MetaInfoClassMember('network-access-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifier of network access
                ''',
                'network_access_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('access-diversity', REFERENCE_CLASS, 'AccessDiversity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity', 
                [], [], 
                '''                Diversity parameters.
                ''',
                'access_diversity',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('availability', REFERENCE_CLASS, 'Availability' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Availability', 
                [], [], 
                '''                Container of availability optional configurations
                ''',
                'availability',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('bearer', REFERENCE_CLASS, 'Bearer' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Bearer', 
                [], [], 
                '''                Bearer specific parameters.
                To be augmented.
                ''',
                'bearer',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ethernet-connection', REFERENCE_CLASS, 'EthernetConnection' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection', 
                [], [], 
                '''                Container for bearer
                ''',
                'ethernet_connection',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('Ethernet-Service-OAM', REFERENCE_CLASS, 'EthernetServiceOam' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam', 
                [], [], 
                '''                Container for Ethernet service OAM.
                ''',
                'ethernet_service_oam',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('evc-mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                EVC MTU
                ''',
                'evc_mtu',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('L2CP-control', REFERENCE_CLASS, 'L2CpControl' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.L2CpControl', 
                [], [], 
                '''                Container of L2CP control configurations
                ''',
                'l2cp_control',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('remote-carrier-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote carrier name
                ''',
                'remote_carrier_name',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('security-filtering', REFERENCE_CLASS, 'SecurityFiltering' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering', 
                [], [], 
                '''                Security parameters
                ''',
                'security_filtering',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('service', REFERENCE_CLASS, 'Service' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.Service', 
                [], [], 
                '''                Container for service
                ''',
                'service',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn-attachment', REFERENCE_CLASS, 'VpnAttachment' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment', 
                [], [], 
                '''                Defines VPN attachment of a site.
                ''',
                'vpn_attachment',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'port',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site.Ports' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site.Ports',
            False, 
            [
            _MetaInfoClassMember('port', REFERENCE_LIST, 'Port' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports.Port', 
                [], [], 
                '''                List of ports
                ''',
                'port',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'ports',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites.Site' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites.Site',
            False, 
            [
            _MetaInfoClassMember('site-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Site id
                ''',
                'site_id',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('site-type', REFERENCE_IDENTITY_CLASS, 'SiteTypeIdentity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'SiteTypeIdentity', 
                [], [], 
                '''                Site type
                ''',
                'site_type',
                'ietf-l2vpn-svc', True),
            _MetaInfoClassMember('actual-site-start', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Optional leaf indicating actual date
                and time when the service at a particular
                site actually started
                ''',
                'actual_site_start',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('actual-site-stop', ATTRIBUTE, 'str' , None, None, 
                [], ['\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Optional leaf indicating actual date
                and time when the service at a particular
                site actually stopped
                ''',
                'actual_site_stop',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('device', REFERENCE_CLASS, 'Device' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Device', 
                [], [], 
                '''                Devices configuration
                ''',
                'device',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('load-balance-options', REFERENCE_CLASS, 'LoadBalanceOptions' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.LoadBalanceOptions', 
                [], [], 
                '''                Container for load balance options
                ''',
                'load_balance_options',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('location', REFERENCE_CLASS, 'Location' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Location', 
                [], [], 
                '''                Location of the site.
                ''',
                'location',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('managemnt', REFERENCE_CLASS, 'Managemnt' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Managemnt', 
                [], [], 
                '''                Container for management
                ''',
                'managemnt',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('ports', REFERENCE_CLASS, 'Ports' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.Ports', 
                [], [], 
                '''                Container of port configurations
                ''',
                'ports',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('signaling-option', REFERENCE_CLASS, 'SignalingOption' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SignalingOption', 
                [], [], 
                '''                Container for signaling option
                ''',
                'signaling_option',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('site-diversity', REFERENCE_CLASS, 'SiteDiversity' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.SiteDiversity', 
                [], [], 
                '''                Diversity constraint type.
                ''',
                'site_diversity',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn-policies', REFERENCE_CLASS, 'VpnPolicies' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site.VpnPolicies', 
                [], [], 
                '''                VPN policy.
                ''',
                'vpn_policies',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'site',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc.Sites' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc.Sites',
            False, 
            [
            _MetaInfoClassMember('site', REFERENCE_LIST, 'Site' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites.Site', 
                [], [], 
                '''                List of sites
                ''',
                'site',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'sites',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'L2VpnSvc' : {
        'meta_info' : _MetaInfoClass('L2VpnSvc',
            False, 
            [
            _MetaInfoClassMember('customer-info', REFERENCE_CLASS, 'CustomerInfo' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.CustomerInfo', 
                [], [], 
                '''                Container for customer information.
                ''',
                'customer_info',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('sites', REFERENCE_CLASS, 'Sites' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.Sites', 
                [], [], 
                '''                Container of site configurations
                ''',
                'sites',
                'ietf-l2vpn-svc', False),
            _MetaInfoClassMember('vpn-services', REFERENCE_CLASS, 'VpnServices' , 'ydk.models.ietf.ietf_l2vpn_svc', 'L2VpnSvc.VpnServices', 
                [], [], 
                '''                Container for VPN services.
                ''',
                'vpn_services',
                'ietf-l2vpn-svc', False),
            ],
            'ietf-l2vpn-svc',
            'l2vpn-svc',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'DataPlaneIdentity' : {
        'meta_info' : _MetaInfoClass('DataPlaneIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'data-plane',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'GlobalIdentity' : {
        'meta_info' : _MetaInfoClass('GlobalIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'global',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CosIdEvcDscpIdentity' : {
        'meta_info' : _MetaInfoClass('CosIdEvcDscpIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'cos-id-evc-dscp',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'BwPerCosIdentity' : {
        'meta_info' : _MetaInfoClass('BwPerCosIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'bw-per-cos',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ProviderManagedIdentity' : {
        'meta_info' : _MetaInfoClass('ProviderManagedIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'provider-managed',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'EnniIdentity' : {
        'meta_info' : _MetaInfoClass('EnniIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'enni',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpOnIdentity' : {
        'meta_info' : _MetaInfoClass('LacpOnIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-on',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'VxlanIdentity' : {
        'meta_info' : _MetaInfoClass('VxlanIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'vxlan',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpSlowIdentity' : {
        'meta_info' : _MetaInfoClass('LacpSlowIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-slow',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'EviIdentity' : {
        'meta_info' : _MetaInfoClass('EviIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'evi',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'RegionalIdentity' : {
        'meta_info' : _MetaInfoClass('RegionalIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'regional',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CoManagedIdentity' : {
        'meta_info' : _MetaInfoClass('CoManagedIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'co-managed',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'HubRoleIdentity' : {
        'meta_info' : _MetaInfoClass('HubRoleIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'hub-role',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'YellowIdentity' : {
        'meta_info' : _MetaInfoClass('YellowIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'yellow',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'RootedMultipointIdentity' : {
        'meta_info' : _MetaInfoClass('RootedMultipointIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'rooted-multipoint',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'EvpnIdentity' : {
        'meta_info' : _MetaInfoClass('EvpnIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'evpn',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LossIdentity' : {
        'meta_info' : _MetaInfoClass('LossIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'loss',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'MultipointToMultipointIdentity' : {
        'meta_info' : _MetaInfoClass('MultipointToMultipointIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'multipoint-to-multipoint',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'EvcIdentity' : {
        'meta_info' : _MetaInfoClass('EvcIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'evc',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'RemoteMacErrorIdentity' : {
        'meta_info' : _MetaInfoClass('RemoteMacErrorIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'remote-mac-error',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'VpwsIdentity' : {
        'meta_info' : _MetaInfoClass('VpwsIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'vpws',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'TrapIdentity' : {
        'meta_info' : _MetaInfoClass('TrapIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'trap',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'OneRateTwoColorIdentity' : {
        'meta_info' : _MetaInfoClass('OneRateTwoColorIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'one-rate-two-color',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'HubSpokeIdentity' : {
        'meta_info' : _MetaInfoClass('HubSpokeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'hub-spoke',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'BundlingIdentity' : {
        'meta_info' : _MetaInfoClass('BundlingIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'bundling',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ConditionalIdentity' : {
        'meta_info' : _MetaInfoClass('ConditionalIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'conditional',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CosIdEvcPcpIdentity' : {
        'meta_info' : _MetaInfoClass('CosIdEvcPcpIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'cos-id-evc-pcp',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'HubSpokeDisjointIdentity' : {
        'meta_info' : _MetaInfoClass('HubSpokeDisjointIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'hub-spoke-disjoint',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PortIdentity' : {
        'meta_info' : _MetaInfoClass('PortIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'port',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ColorIdEvcIdentity' : {
        'meta_info' : _MetaInfoClass('ColorIdEvcIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'color-id-evc',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'InvalidCcmIdentity' : {
        'meta_info' : _MetaInfoClass('InvalidCcmIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'invalid-ccm',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'OpaqueIdentity' : {
        'meta_info' : _MetaInfoClass('OpaqueIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'opaque',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PeDiverseIdentity' : {
        'meta_info' : _MetaInfoClass('PeDiverseIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'pe-diverse',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'SamePeIdentity' : {
        'meta_info' : _MetaInfoClass('SamePeIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'same-pe',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'RedIdentity' : {
        'meta_info' : _MetaInfoClass('RedIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'red',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ShutIdentity' : {
        'meta_info' : _MetaInfoClass('ShutIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'shut',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LinecardDiverseIdentity' : {
        'meta_info' : _MetaInfoClass('LinecardDiverseIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'linecard-diverse',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'BearerDiverseIdentity' : {
        'meta_info' : _MetaInfoClass('BearerDiverseIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'bearer-diverse',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'AnyToAnyIdentity' : {
        'meta_info' : _MetaInfoClass('AnyToAnyIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'any-to-any',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'VrfIdentity' : {
        'meta_info' : _MetaInfoClass('VrfIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'vrf',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'AnyToAnyRoleIdentity' : {
        'meta_info' : _MetaInfoClass('AnyToAnyRoleIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'any-to-any-role',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpActiveIdentity' : {
        'meta_info' : _MetaInfoClass('LacpActiveIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-active',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'MetroIdentity' : {
        'meta_info' : _MetaInfoClass('MetroIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'metro',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PopDiverseIdentity' : {
        'meta_info' : _MetaInfoClass('PopDiverseIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'pop-diverse',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'MulticastIdentity' : {
        'meta_info' : _MetaInfoClass('MulticastIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'multicast',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'RemoteInvalidCcmIdentity' : {
        'meta_info' : _MetaInfoClass('RemoteInvalidCcmIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'remote-invalid-ccm',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'DiscardIdentity' : {
        'meta_info' : _MetaInfoClass('DiscardIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'discard',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'TwoRateThreeColorIdentity' : {
        'meta_info' : _MetaInfoClass('TwoRateThreeColorIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'two-rate-three-color',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpPassiveIdentity' : {
        'meta_info' : _MetaInfoClass('LacpPassiveIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-passive',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ContinentalIdentity' : {
        'meta_info' : _MetaInfoClass('ContinentalIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'continental',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ControlPlaneIdentity' : {
        'meta_info' : _MetaInfoClass('ControlPlaneIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'control-plane',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'Ipv4Identity' : {
        'meta_info' : _MetaInfoClass('Ipv4Identity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'ipv4',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'Ipv6Identity' : {
        'meta_info' : _MetaInfoClass('Ipv6Identity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'ipv6',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'SubInterfaceIdentity' : {
        'meta_info' : _MetaInfoClass('SubInterfaceIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'sub-interface',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'BroadcastIdentity' : {
        'meta_info' : _MetaInfoClass('BroadcastIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'broadcast',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'UniIdentity' : {
        'meta_info' : _MetaInfoClass('UniIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'uni',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'UntagIdentity' : {
        'meta_info' : _MetaInfoClass('UntagIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'untag',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CustomerManagedIdentity' : {
        'meta_info' : _MetaInfoClass('CustomerManagedIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'customer-managed',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'Dot1QIdentity' : {
        'meta_info' : _MetaInfoClass('Dot1QIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'dot1q',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpOffIdentity' : {
        'meta_info' : _MetaInfoClass('LacpOffIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-off',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'UnconditionalIdentity' : {
        'meta_info' : _MetaInfoClass('UnconditionalIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'unconditional',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'UnicastIdentity' : {
        'meta_info' : _MetaInfoClass('UnicastIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'unicast',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'LacpFastIdentity' : {
        'meta_info' : _MetaInfoClass('LacpFastIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'lacp-fast',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'DelayIdentity' : {
        'meta_info' : _MetaInfoClass('DelayIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'delay',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'ColorIdEvcCvlanIdentity' : {
        'meta_info' : _MetaInfoClass('ColorIdEvcCvlanIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'color-id-evc-cvlan',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'GreenIdentity' : {
        'meta_info' : _MetaInfoClass('GreenIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'green',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'SpokeRoleIdentity' : {
        'meta_info' : _MetaInfoClass('SpokeRoleIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'spoke-role',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'QinqIdentity' : {
        'meta_info' : _MetaInfoClass('QinqIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'qinq',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'PointToPointIdentity' : {
        'meta_info' : _MetaInfoClass('PointToPointIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'point-to-point',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CrossConnectCcmIdentity' : {
        'meta_info' : _MetaInfoClass('CrossConnectCcmIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'cross-connect-ccm',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'SameBearerIdentity' : {
        'meta_info' : _MetaInfoClass('SameBearerIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'same-bearer',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'All2OneBundlingIdentity' : {
        'meta_info' : _MetaInfoClass('All2OneBundlingIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'all2one-Bundling',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'OvcIdentity' : {
        'meta_info' : _MetaInfoClass('OvcIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'ovc',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'VplsIdentity' : {
        'meta_info' : _MetaInfoClass('VplsIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'vpls',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CosIdEvcIdentity' : {
        'meta_info' : _MetaInfoClass('CosIdEvcIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'cos-id-evc',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'VfiIdentity' : {
        'meta_info' : _MetaInfoClass('VfiIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'vfi',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'CosIdOvcEpIdentity' : {
        'meta_info' : _MetaInfoClass('CosIdOvcEpIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'cos-id-ovc-ep',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
    'RemoteRdiIdentity' : {
        'meta_info' : _MetaInfoClass('RemoteRdiIdentity',
            False, 
            [
            ],
            'ietf-l2vpn-svc',
            'remote-rdi',
            _yang_ns._namespaces['ietf-l2vpn-svc'],
        'ydk.models.ietf.ietf_l2vpn_svc'
        ),
    },
}
_meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter.CustomerNocPhoneNumber']['meta_info'].parent =_meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter']['meta_info']
_meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_.CustomerOperationCenter']['meta_info'].parent =_meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_']['meta_info']
_meta_table['L2VpnSvc.CustomerInfo.CustomerInfo_']['meta_info'].parent =_meta_table['L2VpnSvc.CustomerInfo']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList.UniList_']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType.UniList']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.OvcType.OvcList']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.OvcType']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites.AuthorizedSite']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites.DeniedSite']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.AuthorizedSites']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess.DeniedSites']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses.CloudAccess']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId.IntraMkt']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap.CvlanId']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.ProtectionModel']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection.PeerEvcId']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.EvcType']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.OvcType']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.EthernetSvcType']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CloudAccesses']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CeVlanPreservation']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.MetroNetworkId']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.L2CpControl']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.LoadBalanceOptions']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.CvlanIdToEvcMap']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.ServiceProtection']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc.SlaTargets']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices.VpnSvc']['meta_info'].parent =_meta_table['L2VpnSvc.VpnServices']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Device.Devices.Management']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Device.Devices']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Device.Devices']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Device']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SiteDiversity.Groups.Group']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SiteDiversity.Groups']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SiteDiversity.Groups']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SiteDiversity']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Filter']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries.Vpn']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy.Entries']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.VpnPolicies.VpnPolicy']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.VpnPolicies']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe.PeEgList']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpL2Vpn']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.MpBgpEvpn']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.TLdpPwe']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweEncapsulationType']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.PweMtu']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_.ControlWord']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption.SignalingOption_']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.SignalingOption']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups.Group']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target.Group']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint.Target']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints.Constraint']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Groups']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity.Constraints']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile.Dot1Q']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType.RequestTypeProfile']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer.RequestedType']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan.PeerList']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface.Oam802__Dot__3AhLink']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink.Oam802__Dot__3AhLink']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList.MemberLink']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MicroBfd']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.Bfd']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp.MemberLinkList']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_.Lacp']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface.LagInterface_']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vlan']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Dot1Q']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Qinq']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.Vxlan']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.PhyInterface']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection.LagInterface']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment.Management']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth.InputBandwidth']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth.OutputBandwidth']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap.CvlanId']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow.CosColorId']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule.MatchFlow']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy.Rule']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameDelay']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameJitter']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_.FrameLoss']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes.Class_']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile.Classes']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosClassificationPolicy']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos.QosProfile']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcInputBandwidth']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.SvcOutputBandwidth']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.CvlanIdToEvcMap']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service.Qos']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniC']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag.N2UniN']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731.DelayMeasurement']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Cfm802__Dot__1Ag']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam.Y1731']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList.Mac']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl.BumRatePerType']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacLoopPrevention']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.AccessControlList']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.MacAddrLimit']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering.BUMStormControl']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.AccessDiversity']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Bearer']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetConnection']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.L2CpControl']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Availability']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.VpnAttachment']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.Service']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.EthernetServiceOam']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port.SecurityFiltering']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports.Port']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site.Ports']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Device']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Managemnt']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Location']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SiteDiversity']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.VpnPolicies']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.SignalingOption']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.LoadBalanceOptions']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site.Ports']['meta_info'].parent =_meta_table['L2VpnSvc.Sites.Site']['meta_info']
_meta_table['L2VpnSvc.Sites.Site']['meta_info'].parent =_meta_table['L2VpnSvc.Sites']['meta_info']
_meta_table['L2VpnSvc.CustomerInfo']['meta_info'].parent =_meta_table['L2VpnSvc']['meta_info']
_meta_table['L2VpnSvc.VpnServices']['meta_info'].parent =_meta_table['L2VpnSvc']['meta_info']
_meta_table['L2VpnSvc.Sites']['meta_info'].parent =_meta_table['L2VpnSvc']['meta_info']
