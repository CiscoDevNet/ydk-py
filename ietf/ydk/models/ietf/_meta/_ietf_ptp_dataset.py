


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns

_meta_table = {
    'DelayMechanismEnumerationEnum' : _MetaInfoEnum('DelayMechanismEnumerationEnum', 'ydk.models.ietf.ietf_ptp_dataset',
        {
            'E2E':'E2E',
            'P2P':'P2P',
            'DISABLED':'DISABLED',
        }, 'ietf-ptp-dataset', _yang_ns._namespaces['ietf-ptp-dataset']),
    'PortStateEnumerationEnum' : _MetaInfoEnum('PortStateEnumerationEnum', 'ydk.models.ietf.ietf_ptp_dataset',
        {
            'INITIALIZING':'INITIALIZING',
            'FAULTY':'FAULTY',
            'DISABLED':'DISABLED',
            'LISTENING':'LISTENING',
            'PRE_MASTER':'PRE_MASTER',
            'MASTER':'MASTER',
            'PASSIVE':'PASSIVE',
            'UNCALIBRATED':'UNCALIBRATED',
            'SLAVE':'SLAVE',
        }, 'ietf-ptp-dataset', _yang_ns._namespaces['ietf-ptp-dataset']),
    'InstanceList.DefaultDs.ClockQuality' : {
        'meta_info' : _MetaInfoClass('InstanceList.DefaultDs.ClockQuality',
            False, 
            [
            _MetaInfoClassMember('clock-accuracy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The clockAccuracy indicates the expected accuracy
                of the clock.
                ''',
                'clock_accuracy',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('clock-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The clockClass denotes the traceability of the time
                or frequency distributed by the clock.
                ''',
                'clock_class',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('offset-scaled-log-variance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The offsetScaledLogVariance provides an
                estimate of the variations of the clock
                from a linear timescale when it is not synchronized
                to another clock using the protocol.
                ''',
                'offset_scaled_log_variance',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'clock-quality',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.DefaultDs' : {
        'meta_info' : _MetaInfoClass('InstanceList.DefaultDs',
            False, 
            [
            _MetaInfoClassMember('clock-identity', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The clockIdentity of the local clock
                ''',
                'clock_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('clock-quality', REFERENCE_CLASS, 'ClockQuality' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.DefaultDs.ClockQuality', 
                [], [], 
                '''                The clockQuality of the local clock.
                ''',
                'clock_quality',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('domain-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The domain number of the current syntonization
                domain.
                ''',
                'domain_number',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('number-ports', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of PTP ports on the device.
                ''',
                'number_ports',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('priority1', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The priority1 attribute of the local clock.
                ''',
                'priority1',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('priority2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The priority2 attribute of the local clock. 
                ''',
                'priority2',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('slave-only', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the clock is a slave-only clock.
                ''',
                'slave_only',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('two-step-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the clock is a two-step clock; otherwise,
                the clock is a one-step clock.
                ''',
                'two_step_flag',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'default-ds',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.CurrentDs' : {
        'meta_info' : _MetaInfoClass('InstanceList.CurrentDs',
            False, 
            [
            _MetaInfoClassMember('mean-path-delay', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                The current value of the mean propagation time between
                a master and a slave clock as computed by the slave.
                ''',
                'mean_path_delay',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('offset-from-master', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                The current value of the time difference between
                a master and a slave clock as computed by the slave.
                ''',
                'offset_from_master',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('steps-removed', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of communication paths traversed
                between the local clock and the grandmaster clock.
                ''',
                'steps_removed',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'current-ds',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.ParentDs.ParentPortIdentity' : {
        'meta_info' : _MetaInfoClass('InstanceList.ParentDs.ParentPortIdentity',
            False, 
            [
            _MetaInfoClassMember('clock-identity', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                Identity of the clock
                ''',
                'clock_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port number
                ''',
                'port_number',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'parent-port-identity',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.ParentDs.GrandmasterClockQuality' : {
        'meta_info' : _MetaInfoClass('InstanceList.ParentDs.GrandmasterClockQuality',
            False, 
            [
            _MetaInfoClassMember('clock-accuracy', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The clockAccuracy indicates the expected accuracy
                of the clock.
                ''',
                'clock_accuracy',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('clock-class', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The clockClass denotes the traceability of the time
                or frequency distributed by the clock.
                ''',
                'clock_class',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('offset-scaled-log-variance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The offsetScaledLogVariance provides an
                estimate of the variations of the clock
                from a linear timescale when it is not synchronized
                to another clock using the protocol.
                ''',
                'offset_scaled_log_variance',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'grandmaster-clock-quality',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.ParentDs' : {
        'meta_info' : _MetaInfoClass('InstanceList.ParentDs',
            False, 
            [
            _MetaInfoClassMember('grandmaster-clock-quality', REFERENCE_CLASS, 'GrandmasterClockQuality' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.ParentDs.GrandmasterClockQuality', 
                [], [], 
                '''                The clockQuality of the grandmaster clock.
                ''',
                'grandmaster_clock_quality',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('grandmaster-identity', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The clockIdentity attribute of the grandmaster clock.
                ''',
                'grandmaster_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('grandmaster-priority1', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The priority1 attribute of the grandmaster clock.
                ''',
                'grandmaster_priority1',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('grandmaster-priority2', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The priority2 attribute of the grandmaster clock.
                ''',
                'grandmaster_priority2',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('observed-parent-clock-phase-change-rate', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                An estimate of the parent clock's phase change rate
                as observed by the slave clock.
                ''',
                'observed_parent_clock_phase_change_rate',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('observed-parent-offset-scaled-log-variance', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                An estimate of the parent clock's PTP variance
                as observed by the slave clock.
                ''',
                'observed_parent_offset_scaled_log_variance',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('parent-port-identity', REFERENCE_CLASS, 'ParentPortIdentity' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.ParentDs.ParentPortIdentity', 
                [], [], 
                '''                The portIdentity of the port on the master
                ''',
                'parent_port_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('parent-stats', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the values of
                observedParentOffsetScaledLogVariance and
                observedParentClockPhaseChangeRate of parentDS
                have been measured and are valid.
                ''',
                'parent_stats',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'parent-ds',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.TimePropertiesDs' : {
        'meta_info' : _MetaInfoClass('InstanceList.TimePropertiesDs',
            False, 
            [
            _MetaInfoClassMember('current-utc-offset', ATTRIBUTE, 'int' , None, None, 
                [('-32768', '32767')], [], 
                '''                The offset between TAI and UTC when the epoch of the
                PTP system is the PTP epoch, i.e., when ptp-timescale
                is TRUE; otherwise, the value has no meaning.
                ''',
                'current_utc_offset',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('current-utc-offset-valid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the current UTC offset is valid.
                ''',
                'current_utc_offset_valid',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('frequency-traceable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the frequency determining the timescale
                is traceable to a primary reference.
                ''',
                'frequency_traceable',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('leap59', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the last minute of the current UTC day
                contains 59 seconds.
                ''',
                'leap59',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('leap61', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the last minute of the current UTC day
                contains 61 seconds.
                ''',
                'leap61',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('ptp-timescale', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the clock timescale of the grandmaster
                    clock is PTP; otherwise, the timescale is ARB
                   (arbitrary).
                ''',
                'ptp_timescale',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('time-source', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The source of time used by the grandmaster clock.
                ''',
                'time_source',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('time-traceable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the timescale and the currentUtcOffset are
                   traceable to a primary reference.
                ''',
                'time_traceable',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'time-properties-ds',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.PortDsList.PortIdentity' : {
        'meta_info' : _MetaInfoClass('InstanceList.PortDsList.PortIdentity',
            False, 
            [
            _MetaInfoClassMember('clock-identity', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                Identity of the clock
                ''',
                'clock_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port number
                ''',
                'port_number',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'port-identity',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList.PortDsList' : {
        'meta_info' : _MetaInfoClass('InstanceList.PortDsList',
            False, 
            [
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Refers to the portNumber memer of
                portDS.portIdentity.
                ''',
                'port_number',
                'ietf-ptp-dataset', True),
            _MetaInfoClassMember('announce-receipt-timeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The number of announceInterval that have to pass
                without receipt of an Announce message before the
                occurrence of the event ANNOUNCE_RECEIPT_TIMEOUT_
                EXPIRES.
                ''',
                'announce_receipt_timeout',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('delay-mechanism', REFERENCE_ENUM_CLASS, 'DelayMechanismEnumerationEnum' , 'ydk.models.ietf.ietf_ptp_dataset', 'DelayMechanismEnumerationEnum', 
                [], [], 
                '''                The propagation delay measuring option used by the
                port in computing meanPathDelay.
                ''',
                'delay_mechanism',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('log-announce-interval', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                The base-two logarithm of the mean
                announceInterval (mean time interval between
                successive Announce messages).
                ''',
                'log_announce_interval',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('log-min-delay-req-interval', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                The base-two logarithm of the minDelayReqInterval
                (the minimum permitted mean time interval between
                successive Delay_Req messages).
                ''',
                'log_min_delay_req_interval',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('log-min-pdelay-req-interval', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                The base-two logarithm of the
                minPdelayReqInterval (minimum permitted mean time
                interval between successive Pdelay_Req messages).
                ''',
                'log_min_pdelay_req_interval',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('log-sync-interval', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                The base-two logarithm of the mean SyncInterval
                for multicast messages.  The rates for unicast
                transmissions are negotiated separately on a per port
                basis and are not constrained by this attribute.
                ''',
                'log_sync_interval',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('peer-mean-path-delay', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                An estimate of the current one-way propagation delay
                on the link when the delayMechanism is P2P; otherwise,
                it is zero.
                ''',
                'peer_mean_path_delay',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('port-identity', REFERENCE_CLASS, 'PortIdentity' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.PortDsList.PortIdentity', 
                [], [], 
                '''                The portIdentity attribute of the local port.
                ''',
                'port_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('port-state', REFERENCE_ENUM_CLASS, 'PortStateEnumerationEnum' , 'ydk.models.ietf.ietf_ptp_dataset', 'PortStateEnumerationEnum', 
                [], [], 
                '''                Current state associated with the port.
                ''',
                'port_state',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('version-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The PTP version in use on the port.
                ''',
                'version_number',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'port-ds-list',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'InstanceList' : {
        'meta_info' : _MetaInfoClass('InstanceList',
            False, 
            [
            _MetaInfoClassMember('instance-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The instance number of the current PTP instance
                ''',
                'instance_number',
                'ietf-ptp-dataset', True),
            _MetaInfoClassMember('current-ds', REFERENCE_CLASS, 'CurrentDs' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.CurrentDs', 
                [], [], 
                '''                The current data set of the clock.
                ''',
                'current_ds',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('default-ds', REFERENCE_CLASS, 'DefaultDs' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.DefaultDs', 
                [], [], 
                '''                The default data set of the clock.
                ''',
                'default_ds',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('parent-ds', REFERENCE_CLASS, 'ParentDs' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.ParentDs', 
                [], [], 
                '''                The parent data set of the clock.
                ''',
                'parent_ds',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('port-ds-list', REFERENCE_LIST, 'PortDsList' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.PortDsList', 
                [], [], 
                '''                List of port data sets of the clock.
                ''',
                'port_ds_list',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('time-properties-ds', REFERENCE_CLASS, 'TimePropertiesDs' , 'ydk.models.ietf.ietf_ptp_dataset', 'InstanceList.TimePropertiesDs', 
                [], [], 
                '''                The timeProperties data set of the clock.
                ''',
                'time_properties_ds',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'instance-list',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'TransparentClockDefaultDs' : {
        'meta_info' : _MetaInfoClass('TransparentClockDefaultDs',
            False, 
            [
            _MetaInfoClassMember('clock-identity', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                The clockIdentity of the transparent clock.
                ''',
                'clock_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('delay-mechanism', REFERENCE_ENUM_CLASS, 'DelayMechanismEnumerationEnum' , 'ydk.models.ietf.ietf_ptp_dataset', 'DelayMechanismEnumerationEnum', 
                [], [], 
                '''                The propagation delay measuring option
                used by the transparent clock.
                ''',
                'delay_mechanism',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('number-ports', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of PTP ports on the device.
                ''',
                'number_ports',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('primary-domain', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The domainNumber of the primary syntonization domain.
                ''',
                'primary_domain',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'transparent-clock-default-ds',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'TransparentClockPortDsList.PortIdentity' : {
        'meta_info' : _MetaInfoClass('TransparentClockPortDsList.PortIdentity',
            False, 
            [
            _MetaInfoClassMember('clock-identity', ATTRIBUTE, 'str' , None, None, 
                [(8, None)], [], 
                '''                Identity of the clock
                ''',
                'clock_identity',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Port number
                ''',
                'port_number',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'port-identity',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
    'TransparentClockPortDsList' : {
        'meta_info' : _MetaInfoClass('TransparentClockPortDsList',
            False, 
            [
            _MetaInfoClassMember('port-number', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                Refers to the portNumber memer
                of transparentClockPortDS.portIdentity.
                ''',
                'port_number',
                'ietf-ptp-dataset', True),
            _MetaInfoClassMember('faulty-flag', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                When set, the port is faulty.
                ''',
                'faulty_flag',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('log-min-pdelay-req-interval', ATTRIBUTE, 'int' , None, None, 
                [('-128', '127')], [], 
                '''                The logarithm to the base 2 of the
                minPdelayReqInterval (minimum permitted mean time
                interval between successive Pdelay_Req messages).
                ''',
                'log_min_pdelay_req_interval',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('peer-mean-path-delay', ATTRIBUTE, 'int' , None, None, 
                [('-9223372036854775808', '9223372036854775807')], [], 
                '''                An estimate of the current one-way propagation delay
                on the link when the delayMechanism is P2P; otherwise,
                it is zero.
                ''',
                'peer_mean_path_delay',
                'ietf-ptp-dataset', False),
            _MetaInfoClassMember('port-identity', REFERENCE_CLASS, 'PortIdentity' , 'ydk.models.ietf.ietf_ptp_dataset', 'TransparentClockPortDsList.PortIdentity', 
                [], [], 
                '''                The portIdentity of the local port.
                ''',
                'port_identity',
                'ietf-ptp-dataset', False),
            ],
            'ietf-ptp-dataset',
            'transparent-clock-port-ds-list',
            _yang_ns._namespaces['ietf-ptp-dataset'],
        'ydk.models.ietf.ietf_ptp_dataset'
        ),
    },
}
_meta_table['InstanceList.DefaultDs.ClockQuality']['meta_info'].parent =_meta_table['InstanceList.DefaultDs']['meta_info']
_meta_table['InstanceList.ParentDs.ParentPortIdentity']['meta_info'].parent =_meta_table['InstanceList.ParentDs']['meta_info']
_meta_table['InstanceList.ParentDs.GrandmasterClockQuality']['meta_info'].parent =_meta_table['InstanceList.ParentDs']['meta_info']
_meta_table['InstanceList.PortDsList.PortIdentity']['meta_info'].parent =_meta_table['InstanceList.PortDsList']['meta_info']
_meta_table['InstanceList.DefaultDs']['meta_info'].parent =_meta_table['InstanceList']['meta_info']
_meta_table['InstanceList.CurrentDs']['meta_info'].parent =_meta_table['InstanceList']['meta_info']
_meta_table['InstanceList.ParentDs']['meta_info'].parent =_meta_table['InstanceList']['meta_info']
_meta_table['InstanceList.TimePropertiesDs']['meta_info'].parent =_meta_table['InstanceList']['meta_info']
_meta_table['InstanceList.PortDsList']['meta_info'].parent =_meta_table['InstanceList']['meta_info']
_meta_table['TransparentClockPortDsList.PortIdentity']['meta_info'].parent =_meta_table['TransparentClockPortDsList']['meta_info']
