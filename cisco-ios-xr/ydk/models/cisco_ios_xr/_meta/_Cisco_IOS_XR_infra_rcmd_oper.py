


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RcmdShowIntfEventEnum' : _MetaInfoEnum('RcmdShowIntfEventEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'create':'create',
            'delete':'delete',
            'link-up':'link_up',
            'link-down':'link_down',
            'primary-address':'primary_address',
            'secondary-address':'secondary_address',
            'ipv6-link-local-address':'ipv6_link_local_address',
            'ipv6-global-address':'ipv6_global_address',
            'mtu':'mtu',
            'band-width':'band_width',
            'ldp-sync':'ldp_sync',
            'forward-reference':'forward_reference',
            'ldp-no-sync':'ldp_no_sync',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowInstStateEnum' : _MetaInfoEnum('RcmdShowInstStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'unknown':'unknown',
            'active':'active',
            'in-active':'in_active',
            'na':'na',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdLsChangeEnum' : _MetaInfoEnum('RcmdLsChangeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'new':'new',
            'delete':'delete',
            'modify':'modify',
            'noop':'noop',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowRoutePathChangeEnum' : _MetaInfoEnum('RcmdShowRoutePathChangeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'primary':'primary',
            'backup':'backup',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowLdpConvStateEnum' : _MetaInfoEnum('RcmdShowLdpConvStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'not-full':'not_full',
            'fully-covered':'fully_covered',
            'coverage-above-threshold':'coverage_above_threshold',
            'coverage-below-threshold':'coverage_below_threshold',
            'coverage-flapping':'coverage_flapping',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowLdpNeighbourStatusEnum' : _MetaInfoEnum('RcmdShowLdpNeighbourStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'down':'down',
            'up':'up',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdBagEnableDisableEnum' : _MetaInfoEnum('RcmdBagEnableDisableEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'disable':'disable',
            'enable':'enable',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdSpfStateEnum' : _MetaInfoEnum('RcmdSpfStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'complete':'complete',
            'in-complete':'in_complete',
            'collecting':'collecting',
            'no-route-change':'no_route_change',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdIsisLvlEnum' : _MetaInfoEnum('RcmdIsisLvlEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'l1':'l1',
            'l2':'l2',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdLdpEventEnum' : _MetaInfoEnum('RcmdLdpEventEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'neighbor':'neighbor',
            'adjacency':'adjacency',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowCompIdEnum' : _MetaInfoEnum('RcmdShowCompIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'ospf':'ospf',
            'isis':'isis',
            'un-known':'un_known',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdPriorityLevelEnum' : _MetaInfoEnum('RcmdPriorityLevelEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'critical':'critical',
            'high':'high',
            'medium':'medium',
            'low':'low',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowNodeEnum' : _MetaInfoEnum('RcmdShowNodeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'unknown':'unknown',
            'lc':'lc',
            'rp':'rp',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdProtocolIdEnum' : _MetaInfoEnum('RcmdProtocolIdEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'ospf':'ospf',
            'isis':'isis',
            'na':'na',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdIsisSpfEnum' : _MetaInfoEnum('RcmdIsisSpfEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'full':'full',
            'incremental':'incremental',
            'next-hop':'next_hop',
            'partial-route':'partial_route',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowIpfrrLfaEnum' : _MetaInfoEnum('RcmdShowIpfrrLfaEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'none':'none',
            'local':'local',
            'remote':'remote',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowMemEnum' : _MetaInfoEnum('RcmdShowMemEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'standard':'standard',
            'chunk':'chunk',
            'edm':'edm',
            'string':'string',
            'static':'static',
            'unknown':'unknown',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowRouteEnum' : _MetaInfoEnum('RcmdShowRouteEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'ospf':'ospf',
            'intra':'intra',
            'inter':'inter',
            'ext-1':'ext_1',
            'ext-2':'ext_2',
            'nssa-1':'nssa_1',
            'nssa-2':'nssa_2',
            'isis':'isis',
            'l1-summary':'l1_summary',
            'l1':'l1',
            'l2-summary':'l2_summary',
            'l2':'l2',
            'inter-area-summary':'inter_area_summary',
            'inter-area':'inter_area',
            'default-attached':'default_attached',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdLsaEnum' : _MetaInfoEnum('RcmdLsaEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'unknown':'unknown',
            'router':'router',
            'network':'network',
            'summary':'summary',
            'asbr':'asbr',
            'external':'external',
            'multicast':'multicast',
            'nssa':'nssa',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowPrcsStateEnum' : _MetaInfoEnum('RcmdShowPrcsStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'success':'success',
            'cpu':'cpu',
            'memory':'memory',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdBoolYesNoEnum' : _MetaInfoEnum('RcmdBoolYesNoEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'no':'no',
            'yes':'yes',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdBagEnblDsblEnum' : _MetaInfoEnum('RcmdBagEnblDsblEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'dsbl':'dsbl',
            'enbl':'enbl',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdLinecardSpeedEnum' : _MetaInfoEnum('RcmdLinecardSpeedEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'other':'other',
            'fastest':'fastest',
            'slowest':'slowest',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdShowLdpSessionStateEnum' : _MetaInfoEnum('RcmdShowLdpSessionStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'gr-down':'gr_down',
            'gr-converging':'gr_converging',
            'establishing':'establishing',
            'converging':'converging',
            'converged':'converged',
            'retrying':'retrying',
            'total':'total',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'RcmdChangeEnum' : _MetaInfoEnum('RcmdChangeEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper',
        {
            'none':'none',
            'add':'add',
            'delete':'delete',
            'modify':'modify',
            'no-change':'no_change',
        }, 'Cisco-IOS-XR-infra-rcmd-oper', _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper']),
    'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic',
            False, 
            [
            _MetaInfoClassMember('below-threshold', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Covearge is below Configured Threshold
                ''',
                'below_threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('local-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local LFA Coverage in percentage
                ''',
                'local_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote LFA Coverage in percentage
                ''',
                'remote_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'primary-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode',
            False, 
            [
            _MetaInfoClassMember('in-use-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inuse time of the Remote Node (eg: Apr 24 13:16
                :04.961)
                ''',
                'in_use_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths protected by this Remote Node
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('primary-path', REFERENCE_LIST, 'PrimaryPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath', 
                [], [], 
                '''                Protected Primary Paths
                ''',
                'primary_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote-LFA Node ID
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific IP-FRR Event
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('completed-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Completed reference SPF Run Number
                ''',
                'completed_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage for all priorities
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration for the calculation (in milliseconds)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Event ID
                ''',
                'event_id_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-statistic', REFERENCE_LIST, 'IpfrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic', 
                [], [], 
                '''                IP-Frr Statistics categorized by priority
                ''',
                'ipfrr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node', REFERENCE_LIST, 'RemoteNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode', 
                [], [], 
                '''                Remote Node Information
                ''',
                'remote_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time-offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start Time offset from trigger time (in
                milliseconds)
                ''',
                'start_time_offset',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Routes for all priorities
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Triggered reference SPF Run Number
                ''',
                'trigger_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time  (eg: Apr 24 13:16:04.961)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Waiting Time (in milliseconds)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries',
            False, 
            [
            _MetaInfoClassMember('ipfrr-event-summary', REFERENCE_LIST, 'IpfrrEventSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary', 
                [], [], 
                '''                IP-FRR Event data
                ''',
                'ipfrr_event_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic',
            False, 
            [
            _MetaInfoClassMember('prefix-info', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Events with Prefix
                ''',
                'prefix_info',
                'Cisco-IOS-XR-infra-rcmd-oper', True, [
                    _MetaInfoClassMember('prefix-info', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Events with Prefix
                        ''',
                        'prefix_info',
                        'Cisco-IOS-XR-infra-rcmd-oper', True),
                    _MetaInfoClassMember('prefix-info', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Events with Prefix
                        ''',
                        'prefix_info',
                        'Cisco-IOS-XR-infra-rcmd-oper', True),
                ]),
            _MetaInfoClassMember('add-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times route gets Added
                ''',
                'add_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('critical-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under Critical Priority
                ''',
                'critical_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('delete-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times route gets Deleted
                ''',
                'delete_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('high-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under High Priority
                ''',
                'high_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Last event Add/Delete
                ''',
                'last_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Known Cost
                ''',
                'last_cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-event-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last event trigger time
                ''',
                'last_event_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Last event processed priority
                ''',
                'last_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Last event Route Type
                ''',
                'last_route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('low-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under Low Priority
                ''',
                'low_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('medium-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under Medium Priority
                ''',
                'medium_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modify-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times route gets Deleted
                ''',
                'modify_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times threshold got exceeded
                ''',
                'threshold_exceed_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventStatistics',
            False, 
            [
            _MetaInfoClassMember('prefix-event-statistic', REFERENCE_LIST, 'PrefixEventStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic', 
                [], [], 
                '''                Prefix Event statistics
                ''',
                'prefix_event_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of complete SPF calculation (in ss
                .msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('is-data-complete', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the event has all information
                ''',
                'is_data_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_LIST, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary', 
                [], [], 
                '''                Convergence information summary on per-priority
                basis
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start time (offset from event trigger time in ss
                .msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'RcmdSpfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdSpfStateEnum', 
                [], [], 
                '''                SPF state
                ''',
                'state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-dijkstra-runs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of Dijkstra runs
                ''',
                'total_dijkstra_runs',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-inter-area-and-external-batches', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of inter-area/external computation
                batches
                ''',
                'total_inter_area_and_external_batches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-type12lsa-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of Type 1/2 LSA changes processed
                ''',
                'total_type12lsa_changes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-type357lsa-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of Type 3/5/7 LSA changes processed
                ''',
                'total_type357lsa_changes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time (in hh:mm:ss.msec)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', REFERENCE_CLASS, 'LdpEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter', 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', REFERENCE_CLASS, 'LdpExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpExit', 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', REFERENCE_CLASS, 'LsdEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter', 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', REFERENCE_CLASS, 'LsdExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdExit', 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', REFERENCE_CLASS, 'RiBv4Enter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter', 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', REFERENCE_CLASS, 'RiBv4Exit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit', 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', REFERENCE_CLASS, 'RiBv4Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute', 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', REFERENCE_CLASS, 'RouteOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin', 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'convergence-timeline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksAdded' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksAdded',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-added',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksDeleted' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksDeleted',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-deleted',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority',
            False, 
            [
            _MetaInfoClassMember('convergence-timeline', REFERENCE_LIST, 'ConvergenceTimeline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline', 
                [], [], 
                '''                Convergence timeline details
                ''',
                'convergence_timeline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-added', REFERENCE_LIST, 'LeafNetworksAdded' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksAdded', 
                [], [], 
                '''                List of Leaf Networks Added
                ''',
                'leaf_networks_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-deleted', REFERENCE_LIST, 'LeafNetworksDeleted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksDeleted', 
                [], [], 
                '''                List of Leaf Networks Deleted
                ''',
                'leaf_networks_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_CLASS, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary', 
                [], [], 
                '''                Summary of the priority
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun',
            False, 
            [
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID
                ''',
                'area_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('dijkstra-run-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Area Dijkstra run number
                ''',
                'dijkstra_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of Dijktra calculation (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.LsaProcessed', 
                [], [], 
                '''                List of type 1/2 LSA changes processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority', 
                [], [], 
                '''                Convergence information on per-priority basis
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start time (offset from event trigger time in ss
                .msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.TriggerLsa', 
                [], [], 
                '''                LSA that triggered the Dijkstra run
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time (in hh:mm:ss.msec)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wait time (offset from event trigger time in ss
                .msec)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'dijkstra-run',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type3ls-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Type 3 LSA
                ''',
                'type3ls_as',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type4ls-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Type 4 LSA
                ''',
                'type4ls_as',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type57ls-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Type 5/7 LSA
                ''',
                'type57ls_as',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', REFERENCE_CLASS, 'LdpEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter', 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', REFERENCE_CLASS, 'LdpExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit', 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', REFERENCE_CLASS, 'LsdEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter', 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', REFERENCE_CLASS, 'LsdExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit', 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', REFERENCE_CLASS, 'RiBv4Enter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter', 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', REFERENCE_CLASS, 'RiBv4Exit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit', 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', REFERENCE_CLASS, 'RiBv4Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute', 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', REFERENCE_CLASS, 'RouteOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin', 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'convergence-timeline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksAdded' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksAdded',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-added',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksDeleted' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksDeleted',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-deleted',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority',
            False, 
            [
            _MetaInfoClassMember('convergence-timeline', REFERENCE_LIST, 'ConvergenceTimeline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline', 
                [], [], 
                '''                Convergence timeline details
                ''',
                'convergence_timeline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-added', REFERENCE_LIST, 'LeafNetworksAdded' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksAdded', 
                [], [], 
                '''                List of Leaf Networks Added
                ''',
                'leaf_networks_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-deleted', REFERENCE_LIST, 'LeafNetworksDeleted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksDeleted', 
                [], [], 
                '''                List of Leaf Networks Deleted
                ''',
                'leaf_networks_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_CLASS, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary', 
                [], [], 
                '''                Summary of the priority
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority', 
                [], [], 
                '''                Convergence information on a per-priority basis
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'inter-area-and-external',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary',
            False, 
            [
            _MetaInfoClassMember('spf-run-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific SPF run
                ''',
                'spf_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('dijkstra-run', REFERENCE_LIST, 'DijkstraRun' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun', 
                [], [], 
                '''                List of Dijkstra runs
                ''',
                'dijkstra_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-and-external', REFERENCE_LIST, 'InterAreaAndExternal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal', 
                [], [], 
                '''                Inter-area & external calculation information
                ''',
                'inter_area_and_external',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-summary', REFERENCE_CLASS, 'SpfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary', 
                [], [], 
                '''                SPF summary information
                ''',
                'spf_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunSummaries',
            False, 
            [
            _MetaInfoClassMember('spf-run-summary', REFERENCE_LIST, 'SpfRunSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary', 
                [], [], 
                '''                SPF Event data
                ''',
                'spf_run_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic',
            False, 
            [
            _MetaInfoClassMember('below-threshold', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Covearge is below Configured Threshold
                ''',
                'below_threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('local-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local LFA Coverage in percentage
                ''',
                'local_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote LFA Coverage in percentage
                ''',
                'remote_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'primary-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode',
            False, 
            [
            _MetaInfoClassMember('in-use-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inuse time of the Remote Node (eg: Apr 24 13:16
                :04.961)
                ''',
                'in_use_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths protected by this Remote Node
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('primary-path', REFERENCE_LIST, 'PrimaryPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath', 
                [], [], 
                '''                Protected Primary Paths
                ''',
                'primary_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote-LFA Node ID
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific IP-FRR Event
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('completed-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Completed reference SPF Run Number
                ''',
                'completed_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage for all priorities
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration for the calculation (in milliseconds)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Event ID
                ''',
                'event_id_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-statistic', REFERENCE_LIST, 'IpfrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic', 
                [], [], 
                '''                IP-Frr Statistics categorized by priority
                ''',
                'ipfrr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node', REFERENCE_LIST, 'RemoteNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode', 
                [], [], 
                '''                Remote Node Information
                ''',
                'remote_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time-offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start Time offset from trigger time (in
                milliseconds)
                ''',
                'start_time_offset',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Routes for all priorities
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Triggered reference SPF Run Number
                ''',
                'trigger_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time  (eg: Apr 24 13:16:04.961)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Waiting Time (in milliseconds)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-offline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines',
            False, 
            [
            _MetaInfoClassMember('ipfrr-event-offline', REFERENCE_LIST, 'IpfrrEventOffline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline', 
                [], [], 
                '''                Offline operational data for particular OSPF
                IP-FRR Event
                ''',
                'ipfrr_event_offline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-offlines',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of complete SPF calculation (in ss
                .msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('is-data-complete', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the event has all information
                ''',
                'is_data_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_LIST, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary', 
                [], [], 
                '''                Convergence information summary on per-priority
                basis
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start time (offset from event trigger time in ss
                .msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'RcmdSpfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdSpfStateEnum', 
                [], [], 
                '''                SPF state
                ''',
                'state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-dijkstra-runs', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of Dijkstra runs
                ''',
                'total_dijkstra_runs',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-inter-area-and-external-batches', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of inter-area/external computation
                batches
                ''',
                'total_inter_area_and_external_batches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-type12lsa-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of Type 1/2 LSA changes processed
                ''',
                'total_type12lsa_changes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-type357lsa-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of Type 3/5/7 LSA changes processed
                ''',
                'total_type357lsa_changes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time (in hh:mm:ss.msec)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', REFERENCE_CLASS, 'LdpEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter', 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', REFERENCE_CLASS, 'LdpExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpExit', 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', REFERENCE_CLASS, 'LsdEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter', 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', REFERENCE_CLASS, 'LsdExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdExit', 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', REFERENCE_CLASS, 'RiBv4Enter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter', 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', REFERENCE_CLASS, 'RiBv4Exit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit', 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', REFERENCE_CLASS, 'RiBv4Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute', 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', REFERENCE_CLASS, 'RouteOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin', 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'convergence-timeline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksAdded' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksAdded',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-added',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksDeleted' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksDeleted',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-deleted',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority',
            False, 
            [
            _MetaInfoClassMember('convergence-timeline', REFERENCE_LIST, 'ConvergenceTimeline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline', 
                [], [], 
                '''                Convergence timeline details
                ''',
                'convergence_timeline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-added', REFERENCE_LIST, 'LeafNetworksAdded' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksAdded', 
                [], [], 
                '''                List of Leaf Networks Added
                ''',
                'leaf_networks_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-deleted', REFERENCE_LIST, 'LeafNetworksDeleted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksDeleted', 
                [], [], 
                '''                List of Leaf Networks Deleted
                ''',
                'leaf_networks_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_CLASS, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary', 
                [], [], 
                '''                Summary of the priority
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun',
            False, 
            [
            _MetaInfoClassMember('area-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Area ID
                ''',
                'area_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('dijkstra-run-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Area Dijkstra run number
                ''',
                'dijkstra_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of Dijktra calculation (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.LsaProcessed', 
                [], [], 
                '''                List of type 1/2 LSA changes processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority', 
                [], [], 
                '''                Convergence information on per-priority basis
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start time (offset from event trigger time in ss
                .msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.TriggerLsa', 
                [], [], 
                '''                LSA that triggered the Dijkstra run
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time (in hh:mm:ss.msec)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wait time (offset from event trigger time in ss
                .msec)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'dijkstra-run',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type3ls-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Type 3 LSA
                ''',
                'type3ls_as',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type4ls-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Type 4 LSA
                ''',
                'type4ls_as',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type57ls-as', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Type 5/7 LSA
                ''',
                'type57ls_as',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', REFERENCE_CLASS, 'LdpEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter', 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', REFERENCE_CLASS, 'LdpExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit', 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', REFERENCE_CLASS, 'LsdEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter', 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', REFERENCE_CLASS, 'LsdExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit', 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', REFERENCE_CLASS, 'RiBv4Enter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter', 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', REFERENCE_CLASS, 'RiBv4Exit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit', 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', REFERENCE_CLASS, 'RiBv4Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute', 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', REFERENCE_CLASS, 'RouteOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin', 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'convergence-timeline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksAdded' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksAdded',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-added',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksDeleted' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksDeleted',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-deleted',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority',
            False, 
            [
            _MetaInfoClassMember('convergence-timeline', REFERENCE_LIST, 'ConvergenceTimeline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline', 
                [], [], 
                '''                Convergence timeline details
                ''',
                'convergence_timeline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-added', REFERENCE_LIST, 'LeafNetworksAdded' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksAdded', 
                [], [], 
                '''                List of Leaf Networks Added
                ''',
                'leaf_networks_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-deleted', REFERENCE_LIST, 'LeafNetworksDeleted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksDeleted', 
                [], [], 
                '''                List of Leaf Networks Deleted
                ''',
                'leaf_networks_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_CLASS, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary', 
                [], [], 
                '''                Summary of the priority
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority', 
                [], [], 
                '''                Convergence information on a per-priority basis
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'inter-area-and-external',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline',
            False, 
            [
            _MetaInfoClassMember('spf-run-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific SPF run
                ''',
                'spf_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('dijkstra-run', REFERENCE_LIST, 'DijkstraRun' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun', 
                [], [], 
                '''                List of Dijkstra runs
                ''',
                'dijkstra_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-and-external', REFERENCE_LIST, 'InterAreaAndExternal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal', 
                [], [], 
                '''                Inter-area & external calculation information
                ''',
                'inter_area_and_external',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-summary', REFERENCE_CLASS, 'SpfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary', 
                [], [], 
                '''                SPF summary information
                ''',
                'spf_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-offline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SpfRunOfflines' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SpfRunOfflines',
            False, 
            [
            _MetaInfoClassMember('spf-run-offline', REFERENCE_LIST, 'SpfRunOffline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline', 
                [], [], 
                '''                Offline operational data for particular OSPF
                SPF run
                ''',
                'spf_run_offline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-offlines',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path.LfaPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path.LfaPath',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-type', REFERENCE_ENUM_CLASS, 'RcmdShowIpfrrLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowIpfrrLfaEnum', 
                [], [], 
                '''                Type of LFA
                ''',
                'lfa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID, in case of Remote LFA
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lfa-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-path', REFERENCE_LIST, 'LfaPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path.LfaPath', 
                [], [], 
                '''                Backup Path Informatoin
                ''',
                'lfa_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'time-line',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol route cost
                ''',
                'cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced IP-FRR Event ID (0 - Not Applicable)
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.LsaProcessed', 
                [], [], 
                '''                List of LSAs processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path', 
                [], [], 
                '''                Path information
                ''',
                'path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Event processed priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-path-change-type', REFERENCE_ENUM_CLASS, 'RcmdShowRoutePathChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRoutePathChangeEnum', 
                [], [], 
                '''                Route Path Change Type
                ''',
                'route_path_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Route Type intra/inter/l1/l2
                ''',
                'route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced SPF Run No (0 - Not Applicable)
                ''',
                'spf_run_no',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('time-line', REFERENCE_LIST, 'TimeLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine', 
                [], [], 
                '''                Timeline information
                ''',
                'time_line',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TriggerLsa', 
                [], [], 
                '''                LSA that triggered this event
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event trigger time
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'summary-external-event-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries',
            False, 
            [
            _MetaInfoClassMember('summary-external-event-summary', REFERENCE_LIST, 'SummaryExternalEventSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary', 
                [], [], 
                '''                OSPF Summary-External Prefix Event data
                ''',
                'summary_external_event_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'summary-external-event-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-type', REFERENCE_ENUM_CLASS, 'RcmdShowIpfrrLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowIpfrrLfaEnum', 
                [], [], 
                '''                Type of LFA
                ''',
                'lfa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID, in case of Remote LFA
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lfa-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-path', REFERENCE_LIST, 'LfaPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath', 
                [], [], 
                '''                Backup Path Informatoin
                ''',
                'lfa_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'time-line',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol route cost
                ''',
                'cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced IP-FRR Event ID (0 - Not Applicable)
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed', 
                [], [], 
                '''                List of LSAs processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path', 
                [], [], 
                '''                Path information
                ''',
                'path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Event processed priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-path-change-type', REFERENCE_ENUM_CLASS, 'RcmdShowRoutePathChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRoutePathChangeEnum', 
                [], [], 
                '''                Route Path Change Type
                ''',
                'route_path_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Route Type intra/inter/l1/l2
                ''',
                'route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced SPF Run No (0 - Not Applicable)
                ''',
                'spf_run_no',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('time-line', REFERENCE_LIST, 'TimeLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine', 
                [], [], 
                '''                Timeline information
                ''',
                'time_line',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa', 
                [], [], 
                '''                LSA that triggered this event
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event trigger time
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventSummaries',
            False, 
            [
            _MetaInfoClassMember('prefix-event-summary', REFERENCE_LIST, 'PrefixEventSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary', 
                [], [], 
                '''                OSPF Prefix Event data
                ''',
                'prefix_event_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path.LfaPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path.LfaPath',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-type', REFERENCE_ENUM_CLASS, 'RcmdShowIpfrrLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowIpfrrLfaEnum', 
                [], [], 
                '''                Type of LFA
                ''',
                'lfa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID, in case of Remote LFA
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lfa-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-path', REFERENCE_LIST, 'LfaPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path.LfaPath', 
                [], [], 
                '''                Backup Path Informatoin
                ''',
                'lfa_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'time-line',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol route cost
                ''',
                'cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced IP-FRR Event ID (0 - Not Applicable)
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.LsaProcessed', 
                [], [], 
                '''                List of LSAs processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path', 
                [], [], 
                '''                Path information
                ''',
                'path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Event processed priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-path-change-type', REFERENCE_ENUM_CLASS, 'RcmdShowRoutePathChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRoutePathChangeEnum', 
                [], [], 
                '''                Route Path Change Type
                ''',
                'route_path_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Route Type intra/inter/l1/l2
                ''',
                'route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced SPF Run No (0 - Not Applicable)
                ''',
                'spf_run_no',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('time-line', REFERENCE_LIST, 'TimeLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine', 
                [], [], 
                '''                Timeline information
                ''',
                'time_line',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TriggerLsa', 
                [], [], 
                '''                LSA that triggered this event
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event trigger time
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'summary-external-event-offline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines',
            False, 
            [
            _MetaInfoClassMember('summary-external-event-offline', REFERENCE_LIST, 'SummaryExternalEventOffline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline', 
                [], [], 
                '''                Offline operational data for particular OSPF
                Prefix Event
                ''',
                'summary_external_event_offline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'summary-external-event-offlines',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-type', REFERENCE_ENUM_CLASS, 'RcmdShowIpfrrLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowIpfrrLfaEnum', 
                [], [], 
                '''                Type of LFA
                ''',
                'lfa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID, in case of Remote LFA
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lfa-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-path', REFERENCE_LIST, 'LfaPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath', 
                [], [], 
                '''                Backup Path Informatoin
                ''',
                'lfa_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'time-line',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol route cost
                ''',
                'cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced IP-FRR Event ID (0 - Not Applicable)
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed', 
                [], [], 
                '''                List of LSAs processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path', 
                [], [], 
                '''                Path information
                ''',
                'path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Event processed priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-path-change-type', REFERENCE_ENUM_CLASS, 'RcmdShowRoutePathChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRoutePathChangeEnum', 
                [], [], 
                '''                Route Path Change Type
                ''',
                'route_path_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Route Type intra/inter/l1/l2
                ''',
                'route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced SPF Run No (0 - Not Applicable)
                ''',
                'spf_run_no',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('time-line', REFERENCE_LIST, 'TimeLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine', 
                [], [], 
                '''                Timeline information
                ''',
                'time_line',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa', 
                [], [], 
                '''                LSA that triggered this event
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event trigger time
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-offline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.PrefixEventOfflines',
            False, 
            [
            _MetaInfoClassMember('prefix-event-offline', REFERENCE_LIST, 'PrefixEventOffline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline', 
                [], [], 
                '''                Offline operational data for particular OSPF
                Prefix Event
                ''',
                'prefix_event_offline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-offlines',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance.SummaryExternalEventStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance.SummaryExternalEventStatistics',
            False, 
            [
            _MetaInfoClassMember('external-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Ext Routes Added
                ''',
                'external_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('external-critical', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Ext Routes Critical
                ''',
                'external_critical',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('external-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Ext Routes Deleted
                ''',
                'external_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('external-high', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Ext Routes High
                ''',
                'external_high',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('external-low', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Ext Routes Low
                ''',
                'external_low',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('external-medium', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Ext Routes Medium
                ''',
                'external_medium',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('external-modified', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Ext Routes Modified
                ''',
                'external_modified',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('external-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total External Routes
                ''',
                'external_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-added', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IA Routes Added
                ''',
                'inter_area_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-critical', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IA Routes Critical
                ''',
                'inter_area_critical',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-deleted', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IA Routes Deleted
                ''',
                'inter_area_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-high', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IA Routes High
                ''',
                'inter_area_high',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-low', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IA Routes Low
                ''',
                'inter_area_low',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-medium', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IA Routes Medium
                ''',
                'inter_area_medium',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-modified', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total IA Routes Modified
                ''',
                'inter_area_modified',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('inter-area-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Inter-Area Routes
                ''',
                'inter_area_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'summary-external-event-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Operational data for a particular instance
                ''',
                'instance_name',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('ipfrr-event-offlines', REFERENCE_CLASS, 'IpfrrEventOfflines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines', 
                [], [], 
                '''                OSPF IP-FRR Event offline data
                ''',
                'ipfrr_event_offlines',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-summaries', REFERENCE_CLASS, 'IpfrrEventSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries', 
                [], [], 
                '''                OSPF IP-FRR events summary data
                ''',
                'ipfrr_event_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-event-offlines', REFERENCE_CLASS, 'PrefixEventOfflines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventOfflines', 
                [], [], 
                '''                OSPF Prefix events offline data
                ''',
                'prefix_event_offlines',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-event-statistics', REFERENCE_CLASS, 'PrefixEventStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventStatistics', 
                [], [], 
                '''                OSPF Prefix events summary data
                ''',
                'prefix_event_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-event-summaries', REFERENCE_CLASS, 'PrefixEventSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.PrefixEventSummaries', 
                [], [], 
                '''                OSPF Prefix events summary data
                ''',
                'prefix_event_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-offlines', REFERENCE_CLASS, 'SpfRunOfflines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunOfflines', 
                [], [], 
                '''                OSPF SPF run offline data
                ''',
                'spf_run_offlines',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-summaries', REFERENCE_CLASS, 'SpfRunSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SpfRunSummaries', 
                [], [], 
                '''                OSPF SPF run summary data
                ''',
                'spf_run_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('summary-external-event-offlines', REFERENCE_CLASS, 'SummaryExternalEventOfflines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines', 
                [], [], 
                '''                OSPF Summary-External Prefix events offline
                data
                ''',
                'summary_external_event_offlines',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('summary-external-event-statistics', REFERENCE_CLASS, 'SummaryExternalEventStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventStatistics', 
                [], [], 
                '''                Summary-External prefix monitoring statistics
                ''',
                'summary_external_event_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('summary-external-event-summaries', REFERENCE_CLASS, 'SummaryExternalEventSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries', 
                [], [], 
                '''                OSPF Summary-External Prefix events summary
                data
                ''',
                'summary_external_event_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf.Instances' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances.Instance', 
                [], [], 
                '''                Operational data for a particular instance
                ''',
                'instance',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instances',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ospf' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ospf',
            False, 
            [
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf.Instances', 
                [], [], 
                '''                Operational data
                ''',
                'instances',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Normal.ProtocolConfig.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Normal.ProtocolConfig.Priority',
            False, 
            [
            _MetaInfoClassMember('disable', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Enable/Disable cfg
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-name', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Priority Level
                ''',
                'priority_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                threshold value
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Normal.ProtocolConfig' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Normal.ProtocolConfig',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Normal.ProtocolConfig.Priority', 
                [], [], 
                '''                Priority level configuration
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protocol-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol Name
                ''',
                'protocol_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'protocol-config',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Normal.ServerDetail.TraceInformation' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Normal.ServerDetail.TraceInformation',
            False, 
            [
            _MetaInfoClassMember('error-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Server Error Status
                ''',
                'error_stats',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-run-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Server Last Run Status
                ''',
                'last_run_stats',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Server Total Status
                ''',
                'total_stats',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trace-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configured Hostname
                ''',
                'trace_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trace-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Normal.ServerDetail' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Normal.ServerDetail',
            False, 
            [
            _MetaInfoClassMember('memory-suspend', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Memory Suspend
                ''',
                'memory_suspend',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('overload-suspend', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Overload suspend
                ''',
                'overload_suspend',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trace-information', REFERENCE_LIST, 'TraceInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Normal.ServerDetail.TraceInformation', 
                [], [], 
                '''                Trace Information
                ''',
                'trace_information',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'server-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Normal' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Normal',
            False, 
            [
            _MetaInfoClassMember('archive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive Count
                ''',
                'archive_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('diag-node-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diag Node count
                ''',
                'diag_node_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('diagnostics-archive-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diagnostics Archival Node (Applicable for local
                location)
                ''',
                'diagnostics_archive_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('diagnostics-archive-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diagnostics Archival Path
                ''',
                'diagnostics_archive_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('disabled-node-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disabled Node count
                ''',
                'disabled_node_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Event Buffer Size
                ''',
                'event_buffer_size',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configured Hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('in-active-node-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disabled Node count
                ''',
                'in_active_node_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface events count
                ''',
                'interface_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-archival-error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Archival Error
                ''',
                'last_archival_error',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-archival-error-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Archival Status
                ''',
                'last_archival_error_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-archival-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Archival Status
                ''',
                'last_archival_status',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-process-duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Processing Duration
                ''',
                'last_process_duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-process-start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Processing Start Time
                ''',
                'last_process_start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-process-state', REFERENCE_ENUM_CLASS, 'RcmdShowPrcsStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowPrcsStateEnum', 
                [], [], 
                '''                Process state
                ''',
                'last_process_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('max-events', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Events
                ''',
                'max_events',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('max-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Interface events count
                ''',
                'max_interface_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('monitoring-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured Monitor Interval
                ''',
                'monitoring_interval',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('next-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time for next processing
                ''',
                'next_interval',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-lc-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LC count
                ''',
                'node_lc_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-rp-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RP count
                ''',
                'node_rp_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Post Processing count
                ''',
                'process_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protocol-config', REFERENCE_LIST, 'ProtocolConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Normal.ProtocolConfig', 
                [], [], 
                '''                Protocol level configuration
                ''',
                'protocol_config',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reports-archive-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reports Archival Node (Applicable for local
                location)
                ''',
                'reports_archive_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reports-archive-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reports Archival Path
                ''',
                'reports_archive_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('server-detail', REFERENCE_LIST, 'ServerDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Normal.ServerDetail', 
                [], [], 
                '''                Detailed Information
                ''',
                'server_detail',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-process-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Processing count
                ''',
                'spf_process_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'RcmdBagEnableDisableEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBagEnableDisableEnum', 
                [], [], 
                '''                Server Status
                ''',
                'status',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'normal',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Detail.ProtocolConfig.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Detail.ProtocolConfig.Priority',
            False, 
            [
            _MetaInfoClassMember('disable', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Enable/Disable cfg
                ''',
                'disable',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-name', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Priority Level
                ''',
                'priority_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                threshold value
                ''',
                'threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Detail.ProtocolConfig' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Detail.ProtocolConfig',
            False, 
            [
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Detail.ProtocolConfig.Priority', 
                [], [], 
                '''                Priority level configuration
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protocol-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Protocol Name
                ''',
                'protocol_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'protocol-config',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Detail.ServerDetail.TraceInformation' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Detail.ServerDetail.TraceInformation',
            False, 
            [
            _MetaInfoClassMember('error-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Server Error Status
                ''',
                'error_stats',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-run-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Server Last Run Status
                ''',
                'last_run_stats',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-stats', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Server Total Status
                ''',
                'total_stats',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trace-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configured Hostname
                ''',
                'trace_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trace-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Detail.ServerDetail' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Detail.ServerDetail',
            False, 
            [
            _MetaInfoClassMember('memory-suspend', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Memory Suspend
                ''',
                'memory_suspend',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('overload-suspend', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Overload suspend
                ''',
                'overload_suspend',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trace-information', REFERENCE_LIST, 'TraceInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Detail.ServerDetail.TraceInformation', 
                [], [], 
                '''                Trace Information
                ''',
                'trace_information',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'server-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server.Detail' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server.Detail',
            False, 
            [
            _MetaInfoClassMember('archive-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive Count
                ''',
                'archive_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('diag-node-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diag Node count
                ''',
                'diag_node_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('diagnostics-archive-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diagnostics Archival Node (Applicable for local
                location)
                ''',
                'diagnostics_archive_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('diagnostics-archive-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Diagnostics Archival Path
                ''',
                'diagnostics_archive_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('disabled-node-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disabled Node count
                ''',
                'disabled_node_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-buffer-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Event Buffer Size
                ''',
                'event_buffer_size',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('host-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Configured Hostname
                ''',
                'host_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('in-active-node-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Disabled Node count
                ''',
                'in_active_node_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface events count
                ''',
                'interface_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-archival-error', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Archival Error
                ''',
                'last_archival_error',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-archival-error-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Archival Status
                ''',
                'last_archival_error_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-archival-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Archival Status
                ''',
                'last_archival_status',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-process-duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Processing Duration
                ''',
                'last_process_duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-process-start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Processing Start Time
                ''',
                'last_process_start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-process-state', REFERENCE_ENUM_CLASS, 'RcmdShowPrcsStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowPrcsStateEnum', 
                [], [], 
                '''                Process state
                ''',
                'last_process_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('max-events', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Events
                ''',
                'max_events',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('max-interface-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Max Interface events count
                ''',
                'max_interface_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('monitoring-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured Monitor Interval
                ''',
                'monitoring_interval',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('next-interval', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time for next processing
                ''',
                'next_interval',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-lc-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LC count
                ''',
                'node_lc_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-rp-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                RP count
                ''',
                'node_rp_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Post Processing count
                ''',
                'process_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protocol-config', REFERENCE_LIST, 'ProtocolConfig' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Detail.ProtocolConfig', 
                [], [], 
                '''                Protocol level configuration
                ''',
                'protocol_config',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reports-archive-node', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reports Archival Node (Applicable for local
                location)
                ''',
                'reports_archive_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reports-archive-path', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reports Archival Path
                ''',
                'reports_archive_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('server-detail', REFERENCE_LIST, 'ServerDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Detail.ServerDetail', 
                [], [], 
                '''                Detailed Information
                ''',
                'server_detail',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-process-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Processing count
                ''',
                'spf_process_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'RcmdBagEnableDisableEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBagEnableDisableEnum', 
                [], [], 
                '''                Server Status
                ''',
                'status',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'detail',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Server' : {
        'meta_info' : _MetaInfoClass('Rcmd.Server',
            False, 
            [
            _MetaInfoClassMember('detail', REFERENCE_CLASS, 'Detail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Detail', 
                [], [], 
                '''                Server Info
                ''',
                'detail',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('normal', REFERENCE_CLASS, 'Normal' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server.Normal', 
                [], [], 
                '''                Server Info
                ''',
                'normal',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'server',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Node.NodeInformation' : {
        'meta_info' : _MetaInfoClass('Rcmd.Node.NodeInformation',
            False, 
            [
            _MetaInfoClassMember('card-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Card State
                ''',
                'card_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('diag-mode', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Diag Mode
                ''',
                'diag_mode',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fwd-referenced', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Forward Referenced
                ''',
                'fwd_referenced',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Updated Time
                ''',
                'last_update_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node Id
                ''',
                'node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Node Name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-state', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Node State
                ''',
                'node_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-type', REFERENCE_ENUM_CLASS, 'RcmdShowNodeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowNodeEnum', 
                [], [], 
                '''                Node Type
                ''',
                'node_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('rack-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Rack Id
                ''',
                'rack_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('redundancy-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Redundancy State
                ''',
                'redundancy_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('software-state', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Software State
                ''',
                'software_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('status', REFERENCE_ENUM_CLASS, 'RcmdBagEnblDsblEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBagEnblDsblEnum', 
                [], [], 
                '''                Status
                ''',
                'status',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'node-information',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Node' : {
        'meta_info' : _MetaInfoClass('Rcmd.Node',
            False, 
            [
            _MetaInfoClassMember('node-information', REFERENCE_LIST, 'NodeInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Node.NodeInformation', 
                [], [], 
                '''                Node Info
                ''',
                'node_information',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic',
            False, 
            [
            _MetaInfoClassMember('below-threshold', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Covearge is below Configured Threshold
                ''',
                'below_threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('local-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local LFA Coverage in percentage
                ''',
                'local_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote LFA Coverage in percentage
                ''',
                'remote_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'primary-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode',
            False, 
            [
            _MetaInfoClassMember('in-use-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inuse time of the Remote Node (eg: Apr 24 13:16
                :04.961)
                ''',
                'in_use_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths protected by this Remote Node
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('primary-path', REFERENCE_LIST, 'PrimaryPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath', 
                [], [], 
                '''                Protected Primary Paths
                ''',
                'primary_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote-LFA Node ID
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific IP-FRR Event
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('completed-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Completed reference SPF Run Number
                ''',
                'completed_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage for all priorities
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration for the calculation (in milliseconds)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Event ID
                ''',
                'event_id_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-statistic', REFERENCE_LIST, 'IpfrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic', 
                [], [], 
                '''                IP-Frr Statistics categorized by priority
                ''',
                'ipfrr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node', REFERENCE_LIST, 'RemoteNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode', 
                [], [], 
                '''                Remote Node Information
                ''',
                'remote_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time-offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start Time offset from trigger time (in
                milliseconds)
                ''',
                'start_time_offset',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Routes for all priorities
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Triggered reference SPF Run Number
                ''',
                'trigger_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time  (eg: Apr 24 13:16:04.961)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Waiting Time (in milliseconds)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventSummaries',
            False, 
            [
            _MetaInfoClassMember('ipfrr-event-summary', REFERENCE_LIST, 'IpfrrEventSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary', 
                [], [], 
                '''                IP-FRR Event data
                ''',
                'ipfrr_event_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic',
            False, 
            [
            _MetaInfoClassMember('prefix-info', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Events with Prefix
                ''',
                'prefix_info',
                'Cisco-IOS-XR-infra-rcmd-oper', True, [
                    _MetaInfoClassMember('prefix-info', ATTRIBUTE, 'str' , None, None, 
                        [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])/(([0-9])|([1-2][0-9])|(3[0-2]))'], 
                        '''                        Events with Prefix
                        ''',
                        'prefix_info',
                        'Cisco-IOS-XR-infra-rcmd-oper', True),
                    _MetaInfoClassMember('prefix-info', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(/(([0-9])|([0-9]{2})|(1[0-1][0-9])|(12[0-8])))'], 
                        '''                        Events with Prefix
                        ''',
                        'prefix_info',
                        'Cisco-IOS-XR-infra-rcmd-oper', True),
                ]),
            _MetaInfoClassMember('add-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times route gets Added
                ''',
                'add_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('critical-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under Critical Priority
                ''',
                'critical_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('delete-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times route gets Deleted
                ''',
                'delete_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('high-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under High Priority
                ''',
                'high_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Last event Add/Delete
                ''',
                'last_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Known Cost
                ''',
                'last_cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-event-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last event trigger time
                ''',
                'last_event_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Last event processed priority
                ''',
                'last_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Last event Route Type
                ''',
                'last_route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('low-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under Low Priority
                ''',
                'low_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('medium-priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times processed under Medium Priority
                ''',
                'medium_priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modify-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times route gets Deleted
                ''',
                'modify_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of times threshold got exceeded
                ''',
                'threshold_exceed_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventStatistics',
            False, 
            [
            _MetaInfoClassMember('prefix-event-statistic', REFERENCE_LIST, 'PrefixEventStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic', 
                [], [], 
                '''                Monitoring Statistics
                ''',
                'prefix_event_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of SPF calculation (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('is-data-complete', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the event has all information
                ''',
                'is_data_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('isis-level', REFERENCE_ENUM_CLASS, 'RcmdIsisLvlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdIsisLvlEnum', 
                [], [], 
                '''                ISIS Level
                ''',
                'isis_level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_LIST, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary', 
                [], [], 
                '''                Convergence information summary on per-priority
                basis
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'RcmdSpfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdSpfStateEnum', 
                [], [], 
                '''                SPF state
                ''',
                'state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('topology', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Topology index (multi-topology)
                ''',
                'topology',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-lsp-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of LSP changes processed
                ''',
                'total_lsp_changes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time (in hh:mm:ss.msec)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'RcmdIsisSpfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdIsisSpfEnum', 
                [], [], 
                '''                Type of SPF
                ''',
                'type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.NodeStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.NodeStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'node-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.TriggerLsp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.TriggerLsp',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP ID
                ''',
                'lsp_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RouteOrigin' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RouteOrigin',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Enter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Enter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Exit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Exit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Redistribute' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Redistribute',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', REFERENCE_CLASS, 'LdpEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpEnter', 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', REFERENCE_CLASS, 'LdpExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpExit', 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', REFERENCE_CLASS, 'LsdEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdEnter', 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', REFERENCE_CLASS, 'LsdExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdExit', 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', REFERENCE_CLASS, 'RiBv4Enter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Enter', 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', REFERENCE_CLASS, 'RiBv4Exit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Exit', 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', REFERENCE_CLASS, 'RiBv4Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Redistribute', 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', REFERENCE_CLASS, 'RouteOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RouteOrigin', 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'convergence-timeline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksAdded' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksAdded',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-added',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksDeleted' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksDeleted',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-deleted',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority',
            False, 
            [
            _MetaInfoClassMember('convergence-timeline', REFERENCE_LIST, 'ConvergenceTimeline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline', 
                [], [], 
                '''                Convergence timeline details
                ''',
                'convergence_timeline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-added', REFERENCE_LIST, 'LeafNetworksAdded' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksAdded', 
                [], [], 
                '''                List of Leaf Networks Added
                ''',
                'leaf_networks_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-deleted', REFERENCE_LIST, 'LeafNetworksDeleted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksDeleted', 
                [], [], 
                '''                List of Leaf Networks Deleted
                ''',
                'leaf_networks_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_CLASS, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary', 
                [], [], 
                '''                Summary of the priority
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP ID
                ''',
                'lsp_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsp-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspRegenerated' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspRegenerated',
            False, 
            [
            _MetaInfoClassMember('isis-level', REFERENCE_ENUM_CLASS, 'RcmdIsisLvlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdIsisLvlEnum', 
                [], [], 
                '''                ISIS Level
                ''',
                'isis_level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP ID
                ''',
                'lsp_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger reasons for LSP regeneration. Example:
                pr^ - periodic, cr^ - clear (Check the
                documentation for the entire list)
                ''',
                'reason',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('serial-number-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Serial Number of the session event
                ''',
                'serial_number_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Run Number
                ''',
                'spf_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsp-regenerated',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary',
            False, 
            [
            _MetaInfoClassMember('spf-run-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific SPF run
                ''',
                'spf_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('lsp-processed', REFERENCE_LIST, 'LspProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspProcessed', 
                [], [], 
                '''                List of LSP changes processed
                ''',
                'lsp_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regenerated', REFERENCE_LIST, 'LspRegenerated' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspRegenerated', 
                [], [], 
                '''                List of LSP regenerated
                ''',
                'lsp_regenerated',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-statistics', REFERENCE_CLASS, 'NodeStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.NodeStatistics', 
                [], [], 
                '''                SPF Node statistics
                ''',
                'node_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority', 
                [], [], 
                '''                Convergence information on per-priority basis
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger reasons for SPF run. Example: pr^ -
                periodic, cr^ - clear (Check the documentation
                for the entire list)
                ''',
                'reason',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-summary', REFERENCE_CLASS, 'SpfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary', 
                [], [], 
                '''                SPF summary information
                ''',
                'spf_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start time (offset from event trigger time in ss
                .msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsp', REFERENCE_LIST, 'TriggerLsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.TriggerLsp', 
                [], [], 
                '''                Trigger LSP
                ''',
                'trigger_lsp',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wait time applied at SPF schedule (in msec)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunSummaries',
            False, 
            [
            _MetaInfoClassMember('spf-run-summary', REFERENCE_LIST, 'SpfRunSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary', 
                [], [], 
                '''                SPF Event data
                ''',
                'spf_run_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic',
            False, 
            [
            _MetaInfoClassMember('below-threshold', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Covearge is below Configured Threshold
                ''',
                'below_threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('local-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Local LFA Coverage in percentage
                ''',
                'local_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-lfa-coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Remote LFA Coverage in percentage
                ''',
                'remote_lfa_coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'primary-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode',
            False, 
            [
            _MetaInfoClassMember('in-use-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inuse time of the Remote Node (eg: Apr 24 13:16
                :04.961)
                ''',
                'in_use_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of paths protected by this Remote Node
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('primary-path', REFERENCE_LIST, 'PrimaryPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath', 
                [], [], 
                '''                Protected Primary Paths
                ''',
                'primary_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote-LFA Node ID
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific IP-FRR Event
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('completed-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Completed reference SPF Run Number
                ''',
                'completed_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage for all priorities
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration for the calculation (in milliseconds)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Event ID
                ''',
                'event_id_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-statistic', REFERENCE_LIST, 'IpfrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic', 
                [], [], 
                '''                IP-Frr Statistics categorized by priority
                ''',
                'ipfrr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node', REFERENCE_LIST, 'RemoteNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode', 
                [], [], 
                '''                Remote Node Information
                ''',
                'remote_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time-offset', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start Time offset from trigger time (in
                milliseconds)
                ''',
                'start_time_offset',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cumulative Number of Routes for all priorities
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IP-Frr Triggered reference SPF Run Number
                ''',
                'trigger_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time  (eg: Apr 24 13:16:04.961)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Waiting Time (in milliseconds)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-offline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.IpfrrEventOfflines',
            False, 
            [
            _MetaInfoClassMember('ipfrr-event-offline', REFERENCE_LIST, 'IpfrrEventOffline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline', 
                [], [], 
                '''                Offline operational data for particular ISIS
                IP-FRR Event
                ''',
                'ipfrr_event_offline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ipfrr-event-offlines',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of SPF calculation (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('is-data-complete', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Whether the event has all information
                ''',
                'is_data_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('isis-level', REFERENCE_ENUM_CLASS, 'RcmdIsisLvlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdIsisLvlEnum', 
                [], [], 
                '''                ISIS Level
                ''',
                'isis_level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_LIST, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary', 
                [], [], 
                '''                Convergence information summary on per-priority
                basis
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'RcmdSpfStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdSpfStateEnum', 
                [], [], 
                '''                SPF state
                ''',
                'state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('topology', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Topology index (multi-topology)
                ''',
                'topology',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-lsp-changes', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Total number of LSP changes processed
                ''',
                'total_lsp_changes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger time (in hh:mm:ss.msec)
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('type', REFERENCE_ENUM_CLASS, 'RcmdIsisSpfEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdIsisSpfEnum', 
                [], [], 
                '''                Type of SPF
                ''',
                'type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.NodeStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.NodeStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'node-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.TriggerLsp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.TriggerLsp',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP ID
                ''',
                'lsp_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.RouteStatistics' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.RouteStatistics',
            False, 
            [
            _MetaInfoClassMember('adds', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Added
                ''',
                'adds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('deletes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Deleted
                ''',
                'deletes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('modifies', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Modified
                ''',
                'modifies',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Reachable
                ''',
                'reachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('touches', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Touched
                ''',
                'touches',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('unreachables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Unreachable
                ''',
                'unreachables',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.FrrStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.FrrStatistic',
            False, 
            [
            _MetaInfoClassMember('coverage', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Coverage in percentage
                ''',
                'coverage',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fully-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Fully Protected Routes
                ''',
                'fully_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('partially-protected-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Partially Protected Routes
                ''',
                'partially_protected_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-routes', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Number of Routes
                ''',
                'total_routes',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'frr-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary',
            False, 
            [
            _MetaInfoClassMember('frr-statistic', REFERENCE_LIST, 'FrrStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.FrrStatistic', 
                [], [], 
                '''                Fast Re-Route Statistics
                ''',
                'frr_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('level', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Critical, High, Medium or Low
                ''',
                'level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-statistics', REFERENCE_CLASS, 'RouteStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.RouteStatistics', 
                [], [], 
                '''                Route statistics
                ''',
                'route_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RouteOrigin' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RouteOrigin',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'route-origin',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Enter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Enter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Exit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Exit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Redistribute' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Redistribute',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ri-bv4-redistribute',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdEnter' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdEnter',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-enter',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdExit' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdExit',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsd-exit',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls.FibComplete' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls.FibComplete',
            False, 
            [
            _MetaInfoClassMember('duration', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duration of processing (in ss.msec)
                ''',
                'duration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last route process time relative to event
                trigger time (in ss.msec)
                ''',
                'end_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                First route process time relative to event
                trigger time (in ss.msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'fib-complete',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', REFERENCE_CLASS, 'FibComplete' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls.FibComplete', 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', REFERENCE_CLASS, 'LdpEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpEnter', 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', REFERENCE_CLASS, 'LdpExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpExit', 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', REFERENCE_CLASS, 'LsdEnter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdEnter', 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', REFERENCE_CLASS, 'LsdExit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdExit', 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', REFERENCE_CLASS, 'RiBv4Enter' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Enter', 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', REFERENCE_CLASS, 'RiBv4Exit' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Exit', 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', REFERENCE_CLASS, 'RiBv4Redistribute' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Redistribute', 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', REFERENCE_CLASS, 'RouteOrigin' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RouteOrigin', 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'convergence-timeline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksAdded' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksAdded',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-added',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksDeleted' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksDeleted',
            False, 
            [
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                IP address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('net-mask', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Mask
                ''',
                'net_mask',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'leaf-networks-deleted',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority',
            False, 
            [
            _MetaInfoClassMember('convergence-timeline', REFERENCE_LIST, 'ConvergenceTimeline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline', 
                [], [], 
                '''                Convergence timeline details
                ''',
                'convergence_timeline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-added', REFERENCE_LIST, 'LeafNetworksAdded' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksAdded', 
                [], [], 
                '''                List of Leaf Networks Added
                ''',
                'leaf_networks_added',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('leaf-networks-deleted', REFERENCE_LIST, 'LeafNetworksDeleted' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksDeleted', 
                [], [], 
                '''                List of Leaf Networks Deleted
                ''',
                'leaf_networks_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority-summary', REFERENCE_CLASS, 'PrioritySummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary', 
                [], [], 
                '''                Summary of the priority
                ''',
                'priority_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'priority',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP ID
                ''',
                'lsp_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsp-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspRegenerated' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspRegenerated',
            False, 
            [
            _MetaInfoClassMember('isis-level', REFERENCE_ENUM_CLASS, 'RcmdIsisLvlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdIsisLvlEnum', 
                [], [], 
                '''                ISIS Level
                ''',
                'isis_level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP ID
                ''',
                'lsp_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger reasons for LSP regeneration. Example:
                pr^ - periodic, cr^ - clear (Check the
                documentation for the entire list)
                ''',
                'reason',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('serial-number-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Serial Number of the session event
                ''',
                'serial_number_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Run Number
                ''',
                'spf_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsp-regenerated',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline',
            False, 
            [
            _MetaInfoClassMember('spf-run-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific SPF run
                ''',
                'spf_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('lsp-processed', REFERENCE_LIST, 'LspProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspProcessed', 
                [], [], 
                '''                List of LSP changes processed
                ''',
                'lsp_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regenerated', REFERENCE_LIST, 'LspRegenerated' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspRegenerated', 
                [], [], 
                '''                List of LSP regenerated
                ''',
                'lsp_regenerated',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-statistics', REFERENCE_CLASS, 'NodeStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.NodeStatistics', 
                [], [], 
                '''                SPF Node statistics
                ''',
                'node_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_LIST, 'Priority' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority', 
                [], [], 
                '''                Convergence information on per-priority basis
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger reasons for SPF run. Example: pr^ -
                periodic, cr^ - clear (Check the documentation
                for the entire list)
                ''',
                'reason',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-summary', REFERENCE_CLASS, 'SpfSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary', 
                [], [], 
                '''                SPF summary information
                ''',
                'spf_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Start time (offset from event trigger time in ss
                .msec)
                ''',
                'start_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsp', REFERENCE_LIST, 'TriggerLsp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.TriggerLsp', 
                [], [], 
                '''                Trigger LSP
                ''',
                'trigger_lsp',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('wait-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Wait time applied at SPF schedule (in msec)
                ''',
                'wait_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-offline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.SpfRunOfflines' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.SpfRunOfflines',
            False, 
            [
            _MetaInfoClassMember('spf-run-offline', REFERENCE_LIST, 'SpfRunOffline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline', 
                [], [], 
                '''                Offline operational data for particular ISIS
                SPF run
                ''',
                'spf_run_offline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'spf-run-offlines',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-type', REFERENCE_ENUM_CLASS, 'RcmdShowIpfrrLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowIpfrrLfaEnum', 
                [], [], 
                '''                Type of LFA
                ''',
                'lfa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID, in case of Remote LFA
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lfa-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-path', REFERENCE_LIST, 'LfaPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath', 
                [], [], 
                '''                Backup Path Informatoin
                ''',
                'lfa_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'time-line',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol route cost
                ''',
                'cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced IP-FRR Event ID (0 - Not Applicable)
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed', 
                [], [], 
                '''                List of LSAs processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path', 
                [], [], 
                '''                Path information
                ''',
                'path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Event processed priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-path-change-type', REFERENCE_ENUM_CLASS, 'RcmdShowRoutePathChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRoutePathChangeEnum', 
                [], [], 
                '''                Route Path Change Type
                ''',
                'route_path_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Route Type intra/inter/l1/l2
                ''',
                'route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced SPF Run No (0 - Not Applicable)
                ''',
                'spf_run_no',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('time-line', REFERENCE_LIST, 'TimeLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine', 
                [], [], 
                '''                Timeline information
                ''',
                'time_line',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa', 
                [], [], 
                '''                LSA that triggered this event
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event trigger time
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventSummaries',
            False, 
            [
            _MetaInfoClassMember('prefix-event-summary', REFERENCE_LIST, 'PrefixEventSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary', 
                [], [], 
                '''                Prefix Event data
                ''',
                'prefix_event_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ip-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime',
            False, 
            [
            _MetaInfoClassMember('fastest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the minimum time
                ''',
                'fastest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('maximum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Maximum time(in seconds.milliseconds)
                ''',
                'maximum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('minimum-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Minimum time(in seconds.milliseconds)
                ''',
                'minimum_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('slowest-node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name which took the maximum time
                ''',
                'slowest_node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'mpls-convergence-time',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-type', REFERENCE_ENUM_CLASS, 'RcmdShowIpfrrLfaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowIpfrrLfaEnum', 
                [], [], 
                '''                Type of LFA
                ''',
                'lfa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID, in case of Remote LFA
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lfa-path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lfa-path', REFERENCE_LIST, 'LfaPath' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath', 
                [], [], 
                '''                Backup Path Informatoin
                ''',
                'lfa_path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('neighbour-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Nexthop Address
                ''',
                'neighbour_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-metric', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Path Metric
                ''',
                'path_metric',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'path',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'trigger-lsa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-ip',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls',
            False, 
            [
            _MetaInfoClassMember('fib-complete', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Completion point of FIB
                ''',
                'fib_complete',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Linecard node name
                ''',
                'node_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('speed', REFERENCE_ENUM_CLASS, 'RcmdLinecardSpeedEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLinecardSpeedEnum', 
                [], [], 
                '''                Relative convergence speed
                ''',
                'speed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lc-mpls',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine',
            False, 
            [
            _MetaInfoClassMember('lc-ip', REFERENCE_LIST, 'LcIp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp', 
                [], [], 
                '''                List of Linecards' completion point for IP
                routes
                ''',
                'lc_ip',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lc-mpls', REFERENCE_LIST, 'LcMpls' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls', 
                [], [], 
                '''                List of Linecards' completion point for MPLS
                labels
                ''',
                'lc_mpls',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LDP
                ''',
                'ldp_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LDP to LSD
                ''',
                'ldp_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of LSD
                ''',
                'lsd_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsd-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point of LSD to FIBs
                ''',
                'lsd_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-enter', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Entry point of IPv4 RIB
                ''',
                'ri_bv4_enter',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-exit', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Exit point from IPv4 RIB to FIBs
                ''',
                'ri_bv4_exit',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ri-bv4-redistribute', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route Redistribute point from IPv4 RIB to LDP
                ''',
                'ri_bv4_redistribute',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-origin', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Route origin (routing protocol)
                ''',
                'route_origin',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'time-line',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed',
            False, 
            [
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdLsChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsChangeEnum', 
                [], [], 
                '''                Add, Delete, Modify
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                LSA ID
                ''',
                'lsa_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-type', REFERENCE_ENUM_CLASS, 'RcmdLsaEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLsaEnum', 
                [], [], 
                '''                LSA type
                ''',
                'lsa_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('origin-router-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Originating Router ID
                ''',
                'origin_router_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsa-processed',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('change-type', REFERENCE_ENUM_CLASS, 'RcmdChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdChangeEnum', 
                [], [], 
                '''                Event Add/Delete
                ''',
                'change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('cost', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protocol route cost
                ''',
                'cost',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ip-convergence-time', REFERENCE_CLASS, 'IpConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime', 
                [], [], 
                '''                Convergence time for IP route programming
                ''',
                'ip_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced IP-FRR Event ID (0 - Not Applicable)
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsa-processed', REFERENCE_LIST, 'LsaProcessed' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed', 
                [], [], 
                '''                List of LSAs processed
                ''',
                'lsa_processed',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('mpls-convergence-time', REFERENCE_CLASS, 'MplsConvergenceTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime', 
                [], [], 
                '''                Convergence time for MPLS label programming
                ''',
                'mpls_convergence_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path', REFERENCE_LIST, 'Path' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path', 
                [], [], 
                '''                Path information
                ''',
                'path',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Prefix
                ''',
                'prefix',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-lenth', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Prefix length
                ''',
                'prefix_lenth',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('priority', REFERENCE_ENUM_CLASS, 'RcmdPriorityLevelEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdPriorityLevelEnum', 
                [], [], 
                '''                Event processed priority
                ''',
                'priority',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-path-change-type', REFERENCE_ENUM_CLASS, 'RcmdShowRoutePathChangeEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRoutePathChangeEnum', 
                [], [], 
                '''                Route Path Change Type
                ''',
                'route_path_change_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-type', REFERENCE_ENUM_CLASS, 'RcmdShowRouteEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowRouteEnum', 
                [], [], 
                '''                Route Type intra/inter/l1/l2
                ''',
                'route_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Referenced SPF Run No (0 - Not Applicable)
                ''',
                'spf_run_no',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('threshold-exceeded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Threshold exceeded
                ''',
                'threshold_exceeded',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('time-line', REFERENCE_LIST, 'TimeLine' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine', 
                [], [], 
                '''                Timeline information
                ''',
                'time_line',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-lsa', REFERENCE_LIST, 'TriggerLsa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa', 
                [], [], 
                '''                LSA that triggered this event
                ''',
                'trigger_lsa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('trigger-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event trigger time
                ''',
                'trigger_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-offline',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.PrefixEventOfflines' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.PrefixEventOfflines',
            False, 
            [
            _MetaInfoClassMember('prefix-event-offline', REFERENCE_LIST, 'PrefixEventOffline' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline', 
                [], [], 
                '''                Offline operational data for particular ISIS
                Prefix Event
                ''',
                'prefix_event_offline',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'prefix-event-offlines',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.LspRegenerateds.LspRegenerated' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.LspRegenerateds.LspRegenerated',
            False, 
            [
            _MetaInfoClassMember('serial-number', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Data for a particular regenerated LSP
                ''',
                'serial_number',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('isis-level', REFERENCE_ENUM_CLASS, 'RcmdIsisLvlEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdIsisLvlEnum', 
                [], [], 
                '''                ISIS Level
                ''',
                'isis_level',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                LSP ID
                ''',
                'lsp_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reason', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trigger reasons for LSP regeneration. Example:
                pr^ - periodic, cr^ - clear (Check the
                documentation for the entire list)
                ''',
                'reason',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('reception-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Reception Time on router (in hh:mm:ss.msec)
                ''',
                'reception_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence Number
                ''',
                'sequence_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('serial-number-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Serial Number of the session event
                ''',
                'serial_number_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Run Number
                ''',
                'spf_run_number',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsp-regenerated',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance.LspRegenerateds' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance.LspRegenerateds',
            False, 
            [
            _MetaInfoClassMember('lsp-regenerated', REFERENCE_LIST, 'LspRegenerated' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.LspRegenerateds.LspRegenerated', 
                [], [], 
                '''                Regenerated LSP data
                ''',
                'lsp_regenerated',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'lsp-regenerateds',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances.Instance' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances.Instance',
            False, 
            [
            _MetaInfoClassMember('instance-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Operational data for a particular instance
                ''',
                'instance_name',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('ipfrr-event-offlines', REFERENCE_CLASS, 'IpfrrEventOfflines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventOfflines', 
                [], [], 
                '''                ISIS IP-FRR Event offline data
                ''',
                'ipfrr_event_offlines',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-summaries', REFERENCE_CLASS, 'IpfrrEventSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.IpfrrEventSummaries', 
                [], [], 
                '''                ISIS IP-FRR events summary data
                ''',
                'ipfrr_event_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regenerateds', REFERENCE_CLASS, 'LspRegenerateds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.LspRegenerateds', 
                [], [], 
                '''                Regenerated LSP data
                ''',
                'lsp_regenerateds',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-event-offlines', REFERENCE_CLASS, 'PrefixEventOfflines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventOfflines', 
                [], [], 
                '''                ISIS Prefix events offline data
                ''',
                'prefix_event_offlines',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-event-statistics', REFERENCE_CLASS, 'PrefixEventStatistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventStatistics', 
                [], [], 
                '''                ISIS Prefix events statistics data
                ''',
                'prefix_event_statistics',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('prefix-event-summaries', REFERENCE_CLASS, 'PrefixEventSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.PrefixEventSummaries', 
                [], [], 
                '''                ISIS Prefix events summary data
                ''',
                'prefix_event_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-offlines', REFERENCE_CLASS, 'SpfRunOfflines' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunOfflines', 
                [], [], 
                '''                ISIS SPF run offline data
                ''',
                'spf_run_offlines',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-run-summaries', REFERENCE_CLASS, 'SpfRunSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance.SpfRunSummaries', 
                [], [], 
                '''                ISIS SPF run summary data
                ''',
                'spf_run_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis.Instances' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis.Instances',
            False, 
            [
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances.Instance', 
                [], [], 
                '''                Operational data for a particular instance
                ''',
                'instance',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instances',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Isis' : {
        'meta_info' : _MetaInfoClass('Rcmd.Isis',
            False, 
            [
            _MetaInfoClassMember('instances', REFERENCE_CLASS, 'Instances' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis.Instances', 
                [], [], 
                '''                Operational data
                ''',
                'instances',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Memory.MemoryInfo' : {
        'meta_info' : _MetaInfoClass('Rcmd.Memory.MemoryInfo',
            False, 
            [
            _MetaInfoClassMember('alloc-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocated count
                ''',
                'alloc_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('alloc-fails', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Allocation Fails
                ''',
                'alloc_fails',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('current-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current Count
                ''',
                'current_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('freed-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Freed Count
                ''',
                'freed_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('memory-type', REFERENCE_ENUM_CLASS, 'RcmdShowMemEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowMemEnum', 
                [], [], 
                '''                Memory Type
                ''',
                'memory_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Size of the datastructure
                ''',
                'size',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('structure-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Structure Name
                ''',
                'structure_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'memory-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Memory.EdmMemoryInfo' : {
        'meta_info' : _MetaInfoClass('Rcmd.Memory.EdmMemoryInfo',
            False, 
            [
            _MetaInfoClassMember('failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit failure
                ''',
                'failure',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Size of the block
                ''',
                'size',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit success
                ''',
                'success',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total request
                ''',
                'total',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'edm-memory-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Memory.StringMemoryInfo' : {
        'meta_info' : _MetaInfoClass('Rcmd.Memory.StringMemoryInfo',
            False, 
            [
            _MetaInfoClassMember('failure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit failure
                ''',
                'failure',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Size of the block
                ''',
                'size',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('success', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Cache-hit success
                ''',
                'success',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total request
                ''',
                'total',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'string-memory-info',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Memory' : {
        'meta_info' : _MetaInfoClass('Rcmd.Memory',
            False, 
            [
            _MetaInfoClassMember('edm-memory-info', REFERENCE_LIST, 'EdmMemoryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Memory.EdmMemoryInfo', 
                [], [], 
                '''                Memory Info
                ''',
                'edm_memory_info',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('memory-info', REFERENCE_LIST, 'MemoryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Memory.MemoryInfo', 
                [], [], 
                '''                Memory Info
                ''',
                'memory_info',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('string-memory-info', REFERENCE_LIST, 'StringMemoryInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Memory.StringMemoryInfo', 
                [], [], 
                '''                Memory Info
                ''',
                'string_memory_info',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'memory',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                transport address or adjacency address
                ''',
                'address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Event ID
                ''',
                'event_id_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event Time
                ''',
                'event_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-type', REFERENCE_ENUM_CLASS, 'RcmdLdpEventEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdLdpEventEnum', 
                [], [], 
                '''                Type of event
                ''',
                'event_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Label Space Router ID
                ''',
                'lsr_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('state', REFERENCE_ENUM_CLASS, 'RcmdShowLdpNeighbourStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowLdpNeighbourStatusEnum', 
                [], [], 
                '''                Adjacency Session Status
                ''',
                'state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'session',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.Sessions' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.Sessions.Session', 
                [], [], 
                '''                Session
                ''',
                'session',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'sessions',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaS.RemoteLfa.SessionStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaS.RemoteLfa.SessionStatistic',
            False, 
            [
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Path Count
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Path Count
                ''',
                'protected_path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Route Count
                ''',
                'protected_route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-label-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Label Count
                ''',
                'remote_label_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Route Count
                ''',
                'route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LDP Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'RcmdShowLdpSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowLdpSessionStateEnum', 
                [], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'session-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaS.RemoteLfa.RemoteNode' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaS.RemoteLfa.RemoteNode',
            False, 
            [
            _MetaInfoClassMember('in-use-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inuse time of the Session
                ''',
                'in_use_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Label Space Router ID
                ''',
                'lsr_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Path Count
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Path Count
                ''',
                'protected_path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Route Count
                ''',
                'protected_route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-label-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Label Count
                ''',
                'remote_label_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Route Count
                ''',
                'route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'RcmdShowLdpSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowLdpSessionStateEnum', 
                [], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('transport-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Transport Address
                ''',
                'transport_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaS.RemoteLfa.Logs' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaS.RemoteLfa.Logs',
            False, 
            [
            _MetaInfoClassMember('label-coverage-state', REFERENCE_ENUM_CLASS, 'RcmdShowLdpConvStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowLdpConvStateEnum', 
                [], [], 
                '''                Label Coverage State
                ''',
                'label_coverage_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('log-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event Time (eg: Apr 24 13:16:04.961)
                ''',
                'log_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-label-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Label Count
                ''',
                'remote_label_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Route Count
                ''',
                'route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'logs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaS.RemoteLfa' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaS.RemoteLfa',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('below-threshold', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Coverage Below Threshold
                ''',
                'below_threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-of-calculation-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                End of IGP LFA Calculation Time (eg: Apr 24 13
                :16:04.961)
                ''',
                'end_of_calculation_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LDP-rLFA Event ID
                ''',
                'event_id_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('igp-protocol', REFERENCE_ENUM_CLASS, 'RcmdProtocolIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdProtocolIdEnum', 
                [], [], 
                '''                IGP Protocol
                ''',
                'igp_protocol',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IGP IP-FRR Event ID (ref:
                rcmd_show_ipfrr_event_info(EventID))
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('logs', REFERENCE_LIST, 'Logs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaS.RemoteLfa.Logs', 
                [], [], 
                '''                Logs Information
                ''',
                'logs',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process Name
                ''',
                'process_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node', REFERENCE_LIST, 'RemoteNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaS.RemoteLfa.RemoteNode', 
                [], [], 
                '''                Remote Node Information
                ''',
                'remote_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-statistic', REFERENCE_LIST, 'SessionStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaS.RemoteLfa.SessionStatistic', 
                [], [], 
                '''                RLFA Statistics categorized by session state
                ''',
                'session_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-lfa',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaS' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaS',
            False, 
            [
            _MetaInfoClassMember('remote-lfa', REFERENCE_LIST, 'RemoteLfa' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaS.RemoteLfa', 
                [], [], 
                '''                RemoteLFA
                ''',
                'remote_lfa',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-lfa-s',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.SessionStatistic' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.SessionStatistic',
            False, 
            [
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Path Count
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Path Count
                ''',
                'protected_path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Route Count
                ''',
                'protected_route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-label-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Label Count
                ''',
                'remote_label_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Route Count
                ''',
                'route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LDP Session Count
                ''',
                'session_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'RcmdShowLdpSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowLdpSessionStateEnum', 
                [], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'session-statistic',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.RemoteNode' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.RemoteNode',
            False, 
            [
            _MetaInfoClassMember('in-use-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Inuse time of the Session
                ''',
                'in_use_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsr-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Label Space Router ID
                ''',
                'lsr_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Path Count
                ''',
                'path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-path-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Path Count
                ''',
                'protected_path_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protected-route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Protected Route Count
                ''',
                'protected_route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-label-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Label Count
                ''',
                'remote_label_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Remote Node ID
                ''',
                'remote_node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Route Count
                ''',
                'route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-state', REFERENCE_ENUM_CLASS, 'RcmdShowLdpSessionStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowLdpSessionStateEnum', 
                [], [], 
                '''                Session State
                ''',
                'session_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('transport-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Transport Address
                ''',
                'transport_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-node',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.Logs' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.Logs',
            False, 
            [
            _MetaInfoClassMember('label-coverage-state', REFERENCE_ENUM_CLASS, 'RcmdShowLdpConvStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowLdpConvStateEnum', 
                [], [], 
                '''                Label Coverage State
                ''',
                'label_coverage_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('log-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event Time (eg: Apr 24 13:16:04.961)
                ''',
                'log_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-label-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Remote Label Count
                ''',
                'remote_label_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total Route Count
                ''',
                'route_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'logs',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary',
            False, 
            [
            _MetaInfoClassMember('event-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event ID
                ''',
                'event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('below-threshold', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Coverage Below Threshold
                ''',
                'below_threshold',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('end-of-calculation-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                End of IGP LFA Calculation Time (eg: Apr 24 13
                :16:04.961)
                ''',
                'end_of_calculation_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-id-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LDP-rLFA Event ID
                ''',
                'event_id_xr',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('igp-protocol', REFERENCE_ENUM_CLASS, 'RcmdProtocolIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdProtocolIdEnum', 
                [], [], 
                '''                IGP Protocol
                ''',
                'igp_protocol',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ipfrr-event-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                IGP IP-FRR Event ID (ref:
                rcmd_show_ipfrr_event_info(EventID))
                ''',
                'ipfrr_event_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('logs', REFERENCE_LIST, 'Logs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.Logs', 
                [], [], 
                '''                Logs Information
                ''',
                'logs',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process Name
                ''',
                'process_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-node', REFERENCE_LIST, 'RemoteNode' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.RemoteNode', 
                [], [], 
                '''                Remote Node Information
                ''',
                'remote_node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('session-statistic', REFERENCE_LIST, 'SessionStatistic' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.SessionStatistic', 
                [], [], 
                '''                RLFA Statistics categorized by session state
                ''',
                'session_statistic',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-lfa-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp.RemoteLfaSummaries' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp.RemoteLfaSummaries',
            False, 
            [
            _MetaInfoClassMember('remote-lfa-summary', REFERENCE_LIST, 'RemoteLfaSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary', 
                [], [], 
                '''                Summary operational data for Remote LFA
                ''',
                'remote_lfa_summary',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'remote-lfa-summaries',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Ldp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Ldp',
            False, 
            [
            _MetaInfoClassMember('remote-lfa-s', REFERENCE_CLASS, 'RemoteLfaS' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaS', 
                [], [], 
                '''                Remote LFA Coverage Events
                ''',
                'remote_lfa_s',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('remote-lfa-summaries', REFERENCE_CLASS, 'RemoteLfaSummaries' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.RemoteLfaSummaries', 
                [], [], 
                '''                Remote LFA Coverage Events
                ''',
                'remote_lfa_summaries',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp.Sessions', 
                [], [], 
                '''                Session Events
                ''',
                'sessions',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Intf.Events.Event' : {
        'meta_info' : _MetaInfoClass('Rcmd.Intf.Events.Event',
            False, 
            [
            _MetaInfoClassMember('event-no', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specific Event No.
                ''',
                'event_no',
                'Cisco-IOS-XR-infra-rcmd-oper', True),
            _MetaInfoClassMember('component', REFERENCE_ENUM_CLASS, 'RcmdShowCompIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowCompIdEnum', 
                [], [], 
                '''                Component info
                ''',
                'component',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Event Time
                ''',
                'event_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('event-type', REFERENCE_ENUM_CLASS, 'RcmdShowIntfEventEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowIntfEventEnum', 
                [], [], 
                '''                Event Info
                ''',
                'event_type',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('primary-address', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                Primary Address
                ''',
                'primary_address',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('sequence-no', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sequence No
                ''',
                'sequence_no',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'event',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Intf.Events' : {
        'meta_info' : _MetaInfoClass('Rcmd.Intf.Events',
            False, 
            [
            _MetaInfoClassMember('event', REFERENCE_LIST, 'Event' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Intf.Events.Event', 
                [], [], 
                '''                Events
                ''',
                'event',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'events',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Intf' : {
        'meta_info' : _MetaInfoClass('Rcmd.Intf',
            False, 
            [
            _MetaInfoClassMember('events', REFERENCE_CLASS, 'Events' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Intf.Events', 
                [], [], 
                '''                Events
                ''',
                'events',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'intf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Isis.Process_.InstanceName.Instance' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Isis.Process_.InstanceName.Instance',
            False, 
            [
            _MetaInfoClassMember('arch-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                spf run can be archived
                ''',
                'arch_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fwd-referenced', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Forward Referenced
                ''',
                'fwd_referenced',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-deleted', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Instance Deleted
                ''',
                'instance_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance Id
                ''',
                'instance_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-state', REFERENCE_ENUM_CLASS, 'RcmdShowInstStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowInstStateEnum', 
                [], [], 
                '''                Instance State
                ''',
                'instance_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Updated Time
                ''',
                'last_update_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('no-route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Route change spf nos
                ''',
                'no_route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node Id
                ''',
                'node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('not-interested-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Not Interested SPF nos
                ''',
                'not_interested_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route change spf nos
                ''',
                'route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Offset
                ''',
                'spf_offset',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spf nos
                ''',
                'total_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spt-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spt nos
                ''',
                'total_spt_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Isis.Process_.InstanceName' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Isis.Process_.InstanceName',
            False, 
            [
            _MetaInfoClassMember('arch-lsp-regeneration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive Lsp regen
                ''',
                'arch_lsp_regeneration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('arch-spf-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive SPF event
                ''',
                'arch_spf_event',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Isis.Process_.InstanceName.Instance', 
                [], [], 
                '''                Instance Information
                ''',
                'instance',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Updated Time
                ''',
                'last_update_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regeneration-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Regen Count
                ''',
                'lsp_regeneration_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regeneration-serial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Serial
                ''',
                'lsp_regeneration_serial',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance Name
                ''',
                'name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('no-route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Route change spf nos
                ''',
                'no_route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('not-interested-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Not Interested SPF nos
                ''',
                'not_interested_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route change spf nos
                ''',
                'route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spf nos
                ''',
                'total_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Isis.Process_' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Isis.Process_',
            False, 
            [
            _MetaInfoClassMember('instance-name', REFERENCE_LIST, 'InstanceName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Isis.Process_.InstanceName', 
                [], [], 
                '''                Instance/VRF Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process Name
                ''',
                'process_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protocol-id', REFERENCE_ENUM_CLASS, 'RcmdProtocolIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdProtocolIdEnum', 
                [], [], 
                '''                Protocol id
                ''',
                'protocol_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Isis' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Isis',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Isis.Process_', 
                [], [], 
                '''                Process Information
                ''',
                'process',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'isis',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ospf.Process_.InstanceName.Instance' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ospf.Process_.InstanceName.Instance',
            False, 
            [
            _MetaInfoClassMember('arch-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                spf run can be archived
                ''',
                'arch_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fwd-referenced', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Forward Referenced
                ''',
                'fwd_referenced',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-deleted', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Instance Deleted
                ''',
                'instance_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance Id
                ''',
                'instance_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-state', REFERENCE_ENUM_CLASS, 'RcmdShowInstStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowInstStateEnum', 
                [], [], 
                '''                Instance State
                ''',
                'instance_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Updated Time
                ''',
                'last_update_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('no-route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Route change spf nos
                ''',
                'no_route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node Id
                ''',
                'node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('not-interested-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Not Interested SPF nos
                ''',
                'not_interested_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route change spf nos
                ''',
                'route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Offset
                ''',
                'spf_offset',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spf nos
                ''',
                'total_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spt-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spt nos
                ''',
                'total_spt_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ospf.Process_.InstanceName' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ospf.Process_.InstanceName',
            False, 
            [
            _MetaInfoClassMember('arch-lsp-regeneration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive Lsp regen
                ''',
                'arch_lsp_regeneration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('arch-spf-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive SPF event
                ''',
                'arch_spf_event',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ospf.Process_.InstanceName.Instance', 
                [], [], 
                '''                Instance Information
                ''',
                'instance',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Updated Time
                ''',
                'last_update_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regeneration-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Regen Count
                ''',
                'lsp_regeneration_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regeneration-serial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Serial
                ''',
                'lsp_regeneration_serial',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance Name
                ''',
                'name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('no-route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Route change spf nos
                ''',
                'no_route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('not-interested-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Not Interested SPF nos
                ''',
                'not_interested_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route change spf nos
                ''',
                'route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spf nos
                ''',
                'total_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ospf.Process_' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ospf.Process_',
            False, 
            [
            _MetaInfoClassMember('instance-name', REFERENCE_LIST, 'InstanceName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ospf.Process_.InstanceName', 
                [], [], 
                '''                Instance/VRF Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process Name
                ''',
                'process_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protocol-id', REFERENCE_ENUM_CLASS, 'RcmdProtocolIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdProtocolIdEnum', 
                [], [], 
                '''                Protocol id
                ''',
                'protocol_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ospf' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ospf',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ospf.Process_', 
                [], [], 
                '''                Process Information
                ''',
                'process',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ospf',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ldp.Process_.InstanceName.Instance' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ldp.Process_.InstanceName.Instance',
            False, 
            [
            _MetaInfoClassMember('arch-spf-run', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                spf run can be archived
                ''',
                'arch_spf_run',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('fwd-referenced', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Forward Referenced
                ''',
                'fwd_referenced',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-deleted', REFERENCE_ENUM_CLASS, 'RcmdBoolYesNoEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdBoolYesNoEnum', 
                [], [], 
                '''                Instance Deleted
                ''',
                'instance_deleted',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Instance Id
                ''',
                'instance_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance-state', REFERENCE_ENUM_CLASS, 'RcmdShowInstStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdShowInstStateEnum', 
                [], [], 
                '''                Instance State
                ''',
                'instance_state',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Updated Time
                ''',
                'last_update_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('no-route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Route change spf nos
                ''',
                'no_route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Node Id
                ''',
                'node_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('not-interested-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Not Interested SPF nos
                ''',
                'not_interested_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route change spf nos
                ''',
                'route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('spf-offset', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                SPF Offset
                ''',
                'spf_offset',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spf nos
                ''',
                'total_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spt-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spt nos
                ''',
                'total_spt_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ldp.Process_.InstanceName' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ldp.Process_.InstanceName',
            False, 
            [
            _MetaInfoClassMember('arch-lsp-regeneration', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive Lsp regen
                ''',
                'arch_lsp_regeneration',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('arch-spf-event', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Archive SPF event
                ''',
                'arch_spf_event',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('instance', REFERENCE_LIST, 'Instance' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ldp.Process_.InstanceName.Instance', 
                [], [], 
                '''                Instance Information
                ''',
                'instance',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('last-update-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Updated Time
                ''',
                'last_update_time',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regeneration-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                LSP Regen Count
                ''',
                'lsp_regeneration_count',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('lsp-regeneration-serial', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Last Serial
                ''',
                'lsp_regeneration_serial',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance Name
                ''',
                'name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('no-route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No Route change spf nos
                ''',
                'no_route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('not-interested-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Not Interested SPF nos
                ''',
                'not_interested_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('route-change-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Route change spf nos
                ''',
                'route_change_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('total-spf-nos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total spf nos
                ''',
                'total_spf_nos',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'instance-name',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ldp.Process_' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ldp.Process_',
            False, 
            [
            _MetaInfoClassMember('instance-name', REFERENCE_LIST, 'InstanceName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ldp.Process_.InstanceName', 
                [], [], 
                '''                Instance/VRF Name
                ''',
                'instance_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Process Name
                ''',
                'process_name',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('protocol-id', REFERENCE_ENUM_CLASS, 'RcmdProtocolIdEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'RcmdProtocolIdEnum', 
                [], [], 
                '''                Protocol id
                ''',
                'protocol_id',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process.Ldp' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process.Ldp',
            False, 
            [
            _MetaInfoClassMember('process', REFERENCE_LIST, 'Process_' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ldp.Process_', 
                [], [], 
                '''                Process Information
                ''',
                'process',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'ldp',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd.Process' : {
        'meta_info' : _MetaInfoClass('Rcmd.Process',
            False, 
            [
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Isis', 
                [], [], 
                '''                ISIS Process Information
                ''',
                'isis',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp', REFERENCE_CLASS, 'Ldp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ldp', 
                [], [], 
                '''                LDP Process Information
                ''',
                'ldp',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process.Ospf', 
                [], [], 
                '''                OSPF Process Information
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'process',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
    'Rcmd' : {
        'meta_info' : _MetaInfoClass('Rcmd',
            False, 
            [
            _MetaInfoClassMember('intf', REFERENCE_CLASS, 'Intf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Intf', 
                [], [], 
                '''                Interface data
                ''',
                'intf',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('isis', REFERENCE_CLASS, 'Isis' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Isis', 
                [], [], 
                '''                Operational data for ISIS
                ''',
                'isis',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ldp', REFERENCE_CLASS, 'Ldp' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ldp', 
                [], [], 
                '''                LDP data
                ''',
                'ldp',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('memory', REFERENCE_CLASS, 'Memory' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Memory', 
                [], [], 
                '''                Memory Info
                ''',
                'memory',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('node', REFERENCE_CLASS, 'Node' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Node', 
                [], [], 
                '''                Node Info
                ''',
                'node',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('ospf', REFERENCE_CLASS, 'Ospf' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Ospf', 
                [], [], 
                '''                Operational data for OSPF
                ''',
                'ospf',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('process', REFERENCE_CLASS, 'Process' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Process', 
                [], [], 
                '''                Process information
                ''',
                'process',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            _MetaInfoClassMember('server', REFERENCE_CLASS, 'Server' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper', 'Rcmd.Server', 
                [], [], 
                '''                Server Info
                ''',
                'server',
                'Cisco-IOS-XR-infra-rcmd-oper', False),
            ],
            'Cisco-IOS-XR-infra-rcmd-oper',
            'rcmd',
            _yang_ns._namespaces['Cisco-IOS-XR-infra-rcmd-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_infra_rcmd_oper'
        ),
    },
}
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventStatistics']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LdpExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LsdExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.ConvergenceTimeline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksAdded']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority.LeafNetworksDeleted']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.Priority']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksAdded']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority.LeafNetworksDeleted']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal.Priority']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.DijkstraRun']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary.InterAreaAndExternal']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RouteOrigin']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Enter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Exit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.RiBv4Redistribute']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LdpExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LsdExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.ConvergenceTimeline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksAdded']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority.LeafNetworksDeleted']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.Priority']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RouteOrigin']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Enter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Exit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.RiBv4Redistribute']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LdpExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdEnter']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LsdExit']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.ConvergenceTimeline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksAdded']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority.LeafNetworksDeleted']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal.Priority']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.DijkstraRun']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline.InterAreaAndExternal']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path.LfaPath']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.Path']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.TimeLine']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries.SummaryExternalEventSummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path.LfaPath']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.Path']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.TimeLine']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines.SummaryExternalEventOffline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventSummaries']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunSummaries']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.IpfrrEventOfflines']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SpfRunOfflines']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventSummaries']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventSummaries']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventOfflines']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.PrefixEventOfflines']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance.SummaryExternalEventStatistics']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info']
_meta_table['Rcmd.Ospf.Instances.Instance']['meta_info'].parent =_meta_table['Rcmd.Ospf.Instances']['meta_info']
_meta_table['Rcmd.Ospf.Instances']['meta_info'].parent =_meta_table['Rcmd.Ospf']['meta_info']
_meta_table['Rcmd.Server.Normal.ProtocolConfig.Priority']['meta_info'].parent =_meta_table['Rcmd.Server.Normal.ProtocolConfig']['meta_info']
_meta_table['Rcmd.Server.Normal.ServerDetail.TraceInformation']['meta_info'].parent =_meta_table['Rcmd.Server.Normal.ServerDetail']['meta_info']
_meta_table['Rcmd.Server.Normal.ProtocolConfig']['meta_info'].parent =_meta_table['Rcmd.Server.Normal']['meta_info']
_meta_table['Rcmd.Server.Normal.ServerDetail']['meta_info'].parent =_meta_table['Rcmd.Server.Normal']['meta_info']
_meta_table['Rcmd.Server.Detail.ProtocolConfig.Priority']['meta_info'].parent =_meta_table['Rcmd.Server.Detail.ProtocolConfig']['meta_info']
_meta_table['Rcmd.Server.Detail.ServerDetail.TraceInformation']['meta_info'].parent =_meta_table['Rcmd.Server.Detail.ServerDetail']['meta_info']
_meta_table['Rcmd.Server.Detail.ProtocolConfig']['meta_info'].parent =_meta_table['Rcmd.Server.Detail']['meta_info']
_meta_table['Rcmd.Server.Detail.ServerDetail']['meta_info'].parent =_meta_table['Rcmd.Server.Detail']['meta_info']
_meta_table['Rcmd.Server.Normal']['meta_info'].parent =_meta_table['Rcmd.Server']['meta_info']
_meta_table['Rcmd.Server.Detail']['meta_info'].parent =_meta_table['Rcmd.Server']['meta_info']
_meta_table['Rcmd.Node.NodeInformation']['meta_info'].parent =_meta_table['Rcmd.Node']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode.PrimaryPath']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.IpfrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary.RemoteNode']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries.IpfrrEventSummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventStatistics.PrefixEventStatistic']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventStatistics']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RouteOrigin']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Enter']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Exit']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.RiBv4Redistribute']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpEnter']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LdpExit']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdEnter']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LsdExit']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcIp']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.ConvergenceTimeline']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksAdded']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority.LeafNetworksDeleted']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.SpfSummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.NodeStatistics']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.TriggerLsp']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.Priority']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspProcessed']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary.LspRegenerated']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries.SpfRunSummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode.PrimaryPath']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.IpfrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline.RemoteNode']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines.IpfrrEventOffline']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.RouteStatistics']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary.FrrStatistic']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls.FibComplete']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RouteOrigin']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Enter']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Exit']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.RiBv4Redistribute']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpEnter']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LdpExit']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdEnter']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LsdExit']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcIp']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.PrioritySummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.ConvergenceTimeline']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksAdded']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority.LeafNetworksDeleted']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.SpfSummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.NodeStatistics']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.TriggerLsp']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.Priority']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspProcessed']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline.LspRegenerated']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines.SpfRunOffline']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path.LfaPath']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcIp']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.Path']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.TimeLine']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries.PrefixEventSummary']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path.LfaPath']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcIp']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine.LcMpls']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.IpConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.MplsConvergenceTime']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.Path']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TriggerLsa']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.TimeLine']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline.LsaProcessed']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines.PrefixEventOffline']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.LspRegenerateds.LspRegenerated']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance.LspRegenerateds']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventSummaries']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventStatistics']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunSummaries']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.IpfrrEventOfflines']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.SpfRunOfflines']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventSummaries']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.PrefixEventOfflines']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance.LspRegenerateds']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances.Instance']['meta_info']
_meta_table['Rcmd.Isis.Instances.Instance']['meta_info'].parent =_meta_table['Rcmd.Isis.Instances']['meta_info']
_meta_table['Rcmd.Isis.Instances']['meta_info'].parent =_meta_table['Rcmd.Isis']['meta_info']
_meta_table['Rcmd.Memory.MemoryInfo']['meta_info'].parent =_meta_table['Rcmd.Memory']['meta_info']
_meta_table['Rcmd.Memory.EdmMemoryInfo']['meta_info'].parent =_meta_table['Rcmd.Memory']['meta_info']
_meta_table['Rcmd.Memory.StringMemoryInfo']['meta_info'].parent =_meta_table['Rcmd.Memory']['meta_info']
_meta_table['Rcmd.Ldp.Sessions.Session']['meta_info'].parent =_meta_table['Rcmd.Ldp.Sessions']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaS.RemoteLfa.SessionStatistic']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaS.RemoteLfa']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaS.RemoteLfa.RemoteNode']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaS.RemoteLfa']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaS.RemoteLfa.Logs']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaS.RemoteLfa']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaS.RemoteLfa']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaS']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.SessionStatistic']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.RemoteNode']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary.Logs']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaSummaries.RemoteLfaSummary']['meta_info'].parent =_meta_table['Rcmd.Ldp.RemoteLfaSummaries']['meta_info']
_meta_table['Rcmd.Ldp.Sessions']['meta_info'].parent =_meta_table['Rcmd.Ldp']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaS']['meta_info'].parent =_meta_table['Rcmd.Ldp']['meta_info']
_meta_table['Rcmd.Ldp.RemoteLfaSummaries']['meta_info'].parent =_meta_table['Rcmd.Ldp']['meta_info']
_meta_table['Rcmd.Intf.Events.Event']['meta_info'].parent =_meta_table['Rcmd.Intf.Events']['meta_info']
_meta_table['Rcmd.Intf.Events']['meta_info'].parent =_meta_table['Rcmd.Intf']['meta_info']
_meta_table['Rcmd.Process.Isis.Process_.InstanceName.Instance']['meta_info'].parent =_meta_table['Rcmd.Process.Isis.Process_.InstanceName']['meta_info']
_meta_table['Rcmd.Process.Isis.Process_.InstanceName']['meta_info'].parent =_meta_table['Rcmd.Process.Isis.Process_']['meta_info']
_meta_table['Rcmd.Process.Isis.Process_']['meta_info'].parent =_meta_table['Rcmd.Process.Isis']['meta_info']
_meta_table['Rcmd.Process.Ospf.Process_.InstanceName.Instance']['meta_info'].parent =_meta_table['Rcmd.Process.Ospf.Process_.InstanceName']['meta_info']
_meta_table['Rcmd.Process.Ospf.Process_.InstanceName']['meta_info'].parent =_meta_table['Rcmd.Process.Ospf.Process_']['meta_info']
_meta_table['Rcmd.Process.Ospf.Process_']['meta_info'].parent =_meta_table['Rcmd.Process.Ospf']['meta_info']
_meta_table['Rcmd.Process.Ldp.Process_.InstanceName.Instance']['meta_info'].parent =_meta_table['Rcmd.Process.Ldp.Process_.InstanceName']['meta_info']
_meta_table['Rcmd.Process.Ldp.Process_.InstanceName']['meta_info'].parent =_meta_table['Rcmd.Process.Ldp.Process_']['meta_info']
_meta_table['Rcmd.Process.Ldp.Process_']['meta_info'].parent =_meta_table['Rcmd.Process.Ldp']['meta_info']
_meta_table['Rcmd.Process.Isis']['meta_info'].parent =_meta_table['Rcmd.Process']['meta_info']
_meta_table['Rcmd.Process.Ospf']['meta_info'].parent =_meta_table['Rcmd.Process']['meta_info']
_meta_table['Rcmd.Process.Ldp']['meta_info'].parent =_meta_table['Rcmd.Process']['meta_info']
_meta_table['Rcmd.Ospf']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
_meta_table['Rcmd.Server']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
_meta_table['Rcmd.Node']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
_meta_table['Rcmd.Isis']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
_meta_table['Rcmd.Memory']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
_meta_table['Rcmd.Ldp']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
_meta_table['Rcmd.Intf']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
_meta_table['Rcmd.Process']['meta_info'].parent =_meta_table['Rcmd']['meta_info']
