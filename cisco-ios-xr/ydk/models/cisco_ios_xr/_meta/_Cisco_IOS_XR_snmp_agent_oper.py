


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'SnmpCorrRuleStateEnum' : _MetaInfoEnum('SnmpCorrRuleStateEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper',
        {
            'rule-unapplied':'rule_unapplied',
            'rule-applied':'rule_applied',
            'rule-applied-all':'rule_applied_all',
        }, 'Cisco-IOS-XR-snmp-agent-oper', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper']),
    'SnmpCorrVbindMatchEnum' : _MetaInfoEnum('SnmpCorrVbindMatchEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper',
        {
            'index':'index',
            'value':'value',
        }, 'Cisco-IOS-XR-snmp-agent-oper', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper']),
    'DupReqDropStatusEnum' : _MetaInfoEnum('DupReqDropStatusEnum', 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper',
        {
            'disabled':'disabled',
            'enabled':'enabled',
        }, 'Cisco-IOS-XR-snmp-agent-oper', _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper']),
    'Snmp.TrapServers.TrapServer' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapServers.TrapServer',
            False, 
            [
            _MetaInfoClassMember('max-q-length-of-trap-q', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Maximum Queue length of trapQ
                ''',
                'max_q_length_of_trap_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('number-of-pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of trap packets dropped
                ''',
                'number_of_pkts_dropped',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('number-of-pkts-in-trap-q', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of trap packets in trapQ
                ''',
                'number_of_pkts_in_trap_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('number-of-pkts-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                No. of trap packets sent
                ''',
                'number_of_pkts_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Trap port
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trap Host
                ''',
                'trap_host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-server',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.TrapServers' : {
        'meta_info' : _MetaInfoClass('Snmp.TrapServers',
            False, 
            [
            _MetaInfoClassMember('trap-server', REFERENCE_LIST, 'TrapServer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.TrapServers.TrapServer', 
                [], [], 
                '''                Trap server and port to which the trap is to be
                sent and statistics
                ''',
                'trap_server',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-servers',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Hosts.Host.HostInformation' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Hosts.Host.HostInformation',
            False, 
            [
            _MetaInfoClassMember('user', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMP host user
                ''',
                'user',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('snmp-target-address-port', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Target UDP port
                ''',
                'snmp_target_address_port',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('snmp-target-address-t-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Transport type of address
                ''',
                'snmp_target_address_t_host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('snmp-target-addresstype', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Target host type (Inform or Trap)
                ''',
                'snmp_target_addresstype',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('snmp-target-params-security-level', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Security level
                ''',
                'snmp_target_params_security_level',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('snmp-target-params-security-model', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Security model
                ''',
                'snmp_target_params_security_model',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('snmp-target-params-security-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Security name
                ''',
                'snmp_target_params_security_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'host-information',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Hosts.Host' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Hosts.Host',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('host-information', REFERENCE_LIST, 'HostInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Hosts.Host.HostInformation', 
                [], [], 
                '''                Host name ,udp-port , user, security model
                and level
                ''',
                'host_information',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Hosts' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Hosts',
            False, 
            [
            _MetaInfoClassMember('host', REFERENCE_LIST, 'Host' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Hosts.Host', 
                [], [], 
                '''                SNMP target host name
                ''',
                'host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'hosts',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.SystemUpTime' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.SystemUpTime',
            False, 
            [
            _MetaInfoClassMember('system-up-time-edm', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                sysUpTime  1.3.6.1.2.1.1.3
                ''',
                'system_up_time_edm',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'system-up-time',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.NmsAddresses.NmsAddress' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.NmsAddresses.NmsAddress',
            False, 
            [
            _MetaInfoClassMember('nms-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                NMS address
                ''',
                'nms_addr',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('get-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Get Request Count
                ''',
                'get_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('getbulk-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Getbulk Request Count
                ''',
                'getbulk_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('getnext-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Getnext Request Count
                ''',
                'getnext_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('nms-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NMS address of server
                ''',
                'nms_address',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('set-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Set Request Count
                ''',
                'set_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('test-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Test Request Count
                ''',
                'test_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'nms-address',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.NmsAddresses' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.NmsAddresses',
            False, 
            [
            _MetaInfoClassMember('nms-address', REFERENCE_LIST, 'NmsAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.NmsAddresses.NmsAddress', 
                [], [], 
                '''                NMS address
                ''',
                'nms_address',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'nms-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.EngineId' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.EngineId',
            False, 
            [
            _MetaInfoClassMember('engine-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                SNMPv3 engineID
                ''',
                'engine_id',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'engine-id',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.RxQueue' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.RxQueue',
            False, 
            [
            _MetaInfoClassMember('in-avg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                in avg
                ''',
                'in_avg',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('in-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                in max
                ''',
                'in_max',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('in-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                in min
                ''',
                'in_min',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('incoming-q', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                incomingQ
                ''',
                'incoming_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('pend-avg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pend avg
                ''',
                'pend_avg',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('pend-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pend max
                ''',
                'pend_max',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('pend-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                pend min
                ''',
                'pend_min',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('pending-q', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                pendingQ
                ''',
                'pending_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('qlen', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                qlen
                ''',
                'qlen',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'rx-queue',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.SystemName' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.SystemName',
            False, 
            [
            _MetaInfoClassMember('system-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                sysName  1.3.6.1.2.1.1.5
                ''',
                'system_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'system-name',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress',
            False, 
            [
            _MetaInfoClassMember('nms-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                NMS address
                ''',
                'nms_addr',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('agent-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Processing agent request count for each client
                for particluar managment station
                ''',
                'agent_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('entity-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Processing entity request count for each client
                for particluar managment station
                ''',
                'entity_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('infra-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Processing infra request count for each client
                for particluar Managment station
                ''',
                'infra_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('interface-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Processing interfce request count for each
                client for particluar managment station
                ''',
                'interface_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('route-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Processing route request count for each client
                for particluar Managment station
                ''',
                'route_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('total-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total request count for each managment station
                or client
                ''',
                'total_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'nms-address',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.RequestTypeDetail.NmsAddresses' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.RequestTypeDetail.NmsAddresses',
            False, 
            [
            _MetaInfoClassMember('nms-address', REFERENCE_LIST, 'NmsAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress', 
                [], [], 
                '''                NMS address
                ''',
                'nms_address',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'nms-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.RequestTypeDetail' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.RequestTypeDetail',
            False, 
            [
            _MetaInfoClassMember('nms-addresses', REFERENCE_CLASS, 'NmsAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.RequestTypeDetail.NmsAddresses', 
                [], [], 
                '''                snmp request type details 
                ''',
                'nms_addresses',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'request-type-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.DuplicateDrop' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.DuplicateDrop',
            False, 
            [
            _MetaInfoClassMember('duplicate-drop-configured-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured Duplicate Drop feature Timeout.
                ''',
                'duplicate_drop_configured_timeout',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('duplicate-drop-disable-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of times duplicate request drop feature
                is disabled.
                ''',
                'duplicate_drop_disable_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('duplicate-drop-enable-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Number of times duplicate request drop feature
                is enabled.
                ''',
                'duplicate_drop_enable_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('duplicate-dropped-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of duplicate SNMP requests are dropped.
                ''',
                'duplicate_dropped_requests',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('duplicate-request-latest-enable-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duplicate request drop feature last enable
                time(Day Mon Date HH:MM:SS)
                ''',
                'duplicate_request_latest_enable_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('duplicate-request-status', REFERENCE_ENUM_CLASS, 'DupReqDropStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'DupReqDropStatusEnum', 
                [], [], 
                '''                Duplicate requests drop feature status.
                ''',
                'duplicate_request_status',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('first-enable-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duplicate request drop feature first  enable
                time (Day Mon Date HH:MM:SS)
                ''',
                'first_enable_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('last-status-change-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Duplicate request drop feature last enable
                disable time (Day Mon Date HH:MM:SS)
                ''',
                'last_status_change_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('latest-duplicate-dropped-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of duplicate SNMP requests dropped, from
                the last enable time.
                ''',
                'latest_duplicate_dropped_requests',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('latest-retry-processed-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of retry SNMP requests processed, from
                the last enable time.
                ''',
                'latest_retry_processed_requests',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('retry-processed-requests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Retry SNMP requests are Processed.
                ''',
                'retry_processed_requests',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'duplicate-drop',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.BulkStatsTransfers.BulkStatsTransfer' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.BulkStatsTransfers.BulkStatsTransfer',
            False, 
            [
            _MetaInfoClassMember('transfer-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Transfer name
                ''',
                'transfer_name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('retained-file', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bulkstats transfer retained file name
                ''',
                'retained_file',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('retry-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bulkstats transfer retry attempt left
                ''',
                'retry_left',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('time-left', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Bulkstats transfer retry time left in seconds
                ''',
                'time_left',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('transfer-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the bulkstats transfer session
                ''',
                'transfer_name_xr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('url-primary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bulkstats transfer primary URL
                ''',
                'url_primary',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('url-secondary', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Bulkstats transfer secondary URL
                ''',
                'url_secondary',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'bulk-stats-transfer',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.BulkStatsTransfers' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.BulkStatsTransfers',
            False, 
            [
            _MetaInfoClassMember('bulk-stats-transfer', REFERENCE_LIST, 'BulkStatsTransfer' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.BulkStatsTransfers.BulkStatsTransfer', 
                [], [], 
                '''                SNMP bulkstats transfer name
                ''',
                'bulk_stats_transfer',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'bulk-stats-transfers',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of traps sent
                ''',
                'count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('drop-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Traps Dropped
                ''',
                'drop_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('lasrdrop-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp of latest droped
                ''',
                'lasrdrop_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('lastsent-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp of latest successfully sent
                ''',
                'lastsent_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Num of times retry
                ''',
                'retry_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TRAP OID
                ''',
                'trap_oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-oi-dinfo',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.TrapInfos.TrapInfo' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.TrapInfos.TrapInfo',
            False, 
            [
            _MetaInfoClassMember('host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NMS/Host address
                ''',
                'host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Trap port
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                udp port number
                ''',
                'port_xr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trap Host
                ''',
                'trap_host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oi-dinfo', REFERENCE_LIST, 'TrapOiDinfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo', 
                [], [], 
                '''                Per trap OID statistics
                ''',
                'trap_oi_dinfo',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of OID's sent
                ''',
                'trap_oid_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-info',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.TrapInfos' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.TrapInfos',
            False, 
            [
            _MetaInfoClassMember('trap-info', REFERENCE_LIST, 'TrapInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.TrapInfos.TrapInfo', 
                [], [], 
                '''                SNMP Trap infomation like server , port and
                trapOID
                ''',
                'trap_info',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-infos',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.PollOids.PollOid' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.PollOids.PollOid',
            False, 
            [
            _MetaInfoClassMember('object-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Object ID
                ''',
                'object_id',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('nms', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                Network Managment station ipadress
                ''',
                'nms',
                'Cisco-IOS-XR-snmp-agent-oper', False, max_elements=15),
            _MetaInfoClassMember('nms-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 Managment station count
                ''',
                'nms_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('request-count', REFERENCE_LEAFLIST, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                OID request count for each Managment station 
                ''',
                'request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False, max_elements=15),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'poll-oid',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.PollOids' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.PollOids',
            False, 
            [
            _MetaInfoClassMember('poll-oid', REFERENCE_LIST, 'PollOid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.PollOids.PollOid', 
                [], [], 
                '''                PDU drop info for OID
                ''',
                'poll_oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'poll-oids',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo',
            False, 
            [
            _MetaInfoClassMember('count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of traps sent
                ''',
                'count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('drop-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of Traps Dropped
                ''',
                'drop_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('lasrdrop-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp of latest droped
                ''',
                'lasrdrop_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('lastsent-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Timestamp of latest successfully sent
                ''',
                'lastsent_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('retry-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Num of times retry
                ''',
                'retry_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TRAP OID
                ''',
                'trap_oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-oi-dinfo',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.InfomDetails.InfomDetail' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.InfomDetails.InfomDetail',
            False, 
            [
            _MetaInfoClassMember('host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NMS/Host address
                ''',
                'host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Trap port
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                udp port number
                ''',
                'port_xr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-host', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Trap Host
                ''',
                'trap_host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oi-dinfo', REFERENCE_LIST, 'TrapOiDinfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo', 
                [], [], 
                '''                Per trap OID statistics
                ''',
                'trap_oi_dinfo',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of OID's sent
                ''',
                'trap_oid_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'infom-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.InfomDetails' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.InfomDetails',
            False, 
            [
            _MetaInfoClassMember('infom-detail', REFERENCE_LIST, 'InfomDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.InfomDetails.InfomDetail', 
                [], [], 
                '''                SNMP Trap infomation like server , port and
                trapOID
                ''',
                'infom_detail',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'infom-details',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Statistics' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Statistics',
            False, 
            [
            _MetaInfoClassMember('asn-parse-errors-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInASNParseErrs
                ''',
                'asn_parse_errors_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('bad-community-names-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInBadCommunityNames
                ''',
                'bad_community_names_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('bad-community-uses-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInBadCommunityUses
                ''',
                'bad_community_uses_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('bad-values-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInBadValues
                ''',
                'bad_values_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('bad-values-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutBadValues
                ''',
                'bad_values_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('bad-versions-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInBadVersions
                ''',
                'bad_versions_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('general-errors-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutGenErrs
                ''',
                'general_errors_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('get-next-request-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutGetNexts
                ''',
                'get_next_request_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('get-next-requests-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInGetNexts
                ''',
                'get_next_requests_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('get-requests-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInGetRequests
                ''',
                'get_requests_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('get-requests-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutGetRequests
                ''',
                'get_requests_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('get-responses-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInGetResponses
                ''',
                'get_responses_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('get-responses-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutGetResponses
                ''',
                'get_responses_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('max-packet-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmp maximum packet size
                ''',
                'max_packet_size',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('no-such-names-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInNoSuchNames
                ''',
                'no_such_names_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('no-such-names-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutNoSuchNames
                ''',
                'no_such_names_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('packets-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInPkts
                ''',
                'packets_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('proxy-drop-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpProxyDrops
                ''',
                'proxy_drop_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('read-only-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInReadOnlys
                ''',
                'read_only_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('set-requests-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInSetRequests
                ''',
                'set_requests_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('set-requests-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutSetRequests
                ''',
                'set_requests_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('silent-drop-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpSilentDrops
                ''',
                'silent_drop_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('too-big-packet-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInTooBigs
                ''',
                'too_big_packet_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('too-big-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutTooBigs
                ''',
                'too_big_packets_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('total-general-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInGenErrs
                ''',
                'total_general_errors',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('total-packets-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutPkts
                ''',
                'total_packets_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('total-requested-variables', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInTotalReqVars
                ''',
                'total_requested_variables',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('total-set-variables-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInTotalSetVars
                ''',
                'total_set_variables_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('traps-received', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpInTraps
                ''',
                'traps_received',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('traps-sent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                snmpOutTraps
                ''',
                'traps_sent',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'statistics',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.IncomingQueue.InqEntry' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.IncomingQueue.InqEntry',
            False, 
            [
            _MetaInfoClassMember('address-of-queue', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Address of NMS Q
                ''',
                'address_of_queue',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('last-access-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Last Access time of Each Queue.
                ''',
                'last_access_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('priority', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                Priority of Each Queue.
                ''',
                'priority',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('processed-request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Processed request Count.
                ''',
                'processed_request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('request-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Request Count of Each Queue.
                ''',
                'request_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'inq-entry',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.IncomingQueue' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.IncomingQueue',
            False, 
            [
            _MetaInfoClassMember('inq-entry', REFERENCE_LIST, 'InqEntry' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.IncomingQueue.InqEntry', 
                [], [], 
                '''                Each Entry Details.
                ''',
                'inq_entry',
                'Cisco-IOS-XR-snmp-agent-oper', False, max_elements=16),
            _MetaInfoClassMember('queue-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of NMS Queues Exist.
                ''',
                'queue_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'incoming-queue',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.ContextMapping.ContexMapping' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.ContextMapping.ContexMapping',
            False, 
            [
            _MetaInfoClassMember('context', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Context name
                ''',
                'context',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('feature', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Feature
                ''',
                'feature',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('feature-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Feature name
                ''',
                'feature_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('instance', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Instance name
                ''',
                'instance',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('topology', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Topology name
                ''',
                'topology',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'contex-mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.ContextMapping' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.ContextMapping',
            False, 
            [
            _MetaInfoClassMember('contex-mapping', REFERENCE_LIST, 'ContexMapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.ContextMapping.ContexMapping', 
                [], [], 
                '''                Context Mapping
                ''',
                'contex_mapping',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'context-mapping',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.TrapOids.TrapOid' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.TrapOids.TrapOid',
            False, 
            [
            _MetaInfoClassMember('trap-oid', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Trap object ID
                ''',
                'trap_oid',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('trap-oid-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Total number of OID's sent
                ''',
                'trap_oid_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oid-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                TRAP OID
                ''',
                'trap_oid_xr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-oid',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.TrapOids' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.TrapOids',
            False, 
            [
            _MetaInfoClassMember('trap-oid', REFERENCE_LIST, 'TrapOid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.TrapOids.TrapOid', 
                [], [], 
                '''                SNMP trap 
                ''',
                'trap_oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-oids',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.NmSpackets.NmSpacket' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.NmSpackets.NmSpacket',
            False, 
            [
            _MetaInfoClassMember('packetcount', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                NMS packet drop count
                ''',
                'packetcount',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('number-of-nmsq-pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets which are currently enqueued
                within the NMS queues
                ''',
                'number_of_nmsq_pkts_dropped',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('number-of-pkts-dropped', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of packets dropped
                ''',
                'number_of_pkts_dropped',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('overload-end-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time of overload contol End
                ''',
                'overload_end_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('overload-start-time', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Time of overload contol begin
                ''',
                'overload_start_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'nm-spacket',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.NmSpackets' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.NmSpackets',
            False, 
            [
            _MetaInfoClassMember('nm-spacket', REFERENCE_LIST, 'NmSpacket' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.NmSpackets.NmSpacket', 
                [], [], 
                '''                NMS packet drop count
                ''',
                'nm_spacket',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'nm-spackets',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Mibs.Mib.Oids.Oid' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Mibs.Mib.Oids.Oid',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Object Identifier
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('oid-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MIB OID Name
                ''',
                'oid_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'oid',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Mibs.Mib.Oids' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Mibs.Mib.Oids',
            False, 
            [
            _MetaInfoClassMember('oid', REFERENCE_LIST, 'Oid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Mibs.Mib.Oids.Oid', 
                [], [], 
                '''                Object identifiers of a mib
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'oids',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Mibs.Mib.MibInformation' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Mibs.Mib.MibInformation',
            False, 
            [
            _MetaInfoClassMember('dll-capabilities', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                DLL capabilities
                ''',
                'dll_capabilities',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('dll-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MIB DLL filename, non-DLL MIBs will have no
                value
                ''',
                'dll_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('is-mib-loaded', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE if MIB DLL is currently loaded, will always
                be TRUE for non-DLL MIBs
                ''',
                'is_mib_loaded',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('load-time', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Load time
                ''',
                'load_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('mib-config-filename', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                MIB config filename, non-DLL MIBs will have no
                value
                ''',
                'mib_config_filename',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('mib-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Name of the MIB module
                ''',
                'mib_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                TRUE is mib is in phase 1 timeout
                ''',
                'timeout',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-strings', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                List of trapstring configured
                ''',
                'trap_strings',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'mib-information',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Mibs.Mib' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Mibs.Mib',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                MIB Name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('mib-information', REFERENCE_CLASS, 'MibInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Mibs.Mib.MibInformation', 
                [], [], 
                '''                MIB state and information
                ''',
                'mib_information',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('oids', REFERENCE_CLASS, 'Oids' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Mibs.Mib.Oids', 
                [], [], 
                '''                List of OIDs per MIB
                ''',
                'oids',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'mib',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Mibs' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Mibs',
            False, 
            [
            _MetaInfoClassMember('mib', REFERENCE_LIST, 'Mib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Mibs.Mib', 
                [], [], 
                '''                SNMP MIB Name
                ''',
                'mib',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'mibs',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.SerialNumbers.SerialNumber' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.SerialNumbers.SerialNumber',
            False, 
            [
            _MetaInfoClassMember('error-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Is reques dropped due to error
                ''',
                'error_status',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('input-q', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Request inserted into input queue
                ''',
                'input_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('nms', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                 NMS address Rx PDU
                ''',
                'nms',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('number', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Serial number
                ''',
                'number',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('output-q', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                De-queue the request from the input queue
                ''',
                'output_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('pdu-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                 PDU type
                ''',
                'pdu_type',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('pending-q', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Enqueue the request into pending queue
                ''',
                'pending_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port-xr', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                NMS port number
                ''',
                'port_xr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('req-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Request ID
                ''',
                'req_id',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('request-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 SNMP request id per PDU
                ''',
                'request_id',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('response-out', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Response sent
                ''',
                'response_out',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('serial-num', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Serial number per PDU processing
                ''',
                'serial_num',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'serial-number',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.SerialNumbers' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.SerialNumbers',
            False, 
            [
            _MetaInfoClassMember('serial-number', REFERENCE_LIST, 'SerialNumber' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.SerialNumbers.SerialNumber', 
                [], [], 
                '''                Serial number
                ''',
                'serial_number',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'serial-numbers',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.DropNmsAddresses.DropNmsAddress' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.DropNmsAddresses.DropNmsAddress',
            False, 
            [
            _MetaInfoClassMember('nms-addr', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                NMS address
                ''',
                'nms_addr',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('aipc-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                drop count with AIPC Buffer Full
                ''',
                'aipc_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('duplicate-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Duplicate request drop count
                ''',
                'duplicate_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('encode-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop Count with Encode errors
                ''',
                'encode_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('incoming-q-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop Count at Incoming Q
                ''',
                'incoming_q_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('internal-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                 drop with Internal Errors
                ''',
                'internal_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('nms-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                NMS address of server
                ''',
                'nms_address',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('overload-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop Count with overload notification
                ''',
                'overload_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('stack-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop Count at snmp Stack
                ''',
                'stack_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('threshold-incoming-q-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop Count at Incoming Q after threshold limit
                ''',
                'threshold_incoming_q_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('timeout-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Drop count with timeout
                ''',
                'timeout_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'drop-nms-address',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.DropNmsAddresses' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.DropNmsAddresses',
            False, 
            [
            _MetaInfoClassMember('drop-nms-address', REFERENCE_LIST, 'DropNmsAddress' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.DropNmsAddresses.DropNmsAddress', 
                [], [], 
                '''                PDU drop info for NMS
                ''',
                'drop_nms_address',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'drop-nms-addresses',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Views.View.ViewInformation' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Views.View.ViewInformation',
            False, 
            [
            _MetaInfoClassMember('object-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMP view OID
                ''',
                'object_id',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('snmp-view-family-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Status of this entry
                ''',
                'snmp_view_family_status',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('snmp-view-family-storage-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Storage type
                ''',
                'snmp_view_family_storage_type',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('snmp-view-family-type', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Include or exclude
                ''',
                'snmp_view_family_type',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'view-information',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Views.View' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Views.View',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                View name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('view-information', REFERENCE_LIST, 'ViewInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Views.View.ViewInformation', 
                [], [], 
                '''                View name ,familytype, storagetype and status
                ''',
                'view_information',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'view',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Views' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Views',
            False, 
            [
            _MetaInfoClassMember('view', REFERENCE_LIST, 'View' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Views.View', 
                [], [], 
                '''                SNMP target view name
                ''',
                'view',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'views',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.SystemDescr' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.SystemDescr',
            False, 
            [
            _MetaInfoClassMember('sys-descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                sysDescr  1.3.6.1.2.1.1.1
                ''',
                'sys_descr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'system-descr',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation',
            False, 
            [
            _MetaInfoClassMember('level', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Level
                ''',
                'level',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('modelnumber', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Model number
                ''',
                'modelnumber',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('vacm-access-notify-view-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Notify view name
                ''',
                'vacm_access_notify_view_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('vacm-access-read-view-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Read view name
                ''',
                'vacm_access_read_view_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('vacm-access-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Status of this view configuration
                ''',
                'vacm_access_status',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('vacm-access-write-view-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Write view name
                ''',
                'vacm_access_write_view_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'group-information',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables.Groups.Group.GroupInformations' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables.Groups.Group.GroupInformations',
            False, 
            [
            _MetaInfoClassMember('group-information', REFERENCE_LIST, 'GroupInformation' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation', 
                [], [], 
                '''                Group name ,status  and information
                ''',
                'group_information',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'group-informations',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables.Groups.Group' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables.Groups.Group',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Group Name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('group-informations', REFERENCE_CLASS, 'GroupInformations' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables.Groups.Group.GroupInformations', 
                [], [], 
                '''                Group Model
                ''',
                'group_informations',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'group',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables.Groups' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables.Groups',
            False, 
            [
            _MetaInfoClassMember('group', REFERENCE_LIST, 'Group' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables.Groups.Group', 
                [], [], 
                '''                SNMP group name
                ''',
                'group',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'groups',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName',
            False, 
            [
            _MetaInfoClassMember('user-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                User name
                ''',
                'user_name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('usm-user-status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Status of this user
                ''',
                'usm_user_status',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('usm-user-storage-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Storage type
                ''',
                'usm_user_storage_type',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'user-name',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables.UserEngineIds.UserEngineId' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables.UserEngineIds.UserEngineId',
            False, 
            [
            _MetaInfoClassMember('engine-id', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                SNMP Engine ID
                ''',
                'engine_id',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('user-name', REFERENCE_LIST, 'UserName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName', 
                [], [], 
                '''                User name ,storage type ,status 
                ''',
                'user_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'user-engine-id',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables.UserEngineIds' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables.UserEngineIds',
            False, 
            [
            _MetaInfoClassMember('user-engine-id', REFERENCE_LIST, 'UserEngineId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables.UserEngineIds.UserEngineId', 
                [], [], 
                '''                SNMP engineId
                ''',
                'user_engine_id',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'user-engine-ids',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.Tables' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.Tables',
            False, 
            [
            _MetaInfoClassMember('groups', REFERENCE_CLASS, 'Groups' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables.Groups', 
                [], [], 
                '''                List of vacmAccessTable
                ''',
                'groups',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('user-engine-ids', REFERENCE_CLASS, 'UserEngineIds' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables.UserEngineIds', 
                [], [], 
                '''                List of User
                ''',
                'user_engine_ids',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'tables',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.SystemOid' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.SystemOid',
            False, 
            [
            _MetaInfoClassMember('sys-obj-id', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                sysObjID  1.3.6.1.2.1.1.2
                ''',
                'sys_obj_id',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'system-oid',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information.TrapQueue' : {
        'meta_info' : _MetaInfoClass('Snmp.Information.TrapQueue',
            False, 
            [
            _MetaInfoClassMember('trap-avg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                trap avg
                ''',
                'trap_avg',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-max', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                trap max
                ''',
                'trap_max',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-min', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                trap min
                ''',
                'trap_min',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-q', ATTRIBUTE, 'str' , None, None, 
                [], [b'([0-9a-fA-F]{2}(:[0-9a-fA-F]{2})*)?'], 
                '''                trapQ
                ''',
                'trap_q',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-queue',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Information' : {
        'meta_info' : _MetaInfoClass('Snmp.Information',
            False, 
            [
            _MetaInfoClassMember('bulk-stats-transfers', REFERENCE_CLASS, 'BulkStatsTransfers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.BulkStatsTransfers', 
                [], [], 
                '''                List of bulkstats transfer on the system
                ''',
                'bulk_stats_transfers',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('context-mapping', REFERENCE_CLASS, 'ContextMapping' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.ContextMapping', 
                [], [], 
                '''                Context name, features name, topology name,
                instance
                ''',
                'context_mapping',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('drop-nms-addresses', REFERENCE_CLASS, 'DropNmsAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.DropNmsAddresses', 
                [], [], 
                '''                NMS list for drop PDU
                ''',
                'drop_nms_addresses',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('duplicate-drop', REFERENCE_CLASS, 'DuplicateDrop' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.DuplicateDrop', 
                [], [], 
                '''                Duplicate request status, count, time 
                ''',
                'duplicate_drop',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('engine-id', REFERENCE_CLASS, 'EngineId' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.EngineId', 
                [], [], 
                '''                SNMP engine ID
                ''',
                'engine_id',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('hosts', REFERENCE_CLASS, 'Hosts' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Hosts', 
                [], [], 
                '''                SNMP host information
                ''',
                'hosts',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('incoming-queue', REFERENCE_CLASS, 'IncomingQueue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.IncomingQueue', 
                [], [], 
                '''                Incoming queue details 
                ''',
                'incoming_queue',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('infom-details', REFERENCE_CLASS, 'InfomDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.InfomDetails', 
                [], [], 
                '''                SNMP trap OID
                ''',
                'infom_details',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('mibs', REFERENCE_CLASS, 'Mibs' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Mibs', 
                [], [], 
                '''                List of MIBS supported on the system
                ''',
                'mibs',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('nm-spackets', REFERENCE_CLASS, 'NmSpackets' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.NmSpackets', 
                [], [], 
                '''                SNMP overload statistics 
                ''',
                'nm_spackets',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('nms-addresses', REFERENCE_CLASS, 'NmsAddresses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.NmsAddresses', 
                [], [], 
                '''                SNMP request type summary 
                ''',
                'nms_addresses',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('poll-oids', REFERENCE_CLASS, 'PollOids' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.PollOids', 
                [], [], 
                '''                OID list for poll PDU
                ''',
                'poll_oids',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('request-type-detail', REFERENCE_CLASS, 'RequestTypeDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.RequestTypeDetail', 
                [], [], 
                '''                SNMP request type details 
                ''',
                'request_type_detail',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rx-queue', REFERENCE_CLASS, 'RxQueue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.RxQueue', 
                [], [], 
                '''                SNMP rx queue statistics
                ''',
                'rx_queue',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('serial-numbers', REFERENCE_CLASS, 'SerialNumbers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.SerialNumbers', 
                [], [], 
                '''                SNMP statistics pdu 
                ''',
                'serial_numbers',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Statistics', 
                [], [], 
                '''                SNMP statistics
                ''',
                'statistics',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('system-descr', REFERENCE_CLASS, 'SystemDescr' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.SystemDescr', 
                [], [], 
                '''                System description
                ''',
                'system_descr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('system-name', REFERENCE_CLASS, 'SystemName' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.SystemName', 
                [], [], 
                '''                System name
                ''',
                'system_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('system-oid', REFERENCE_CLASS, 'SystemOid' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.SystemOid', 
                [], [], 
                '''                System object ID
                ''',
                'system_oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('system-up-time', REFERENCE_CLASS, 'SystemUpTime' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.SystemUpTime', 
                [], [], 
                '''                System up time
                ''',
                'system_up_time',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('tables', REFERENCE_CLASS, 'Tables' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Tables', 
                [], [], 
                '''                List of table
                ''',
                'tables',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-infos', REFERENCE_CLASS, 'TrapInfos' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.TrapInfos', 
                [], [], 
                '''                SNMP trap OID
                ''',
                'trap_infos',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-oids', REFERENCE_CLASS, 'TrapOids' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.TrapOids', 
                [], [], 
                '''                SNMP trap OID
                ''',
                'trap_oids',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-queue', REFERENCE_CLASS, 'TrapQueue' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.TrapQueue', 
                [], [], 
                '''                SNMP trap queue statistics
                ''',
                'trap_queue',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('views', REFERENCE_CLASS, 'Views' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information.Views', 
                [], [], 
                '''                SNMP view information
                ''',
                'views',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'information',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Snmp.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('interface-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Index as used by MIB tables
                ''',
                'interface_index',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Interfaces' : {
        'meta_info' : _MetaInfoClass('Snmp.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Interfaces.Interface', 
                [], [], 
                '''                Interface Name
                ''',
                'interface',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary',
            False, 
            [
            _MetaInfoClassMember('buffered-traps-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of buffered traps correlated to this rule
                ''',
                'buffered_traps_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'SnmpCorrRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'rule-summary',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind',
            False, 
            [
            _MetaInfoClassMember('match-type', REFERENCE_ENUM_CLASS, 'SnmpCorrVbindMatchEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrVbindMatchEnum', 
                [], [], 
                '''                Varbind match type
                ''',
                'match_type',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of the varbind
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('reg-exp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular expression to match
                ''',
                'reg_exp',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'var-bind',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails.RuleDetail.RootCause' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails.RuleDetail.RootCause',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of the trap
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('var-bind', REFERENCE_LIST, 'VarBind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind', 
                [], [], 
                '''                VarBinds of the trap
                ''',
                'var_bind',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'root-cause',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind',
            False, 
            [
            _MetaInfoClassMember('match-type', REFERENCE_ENUM_CLASS, 'SnmpCorrVbindMatchEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrVbindMatchEnum', 
                [], [], 
                '''                Varbind match type
                ''',
                'match_type',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of the varbind
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('reg-exp', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Regular expression to match
                ''',
                'reg_exp',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'var-bind',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of the trap
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('var-bind', REFERENCE_LIST, 'VarBind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind', 
                [], [], 
                '''                VarBinds of the trap
                ''',
                'var_bind',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'non-rootcaus',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost',
            False, 
            [
            _MetaInfoClassMember('ip-address', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                IP address of the host
                ''',
                'ip_address',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('port', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port of the host
                ''',
                'port',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'apply-host',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails.RuleDetail' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails.RuleDetail',
            False, 
            [
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('apply-host', REFERENCE_LIST, 'ApplyHost' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost', 
                [], [], 
                '''                Hosts (IP/port) to which the rule is applied
                ''',
                'apply_host',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('non-rootcaus', REFERENCE_LIST, 'NonRootcaus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus', 
                [], [], 
                '''                OIDs/VarBinds defining the nonrootcause match
                conditions.
                ''',
                'non_rootcaus',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('root-cause', REFERENCE_CLASS, 'RootCause' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails.RuleDetail.RootCause', 
                [], [], 
                '''                OID/VarBinds defining the rootcause match
                conditions.
                ''',
                'root_cause',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-summary', REFERENCE_CLASS, 'RuleSummary' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary', 
                [], [], 
                '''                Rule summary, name, etc
                ''',
                'rule_summary',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Time window (in ms) for which root/all messages
                are kept in correlater before sending them to
                hosts
                ''',
                'timeout',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'rule-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleDetails' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleDetails',
            False, 
            [
            _MetaInfoClassMember('rule-detail', REFERENCE_LIST, 'RuleDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails.RuleDetail', 
                [], [], 
                '''                Details of one of the correlation rules
                ''',
                'rule_detail',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'rule-details',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.BufferStatus' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.BufferStatus',
            False, 
            [
            _MetaInfoClassMember('configured-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Configured buffer size
                ''',
                'configured_size',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('current-size', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current buffer usage
                ''',
                'current_size',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'buffer-status',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules',
            False, 
            [
            _MetaInfoClassMember('buffered-traps-count', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of buffered traps correlated to this rule
                ''',
                'buffered_traps_count',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation Rule Name
                ''',
                'rule_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-state', REFERENCE_ENUM_CLASS, 'SnmpCorrRuleStateEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'SnmpCorrRuleStateEnum', 
                [], [], 
                '''                Applied state of the rule It could be not
                applied, applied or applied to all
                ''',
                'rule_state',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'rules',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleSetDetails.RuleSetDetail' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSetDetails.RuleSetDetail',
            False, 
            [
            _MetaInfoClassMember('rule-set-name', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                Ruleset Name
                ''',
                'rule_set_name',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('rule-set-name-xr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Ruleset Name
                ''',
                'rule_set_name_xr',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rules', REFERENCE_LIST, 'Rules' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules', 
                [], [], 
                '''                Rules contained in a ruleset
                ''',
                'rules',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'rule-set-detail',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.RuleSetDetails' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.RuleSetDetails',
            False, 
            [
            _MetaInfoClassMember('rule-set-detail', REFERENCE_LIST, 'RuleSetDetail' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleSetDetails.RuleSetDetail', 
                [], [], 
                '''                Detail of one of the correlation rulesets
                ''',
                'rule_set_detail',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'rule-set-details',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.Traps.Trap.TrapInfo.VarBind' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Traps.Trap.TrapInfo.VarBind',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                OID of the varbind
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Value of the varbind
                ''',
                'value',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'var-bind',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.Traps.Trap.TrapInfo' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Traps.Trap.TrapInfo',
            False, 
            [
            _MetaInfoClassMember('oid', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Object ID
                ''',
                'oid',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('relative-timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of hsecs elapsed since snmpd was started
                ''',
                'relative_timestamp',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('timestamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Time when the trap was generated. It is
                expressed in number of milliseconds since 00:00
                :00 UTC, January 1, 1970
                ''',
                'timestamp',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('var-bind', REFERENCE_LIST, 'VarBind' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.Traps.Trap.TrapInfo.VarBind', 
                [], [], 
                '''                VarBinds on the trap
                ''',
                'var_bind',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap-info',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.Traps.Trap' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Traps.Trap',
            False, 
            [
            _MetaInfoClassMember('entry-id', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Entry ID
                ''',
                'entry_id',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('correlation-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Correlation ID
                ''',
                'correlation_id',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('is-root-cause', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True if this is the rootcause
                ''',
                'is_root_cause',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Correlation rule name
                ''',
                'rule_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('trap-info', REFERENCE_CLASS, 'TrapInfo' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.Traps.Trap.TrapInfo', 
                [], [], 
                '''                Correlated trap information
                ''',
                'trap_info',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'trap',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator.Traps' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator.Traps',
            False, 
            [
            _MetaInfoClassMember('trap', REFERENCE_LIST, 'Trap' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.Traps.Trap', 
                [], [], 
                '''                One of the correlated traps
                ''',
                'trap',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'traps',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.Correlator' : {
        'meta_info' : _MetaInfoClass('Snmp.Correlator',
            False, 
            [
            _MetaInfoClassMember('buffer-status', REFERENCE_CLASS, 'BufferStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.BufferStatus', 
                [], [], 
                '''                Describes buffer utilization and parameters
                configured
                ''',
                'buffer_status',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-details', REFERENCE_CLASS, 'RuleDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleDetails', 
                [], [], 
                '''                Table that contains the database of correlation
                rule details
                ''',
                'rule_details',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('rule-set-details', REFERENCE_CLASS, 'RuleSetDetails' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.RuleSetDetails', 
                [], [], 
                '''                Table that contains the ruleset detail info
                ''',
                'rule_set_details',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('traps', REFERENCE_CLASS, 'Traps' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator.Traps', 
                [], [], 
                '''                Correlated traps Table
                ''',
                'traps',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'correlator',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceIndexes.InterfaceIndex' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceIndexes.InterfaceIndex',
            False, 
            [
            _MetaInfoClassMember('interface-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Index as used by MIB tables
                ''',
                'interface_index',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'interface-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceIndexes' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceIndexes',
            False, 
            [
            _MetaInfoClassMember('interface-index', REFERENCE_LIST, 'InterfaceIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceIndexes.InterfaceIndex', 
                [], [], 
                '''                Interface Index
                ''',
                'interface_index',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'interface-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.IfIndexes.IfIndex' : {
        'meta_info' : _MetaInfoClass('Snmp.IfIndexes.IfIndex',
            False, 
            [
            _MetaInfoClassMember('interface-index', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Interface Index as used by MIB tables
                ''',
                'interface_index',
                'Cisco-IOS-XR-snmp-agent-oper', True),
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'if-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.IfIndexes' : {
        'meta_info' : _MetaInfoClass('Snmp.IfIndexes',
            False, 
            [
            _MetaInfoClassMember('if-index', REFERENCE_LIST, 'IfIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.IfIndexes.IfIndex', 
                [], [], 
                '''                Interface Index
                ''',
                'if_index',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'if-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex' : {
        'meta_info' : _MetaInfoClass('Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex',
            False, 
            [
            _MetaInfoClassMember('entity-phynum', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Entity physical index
                ''',
                'entity_phynum',
                'Cisco-IOS-XR-snmp-entitymib-oper', True),
            _MetaInfoClassMember('ent-physical-descr', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                EntPhysicalDescription
                ''',
                'ent_physical_descr',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('ent-physical-firmware-rev', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                entphysicalFirmwareRev
                ''',
                'ent_physical_firmware_rev',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('ent-physical-hardware-rev', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                entphysicalHardwareRev
                ''',
                'ent_physical_hardware_rev',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('ent-physical-mfg-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                entphysicalMfgName
                ''',
                'ent_physical_mfg_name',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('ent-physical-modelname', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                entphysicalModelName
                ''',
                'ent_physical_modelname',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('ent-physical-name', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                entPhysicalName
                ''',
                'ent_physical_name',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('ent-physical-serial-num', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                entphysicalSerialNum
                ''',
                'ent_physical_serial_num',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('ent-physical-software-rev', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                entphysicalSoftwareRev
                ''',
                'ent_physical_software_rev',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('location', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                invmgr EDM path
                ''',
                'location',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('physical-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                entPhysicalIndex
                ''',
                'physical_index',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-entitymib-oper',
            'entity-physical-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-entitymib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.EntityMib.EntityPhysicalIndexes' : {
        'meta_info' : _MetaInfoClass('Snmp.EntityMib.EntityPhysicalIndexes',
            False, 
            [
            _MetaInfoClassMember('entity-physical-index', REFERENCE_LIST, 'EntityPhysicalIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex', 
                [], [], 
                '''                SNMP entPhysical index number
                ''',
                'entity_physical_index',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-entitymib-oper',
            'entity-physical-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-entitymib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.EntityMib' : {
        'meta_info' : _MetaInfoClass('Snmp.EntityMib',
            False, 
            [
            _MetaInfoClassMember('entity-physical-indexes', REFERENCE_CLASS, 'EntityPhysicalIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.EntityMib.EntityPhysicalIndexes', 
                [], [], 
                '''                SNMP entity mib
                ''',
                'entity_physical_indexes',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-entitymib-oper',
            'entity-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-entitymib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.Interfaces.Interface' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.Interfaces.Interface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-ifmib-oper', True),
            _MetaInfoClassMember('if-index', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Interface Index
                ''',
                'if_index',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.Interfaces' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.Interfaces',
            False, 
            [
            _MetaInfoClassMember('interface', REFERENCE_LIST, 'Interface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.Interfaces.Interface', 
                [], [], 
                '''                ifIndex for a specific Interface Name
                ''',
                'interface',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-ifmib-oper', True),
            _MetaInfoClassMember('if-connector-present', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface ifConnector
                ''',
                'if_connector_present',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface-connector',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.InterfaceConnectors' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.InterfaceConnectors',
            False, 
            [
            _MetaInfoClassMember('interface-connector', REFERENCE_LIST, 'InterfaceConnector' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector', 
                [], [], 
                '''                ifConnectorPresent for a specific Interface
                Name
                ''',
                'interface_connector',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface-connectors',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-ifmib-oper', True),
            _MetaInfoClassMember('if-alias', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface ifAlias
                ''',
                'if_alias',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface-alias',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.InterfaceAliases' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.InterfaceAliases',
            False, 
            [
            _MetaInfoClassMember('interface-alias', REFERENCE_LIST, 'InterfaceAlias' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias', 
                [], [], 
                '''                ifAlias for a specific Interface Name
                ''',
                'interface_alias',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface-aliases',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface',
            False, 
            [
            _MetaInfoClassMember('interface-name', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([a-zA-Z0-9_]*\\d+/){3,4}\\d+)|(([a-zA-Z0-9_]*\\d+/){3,4}\\d+\\.\\d+)|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]*\\d+))|(([a-zA-Z0-9_]*\\d+/){2}([a-zA-Z0-9_]+))|([a-zA-Z0-9_-]*\\d+)|([a-zA-Z0-9_-]*\\d+\\.\\d+)|(mpls)|(dwdm)'], 
                '''                Interface Name
                ''',
                'interface_name',
                'Cisco-IOS-XR-snmp-ifmib-oper', True),
            _MetaInfoClassMember('link-up-down-notif-status', REFERENCE_ENUM_CLASS, 'LinkUpDownStatusEnum' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_ifmib_oper', 'LinkUpDownStatusEnum', 
                [], [], 
                '''                LinkUpDown notification status
                ''',
                'link_up_down_notif_status',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'notification-interface',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.NotificationInterfaces' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.NotificationInterfaces',
            False, 
            [
            _MetaInfoClassMember('notification-interface', REFERENCE_LIST, 'NotificationInterface' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface', 
                [], [], 
                '''                Notification for specific Interface Name
                ''',
                'notification_interface',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'notification-interfaces',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus',
            False, 
            [
            _MetaInfoClassMember('interface-stack-status', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                StackHigherLayer.StackLowerLayer
                ''',
                'interface_stack_status',
                'Cisco-IOS-XR-snmp-ifmib-oper', True),
            _MetaInfoClassMember('if-stack-higher-layer', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Higher Layer Index
                ''',
                'if_stack_higher_layer',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            _MetaInfoClassMember('if-stack-lower-layer', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Lowyer Layer Index
                ''',
                'if_stack_lower_layer',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            _MetaInfoClassMember('if-stack-status', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Interface ifStackStaus info
                ''',
                'if_stack_status',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface-stack-status',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib.InterfaceStackStatuses' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib.InterfaceStackStatuses',
            False, 
            [
            _MetaInfoClassMember('interface-stack-status', REFERENCE_LIST, 'InterfaceStackStatus' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus', 
                [], [], 
                '''                ifstatus for a pair of Interface
                ''',
                'interface_stack_status',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface-stack-statuses',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.InterfaceMib' : {
        'meta_info' : _MetaInfoClass('Snmp.InterfaceMib',
            False, 
            [
            _MetaInfoClassMember('interface-aliases', REFERENCE_CLASS, 'InterfaceAliases' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.InterfaceAliases', 
                [], [], 
                '''                Interfaces ifAlias information
                ''',
                'interface_aliases',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            _MetaInfoClassMember('interface-connectors', REFERENCE_CLASS, 'InterfaceConnectors' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.InterfaceConnectors', 
                [], [], 
                '''                Interfaces ifConnectorPresent information
                ''',
                'interface_connectors',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            _MetaInfoClassMember('interface-stack-statuses', REFERENCE_CLASS, 'InterfaceStackStatuses' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.InterfaceStackStatuses', 
                [], [], 
                '''                Interfaces ifstackstatus information
                ''',
                'interface_stack_statuses',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.Interfaces', 
                [], [], 
                '''                Interfaces ifIndex information
                ''',
                'interfaces',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            _MetaInfoClassMember('notification-interfaces', REFERENCE_CLASS, 'NotificationInterfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib.NotificationInterfaces', 
                [], [], 
                '''                Interfaces Notification information
                ''',
                'notification_interfaces',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-ifmib-oper',
            'interface-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-ifmib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex' : {
        'meta_info' : _MetaInfoClass('Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex',
            False, 
            [
            _MetaInfoClassMember('phy-index', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Physical Index
                ''',
                'phy_index',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('thre-index', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Threshold index
                ''',
                'thre_index',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('threshold-evaluation', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates the result of the most recent
                evaluation of the thresholD
                ''',
                'threshold_evaluation',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('threshold-notification-enabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether or not a notification should
                result, in case of threshold violation
                ''',
                'threshold_notification_enabled',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('threshold-relation', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates relation between sensor value and
                threshold
                ''',
                'threshold_relation',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('threshold-severity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates minor, major, critical severities
                ''',
                'threshold_severity',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('threshold-value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Value of the configured threshold
                ''',
                'threshold_value',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-sensormib-oper',
            'threshold-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-sensormib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes' : {
        'meta_info' : _MetaInfoClass('Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes',
            False, 
            [
            _MetaInfoClassMember('threshold-index', REFERENCE_LIST, 'ThresholdIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex', 
                [], [], 
                '''                Threshold value for threshold index
                ''',
                'threshold_index',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-sensormib-oper',
            'threshold-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-sensormib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.SensorMib.PhysicalIndexes.PhysicalIndex' : {
        'meta_info' : _MetaInfoClass('Snmp.SensorMib.PhysicalIndexes.PhysicalIndex',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Physical index
                ''',
                'index',
                'Cisco-IOS-XR-snmp-sensormib-oper', True),
            _MetaInfoClassMember('threshold-indexes', REFERENCE_CLASS, 'ThresholdIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes', 
                [], [], 
                '''                List of threshold index
                ''',
                'threshold_indexes',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-sensormib-oper',
            'physical-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-sensormib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.SensorMib.PhysicalIndexes' : {
        'meta_info' : _MetaInfoClass('Snmp.SensorMib.PhysicalIndexes',
            False, 
            [
            _MetaInfoClassMember('physical-index', REFERENCE_LIST, 'PhysicalIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.SensorMib.PhysicalIndexes.PhysicalIndex', 
                [], [], 
                '''                Threshold value for physical index
                ''',
                'physical_index',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-sensormib-oper',
            'physical-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-sensormib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.SensorMib.EntPhyIndexes.EntPhyIndex' : {
        'meta_info' : _MetaInfoClass('Snmp.SensorMib.EntPhyIndexes.EntPhyIndex',
            False, 
            [
            _MetaInfoClassMember('index', ATTRIBUTE, 'str' , None, None, 
                [], [b'[\\w\\-\\.:,_@#%$\\+=\\|;]+'], 
                '''                Physical index
                ''',
                'index',
                'Cisco-IOS-XR-snmp-sensormib-oper', True),
            _MetaInfoClassMember('age-time-stamp', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Age of the sensor value; set to the current time
                if directly access the value from sensor
                ''',
                'age_time_stamp',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('alarm-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates threshold violation
                ''',
                'alarm_type',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('data-type', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor data type enums
                ''',
                'data_type',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('device-description', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Device Name
                ''',
                'device_description',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('device-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Identifier for this device
                ''',
                'device_id',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('field-validity-bitmap', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor valid bitmap
                ''',
                'field_validity_bitmap',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('measured-entity', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                physical entity for which the sensor is taking
                measurements
                ''',
                'measured_entity',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('precision', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor precision range
                ''',
                'precision',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('scale', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor scale enums
                ''',
                'scale',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('status', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor operation state enums
                ''',
                'status',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('units', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                Units of variable being read
                ''',
                'units',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('update-rate', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Sensor value update rate;set to 0 if sensor
                value is updated and evaluated immediately
                ''',
                'update_rate',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('value', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Current reading of sensor
                ''',
                'value',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-sensormib-oper',
            'ent-phy-index',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-sensormib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.SensorMib.EntPhyIndexes' : {
        'meta_info' : _MetaInfoClass('Snmp.SensorMib.EntPhyIndexes',
            False, 
            [
            _MetaInfoClassMember('ent-phy-index', REFERENCE_LIST, 'EntPhyIndex' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.SensorMib.EntPhyIndexes.EntPhyIndex', 
                [], [], 
                '''                Sensor value for physical index
                ''',
                'ent_phy_index',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-sensormib-oper',
            'ent-phy-indexes',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-sensormib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp.SensorMib' : {
        'meta_info' : _MetaInfoClass('Snmp.SensorMib',
            False, 
            [
            _MetaInfoClassMember('ent-phy-indexes', REFERENCE_CLASS, 'EntPhyIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.SensorMib.EntPhyIndexes', 
                [], [], 
                '''                List of physical index 
                ''',
                'ent_phy_indexes',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('physical-indexes', REFERENCE_CLASS, 'PhysicalIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.SensorMib.PhysicalIndexes', 
                [], [], 
                '''                List of physical index table for threshold
                value
                ''',
                'physical_indexes',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            ],
            'Cisco-IOS-XR-snmp-sensormib-oper',
            'sensor-mib',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-sensormib-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
    'Snmp' : {
        'meta_info' : _MetaInfoClass('Snmp',
            False, 
            [
            _MetaInfoClassMember('correlator', REFERENCE_CLASS, 'Correlator' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Correlator', 
                [], [], 
                '''                Trap Correlator operational data
                ''',
                'correlator',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('entity-mib', REFERENCE_CLASS, 'EntityMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.EntityMib', 
                [], [], 
                '''                SNMP entity mib
                ''',
                'entity_mib',
                'Cisco-IOS-XR-snmp-entitymib-oper', False),
            _MetaInfoClassMember('if-indexes', REFERENCE_CLASS, 'IfIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.IfIndexes', 
                [], [], 
                '''                List of ifnames
                ''',
                'if_indexes',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('information', REFERENCE_CLASS, 'Information' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Information', 
                [], [], 
                '''                SNMP operational information
                ''',
                'information',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('interface-indexes', REFERENCE_CLASS, 'InterfaceIndexes' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceIndexes', 
                [], [], 
                '''                List of index
                ''',
                'interface_indexes',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('interface-mib', REFERENCE_CLASS, 'InterfaceMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.InterfaceMib', 
                [], [], 
                '''                SNMP IF-MIB information
                ''',
                'interface_mib',
                'Cisco-IOS-XR-snmp-ifmib-oper', False),
            _MetaInfoClassMember('interfaces', REFERENCE_CLASS, 'Interfaces' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.Interfaces', 
                [], [], 
                '''                List of interfaces
                ''',
                'interfaces',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            _MetaInfoClassMember('sensor-mib', REFERENCE_CLASS, 'SensorMib' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.SensorMib', 
                [], [], 
                '''                SNMP sensor MIB information
                ''',
                'sensor_mib',
                'Cisco-IOS-XR-snmp-sensormib-oper', False),
            _MetaInfoClassMember('trap-servers', REFERENCE_CLASS, 'TrapServers' , 'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper', 'Snmp.TrapServers', 
                [], [], 
                '''                List of trap hosts
                ''',
                'trap_servers',
                'Cisco-IOS-XR-snmp-agent-oper', False),
            ],
            'Cisco-IOS-XR-snmp-agent-oper',
            'snmp',
            _yang_ns._namespaces['Cisco-IOS-XR-snmp-agent-oper'],
        'ydk.models.cisco_ios_xr.Cisco_IOS_XR_snmp_agent_oper'
        ),
    },
}
_meta_table['Snmp.TrapServers.TrapServer']['meta_info'].parent =_meta_table['Snmp.TrapServers']['meta_info']
_meta_table['Snmp.Information.Hosts.Host.HostInformation']['meta_info'].parent =_meta_table['Snmp.Information.Hosts.Host']['meta_info']
_meta_table['Snmp.Information.Hosts.Host']['meta_info'].parent =_meta_table['Snmp.Information.Hosts']['meta_info']
_meta_table['Snmp.Information.NmsAddresses.NmsAddress']['meta_info'].parent =_meta_table['Snmp.Information.NmsAddresses']['meta_info']
_meta_table['Snmp.Information.RequestTypeDetail.NmsAddresses.NmsAddress']['meta_info'].parent =_meta_table['Snmp.Information.RequestTypeDetail.NmsAddresses']['meta_info']
_meta_table['Snmp.Information.RequestTypeDetail.NmsAddresses']['meta_info'].parent =_meta_table['Snmp.Information.RequestTypeDetail']['meta_info']
_meta_table['Snmp.Information.BulkStatsTransfers.BulkStatsTransfer']['meta_info'].parent =_meta_table['Snmp.Information.BulkStatsTransfers']['meta_info']
_meta_table['Snmp.Information.TrapInfos.TrapInfo.TrapOiDinfo']['meta_info'].parent =_meta_table['Snmp.Information.TrapInfos.TrapInfo']['meta_info']
_meta_table['Snmp.Information.TrapInfos.TrapInfo']['meta_info'].parent =_meta_table['Snmp.Information.TrapInfos']['meta_info']
_meta_table['Snmp.Information.PollOids.PollOid']['meta_info'].parent =_meta_table['Snmp.Information.PollOids']['meta_info']
_meta_table['Snmp.Information.InfomDetails.InfomDetail.TrapOiDinfo']['meta_info'].parent =_meta_table['Snmp.Information.InfomDetails.InfomDetail']['meta_info']
_meta_table['Snmp.Information.InfomDetails.InfomDetail']['meta_info'].parent =_meta_table['Snmp.Information.InfomDetails']['meta_info']
_meta_table['Snmp.Information.IncomingQueue.InqEntry']['meta_info'].parent =_meta_table['Snmp.Information.IncomingQueue']['meta_info']
_meta_table['Snmp.Information.ContextMapping.ContexMapping']['meta_info'].parent =_meta_table['Snmp.Information.ContextMapping']['meta_info']
_meta_table['Snmp.Information.TrapOids.TrapOid']['meta_info'].parent =_meta_table['Snmp.Information.TrapOids']['meta_info']
_meta_table['Snmp.Information.NmSpackets.NmSpacket']['meta_info'].parent =_meta_table['Snmp.Information.NmSpackets']['meta_info']
_meta_table['Snmp.Information.Mibs.Mib.Oids.Oid']['meta_info'].parent =_meta_table['Snmp.Information.Mibs.Mib.Oids']['meta_info']
_meta_table['Snmp.Information.Mibs.Mib.Oids']['meta_info'].parent =_meta_table['Snmp.Information.Mibs.Mib']['meta_info']
_meta_table['Snmp.Information.Mibs.Mib.MibInformation']['meta_info'].parent =_meta_table['Snmp.Information.Mibs.Mib']['meta_info']
_meta_table['Snmp.Information.Mibs.Mib']['meta_info'].parent =_meta_table['Snmp.Information.Mibs']['meta_info']
_meta_table['Snmp.Information.SerialNumbers.SerialNumber']['meta_info'].parent =_meta_table['Snmp.Information.SerialNumbers']['meta_info']
_meta_table['Snmp.Information.DropNmsAddresses.DropNmsAddress']['meta_info'].parent =_meta_table['Snmp.Information.DropNmsAddresses']['meta_info']
_meta_table['Snmp.Information.Views.View.ViewInformation']['meta_info'].parent =_meta_table['Snmp.Information.Views.View']['meta_info']
_meta_table['Snmp.Information.Views.View']['meta_info'].parent =_meta_table['Snmp.Information.Views']['meta_info']
_meta_table['Snmp.Information.Tables.Groups.Group.GroupInformations.GroupInformation']['meta_info'].parent =_meta_table['Snmp.Information.Tables.Groups.Group.GroupInformations']['meta_info']
_meta_table['Snmp.Information.Tables.Groups.Group.GroupInformations']['meta_info'].parent =_meta_table['Snmp.Information.Tables.Groups.Group']['meta_info']
_meta_table['Snmp.Information.Tables.Groups.Group']['meta_info'].parent =_meta_table['Snmp.Information.Tables.Groups']['meta_info']
_meta_table['Snmp.Information.Tables.UserEngineIds.UserEngineId.UserName']['meta_info'].parent =_meta_table['Snmp.Information.Tables.UserEngineIds.UserEngineId']['meta_info']
_meta_table['Snmp.Information.Tables.UserEngineIds.UserEngineId']['meta_info'].parent =_meta_table['Snmp.Information.Tables.UserEngineIds']['meta_info']
_meta_table['Snmp.Information.Tables.Groups']['meta_info'].parent =_meta_table['Snmp.Information.Tables']['meta_info']
_meta_table['Snmp.Information.Tables.UserEngineIds']['meta_info'].parent =_meta_table['Snmp.Information.Tables']['meta_info']
_meta_table['Snmp.Information.Hosts']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.SystemUpTime']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.NmsAddresses']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.EngineId']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.RxQueue']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.SystemName']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.RequestTypeDetail']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.DuplicateDrop']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.BulkStatsTransfers']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.TrapInfos']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.PollOids']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.InfomDetails']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.Statistics']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.IncomingQueue']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.ContextMapping']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.TrapOids']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.NmSpackets']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.Mibs']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.SerialNumbers']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.DropNmsAddresses']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.Views']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.SystemDescr']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.Tables']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.SystemOid']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Information.TrapQueue']['meta_info'].parent =_meta_table['Snmp.Information']['meta_info']
_meta_table['Snmp.Interfaces.Interface']['meta_info'].parent =_meta_table['Snmp.Interfaces']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RootCause.VarBind']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RootCause']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus.VarBind']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RuleSummary']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleDetails.RuleDetail']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.RootCause']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleDetails.RuleDetail']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.NonRootcaus']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleDetails.RuleDetail']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails.RuleDetail.ApplyHost']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleDetails.RuleDetail']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails.RuleDetail']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleDetails']['meta_info']
_meta_table['Snmp.Correlator.RuleSetDetails.RuleSetDetail.Rules']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSetDetails.RuleSetDetail']['meta_info']
_meta_table['Snmp.Correlator.RuleSetDetails.RuleSetDetail']['meta_info'].parent =_meta_table['Snmp.Correlator.RuleSetDetails']['meta_info']
_meta_table['Snmp.Correlator.Traps.Trap.TrapInfo.VarBind']['meta_info'].parent =_meta_table['Snmp.Correlator.Traps.Trap.TrapInfo']['meta_info']
_meta_table['Snmp.Correlator.Traps.Trap.TrapInfo']['meta_info'].parent =_meta_table['Snmp.Correlator.Traps.Trap']['meta_info']
_meta_table['Snmp.Correlator.Traps.Trap']['meta_info'].parent =_meta_table['Snmp.Correlator.Traps']['meta_info']
_meta_table['Snmp.Correlator.RuleDetails']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.Correlator.BufferStatus']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.Correlator.RuleSetDetails']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.Correlator.Traps']['meta_info'].parent =_meta_table['Snmp.Correlator']['meta_info']
_meta_table['Snmp.InterfaceIndexes.InterfaceIndex']['meta_info'].parent =_meta_table['Snmp.InterfaceIndexes']['meta_info']
_meta_table['Snmp.IfIndexes.IfIndex']['meta_info'].parent =_meta_table['Snmp.IfIndexes']['meta_info']
_meta_table['Snmp.EntityMib.EntityPhysicalIndexes.EntityPhysicalIndex']['meta_info'].parent =_meta_table['Snmp.EntityMib.EntityPhysicalIndexes']['meta_info']
_meta_table['Snmp.EntityMib.EntityPhysicalIndexes']['meta_info'].parent =_meta_table['Snmp.EntityMib']['meta_info']
_meta_table['Snmp.InterfaceMib.Interfaces.Interface']['meta_info'].parent =_meta_table['Snmp.InterfaceMib.Interfaces']['meta_info']
_meta_table['Snmp.InterfaceMib.InterfaceConnectors.InterfaceConnector']['meta_info'].parent =_meta_table['Snmp.InterfaceMib.InterfaceConnectors']['meta_info']
_meta_table['Snmp.InterfaceMib.InterfaceAliases.InterfaceAlias']['meta_info'].parent =_meta_table['Snmp.InterfaceMib.InterfaceAliases']['meta_info']
_meta_table['Snmp.InterfaceMib.NotificationInterfaces.NotificationInterface']['meta_info'].parent =_meta_table['Snmp.InterfaceMib.NotificationInterfaces']['meta_info']
_meta_table['Snmp.InterfaceMib.InterfaceStackStatuses.InterfaceStackStatus']['meta_info'].parent =_meta_table['Snmp.InterfaceMib.InterfaceStackStatuses']['meta_info']
_meta_table['Snmp.InterfaceMib.Interfaces']['meta_info'].parent =_meta_table['Snmp.InterfaceMib']['meta_info']
_meta_table['Snmp.InterfaceMib.InterfaceConnectors']['meta_info'].parent =_meta_table['Snmp.InterfaceMib']['meta_info']
_meta_table['Snmp.InterfaceMib.InterfaceAliases']['meta_info'].parent =_meta_table['Snmp.InterfaceMib']['meta_info']
_meta_table['Snmp.InterfaceMib.NotificationInterfaces']['meta_info'].parent =_meta_table['Snmp.InterfaceMib']['meta_info']
_meta_table['Snmp.InterfaceMib.InterfaceStackStatuses']['meta_info'].parent =_meta_table['Snmp.InterfaceMib']['meta_info']
_meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes.ThresholdIndex']['meta_info'].parent =_meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes']['meta_info']
_meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex.ThresholdIndexes']['meta_info'].parent =_meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex']['meta_info']
_meta_table['Snmp.SensorMib.PhysicalIndexes.PhysicalIndex']['meta_info'].parent =_meta_table['Snmp.SensorMib.PhysicalIndexes']['meta_info']
_meta_table['Snmp.SensorMib.EntPhyIndexes.EntPhyIndex']['meta_info'].parent =_meta_table['Snmp.SensorMib.EntPhyIndexes']['meta_info']
_meta_table['Snmp.SensorMib.PhysicalIndexes']['meta_info'].parent =_meta_table['Snmp.SensorMib']['meta_info']
_meta_table['Snmp.SensorMib.EntPhyIndexes']['meta_info'].parent =_meta_table['Snmp.SensorMib']['meta_info']
_meta_table['Snmp.TrapServers']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Information']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Interfaces']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.Correlator']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.InterfaceIndexes']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.IfIndexes']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.EntityMib']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.InterfaceMib']['meta_info'].parent =_meta_table['Snmp']['meta_info']
_meta_table['Snmp.SensorMib']['meta_info'].parent =_meta_table['Snmp']['meta_info']
