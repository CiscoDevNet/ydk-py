


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'CISCOPROCESSMIB.CpmCPUHistory' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUHistory',
            False, 
            [
            _MetaInfoClassMember('cpmCPUHistorySize', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                A value configured by the user which specifies the
                number of reports in the history table. 
                A report contains set of processes which crossed
                the cpmCPUHistoryThreshold 
                in the last cpmCPUMonInterval along with 
                the time at which this report is
                created, total and interrupt CPU utilizations. 
                When this object is changed
                the new value will have effect in the next interval.
                ''',
                'cpmcpuhistorysize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryThreshold', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                The user  configured value of this object gives
                the minimum percent CPU utilization of a process
                in the last cpmCPUMonInterval duration required to be a 
                member of history table. When this object is changed
                the new value will have effect in the next interval.
                ''',
                'cpmcpuhistorythreshold',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUHistory',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUHistoryReportId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                All the entries which are created at the same time
                will have same value for this object. When the
                configured threshold for being a part of History table
                is reached then the qualified processes become the
                part of history table. The entries which became the 
                part of history table at one instant will have
                the same value for this object. When this object
                reaches the max index value then it will wrap around.
                ''',
                'cpmcpuhistoryreportid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUHistoryCreatedTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Time stamp with respect to sysUpTime indicating
                the time at which this report is created.
                ''',
                'cpmcpuhistorycreatedtime',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryInterruptUtil', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                Percentage of CPU utilization in the interrupt context
                at cpmCPUHistoryCreated.
                ''',
                'cpmcpuhistoryinterruptutil',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryReportSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of process entries in a report.
                This object gives information about how many processes 
                became a part of history table at one instant.
                ''',
                'cpmcpuhistoryreportsize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryTotalUtil', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                Total percentage of CPU utilization
                at cpmCPUHistoryCreated.
                ''',
                'cpmcpuhistorytotalutil',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUHistoryEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUHistoryTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUHistoryTable',
            False, 
            [
            _MetaInfoClassMember('cpmCPUHistoryEntry', REFERENCE_LIST, 'CpmCPUHistoryEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry', 
                [], [], 
                '''                A historical sample of CPU utilization statistics.
                cpmCPUTotalIndex identifies the CPU (or group of CPUs)
                for which this history is collected. 
                When the cpmCPUHistorySize is
                reached the least recent entry is lost.
                ''',
                'cpmcpuhistoryentry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUHistoryTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUHistoryReportId', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cpmcpuhistoryreportid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUProcessHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index that uniquely identifies an entry in
                the cmpCPUProcessHistory table among those in the 
                same report. This index is between 1 to N, 
                where N is the cpmCPUHistoryReportSize.
                ''',
                'cpmcpuprocesshistoryindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUHistoryProcCreated', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time when the process was created. The process ID
                and the time when the process was created, uniquely 
                identifies a process.
                ''',
                'cpmcpuhistoryproccreated',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryProcId', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The process Id associated with this entry.
                ''',
                'cpmcpuhistoryprocid',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryProcName', ATTRIBUTE, 'str' , None, None, 
                [], ['\\p{IsBasicLatin}{0,255}'], 
                '''                The process name associated with this entry.
                ''',
                'cpmcpuhistoryprocname',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryProcUtil', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The percentage CPU utilization of a process at
                cpmCPUHistoryCreatedTime.
                ''',
                'cpmcpuhistoryprocutil',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUProcessHistoryEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUProcessHistoryTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUProcessHistoryTable',
            False, 
            [
            _MetaInfoClassMember('cpmCPUProcessHistoryEntry', REFERENCE_LIST, 'CpmCPUProcessHistoryEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry', 
                [], [], 
                '''                A historical sample of process utilization
                statistics. The entries in this table will have
                corresponding entires in the cpmCPUHistoryTable.
                The entries in this table get deleted when the entry
                associated with this entry in the cpmCPUHistoryTable 
                gets deleted.
                ''',
                'cpmcpuprocesshistoryentry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUProcessHistoryTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry.CpmCPUThresholdClass_Enum' : _MetaInfoEnum('CpmCPUThresholdClass_Enum', 'ydk.models.process.CISCO_PROCESS_MIB',
        {
            'total':'TOTAL',
            'interrupt':'INTERRUPT',
            'process':'PROCESS',
        }, 'CISCO-PROCESS-MIB', _yang_ns._namespaces['CISCO-PROCESS-MIB']),
    'CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUThresholdClass', REFERENCE_ENUM_CLASS, 'CpmCPUThresholdClass_Enum' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry.CpmCPUThresholdClass_Enum', 
                [], [], 
                '''                Value of this object indicates the type of
                utilization, which is monitored. The total(1) indicates
                the total CPU utilization, interrupt(2) indicates the
                the CPU utilization in interrupt context and process(3)
                indicates the CPU utilization in the process level
                execution context.
                ''',
                'cpmcputhresholdclass',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUFallingThresholdPeriod', ATTRIBUTE, 'int' , None, None, 
                [(5, 4294967295)], [], 
                '''                This is an observation interval. The value of this
                object indicates that CPU utilization should be below
                cpmCPUFallingThresholdValue for this duration to send a 
                cpmCPURisingThreshold notification to the NMS.
                ''',
                'cpmcpufallingthresholdperiod',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUFallingThresholdValue', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                The percentage falling threshold value configured by
                the user. The value indicates, if the percentage 
                CPU utilization is equal to or below this value for 
                cpmCPUFallingThresholdPeriod duration
                then send a cpmCPUFallingThreshold notification 
                to the NMS.
                ''',
                'cpmcpufallingthresholdvalue',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPURisingThresholdPeriod', ATTRIBUTE, 'int' , None, None, 
                [(5, 4294967295)], [], 
                '''                This is an observation interval.
                The value of this object indicates that 
                the CPU utilization should be above
                cpmCPURisingThresholdValue for this duration to send a 
                cpmCPURisingThreshold notification to the NMS.
                ''',
                'cpmcpurisingthresholdperiod',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPURisingThresholdValue', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                The percentage rising threshold value configured by
                the user. The value indicates, 
                if the percentage CPU utilization is equal to or above
                this value for cpmCPURisingThresholdPeriod duration 
                then send a cpmCPURisingThreshold notification to
                the NMS.
                ''',
                'cpmcpurisingthresholdvalue',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUThresholdEntryStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this table entry.
                ''',
                'cpmcputhresholdentrystatus',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUThresholdEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUThresholdTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUThresholdTable',
            False, 
            [
            _MetaInfoClassMember('cpmCPUThresholdEntry', REFERENCE_LIST, 'CpmCPUThresholdEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry', 
                [], [], 
                '''                An entry containing information about
                CPU thresholding parameters. cpmCPUTotalIndex
                identifies the CPU (or group of CPUs) for which this
                configuration applies.
                ''',
                'cpmcputhresholdentry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUThresholdTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                An index that uniquely represents a CPU (or group of CPUs)
                whose CPU load information is reported by a row in this table.
                This index is assigned arbitrarily by the engine
                and is not saved over reboots.
                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmCPUInterruptMonIntervalValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The overall CPU busy percentage in the
                interrupt context in the last cpmCPUMonInterval
                period.
                ''',
                'cpmcpuinterruptmonintervalvalue',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPULoadAvg15min', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The overall CPU load Average in the last 15 minutes period
                ''',
                'cpmcpuloadavg15min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPULoadAvg1min', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The overall CPU load Average in the last 1 minute period
                ''',
                'cpmcpuloadavg1min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPULoadAvg5min', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The overall CPU load Average in the last 5 minutes period
                ''',
                'cpmcpuloadavg5min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryCommitted', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The overall CPU wide system memory which is currently
                Committed.
                ''',
                'cpmcpumemorycommitted',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryCommittedOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmCPUMemoryCommitted.
                This object needs to be supported only when the value of
                cpmCPUMemoryCommitted exceeds 32-bit, otherwise this object
                value would be set to 0.
                ''',
                'cpmcpumemorycommittedovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryFree', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The overall CPU wide system memory which is currently
                free.
                ''',
                'cpmcpumemoryfree',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryFreeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of cpmCPUMemoryFree.
                This object needs to be supported only when the value of
                cpmCPUMemoryFree exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'cpmcpumemoryfreeovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryHCCommitted', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The overall CPU wide system memory which is currently
                committed. This object is a 64-bit version of
                cpmCPUMemoryCommitted
                ''',
                'cpmcpumemoryhccommitted',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryHCFree', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The overall CPU wide system memory which is currently free.
                This object is a 64-bit version of cpmCPUMemoryFree.
                ''',
                'cpmcpumemoryhcfree',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryHCKernelReserved', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The overall CPU wide system memory which is reserved
                for kernel usage. This object is a 64-bit version of
                cpmCPUMemoryKernelReserved.
                ''',
                'cpmcpumemoryhckernelreserved',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryHCLowest', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The lowest free memory that has been recorded since device has
                booted. This object is a 64-bit version of cpmCPUMemoryLowest.
                ''',
                'cpmcpumemoryhclowest',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryHCUsed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The overall CPU wide system memory which is currently under
                use. This object is a 64-bit version of cpmCPUMemoryUsed.
                ''',
                'cpmcpumemoryhcused',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryKernelReserved', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The overall CPU wide system memory which is reserved
                for kernel usage.
                ''',
                'cpmcpumemorykernelreserved',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryKernelReservedOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmCPUMemoryKernelReserved. This object needs 
                to be supported only when the value of 
                cpmCPUMemoryKernelReserved exceeds 32-bit, otherwise
                this object value would be set to 0.
                ''',
                'cpmcpumemorykernelreservedovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryLowest', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The lowest free memory that has been recorded since
                device has booted.
                ''',
                'cpmcpumemorylowest',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryLowestOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of cpmCPUMemoryLowest.
                This object needs to be supported only when the value of
                cpmCPUMemoryLowest exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'cpmcpumemorylowestovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryUsed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The overall CPU wide system memory which is currently
                under use.
                ''',
                'cpmcpumemoryused',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMemoryUsedOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of cpmCPUMemoryUsed.
                This object needs to be supported only when the value of
                cpmCPUMemoryUsed exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'cpmcpumemoryusedovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUMonInterval', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                CPU usage monitoring interval. The value of this
                object in seconds indicates the how often the 
                CPU utilization is calculated and monitored.
                ''',
                'cpmcpumoninterval',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotal1min', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                The overall CPU busy percentage in the last 1 minute
                period. This object obsoletes the avgBusy1 object from 
                the OLD-CISCO-SYSTEM-MIB. This object is deprecated
                by cpmCPUTotal1minRev which has the changed range
                of value (0..100).
                ''',
                'cpmcputotal1min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotal1minRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The overall CPU busy percentage in the last 1 minute
                period. This object deprecates the object cpmCPUTotal1min 
                and increases the value range to (0..100).
                ''',
                'cpmcputotal1minrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotal5min', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                The overall CPU busy percentage in the last 5 minute
                period. This object deprecates the avgBusy5 object from 
                the OLD-CISCO-SYSTEM-MIB. This object is deprecated
                by cpmCPUTotal5minRev which has the changed range 
                of value (0..100).
                ''',
                'cpmcputotal5min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotal5minRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The overall CPU busy percentage in the last 5 minute
                period. This object deprecates the object cpmCPUTotal5min 
                and increases the value range to (0..100).
                ''',
                'cpmcputotal5minrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotal5sec', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                The overall CPU busy percentage in the last 5 second
                period. This object obsoletes the busyPer object from 
                the OLD-CISCO-SYSTEM-MIB. This object is deprecated
                by cpmCPUTotal5secRev which has the changed range of
                value (0..100).
                ''',
                'cpmcputotal5sec',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotal5secRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The overall CPU busy percentage in the last 5 second
                period. This object deprecates the object cpmCPUTotal5sec 
                and increases the value range to (0..100). This object
                is deprecated by cpmCPUTotalMonIntervalValue
                ''',
                'cpmcputotal5secrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotalMonIntervalValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                The overall CPU busy percentage in the last
                cpmCPUMonInterval period. 
                This object deprecates the object cpmCPUTotal5secRev.
                ''',
                'cpmcputotalmonintervalvalue',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotalPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The entPhysicalIndex of the physical entity for which
                the CPU statistics in this entry are maintained.
                The physical entity can be a CPU chip, a group of CPUs,
                a CPU card etc. The exact type of this entity is described by
                its entPhysicalVendorType value. If the CPU statistics
                in this entry correspond to more than one physical entity
                (or to no physical entity), or if the entPhysicalTable is
                not supported on the SNMP agent, the value of this object
                must be zero.
                ''',
                'cpmcputotalphysicalindex',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUTotalEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmCPUTotalTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmCPUTotalTable',
            False, 
            [
            _MetaInfoClassMember('cpmCPUTotalEntry', REFERENCE_LIST, 'CpmCPUTotalEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry', 
                [], [], 
                '''                Overall information about the CPU load. Entries in this
                table come and go as CPUs are added and removed from the
                system.
                ''',
                'cpmcputotalentry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmCPUTotalTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcExtPriorityRev_Enum' : _MetaInfoEnum('CpmProcExtPriorityRev_Enum', 'ydk.models.process.CISCO_PROCESS_MIB',
        {
            'critical':'CRITICAL',
            'high':'HIGH',
            'normal':'NORMAL',
            'low':'LOW',
            'notAssigned':'NOTASSIGNED',
        }, 'CISCO-PROCESS-MIB', _yang_ns._namespaces['CISCO-PROCESS-MIB']),
    'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessMemoryCore_Enum' : _MetaInfoEnum('CpmProcessMemoryCore_Enum', 'ydk.models.process.CISCO_PROCESS_MIB',
        {
            'other':'OTHER',
            'mainmem':'MAINMEM',
            'mainmemSharedmem':'MAINMEMSHAREDMEM',
            'mainmemText':'MAINMEMTEXT',
            'mainmemTextSharedmem':'MAINMEMTEXTSHAREDMEM',
            'sharedmem':'SHAREDMEM',
            'sparse':'SPARSE',
            'off':'OFF',
        }, 'CISCO-PROCESS-MIB', _yang_ns._namespaces['CISCO-PROCESS-MIB']),
    'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessType_Enum' : _MetaInfoEnum('CpmProcessType_Enum', 'ydk.models.process.CISCO_PROCESS_MIB',
        {
            'other':'OTHER',
            'posix':'POSIX',
            'ios':'IOS',
        }, 'CISCO-PROCESS-MIB', _yang_ns._namespaces['CISCO-PROCESS-MIB']),
    'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmProcessPID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cpmprocesspid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmProcessDataSegmentSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This indicates the data segment of a process and
                all its shared objects.
                ''',
                'cpmprocessdatasegmentsize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessDataSegmentSizeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmProcessDataSegmentSize. This object needs
                to be supported only when the value of 
                cpmProcessDataSegmentSize exceeds 32-bit, 
                otherwise this object value would be set to 0.
                ''',
                'cpmprocessdatasegmentsizeovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessDynamicMemorySize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This indicates the amount of dynamic memory being used
                by the process.
                ''',
                'cpmprocessdynamicmemorysize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessDynamicMemorySizeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmProcessDynamicMemorySize. This object needs
                to be supported only when the value of 
                cpmProcessDynamicMemorySize exceeds 32-bit, 
                otherwise this object value would be set to 0.
                ''',
                'cpmprocessdynamicmemorysizeovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessHCDataSegmentSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This indicates the data segment of a process and
                all its shared objects.. This object is a 64-bit
                version of cpmProcessDataSegmentSize.
                ''',
                'cpmprocesshcdatasegmentsize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessHCDynamicMemorySize', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This indicates the amount of dynamic memory being used
                by the process. This object is a 64-bit version of
                cpmProcessDynamicMemorySize.
                ''',
                'cpmprocesshcdynamicmemorysize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessHCStackSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This indicates the amount of stack memory used by the process.
                This object is a 64-bit version of cpmProcessStackSize.
                ''',
                'cpmprocesshcstacksize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessHCTextSegmentSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This indicates the text memory of a process and all
                its shared objects. This object is a 64-bit version
                of cpmProcessTextSegmentSize.
                ''',
                'cpmprocesshctextsegmentsize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessLastRestartUser', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This indicate the user that has last restarted the
                process or has taken running coredump of the process.
                ''',
                'cpmprocesslastrestartuser',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessMemoryCore', REFERENCE_ENUM_CLASS, 'CpmProcessMemoryCore_Enum' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessMemoryCore_Enum', 
                [], [], 
                '''                This indicates the part of process memory to be
                dumped when a process crashes. The process 
                memory is used for debugging purposes to trace the 
                root cause of the crash.
                sparse        - Some operating systems support minimal
                                dump of process core like register
                                info, partial stack, partial memory
                                pages especially for critical process
                                to facilitate faster process restart.
                ''',
                'cpmprocessmemorycore',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessRespawn', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This indicates whether respawn of a process is enabled
                or not. If enabled the process in context repawns after
                it has crashed/stopped.
                ''',
                'cpmprocessrespawn',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessRespawnAfterLastPatch', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This indicates the number of times a process has
                restarted after the last patch is applied. This is to 
                determine the stability of the last patch.
                ''',
                'cpmprocessrespawnafterlastpatch',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessRespawnCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This indicates the number of times the process has
                respawned/restarted.
                ''',
                'cpmprocessrespawncount',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessStackSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This indicates the amount of stack memory used by the
                process.
                ''',
                'cpmprocessstacksize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessStackSizeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of cpmProcessStackSize.
                This object needs to be supported only when the value of
                cpmProcessStackSize exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'cpmprocessstacksizeovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessTextSegmentSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This indicates the text memory of a process and all
                its shared objects.
                ''',
                'cpmprocesstextsegmentsize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessTextSegmentSizeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmProcessTextSegmentSize. This object needs
                to be supported only when the value of 
                cpmProcessTextSegmentSize exceeds 32-bit, 
                otherwise this object value would be set to 0.
                ''',
                'cpmprocesstextsegmentsizeovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessType', REFERENCE_ENUM_CLASS, 'CpmProcessType_Enum' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessType_Enum', 
                [], [], 
                '''                This indicates the kind of process in context.
                ''',
                'cpmprocesstype',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtHCMemAllocatedRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The sum of all the dynamically allocated memory that this
                process has received from the system. This includes memory
                that may have been returned. This object is a 64-bit version
                of cpmProcExtMemAllocatedRev.
                ''',
                'cpmprocexthcmemallocatedrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtHCMemFreedRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                The sum of all memory that this process has returned to the
                system. This object is a 64-bit version of
                cpmProcExtMemFreedRev.
                ''',
                'cpmprocexthcmemfreedrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtInvokedRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times since cpmTimeCreated that
                the process has been invoked. This object 
                deprecates cpmProcExtInvoked.
                ''',
                'cpmprocextinvokedrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtMemAllocatedRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The sum of all the dynamically allocated memory that
                this process has received from the system. This includes
                memory that may have been returned. The sum of freed
                memory is provided by cpmProcExtMemFreedRev. This object
                deprecates cpmProcExtMemAllocated.
                ''',
                'cpmprocextmemallocatedrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtMemAllocatedRevOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmProcExtMemAllocatedRev. This object needs
                to be supported only when the value of 
                cpmProcExtMemAllocatedRev exceeds 32-bit, 
                otherwise this object value would be set to 0.
                ''',
                'cpmprocextmemallocatedrevovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtMemFreedRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The sum of all memory that this process has returned
                to the system. This object  deprecates 
                cpmProcExtMemFreed.
                ''',
                'cpmprocextmemfreedrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtMemFreedRevOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmProcExtMemFreedRev. This object needs to 
                be supported only when the value of
                cpmProcExtMemFreedRev exceeds 32-bit,otherwise
                this object value would be set to 0.
                ''',
                'cpmprocextmemfreedrevovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtPriorityRev', REFERENCE_ENUM_CLASS, 'CpmProcExtPriorityRev_Enum' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcExtPriorityRev_Enum', 
                [], [], 
                '''                The priority level at  which the process is
                running. This object deprecates 
                cpmProcExtPriority.
                ''',
                'cpmprocextpriorityrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtRuntimeRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of CPU time the process has used, in
                microseconds. This object deprecates
                cpmProcExtRuntime.
                ''',
                'cpmprocextruntimerev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtUtil1MinRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                This object provides a general idea of how busy
                a process caused the processor to be over a 1 
                minute period. It is determined as a weighted 
                decaying average of the current idle time over the 
                longest idle time. Note that this information 
                should be used as an estimate only. This object 
                deprecates cpmProcExtUtil1Min and increases the value
                range to (0..100).
                ''',
                'cpmprocextutil1minrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtUtil5MinRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                This object provides a general idea of how busy
                a process caused the processor to be over a 5 
                minute period. It is determined as a weighted 
                decaying average of the current idle time over 
                the longest idle time. Note that this information 
                should be used as an estimate only. This object
                deprecates cpmProcExtUtil5Min and increases the
                value range to (0..100).
                ''',
                'cpmprocextutil5minrev',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtUtil5SecRev', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                This object provides a general idea of how busy
                a process caused the processor to be over a 5 
                second period. It is determined as a weighted 
                decaying average of the current idle time over 
                the longest idle time. Note that this information 
                should be used as an estimate only. This object
                deprecates cpmProcExtUtil5Sec and increases the 
                value range to (0..100).
                ''',
                'cpmprocextutil5secrev',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmProcessExtRevEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmProcessExtRevTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmProcessExtRevTable',
            False, 
            [
            _MetaInfoClassMember('cpmProcessExtRevEntry', REFERENCE_LIST, 'CpmProcessExtRevEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry', 
                [], [], 
                '''                An entry containing additional information for
                a particular process. This object deprecates 
                cpmProcessExtEntry.
                ''',
                'cpmprocessextreventry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmProcessExtRevTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry.CpmProcExtPriority_Enum' : _MetaInfoEnum('CpmProcExtPriority_Enum', 'ydk.models.process.CISCO_PROCESS_MIB',
        {
            'critical':'CRITICAL',
            'high':'HIGH',
            'normal':'NORMAL',
            'low':'LOW',
            'notAssigned':'NOTASSIGNED',
        }, 'CISCO-PROCESS-MIB', _yang_ns._namespaces['CISCO-PROCESS-MIB']),
    'CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmProcessPID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object contains the process ID. cpmTimeCreated
                should be checked against the last time it was polled,
                and if it has changed the PID has been reused and the
                entire entry should be polled again.
                ''',
                'cpmprocesspid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmProcessAverageUSecs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average elapsed CPU time in microseconds when the
                process was active. This object deprecates the
                object cpmProcessuSecs.
                ''',
                'cpmprocessaverageusecs',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                The name associated with this process. If the name is
                longer than 32 characters, it will be truncated to the first
                31 characters, and a `*' will be appended as the last
                character to imply this is a truncated process name.
                ''',
                'cpmprocessname',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessTimeCreated', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The time when the process was created. The process ID
                and the time when the process was created, uniquely 
                identifies a process.
                ''',
                'cpmprocesstimecreated',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessuSecs', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                Average elapsed CPU time in microseconds when the
                process was active. This object is deprecated
                by cpmProcessAverageUSecs.
                ''',
                'cpmprocessusecs',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtInvoked', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times since cpmTimeCreated that
                the process has been invoked. This object is
                deprecated by cpmProcExtInvokedRev.
                ''',
                'cpmprocextinvoked',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtMemAllocated', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The sum of all the dynamically allocated memory that
                this process has received from the system. This includes
                memory that may have been returned. The sum of freed
                memory is provided by cpmProcExtMemFreed. This object
                is deprecated by cpmProcExtMemAllocatedRev.
                ''',
                'cpmprocextmemallocated',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtMemFreed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The sum of all memory that this process has returned
                to the system. This object is deprecated by 
                cpmProcExtMemFreedRev.
                ''',
                'cpmprocextmemfreed',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtPriority', REFERENCE_ENUM_CLASS, 'CpmProcExtPriority_Enum' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry.CpmProcExtPriority_Enum', 
                [], [], 
                '''                The priority level at which the process is
                running. This object is deprecated by
                cpmProcExtPriorityRev.
                ''',
                'cpmprocextpriority',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtRuntime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of CPU time the process has used, in
                microseconds. This object is deprecated by
                cpmProcExtRuntimeRev.
                ''',
                'cpmprocextruntime',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtUtil1Min', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                This object provides a general idea of how busy
                a process caused the processor to be over a 1 
                minute period. It is determined as a weighted 
                decaying average of the current idle time over the 
                longest idle time. Note that this information 
                should be used as an estimate only. This object is 
                deprecated by cpmProcExtUtil1MinRev which has
                the changed range of value (0..100).
                ''',
                'cpmprocextutil1min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtUtil5Min', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                This object provides a general idea of how busy
                a process caused the processor to be over a 5 
                minute period. It is determined as a weighted 
                decaying average of the current idle time over 
                the longest idle time. Note that this information 
                should be used as an estimate only. This object
                is deprecated by cpmProcExtUtil5MinRev which
                has the changed range of value (0..100).
                ''',
                'cpmprocextutil5min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcExtUtil5Sec', ATTRIBUTE, 'int' , None, None, 
                [(1, 100)], [], 
                '''                This object provides a general idea of how busy
                a process caused the processor to be over a 5 
                second period. It is determined as a weighted 
                decaying average of the current idle time over 
                the longest idle time. Note that this information 
                should be used as an estimate only. This object is 
                deprecated by cpmProcExtUtil5SecRev which has the 
                changed range of value (0..100).
                ''',
                'cpmprocextutil5sec',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmProcessEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmProcessTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmProcessTable',
            False, 
            [
            _MetaInfoClassMember('cpmProcessEntry', REFERENCE_LIST, 'CpmProcessEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry', 
                [], [], 
                '''                Generic information about an active process on this
                device. Entries in this table come and go as processes are 
                created and destroyed by the device.
                ''',
                'cpmprocessentry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmProcessTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry.CpmThreadState_Enum' : _MetaInfoEnum('CpmThreadState_Enum', 'ydk.models.process.CISCO_PROCESS_MIB',
        {
            'other':'OTHER',
            'dead':'DEAD',
            'running':'RUNNING',
            'ready':'READY',
            'stopped':'STOPPED',
            'send':'SEND',
            'receive':'RECEIVE',
            'reply':'REPLY',
            'stack':'STACK',
            'waitpage':'WAITPAGE',
            'sigsuspend':'SIGSUSPEND',
            'sigwaitinfo':'SIGWAITINFO',
            'nanosleep':'NANOSLEEP',
            'mutex':'MUTEX',
            'condvar':'CONDVAR',
            'join':'JOIN',
            'intr':'INTR',
            'sem':'SEM',
        }, 'CISCO-PROCESS-MIB', _yang_ns._namespaces['CISCO-PROCESS-MIB']),
    'CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmProcessPID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cpmprocesspid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmThreadID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object contains the thread ID. ThreadID is
                Unique per process.
                ''',
                'cpmthreadid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmThreadBlockingProcess', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the process on which the
                current thread is blocked on. This points to the 
                cpmProcessTable of the process on which the thread 
                in context is blocked. This is valid only to threads
                which are either in send/reply states. For the 
                rest of the threads it is returned as 0.0
                ''',
                'cpmthreadblockingprocess',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadCpuUtilization', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object provides a general idea on how busy
                the thread in context caused the processor to be.
                ''',
                'cpmthreadcpuutilization',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadHCStackSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the stack size allocated to the
                thread in context. This object is a 64-bit version of
                cpmThreadStackSize.
                ''',
                'cpmthreadhcstacksize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadName', ATTRIBUTE, 'str' , None, None, 
                [('0', 255)], [], 
                '''                This object represents the name of the thread.
                Thread names need not be unique. Hence statistics 
                should be analyzed against thread ID.
                ''',
                'cpmthreadname',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadPriority', ATTRIBUTE, 'int' , None, None, 
                [(0, 63)], [], 
                '''                This object indicates the priority of a POSIX thread.
                The higher the number, the higher the priority of the 
                thread over other threads.
                ''',
                'cpmthreadpriority',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadStackSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the stack size allocated to
                the thread in context.
                ''',
                'cpmthreadstacksize',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadStackSizeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of cpmThreadStackSize.
                This object needs to be supported only when the value of
                cpmThreadStackSize exceeds 32-bit, otherwise this object value
                would be set to 0.
                ''',
                'cpmthreadstacksizeovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadState', REFERENCE_ENUM_CLASS, 'CpmThreadState_Enum' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry.CpmThreadState_Enum', 
                [], [], 
                '''                This object indicates the current state of a thread.
                Running state means that the thread is actively 
                consumig CPU. All the other states are just waiting 
                states. The valid states are:
                other         - Any other state apart from the listed 
                                ones.
                dead          - Kernel is waiting to release the 
                                thread's resources.
                running       - Actively running on a CPU.
                ready         - Not running on a CPU, but is ready to 
                                run (one or more higher or equal 
                                priority threads are running).
                stopped       - Suspended (SIGSTOP signal).
                send          - Waiting for a server to receive 
                                a message.
                receive       - Waiting for a client to send a message.
                reply         - Waiting for a server to reply to a 
                                message.
                stack         - Waiting for more stack to be allocated.
                waitpage      - Waiting for process manager to 
                                resolve a fault on a page.
                sigsuspend    - Suspended for a signal.
                sigwaitinfo   - Waiting for a signal.
                nanosleep     - Sleeping for a period of time.
                mutex         - Waiting to acquire a mutex
                condvar       - Waiting for a condition variable to be 
                                signalled.
                join          - Waiting for the completion of another 
                                thread.
                intr          - Waiting for an interrupt.
                sem           - Waiting to acquire a semaphore.
                ''',
                'cpmthreadstate',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmThreadEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmThreadTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmThreadTable',
            False, 
            [
            _MetaInfoClassMember('cpmThreadEntry', REFERENCE_LIST, 'CpmThreadEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry', 
                [], [], 
                '''                An entry containing the general statistics
                of a POSIX thread.
                ''',
                'cpmthreadentry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmThreadTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry',
            False, 
            [
            _MetaInfoClassMember('cpmCPUTotalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 4294967295)], [], 
                '''                ''',
                'cpmcputotalindex',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmProcessPID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                ''',
                'cpmprocesspid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmVirtualProcessID', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the process ID of a virtual
                process. PID is unique only inside one address space.
                Virtual process PID should be considered along with 
                Parent process cpmProcessPID.
                ''',
                'cpmvirtualprocessid',
                'CISCO-PROCESS-MIB', True),
            _MetaInfoClassMember('cpmVirtualProcessHCMemAllocated', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the memory allocated by the
                virtual process inside the address space of a process
                running on Native OS. This object is a 64-bit version
                of cpmVirtualProcessMemAllocated.
                ''',
                'cpmvirtualprocesshcmemallocated',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessHCMemFreed', ATTRIBUTE, 'int' , None, None, 
                [(0, 18446744073709551615L)], [], 
                '''                This object indicates the memory freed by the virtual process
                inside the address space of a process running on Native OS.This
                object is a 64-bit version of cpmVirtualProcessMemAllocated.
                ''',
                'cpmvirtualprocesshcmemfreed',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessInvokeCount', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times a virtual process is invoked.
                ''',
                'cpmvirtualprocessinvokecount',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessMemAllocated', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the memory allocated by the
                virtual process inside the address space of a 
                process running on Native OS.
                ''',
                'cpmvirtualprocessmemallocated',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessMemAllocatedOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmVirtualProcessMemAllocated. This object 
                needs to be supported only when the value of
                cpmVirtualProcessMemAllocated exceeds 32-bit,
                otherwise this object value would be set to 0.
                ''',
                'cpmvirtualprocessmemallocatedovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessMemFreed', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object indicates the memory freed by the virtual
                process inside the address space of a process running 
                on Native OS.
                ''',
                'cpmvirtualprocessmemfreed',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessMemFreedOvrflw', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                This object represents the upper 32-bit of
                cpmVirtualProcessMemFreed. This object needs
                to be supported only when the value of 
                cpmVirtualProcessMemFreed exceeds 32-bit, 
                otherwise this object value would be set to 0.
                ''',
                'cpmvirtualprocessmemfreedovrflw',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessName', ATTRIBUTE, 'str' , None, None, 
                [(1, 32)], [], 
                '''                This object indicates the name of a virtual process.
                If the name is longer than 32 characters, it will be
                truncated to the first 31 characters, and a `*' will be
                appended as the last character to imply this is a
                truncated process name.
                ''',
                'cpmvirtualprocessname',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessRuntime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The amount of CPU time a virtual process has used in
                microseconds.
                ''',
                'cpmvirtualprocessruntime',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessUtil1Min', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                This indicates an estimated CPU utilization by
                a virtual process over the last one minute.
                ''',
                'cpmvirtualprocessutil1min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessUtil5Min', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                This indicates an estimated CPU utilization by
                a virtual process over the last 5 minutes.
                ''',
                'cpmvirtualprocessutil5min',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessUtil5Sec', ATTRIBUTE, 'int' , None, None, 
                [(0, 100)], [], 
                '''                This indicates an estimated CPU utilization by
                a virtual process over the last 5 seconds.
                ''',
                'cpmvirtualprocessutil5sec',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmVirtualProcessEntry',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB.CpmVirtualProcessTable' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB.CpmVirtualProcessTable',
            False, 
            [
            _MetaInfoClassMember('cpmVirtualProcessEntry', REFERENCE_LIST, 'CpmVirtualProcessEntry' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry', 
                [], [], 
                '''                An entry containing the general statistics of a
                virtual process in a virtual machine.
                ''',
                'cpmvirtualprocessentry',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'cpmVirtualProcessTable',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
    'CISCOPROCESSMIB' : {
        'meta_info' : _MetaInfoClass('CISCOPROCESSMIB',
            False, 
            [
            _MetaInfoClassMember('cpmCPUHistory', REFERENCE_CLASS, 'CpmCPUHistory' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUHistory', 
                [], [], 
                '''                ''',
                'cpmcpuhistory',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUHistoryTable', REFERENCE_CLASS, 'CpmCPUHistoryTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUHistoryTable', 
                [], [], 
                '''                A list of CPU utilization history entries.
                ''',
                'cpmcpuhistorytable',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUProcessHistoryTable', REFERENCE_CLASS, 'CpmCPUProcessHistoryTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUProcessHistoryTable', 
                [], [], 
                '''                A list of process history entries. This table contains
                CPU utilization of processes which crossed the 
                cpmCPUHistoryThreshold.
                ''',
                'cpmcpuprocesshistorytable',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUThresholdTable', REFERENCE_CLASS, 'CpmCPUThresholdTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUThresholdTable', 
                [], [], 
                '''                This table contains the information about the
                thresholding values for CPU , configured by the user.
                ''',
                'cpmcputhresholdtable',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmCPUTotalTable', REFERENCE_CLASS, 'CpmCPUTotalTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmCPUTotalTable', 
                [], [], 
                '''                A table of overall CPU statistics.
                ''',
                'cpmcputotaltable',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessExtRevTable', REFERENCE_CLASS, 'CpmProcessExtRevTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessExtRevTable', 
                [], [], 
                '''                This table contains information that may or may
                not be available on all cisco devices. It contains
                additional objects for the more general
                cpmProcessTable. This object deprecates 
                cpmProcessExtTable.
                ''',
                'cpmprocessextrevtable',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmProcessTable', REFERENCE_CLASS, 'CpmProcessTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmProcessTable', 
                [], [], 
                '''                A table of generic information on all active
                processes on this device.
                ''',
                'cpmprocesstable',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmThreadTable', REFERENCE_CLASS, 'CpmThreadTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmThreadTable', 
                [], [], 
                '''                This table contains generic information about
                POSIX threads in the device.
                ''',
                'cpmthreadtable',
                'CISCO-PROCESS-MIB', False),
            _MetaInfoClassMember('cpmVirtualProcessTable', REFERENCE_CLASS, 'CpmVirtualProcessTable' , 'ydk.models.process.CISCO_PROCESS_MIB', 'CISCOPROCESSMIB.CpmVirtualProcessTable', 
                [], [], 
                '''                This table contains information about virtual
                processes in a virtual machine.
                ''',
                'cpmvirtualprocesstable',
                'CISCO-PROCESS-MIB', False),
            ],
            'CISCO-PROCESS-MIB',
            'CISCO-PROCESS-MIB',
            _yang_ns._namespaces['CISCO-PROCESS-MIB'],
        'ydk.models.process.CISCO_PROCESS_MIB'
        ),
    },
}
_meta_table['CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmCPUHistoryTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmCPUProcessHistoryTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmCPUThresholdTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmCPUTotalTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmProcessTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmThreadTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry']['meta_info'].parent =_meta_table['CISCOPROCESSMIB.CpmVirtualProcessTable']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUHistory']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUHistoryTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUProcessHistoryTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUThresholdTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmCPUTotalTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmProcessTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmThreadTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
_meta_table['CISCOPROCESSMIB.CpmVirtualProcessTable']['meta_info'].parent =_meta_table['CISCOPROCESSMIB']['meta_info']
