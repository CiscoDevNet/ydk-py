


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr' : {
        'meta_info' : _MetaInfoClass('Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr',
            False, 
            [
            _MetaInfoClassMember('create-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                create ok
                ''',
                'create_ok',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('create-req', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                create req
                ''',
                'create_req',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('delete-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                delete ok
                ''',
                'delete_ok',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('delete-req', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                delete req
                ''',
                'delete_req',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('eod-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                eod ok
                ''',
                'eod_ok',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('eod-req', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                eod req
                ''',
                'eod_req',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('err-db-exists', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                err db exists
                ''',
                'err_db_exists',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('err-db-nomem', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                err db nomem
                ''',
                'err_db_nomem',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('err-db-notfound', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                err db notfound
                ''',
                'err_db_notfound',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('err-hw-fail', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                err hw fail
                ''',
                'err_hw_fail',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('err-ref-resolve', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                err ref resolve
                ''',
                'err_ref_resolve',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                npu id
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('num-objs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num objs
                ''',
                'num_objs',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('update-ok', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                update ok
                ''',
                'update_ok',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('update-req', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                update req
                ''',
                'update_req',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'npu-tblr',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Resources.Nodes.Node.TableDatas.TableData' : {
        'meta_info' : _MetaInfoClass('Dpa.Resources.Nodes.Node.TableDatas.TableData',
            False, 
            [
            _MetaInfoClassMember('resource', ATTRIBUTE, 'int' , None, None, 
                [('0', '106')], [], 
                '''                Resource type
                ''',
                'resource',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('is-global', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is global
                ''',
                'is_global',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                name
                ''',
                'name',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-tblr', REFERENCE_LIST, 'NpuTblr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr', 
                [], [], 
                '''                npu tblr
                ''',
                'npu_tblr',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('num-npus', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                num npus
                ''',
                'num_npus',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('table-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                table id
                ''',
                'table_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('table-specific-list', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                table specific list
                ''',
                'table_specific_list',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'table-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Resources.Nodes.Node.TableDatas' : {
        'meta_info' : _MetaInfoClass('Dpa.Resources.Nodes.Node.TableDatas',
            False, 
            [
            _MetaInfoClassMember('table-data', REFERENCE_LIST, 'TableData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Resources.Nodes.Node.TableDatas.TableData', 
                [], [], 
                '''                Resources table
                ''',
                'table_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'table-datas',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Resources.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Dpa.Resources.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('table-datas', REFERENCE_CLASS, 'TableDatas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Resources.Nodes.Node.TableDatas', 
                [], [], 
                '''                DPA Resources table
                ''',
                'table_datas',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Resources.Nodes' : {
        'meta_info' : _MetaInfoClass('Dpa.Resources.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Resources.Nodes.Node', 
                [], [], 
                '''                DPA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Resources' : {
        'meta_info' : _MetaInfoClass('Dpa.Resources',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Resources.Nodes', 
                [], [], 
                '''                DPA data for available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'resources',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear.VoqBaseStatsClearData' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear.VoqBaseStatsClearData',
            False, 
            [
            _MetaInfoClassMember('base-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface handle
                ''',
                'base_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('clear-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                clear status
                ''',
                'clear_status',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-base-stats-clear-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear',
            False, 
            [
            _MetaInfoClassMember('npu-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Npu Number
                ''',
                'npu_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('voq-base-stats-clear-data', REFERENCE_LIST, 'VoqBaseStatsClearData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear.VoqBaseStatsClearData', 
                [], [], 
                '''                Clear stats  for a particular voq base
                number
                ''',
                'voq_base_stats_clear_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-base-number-stats-clear',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears',
            False, 
            [
            _MetaInfoClassMember('voq-base-number-stats-clear', REFERENCE_LIST, 'VoqBaseNumberStatsClear' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear', 
                [], [], 
                '''                Filter by npu number
                ''',
                'voq_base_number_stats_clear',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-base-number-stats-clears',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData.TrapSpecificStatsData' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData.TrapSpecificStatsData',
            False, 
            [
            _MetaInfoClassMember('trap-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Trap Number
                ''',
                'trap_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('encap-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                encap id
                ''',
                'encap_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('fec-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                fec id
                ''',
                'fec_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('gport', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                gport
                ''',
                'gport',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                id
                ''',
                'id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('mc-group', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                mc group
                ''',
                'mc_group',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                npu id
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                offset
                ''',
                'offset',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('packet-accepted', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet accepted
                ''',
                'packet_accepted',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('packet-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                packet dropped
                ''',
                'packet_dropped',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                policer id
                ''',
                'policer_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                priority
                ''',
                'priority',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('stats-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                stats id
                ''',
                'stats_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('trap-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                trap id
                ''',
                'trap_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('trap-strength', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                trap strength
                ''',
                'trap_strength',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('trap-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                trap string
                ''',
                'trap_string',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'trap-specific-stats-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData',
            False, 
            [
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                NPU number
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('trap-specific-stats-data', REFERENCE_LIST, 'TrapSpecificStatsData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData.TrapSpecificStatsData', 
                [], [], 
                '''                Filter by specific trap id
                ''',
                'trap_specific_stats_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'npu-number-for-trap-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas',
            False, 
            [
            _MetaInfoClassMember('npu-number-for-trap-data', REFERENCE_LIST, 'NpuNumberForTrapData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData', 
                [], [], 
                '''                All trap stats for a particular npu
                ''',
                'npu_number_for_trap_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'npu-number-for-trap-datas',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData.VoqStat' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData.VoqStat',
            False, 
            [
            _MetaInfoClassMember('gport-dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportDroppedBytes
                ''',
                'gport_dropped_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('gport-dropped-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportDroppedPkts
                ''',
                'gport_dropped_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('gport-received-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportReceivedBytes
                ''',
                'gport_received_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('gport-received-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportReceivedPkts
                ''',
                'gport_received_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData',
            False, 
            [
            _MetaInfoClassMember('base-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface handle
                ''',
                'base_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('connector-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                connector id
                ''',
                'connector_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('ifhandle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ifhandle
                ''',
                'ifhandle',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('is-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is inuse
                ''',
                'is_inuse',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is local port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-core', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                npu core
                ''',
                'npu_core',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                npu num
                ''',
                'npu_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('port-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                port num
                ''',
                'port_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('port-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                port speed
                ''',
                'port_speed',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('pp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pp port
                ''',
                'pp_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('sysport', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sysport
                ''',
                'sysport',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('voq-base', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                voq base
                ''',
                'voq_base',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('voq-stat', REFERENCE_LIST, 'VoqStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData.VoqStat', 
                [], [], 
                '''                voq stat
                ''',
                'voq_stat',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False, max_elements=8),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-base-stats-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber',
            False, 
            [
            _MetaInfoClassMember('npu-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Npu Number
                ''',
                'npu_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('voq-base-stats-data', REFERENCE_LIST, 'VoqBaseStatsData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData', 
                [], [], 
                '''                Voq Base Number for a particular voq
                ''',
                'voq_base_stats_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-base-number',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers',
            False, 
            [
            _MetaInfoClassMember('voq-base-number', REFERENCE_LIST, 'VoqBaseNumber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber', 
                [], [], 
                '''                Filter by npu number
                ''',
                'voq_base_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-base-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData.VoqStat' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData.VoqStat',
            False, 
            [
            _MetaInfoClassMember('gport-dropped-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportDroppedBytes
                ''',
                'gport_dropped_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('gport-dropped-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportDroppedPkts
                ''',
                'gport_dropped_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('gport-received-bytes', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportReceivedBytes
                ''',
                'gport_received_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('gport-received-pkts', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                GportReceivedPkts
                ''',
                'gport_received_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData',
            False, 
            [
            _MetaInfoClassMember('voq-data', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Handle
                ''',
                'voq_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('connector-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                connector id
                ''',
                'connector_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('ifhandle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ifhandle
                ''',
                'ifhandle',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('is-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is inuse
                ''',
                'is_inuse',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is local port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-core', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                npu core
                ''',
                'npu_core',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                npu num
                ''',
                'npu_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('port-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                port num
                ''',
                'port_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('port-speed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                port speed
                ''',
                'port_speed',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('pp-port', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pp port
                ''',
                'pp_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('sysport', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                sysport
                ''',
                'sysport',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('voq-base', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                voq base
                ''',
                'voq_base',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('voq-stat', REFERENCE_LIST, 'VoqStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData.VoqStat', 
                [], [], 
                '''                voq stat
                ''',
                'voq_stat',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False, max_elements=8),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-specific-stats-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData',
            False, 
            [
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Npu number
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('voq-specific-stats-data', REFERENCE_LIST, 'VoqSpecificStatsData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData', 
                [], [], 
                '''                Filter data by interface handle
                ''',
                'voq_specific_stats_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'npu-number-for-voq-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas',
            False, 
            [
            _MetaInfoClassMember('npu-number-for-voq-data', REFERENCE_LIST, 'NpuNumberForVoqData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData', 
                [], [], 
                '''                All voq stats for a particular npu
                ''',
                'npu_number_for_voq_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'npu-number-for-voq-datas',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber.VoqSpecificStatsDataClear' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber.VoqSpecificStatsDataClear',
            False, 
            [
            _MetaInfoClassMember('voq-data', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Handle
                ''',
                'voq_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('clear-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                clear status
                ''',
                'clear_status',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'voq-specific-stats-data-clear',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber',
            False, 
            [
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Npu number
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('voq-specific-stats-data-clear', REFERENCE_LIST, 'VoqSpecificStatsDataClear' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber.VoqSpecificStatsDataClear', 
                [], [], 
                '''                Filter data by interface handle
                ''',
                'voq_specific_stats_data_clear',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'clear-voq-data-for-npu-number',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers',
            False, 
            [
            _MetaInfoClassMember('clear-voq-data-for-npu-number', REFERENCE_LIST, 'ClearVoqDataForNpuNumber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber', 
                [], [], 
                '''                Npu id on which stats will be cleared
                ''',
                'clear_voq_data_for_npu_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'clear-voq-data-for-npu-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear.TrapSpecificStatsData' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear.TrapSpecificStatsData',
            False, 
            [
            _MetaInfoClassMember('trap-data', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Trap Number
                ''',
                'trap_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('clear-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                clear status
                ''',
                'clear_status',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'trap-specific-stats-data',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear',
            False, 
            [
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                NPU number
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('trap-specific-stats-data', REFERENCE_LIST, 'TrapSpecificStatsData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear.TrapSpecificStatsData', 
                [], [], 
                '''                Filter by specific trap id
                ''',
                'trap_specific_stats_data',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'npu-number-for-trap-data-clear',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears',
            False, 
            [
            _MetaInfoClassMember('npu-number-for-trap-data-clear', REFERENCE_LIST, 'NpuNumberForTrapDataClear' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear', 
                [], [], 
                '''                All trap stats for a particular npu
                ''',
                'npu_number_for_trap_data_clear',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'npu-number-for-trap-data-clears',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', True),
            _MetaInfoClassMember('clear-voq-data-for-npu-numbers', REFERENCE_CLASS, 'ClearVoqDataForNpuNumbers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers', 
                [], [], 
                '''                Clear voq ingress stats for all interfaces on
                particular npu
                ''',
                'clear_voq_data_for_npu_numbers',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-number-for-trap-data-clears', REFERENCE_CLASS, 'NpuNumberForTrapDataClears' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears', 
                [], [], 
                '''                Trap stats for all traps
                ''',
                'npu_number_for_trap_data_clears',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-number-for-trap-datas', REFERENCE_CLASS, 'NpuNumberForTrapDatas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas', 
                [], [], 
                '''                Trap stats for all traps
                ''',
                'npu_number_for_trap_datas',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('npu-number-for-voq-datas', REFERENCE_CLASS, 'NpuNumberForVoqDatas' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas', 
                [], [], 
                '''                DPA voq ingress stats for all interfaces
                ''',
                'npu_number_for_voq_datas',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('voq-base-number-stats-clears', REFERENCE_CLASS, 'VoqBaseNumberStatsClears' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears', 
                [], [], 
                '''                Clear DPA voq base stats 
                ''',
                'voq_base_number_stats_clears',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('voq-base-numbers', REFERENCE_CLASS, 'VoqBaseNumbers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers', 
                [], [], 
                '''                DPA voq base stats 
                ''',
                'voq_base_numbers',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats.Nodes' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes.Node', 
                [], [], 
                '''                DPA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa.Stats' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats.Nodes', 
                [], [], 
                '''                DPA data for available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
    'Dpa' : {
        'meta_info' : _MetaInfoClass('Dpa',
            False, 
            [
            _MetaInfoClassMember('resources', REFERENCE_CLASS, 'Resources' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Resources', 
                [], [], 
                '''                DPA Resources Data
                ''',
                'resources',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper', 'Dpa.Stats', 
                [], [], 
                '''                DPA voq data
                ''',
                'stats',
                'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-resources-oper',
            'dpa',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-resources-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_fretta_bcm_dpa_resources_oper'
        ),
    },
}
_meta_table['Dpa.Resources.Nodes.Node.TableDatas.TableData.NpuTblr']['meta_info'].parent =_meta_table['Dpa.Resources.Nodes.Node.TableDatas.TableData']['meta_info']
_meta_table['Dpa.Resources.Nodes.Node.TableDatas.TableData']['meta_info'].parent =_meta_table['Dpa.Resources.Nodes.Node.TableDatas']['meta_info']
_meta_table['Dpa.Resources.Nodes.Node.TableDatas']['meta_info'].parent =_meta_table['Dpa.Resources.Nodes.Node']['meta_info']
_meta_table['Dpa.Resources.Nodes.Node']['meta_info'].parent =_meta_table['Dpa.Resources.Nodes']['meta_info']
_meta_table['Dpa.Resources.Nodes']['meta_info'].parent =_meta_table['Dpa.Resources']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear.VoqBaseStatsClearData']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears.VoqBaseNumberStatsClear']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData.TrapSpecificStatsData']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas.NpuNumberForTrapData']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData.VoqStat']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseStatsData']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData.VoqStat']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData.VoqSpecificStatsData']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas.NpuNumberForVoqData']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber.VoqSpecificStatsDataClear']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers.ClearVoqDataForNpuNumber']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear.TrapSpecificStatsData']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears.NpuNumberForTrapDataClear']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumberStatsClears']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDatas']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForVoqDatas']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.ClearVoqDataForNpuNumbers']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.NpuNumberForTrapDataClears']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes']['meta_info']
_meta_table['Dpa.Stats.Nodes']['meta_info'].parent =_meta_table['Dpa.Stats']['meta_info']
_meta_table['Dpa.Resources']['meta_info'].parent =_meta_table['Dpa']['meta_info']
_meta_table['Dpa.Stats']['meta_info'].parent =_meta_table['Dpa']['meta_info']
