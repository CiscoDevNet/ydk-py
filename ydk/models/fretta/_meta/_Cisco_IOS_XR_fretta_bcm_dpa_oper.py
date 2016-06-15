


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.models import _yang_ns

_meta_table = {
    'Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks.AllTrapsStatsDataBlock' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks.AllTrapsStatsDataBlock',
            False, 
            [
            _MetaInfoClassMember('data-block-number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Data Block Number
                ''',
                'data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('encap-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                encap id
                ''',
                'encap_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('fec-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                fec id
                ''',
                'fec_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                gport
                ''',
                'gport',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                id
                ''',
                'id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('mc-group', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                mc group
                ''',
                'mc_group',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                npu id
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                offset
                ''',
                'offset',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('packet-accepted', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                packet accepted
                ''',
                'packet_accepted',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('packet-dropped', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                packet dropped
                ''',
                'packet_dropped',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                policer id
                ''',
                'policer_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                priority
                ''',
                'priority',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('stats-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                stats id
                ''',
                'stats_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('trap-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                trap id
                ''',
                'trap_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('trap-strength', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                trap strength
                ''',
                'trap_strength',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('trap-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                trap string
                ''',
                'trap_string',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'all-traps-stats-data-block',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks',
            False, 
            [
            _MetaInfoClassMember('all-traps-stats-data-block', REFERENCE_LIST, 'AllTrapsStatsDataBlock' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks.AllTrapsStatsDataBlock', 
                [], [], 
                '''                Indicates the data block number for trap
                stats data block and cannot be used to
                extract a single data block
                ''',
                'all_traps_stats_data_block',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'all-traps-stats-data-blocks',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock.TrapDataBlockNumber' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock.TrapDataBlockNumber',
            False, 
            [
            _MetaInfoClassMember('data-block-number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Data Block Number
                ''',
                'data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('encap-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                encap id
                ''',
                'encap_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('fec-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                fec id
                ''',
                'fec_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                gport
                ''',
                'gport',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                id
                ''',
                'id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('mc-group', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                mc group
                ''',
                'mc_group',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-id', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                npu id
                ''',
                'npu_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('offset', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                offset
                ''',
                'offset',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('packet-accepted', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                packet accepted
                ''',
                'packet_accepted',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('packet-dropped', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                packet dropped
                ''',
                'packet_dropped',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('policer-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                policer id
                ''',
                'policer_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                priority
                ''',
                'priority',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('stats-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                stats id
                ''',
                'stats_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('trap-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                trap id
                ''',
                'trap_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('trap-strength', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                trap strength
                ''',
                'trap_strength',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('trap-string', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                trap string
                ''',
                'trap_string',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'trap-data-block-number',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock',
            False, 
            [
            _MetaInfoClassMember('trapid', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Trap number
                ''',
                'trapid',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('trap-data-block-number', REFERENCE_LIST, 'TrapDataBlockNumber' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock.TrapDataBlockNumber', 
                [], [], 
                '''                Indicates the data block number for a
                particular trap and cannot be used to
                extract a particular block
                ''',
                'trap_data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'single-trap-stats-data-block',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks',
            False, 
            [
            _MetaInfoClassMember('single-trap-stats-data-block', REFERENCE_LIST, 'SingleTrapStatsDataBlock' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock', 
                [], [], 
                '''                Trap number
                ''',
                'single_trap_stats_data_block',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'single-trap-stats-data-blocks',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock.VoqStat' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock.VoqStat',
            False, 
            [
            _MetaInfoClassMember('gport-dropped-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportDroppedBytes
                ''',
                'gport_dropped_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-dropped-pkts', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportDroppedPkts
                ''',
                'gport_dropped_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-received-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportReceivedBytes
                ''',
                'gport_received_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-received-pkts', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportReceivedPkts
                ''',
                'gport_received_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'voq-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock',
            False, 
            [
            _MetaInfoClassMember('data-block-number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Data Block Number
                ''',
                'data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('connector-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                connector id
                ''',
                'connector_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('ifhandle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ifhandle
                ''',
                'ifhandle',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('is-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is inuse
                ''',
                'is_inuse',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is local port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-core', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                npu core
                ''',
                'npu_core',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                npu num
                ''',
                'npu_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('port-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                port num
                ''',
                'port_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('port-speed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                port speed
                ''',
                'port_speed',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('pp-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                pp port
                ''',
                'pp_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('sysport', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                sysport
                ''',
                'sysport',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('voq-base', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                voq base
                ''',
                'voq_base',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('voq-stat', REFERENCE_LIST, 'VoqStat' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock.VoqStat', 
                [], [], 
                '''                voq stat
                ''',
                'voq_stat',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False, max_elements=8),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'all-voq-stats-data-block',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks',
            False, 
            [
            _MetaInfoClassMember('all-voq-stats-data-block', REFERENCE_LIST, 'AllVoqStatsDataBlock' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock', 
                [], [], 
                '''                Indicate the data block number of the voq
                stats data block and cannot be used to
                extract a single data block
                ''',
                'all_voq_stats_data_block',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'all-voq-stats-data-blocks',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber.VoqStat' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber.VoqStat',
            False, 
            [
            _MetaInfoClassMember('gport-dropped-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportDroppedBytes
                ''',
                'gport_dropped_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-dropped-pkts', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportDroppedPkts
                ''',
                'gport_dropped_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-received-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportReceivedBytes
                ''',
                'gport_received_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-received-pkts', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportReceivedPkts
                ''',
                'gport_received_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'voq-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber',
            False, 
            [
            _MetaInfoClassMember('data-block-number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Data Block Number
                ''',
                'data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('connector-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                connector id
                ''',
                'connector_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('ifhandle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ifhandle
                ''',
                'ifhandle',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('is-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is inuse
                ''',
                'is_inuse',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is local port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-core', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                npu core
                ''',
                'npu_core',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                npu num
                ''',
                'npu_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('port-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                port num
                ''',
                'port_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('port-speed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                port speed
                ''',
                'port_speed',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('pp-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                pp port
                ''',
                'pp_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('sysport', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                sysport
                ''',
                'sysport',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('voq-base', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                voq base
                ''',
                'voq_base',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('voq-stat', REFERENCE_LIST, 'VoqStat' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber.VoqStat', 
                [], [], 
                '''                voq stat
                ''',
                'voq_stat',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False, max_elements=8),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'voq-base-data-block-number',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber',
            False, 
            [
            _MetaInfoClassMember('base-number', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Interface handle
                ''',
                'base_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('voq-base-data-block-number', REFERENCE_LIST, 'VoqBaseDataBlockNumber' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber', 
                [], [], 
                '''                Indicates the data block number for a
                particular voq base and cannot be used to
                extract a particular block number
                ''',
                'voq_base_data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'voq-base-number',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.VoqBaseNumbers' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.VoqBaseNumbers',
            False, 
            [
            _MetaInfoClassMember('voq-base-number', REFERENCE_LIST, 'VoqBaseNumber' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber', 
                [], [], 
                '''                Voq Base Number for a particular voq
                ''',
                'voq_base_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'voq-base-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber.VoqStat' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber.VoqStat',
            False, 
            [
            _MetaInfoClassMember('gport-dropped-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportDroppedBytes
                ''',
                'gport_dropped_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-dropped-pkts', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportDroppedPkts
                ''',
                'gport_dropped_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-received-bytes', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportReceivedBytes
                ''',
                'gport_received_bytes',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('gport-received-pkts', ATTRIBUTE, 'long' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                GportReceivedPkts
                ''',
                'gport_received_pkts',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'voq-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber',
            False, 
            [
            _MetaInfoClassMember('data-block-number', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                Data Block Number
                ''',
                'data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('connector-id', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                connector id
                ''',
                'connector_id',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('ifhandle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ifhandle
                ''',
                'ifhandle',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('is-inuse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is inuse
                ''',
                'is_inuse',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('is-local-port', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                is local port
                ''',
                'is_local_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-core', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                npu core
                ''',
                'npu_core',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('npu-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                npu num
                ''',
                'npu_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('port-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                port num
                ''',
                'port_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('port-speed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                port speed
                ''',
                'port_speed',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('pp-port', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                pp port
                ''',
                'pp_port',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('rack-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                rack num
                ''',
                'rack_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('slot-num', ATTRIBUTE, 'int' , None, None, 
                [(0, 255)], [], 
                '''                slot num
                ''',
                'slot_num',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('sysport', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                sysport
                ''',
                'sysport',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('voq-base', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                voq base
                ''',
                'voq_base',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('voq-stat', REFERENCE_LIST, 'VoqStat' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber.VoqStat', 
                [], [], 
                '''                voq stat
                ''',
                'voq_stat',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False, max_elements=8),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'voq-stats-data-block-number',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock',
            False, 
            [
            _MetaInfoClassMember('interface-handle', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Interface handle
                ''',
                'interface_handle',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('voq-stats-data-block-number', REFERENCE_LIST, 'VoqStatsDataBlockNumber' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber', 
                [], [], 
                '''                Indicates the data block number for a
                particular voq and cannot be used to
                extract a single element
                ''',
                'voq_stats_data_block_number',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'single-voq-stats-data-block',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks',
            False, 
            [
            _MetaInfoClassMember('single-voq-stats-data-block', REFERENCE_LIST, 'SingleVoqStatsDataBlock' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock', 
                [], [], 
                '''                Interface handle for a particular voq
                ''',
                'single_voq_stats_data_block',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'single-voq-stats-data-blocks',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                Node ID
                ''',
                'node_name',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', True),
            _MetaInfoClassMember('all-traps-stats-data-blocks', REFERENCE_CLASS, 'AllTrapsStatsDataBlocks' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks', 
                [], [], 
                '''                DPA trap stats 
                ''',
                'all_traps_stats_data_blocks',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('all-voq-stats-data-blocks', REFERENCE_CLASS, 'AllVoqStatsDataBlocks' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks', 
                [], [], 
                '''                DPA voq ingress stats 
                ''',
                'all_voq_stats_data_blocks',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('single-trap-stats-data-blocks', REFERENCE_CLASS, 'SingleTrapStatsDataBlocks' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks', 
                [], [], 
                '''                DPA stats for a single trap
                ''',
                'single_trap_stats_data_blocks',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('single-voq-stats-data-blocks', REFERENCE_CLASS, 'SingleVoqStatsDataBlocks' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks', 
                [], [], 
                '''                DPA voq ingress stats for a single interface
                ''',
                'single_voq_stats_data_blocks',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            _MetaInfoClassMember('voq-base-numbers', REFERENCE_CLASS, 'VoqBaseNumbers' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node.VoqBaseNumbers', 
                [], [], 
                '''                DPA voq base stats 
                ''',
                'voq_base_numbers',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats.Nodes' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes.Node', 
                [], [], 
                '''                DPA operational data for a particular node
                ''',
                'node',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa.Stats' : {
        'meta_info' : _MetaInfoClass('Dpa.Stats',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats.Nodes', 
                [], [], 
                '''                DPA data for available nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'stats',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
    'Dpa' : {
        'meta_info' : _MetaInfoClass('Dpa',
            False, 
            [
            _MetaInfoClassMember('stats', REFERENCE_CLASS, 'Stats' , 'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper', 'Dpa.Stats', 
                [], [], 
                '''                DPA voq data
                ''',
                'stats',
                'Cisco-IOS-XR-fretta-bcm-dpa-oper', False),
            ],
            'Cisco-IOS-XR-fretta-bcm-dpa-oper',
            'dpa',
            _yang_ns._namespaces['Cisco-IOS-XR-fretta-bcm-dpa-oper'],
        'ydk.models.fretta.Cisco_IOS_XR_fretta_bcm_dpa_oper'
        ),
    },
}
_meta_table['Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks.AllTrapsStatsDataBlock']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock.TrapDataBlockNumber']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks.SingleTrapStatsDataBlock']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock.VoqStat']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks.AllVoqStatsDataBlock']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber.VoqStat']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber.VoqBaseDataBlockNumber']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers.VoqBaseNumber']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber.VoqStat']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock.VoqStatsDataBlockNumber']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks.SingleVoqStatsDataBlock']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.AllTrapsStatsDataBlocks']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.SingleTrapStatsDataBlocks']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.AllVoqStatsDataBlocks']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.VoqBaseNumbers']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node.SingleVoqStatsDataBlocks']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes.Node']['meta_info']
_meta_table['Dpa.Stats.Nodes.Node']['meta_info'].parent =_meta_table['Dpa.Stats.Nodes']['meta_info']
_meta_table['Dpa.Stats.Nodes']['meta_info'].parent =_meta_table['Dpa.Stats']['meta_info']
_meta_table['Dpa.Stats']['meta_info'].parent =_meta_table['Dpa']['meta_info']
