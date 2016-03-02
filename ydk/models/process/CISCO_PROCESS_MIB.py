""" CISCO_PROCESS_MIB 

The MIB module to describe active system processes.
Virtual Machine refers to those OS which can run the 
code or process of a different executional model OS.
Virtual Process assume the executional model 
of a OS which is different from Native OS. Virtual
Processes are also referred as Tasks.
Thread is a sequence of instructions to be executed
within a program. Thread which adhere to POSIX standard
is referred as a POSIX thread.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class CISCOPROCESSMIB(object):
    """
    
    
    .. attribute:: cpmcpuhistory
    
    	
    	**type**\: :py:class:`CpmCPUHistory <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUHistory>`
    
    .. attribute:: cpmcpuhistorytable
    
    	A list of CPU utilization history entries
    	**type**\: :py:class:`CpmCPUHistoryTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUHistoryTable>`
    
    .. attribute:: cpmcpuprocesshistorytable
    
    	A list of process history entries. This table contains CPU utilization of processes which crossed the  cpmCPUHistoryThreshold
    	**type**\: :py:class:`CpmCPUProcessHistoryTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUProcessHistoryTable>`
    
    .. attribute:: cpmcputhresholdtable
    
    	This table contains the information about the thresholding values for CPU , configured by the user
    	**type**\: :py:class:`CpmCPUThresholdTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUThresholdTable>`
    
    .. attribute:: cpmcputotaltable
    
    	A table of overall CPU statistics
    	**type**\: :py:class:`CpmCPUTotalTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable>`
    
    .. attribute:: cpmprocessextrevtable
    
    	This table contains information that may or may not be available on all cisco devices. It contains additional objects for the more general cpmProcessTable. This object deprecates  cpmProcessExtTable
    	**type**\: :py:class:`CpmProcessExtRevTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable>`
    
    .. attribute:: cpmprocesstable
    
    	A table of generic information on all active processes on this device
    	**type**\: :py:class:`CpmProcessTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable>`
    
    .. attribute:: cpmthreadtable
    
    	This table contains generic information about POSIX threads in the device
    	**type**\: :py:class:`CpmThreadTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmThreadTable>`
    
    .. attribute:: cpmvirtualprocesstable
    
    	This table contains information about virtual processes in a virtual machine
    	**type**\: :py:class:`CpmVirtualProcessTable <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmVirtualProcessTable>`
    
    

    """

    _prefix = 'cisco-process'
    _revision = '2010-05-06'

    def __init__(self):
        self.cpmcpuhistory = CISCOPROCESSMIB.CpmCPUHistory()
        self.cpmcpuhistory.parent = self
        self.cpmcpuhistorytable = CISCOPROCESSMIB.CpmCPUHistoryTable()
        self.cpmcpuhistorytable.parent = self
        self.cpmcpuprocesshistorytable = CISCOPROCESSMIB.CpmCPUProcessHistoryTable()
        self.cpmcpuprocesshistorytable.parent = self
        self.cpmcputhresholdtable = CISCOPROCESSMIB.CpmCPUThresholdTable()
        self.cpmcputhresholdtable.parent = self
        self.cpmcputotaltable = CISCOPROCESSMIB.CpmCPUTotalTable()
        self.cpmcputotaltable.parent = self
        self.cpmprocessextrevtable = CISCOPROCESSMIB.CpmProcessExtRevTable()
        self.cpmprocessextrevtable.parent = self
        self.cpmprocesstable = CISCOPROCESSMIB.CpmProcessTable()
        self.cpmprocesstable.parent = self
        self.cpmthreadtable = CISCOPROCESSMIB.CpmThreadTable()
        self.cpmthreadtable.parent = self
        self.cpmvirtualprocesstable = CISCOPROCESSMIB.CpmVirtualProcessTable()
        self.cpmvirtualprocesstable.parent = self


    class CpmCPUHistory(object):
        """
        
        
        .. attribute:: cpmcpuhistorysize
        
        	A value configured by the user which specifies the number of reports in the history table.  A report contains set of processes which crossed the cpmCPUHistoryThreshold  in the last cpmCPUMonInterval along with  the time at which this report is created, total and interrupt CPU utilizations.  When this object is changed the new value will have effect in the next interval
        	**type**\: int
        
        	**range:** 1..4294967295
        
        .. attribute:: cpmcpuhistorythreshold
        
        	The user  configured value of this object gives the minimum percent CPU utilization of a process in the last cpmCPUMonInterval duration required to be a  member of history table. When this object is changed the new value will have effect in the next interval
        	**type**\: int
        
        	**range:** 1..100
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmcpuhistorysize = None
            self.cpmcpuhistorythreshold = None

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUHistory'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmcpuhistorysize is not None:
                return True

            if self.cpmcpuhistorythreshold is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmCPUHistory']['meta_info']


    class CpmCPUHistoryTable(object):
        """
        A list of CPU utilization history entries.
        
        .. attribute:: cpmcpuhistoryentry
        
        	A historical sample of CPU utilization statistics. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this history is collected.  When the cpmCPUHistorySize is reached the least recent entry is lost
        	**type**\: list of :py:class:`CpmCPUHistoryEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmcpuhistoryentry = YList()
            self.cpmcpuhistoryentry.parent = self
            self.cpmcpuhistoryentry.name = 'cpmcpuhistoryentry'


        class CpmCPUHistoryEntry(object):
            """
            A historical sample of CPU utilization statistics.
            cpmCPUTotalIndex identifies the CPU (or group of CPUs)
            for which this history is collected. 
            When the cpmCPUHistorySize is
            reached the least recent entry is lost.
            
            .. attribute:: cpmcpuhistoryreportid
            
            	All the entries which are created at the same time will have same value for this object. When the configured threshold for being a part of History table is reached then the qualified processes become the part of history table. The entries which became the  part of history table at one instant will have the same value for this object. When this object reaches the max index value then it will wrap around
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcputotalindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmcpuhistorycreatedtime
            
            	Time stamp with respect to sysUpTime indicating the time at which this report is created
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuhistoryinterruptutil
            
            	Percentage of CPU utilization in the interrupt context at cpmCPUHistoryCreated
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmcpuhistoryreportsize
            
            	The number of process entries in a report. This object gives information about how many processes  became a part of history table at one instant
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuhistorytotalutil
            
            	Total percentage of CPU utilization at cpmCPUHistoryCreated
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcpuhistoryreportid = None
                self.cpmcputotalindex = None
                self.cpmcpuhistorycreatedtime = None
                self.cpmcpuhistoryinterruptutil = None
                self.cpmcpuhistoryreportsize = None
                self.cpmcpuhistorytotalutil = None

            @property
            def _common_path(self):
                if self.cpmcpuhistoryreportid is None:
                    raise YPYDataValidationError('Key property cpmcpuhistoryreportid is None')
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUHistoryTable/CISCO-PROCESS-MIB:cpmCPUHistoryEntry[CISCO-PROCESS-MIB:cpmCPUHistoryReportId = ' + str(self.cpmcpuhistoryreportid) + '][CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcpuhistoryreportid is not None:
                    return True

                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmcpuhistorycreatedtime is not None:
                    return True

                if self.cpmcpuhistoryinterruptutil is not None:
                    return True

                if self.cpmcpuhistoryreportsize is not None:
                    return True

                if self.cpmcpuhistorytotalutil is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmCPUHistoryTable.CpmCPUHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmcpuhistoryentry is not None:
                for child_ref in self.cpmcpuhistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmCPUHistoryTable']['meta_info']


    class CpmCPUProcessHistoryTable(object):
        """
        A list of process history entries. This table contains
        CPU utilization of processes which crossed the 
        cpmCPUHistoryThreshold.
        
        .. attribute:: cpmcpuprocesshistoryentry
        
        	A historical sample of process utilization statistics. The entries in this table will have corresponding entires in the cpmCPUHistoryTable. The entries in this table get deleted when the entry associated with this entry in the cpmCPUHistoryTable  gets deleted
        	**type**\: list of :py:class:`CpmCPUProcessHistoryEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmcpuprocesshistoryentry = YList()
            self.cpmcpuprocesshistoryentry.parent = self
            self.cpmcpuprocesshistoryentry.name = 'cpmcpuprocesshistoryentry'


        class CpmCPUProcessHistoryEntry(object):
            """
            A historical sample of process utilization
            statistics. The entries in this table will have
            corresponding entires in the cpmCPUHistoryTable.
            The entries in this table get deleted when the entry
            associated with this entry in the cpmCPUHistoryTable 
            gets deleted.
            
            .. attribute:: cpmcpuhistoryreportid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuprocesshistoryindex
            
            	An index that uniquely identifies an entry in the cmpCPUProcessHistory table among those in the  same report. This index is between 1 to N,  where N is the cpmCPUHistoryReportSize
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmcputotalindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmcpuhistoryproccreated
            
            	The time when the process was created. The process ID and the time when the process was created, uniquely  identifies a process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuhistoryprocid
            
            	The process Id associated with this entry
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: cpmcpuhistoryprocname
            
            	The process name associated with this entry
            	**type**\: str
            
            	**pattern:** \\p{IsBasicLatin}{0,255}
            
            .. attribute:: cpmcpuhistoryprocutil
            
            	The percentage CPU utilization of a process at cpmCPUHistoryCreatedTime
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcpuhistoryreportid = None
                self.cpmcpuprocesshistoryindex = None
                self.cpmcputotalindex = None
                self.cpmcpuhistoryproccreated = None
                self.cpmcpuhistoryprocid = None
                self.cpmcpuhistoryprocname = None
                self.cpmcpuhistoryprocutil = None

            @property
            def _common_path(self):
                if self.cpmcpuhistoryreportid is None:
                    raise YPYDataValidationError('Key property cpmcpuhistoryreportid is None')
                if self.cpmcpuprocesshistoryindex is None:
                    raise YPYDataValidationError('Key property cpmcpuprocesshistoryindex is None')
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUProcessHistoryTable/CISCO-PROCESS-MIB:cpmCPUProcessHistoryEntry[CISCO-PROCESS-MIB:cpmCPUHistoryReportId = ' + str(self.cpmcpuhistoryreportid) + '][CISCO-PROCESS-MIB:cpmCPUProcessHistoryIndex = ' + str(self.cpmcpuprocesshistoryindex) + '][CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcpuhistoryreportid is not None:
                    return True

                if self.cpmcpuprocesshistoryindex is not None:
                    return True

                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmcpuhistoryproccreated is not None:
                    return True

                if self.cpmcpuhistoryprocid is not None:
                    return True

                if self.cpmcpuhistoryprocname is not None:
                    return True

                if self.cpmcpuhistoryprocutil is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmCPUProcessHistoryTable.CpmCPUProcessHistoryEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUProcessHistoryTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmcpuprocesshistoryentry is not None:
                for child_ref in self.cpmcpuprocesshistoryentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmCPUProcessHistoryTable']['meta_info']


    class CpmCPUThresholdTable(object):
        """
        This table contains the information about the
        thresholding values for CPU , configured by the user.
        
        .. attribute:: cpmcputhresholdentry
        
        	An entry containing information about CPU thresholding parameters. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this configuration applies
        	**type**\: list of :py:class:`CpmCPUThresholdEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmcputhresholdentry = YList()
            self.cpmcputhresholdentry.parent = self
            self.cpmcputhresholdentry.name = 'cpmcputhresholdentry'


        class CpmCPUThresholdEntry(object):
            """
            An entry containing information about
            CPU thresholding parameters. cpmCPUTotalIndex
            identifies the CPU (or group of CPUs) for which this
            configuration applies.
            
            .. attribute:: cpmcputhresholdclass
            
            	Value of this object indicates the type of utilization, which is monitored. The total(1) indicates the total CPU utilization, interrupt(2) indicates the the CPU utilization in interrupt context and process(3) indicates the CPU utilization in the process level execution context
            	**type**\: :py:class:`CpmCPUThresholdClass_Enum <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry.CpmCPUThresholdClass_Enum>`
            
            .. attribute:: cpmcputotalindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmcpufallingthresholdperiod
            
            	This is an observation interval. The value of this object indicates that CPU utilization should be below cpmCPUFallingThresholdValue for this duration to send a  cpmCPURisingThreshold notification to the NMS
            	**type**\: int
            
            	**range:** 5..4294967295
            
            .. attribute:: cpmcpufallingthresholdvalue
            
            	The percentage falling threshold value configured by the user. The value indicates, if the percentage  CPU utilization is equal to or below this value for  cpmCPUFallingThresholdPeriod duration then send a cpmCPUFallingThreshold notification  to the NMS
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cpmcpurisingthresholdperiod
            
            	This is an observation interval. The value of this object indicates that  the CPU utilization should be above cpmCPURisingThresholdValue for this duration to send a  cpmCPURisingThreshold notification to the NMS
            	**type**\: int
            
            	**range:** 5..4294967295
            
            .. attribute:: cpmcpurisingthresholdvalue
            
            	The percentage rising threshold value configured by the user. The value indicates,  if the percentage CPU utilization is equal to or above this value for cpmCPURisingThresholdPeriod duration  then send a cpmCPURisingThreshold notification to the NMS
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cpmcputhresholdentrystatus
            
            	The status of this table entry
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcputhresholdclass = None
                self.cpmcputotalindex = None
                self.cpmcpufallingthresholdperiod = None
                self.cpmcpufallingthresholdvalue = None
                self.cpmcpurisingthresholdperiod = None
                self.cpmcpurisingthresholdvalue = None
                self.cpmcputhresholdentrystatus = None

            class CpmCPUThresholdClass_Enum(Enum):
                """
                CpmCPUThresholdClass_Enum

                Value of this object indicates the type of
                utilization, which is monitored. The total(1) indicates
                the total CPU utilization, interrupt(2) indicates the
                the CPU utilization in interrupt context and process(3)
                indicates the CPU utilization in the process level
                execution context.

                """

                TOTAL = 1

                INTERRUPT = 2

                PROCESS = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                    return meta._meta_table['CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry.CpmCPUThresholdClass_Enum']


            @property
            def _common_path(self):
                if self.cpmcputhresholdclass is None:
                    raise YPYDataValidationError('Key property cpmcputhresholdclass is None')
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUThresholdTable/CISCO-PROCESS-MIB:cpmCPUThresholdEntry[CISCO-PROCESS-MIB:cpmCPUThresholdClass = ' + str(self.cpmcputhresholdclass) + '][CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcputhresholdclass is not None:
                    return True

                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmcpufallingthresholdperiod is not None:
                    return True

                if self.cpmcpufallingthresholdvalue is not None:
                    return True

                if self.cpmcpurisingthresholdperiod is not None:
                    return True

                if self.cpmcpurisingthresholdvalue is not None:
                    return True

                if self.cpmcputhresholdentrystatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmCPUThresholdTable.CpmCPUThresholdEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUThresholdTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmcputhresholdentry is not None:
                for child_ref in self.cpmcputhresholdentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmCPUThresholdTable']['meta_info']


    class CpmCPUTotalTable(object):
        """
        A table of overall CPU statistics.
        
        .. attribute:: cpmcputotalentry
        
        	Overall information about the CPU load. Entries in this table come and go as CPUs are added and removed from the system
        	**type**\: list of :py:class:`CpmCPUTotalEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmcputotalentry = YList()
            self.cpmcputotalentry.parent = self
            self.cpmcputotalentry.name = 'cpmcputotalentry'


        class CpmCPUTotalEntry(object):
            """
            Overall information about the CPU load. Entries in this
            table come and go as CPUs are added and removed from the
            system.
            
            .. attribute:: cpmcputotalindex
            
            	An index that uniquely represents a CPU (or group of CPUs) whose CPU load information is reported by a row in this table. This index is assigned arbitrarily by the engine and is not saved over reboots
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmcpuinterruptmonintervalvalue
            
            	The overall CPU busy percentage in the interrupt context in the last cpmCPUMonInterval period
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmcpuloadavg15min
            
            	The overall CPU load Average in the last 15 minutes period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuloadavg1min
            
            	The overall CPU load Average in the last 1 minute period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuloadavg5min
            
            	The overall CPU load Average in the last 5 minutes period
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemorycommitted
            
            	The overall CPU wide system memory which is currently Committed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemorycommittedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryCommitted. This object needs to be supported only when the value of cpmCPUMemoryCommitted exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemoryfree
            
            	The overall CPU wide system memory which is currently free
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemoryfreeovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryFree. This object needs to be supported only when the value of cpmCPUMemoryFree exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemoryhccommitted
            
            	The overall CPU wide system memory which is currently committed. This object is a 64\-bit version of cpmCPUMemoryCommitted
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmcpumemoryhcfree
            
            	The overall CPU wide system memory which is currently free. This object is a 64\-bit version of cpmCPUMemoryFree
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmcpumemoryhckernelreserved
            
            	The overall CPU wide system memory which is reserved for kernel usage. This object is a 64\-bit version of cpmCPUMemoryKernelReserved
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmcpumemoryhclowest
            
            	The lowest free memory that has been recorded since device has booted. This object is a 64\-bit version of cpmCPUMemoryLowest
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmcpumemoryhcused
            
            	The overall CPU wide system memory which is currently under use. This object is a 64\-bit version of cpmCPUMemoryUsed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmcpumemorykernelreserved
            
            	The overall CPU wide system memory which is reserved for kernel usage
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemorykernelreservedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryKernelReserved. This object needs  to be supported only when the value of  cpmCPUMemoryKernelReserved exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemorylowest
            
            	The lowest free memory that has been recorded since device has booted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemorylowestovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryLowest. This object needs to be supported only when the value of cpmCPUMemoryLowest exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemoryused
            
            	The overall CPU wide system memory which is currently under use
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemoryusedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryUsed. This object needs to be supported only when the value of cpmCPUMemoryUsed exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumoninterval
            
            	CPU usage monitoring interval. The value of this object in seconds indicates the how often the  CPU utilization is calculated and monitored
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcputotal1min
            
            	The overall CPU busy percentage in the last 1 minute period. This object obsoletes the avgBusy1 object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal1minRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cpmcputotal1minrev
            
            	The overall CPU busy percentage in the last 1 minute period. This object deprecates the object cpmCPUTotal1min  and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmcputotal5min
            
            	The overall CPU busy percentage in the last 5 minute period. This object deprecates the avgBusy5 object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal5minRev which has the changed range  of value (0..100)
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cpmcputotal5minrev
            
            	The overall CPU busy percentage in the last 5 minute period. This object deprecates the object cpmCPUTotal5min  and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmcputotal5sec
            
            	The overall CPU busy percentage in the last 5 second period. This object obsoletes the busyPer object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal5secRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cpmcputotal5secrev
            
            	The overall CPU busy percentage in the last 5 second period. This object deprecates the object cpmCPUTotal5sec  and increases the value range to (0..100). This object is deprecated by cpmCPUTotalMonIntervalValue
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmcputotalmonintervalvalue
            
            	The overall CPU busy percentage in the last cpmCPUMonInterval period.  This object deprecates the object cpmCPUTotal5secRev
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmcputotalphysicalindex
            
            	The entPhysicalIndex of the physical entity for which the CPU statistics in this entry are maintained. The physical entity can be a CPU chip, a group of CPUs, a CPU card etc. The exact type of this entity is described by its entPhysicalVendorType value. If the CPU statistics in this entry correspond to more than one physical entity (or to no physical entity), or if the entPhysicalTable is not supported on the SNMP agent, the value of this object must be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcputotalindex = None
                self.cpmcpuinterruptmonintervalvalue = None
                self.cpmcpuloadavg15min = None
                self.cpmcpuloadavg1min = None
                self.cpmcpuloadavg5min = None
                self.cpmcpumemorycommitted = None
                self.cpmcpumemorycommittedovrflw = None
                self.cpmcpumemoryfree = None
                self.cpmcpumemoryfreeovrflw = None
                self.cpmcpumemoryhccommitted = None
                self.cpmcpumemoryhcfree = None
                self.cpmcpumemoryhckernelreserved = None
                self.cpmcpumemoryhclowest = None
                self.cpmcpumemoryhcused = None
                self.cpmcpumemorykernelreserved = None
                self.cpmcpumemorykernelreservedovrflw = None
                self.cpmcpumemorylowest = None
                self.cpmcpumemorylowestovrflw = None
                self.cpmcpumemoryused = None
                self.cpmcpumemoryusedovrflw = None
                self.cpmcpumoninterval = None
                self.cpmcputotal1min = None
                self.cpmcputotal1minrev = None
                self.cpmcputotal5min = None
                self.cpmcputotal5minrev = None
                self.cpmcputotal5sec = None
                self.cpmcputotal5secrev = None
                self.cpmcputotalmonintervalvalue = None
                self.cpmcputotalphysicalindex = None

            @property
            def _common_path(self):
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUTotalTable/CISCO-PROCESS-MIB:cpmCPUTotalEntry[CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmcpuinterruptmonintervalvalue is not None:
                    return True

                if self.cpmcpuloadavg15min is not None:
                    return True

                if self.cpmcpuloadavg1min is not None:
                    return True

                if self.cpmcpuloadavg5min is not None:
                    return True

                if self.cpmcpumemorycommitted is not None:
                    return True

                if self.cpmcpumemorycommittedovrflw is not None:
                    return True

                if self.cpmcpumemoryfree is not None:
                    return True

                if self.cpmcpumemoryfreeovrflw is not None:
                    return True

                if self.cpmcpumemoryhccommitted is not None:
                    return True

                if self.cpmcpumemoryhcfree is not None:
                    return True

                if self.cpmcpumemoryhckernelreserved is not None:
                    return True

                if self.cpmcpumemoryhclowest is not None:
                    return True

                if self.cpmcpumemoryhcused is not None:
                    return True

                if self.cpmcpumemorykernelreserved is not None:
                    return True

                if self.cpmcpumemorykernelreservedovrflw is not None:
                    return True

                if self.cpmcpumemorylowest is not None:
                    return True

                if self.cpmcpumemorylowestovrflw is not None:
                    return True

                if self.cpmcpumemoryused is not None:
                    return True

                if self.cpmcpumemoryusedovrflw is not None:
                    return True

                if self.cpmcpumoninterval is not None:
                    return True

                if self.cpmcputotal1min is not None:
                    return True

                if self.cpmcputotal1minrev is not None:
                    return True

                if self.cpmcputotal5min is not None:
                    return True

                if self.cpmcputotal5minrev is not None:
                    return True

                if self.cpmcputotal5sec is not None:
                    return True

                if self.cpmcputotal5secrev is not None:
                    return True

                if self.cpmcputotalmonintervalvalue is not None:
                    return True

                if self.cpmcputotalphysicalindex is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmCPUTotalTable.CpmCPUTotalEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmCPUTotalTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmcputotalentry is not None:
                for child_ref in self.cpmcputotalentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmCPUTotalTable']['meta_info']


    class CpmProcessExtRevTable(object):
        """
        This table contains information that may or may
        not be available on all cisco devices. It contains
        additional objects for the more general
        cpmProcessTable. This object deprecates 
        cpmProcessExtTable.
        
        .. attribute:: cpmprocessextreventry
        
        	An entry containing additional information for a particular process. This object deprecates  cpmProcessExtEntry
        	**type**\: list of :py:class:`CpmProcessExtRevEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmprocessextreventry = YList()
            self.cpmprocessextreventry.parent = self
            self.cpmprocessextreventry.name = 'cpmprocessextreventry'


        class CpmProcessExtRevEntry(object):
            """
            An entry containing additional information for
            a particular process. This object deprecates 
            cpmProcessExtEntry.
            
            .. attribute:: cpmcputotalindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmprocesspid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessdatasegmentsize
            
            	This indicates the data segment of a process and all its shared objects
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessdatasegmentsizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessDataSegmentSize. This object needs to be supported only when the value of  cpmProcessDataSegmentSize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessdynamicmemorysize
            
            	This indicates the amount of dynamic memory being used by the process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessdynamicmemorysizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessDynamicMemorySize. This object needs to be supported only when the value of  cpmProcessDynamicMemorySize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocesshcdatasegmentsize
            
            	This indicates the data segment of a process and all its shared objects.. This object is a 64\-bit version of cpmProcessDataSegmentSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmprocesshcdynamicmemorysize
            
            	This indicates the amount of dynamic memory being used by the process. This object is a 64\-bit version of cpmProcessDynamicMemorySize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmprocesshcstacksize
            
            	This indicates the amount of stack memory used by the process. This object is a 64\-bit version of cpmProcessStackSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmprocesshctextsegmentsize
            
            	This indicates the text memory of a process and all its shared objects. This object is a 64\-bit version of cpmProcessTextSegmentSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmprocesslastrestartuser
            
            	This indicate the user that has last restarted the process or has taken running coredump of the process
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cpmprocessmemorycore
            
            	This indicates the part of process memory to be dumped when a process crashes. The process  memory is used for debugging purposes to trace the  root cause of the crash. sparse        \- Some operating systems support minimal                 dump of process core like register                 info, partial stack, partial memory                 pages especially for critical process                 to facilitate faster process restart
            	**type**\: :py:class:`CpmProcessMemoryCore_Enum <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessMemoryCore_Enum>`
            
            .. attribute:: cpmprocessrespawn
            
            	This indicates whether respawn of a process is enabled or not. If enabled the process in context repawns after it has crashed/stopped
            	**type**\: bool
            
            .. attribute:: cpmprocessrespawnafterlastpatch
            
            	This indicates the number of times a process has restarted after the last patch is applied. This is to  determine the stability of the last patch
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessrespawncount
            
            	This indicates the number of times the process has respawned/restarted
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessstacksize
            
            	This indicates the amount of stack memory used by the process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessstacksizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessStackSize. This object needs to be supported only when the value of cpmProcessStackSize exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocesstextsegmentsize
            
            	This indicates the text memory of a process and all its shared objects
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocesstextsegmentsizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessTextSegmentSize. This object needs to be supported only when the value of  cpmProcessTextSegmentSize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocesstype
            
            	This indicates the kind of process in context
            	**type**\: :py:class:`CpmProcessType_Enum <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessType_Enum>`
            
            .. attribute:: cpmprocexthcmemallocatedrev
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. This object is a 64\-bit version of cpmProcExtMemAllocatedRev
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmprocexthcmemfreedrev
            
            	The sum of all memory that this process has returned to the system. This object is a 64\-bit version of cpmProcExtMemFreedRev
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmprocextinvokedrev
            
            	The number of times since cpmTimeCreated that the process has been invoked. This object  deprecates cpmProcExtInvoked
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextmemallocatedrev
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. The sum of freed memory is provided by cpmProcExtMemFreedRev. This object deprecates cpmProcExtMemAllocated
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextmemallocatedrevovrflw
            
            	This object represents the upper 32\-bit of cpmProcExtMemAllocatedRev. This object needs to be supported only when the value of  cpmProcExtMemAllocatedRev exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextmemfreedrev
            
            	The sum of all memory that this process has returned to the system. This object  deprecates  cpmProcExtMemFreed
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextmemfreedrevovrflw
            
            	This object represents the upper 32\-bit of cpmProcExtMemFreedRev. This object needs to  be supported only when the value of cpmProcExtMemFreedRev exceeds 32\-bit,otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextpriorityrev
            
            	The priority level at  which the process is running. This object deprecates  cpmProcExtPriority
            	**type**\: :py:class:`CpmProcExtPriorityRev_Enum <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcExtPriorityRev_Enum>`
            
            .. attribute:: cpmprocextruntimerev
            
            	The amount of CPU time the process has used, in microseconds. This object deprecates cpmProcExtRuntime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextutil1minrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 1  minute period. It is determined as a weighted  decaying average of the current idle time over the  longest idle time. Note that this information  should be used as an estimate only. This object  deprecates cpmProcExtUtil1Min and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmprocextutil5minrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  minute period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object deprecates cpmProcExtUtil5Min and increases the value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmprocextutil5secrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  second period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object deprecates cpmProcExtUtil5Sec and increases the  value range to (0..100)
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmprocessdatasegmentsize = None
                self.cpmprocessdatasegmentsizeovrflw = None
                self.cpmprocessdynamicmemorysize = None
                self.cpmprocessdynamicmemorysizeovrflw = None
                self.cpmprocesshcdatasegmentsize = None
                self.cpmprocesshcdynamicmemorysize = None
                self.cpmprocesshcstacksize = None
                self.cpmprocesshctextsegmentsize = None
                self.cpmprocesslastrestartuser = None
                self.cpmprocessmemorycore = None
                self.cpmprocessrespawn = None
                self.cpmprocessrespawnafterlastpatch = None
                self.cpmprocessrespawncount = None
                self.cpmprocessstacksize = None
                self.cpmprocessstacksizeovrflw = None
                self.cpmprocesstextsegmentsize = None
                self.cpmprocesstextsegmentsizeovrflw = None
                self.cpmprocesstype = None
                self.cpmprocexthcmemallocatedrev = None
                self.cpmprocexthcmemfreedrev = None
                self.cpmprocextinvokedrev = None
                self.cpmprocextmemallocatedrev = None
                self.cpmprocextmemallocatedrevovrflw = None
                self.cpmprocextmemfreedrev = None
                self.cpmprocextmemfreedrevovrflw = None
                self.cpmprocextpriorityrev = None
                self.cpmprocextruntimerev = None
                self.cpmprocextutil1minrev = None
                self.cpmprocextutil5minrev = None
                self.cpmprocextutil5secrev = None

            class CpmProcExtPriorityRev_Enum(Enum):
                """
                CpmProcExtPriorityRev_Enum

                The priority level at  which the process is
                running. This object deprecates 
                cpmProcExtPriority.

                """

                CRITICAL = 1

                HIGH = 2

                NORMAL = 3

                LOW = 4

                NOTASSIGNED = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                    return meta._meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcExtPriorityRev_Enum']


            class CpmProcessMemoryCore_Enum(Enum):
                """
                CpmProcessMemoryCore_Enum

                This indicates the part of process memory to be
                dumped when a process crashes. The process 
                memory is used for debugging purposes to trace the 
                root cause of the crash.
                sparse        \- Some operating systems support minimal
                                dump of process core like register
                                info, partial stack, partial memory
                                pages especially for critical process
                                to facilitate faster process restart.

                """

                OTHER = 1

                MAINMEM = 2

                MAINMEMSHAREDMEM = 3

                MAINMEMTEXT = 4

                MAINMEMTEXTSHAREDMEM = 5

                SHAREDMEM = 6

                SPARSE = 7

                OFF = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                    return meta._meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessMemoryCore_Enum']


            class CpmProcessType_Enum(Enum):
                """
                CpmProcessType_Enum

                This indicates the kind of process in context.

                """

                OTHER = 1

                POSIX = 2

                IOS = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                    return meta._meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry.CpmProcessType_Enum']


            @property
            def _common_path(self):
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')
                if self.cpmprocesspid is None:
                    raise YPYDataValidationError('Key property cpmprocesspid is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmProcessExtRevTable/CISCO-PROCESS-MIB:cpmProcessExtRevEntry[CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + '][CISCO-PROCESS-MIB:cpmProcessPID = ' + str(self.cpmprocesspid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmprocesspid is not None:
                    return True

                if self.cpmprocessdatasegmentsize is not None:
                    return True

                if self.cpmprocessdatasegmentsizeovrflw is not None:
                    return True

                if self.cpmprocessdynamicmemorysize is not None:
                    return True

                if self.cpmprocessdynamicmemorysizeovrflw is not None:
                    return True

                if self.cpmprocesshcdatasegmentsize is not None:
                    return True

                if self.cpmprocesshcdynamicmemorysize is not None:
                    return True

                if self.cpmprocesshcstacksize is not None:
                    return True

                if self.cpmprocesshctextsegmentsize is not None:
                    return True

                if self.cpmprocesslastrestartuser is not None:
                    return True

                if self.cpmprocessmemorycore is not None:
                    return True

                if self.cpmprocessrespawn is not None:
                    return True

                if self.cpmprocessrespawnafterlastpatch is not None:
                    return True

                if self.cpmprocessrespawncount is not None:
                    return True

                if self.cpmprocessstacksize is not None:
                    return True

                if self.cpmprocessstacksizeovrflw is not None:
                    return True

                if self.cpmprocesstextsegmentsize is not None:
                    return True

                if self.cpmprocesstextsegmentsizeovrflw is not None:
                    return True

                if self.cpmprocesstype is not None:
                    return True

                if self.cpmprocexthcmemallocatedrev is not None:
                    return True

                if self.cpmprocexthcmemfreedrev is not None:
                    return True

                if self.cpmprocextinvokedrev is not None:
                    return True

                if self.cpmprocextmemallocatedrev is not None:
                    return True

                if self.cpmprocextmemallocatedrevovrflw is not None:
                    return True

                if self.cpmprocextmemfreedrev is not None:
                    return True

                if self.cpmprocextmemfreedrevovrflw is not None:
                    return True

                if self.cpmprocextpriorityrev is not None:
                    return True

                if self.cpmprocextruntimerev is not None:
                    return True

                if self.cpmprocextutil1minrev is not None:
                    return True

                if self.cpmprocextutil5minrev is not None:
                    return True

                if self.cpmprocextutil5secrev is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable.CpmProcessExtRevEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmProcessExtRevTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmprocessextreventry is not None:
                for child_ref in self.cpmprocessextreventry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmProcessExtRevTable']['meta_info']


    class CpmProcessTable(object):
        """
        A table of generic information on all active
        processes on this device.
        
        .. attribute:: cpmprocessentry
        
        	Generic information about an active process on this device. Entries in this table come and go as processes are  created and destroyed by the device
        	**type**\: list of :py:class:`CpmProcessEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmprocessentry = YList()
            self.cpmprocessentry.parent = self
            self.cpmprocessentry.name = 'cpmprocessentry'


        class CpmProcessEntry(object):
            """
            Generic information about an active process on this
            device. Entries in this table come and go as processes are 
            created and destroyed by the device.
            
            .. attribute:: cpmcputotalindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmprocesspid
            
            	This object contains the process ID. cpmTimeCreated should be checked against the last time it was polled, and if it has changed the PID has been reused and the entire entry should be polled again
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessaverageusecs
            
            	Average elapsed CPU time in microseconds when the process was active. This object deprecates the object cpmProcessuSecs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessname
            
            	The name associated with this process. If the name is longer than 32 characters, it will be truncated to the first 31 characters, and a `\*' will be appended as the last character to imply this is a truncated process name
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: cpmprocesstimecreated
            
            	The time when the process was created. The process ID and the time when the process was created, uniquely  identifies a process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessusecs
            
            	Average elapsed CPU time in microseconds when the process was active. This object is deprecated by cpmProcessAverageUSecs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextinvoked
            
            	The number of times since cpmTimeCreated that the process has been invoked. This object is deprecated by cpmProcExtInvokedRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextmemallocated
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. The sum of freed memory is provided by cpmProcExtMemFreed. This object is deprecated by cpmProcExtMemAllocatedRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextmemfreed
            
            	The sum of all memory that this process has returned to the system. This object is deprecated by  cpmProcExtMemFreedRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextpriority
            
            	The priority level at which the process is running. This object is deprecated by cpmProcExtPriorityRev
            	**type**\: :py:class:`CpmProcExtPriority_Enum <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry.CpmProcExtPriority_Enum>`
            
            .. attribute:: cpmprocextruntime
            
            	The amount of CPU time the process has used, in microseconds. This object is deprecated by cpmProcExtRuntimeRev
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextutil1min
            
            	This object provides a general idea of how busy a process caused the processor to be over a 1  minute period. It is determined as a weighted  decaying average of the current idle time over the  longest idle time. Note that this information  should be used as an estimate only. This object is  deprecated by cpmProcExtUtil1MinRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cpmprocextutil5min
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  minute period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object is deprecated by cpmProcExtUtil5MinRev which has the changed range of value (0..100)
            	**type**\: int
            
            	**range:** 1..100
            
            .. attribute:: cpmprocextutil5sec
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  second period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object is  deprecated by cpmProcExtUtil5SecRev which has the  changed range of value (0..100)
            	**type**\: int
            
            	**range:** 1..100
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmprocessaverageusecs = None
                self.cpmprocessname = None
                self.cpmprocesstimecreated = None
                self.cpmprocessusecs = None
                self.cpmprocextinvoked = None
                self.cpmprocextmemallocated = None
                self.cpmprocextmemfreed = None
                self.cpmprocextpriority = None
                self.cpmprocextruntime = None
                self.cpmprocextutil1min = None
                self.cpmprocextutil5min = None
                self.cpmprocextutil5sec = None

            class CpmProcExtPriority_Enum(Enum):
                """
                CpmProcExtPriority_Enum

                The priority level at which the process is
                running. This object is deprecated by
                cpmProcExtPriorityRev.

                """

                CRITICAL = 1

                HIGH = 2

                NORMAL = 3

                LOW = 4

                NOTASSIGNED = 5


                @staticmethod
                def _meta_info():
                    from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                    return meta._meta_table['CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry.CpmProcExtPriority_Enum']


            @property
            def _common_path(self):
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')
                if self.cpmprocesspid is None:
                    raise YPYDataValidationError('Key property cpmprocesspid is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmProcessTable/CISCO-PROCESS-MIB:cpmProcessEntry[CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + '][CISCO-PROCESS-MIB:cpmProcessPID = ' + str(self.cpmprocesspid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmprocesspid is not None:
                    return True

                if self.cpmprocessaverageusecs is not None:
                    return True

                if self.cpmprocessname is not None:
                    return True

                if self.cpmprocesstimecreated is not None:
                    return True

                if self.cpmprocessusecs is not None:
                    return True

                if self.cpmprocextinvoked is not None:
                    return True

                if self.cpmprocextmemallocated is not None:
                    return True

                if self.cpmprocextmemfreed is not None:
                    return True

                if self.cpmprocextpriority is not None:
                    return True

                if self.cpmprocextruntime is not None:
                    return True

                if self.cpmprocextutil1min is not None:
                    return True

                if self.cpmprocextutil5min is not None:
                    return True

                if self.cpmprocextutil5sec is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmProcessTable.CpmProcessEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmProcessTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmprocessentry is not None:
                for child_ref in self.cpmprocessentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmProcessTable']['meta_info']


    class CpmThreadTable(object):
        """
        This table contains generic information about
        POSIX threads in the device.
        
        .. attribute:: cpmthreadentry
        
        	An entry containing the general statistics of a POSIX thread
        	**type**\: list of :py:class:`CpmThreadEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmthreadentry = YList()
            self.cpmthreadentry.parent = self
            self.cpmthreadentry.name = 'cpmthreadentry'


        class CpmThreadEntry(object):
            """
            An entry containing the general statistics
            of a POSIX thread.
            
            .. attribute:: cpmcputotalindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmprocesspid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmthreadid
            
            	This object contains the thread ID. ThreadID is Unique per process
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmthreadblockingprocess
            
            	This object identifies the process on which the current thread is blocked on. This points to the  cpmProcessTable of the process on which the thread  in context is blocked. This is valid only to threads which are either in send/reply states. For the  rest of the threads it is returned as 0.0
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cpmthreadcpuutilization
            
            	This object provides a general idea on how busy the thread in context caused the processor to be
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmthreadhcstacksize
            
            	This object indicates the stack size allocated to the thread in context. This object is a 64\-bit version of cpmThreadStackSize
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmthreadname
            
            	This object represents the name of the thread. Thread names need not be unique. Hence statistics  should be analyzed against thread ID
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: cpmthreadpriority
            
            	This object indicates the priority of a POSIX thread. The higher the number, the higher the priority of the  thread over other threads
            	**type**\: int
            
            	**range:** 0..63
            
            .. attribute:: cpmthreadstacksize
            
            	This object indicates the stack size allocated to the thread in context
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmthreadstacksizeovrflw
            
            	This object represents the upper 32\-bit of cpmThreadStackSize. This object needs to be supported only when the value of cpmThreadStackSize exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmthreadstate
            
            	This object indicates the current state of a thread. Running state means that the thread is actively  consumig CPU. All the other states are just waiting  states. The valid states are\: other         \- Any other state apart from the listed                  ones. dead          \- Kernel is waiting to release the                  thread's resources. running       \- Actively running on a CPU. ready         \- Not running on a CPU, but is ready to                  run (one or more higher or equal                  priority threads are running). stopped       \- Suspended (SIGSTOP signal). send          \- Waiting for a server to receive                  a message. receive       \- Waiting for a client to send a message. reply         \- Waiting for a server to reply to a                  message. stack         \- Waiting for more stack to be allocated. waitpage      \- Waiting for process manager to                  resolve a fault on a page. sigsuspend    \- Suspended for a signal. sigwaitinfo   \- Waiting for a signal. nanosleep     \- Sleeping for a period of time. mutex         \- Waiting to acquire a mutex condvar       \- Waiting for a condition variable to be                  signalled. join          \- Waiting for the completion of another                  thread. intr          \- Waiting for an interrupt. sem           \- Waiting to acquire a semaphore
            	**type**\: :py:class:`CpmThreadState_Enum <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry.CpmThreadState_Enum>`
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmthreadid = None
                self.cpmthreadblockingprocess = None
                self.cpmthreadcpuutilization = None
                self.cpmthreadhcstacksize = None
                self.cpmthreadname = None
                self.cpmthreadpriority = None
                self.cpmthreadstacksize = None
                self.cpmthreadstacksizeovrflw = None
                self.cpmthreadstate = None

            class CpmThreadState_Enum(Enum):
                """
                CpmThreadState_Enum

                This object indicates the current state of a thread.
                Running state means that the thread is actively 
                consumig CPU. All the other states are just waiting 
                states. The valid states are\:
                other         \- Any other state apart from the listed 
                                ones.
                dead          \- Kernel is waiting to release the 
                                thread's resources.
                running       \- Actively running on a CPU.
                ready         \- Not running on a CPU, but is ready to 
                                run (one or more higher or equal 
                                priority threads are running).
                stopped       \- Suspended (SIGSTOP signal).
                send          \- Waiting for a server to receive 
                                a message.
                receive       \- Waiting for a client to send a message.
                reply         \- Waiting for a server to reply to a 
                                message.
                stack         \- Waiting for more stack to be allocated.
                waitpage      \- Waiting for process manager to 
                                resolve a fault on a page.
                sigsuspend    \- Suspended for a signal.
                sigwaitinfo   \- Waiting for a signal.
                nanosleep     \- Sleeping for a period of time.
                mutex         \- Waiting to acquire a mutex
                condvar       \- Waiting for a condition variable to be 
                                signalled.
                join          \- Waiting for the completion of another 
                                thread.
                intr          \- Waiting for an interrupt.
                sem           \- Waiting to acquire a semaphore.

                """

                OTHER = 1

                DEAD = 2

                RUNNING = 3

                READY = 4

                STOPPED = 5

                SEND = 6

                RECEIVE = 7

                REPLY = 8

                STACK = 9

                WAITPAGE = 10

                SIGSUSPEND = 11

                SIGWAITINFO = 12

                NANOSLEEP = 13

                MUTEX = 14

                CONDVAR = 15

                JOIN = 16

                INTR = 17

                SEM = 18


                @staticmethod
                def _meta_info():
                    from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                    return meta._meta_table['CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry.CpmThreadState_Enum']


            @property
            def _common_path(self):
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')
                if self.cpmprocesspid is None:
                    raise YPYDataValidationError('Key property cpmprocesspid is None')
                if self.cpmthreadid is None:
                    raise YPYDataValidationError('Key property cpmthreadid is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmThreadTable/CISCO-PROCESS-MIB:cpmThreadEntry[CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + '][CISCO-PROCESS-MIB:cpmProcessPID = ' + str(self.cpmprocesspid) + '][CISCO-PROCESS-MIB:cpmThreadID = ' + str(self.cpmthreadid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmprocesspid is not None:
                    return True

                if self.cpmthreadid is not None:
                    return True

                if self.cpmthreadblockingprocess is not None:
                    return True

                if self.cpmthreadcpuutilization is not None:
                    return True

                if self.cpmthreadhcstacksize is not None:
                    return True

                if self.cpmthreadname is not None:
                    return True

                if self.cpmthreadpriority is not None:
                    return True

                if self.cpmthreadstacksize is not None:
                    return True

                if self.cpmthreadstacksizeovrflw is not None:
                    return True

                if self.cpmthreadstate is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmThreadTable.CpmThreadEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmThreadTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmthreadentry is not None:
                for child_ref in self.cpmthreadentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmThreadTable']['meta_info']


    class CpmVirtualProcessTable(object):
        """
        This table contains information about virtual
        processes in a virtual machine.
        
        .. attribute:: cpmvirtualprocessentry
        
        	An entry containing the general statistics of a virtual process in a virtual machine
        	**type**\: list of :py:class:`CpmVirtualProcessEntry <ydk.models.process.CISCO_PROCESS_MIB.CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry>`
        
        

        """

        _prefix = 'cisco-process'
        _revision = '2010-05-06'

        def __init__(self):
            self.parent = None
            self.cpmvirtualprocessentry = YList()
            self.cpmvirtualprocessentry.parent = self
            self.cpmvirtualprocessentry.name = 'cpmvirtualprocessentry'


        class CpmVirtualProcessEntry(object):
            """
            An entry containing the general statistics of a
            virtual process in a virtual machine.
            
            .. attribute:: cpmcputotalindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmprocesspid
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessid
            
            	This object indicates the process ID of a virtual process. PID is unique only inside one address space. Virtual process PID should be considered along with  Parent process cpmProcessPID
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocesshcmemallocated
            
            	This object indicates the memory allocated by the virtual process inside the address space of a process running on Native OS. This object is a 64\-bit version of cpmVirtualProcessMemAllocated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmvirtualprocesshcmemfreed
            
            	This object indicates the memory freed by the virtual process inside the address space of a process running on Native OS.This object is a 64\-bit version of cpmVirtualProcessMemAllocated
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmvirtualprocessinvokecount
            
            	The number of times a virtual process is invoked
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessmemallocated
            
            	This object indicates the memory allocated by the virtual process inside the address space of a  process running on Native OS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessmemallocatedovrflw
            
            	This object represents the upper 32\-bit of cpmVirtualProcessMemAllocated. This object  needs to be supported only when the value of cpmVirtualProcessMemAllocated exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessmemfreed
            
            	This object indicates the memory freed by the virtual process inside the address space of a process running  on Native OS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessmemfreedovrflw
            
            	This object represents the upper 32\-bit of cpmVirtualProcessMemFreed. This object needs to be supported only when the value of  cpmVirtualProcessMemFreed exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessname
            
            	This object indicates the name of a virtual process. If the name is longer than 32 characters, it will be truncated to the first 31 characters, and a `\*' will be appended as the last character to imply this is a truncated process name
            	**type**\: str
            
            	**range:** 1..32
            
            .. attribute:: cpmvirtualprocessruntime
            
            	The amount of CPU time a virtual process has used in microseconds
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessutil1min
            
            	This indicates an estimated CPU utilization by a virtual process over the last one minute
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmvirtualprocessutil5min
            
            	This indicates an estimated CPU utilization by a virtual process over the last 5 minutes
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: cpmvirtualprocessutil5sec
            
            	This indicates an estimated CPU utilization by a virtual process over the last 5 seconds
            	**type**\: int
            
            	**range:** 0..100
            
            

            """

            _prefix = 'cisco-process'
            _revision = '2010-05-06'

            def __init__(self):
                self.parent = None
                self.cpmcputotalindex = None
                self.cpmprocesspid = None
                self.cpmvirtualprocessid = None
                self.cpmvirtualprocesshcmemallocated = None
                self.cpmvirtualprocesshcmemfreed = None
                self.cpmvirtualprocessinvokecount = None
                self.cpmvirtualprocessmemallocated = None
                self.cpmvirtualprocessmemallocatedovrflw = None
                self.cpmvirtualprocessmemfreed = None
                self.cpmvirtualprocessmemfreedovrflw = None
                self.cpmvirtualprocessname = None
                self.cpmvirtualprocessruntime = None
                self.cpmvirtualprocessutil1min = None
                self.cpmvirtualprocessutil5min = None
                self.cpmvirtualprocessutil5sec = None

            @property
            def _common_path(self):
                if self.cpmcputotalindex is None:
                    raise YPYDataValidationError('Key property cpmcputotalindex is None')
                if self.cpmprocesspid is None:
                    raise YPYDataValidationError('Key property cpmprocesspid is None')
                if self.cpmvirtualprocessid is None:
                    raise YPYDataValidationError('Key property cpmvirtualprocessid is None')

                return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmVirtualProcessTable/CISCO-PROCESS-MIB:cpmVirtualProcessEntry[CISCO-PROCESS-MIB:cpmCPUTotalIndex = ' + str(self.cpmcputotalindex) + '][CISCO-PROCESS-MIB:cpmProcessPID = ' + str(self.cpmprocesspid) + '][CISCO-PROCESS-MIB:cpmVirtualProcessID = ' + str(self.cpmvirtualprocessid) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.cpmcputotalindex is not None:
                    return True

                if self.cpmprocesspid is not None:
                    return True

                if self.cpmvirtualprocessid is not None:
                    return True

                if self.cpmvirtualprocesshcmemallocated is not None:
                    return True

                if self.cpmvirtualprocesshcmemfreed is not None:
                    return True

                if self.cpmvirtualprocessinvokecount is not None:
                    return True

                if self.cpmvirtualprocessmemallocated is not None:
                    return True

                if self.cpmvirtualprocessmemallocatedovrflw is not None:
                    return True

                if self.cpmvirtualprocessmemfreed is not None:
                    return True

                if self.cpmvirtualprocessmemfreedovrflw is not None:
                    return True

                if self.cpmvirtualprocessname is not None:
                    return True

                if self.cpmvirtualprocessruntime is not None:
                    return True

                if self.cpmvirtualprocessutil1min is not None:
                    return True

                if self.cpmvirtualprocessutil5min is not None:
                    return True

                if self.cpmvirtualprocessutil5sec is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
                return meta._meta_table['CISCOPROCESSMIB.CpmVirtualProcessTable.CpmVirtualProcessEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/CISCO-PROCESS-MIB:cpmVirtualProcessTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.cpmvirtualprocessentry is not None:
                for child_ref in self.cpmvirtualprocessentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
            return meta._meta_table['CISCOPROCESSMIB.CpmVirtualProcessTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-PROCESS-MIB:CISCO-PROCESS-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.cpmcpuhistory is not None and self.cpmcpuhistory._has_data():
            return True

        if self.cpmcpuhistory is not None and self.cpmcpuhistory.is_presence():
            return True

        if self.cpmcpuhistorytable is not None and self.cpmcpuhistorytable._has_data():
            return True

        if self.cpmcpuhistorytable is not None and self.cpmcpuhistorytable.is_presence():
            return True

        if self.cpmcpuprocesshistorytable is not None and self.cpmcpuprocesshistorytable._has_data():
            return True

        if self.cpmcpuprocesshistorytable is not None and self.cpmcpuprocesshistorytable.is_presence():
            return True

        if self.cpmcputhresholdtable is not None and self.cpmcputhresholdtable._has_data():
            return True

        if self.cpmcputhresholdtable is not None and self.cpmcputhresholdtable.is_presence():
            return True

        if self.cpmcputotaltable is not None and self.cpmcputotaltable._has_data():
            return True

        if self.cpmcputotaltable is not None and self.cpmcputotaltable.is_presence():
            return True

        if self.cpmprocessextrevtable is not None and self.cpmprocessextrevtable._has_data():
            return True

        if self.cpmprocessextrevtable is not None and self.cpmprocessextrevtable.is_presence():
            return True

        if self.cpmprocesstable is not None and self.cpmprocesstable._has_data():
            return True

        if self.cpmprocesstable is not None and self.cpmprocesstable.is_presence():
            return True

        if self.cpmthreadtable is not None and self.cpmthreadtable._has_data():
            return True

        if self.cpmthreadtable is not None and self.cpmthreadtable.is_presence():
            return True

        if self.cpmvirtualprocesstable is not None and self.cpmvirtualprocesstable._has_data():
            return True

        if self.cpmvirtualprocesstable is not None and self.cpmvirtualprocesstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.process._meta import _CISCO_PROCESS_MIB as meta
        return meta._meta_table['CISCOPROCESSMIB']['meta_info']


