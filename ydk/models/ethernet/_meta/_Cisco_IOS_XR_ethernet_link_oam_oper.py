


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'LogEnum' : _MetaInfoEnum('LogEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper',
        {
            'log-type-symbol-event':'LOG_TYPE_SYMBOL_EVENT',
            'log-type-period-event':'LOG_TYPE_PERIOD_EVENT',
            'log-type-frame-event':'LOG_TYPE_FRAME_EVENT',
            'log-type-secs-event':'LOG_TYPE_SECS_EVENT',
            'log-type-link-fault':'LOG_TYPE_LINK_FAULT',
            'log-type-dying-gasp':'LOG_TYPE_DYING_GASP',
            'log-type-critical-event':'LOG_TYPE_CRITICAL_EVENT',
        }, 'Cisco-IOS-XR-ethernet-link-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper']),
    'LogLocationEnum' : _MetaInfoEnum('LogLocationEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper',
        {
            'log-location-local':'LOG_LOCATION_LOCAL',
            'log-location-remote':'LOG_LOCATION_REMOTE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper']),
    'LoopbackStatusEnum' : _MetaInfoEnum('LoopbackStatusEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper',
        {
            'none':'NONE',
            'initiating':'INITIATING',
            'master-loopback':'MASTER_LOOPBACK',
            'terminating':'TERMINATING',
            'local-loopback':'LOCAL_LOOPBACK',
            'unknown':'UNKNOWN',
        }, 'Cisco-IOS-XR-ethernet-link-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper']),
    'OperationalStateEnum' : _MetaInfoEnum('OperationalStateEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper',
        {
            'disabled':'DISABLED',
            'link-fault':'LINK_FAULT',
            'passive-wait':'PASSIVE_WAIT',
            'active-send-local':'ACTIVE_SEND_LOCAL',
            'send-local-and-remote':'SEND_LOCAL_AND_REMOTE',
            'send-local-and-remote-ok':'SEND_LOCAL_AND_REMOTE_OK',
            'peering-locally-rejected':'PEERING_LOCALLY_REJECTED',
            'peering-remotely-rejected':'PEERING_REMOTELY_REJECTED',
            'operational':'OPERATIONAL',
            'operational-half-duplex':'OPERATIONAL_HALF_DUPLEX',
        }, 'Cisco-IOS-XR-ethernet-link-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper']),
    'ModeEnum' : _MetaInfoEnum('ModeEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper',
        {
            'passive':'PASSIVE',
            'active':'ACTIVE',
            'dont-care':'DONT_CARE',
        }, 'Cisco-IOS-XR-ethernet-link-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper']),
    'ActionEnum' : _MetaInfoEnum('ActionEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper',
        {
            'no-action':'NO_ACTION',
            'disable-interface':'DISABLE_INTERFACE',
            'log':'LOG',
            'efd':'EFD',
        }, 'Cisco-IOS-XR-ethernet-link-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper']),
    'ProtocolStateEnum' : _MetaInfoEnum('ProtocolStateEnum', 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper',
        {
            'protocol-state-inactive':'PROTOCOL_STATE_INACTIVE',
            'protocol-state-fault':'PROTOCOL_STATE_FAULT',
            'protocol-state-active-send-local':'PROTOCOL_STATE_ACTIVE_SEND_LOCAL',
            'protocol-state-passive-wait':'PROTOCOL_STATE_PASSIVE_WAIT',
            'protocol-state-send-local-remote':'PROTOCOL_STATE_SEND_LOCAL_REMOTE',
            'protocol-state-send-local-remote-ok':'PROTOCOL_STATE_SEND_LOCAL_REMOTE_OK',
            'protocol-state-send-any':'PROTOCOL_STATE_SEND_ANY',
        }, 'Cisco-IOS-XR-ethernet-link-oam-oper', _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper']),
    'EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface',
            False, 
            [
            _MetaInfoClassMember('member-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Member Interface
                ''',
                'member_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', True),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'name',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('operational-status', REFERENCE_ENUM_CLASS, 'OperationalStateEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'OperationalStateEnum', 
                [], [], 
                '''                Operational status
                ''',
                'operational_status',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('loopback-mode', REFERENCE_ENUM_CLASS, 'LoopbackStatusEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'LoopbackStatusEnum', 
                [], [], 
                '''                The loopback mode the interface is in
                ''',
                'loopback_mode',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-mode', REFERENCE_ENUM_CLASS, 'ModeEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ModeEnum', 
                [], [], 
                '''                Local Mode (passive/active)
                ''',
                'local_mode',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('miswired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has the interface mis-wired?
                ''',
                'miswired',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-mwd-key', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Local Mis-wiring Detection key
                ''',
                'local_mwd_key',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-function-unidirectional', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Local Unidirectional support
                ''',
                'local_function_unidirectional',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-function-loopback', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Local loopback support
                ''',
                'local_function_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-function-event', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Local event support
                ''',
                'local_function_event',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-functionvariable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Local variable retreival support
                ''',
                'local_functionvariable',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-revision', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Local revision
                ''',
                'local_revision',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-mtu', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Local MTU
                ''',
                'local_mtu',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-operational', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the local OAM session operational?
                ''',
                'local_operational',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-evaluating', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is the local OAM session evaluating?
                ''',
                'local_evaluating',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mode', REFERENCE_ENUM_CLASS, 'ModeEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ModeEnum', 
                [], [], 
                '''                Remote Mode (passive/active)
                ''',
                'remote_mode',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-unidirectional', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote unidirectional support
                ''',
                'remote_unidirectional',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-loopback', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote loopback support
                ''',
                'remote_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-event', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote event support
                ''',
                'remote_event',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-variable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Remote variable retreival support
                ''',
                'remote_variable',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mtu', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote MTU
                ''',
                'remote_mtu',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mac-address', ATTRIBUTE, 'str' , None, None, 
                [], ['[0-9a-fA-F]{2}(:[0-9a-fA-F]{2}){5}'], 
                '''                Remote MAC address
                ''',
                'remote_mac_address',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-vendor-oui', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                Remote vendor OUI
                ''',
                'remote_vendor_oui',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-revision', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                Remote revision
                ''',
                'remote_revision',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-vendor-info', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote vendor info
                ''',
                'remote_vendor_info',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mwd-key', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Remote Mis-wiring Detection key
                ''',
                'remote_mwd_key',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('operational-status-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'operational_status_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('loopback-mode-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'loopback_mode_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-mode-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_mode_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('miswired-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'miswired_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-mwd-key-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_mwd_key_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-function-unidirectional-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_function_unidirectional_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-function-loopback-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_function_loopback_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-function-event-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_function_event_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-functionvariable-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_functionvariable_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-revisionvalid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_revisionvalid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-mtu-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'local_mtu_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mode-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_mode_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-unidirectional-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_unidirectional_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-loopback-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_loopback_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-event-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_event_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-variable-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_variable_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mtu-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_mtu_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mac-address-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_mac_address_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-vendor-oui-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_vendor_oui_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-revisionvalid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_revisionvalid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-vendor-info-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_vendor_info_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mwd-key-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has this value been received successfully?
                ''',
                'remote_mwd_key_valid',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'discovery-info-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.DiscoveryInfoInterfaces' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.DiscoveryInfoInterfaces',
            False, 
            [
            _MetaInfoClassMember('discovery-info-interface', REFERENCE_LIST, 'DiscoveryInfoInterface' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface', 
                [], [], 
                '''                Ethernet Link OAM interface to get Discovery
                Info for
                ''',
                'discovery_info_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'discovery-info-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors',
            False, 
            [
            _MetaInfoClassMember('pfi-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reason for the Interface Management error (if
                applicable)
                ''',
                'pfi_reason',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('pfi-error-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Interface Management error/success code
                ''',
                'pfi_error_code',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('platform-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reason for the platform error (if applicable)
                ''',
                'platform_reason',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('platform-error-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The platform error/success code
                ''',
                'platform_error_code',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('spio-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reason for the Packet I/O error (if applicable)
                ''',
                'spio_reason',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('spio-error-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Packet I/O error/success code
                ''',
                'spio_error_code',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('epi-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reason for the Packet error (if applicable)
                ''',
                'epi_reason',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('epi-error-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The Packet error/success code
                ''',
                'epi_error_code',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('caps-add-reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reason for the caps add error (if applicable)
                ''',
                'caps_add_reason',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('caps-add-error-code', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The caps add error/success code
                ''',
                'caps_add_error_code',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'errors',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers',
            False, 
            [
            _MetaInfoClassMember('link-fault-received', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Link-fault messages being received
                ''',
                'link_fault_received',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('discovery-timed-out', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The discovery process has timed out
                ''',
                'discovery_timed_out',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('capabilities-conflict', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A capabilities conflict has been detected
                ''',
                'capabilities_conflict',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('wiring-conflict', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                A wiring conflict has been detected
                ''',
                'wiring_conflict',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('session-down', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The 802.3 OAM session is down
                ''',
                'session_down',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'efd-triggers',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface',
            False, 
            [
            _MetaInfoClassMember('member-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Member Interface
                ''',
                'member_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', True),
            _MetaInfoClassMember('errors', REFERENCE_CLASS, 'Errors' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors', 
                [], [], 
                '''                The errors that have occurred on this interface
                ''',
                'errors',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('efd-triggers', REFERENCE_CLASS, 'EfdTriggers' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers', 
                [], [], 
                '''                Any present EFD triggers
                ''',
                'efd_triggers',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('protocol-code', REFERENCE_ENUM_CLASS, 'ProtocolStateEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ProtocolStateEnum', 
                [], [], 
                '''                The state the protocol is in
                ''',
                'protocol_code',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('rx-fault', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Has a uni-directional link-fault been detected?
                ''',
                'rx_fault',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-mwd-key', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The local MWD key
                ''',
                'local_mwd_key',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mwd-key-present', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Does the remote side have an MWD key?
                ''',
                'remote_mwd_key_present',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-mwd-key', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The remote MWD key
                ''',
                'remote_mwd_key',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'interface-state-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.InterfaceStateInterfaces' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.InterfaceStateInterfaces',
            False, 
            [
            _MetaInfoClassMember('interface-state-interface', REFERENCE_LIST, 'InterfaceStateInterface' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface', 
                [], [], 
                '''                Ethernet Link OAM interface to get Interface
                State for
                ''',
                'interface_state_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'interface-state-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface',
            False, 
            [
            _MetaInfoClassMember('member-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Member Interface
                ''',
                'member_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', True),
            _MetaInfoClassMember('fast-hello-interval-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is 100ms hello interval time enabled?
                ''',
                'fast_hello_interval_enabled',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('link-monitor-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is link monitoring enabled?
                ''',
                'link_monitor_enabled',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-loopback-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is remote loopback enabled?
                ''',
                'remote_loopback_enabled',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('mib-retrieval-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is MIB retrieval enabled?
                ''',
                'mib_retrieval_enabled',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('udlf-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is uni-directional link-fault detection enabled?
                ''',
                'udlf_enabled',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('mode', REFERENCE_ENUM_CLASS, 'ModeEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ModeEnum', 
                [], [], 
                '''                Configured mode
                ''',
                'mode',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('connection-timeout', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                Connection timeout
                ''',
                'connection_timeout',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('symbol-period-window', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Symbol period event window size
                ''',
                'symbol_period_window',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('symbol-period-threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Low symbol period event threshold
                ''',
                'symbol_period_threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('symbol-period-threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                High symbol period event threshold
                ''',
                'symbol_period_threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-window', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame event window size
                ''',
                'frame_window',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame event low threshold
                ''',
                'frame_threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame event high threshold
                ''',
                'frame_threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-period-window', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame period event window size
                ''',
                'frame_period_window',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-period-threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame period event low threshold
                ''',
                'frame_period_threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-period-threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame period event high threshold
                ''',
                'frame_period_threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-seconds-window', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame seconds event high threshold
                ''',
                'frame_seconds_window',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-seconds-threshold-low', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame seconds event high threshold
                ''',
                'frame_seconds_threshold_low',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-seconds-threshold-high', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Frame seconds event high threshold
                ''',
                'frame_seconds_threshold_high',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('high-threshold-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a high threshold is
                breached
                ''',
                'high_threshold_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('link-fault-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a link fault occurs
                ''',
                'link_fault_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('dying-gasp-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a dying gasp occurs
                ''',
                'dying_gasp_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('critical-event-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a critical event occurs
                ''',
                'critical_event_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('discovery-timeout-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a discovery timeout
                occurs
                ''',
                'discovery_timeout_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('capabilities-conflict-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a capabilities conflict
                occurs
                ''',
                'capabilities_conflict_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('wiring-conflict-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a wiring conflict occurs
                ''',
                'wiring_conflict_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('session-up-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a session comes up
                ''',
                'session_up_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('session-down-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a session comes down
                ''',
                'session_down_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-loopback-action', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Action to perform when a session enters or exits
                remote loopback
                ''',
                'remote_loopback_action',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-remote-mode', REFERENCE_ENUM_CLASS, 'ModeEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ModeEnum', 
                [], [], 
                '''                The mode that is required of the remote peer
                ''',
                'require_remote_mode',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-remote-mib-retrieval', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Require the remote peer to support MIB retrieval
                ''',
                'require_remote_mib_retrieval',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-loopback', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Require the remote peer to support loopback mode
                ''',
                'require_loopback',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-link-monitoring', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Require the remote peer to support link
                monitoring
                ''',
                'require_link_monitoring',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('fast-hello-interval-enabled-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'fast_hello_interval_enabled_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('link-monitoring-enabled-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'link_monitoring_enabled_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-loopback-enabled-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'remote_loopback_enabled_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('mib-retrieval-enabled-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'mib_retrieval_enabled_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('udlf-enabled-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'udlf_enabled_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('mode-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'mode_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('connection-timeout-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'connection_timeout_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('symbol-period-window-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'symbol_period_window_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('symbol-period-threshold-low-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'symbol_period_threshold_low_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('symbol-period-threshold-high-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'symbol_period_threshold_high_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-window-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_window_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-threshold-low-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_threshold_low_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-threshold-high-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_threshold_high_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-period-window-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_period_window_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-period-threshold-low-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_period_threshold_low_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-period-threshold-high-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_period_threshold_high_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-seconds-window-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_seconds_window_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-seconds-threshold-low-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_seconds_threshold_low_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frame-seconds-threshold-high-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'frame_seconds_threshold_high_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('high-threshold-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'high_threshold_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('link-fault-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'link_fault_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('dying-gasp-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'dying_gasp_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('critical-event-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'critical_event_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('discovery-timeout-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'discovery_timeout_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('capabilities-conflict-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'capabilities_conflict_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('wiring-conflict-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'wiring_conflict_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('session-down-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'session_down_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('session-up-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'session_up_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-loopback-action-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'remote_loopback_action_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-mode-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'require_mode_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-mib-retrieval-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'require_mib_retrieval_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-loopback-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'require_loopback_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('require-link-monitoring-overridden', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Is this configuration information an interface
                override?
                ''',
                'require_link_monitoring_overridden',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'running-config-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.RunningConfigInterfaces' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.RunningConfigInterfaces',
            False, 
            [
            _MetaInfoClassMember('running-config-interface', REFERENCE_LIST, 'RunningConfigInterface' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface', 
                [], [], 
                '''                Ethernet Link OAM interface to get Running
                Config for
                ''',
                'running_config_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'running-config-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.Nodes.Node.Summary' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.Nodes.Node.Summary',
            False, 
            [
            _MetaInfoClassMember('interfaces', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces with 802.3 OAM
                configured
                ''',
                'interfaces',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('port-down', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Port Down' state
                ''',
                'port_down',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('passive-wait', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Passive Wait' state
                ''',
                'passive_wait',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('active-send', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Active Send' state
                ''',
                'active_send',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('evaluating', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Evaluating' state
                ''',
                'evaluating',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-accept', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Local Accept' state
                ''',
                'local_accept',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-reject', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Local Reject' state
                ''',
                'local_reject',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-reject', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Remote Reject'
                state
                ''',
                'remote_reject',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('operational', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in 'Operational' state
                ''',
                'operational',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('loopback-mode', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of interfaces in loopback mode
                ''',
                'loopback_mode',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('miswired-connections', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of miswired connections
                ''',
                'miswired_connections',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('events', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of events recorded
                ''',
                'events',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-events', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of local events recorded
                ''',
                'local_events',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-symbol-period', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of local symbol period events
                recorded
                ''',
                'local_symbol_period',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-frame', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The mumber of local frame error events recorded
                ''',
                'local_frame',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-frame-period', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of local frame period events recorded
                ''',
                'local_frame_period',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-frame-seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of local frame second events recoded
                ''',
                'local_frame_seconds',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-events', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of remote events recorded
                ''',
                'remote_events',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-symbol-period', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of remote symbol period events
                recorded
                ''',
                'remote_symbol_period',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-frame', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The mumber of remote frame error events recorded
                ''',
                'remote_frame',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-frame-period', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of remote frame period events
                recorded
                ''',
                'remote_frame_period',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-frame-seconds', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The number of remote frame second events recoded
                ''',
                'remote_frame_seconds',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'summary',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node
                ''',
                'node_name',
                'Cisco-IOS-XR-ethernet-link-oam-oper', True),
            _MetaInfoClassMember('summary', REFERENCE_CLASS, 'Summary' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.Nodes.Node.Summary', 
                [], [], 
                '''                Ethernet Link OAM Summary information for the
                entire node
                ''',
                'summary',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.Nodes' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.Nodes.Node', 
                [], [], 
                '''                Node-specific data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex',
            False, 
            [
            _MetaInfoClassMember('event-log-entry-index', ATTRIBUTE, 'str' , None, None, 
                [], ['[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Event Log Entry index
                ''',
                'event_log_entry_index',
                'Cisco-IOS-XR-ethernet-link-oam-oper', True),
            _MetaInfoClassMember('index', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Index in the log entries table
                ''',
                'index',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('handle', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface handle for this log entry
                ''',
                'handle',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('oui', ATTRIBUTE, 'str' , None, None, 
                [], ['([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                OUI for the log entry
                ''',
                'oui',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Timestamp in hundredths of a second since unix
                epoch for when the event occurred
                ''',
                'timestamp',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'LogEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'LogEnum', 
                [], [], 
                '''                Type of event that this entry describes
                ''',
                'type',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('location', REFERENCE_ENUM_CLASS, 'LogLocationEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'LogLocationEnum', 
                [], [], 
                '''                Where the event occurred
                ''',
                'location',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('event-total', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Total number of times event has occurred
                ''',
                'event_total',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('action-taken', REFERENCE_ENUM_CLASS, 'ActionEnum' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'ActionEnum', 
                [], [], 
                '''                Local action taken (If applicable)
                ''',
                'action_taken',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('window', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Size of the window (If applicable)
                ''',
                'window',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Size of the threshold (If applicable)
                ''',
                'threshold',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-high-threshold', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Size of the local high threshold (If applicable)
                . For remote threshold events this is scaled for
                comparison with the Breaching Value. This is to
                account for different local and remote window
                sizes.
                ''',
                'local_high_threshold',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                Breaching value (If applicable)
                ''',
                'value',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('running-total', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The running total number of errors seen since
                OAM was enabled on the interface(If applicable)
                ''',
                'running_total',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'event-log-entry-index',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes',
            False, 
            [
            _MetaInfoClassMember('event-log-entry-index', REFERENCE_LIST, 'EventLogEntryIndex' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex', 
                [], [], 
                '''                Ethernet Link OAM Event Log Entry Index to
                get data for
                ''',
                'event_log_entry_index',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'event-log-entry-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface',
            False, 
            [
            _MetaInfoClassMember('member-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Member Interface
                ''',
                'member_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', True),
            _MetaInfoClassMember('event-log-entry-indexes', REFERENCE_CLASS, 'EventLogEntryIndexes' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes', 
                [], [], 
                '''                Table of Ethernet Link OAM Event Log entries
                on the interface
                ''',
                'event_log_entry_indexes',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'event-log-entry-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.EventLogEntryInterfaces' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.EventLogEntryInterfaces',
            False, 
            [
            _MetaInfoClassMember('event-log-entry-interface', REFERENCE_LIST, 'EventLogEntryInterface' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface', 
                [], [], 
                '''                Ethernet Link OAM enabled interface to get
                Event Log Entry for
                ''',
                'event_log_entry_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'event-log-entry-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.StatsInterfaces.StatsInterface' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.StatsInterfaces.StatsInterface',
            False, 
            [
            _MetaInfoClassMember('member-interface', ATTRIBUTE, 'str' , None, None, 
                [], ['(([a-zA-Z0-9_]*\\d+/){3}\\d+)|(([a-zA-Z0-9_]*\\d+/){4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Member Interface
                ''',
                'member_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', True),
            _MetaInfoClassMember('information-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of information OAMPDUs transmitted
                ''',
                'information_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('information-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of information OAMPDUs received
                ''',
                'information_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('unique-event-notification-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of unique event notification OAMPDUs
                transmitted
                ''',
                'unique_event_notification_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('unique-event-notification-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of unique event notification OAMPDUs
                received
                ''',
                'unique_event_notification_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('duplicate-event-notification-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of duplicate event notification OAMPDUs
                transmitted
                ''',
                'duplicate_event_notification_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('duplicate-event-notification-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of duplicate event notification OAMPDUs
                received
                ''',
                'duplicate_event_notification_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('loopback-control-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of loopback control OAMPDUs transmitted
                ''',
                'loopback_control_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('loopback-control-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of loopback control OAMPDUs received
                ''',
                'loopback_control_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('variable-request-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of variable request OAMPDUs transmitted
                ''',
                'variable_request_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('variable-request-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of variable request OAMPDUs received
                ''',
                'variable_request_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('variable-response-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of variable response OAMPDUs transmitted
                ''',
                'variable_response_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('variable-response-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of variable response OAMPDUs received
                ''',
                'variable_response_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('org-specific-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of organization specific OAMPDUs
                transmitted
                ''',
                'org_specific_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('org-specific-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of organization specific OAMPDUs received
                ''',
                'org_specific_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('unsupported-codes-tx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of OAMPDUs with unsupported codes
                transmitted
                ''',
                'unsupported_codes_tx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('unsupported-codes-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of OAMPDUs with unsupported codes
                received
                ''',
                'unsupported_codes_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('frames-lost-due-to-oam', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of frames lost due to OAM
                ''',
                'frames_lost_due_to_oam',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('fixed-frames-rx', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of RX frames 'fixed' by OAM
                ''',
                'fixed_frames_rx',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-error-symbol-period-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of local error symbol period records
                ''',
                'local_error_symbol_period_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-error-frame-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of local error frame records
                ''',
                'local_error_frame_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-error-frame-period-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of local error frame period records
                ''',
                'local_error_frame_period_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('local-error-frame-second-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of local error frame second records
                ''',
                'local_error_frame_second_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-error-symbol-period-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of remote error symbol period records
                ''',
                'remote_error_symbol_period_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-error-frame-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of remote error frame records
                ''',
                'remote_error_frame_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-error-frame-period-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of remote error frame period records
                ''',
                'remote_error_frame_period_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('remote-error-frame-second-records', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Number of remote error frame second records
                ''',
                'remote_error_frame_second_records',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'stats-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam.StatsInterfaces' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam.StatsInterfaces',
            False, 
            [
            _MetaInfoClassMember('stats-interface', REFERENCE_LIST, 'StatsInterface' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.StatsInterfaces.StatsInterface', 
                [], [], 
                '''                Ethernet Link OAM interface to get Stats for
                ''',
                'stats_interface',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'stats-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
    'EtherLinkOam' : {
        'meta_info' : _MetaInfoClass('EtherLinkOam',
            False, 
            [
            _MetaInfoClassMember('discovery-info-interfaces', REFERENCE_CLASS, 'DiscoveryInfoInterfaces' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.DiscoveryInfoInterfaces', 
                [], [], 
                '''                Table of Ethernet Link OAM enabled interfaces
                within Discovery Info container
                ''',
                'discovery_info_interfaces',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('interface-state-interfaces', REFERENCE_CLASS, 'InterfaceStateInterfaces' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.InterfaceStateInterfaces', 
                [], [], 
                '''                Table of Ethernet Link OAM enabled interfaces
                within Interface State container
                ''',
                'interface_state_interfaces',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('running-config-interfaces', REFERENCE_CLASS, 'RunningConfigInterfaces' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.RunningConfigInterfaces', 
                [], [], 
                '''                Table of Ethernet Link OAM enabled interfaces
                within Running Config container
                ''',
                'running_config_interfaces',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.Nodes', 
                [], [], 
                '''                Node table for node-specific operational data
                ''',
                'nodes',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('event-log-entry-interfaces', REFERENCE_CLASS, 'EventLogEntryInterfaces' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.EventLogEntryInterfaces', 
                [], [], 
                '''                Table of Ethernet Link OAM enabled interfaces
                within Event Log Entry container
                ''',
                'event_log_entry_interfaces',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            _MetaInfoClassMember('stats-interfaces', REFERENCE_CLASS, 'StatsInterfaces' , 'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper', 'EtherLinkOam.StatsInterfaces', 
                [], [], 
                '''                Table of Ethernet Link OAM enabled interfaces
                within Stats container
                ''',
                'stats_interfaces',
                'Cisco-IOS-XR-ethernet-link-oam-oper', False),
            ],
            'Cisco-IOS-XR-ethernet-link-oam-oper',
            'ether-link-oam',
            _yang_ns._namespaces['Cisco-IOS-XR-ethernet-link-oam-oper'],
        'ydk.models.ethernet.Cisco_IOS_XR_ethernet_link_oam_oper'
        ),
    },
}
_meta_table['EtherLinkOam.DiscoveryInfoInterfaces.DiscoveryInfoInterface']['meta_info'].parent =_meta_table['EtherLinkOam.DiscoveryInfoInterfaces']['meta_info']
_meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.Errors']['meta_info'].parent =_meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface']['meta_info']
_meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface.EfdTriggers']['meta_info'].parent =_meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface']['meta_info']
_meta_table['EtherLinkOam.InterfaceStateInterfaces.InterfaceStateInterface']['meta_info'].parent =_meta_table['EtherLinkOam.InterfaceStateInterfaces']['meta_info']
_meta_table['EtherLinkOam.RunningConfigInterfaces.RunningConfigInterface']['meta_info'].parent =_meta_table['EtherLinkOam.RunningConfigInterfaces']['meta_info']
_meta_table['EtherLinkOam.Nodes.Node.Summary']['meta_info'].parent =_meta_table['EtherLinkOam.Nodes.Node']['meta_info']
_meta_table['EtherLinkOam.Nodes.Node']['meta_info'].parent =_meta_table['EtherLinkOam.Nodes']['meta_info']
_meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes.EventLogEntryIndex']['meta_info'].parent =_meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes']['meta_info']
_meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface.EventLogEntryIndexes']['meta_info'].parent =_meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface']['meta_info']
_meta_table['EtherLinkOam.EventLogEntryInterfaces.EventLogEntryInterface']['meta_info'].parent =_meta_table['EtherLinkOam.EventLogEntryInterfaces']['meta_info']
_meta_table['EtherLinkOam.StatsInterfaces.StatsInterface']['meta_info'].parent =_meta_table['EtherLinkOam.StatsInterfaces']['meta_info']
_meta_table['EtherLinkOam.DiscoveryInfoInterfaces']['meta_info'].parent =_meta_table['EtherLinkOam']['meta_info']
_meta_table['EtherLinkOam.InterfaceStateInterfaces']['meta_info'].parent =_meta_table['EtherLinkOam']['meta_info']
_meta_table['EtherLinkOam.RunningConfigInterfaces']['meta_info'].parent =_meta_table['EtherLinkOam']['meta_info']
_meta_table['EtherLinkOam.Nodes']['meta_info'].parent =_meta_table['EtherLinkOam']['meta_info']
_meta_table['EtherLinkOam.EventLogEntryInterfaces']['meta_info'].parent =_meta_table['EtherLinkOam']['meta_info']
_meta_table['EtherLinkOam.StatsInterfaces']['meta_info'].parent =_meta_table['EtherLinkOam']['meta_info']
