


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'this-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'far-end-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId',
            False, 
            [
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'far-end-link-in-hw',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                oper state
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                error state
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                timestamp
                ''',
                'timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reasons', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reasons
                ''',
                'reasons',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'hist',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History',
            False, 
            [
            _MetaInfoClassMember('histnum', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                histnum
                ''',
                'histnum',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                start index
                ''',
                'start_index',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('hist', REFERENCE_LIST, 'Hist' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist', 
                [], [], 
                '''                hist
                ''',
                'hist',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=5),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink',
            False, 
            [
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Single link
                ''',
                'link',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('this-link', REFERENCE_CLASS, 'ThisLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink', 
                [], [], 
                '''                this link
                ''',
                'this_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('far-end-link', REFERENCE_CLASS, 'FarEndLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink', 
                [], [], 
                '''                far end link
                ''',
                'far_end_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('far-end-link-in-hw', REFERENCE_CLASS, 'FarEndLinkInHw' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw', 
                [], [], 
                '''                far end link in hw
                ''',
                'far_end_link_in_hw',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History', 
                [], [], 
                '''                history
                ''',
                'history',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                speed
                ''',
                'speed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('stage', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                stage
                ''',
                'stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-link-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is link valid
                ''',
                'is_link_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-conf-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is conf pending
                ''',
                'is_conf_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                oper state
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                error state
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('flags', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                flags
                ''',
                'flags',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('flap-cnt', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                flap cnt
                ''',
                'flap_cnt',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-admin-shuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num admin shuts
                ''',
                'num_admin_shuts',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink',
            False, 
            [
            _MetaInfoClassMember('start-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 35)], [], 
                '''                Start number
                ''',
                'start_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('end-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 35)], [], 
                '''                End number
                ''',
                'end_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('status-option', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                RX link status option
                ''',
                'status_option',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-link', REFERENCE_LIST, 'RxLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink', 
                [], [], 
                '''                Single link information
                ''',
                'rx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks',
            False, 
            [
            _MetaInfoClassMember('rx-link', REFERENCE_LIST, 'RxLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink', 
                [], [], 
                '''                Link number for rx link information
                ''',
                'rx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-links',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance',
            False, 
            [
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 16)], [], 
                '''                Receive instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('rx-links', REFERENCE_CLASS, 'RxLinks' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks', 
                [], [], 
                '''                Link table class for rx information
                ''',
                'rx_links',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances',
            False, 
            [
            _MetaInfoClassMember('rx-asic-instance', REFERENCE_LIST, 'RxAsicInstance' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance', 
                [], [], 
                '''                Instance number for rx link information
                ''',
                'rx_asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption',
            False, 
            [
            _MetaInfoClassMember('option', ATTRIBUTE, 'str' , None, None, 
                [], ['(flap)|(topo)'], 
                '''                Link option
                ''',
                'option',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('rx-asic-instances', REFERENCE_CLASS, 'RxAsicInstances' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances', 
                [], [], 
                '''                Instance table for rx information
                ''',
                'rx_asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-option',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation.LinkOptions' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation.LinkOptions',
            False, 
            [
            _MetaInfoClassMember('link-option', REFERENCE_LIST, 'LinkOption' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption', 
                [], [], 
                '''                Option : topo , flag , stats
                ''',
                'link_option',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-options',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RxLinkInformation' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RxLinkInformation',
            False, 
            [
            _MetaInfoClassMember('link-options', REFERENCE_CLASS, 'LinkOptions' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation.LinkOptions', 
                [], [], 
                '''                Option table for link rx information
                ''',
                'link_options',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'rx-link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId',
            False, 
            [
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.DeviceInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.DeviceInfo',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fapid', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                fapid
                ''',
                'fapid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('hotplug-event', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                hotplug event
                ''',
                'hotplug_event',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slice-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slice state
                ''',
                'slice_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                oper state
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic state
                ''',
                'asic_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-init-cause', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                last init cause
                ''',
                'last_init_cause',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pon-resets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num pon resets
                ''',
                'num_pon_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-hard-resets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num hard resets
                ''',
                'num_hard_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-pon-reset-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                last pon reset timestamp
                ''',
                'last_pon_reset_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-hard-reset-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                last hard reset timestamp
                ''',
                'last_hard_reset_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('local-switch-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                local switch state
                ''',
                'local_switch_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'device-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo',
            False, 
            [
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cur-card-state', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                cur card state
                ''',
                'cur_card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fia-oir-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                count
                ''',
                'count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fia-oir-info', REFERENCE_LIST, 'FiaOirInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo', 
                [], [], 
                '''                fia oir info
                ''',
                'fia_oir_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=10),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'oir-circular-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation.CardInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation.CardInfo',
            False, 
            [
            _MetaInfoClassMember('oir-circular-buffer', REFERENCE_CLASS, 'OirCircularBuffer' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer', 
                [], [], 
                '''                oir circular buffer
                ''',
                'oir_circular_buffer',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                card name
                ''',
                'card_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                card state
                ''',
                'card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                exp num asics
                ''',
                'exp_num_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics-per-fsdb', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                exp num asics per fsdb
                ''',
                'exp_num_asics_per_fsdb',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-powered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is powered
                ''',
                'is_powered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cxp-avail-bitmap', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                cxp avail bitmap
                ''',
                'cxp_avail_bitmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-ilkns-per-asic', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num ilkns per asic
                ''',
                'num_ilkns_per_asic',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-local-ports-per-ilkn', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num local ports per ilkn
                ''',
                'num_local_ports_per_ilkn',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cos-per-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num cos per port
                ''',
                'num_cos_per_port',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'card-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DriverInformation' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DriverInformation',
            False, 
            [
            _MetaInfoClassMember('drv-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                drv version
                ''',
                'drv_version',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff-major-rev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                coeff major rev
                ''',
                'coeff_major_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff-minor-rev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                coeff minor rev
                ''',
                'coeff_minor_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('functional-role', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                functional role
                ''',
                'functional_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-role', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                issu role
                ''',
                'issu_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                rack name
                ''',
                'rack_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-driver-ready', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is driver ready
                ''',
                'is_driver_ready',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                card avail mask
                ''',
                'card_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                asic avail mask
                ''',
                'asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                exp asic avail mask
                ''',
                'exp_asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ucmc-ratio', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ucmc ratio
                ''',
                'ucmc_ratio',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-oper-notify-to-fsdb-pending-bmap', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                asic oper notify to fsdb pending bmap
                ''',
                'asic_oper_notify_to_fsdb_pending_bmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-full-fgid-download-req', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is full fgid download req
                ''',
                'is_full_fgid_download_req',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download in progress
                ''',
                'is_fgid_download_in_progress',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-completed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download completed
                ''',
                'is_fgid_download_completed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb conn active
                ''',
                'fsdb_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid conn active
                ''',
                'fgid_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr conn active
                ''',
                'issu_mgr_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb reg active
                ''',
                'fsdb_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid reg active
                ''',
                'fgid_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr reg active
                ''',
                'issu_mgr_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num pm conn reqs
                ''',
                'num_pm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fsdb-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num fsdb conn reqs
                ''',
                'num_fsdb_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fgid-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num fgid conn reqs
                ''',
                'num_fgid_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fstats-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num fstats conn reqs
                ''',
                'num_fstats_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num cm conn reqs
                ''',
                'num_cm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-issu-mgr-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num issu mgr conn reqs
                ''',
                'num_issu_mgr_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-peer-fia-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num peer fia conn reqs
                ''',
                'num_peer_fia_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-gaspp-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is gaspp registered
                ''',
                'is_gaspp_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-cih-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is cih registered
                ''',
                'is_cih_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('offset-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                offset time nsec
                ''',
                'offset_time_nsec',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('drvr-startup-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                drvr startup timestamp
                ''',
                'drvr_startup_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-intf-ports', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num intf ports
                ''',
                'num_intf_ports',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('uc-weight', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                uc weight
                ''',
                'uc_weight',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('respawn-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                respawn count
                ''',
                'respawn_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('total-asics', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                total asics
                ''',
                'total_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-ready-ntfy-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu ready ntfy pending
                ''',
                'issu_ready_ntfy_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-sent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort sent
                ''',
                'issu_abort_sent',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-rcvd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort rcvd
                ''',
                'issu_abort_rcvd',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fc-mode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                fc mode
                ''',
                'fc_mode',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('board-rev-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                board rev id
                ''',
                'board_rev_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('device-info', REFERENCE_LIST, 'DeviceInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.DeviceInfo', 
                [], [], 
                '''                device info
                ''',
                'device_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=40),
            _MetaInfoClassMember('card-info', REFERENCE_LIST, 'CardInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation.CardInfo', 
                [], [], 
                '''                card info
                ''',
                'card_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=16),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'driver-information',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance',
            False, 
            [
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 16)], [], 
                '''                Asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Clear value
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.ClearStatistics.AsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.ClearStatistics.AsicInstances',
            False, 
            [
            _MetaInfoClassMember('asic-instance', REFERENCE_LIST, 'AsicInstance' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance', 
                [], [], 
                '''                Asic instance to be cleared
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.ClearStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.ClearStatistics',
            False, 
            [
            _MetaInfoClassMember('asic-instances', REFERENCE_CLASS, 'AsicInstances' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.ClearStatistics.AsicInstances', 
                [], [], 
                '''                Instance table for clear statistics
                information
                ''',
                'asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'clear-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'this-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId',
            False, 
            [
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link type
                ''',
                'link_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-stage', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                link stage
                ''',
                'link_stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link num
                ''',
                'link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('phy-link-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                phy link num
                ''',
                'phy_link_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'far-end-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats',
            False, 
            [
            _MetaInfoClassMember('dummy', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                dummy
                ''',
                'dummy',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                oper state
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', ATTRIBUTE, 'int' , None, None, 
                [(-128, 127)], [], 
                '''                error state
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                timestamp
                ''',
                'timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reasons', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                reasons
                ''',
                'reasons',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'hist',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History',
            False, 
            [
            _MetaInfoClassMember('histnum', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                histnum
                ''',
                'histnum',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start-index', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                start index
                ''',
                'start_index',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('hist', REFERENCE_LIST, 'Hist' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist', 
                [], [], 
                '''                hist
                ''',
                'hist',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=5),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'history',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink',
            False, 
            [
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Single Link
                ''',
                'link',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('this-link', REFERENCE_CLASS, 'ThisLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink', 
                [], [], 
                '''                this link
                ''',
                'this_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('far-end-link', REFERENCE_CLASS, 'FarEndLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink', 
                [], [], 
                '''                far end link
                ''',
                'far_end_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats', 
                [], [], 
                '''                stats
                ''',
                'stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('history', REFERENCE_CLASS, 'History' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History', 
                [], [], 
                '''                history
                ''',
                'history',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                speed
                ''',
                'speed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('stage', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                stage
                ''',
                'stage',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-link-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is link valid
                ''',
                'is_link_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-conf-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is conf pending
                ''',
                'is_conf_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-power-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is power enabled
                ''',
                'is_power_enabled',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff1', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                coeff1
                ''',
                'coeff1',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff2', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                coeff2
                ''',
                'coeff2',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                oper state
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                error state
                ''',
                'error_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-admin-shuts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num admin shuts
                ''',
                'num_admin_shuts',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink',
            False, 
            [
            _MetaInfoClassMember('start-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 35)], [], 
                '''                Start number
                ''',
                'start_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('end-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 35)], [], 
                '''                End number
                ''',
                'end_number',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-link', REFERENCE_LIST, 'TxLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink', 
                [], [], 
                '''                Single link information
                ''',
                'tx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks',
            False, 
            [
            _MetaInfoClassMember('tx-link', REFERENCE_LIST, 'TxLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink', 
                [], [], 
                '''                Link number for tx link information
                ''',
                'tx_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-links',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance',
            False, 
            [
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 16)], [], 
                '''                Transmit instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('tx-links', REFERENCE_CLASS, 'TxLinks' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks', 
                [], [], 
                '''                Link table for tx information
                ''',
                'tx_links',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances',
            False, 
            [
            _MetaInfoClassMember('tx-asic-instance', REFERENCE_LIST, 'TxAsicInstance' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance', 
                [], [], 
                '''                Instance number for tx link information
                ''',
                'tx_asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption',
            False, 
            [
            _MetaInfoClassMember('tx-asic-instances', REFERENCE_CLASS, 'TxAsicInstances' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances', 
                [], [], 
                '''                Instance table for tx information
                ''',
                'tx_asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-status-option',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable',
            False, 
            [
            _MetaInfoClassMember('tx-status-option', REFERENCE_CLASS, 'TxStatusOption' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption', 
                [], [], 
                '''                Option: data, ctrl, all- for now none
                ''',
                'tx_status_option',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-status-option-table',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.TxLinkInformation' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.TxLinkInformation',
            False, 
            [
            _MetaInfoClassMember('tx-status-option-table', REFERENCE_CLASS, 'TxStatusOptionTable' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable', 
                [], [], 
                '''                Link table for tx information
                ''',
                'tx_status_option_table',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'tx-link-information',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Unit number
                ''',
                'unit',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('output', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                output
                ''',
                'output',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'register-dump-unit',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RegisterDump.RegisterDumpUnits',
            False, 
            [
            _MetaInfoClassMember('register-dump-unit', REFERENCE_LIST, 'RegisterDumpUnit' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit', 
                [], [], 
                '''                Unit number for register dump
                ''',
                'register_dump_unit',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'register-dump-units',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.RegisterDump' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.RegisterDump',
            False, 
            [
            _MetaInfoClassMember('register-dump-units', REFERENCE_CLASS, 'RegisterDumpUnits' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RegisterDump.RegisterDumpUnits', 
                [], [], 
                '''                Unit table for register dump
                ''',
                'register_dump_units',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'register-dump',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output',
            False, 
            [
            _MetaInfoClassMember('output', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                First line
                ''',
                'output',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('output-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                output xr
                ''',
                'output_xr',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'output',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command',
            False, 
            [
            _MetaInfoClassMember('cmd', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Shell command
                ''',
                'cmd',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('output', REFERENCE_LIST, 'Output' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output', 
                [], [], 
                '''                Added to support datalist
                ''',
                'output',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'command',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands',
            False, 
            [
            _MetaInfoClassMember('command', REFERENCE_LIST, 'Command' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command', 
                [], [], 
                '''                Command for diag shell statistics
                ''',
                'command',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'commands',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit',
            False, 
            [
            _MetaInfoClassMember('unit', ATTRIBUTE, 'int' , None, None, 
                [(0, 15)], [], 
                '''                Unit number
                ''',
                'unit',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('commands', REFERENCE_CLASS, 'Commands' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands', 
                [], [], 
                '''                Command table for diag shell
                ''',
                'commands',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'diag-shell-unit',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell.DiagShellUnits' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell.DiagShellUnits',
            False, 
            [
            _MetaInfoClassMember('diag-shell-unit', REFERENCE_LIST, 'DiagShellUnit' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit', 
                [], [], 
                '''                Unit number for diag shell statistics
                ''',
                'diag_shell_unit',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'diag-shell-units',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.DiagShell' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.DiagShell',
            False, 
            [
            _MetaInfoClassMember('diag-shell-units', REFERENCE_CLASS, 'DiagShellUnits' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell.DiagShellUnits', 
                [], [], 
                '''                Unit table for diag shell
                ''',
                'diag_shell_units',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'diag-shell',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId',
            False, 
            [
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-type', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic type
                ''',
                'asic_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-id',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo',
            False, 
            [
            _MetaInfoClassMember('asic-id', REFERENCE_CLASS, 'AsicId' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId', 
                [], [], 
                '''                asic id
                ''',
                'asic_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is valid
                ''',
                'is_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fapid', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                fapid
                ''',
                'fapid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('hotplug-event', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                hotplug event
                ''',
                'hotplug_event',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slice-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slice state
                ''',
                'slice_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oper-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                oper state
                ''',
                'oper_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                asic state
                ''',
                'asic_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-init-cause', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                last init cause
                ''',
                'last_init_cause',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pon-resets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num pon resets
                ''',
                'num_pon_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-hard-resets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num hard resets
                ''',
                'num_hard_resets',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-pon-reset-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                last pon reset timestamp
                ''',
                'last_pon_reset_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('last-hard-reset-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                last hard reset timestamp
                ''',
                'last_hard_reset_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('local-switch-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                local switch state
                ''',
                'local_switch_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'device-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo',
            False, 
            [
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cur-card-state', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                cur card state
                ''',
                'cur_card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fia-oir-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                count
                ''',
                'count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('end', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fia-oir-info', REFERENCE_LIST, 'FiaOirInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo', 
                [], [], 
                '''                fia oir info
                ''',
                'fia_oir_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=10),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'oir-circular-buffer',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo',
            False, 
            [
            _MetaInfoClassMember('oir-circular-buffer', REFERENCE_CLASS, 'OirCircularBuffer' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer', 
                [], [], 
                '''                oir circular buffer
                ''',
                'oir_circular_buffer',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-type', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card type
                ''',
                'card_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                card name
                ''',
                'card_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                card flag
                ''',
                'card_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('evt-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                evt flag
                ''',
                'evt_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('reg-flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                reg flag
                ''',
                'reg_flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-state', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                card state
                ''',
                'card_state',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                exp num asics
                ''',
                'exp_num_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-num-asics-per-fsdb', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                exp num asics per fsdb
                ''',
                'exp_num_asics_per_fsdb',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-powered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is powered
                ''',
                'is_powered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('cxp-avail-bitmap', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                cxp avail bitmap
                ''',
                'cxp_avail_bitmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-ilkns-per-asic', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num ilkns per asic
                ''',
                'num_ilkns_per_asic',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-local-ports-per-ilkn', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num local ports per ilkn
                ''',
                'num_local_ports_per_ilkn',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cos-per-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num cos per port
                ''',
                'num_cos_per_port',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'card-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot',
            False, 
            [
            _MetaInfoClassMember('slot', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Slot number
                ''',
                'slot',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('drv-version', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                drv version
                ''',
                'drv_version',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff-major-rev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                coeff major rev
                ''',
                'coeff_major_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('coeff-minor-rev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                coeff minor rev
                ''',
                'coeff_minor_rev',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('functional-role', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                functional role
                ''',
                'functional_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-role', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                issu role
                ''',
                'issu_role',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                rack name
                ''',
                'rack_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-type', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                rack type
                ''',
                'rack_type',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-driver-ready', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is driver ready
                ''',
                'is_driver_ready',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('card-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                card avail mask
                ''',
                'card_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                asic avail mask
                ''',
                'asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('exp-asic-avail-mask', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                exp asic avail mask
                ''',
                'exp_asic_avail_mask',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ucmc-ratio', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ucmc ratio
                ''',
                'ucmc_ratio',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-oper-notify-to-fsdb-pending-bmap', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                asic oper notify to fsdb pending bmap
                ''',
                'asic_oper_notify_to_fsdb_pending_bmap',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-full-fgid-download-req', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is full fgid download req
                ''',
                'is_full_fgid_download_req',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-in-progress', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download in progress
                ''',
                'is_fgid_download_in_progress',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-fgid-download-completed', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is fgid download completed
                ''',
                'is_fgid_download_completed',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb conn active
                ''',
                'fsdb_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid conn active
                ''',
                'fgid_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-conn-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr conn active
                ''',
                'issu_mgr_conn_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fsdb-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fsdb reg active
                ''',
                'fsdb_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fgid-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                fgid reg active
                ''',
                'fgid_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-mgr-reg-active', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu mgr reg active
                ''',
                'issu_mgr_reg_active',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-pm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num pm conn reqs
                ''',
                'num_pm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fsdb-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num fsdb conn reqs
                ''',
                'num_fsdb_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fgid-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num fgid conn reqs
                ''',
                'num_fgid_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fstats-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num fstats conn reqs
                ''',
                'num_fstats_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-cm-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num cm conn reqs
                ''',
                'num_cm_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-issu-mgr-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num issu mgr conn reqs
                ''',
                'num_issu_mgr_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-peer-fia-conn-reqs', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                num peer fia conn reqs
                ''',
                'num_peer_fia_conn_reqs',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-gaspp-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is gaspp registered
                ''',
                'is_gaspp_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-cih-registered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is cih registered
                ''',
                'is_cih_registered',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('offset-time-nsec', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                offset time nsec
                ''',
                'offset_time_nsec',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('drvr-startup-timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                drvr startup timestamp
                ''',
                'drvr_startup_timestamp',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-intf-ports', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                num intf ports
                ''',
                'num_intf_ports',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('uc-weight', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                uc weight
                ''',
                'uc_weight',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('respawn-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                respawn count
                ''',
                'respawn_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('total-asics', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                total asics
                ''',
                'total_asics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-ready-ntfy-pending', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu ready ntfy pending
                ''',
                'issu_ready_ntfy_pending',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-sent', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort sent
                ''',
                'issu_abort_sent',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('issu-abort-rcvd', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                issu abort rcvd
                ''',
                'issu_abort_rcvd',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fc-mode', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                fc mode
                ''',
                'fc_mode',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('board-rev-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                board rev id
                ''',
                'board_rev_id',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('device-info', REFERENCE_LIST, 'DeviceInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo', 
                [], [], 
                '''                device info
                ''',
                'device_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=40),
            _MetaInfoClassMember('card-info', REFERENCE_LIST, 'CardInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo', 
                [], [], 
                '''                card info
                ''',
                'card_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=16),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'slot',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag.Slots',
            False, 
            [
            _MetaInfoClassMember('slot', REFERENCE_LIST, 'Slot' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot', 
                [], [], 
                '''                Slot number for getting history
                ''',
                'slot',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'slots',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags.Flag' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags.Flag',
            False, 
            [
            _MetaInfoClassMember('flag', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Flag value
                ''',
                'flag',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('slots', REFERENCE_CLASS, 'Slots' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag.Slots', 
                [], [], 
                '''                Slot table for history
                ''',
                'slots',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'flag',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory.Flags' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory.Flags',
            False, 
            [
            _MetaInfoClassMember('flag', REFERENCE_LIST, 'Flag' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags.Flag', 
                [], [], 
                '''                Flag value for physical location
                ''',
                'flag',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'flags',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.OirHistory' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.OirHistory',
            False, 
            [
            _MetaInfoClassMember('flags', REFERENCE_CLASS, 'Flags' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory.Flags', 
                [], [], 
                '''                Flag table for history
                ''',
                'flags',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'oir-history',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo',
            False, 
            [
            _MetaInfoClassMember('field-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 51)], [], 
                '''                Field Name
                ''',
                'field_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('field-value', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Field Value
                ''',
                'field_value',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('is-ovf', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is Ovf
                ''',
                'is_ovf',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'field-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo',
            False, 
            [
            _MetaInfoClassMember('block-name', ATTRIBUTE, 'str' , None, None, 
                [(0, 11)], [], 
                '''                Block Name
                ''',
                'block_name',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('num-fields', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Num Fields
                ''',
                'num_fields',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('field-info', REFERENCE_LIST, 'FieldInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo', 
                [], [], 
                '''                field info
                ''',
                'field_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=200),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'block-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo',
            False, 
            [
            _MetaInfoClassMember('num-blocks', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Num Blocks
                ''',
                'num_blocks',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('block-info', REFERENCE_LIST, 'BlockInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo', 
                [], [], 
                '''                block info
                ''',
                'block_info',
                'Cisco-IOS-XR-dnx-driver-oper', False, max_elements=15),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'stats-info',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats',
            False, 
            [
            _MetaInfoClassMember('stats-info', REFERENCE_CLASS, 'StatsInfo' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo', 
                [], [], 
                '''                stats info
                ''',
                'stats_info',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                valid
                ''',
                'valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-no', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack no
                ''',
                'rack_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('chip-ver', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                chip ver
                ''',
                'chip_ver',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'pbc-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics',
            False, 
            [
            _MetaInfoClassMember('pbc-stats', REFERENCE_CLASS, 'PbcStats' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats', 
                [], [], 
                '''                PBC stats bag
                ''',
                'pbc_stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'pbc-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus',
            False, 
            [
            _MetaInfoClassMember('link-crc-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link crc error
                ''',
                'link_crc_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-size-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link size error
                ''',
                'link_size_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-mis-align-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link mis align error
                ''',
                'link_mis_align_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-code-group-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link code group error
                ''',
                'link_code_group_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-lock-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link no sig lock error
                ''',
                'link_no_sig_lock_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-accept-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link no sig accept error
                ''',
                'link_no_sig_accept_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-tokens-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link tokens error
                ''',
                'link_tokens_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-token-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                error token count
                ''',
                'error_token_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-error-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters',
            False, 
            [
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus',
            False, 
            [
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'ovf-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats',
            False, 
            [
            _MetaInfoClassMember('link-error-status', REFERENCE_CLASS, 'LinkErrorStatus' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus', 
                [], [], 
                '''                link error status
                ''',
                'link_error_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-counters', REFERENCE_CLASS, 'LinkCounters' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters', 
                [], [], 
                '''                link counters
                ''',
                'link_counters',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ovf-status', REFERENCE_CLASS, 'OvfStatus' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus', 
                [], [], 
                '''                ovf status
                ''',
                'ovf_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'aggr-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus',
            False, 
            [
            _MetaInfoClassMember('link-crc-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link crc error
                ''',
                'link_crc_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-size-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link size error
                ''',
                'link_size_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-mis-align-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link mis align error
                ''',
                'link_mis_align_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-code-group-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link code group error
                ''',
                'link_code_group_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-lock-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link no sig lock error
                ''',
                'link_no_sig_lock_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no-sig-accept-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link no sig accept error
                ''',
                'link_no_sig_accept_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-tokens-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link tokens error
                ''',
                'link_tokens_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('error-token-count', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                error token count
                ''',
                'error_token_count',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-error-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters',
            False, 
            [
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'link-counters',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus',
            False, 
            [
            _MetaInfoClassMember('tx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Control cells counter
                ''',
                'tx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data cell counter
                ''',
                'tx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Data byte counter
                ''',
                'tx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-crc-errors-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX CRC errors counter
                ''',
                'rx_crc_errors_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-correctable-error', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC correctable error
                ''',
                'rx_lfec_fec_correctable_error',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-disparity-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b disparity errors
                ''',
                'rx_8b_10b_disparity_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-control-cells-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Control cells counter
                ''',
                'rx_control_cells_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-cell-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data cell counter
                ''',
                'rx_data_cell_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-data-byte-counter', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Data byte counter
                ''',
                'rx_data_byte_counter',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-dropped-retransmitted-control', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX dropped retransmitted control
                ''',
                'rx_dropped_retransmitted_control',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                TX Asyn fifo rate
                ''',
                'tx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-asyn-fifo-rate', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX Asyn fifo rate
                ''',
                'rx_asyn_fifo_rate',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-lfec-fec-uncorrectable-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX LFEC FEC uncorrectable errors
                ''',
                'rx_lfec_fec_uncorrectable_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rx-8b-10b-code-errors', ATTRIBUTE, 'str' , None, None, 
                [(0, 6)], [], 
                '''                RX 8b 10b code errors
                ''',
                'rx_8b_10b_code_errors',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'ovf-status',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats',
            False, 
            [
            _MetaInfoClassMember('link-error-status', REFERENCE_CLASS, 'LinkErrorStatus' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus', 
                [], [], 
                '''                link error status
                ''',
                'link_error_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-counters', REFERENCE_CLASS, 'LinkCounters' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters', 
                [], [], 
                '''                link counters
                ''',
                'link_counters',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('ovf-status', REFERENCE_CLASS, 'OvfStatus' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus', 
                [], [], 
                '''                ovf status
                ''',
                'ovf_status',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'incr-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic',
            False, 
            [
            _MetaInfoClassMember('asic', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Single asic
                ''',
                'asic',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('aggr-stats', REFERENCE_CLASS, 'AggrStats' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats', 
                [], [], 
                '''                aggr stats
                ''',
                'aggr_stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('incr-stats', REFERENCE_CLASS, 'IncrStats' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats', 
                [], [], 
                '''                incr stats
                ''',
                'incr_stats',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                valid
                ''',
                'valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('rack-no', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                rack no
                ''',
                'rack_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('slot-no', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                slot no
                ''',
                'slot_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                asic instance
                ''',
                'asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-no', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                link no
                ''',
                'link_no',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('link-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                link valid
                ''',
                'link_valid',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-asic',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink',
            False, 
            [
            _MetaInfoClassMember('link', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Link number
                ''',
                'link',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('fmac-asic', REFERENCE_LIST, 'FmacAsic' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic', 
                [], [], 
                '''                Single aisc information
                ''',
                'fmac_asic',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-link',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks',
            False, 
            [
            _MetaInfoClassMember('fmac-link', REFERENCE_LIST, 'FmacLink' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink', 
                [], [], 
                '''                Link number for statistics
                ''',
                'fmac_link',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-links',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics',
            False, 
            [
            _MetaInfoClassMember('fmac-links', REFERENCE_CLASS, 'FmacLinks' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks', 
                [], [], 
                '''                Link table for statistics
                ''',
                'fmac_links',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fmac-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance',
            False, 
            [
            _MetaInfoClassMember('instance', ATTRIBUTE, 'int' , None, None, 
                [(0, 16)], [], 
                '''                Asic instance
                ''',
                'instance',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('pbc-statistics', REFERENCE_CLASS, 'PbcStatistics' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics', 
                [], [], 
                '''                Packet Byte Counter for a Asic
                ''',
                'pbc_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('fmac-statistics', REFERENCE_CLASS, 'FmacStatistics' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics', 
                [], [], 
                '''                Statistics of FMAC
                ''',
                'fmac_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'statistics-asic-instance',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances',
            False, 
            [
            _MetaInfoClassMember('statistics-asic-instance', REFERENCE_LIST, 'StatisticsAsicInstance' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance', 
                [], [], 
                '''                Asic instance for statistics
                ''',
                'statistics_asic_instance',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'statistics-asic-instances',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node.AsicStatistics' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node.AsicStatistics',
            False, 
            [
            _MetaInfoClassMember('statistics-asic-instances', REFERENCE_CLASS, 'StatisticsAsicInstances' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances', 
                [], [], 
                '''                Instance table for statistics
                ''',
                'statistics_asic_instances',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'asic-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-dnx-driver-oper', True),
            _MetaInfoClassMember('rx-link-information', REFERENCE_CLASS, 'RxLinkInformation' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RxLinkInformation', 
                [], [], 
                '''                FIA link rx information
                ''',
                'rx_link_information',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('driver-information', REFERENCE_CLASS, 'DriverInformation' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DriverInformation', 
                [], [], 
                '''                FIA driver information
                ''',
                'driver_information',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('clear-statistics', REFERENCE_CLASS, 'ClearStatistics' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.ClearStatistics', 
                [], [], 
                '''                Clear statistics information
                ''',
                'clear_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('tx-link-information', REFERENCE_CLASS, 'TxLinkInformation' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.TxLinkInformation', 
                [], [], 
                '''                FIA link TX information
                ''',
                'tx_link_information',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('register-dump', REFERENCE_CLASS, 'RegisterDump' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.RegisterDump', 
                [], [], 
                '''                FIA register dump information
                ''',
                'register_dump',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('diag-shell', REFERENCE_CLASS, 'DiagShell' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.DiagShell', 
                [], [], 
                '''                FIA diag shell information
                ''',
                'diag_shell',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('oir-history', REFERENCE_CLASS, 'OirHistory' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.OirHistory', 
                [], [], 
                '''                FIA operational data of oir history
                ''',
                'oir_history',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            _MetaInfoClassMember('asic-statistics', REFERENCE_CLASS, 'AsicStatistics' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node.AsicStatistics', 
                [], [], 
                '''                FIA asic statistics information
                ''',
                'asic_statistics',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia.Nodes' : {
        'meta_info' : _MetaInfoClass('Fia.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes.Node', 
                [], [], 
                '''                FIA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
    'Fia' : {
        'meta_info' : _MetaInfoClass('Fia',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper', 'Fia.Nodes', 
                [], [], 
                '''                FIA driver operational data for available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-dnx-driver-oper', False),
            ],
            'Cisco-IOS-XR-dnx-driver-oper',
            'fia',
            _yang_ns._namespaces['Cisco-IOS-XR-dnx-driver-oper'],
        'ydk.models.dnx.Cisco_IOS_XR_dnx_driver_oper'
        ),
    },
}
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History.Hist']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.ThisLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.FarEndLinkInHw']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink.History']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink.RxLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks.RxLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance.RxLinks']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances.RxAsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption.RxAsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions.LinkOption']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation.LinkOptions']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RxLinkInformation']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer.FiaOirInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo.OirCircularBuffer']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.DeviceInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation.CardInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DriverInformation']['meta_info']
_meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances.AsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.ClearStatistics.AsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.ClearStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History.Hist']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.ThisLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.FarEndLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.Stats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink.History']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink.TxLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks.TxLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance.TxLinks']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances.TxAsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption.TxAsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable.TxStatusOption']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation.TxStatusOptionTable']['meta_info'].parent =_meta_table['Fia.Nodes.Node.TxLinkInformation']['meta_info']
_meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits.RegisterDumpUnit']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits']['meta_info']
_meta_table['Fia.Nodes.Node.RegisterDump.RegisterDumpUnits']['meta_info'].parent =_meta_table['Fia.Nodes.Node.RegisterDump']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command.Output']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands.Command']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit.Commands']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits.DiagShellUnit']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell.DiagShellUnits']['meta_info'].parent =_meta_table['Fia.Nodes.Node.DiagShell']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo.AsicId']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer.FiaOirInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo.OirCircularBuffer']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.DeviceInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot.CardInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots.Slot']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag.Slots']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags.Flag']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory.Flags']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory.Flags']['meta_info'].parent =_meta_table['Fia.Nodes.Node.OirHistory']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo.FieldInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo.BlockInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats.StatsInfo']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics.PbcStats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkErrorStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.LinkCounters']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats.OvfStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkErrorStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.LinkCounters']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats.OvfStatus']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.AggrStats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic.IncrStats']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink.FmacAsic']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks.FmacLink']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics.FmacLinks']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.PbcStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance.FmacStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances.StatisticsAsicInstance']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics.StatisticsAsicInstances']['meta_info'].parent =_meta_table['Fia.Nodes.Node.AsicStatistics']['meta_info']
_meta_table['Fia.Nodes.Node.RxLinkInformation']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.DriverInformation']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.ClearStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.TxLinkInformation']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.RegisterDump']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.DiagShell']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.OirHistory']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node.AsicStatistics']['meta_info'].parent =_meta_table['Fia.Nodes.Node']['meta_info']
_meta_table['Fia.Nodes.Node']['meta_info'].parent =_meta_table['Fia.Nodes']['meta_info']
_meta_table['Fia.Nodes']['meta_info'].parent =_meta_table['Fia']['meta_info']
