


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'opts-ea-bulk-create',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'opts-ea-bulk-update',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'dsp-ea-bulk-create',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'dsp-ea-bulk-update',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'laser-on-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'laser-off-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'wl-op-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'txpwr-op-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'cdmin-op-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'cdmax-op-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats',
            False, 
            [
            _MetaInfoClassMember('end', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                end
                ''',
                'end',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('start', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                start
                ''',
                'start',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('time-taken', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                time taken
                ''',
                'time_taken',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('worst-time', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                worst time
                ''',
                'worst_time',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'traffictype-op-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats.PortStat' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats.PortStat',
            False, 
            [
            _MetaInfoClassMember('cd-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                cd max
                ''',
                'cd_max',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('cd-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                cd min
                ''',
                'cd_min',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('cdmax-op-stats', REFERENCE_CLASS, 'CdmaxOpStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats', 
                [], [], 
                '''                cdmax op stats
                ''',
                'cdmax_op_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('cdmin-op-stats', REFERENCE_CLASS, 'CdminOpStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats', 
                [], [], 
                '''                cdmin op stats
                ''',
                'cdmin_op_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('laser-off-stats', REFERENCE_CLASS, 'LaserOffStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats', 
                [], [], 
                '''                laser off stats
                ''',
                'laser_off_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('laser-on-stats', REFERENCE_CLASS, 'LaserOnStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats', 
                [], [], 
                '''                laser on stats
                ''',
                'laser_on_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('laser-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                laser state
                ''',
                'laser_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('traffic-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                traffic type
                ''',
                'traffic_type',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('traffictype-op-stats', REFERENCE_CLASS, 'TraffictypeOpStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats', 
                [], [], 
                '''                traffictype op stats
                ''',
                'traffictype_op_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('tx-power', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                tx power
                ''',
                'tx_power',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('txpwr-op-stats', REFERENCE_CLASS, 'TxpwrOpStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats', 
                [], [], 
                '''                txpwr op stats
                ''',
                'txpwr_op_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('wavelength', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                wavelength
                ''',
                'wavelength',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('wl-op-stats', REFERENCE_CLASS, 'WlOpStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats', 
                [], [], 
                '''                wl op stats
                ''',
                'wl_op_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'port-stat',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.CoherentTimeStats' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.CoherentTimeStats',
            False, 
            [
            _MetaInfoClassMember('device-created', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                device created
                ''',
                'device_created',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('driver-init', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                driver init
                ''',
                'driver_init',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('driver-operational', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                driver operational
                ''',
                'driver_operational',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('dsp-controllers-created', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                dsp controllers created
                ''',
                'dsp_controllers_created',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('dsp-ea-bulk-create', REFERENCE_CLASS, 'DspEaBulkCreate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate', 
                [], [], 
                '''                dsp ea bulk create
                ''',
                'dsp_ea_bulk_create',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('dsp-ea-bulk-update', REFERENCE_CLASS, 'DspEaBulkUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate', 
                [], [], 
                '''                dsp ea bulk update
                ''',
                'dsp_ea_bulk_update',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('eth-intf-created', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                eth intf created
                ''',
                'eth_intf_created',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('optics-controllers-created', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                optics controllers created
                ''',
                'optics_controllers_created',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('opts-ea-bulk-create', REFERENCE_CLASS, 'OptsEaBulkCreate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate', 
                [], [], 
                '''                opts ea bulk create
                ''',
                'opts_ea_bulk_create',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('opts-ea-bulk-update', REFERENCE_CLASS, 'OptsEaBulkUpdate' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate', 
                [], [], 
                '''                opts ea bulk update
                ''',
                'opts_ea_bulk_update',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('port-stat', REFERENCE_LIST, 'PortStat' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats.PortStat', 
                [], [], 
                '''                port stat
                ''',
                'port_stat',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False, max_elements=6),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'coherent-time-stats',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.Devicemapping.DevMap' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.Devicemapping.DevMap',
            False, 
            [
            _MetaInfoClassMember('device-address', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Device address
                ''',
                'device_address',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('ifhandle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface handle
                ''',
                'ifhandle',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('intf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'intf_name',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'dev-map',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.Devicemapping' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.Devicemapping',
            False, 
            [
            _MetaInfoClassMember('dev-map', REFERENCE_LIST, 'DevMap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.Devicemapping.DevMap', 
                [], [], 
                '''                dev map
                ''',
                'dev_map',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False, max_elements=32),
            _MetaInfoClassMember('num-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dev map entries
                ''',
                'num_entries',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'devicemapping',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo',
            False, 
            [
            _MetaInfoClassMember('clei-code-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                CLEI code number
                ''',
                'clei_code_number',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('ctp-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ctp type
                ''',
                'ctp_type',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('date-code-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 10)], [], 
                '''                date code number
                ''',
                'date_code_number',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('description', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                description
                ''',
                'description',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('deviation', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                deviation
                ''',
                'deviation',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('module-firmware-committed-version-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                module firmware committed version number
                ''',
                'module_firmware_committed_version_number',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('module-firmware-running-version-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                module firmware running version number
                ''',
                'module_firmware_running_version_number',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('module-hardware-version-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                module hardware version number
                ''',
                'module_hardware_version_number',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('part-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                part number
                ''',
                'part_number',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('pid', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                pid
                ''',
                'pid',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('vendorname', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                vendorname
                ''',
                'vendorname',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('vid', ATTRIBUTE, 'str' , None, None, 
                [(0, 16)], [], 
                '''                vid
                ''',
                'vid',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'ctp-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData',
            False, 
            [
            _MetaInfoClassMember('admin-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                admin state
                ''',
                'admin_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('ifname', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                ifname
                ''',
                'ifname',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('intf-handle', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                intf handle
                ''',
                'intf_handle',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'eth-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo',
            False, 
            [
            _MetaInfoClassMember('eth-data', REFERENCE_LIST, 'EthData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData', 
                [], [], 
                '''                eth data
                ''',
                'eth_data',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False, max_elements=2),
            _MetaInfoClassMember('intf-count', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                intf count
                ''',
                'intf_count',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'interface-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.Coherenthealth.PortData' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.Coherenthealth.PortData',
            False, 
            [
            _MetaInfoClassMember('ctp-info', REFERENCE_CLASS, 'CtpInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo', 
                [], [], 
                '''                ctp info
                ''',
                'ctp_info',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('dsp-admin-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                dsp admin up
                ''',
                'dsp_admin_up',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('dsp-ctrl-created', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                dsp ctrl created
                ''',
                'dsp_ctrl_created',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('fp-port-idx', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                fp port idx
                ''',
                'fp_port_idx',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('has-pluggable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                has pluggable
                ''',
                'has_pluggable',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('interface-info', REFERENCE_CLASS, 'InterfaceInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo', 
                [], [], 
                '''                interface info
                ''',
                'interface_info',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('laser-op-rc', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                laser op rc
                ''',
                'laser_op_rc',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('laser-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                laser state
                ''',
                'laser_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('optics-admin-up', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                optics admin up
                ''',
                'optics_admin_up',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('optics-ctrl-created', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                optics ctrl created
                ''',
                'optics_ctrl_created',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('traffic-op-rc', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                traffic op rc
                ''',
                'traffic_op_rc',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('traffic-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                traffic type
                ''',
                'traffic_type',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('wavelength', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                wavelength
                ''',
                'wavelength',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('wlen-op-rc', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                wlen op rc
                ''',
                'wlen_op_rc',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'port-data',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.Coherenthealth' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.Coherenthealth',
            False, 
            [
            _MetaInfoClassMember('aipc-srvr-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                aipc srvr state
                ''',
                'aipc_srvr_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('board-type', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                board type
                ''',
                'board_type',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('denali-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                denali version
                ''',
                'denali_version',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('dsp-ea-conn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                dsp ea conn
                ''',
                'dsp_ea_conn',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('im-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                im state
                ''',
                'im_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('jlink-op', ATTRIBUTE, 'str' , None, None, 
                [(0, 1024)], [], 
                '''                jlink op
                ''',
                'jlink_op',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('morgoth-alive', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                morgoth alive
                ''',
                'morgoth_alive',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('morgoth-downloaded-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                morgoth downloaded version
                ''',
                'morgoth_downloaded_version',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('morgoth-golden-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                morgoth golden version
                ''',
                'morgoth_golden_version',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('morgoth-running-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                morgoth running version
                ''',
                'morgoth_running_version',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('optics-ea-conn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                optics ea conn
                ''',
                'optics_ea_conn',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('pm-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                pm state
                ''',
                'pm_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('port-data', REFERENCE_LIST, 'PortData' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.Coherenthealth.PortData', 
                [], [], 
                '''                port data
                ''',
                'port_data',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False, max_elements=6),
            _MetaInfoClassMember('prov-infra-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                prov infra state
                ''',
                'prov_infra_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('sdk-fpga-compatible', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                sdk fpga compatible
                ''',
                'sdk_fpga_compatible',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('sdk-version', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                sdk version
                ''',
                'sdk_version',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('sysdb-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                sysdb state
                ''',
                'sysdb_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('vether-state', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                vether state
                ''',
                'vether_state',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'coherenthealth',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry',
            False, 
            [
            _MetaInfoClassMember('diff', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics diff
                ''',
                'diff',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('fec', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics fec
                ''',
                'fec',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('intf-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'intf_name',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('modulation', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics modulation
                ''',
                'modulation',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('speed', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Optics speed
                ''',
                'speed',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'portmode-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node.PortModeAllInfo' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node.PortModeAllInfo',
            False, 
            [
            _MetaInfoClassMember('num-entries', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of dev map entries
                ''',
                'num_entries',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('portmode-entry', REFERENCE_LIST, 'PortmodeEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry', 
                [], [], 
                '''                portmode entry
                ''',
                'portmode_entry',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False, max_elements=32),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'port-mode-all-info',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes.Node' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes.Node',
            False, 
            [
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], ['([a-zA-Z0-9_]*\\d+/){1,2}([a-zA-Z0-9_]*\\d+)'], 
                '''                The node name
                ''',
                'node_name',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', True),
            _MetaInfoClassMember('coherent-time-stats', REFERENCE_CLASS, 'CoherentTimeStats' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.CoherentTimeStats', 
                [], [], 
                '''                Coherent driver performace information
                ''',
                'coherent_time_stats',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('coherenthealth', REFERENCE_CLASS, 'Coherenthealth' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.Coherenthealth', 
                [], [], 
                '''                Coherent node data for driver health
                ''',
                'coherenthealth',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('devicemapping', REFERENCE_CLASS, 'Devicemapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.Devicemapping', 
                [], [], 
                '''                Coherent node data for device _mapping
                ''',
                'devicemapping',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            _MetaInfoClassMember('port-mode-all-info', REFERENCE_CLASS, 'PortModeAllInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node.PortModeAllInfo', 
                [], [], 
                '''                PortMode all operational data
                ''',
                'port_mode_all_info',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent.Nodes' : {
        'meta_info' : _MetaInfoClass('Coherent.Nodes',
            False, 
            [
            _MetaInfoClassMember('node', REFERENCE_LIST, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes.Node', 
                [], [], 
                '''                Coherent discovery operational data for a
                particular node
                ''',
                'node',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'nodes',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
    'Coherent' : {
        'meta_info' : _MetaInfoClass('Coherent',
            False, 
            [
            _MetaInfoClassMember('nodes', REFERENCE_CLASS, 'Nodes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper', 'Coherent.Nodes', 
                [], [], 
                '''                Coherent list of nodes
                ''',
                'nodes',
                'Cisco-IOS-XR-ncs5500-coherent-node-oper', False),
            ],
            'Cisco-IOS-XR-ncs5500-coherent-node-oper',
            'coherent',
            _yang_ns._namespaces['Cisco-IOS-XR-ncs5500-coherent-node-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_ncs5500_coherent_node_oper'
        ),
    },
}
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOnStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.LaserOffStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.WlOpStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.TxpwrOpStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdminOpStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.CdmaxOpStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat.TraffictypeOpStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkCreate']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.OptsEaBulkUpdate']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkCreate']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.DspEaBulkUpdate']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats.PortStat']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.CoherentTimeStats']['meta_info']
_meta_table['Coherent.Nodes.Node.Devicemapping.DevMap']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.Devicemapping']['meta_info']
_meta_table['Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo.EthData']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo']['meta_info']
_meta_table['Coherent.Nodes.Node.Coherenthealth.PortData.CtpInfo']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.Coherenthealth.PortData']['meta_info']
_meta_table['Coherent.Nodes.Node.Coherenthealth.PortData.InterfaceInfo']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.Coherenthealth.PortData']['meta_info']
_meta_table['Coherent.Nodes.Node.Coherenthealth.PortData']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.Coherenthealth']['meta_info']
_meta_table['Coherent.Nodes.Node.PortModeAllInfo.PortmodeEntry']['meta_info'].parent =_meta_table['Coherent.Nodes.Node.PortModeAllInfo']['meta_info']
_meta_table['Coherent.Nodes.Node.CoherentTimeStats']['meta_info'].parent =_meta_table['Coherent.Nodes.Node']['meta_info']
_meta_table['Coherent.Nodes.Node.Devicemapping']['meta_info'].parent =_meta_table['Coherent.Nodes.Node']['meta_info']
_meta_table['Coherent.Nodes.Node.Coherenthealth']['meta_info'].parent =_meta_table['Coherent.Nodes.Node']['meta_info']
_meta_table['Coherent.Nodes.Node.PortModeAllInfo']['meta_info'].parent =_meta_table['Coherent.Nodes.Node']['meta_info']
_meta_table['Coherent.Nodes.Node']['meta_info'].parent =_meta_table['Coherent.Nodes']['meta_info']
_meta_table['Coherent.Nodes']['meta_info'].parent =_meta_table['Coherent']['meta_info']
