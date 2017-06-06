


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SpaOperStateEnum' : _MetaInfoEnum('SpaOperStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper',
        {
            'spa-state-reset':'spa_state_reset',
            'spa-state-failed':'spa_state_failed',
            'spa-state-booting':'spa_state_booting',
            'spa-state-ready':'spa_state_ready',
        }, 'Cisco-IOS-XR-asr9k-lc-fca-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper']),
    'SpaFailureReasonEnum' : _MetaInfoEnum('SpaFailureReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper',
        {
            'spa-failure-reason-unknown':'spa_failure_reason_unknown',
            'spa-failure-reason-spi-failure':'spa_failure_reason_spi_failure',
            'spa-failure-reason-boot':'spa_failure_reason_boot',
            'spa-failure-reason-hw-failed':'spa_failure_reason_hw_failed',
            'spa-failure-reason-sw-failed':'spa_failure_reason_sw_failed',
            'spa-failure-reason-sw-restart':'spa_failure_reason_sw_restart',
            'spa-failure-reason-check-fpd':'spa_failure_reason_check_fpd',
            'spa-failure-reason-read-type':'spa_failure_reason_read_type',
        }, 'Cisco-IOS-XR-asr9k-lc-fca-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper']),
    'SpaResetReasonEnum' : _MetaInfoEnum('SpaResetReasonEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper',
        {
            'spa-reset-reason-unknown':'spa_reset_reason_unknown',
            'spa-reset-reason-manual':'spa_reset_reason_manual',
            'spa-reset-reason-fpd-upgrade':'spa_reset_reason_fpd_upgrade',
            'spa-reset-reason-audit-fail':'spa_reset_reason_audit_fail',
            'spa-reset-reason-failure':'spa_reset_reason_failure',
        }, 'Cisco-IOS-XR-asr9k-lc-fca-oper', _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper']),
    'MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo' : {
        'meta_info' : _MetaInfoClass('MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo',
            False, 
            [
            _MetaInfoClassMember('bay', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                bay
                ''',
                'bay',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('ep-idprom-data', ATTRIBUTE, 'str' , None, None, 
                [(0, 256)], [], 
                '''                ep idprom data
                ''',
                'ep_idprom_data',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('ep-idprom-major', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ep idprom major
                ''',
                'ep_idprom_major',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('ep-idprom-minor', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ep idprom minor
                ''',
                'ep_idprom_minor',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('ep-presence', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ep presence
                ''',
                'ep_presence',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('ep-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                ep state
                ''',
                'ep_state',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('ep-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ep type
                ''',
                'ep_type',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('if-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                if event
                ''',
                'if_event',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('if-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                if state
                ''',
                'if_state',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('ifsubsys', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ifsubsys
                ''',
                'ifsubsys',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'mpa-internal-info',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy' : {
        'meta_info' : _MetaInfoClass('MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'str' , None, None, 
                [], [b'[0-9a-fA-F]{1,8}'], 
                '''                ifsubsys number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', True),
            _MetaInfoClassMember('mpa-internal-info', REFERENCE_CLASS, 'MpaInternalInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo', 
                [], [], 
                '''                mpa internal info
                ''',
                'mpa_internal_info',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'ifsubsy',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'MpaInternal.Nodes.Node.Bay.Ifsubsies' : {
        'meta_info' : _MetaInfoClass('MpaInternal.Nodes.Node.Bay.Ifsubsies',
            False, 
            [
            _MetaInfoClassMember('ifsubsy', REFERENCE_LIST, 'Ifsubsy' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy', 
                [], [], 
                '''                Number
                ''',
                'ifsubsy',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'ifsubsies',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'MpaInternal.Nodes.Node.Bay' : {
        'meta_info' : _MetaInfoClass('MpaInternal.Nodes.Node.Bay',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                bay number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', True),
            _MetaInfoClassMember('ifsubsies', REFERENCE_CLASS, 'Ifsubsies' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'MpaInternal.Nodes.Node.Bay.Ifsubsies', 
                [], [], 
                '''                Table of Ifsubsys
                ''',
                'ifsubsies',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'bay',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'MpaInternal.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('MpaInternal.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node number
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', True),
            _MetaInfoClassMember('bay', REFERENCE_LIST, 'Bay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'MpaInternal.Nodes.Node.Bay', 
                [], [], 
                '''                Number
                ''',
                'bay',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'MpaInternal.Nodes' : {
        'meta_info' : _MetaInfoClass('MpaInternal.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'MpaInternal.Nodes.Node', 
                [], [], 
                '''                Number
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'MpaInternal' : {
        'meta_info' : _MetaInfoClass('MpaInternal',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'MpaInternal.Nodes', 
                [], [], 
                '''                Table of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'mpa-internal',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail' : {
        'meta_info' : _MetaInfoClass('Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail',
            False, 
            [
            _MetaInfoClassMember('bay-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                BAY number
                ''',
                'bay_number',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('insertion-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time when SPA last insertedin calendar format:
                seconds since00:00:00 UTC, January 1, 1970
                ''',
                'insertion_time',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('is-spa-admin-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SPA admin state is Up
                ''',
                'is_spa_admin_up',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('is-spa-in-reset', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SPA in reset
                ''',
                'is_spa_in_reset',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('is-spa-inserted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SPA inserted
                ''',
                'is_spa_inserted',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('is-spa-power-admin-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SPA power admin state is Up
                ''',
                'is_spa_power_admin_up',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('is-spa-powered', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If SPA powered
                ''',
                'is_spa_powered',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('last-failure-reason', REFERENCE_ENUM_CLASS, 'SpaFailureReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'SpaFailureReasonEnum', 
                [], [], 
                '''                Last Failure Reason
                ''',
                'last_failure_reason',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('last-ready-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time when SPA last reached Ready statein
                calendar format: seconds since00:00:00 UTC,
                January 1, 1970
                ''',
                'last_ready_time',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('last-reset-reason', REFERENCE_ENUM_CLASS, 'SpaResetReasonEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'SpaResetReasonEnum', 
                [], [], 
                '''                Last reset reason
                ''',
                'last_reset_reason',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('spa-oper-state', REFERENCE_ENUM_CLASS, 'SpaOperStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'SpaOperStateEnum', 
                [], [], 
                '''                SPA operational state
                ''',
                'spa_oper_state',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('spa-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                SPA type
                ''',
                'spa_type',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            _MetaInfoClassMember('up-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Uptime in seconds
                ''',
                'up_time',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'mpa-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'Mpa.Nodes.Node.Bay.MpaDetailTable' : {
        'meta_info' : _MetaInfoClass('Mpa.Nodes.Node.Bay.MpaDetailTable',
            False, 
            [
            _MetaInfoClassMember('mpa-detail', REFERENCE_CLASS, 'MpaDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail', 
                [], [], 
                '''                mpa detail status info
                ''',
                'mpa_detail',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'mpa-detail-table',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'Mpa.Nodes.Node.Bay' : {
        'meta_info' : _MetaInfoClass('Mpa.Nodes.Node.Bay',
            False, 
            [
            _MetaInfoClassMember('number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                bay number
                ''',
                'number',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', True),
            _MetaInfoClassMember('mpa-detail-table', REFERENCE_CLASS, 'MpaDetailTable' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'Mpa.Nodes.Node.Bay.MpaDetailTable', 
                [], [], 
                '''                Table of Mpa Detail Info
                ''',
                'mpa_detail_table',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'bay',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'Mpa.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Mpa.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                node number
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', True),
            _MetaInfoClassMember('bay', REFERENCE_LIST, 'Bay' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'Mpa.Nodes.Node.Bay', 
                [], [], 
                '''                Number
                ''',
                'bay',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'Mpa.Nodes' : {
        'meta_info' : _MetaInfoClass('Mpa.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'Mpa.Nodes.Node', 
                [], [], 
                '''                Number
                ''',
                'node',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
    'Mpa' : {
        'meta_info' : _MetaInfoClass('Mpa',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper', 'Mpa.Nodes', 
                [], [], 
                '''                Table of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-asr9k-lc-fca-oper', False),
            ],
            'Cisco-IOS-XR-asr9k-lc-fca-oper',
            'mpa',
            _yang_ns._namespaces['Cisco-IOS-XR-asr9k-lc-fca-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_asr9k_lc_fca_oper'
        ),
    },
}
_meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy.MpaInternalInfo']['meta_info'].parent =_meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy']['meta_info']
_meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies.Ifsubsy']['meta_info'].parent =_meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies']['meta_info']
_meta_table['MpaInternal.Nodes.Node.Bay.Ifsubsies']['meta_info'].parent =_meta_table['MpaInternal.Nodes.Node.Bay']['meta_info']
_meta_table['MpaInternal.Nodes.Node.Bay']['meta_info'].parent =_meta_table['MpaInternal.Nodes.Node']['meta_info']
_meta_table['MpaInternal.Nodes.Node']['meta_info'].parent =_meta_table['MpaInternal.Nodes']['meta_info']
_meta_table['MpaInternal.Nodes']['meta_info'].parent =_meta_table['MpaInternal']['meta_info']
_meta_table['Mpa.Nodes.Node.Bay.MpaDetailTable.MpaDetail']['meta_info'].parent =_meta_table['Mpa.Nodes.Node.Bay.MpaDetailTable']['meta_info']
_meta_table['Mpa.Nodes.Node.Bay.MpaDetailTable']['meta_info'].parent =_meta_table['Mpa.Nodes.Node.Bay']['meta_info']
_meta_table['Mpa.Nodes.Node.Bay']['meta_info'].parent =_meta_table['Mpa.Nodes.Node']['meta_info']
_meta_table['Mpa.Nodes.Node']['meta_info'].parent =_meta_table['Mpa.Nodes']['meta_info']
_meta_table['Mpa.Nodes']['meta_info'].parent =_meta_table['Mpa']['meta_info']
