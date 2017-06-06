


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'ImStateEnumEnum' : _MetaInfoEnum('ImStateEnumEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper',
        {
            'im-state-not-ready':'im_state_not_ready',
            'im-state-admin-down':'im_state_admin_down',
            'im-state-down':'im_state_down',
            'im-state-up':'im_state_up',
            'im-state-shutdown':'im_state_shutdown',
            'im-state-err-disable':'im_state_err_disable',
            'im-state-down-immediate':'im_state_down_immediate',
            'im-state-down-immediate-admin':'im_state_down_immediate_admin',
            'im-state-down-graceful':'im_state_down_graceful',
            'im-state-begin-shutdown':'im_state_begin_shutdown',
            'im-state-end-shutdown':'im_state_end_shutdown',
            'im-state-begin-error-disable':'im_state_begin_error_disable',
            'im-state-end-error-disable':'im_state_end_error_disable',
            'im-state-begin-down-graceful':'im_state_begin_down_graceful',
            'im-state-reset':'im_state_reset',
            'im-state-operational':'im_state_operational',
            'im-state-not-operational':'im_state_not_operational',
            'im-state-unknown':'im_state_unknown',
            'im-state-last':'im_state_last',
        }, 'Cisco-IOS-XR-ifmgr-oper', _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper']),
    'InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_',
            False, 
            [
            _MetaInfoClassMember('flaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of underlying state flaps
                ''',
                'flaps',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-suppressed-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if state is suppressed
                ''',
                'is_suppressed_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampening penalty of the interface
                ''',
                'penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('seconds-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining period of suppression in secs
                ''',
                'seconds_remaining',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Underlying state of the node
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening',
            False, 
            [
            _MetaInfoClassMember('flaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of underlying state flaps
                ''',
                'flaps',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-suppressed-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if state is suppressed
                ''',
                'is_suppressed_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampening penalty of the interface
                ''',
                'penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('seconds-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining period of suppression in secs
                ''',
                'seconds_remaining',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Underlying state of the node
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'capsulation-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation',
            False, 
            [
            _MetaInfoClassMember('capsulation-dampening', REFERENCE_CLASS, 'CapsulationDampening' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening', 
                [], [], 
                '''                Capsulation dampening
                ''',
                'capsulation_dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('capsulation-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capsulation number
                ''',
                'capsulation_number',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'capsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Interfaces.Interface.IfDampening' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Interfaces.Interface.IfDampening',
            False, 
            [
            _MetaInfoClassMember('capsulation', REFERENCE_LIST, 'Capsulation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation', 
                [], [], 
                '''                Dampening information for capsulations
                ''',
                'capsulation',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('half-life', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured decay half life in mins
                ''',
                'half_life',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('interface-dampening', REFERENCE_CLASS, 'InterfaceDampening_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_', 
                [], [], 
                '''                Interface dampening
                ''',
                'interface_dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-dampening-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if dampening is enabled
                ''',
                'is_dampening_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('last-state-transition-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time elasped after the last state transition
                ''',
                'last_state_transition_time',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('maximum-suppress-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum suppress time in mins
                ''',
                'maximum_suppress_time',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('restart-penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured restart penalty
                ''',
                'restart_penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('reuse-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured reuse threshold
                ''',
                'reuse_threshold',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state-transition-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the state has changed
                ''',
                'state_transition_count',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('suppress-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value of suppress threshold
                ''',
                'suppress_threshold',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'if-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the
                ''',
                'interface_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('if-dampening', REFERENCE_CLASS, 'IfDampening' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Interfaces.Interface.IfDampening', 
                [], [], 
                '''                Dampening info for the interface
                ''',
                'if_dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Interfaces' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Interfaces.Interface', 
                [], [], 
                '''                The interface for which dampening info is being
                queried
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_',
            False, 
            [
            _MetaInfoClassMember('flaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of underlying state flaps
                ''',
                'flaps',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-suppressed-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if state is suppressed
                ''',
                'is_suppressed_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampening penalty of the interface
                ''',
                'penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('seconds-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining period of suppression in secs
                ''',
                'seconds_remaining',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Underlying state of the node
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening',
            False, 
            [
            _MetaInfoClassMember('flaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of underlying state flaps
                ''',
                'flaps',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-suppressed-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if state is suppressed
                ''',
                'is_suppressed_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampening penalty of the interface
                ''',
                'penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('seconds-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining period of suppression in secs
                ''',
                'seconds_remaining',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Underlying state of the node
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'capsulation-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation',
            False, 
            [
            _MetaInfoClassMember('capsulation-dampening', REFERENCE_CLASS, 'CapsulationDampening' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening', 
                [], [], 
                '''                Capsulation dampening
                ''',
                'capsulation_dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('capsulation-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capsulation number
                ''',
                'capsulation_number',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'capsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle',
            False, 
            [
            _MetaInfoClassMember('interface-handle-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                The interface handle
                ''',
                'interface_handle_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('capsulation', REFERENCE_LIST, 'Capsulation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation', 
                [], [], 
                '''                Dampening information for capsulations
                ''',
                'capsulation',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('half-life', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured decay half life in mins
                ''',
                'half_life',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('interface-dampening', REFERENCE_CLASS, 'InterfaceDampening_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_', 
                [], [], 
                '''                Interface dampening
                ''',
                'interface_dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-dampening-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if dampening is enabled
                ''',
                'is_dampening_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('last-state-transition-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time elasped after the last state transition
                ''',
                'last_state_transition_time',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('maximum-suppress-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum suppress time in mins
                ''',
                'maximum_suppress_time',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('restart-penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured restart penalty
                ''',
                'restart_penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('reuse-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured reuse threshold
                ''',
                'reuse_threshold',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state-transition-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the state has changed
                ''',
                'state_transition_count',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('suppress-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value of suppress threshold
                ''',
                'suppress_threshold',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'if-handle',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles',
            False, 
            [
            _MetaInfoClassMember('if-handle', REFERENCE_LIST, 'IfHandle' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle', 
                [], [], 
                '''                Dampening info for the interface handle
                ''',
                'if_handle',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'if-handles',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_',
            False, 
            [
            _MetaInfoClassMember('flaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of underlying state flaps
                ''',
                'flaps',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-suppressed-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if state is suppressed
                ''',
                'is_suppressed_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampening penalty of the interface
                ''',
                'penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('seconds-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining period of suppression in secs
                ''',
                'seconds_remaining',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Underlying state of the node
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening',
            False, 
            [
            _MetaInfoClassMember('flaps', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of underlying state flaps
                ''',
                'flaps',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-suppressed-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if state is suppressed
                ''',
                'is_suppressed_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Dampening penalty of the interface
                ''',
                'penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('seconds-remaining', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remaining period of suppression in secs
                ''',
                'seconds_remaining',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Underlying state of the node
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'capsulation-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation',
            False, 
            [
            _MetaInfoClassMember('capsulation-dampening', REFERENCE_CLASS, 'CapsulationDampening' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening', 
                [], [], 
                '''                Capsulation dampening
                ''',
                'capsulation_dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('capsulation-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Capsulation number
                ''',
                'capsulation_number',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'capsulation',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the
                ''',
                'interface_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('capsulation', REFERENCE_LIST, 'Capsulation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation', 
                [], [], 
                '''                Dampening information for capsulations
                ''',
                'capsulation',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('half-life', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured decay half life in mins
                ''',
                'half_life',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('interface-dampening', REFERENCE_CLASS, 'InterfaceDampening_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_', 
                [], [], 
                '''                Interface dampening
                ''',
                'interface_dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('is-dampening-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Flag showing if dampening is enabled
                ''',
                'is_dampening_enabled',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('last-state-transition-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The time elasped after the last state transition
                ''',
                'last_state_transition_time',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('maximum-suppress-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum suppress time in mins
                ''',
                'maximum_suppress_time',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('restart-penalty', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured restart penalty
                ''',
                'restart_penalty',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('reuse-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured reuse threshold
                ''',
                'reuse_threshold',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state-transition-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the state has changed
                ''',
                'state_transition_count',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('suppress-threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value of suppress threshold
                ''',
                'suppress_threshold',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface', 
                [], [], 
                '''                Dampening info for the interface
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show.Dampening' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show.Dampening',
            False, 
            [
            _MetaInfoClassMember('if-handles', REFERENCE_CLASS, 'IfHandles' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles', 
                [], [], 
                '''                Interface handle for which dampening info
                queried
                ''',
                'if_handles',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces', 
                [], [], 
                '''                Table of interfaces for which dampening info
                can be queried
                ''',
                'interfaces',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node.Show' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node.Show',
            False, 
            [
            _MetaInfoClassMember('dampening', REFERENCE_CLASS, 'Dampening' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show.Dampening', 
                [], [], 
                '''                Dampening information of the interface(s)
                being queried
                ''',
                'dampening',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'show',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The location of the interface(s)
                ''',
                'node_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('show', REFERENCE_CLASS, 'Show' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node.Show', 
                [], [], 
                '''                Show details for the interfaces
                ''',
                'show',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening.Nodes' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes.Node', 
                [], [], 
                '''                The location of the interface(s) being queried
                ''',
                'node',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceDampening' : {
        'meta_info' : _MetaInfoClass('InterfaceDampening',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Interfaces', 
                [], [], 
                '''                The interface list for which dampening info is
                available
                ''',
                'interfaces',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceDampening.Nodes', 
                [], [], 
                '''                The location of the interface(s) being queried
                ''',
                'nodes',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface-dampening',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('actual-line-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Line protocol state with no translation of error
                disable or shutdown
                ''',
                'actual_line_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('actual-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Operational state with no translation of error
                disable or shutdown
                ''',
                'actual_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface bandwidth (Kb/s)
                ''',
                'bandwidth',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('encapsulation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface encapsulation
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('encapsulation-type-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Interface encapsulation description string
                ''',
                'encapsulation_type_string',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('l2-transport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L2 transport
                ''',
                'l2_transport',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Line protocol state
                ''',
                'line_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MTU in bytes
                ''',
                'mtu',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('parent-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface
                ''',
                'parent_interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Operational state
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('sub-interface-mtu-overhead', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Subif MTU overhead
                ''',
                'sub_interface_mtu_overhead',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface type
                ''',
                'type',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview',
            False, 
            [
            _MetaInfoClassMember('locationview-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The location to filter on
                ''',
                'locationview_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces', 
                [], [], 
                '''                Operational data for all interfaces and
                controllers
                ''',
                'interfaces',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'locationview',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.Locationviews' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.Locationviews',
            False, 
            [
            _MetaInfoClassMember('locationview', REFERENCE_LIST, 'Locationview' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview', 
                [], [], 
                '''                Operational data for all interfaces and
                controllers on a particular node
                ''',
                'locationview',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'locationviews',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('actual-line-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Line protocol state with no translation of error
                disable or shutdown
                ''',
                'actual_line_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('actual-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Operational state with no translation of error
                disable or shutdown
                ''',
                'actual_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface bandwidth (Kb/s)
                ''',
                'bandwidth',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('encapsulation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface encapsulation
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('encapsulation-type-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Interface encapsulation description string
                ''',
                'encapsulation_type_string',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('l2-transport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L2 transport
                ''',
                'l2_transport',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Line protocol state
                ''',
                'line_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MTU in bytes
                ''',
                'mtu',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('parent-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface
                ''',
                'parent_interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Operational state
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('sub-interface-mtu-overhead', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Subif MTU overhead
                ''',
                'sub_interface_mtu_overhead',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface type
                ''',
                'type',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation',
            False, 
            [
            _MetaInfoClassMember('pq-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'((([a-zA-Z0-9_]*\\d+)|(\\*))/){2}(([a-zA-Z0-9_]*\\d+)|(\\*))'], 
                '''                The partially qualified location to filter
                on
                ''',
                'pq_node_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces', 
                [], [], 
                '''                Operational data for all interfaces and
                controllers
                ''',
                'interfaces',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'pq-node-location',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.PqNodeLocations' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.PqNodeLocations',
            False, 
            [
            _MetaInfoClassMember('pq-node-location', REFERENCE_LIST, 'PqNodeLocation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation', 
                [], [], 
                '''                Operational data for all interfaces and
                controllers on a particular pq_node
                ''',
                'pq_node_location',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'pq-node-locations',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                The name of the interface
                ''',
                'interface_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('actual-line-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Line protocol state with no translation of error
                disable or shutdown
                ''',
                'actual_line_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('actual-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Operational state with no translation of error
                disable or shutdown
                ''',
                'actual_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('bandwidth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface bandwidth (Kb/s)
                ''',
                'bandwidth',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('encapsulation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface encapsulation
                ''',
                'encapsulation',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('encapsulation-type-string', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                Interface encapsulation description string
                ''',
                'encapsulation_type_string',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('l2-transport', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                L2 transport
                ''',
                'l2_transport',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('line-state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Line protocol state
                ''',
                'line_state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('mtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                MTU in bytes
                ''',
                'mtu',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('parent-interface', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Parent Interface
                ''',
                'parent_interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'ImStateEnumEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'ImStateEnumEnum', 
                [], [], 
                '''                Operational state
                ''',
                'state',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('sub-interface-mtu-overhead', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Subif MTU overhead
                ''',
                'sub_interface_mtu_overhead',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface type
                ''',
                'type',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface', 
                [], [], 
                '''                The operational attributes for a particular
                interface
                ''',
                'interface',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode.SystemView' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode.SystemView',
            False, 
            [
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces', 
                [], [], 
                '''                Operational data for all interfaces and
                controllers
                ''',
                'interfaces',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'system-view',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes.DataNode' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes.DataNode',
            False, 
            [
            _MetaInfoClassMember('data-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The location of the (D)RP
                ''',
                'data_node_name',
                'Cisco-IOS-XR-ifmgr-oper', True),
            _MetaInfoClassMember('locationviews', REFERENCE_CLASS, 'Locationviews' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.Locationviews', 
                [], [], 
                '''                Location-specific view of interface
                operational data
                ''',
                'locationviews',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('pq-node-locations', REFERENCE_CLASS, 'PqNodeLocations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.PqNodeLocations', 
                [], [], 
                '''                Partially qualified Location-specific view of
                interface operational data
                ''',
                'pq_node_locations',
                'Cisco-IOS-XR-ifmgr-oper', False),
            _MetaInfoClassMember('system-view', REFERENCE_CLASS, 'SystemView' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode.SystemView', 
                [], [], 
                '''                System-wide view of interface operational data
                ''',
                'system_view',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'data-node',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties.DataNodes' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties.DataNodes',
            False, 
            [
            _MetaInfoClassMember('data-node', REFERENCE_LIST, 'DataNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes.DataNode', 
                [], [], 
                '''                The location of a (D)RP in the same LR as the
                interface being queried
                ''',
                'data_node',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'data-nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
    'InterfaceProperties' : {
        'meta_info' : _MetaInfoClass('InterfaceProperties',
            False, 
            [
            _MetaInfoClassMember('data-nodes', REFERENCE_CLASS, 'DataNodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper', 'InterfaceProperties.DataNodes', 
                [], [], 
                '''                Operational data for interfaces
                ''',
                'data_nodes',
                'Cisco-IOS-XR-ifmgr-oper', False),
            ],
            'Cisco-IOS-XR-ifmgr-oper',
            'interface-properties',
            _yang_ns._namespaces['Cisco-IOS-XR-ifmgr-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ifmgr_oper'
        ),
    },
}
_meta_table['InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation.CapsulationDampening']['meta_info'].parent =_meta_table['InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation']['meta_info']
_meta_table['InterfaceDampening.Interfaces.Interface.IfDampening.InterfaceDampening_']['meta_info'].parent =_meta_table['InterfaceDampening.Interfaces.Interface.IfDampening']['meta_info']
_meta_table['InterfaceDampening.Interfaces.Interface.IfDampening.Capsulation']['meta_info'].parent =_meta_table['InterfaceDampening.Interfaces.Interface.IfDampening']['meta_info']
_meta_table['InterfaceDampening.Interfaces.Interface.IfDampening']['meta_info'].parent =_meta_table['InterfaceDampening.Interfaces.Interface']['meta_info']
_meta_table['InterfaceDampening.Interfaces.Interface']['meta_info'].parent =_meta_table['InterfaceDampening.Interfaces']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation.CapsulationDampening']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.InterfaceDampening_']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle.Capsulation']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles.IfHandle']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation.CapsulationDampening']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.InterfaceDampening_']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface.Capsulation']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces.Interface']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.IfHandles']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening.Interfaces']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show.Dampening']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node.Show']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node.Show']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes.Node']['meta_info']
_meta_table['InterfaceDampening.Nodes.Node']['meta_info'].parent =_meta_table['InterfaceDampening.Nodes']['meta_info']
_meta_table['InterfaceDampening.Interfaces']['meta_info'].parent =_meta_table['InterfaceDampening']['meta_info']
_meta_table['InterfaceDampening.Nodes']['meta_info'].parent =_meta_table['InterfaceDampening']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces.Interface']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview.Interfaces']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews.Locationview']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces.Interface']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation.Interfaces']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations.PqNodeLocation']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces.Interface']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.SystemView.Interfaces']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode.SystemView']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.Locationviews']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.PqNodeLocations']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode.SystemView']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes.DataNode']['meta_info']
_meta_table['InterfaceProperties.DataNodes.DataNode']['meta_info'].parent =_meta_table['InterfaceProperties.DataNodes']['meta_info']
_meta_table['InterfaceProperties.DataNodes']['meta_info'].parent =_meta_table['InterfaceProperties']['meta_info']
