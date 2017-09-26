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
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CISCOPROCESSMIB(Entity):
    """
    
    
    .. attribute:: cpmcoretable
    
    	A table of per\-Core statistics
    	**type**\:   :py:class:`Cpmcoretable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcoretable>`
    
    .. attribute:: cpmcpuhistory
    
    	
    	**type**\:   :py:class:`Cpmcpuhistory <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcpuhistory>`
    
    .. attribute:: cpmcpuhistorytable
    
    	A list of CPU utilization history entries
    	**type**\:   :py:class:`Cpmcpuhistorytable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcpuhistorytable>`
    
    .. attribute:: cpmcpuprocesshistorytable
    
    	A list of process history entries. This table contains CPU utilization of processes which crossed the  cpmCPUHistoryThreshold
    	**type**\:   :py:class:`Cpmcpuprocesshistorytable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcpuprocesshistorytable>`
    
    .. attribute:: cpmcputhresholdtable
    
    	This table contains the information about the thresholding values for CPU , configured by the user
    	**type**\:   :py:class:`Cpmcputhresholdtable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputhresholdtable>`
    
    .. attribute:: cpmcputotaltable
    
    	A table of overall CPU statistics
    	**type**\:   :py:class:`Cpmcputotaltable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable>`
    
    .. attribute:: cpmprocessextrevtable
    
    	This table contains information that may or may not be available on all cisco devices. It contains additional objects for the more general cpmProcessTable. This object deprecates  cpmProcessExtTable
    	**type**\:   :py:class:`Cpmprocessextrevtable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocessextrevtable>`
    
    .. attribute:: cpmprocesstable
    
    	A table of generic information on all active processes on this device
    	**type**\:   :py:class:`Cpmprocesstable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocesstable>`
    
    .. attribute:: cpmthreadtable
    
    	This table contains generic information about POSIX threads in the device
    	**type**\:   :py:class:`Cpmthreadtable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmthreadtable>`
    
    .. attribute:: cpmvirtualprocesstable
    
    	This table contains information about virtual processes in a virtual machine
    	**type**\:   :py:class:`Cpmvirtualprocesstable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmvirtualprocesstable>`
    
    

    """

    _prefix = 'CISCO-PROCESS-MIB'
    _revision = '2011-06-23'

    def __init__(self):
        super(CISCOPROCESSMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PROCESS-MIB"
        self.yang_parent_name = "CISCO-PROCESS-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self._child_container_classes = {"cpmCoreTable" : ("cpmcoretable", CISCOPROCESSMIB.Cpmcoretable), "cpmCPUHistory" : ("cpmcpuhistory", CISCOPROCESSMIB.Cpmcpuhistory), "cpmCPUHistoryTable" : ("cpmcpuhistorytable", CISCOPROCESSMIB.Cpmcpuhistorytable), "cpmCPUProcessHistoryTable" : ("cpmcpuprocesshistorytable", CISCOPROCESSMIB.Cpmcpuprocesshistorytable), "cpmCPUThresholdTable" : ("cpmcputhresholdtable", CISCOPROCESSMIB.Cpmcputhresholdtable), "cpmCPUTotalTable" : ("cpmcputotaltable", CISCOPROCESSMIB.Cpmcputotaltable), "cpmProcessExtRevTable" : ("cpmprocessextrevtable", CISCOPROCESSMIB.Cpmprocessextrevtable), "cpmProcessTable" : ("cpmprocesstable", CISCOPROCESSMIB.Cpmprocesstable), "cpmThreadTable" : ("cpmthreadtable", CISCOPROCESSMIB.Cpmthreadtable), "cpmVirtualProcessTable" : ("cpmvirtualprocesstable", CISCOPROCESSMIB.Cpmvirtualprocesstable)}
        self._child_list_classes = {}

        self.cpmcoretable = CISCOPROCESSMIB.Cpmcoretable()
        self.cpmcoretable.parent = self
        self._children_name_map["cpmcoretable"] = "cpmCoreTable"
        self._children_yang_names.add("cpmCoreTable")

        self.cpmcpuhistory = CISCOPROCESSMIB.Cpmcpuhistory()
        self.cpmcpuhistory.parent = self
        self._children_name_map["cpmcpuhistory"] = "cpmCPUHistory"
        self._children_yang_names.add("cpmCPUHistory")

        self.cpmcpuhistorytable = CISCOPROCESSMIB.Cpmcpuhistorytable()
        self.cpmcpuhistorytable.parent = self
        self._children_name_map["cpmcpuhistorytable"] = "cpmCPUHistoryTable"
        self._children_yang_names.add("cpmCPUHistoryTable")

        self.cpmcpuprocesshistorytable = CISCOPROCESSMIB.Cpmcpuprocesshistorytable()
        self.cpmcpuprocesshistorytable.parent = self
        self._children_name_map["cpmcpuprocesshistorytable"] = "cpmCPUProcessHistoryTable"
        self._children_yang_names.add("cpmCPUProcessHistoryTable")

        self.cpmcputhresholdtable = CISCOPROCESSMIB.Cpmcputhresholdtable()
        self.cpmcputhresholdtable.parent = self
        self._children_name_map["cpmcputhresholdtable"] = "cpmCPUThresholdTable"
        self._children_yang_names.add("cpmCPUThresholdTable")

        self.cpmcputotaltable = CISCOPROCESSMIB.Cpmcputotaltable()
        self.cpmcputotaltable.parent = self
        self._children_name_map["cpmcputotaltable"] = "cpmCPUTotalTable"
        self._children_yang_names.add("cpmCPUTotalTable")

        self.cpmprocessextrevtable = CISCOPROCESSMIB.Cpmprocessextrevtable()
        self.cpmprocessextrevtable.parent = self
        self._children_name_map["cpmprocessextrevtable"] = "cpmProcessExtRevTable"
        self._children_yang_names.add("cpmProcessExtRevTable")

        self.cpmprocesstable = CISCOPROCESSMIB.Cpmprocesstable()
        self.cpmprocesstable.parent = self
        self._children_name_map["cpmprocesstable"] = "cpmProcessTable"
        self._children_yang_names.add("cpmProcessTable")

        self.cpmthreadtable = CISCOPROCESSMIB.Cpmthreadtable()
        self.cpmthreadtable.parent = self
        self._children_name_map["cpmthreadtable"] = "cpmThreadTable"
        self._children_yang_names.add("cpmThreadTable")

        self.cpmvirtualprocesstable = CISCOPROCESSMIB.Cpmvirtualprocesstable()
        self.cpmvirtualprocesstable.parent = self
        self._children_name_map["cpmvirtualprocesstable"] = "cpmVirtualProcessTable"
        self._children_yang_names.add("cpmVirtualProcessTable")
        self._segment_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB"


    class Cpmcoretable(Entity):
        """
        A table of per\-Core statistics.
        
        .. attribute:: cpmcoreentry
        
        	Overall information about the Core load. Entries in this table could come and go as Cores go online or offline
        	**type**\: list of    :py:class:`Cpmcoreentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcoretable.Cpmcoreentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmcoretable, self).__init__()

            self.yang_name = "cpmCoreTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmCoreEntry" : ("cpmcoreentry", CISCOPROCESSMIB.Cpmcoretable.Cpmcoreentry)}

            self.cpmcoreentry = YList(self)
            self._segment_path = lambda: "cpmCoreTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmcoretable, [], name, value)


        class Cpmcoreentry(Entity):
            """
            Overall information about the Core load. Entries in this
            table could come and go as Cores go online or offline.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmcoreindex  <key>
            
            	An index that uniquely represents a Core (or group of Cores) whose Core load information is reported by a row in this table. This index is assigned arbitrarily by the engine and is not saved over reboots
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcore1min
            
            	The overall Core busy percentage in the last 1 minute period
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: cpmcore5min
            
            	The overall Core busy percentage in the last 5 minute period
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: cpmcore5sec
            
            	The overall Core busy percentage in the last 5 second period
            	**type**\:  int
            
            	**range:** 0..100
            
            .. attribute:: cpmcoreloadavg15min
            
            	The overall Core load Average in the last 15 minutes period
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcoreloadavg1min
            
            	The overall Core load Average in the last 1 minute period
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcoreloadavg5min
            
            	The overall Core load Average in the last 5 minutes period
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcorephysicalindex
            
            	The entCorePhysicalIndex of the physical entity for which the Core statistics in this entry are maintained. The physical entity can be a CPU chip, a group of CPUs, a CPU card etc. The exact type of this entity is described by its entPhysicalVendorType value. If the Core statistics in this entry correspond to more than one physical entity (or to no physical entity), or if the entPhysicalTable is not supported on the SNMP agent, the value of this object must be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmcoretable.Cpmcoreentry, self).__init__()

                self.yang_name = "cpmCoreEntry"
                self.yang_parent_name = "cpmCoreTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcoreindex = YLeaf(YType.uint32, "cpmCoreIndex")

                self.cpmcore1min = YLeaf(YType.uint32, "cpmCore1min")

                self.cpmcore5min = YLeaf(YType.uint32, "cpmCore5min")

                self.cpmcore5sec = YLeaf(YType.uint32, "cpmCore5sec")

                self.cpmcoreloadavg15min = YLeaf(YType.uint32, "cpmCoreLoadAvg15min")

                self.cpmcoreloadavg1min = YLeaf(YType.uint32, "cpmCoreLoadAvg1min")

                self.cpmcoreloadavg5min = YLeaf(YType.uint32, "cpmCoreLoadAvg5min")

                self.cpmcorephysicalindex = YLeaf(YType.int32, "cpmCorePhysicalIndex")
                self._segment_path = lambda: "cpmCoreEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCoreIndex='" + self.cpmcoreindex.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCoreTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmcoretable.Cpmcoreentry, ['cpmcputotalindex', 'cpmcoreindex', 'cpmcore1min', 'cpmcore5min', 'cpmcore5sec', 'cpmcoreloadavg15min', 'cpmcoreloadavg1min', 'cpmcoreloadavg5min', 'cpmcorephysicalindex'], name, value)


    class Cpmcpuhistory(Entity):
        """
        
        
        .. attribute:: cpmcpuhistorysize
        
        	A value configured by the user which specifies the number of reports in the history table.  A report contains set of processes which crossed the cpmCPUHistoryThreshold  in the last cpmCPUMonInterval along with  the time at which this report is created, total and interrupt CPU utilizations.  When this object is changed the new value will have effect in the next interval
        	**type**\:  int
        
        	**range:** 1..4294967295
        
        .. attribute:: cpmcpuhistorythreshold
        
        	The user  configured value of this object gives the minimum percent CPU utilization of a process in the last cpmCPUMonInterval duration required to be a  member of history table. When this object is changed the new value will have effect in the next interval
        	**type**\:  int
        
        	**range:** 1..100
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmcpuhistory, self).__init__()

            self.yang_name = "cpmCPUHistory"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {}

            self.cpmcpuhistorysize = YLeaf(YType.uint32, "cpmCPUHistorySize")

            self.cpmcpuhistorythreshold = YLeaf(YType.uint32, "cpmCPUHistoryThreshold")
            self._segment_path = lambda: "cpmCPUHistory"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmcpuhistory, ['cpmcpuhistorysize', 'cpmcpuhistorythreshold'], name, value)


    class Cpmcpuhistorytable(Entity):
        """
        A list of CPU utilization history entries.
        
        .. attribute:: cpmcpuhistoryentry
        
        	A historical sample of CPU utilization statistics. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this history is collected.  When the cpmCPUHistorySize is reached the least recent entry is lost
        	**type**\: list of    :py:class:`Cpmcpuhistoryentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcpuhistorytable.Cpmcpuhistoryentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmcpuhistorytable, self).__init__()

            self.yang_name = "cpmCPUHistoryTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmCPUHistoryEntry" : ("cpmcpuhistoryentry", CISCOPROCESSMIB.Cpmcpuhistorytable.Cpmcpuhistoryentry)}

            self.cpmcpuhistoryentry = YList(self)
            self._segment_path = lambda: "cpmCPUHistoryTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmcpuhistorytable, [], name, value)


        class Cpmcpuhistoryentry(Entity):
            """
            A historical sample of CPU utilization statistics.
            cpmCPUTotalIndex identifies the CPU (or group of CPUs)
            for which this history is collected. 
            When the cpmCPUHistorySize is
            reached the least recent entry is lost.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmcpuhistoryreportid  <key>
            
            	All the entries which are created at the same time will have same value for this object. When the configured threshold for being a part of History table is reached then the qualified processes become the part of history table. The entries which became the  part of history table at one instant will have the same value for this object. When this object reaches the max index value then it will wrap around
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuhistorycreatedtime
            
            	Time stamp with respect to sysUpTime indicating the time at which this report is created
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuhistoryinterruptutil
            
            	Percentage of CPU utilization in the interrupt context at cpmCPUHistoryCreated
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmcpuhistoryreportsize
            
            	The number of process entries in a report. This object gives information about how many processes  became a part of history table at one instant
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuhistorytotalutil
            
            	Total percentage of CPU utilization at cpmCPUHistoryCreated
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmcpuhistorytable.Cpmcpuhistoryentry, self).__init__()

                self.yang_name = "cpmCPUHistoryEntry"
                self.yang_parent_name = "cpmCPUHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcpuhistoryreportid = YLeaf(YType.uint32, "cpmCPUHistoryReportId")

                self.cpmcpuhistorycreatedtime = YLeaf(YType.uint32, "cpmCPUHistoryCreatedTime")

                self.cpmcpuhistoryinterruptutil = YLeaf(YType.uint32, "cpmCPUHistoryInterruptUtil")

                self.cpmcpuhistoryreportsize = YLeaf(YType.uint32, "cpmCPUHistoryReportSize")

                self.cpmcpuhistorytotalutil = YLeaf(YType.uint32, "cpmCPUHistoryTotalUtil")
                self._segment_path = lambda: "cpmCPUHistoryEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCPUHistoryReportId='" + self.cpmcpuhistoryreportid.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmcpuhistorytable.Cpmcpuhistoryentry, ['cpmcputotalindex', 'cpmcpuhistoryreportid', 'cpmcpuhistorycreatedtime', 'cpmcpuhistoryinterruptutil', 'cpmcpuhistoryreportsize', 'cpmcpuhistorytotalutil'], name, value)


    class Cpmcpuprocesshistorytable(Entity):
        """
        A list of process history entries. This table contains
        CPU utilization of processes which crossed the 
        cpmCPUHistoryThreshold.
        
        .. attribute:: cpmcpuprocesshistoryentry
        
        	A historical sample of process utilization statistics. The entries in this table will have corresponding entires in the cpmCPUHistoryTable. The entries in this table get deleted when the entry associated with this entry in the cpmCPUHistoryTable  gets deleted
        	**type**\: list of    :py:class:`Cpmcpuprocesshistoryentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmcpuprocesshistorytable, self).__init__()

            self.yang_name = "cpmCPUProcessHistoryTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmCPUProcessHistoryEntry" : ("cpmcpuprocesshistoryentry", CISCOPROCESSMIB.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry)}

            self.cpmcpuprocesshistoryentry = YList(self)
            self._segment_path = lambda: "cpmCPUProcessHistoryTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmcpuprocesshistorytable, [], name, value)


        class Cpmcpuprocesshistoryentry(Entity):
            """
            A historical sample of process utilization
            statistics. The entries in this table will have
            corresponding entires in the cpmCPUHistoryTable.
            The entries in this table get deleted when the entry
            associated with this entry in the cpmCPUHistoryTable 
            gets deleted.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmcpuhistoryreportid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmcpuhistoryreportid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcpuhistorytable.Cpmcpuhistoryentry>`
            
            .. attribute:: cpmcpuprocesshistoryindex  <key>
            
            	An index that uniquely identifies an entry in the cmpCPUProcessHistory table among those in the  same report. This index is between 1 to N,  where N is the cpmCPUHistoryReportSize
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmcpuhistoryproccreated
            
            	The time when the process was created. The process ID and the time when the process was created, uniquely  identifies a process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpuhistoryprocid
            
            	The process Id associated with this entry
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cpmcpuhistoryprocname
            
            	The process name associated with this entry
            	**type**\:  str
            
            .. attribute:: cpmcpuhistoryprocutil
            
            	The percentage CPU utilization of a process at cpmCPUHistoryCreatedTime
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry, self).__init__()

                self.yang_name = "cpmCPUProcessHistoryEntry"
                self.yang_parent_name = "cpmCPUProcessHistoryTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcpuhistoryreportid = YLeaf(YType.str, "cpmCPUHistoryReportId")

                self.cpmcpuprocesshistoryindex = YLeaf(YType.uint32, "cpmCPUProcessHistoryIndex")

                self.cpmcpuhistoryproccreated = YLeaf(YType.uint32, "cpmCPUHistoryProcCreated")

                self.cpmcpuhistoryprocid = YLeaf(YType.uint32, "cpmCPUHistoryProcId")

                self.cpmcpuhistoryprocname = YLeaf(YType.str, "cpmCPUHistoryProcName")

                self.cpmcpuhistoryprocutil = YLeaf(YType.uint32, "cpmCPUHistoryProcUtil")
                self._segment_path = lambda: "cpmCPUProcessHistoryEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCPUHistoryReportId='" + self.cpmcpuhistoryreportid.get() + "']" + "[cpmCPUProcessHistoryIndex='" + self.cpmcpuprocesshistoryindex.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUProcessHistoryTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry, ['cpmcputotalindex', 'cpmcpuhistoryreportid', 'cpmcpuprocesshistoryindex', 'cpmcpuhistoryproccreated', 'cpmcpuhistoryprocid', 'cpmcpuhistoryprocname', 'cpmcpuhistoryprocutil'], name, value)


    class Cpmcputhresholdtable(Entity):
        """
        This table contains the information about the
        thresholding values for CPU , configured by the user.
        
        .. attribute:: cpmcputhresholdentry
        
        	An entry containing information about CPU thresholding parameters. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this configuration applies
        	**type**\: list of    :py:class:`Cpmcputhresholdentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputhresholdtable.Cpmcputhresholdentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmcputhresholdtable, self).__init__()

            self.yang_name = "cpmCPUThresholdTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmCPUThresholdEntry" : ("cpmcputhresholdentry", CISCOPROCESSMIB.Cpmcputhresholdtable.Cpmcputhresholdentry)}

            self.cpmcputhresholdentry = YList(self)
            self._segment_path = lambda: "cpmCPUThresholdTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmcputhresholdtable, [], name, value)


        class Cpmcputhresholdentry(Entity):
            """
            An entry containing information about
            CPU thresholding parameters. cpmCPUTotalIndex
            identifies the CPU (or group of CPUs) for which this
            configuration applies.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmcputhresholdclass  <key>
            
            	Value of this object indicates the type of utilization, which is monitored. The total(1) indicates the total CPU utilization, interrupt(2) indicates the the CPU utilization in interrupt context and process(3) indicates the CPU utilization in the process level execution context
            	**type**\:   :py:class:`Cpmcputhresholdclass <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputhresholdtable.Cpmcputhresholdentry.Cpmcputhresholdclass>`
            
            .. attribute:: cpmcpufallingthresholdperiod
            
            	This is an observation interval. The value of this object indicates that CPU utilization should be below cpmCPUFallingThresholdValue for this duration to send a  cpmCPURisingThreshold notification to the NMS
            	**type**\:  int
            
            	**range:** 5..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpmcpufallingthresholdvalue
            
            	The percentage falling threshold value configured by the user. The value indicates, if the percentage  CPU utilization is equal to or below this value for  cpmCPUFallingThresholdPeriod duration then send a cpmCPUFallingThreshold notification  to the NMS
            	**type**\:  int
            
            	**range:** 1..100
            
            .. attribute:: cpmcpurisingthresholdperiod
            
            	This is an observation interval. The value of this object indicates that  the CPU utilization should be above cpmCPURisingThresholdValue for this duration to send a  cpmCPURisingThreshold notification to the NMS
            	**type**\:  int
            
            	**range:** 5..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpmcpurisingthresholdvalue
            
            	The percentage rising threshold value configured by the user. The value indicates,  if the percentage CPU utilization is equal to or above this value for cpmCPURisingThresholdPeriod duration  then send a cpmCPURisingThreshold notification to the NMS
            	**type**\:  int
            
            	**range:** 1..100
            
            .. attribute:: cpmcputhresholdentrystatus
            
            	The status of this table entry
            	**type**\:   :py:class:`RowStatus <ydk.models.cisco_ios_xe.SNMPv2_TC.RowStatus>`
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmcputhresholdtable.Cpmcputhresholdentry, self).__init__()

                self.yang_name = "cpmCPUThresholdEntry"
                self.yang_parent_name = "cpmCPUThresholdTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcputhresholdclass = YLeaf(YType.enumeration, "cpmCPUThresholdClass")

                self.cpmcpufallingthresholdperiod = YLeaf(YType.uint32, "cpmCPUFallingThresholdPeriod")

                self.cpmcpufallingthresholdvalue = YLeaf(YType.uint32, "cpmCPUFallingThresholdValue")

                self.cpmcpurisingthresholdperiod = YLeaf(YType.uint32, "cpmCPURisingThresholdPeriod")

                self.cpmcpurisingthresholdvalue = YLeaf(YType.uint32, "cpmCPURisingThresholdValue")

                self.cpmcputhresholdentrystatus = YLeaf(YType.enumeration, "cpmCPUThresholdEntryStatus")
                self._segment_path = lambda: "cpmCPUThresholdEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCPUThresholdClass='" + self.cpmcputhresholdclass.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUThresholdTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmcputhresholdtable.Cpmcputhresholdentry, ['cpmcputotalindex', 'cpmcputhresholdclass', 'cpmcpufallingthresholdperiod', 'cpmcpufallingthresholdvalue', 'cpmcpurisingthresholdperiod', 'cpmcpurisingthresholdvalue', 'cpmcputhresholdentrystatus'], name, value)

            class Cpmcputhresholdclass(Enum):
                """
                Cpmcputhresholdclass

                Value of this object indicates the type of

                utilization, which is monitored. The total(1) indicates

                the total CPU utilization, interrupt(2) indicates the

                the CPU utilization in interrupt context and process(3)

                indicates the CPU utilization in the process level

                execution context.

                .. data:: total = 1

                .. data:: interrupt = 2

                .. data:: process = 3

                """

                total = Enum.YLeaf(1, "total")

                interrupt = Enum.YLeaf(2, "interrupt")

                process = Enum.YLeaf(3, "process")



    class Cpmcputotaltable(Entity):
        """
        A table of overall CPU statistics.
        
        .. attribute:: cpmcputotalentry
        
        	Overall information about the CPU load. Entries in this table come and go as CPUs are added and removed from the system
        	**type**\: list of    :py:class:`Cpmcputotalentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmcputotaltable, self).__init__()

            self.yang_name = "cpmCPUTotalTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmCPUTotalEntry" : ("cpmcputotalentry", CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry)}

            self.cpmcputotalentry = YList(self)
            self._segment_path = lambda: "cpmCPUTotalTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmcputotaltable, [], name, value)


        class Cpmcputotalentry(Entity):
            """
            Overall information about the CPU load. Entries in this
            table come and go as CPUs are added and removed from the
            system.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	An index that uniquely represents a CPU (or group of CPUs) whose CPU load information is reported by a row in this table. This index is assigned arbitrarily by the engine and is not saved over reboots
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            .. attribute:: cpmcpuinterruptmonintervalvalue
            
            	The overall CPU busy percentage in the interrupt context in the last cpmCPUMonInterval period
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmcpuloadavg15min
            
            	The overall CPU load Average in the last 15 minutes period
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcpuloadavg1min
            
            	The overall CPU load Average in the last 1 minute period
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcpuloadavg5min
            
            	The overall CPU load Average in the last 5 minutes period
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: hundredths of processes
            
            .. attribute:: cpmcpumemorycommitted
            
            	The overall CPU wide system memory which is currently Committed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemorycommittedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryCommitted. This object needs to be supported only when the value of cpmCPUMemoryCommitted exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmcpumemoryfree
            
            	The overall CPU wide system memory which is currently free
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryfreeovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryFree. This object needs to be supported only when the value of cpmCPUMemoryFree exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhccommitted
            
            	The overall CPU wide system memory which is currently committed. This object is a 64\-bit version of cpmCPUMemoryCommitted
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            .. attribute:: cpmcpumemoryhcfree
            
            	The overall CPU wide system memory which is currently free. This object is a 64\-bit version of cpmCPUMemoryFree
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhckernelreserved
            
            	The overall CPU wide system memory which is reserved for kernel usage. This object is a 64\-bit version of cpmCPUMemoryKernelReserved
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhclowest
            
            	The lowest free memory that has been recorded since device has booted. This object is a 64\-bit version of cpmCPUMemoryLowest
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryhcused
            
            	The overall CPU wide system memory which is currently under use. This object is a 64\-bit version of cpmCPUMemoryUsed
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemorykernelreserved
            
            	The overall CPU wide system memory which is reserved for kernel usage
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemorykernelreservedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryKernelReserved. This object needs  to be supported only when the value of  cpmCPUMemoryKernelReserved exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemorylowest
            
            	The lowest free memory that has been recorded since device has booted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmcpumemorylowestovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryLowest. This object needs to be supported only when the value of cpmCPUMemoryLowest exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryused
            
            	The overall CPU wide system memory which is currently under use
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumemoryusedovrflw
            
            	This object represents the upper 32\-bit of cpmCPUMemoryUsed. This object needs to be supported only when the value of cpmCPUMemoryUsed exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmcpumoninterval
            
            	CPU usage monitoring interval. The value of this object in seconds indicates the how often the  CPU utilization is calculated and monitored
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: seconds
            
            .. attribute:: cpmcputotal1min
            
            	The overall CPU busy percentage in the last 1 minute period. This object obsoletes the avgBusy1 object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal1minRev which has the changed range of value (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotal1minrev
            
            	The overall CPU busy percentage in the last 1 minute period. This object deprecates the object cpmCPUTotal1min  and increases the value range to (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmcputotal5min
            
            	The overall CPU busy percentage in the last 5 minute period. This object deprecates the avgBusy5 object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal5minRev which has the changed range  of value (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotal5minrev
            
            	The overall CPU busy percentage in the last 5 minute period. This object deprecates the object cpmCPUTotal5min  and increases the value range to (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmcputotal5sec
            
            	The overall CPU busy percentage in the last 5 second period. This object obsoletes the busyPer object from  the OLD\-CISCO\-SYSTEM\-MIB. This object is deprecated by cpmCPUTotal5secRev which has the changed range of value (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotal5secrev
            
            	The overall CPU busy percentage in the last 5 second period. This object deprecates the object cpmCPUTotal5sec  and increases the value range to (0..100). This object is deprecated by cpmCPUTotalMonIntervalValue
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            	**status**\: deprecated
            
            .. attribute:: cpmcputotalmonintervalvalue
            
            	The overall CPU busy percentage in the last cpmCPUMonInterval period.  This object deprecates the object cpmCPUTotal5secRev
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmcputotalphysicalindex
            
            	The entPhysicalIndex of the physical entity for which the CPU statistics in this entry are maintained. The physical entity can be a CPU chip, a group of CPUs, a CPU card etc. The exact type of this entity is described by its entPhysicalVendorType value. If the CPU statistics in this entry correspond to more than one physical entity (or to no physical entity), or if the entPhysicalTable is not supported on the SNMP agent, the value of this object must be zero
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry, self).__init__()

                self.yang_name = "cpmCPUTotalEntry"
                self.yang_parent_name = "cpmCPUTotalTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.uint32, "cpmCPUTotalIndex")

                self.cpmcpuinterruptmonintervalvalue = YLeaf(YType.uint32, "cpmCPUInterruptMonIntervalValue")

                self.cpmcpuloadavg15min = YLeaf(YType.uint32, "cpmCPULoadAvg15min")

                self.cpmcpuloadavg1min = YLeaf(YType.uint32, "cpmCPULoadAvg1min")

                self.cpmcpuloadavg5min = YLeaf(YType.uint32, "cpmCPULoadAvg5min")

                self.cpmcpumemorycommitted = YLeaf(YType.uint32, "cpmCPUMemoryCommitted")

                self.cpmcpumemorycommittedovrflw = YLeaf(YType.uint32, "cpmCPUMemoryCommittedOvrflw")

                self.cpmcpumemoryfree = YLeaf(YType.uint32, "cpmCPUMemoryFree")

                self.cpmcpumemoryfreeovrflw = YLeaf(YType.uint32, "cpmCPUMemoryFreeOvrflw")

                self.cpmcpumemoryhccommitted = YLeaf(YType.uint64, "cpmCPUMemoryHCCommitted")

                self.cpmcpumemoryhcfree = YLeaf(YType.uint64, "cpmCPUMemoryHCFree")

                self.cpmcpumemoryhckernelreserved = YLeaf(YType.uint64, "cpmCPUMemoryHCKernelReserved")

                self.cpmcpumemoryhclowest = YLeaf(YType.uint64, "cpmCPUMemoryHCLowest")

                self.cpmcpumemoryhcused = YLeaf(YType.uint64, "cpmCPUMemoryHCUsed")

                self.cpmcpumemorykernelreserved = YLeaf(YType.uint32, "cpmCPUMemoryKernelReserved")

                self.cpmcpumemorykernelreservedovrflw = YLeaf(YType.uint32, "cpmCPUMemoryKernelReservedOvrflw")

                self.cpmcpumemorylowest = YLeaf(YType.uint32, "cpmCPUMemoryLowest")

                self.cpmcpumemorylowestovrflw = YLeaf(YType.uint32, "cpmCPUMemoryLowestOvrflw")

                self.cpmcpumemoryused = YLeaf(YType.uint32, "cpmCPUMemoryUsed")

                self.cpmcpumemoryusedovrflw = YLeaf(YType.uint32, "cpmCPUMemoryUsedOvrflw")

                self.cpmcpumoninterval = YLeaf(YType.uint32, "cpmCPUMonInterval")

                self.cpmcputotal1min = YLeaf(YType.uint32, "cpmCPUTotal1min")

                self.cpmcputotal1minrev = YLeaf(YType.uint32, "cpmCPUTotal1minRev")

                self.cpmcputotal5min = YLeaf(YType.uint32, "cpmCPUTotal5min")

                self.cpmcputotal5minrev = YLeaf(YType.uint32, "cpmCPUTotal5minRev")

                self.cpmcputotal5sec = YLeaf(YType.uint32, "cpmCPUTotal5sec")

                self.cpmcputotal5secrev = YLeaf(YType.uint32, "cpmCPUTotal5secRev")

                self.cpmcputotalmonintervalvalue = YLeaf(YType.uint32, "cpmCPUTotalMonIntervalValue")

                self.cpmcputotalphysicalindex = YLeaf(YType.int32, "cpmCPUTotalPhysicalIndex")
                self._segment_path = lambda: "cpmCPUTotalEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUTotalTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry, ['cpmcputotalindex', 'cpmcpuinterruptmonintervalvalue', 'cpmcpuloadavg15min', 'cpmcpuloadavg1min', 'cpmcpuloadavg5min', 'cpmcpumemorycommitted', 'cpmcpumemorycommittedovrflw', 'cpmcpumemoryfree', 'cpmcpumemoryfreeovrflw', 'cpmcpumemoryhccommitted', 'cpmcpumemoryhcfree', 'cpmcpumemoryhckernelreserved', 'cpmcpumemoryhclowest', 'cpmcpumemoryhcused', 'cpmcpumemorykernelreserved', 'cpmcpumemorykernelreservedovrflw', 'cpmcpumemorylowest', 'cpmcpumemorylowestovrflw', 'cpmcpumemoryused', 'cpmcpumemoryusedovrflw', 'cpmcpumoninterval', 'cpmcputotal1min', 'cpmcputotal1minrev', 'cpmcputotal5min', 'cpmcputotal5minrev', 'cpmcputotal5sec', 'cpmcputotal5secrev', 'cpmcputotalmonintervalvalue', 'cpmcputotalphysicalindex'], name, value)


    class Cpmprocessextrevtable(Entity):
        """
        This table contains information that may or may
        not be available on all cisco devices. It contains
        additional objects for the more general
        cpmProcessTable. This object deprecates 
        cpmProcessExtTable.
        
        .. attribute:: cpmprocessextreventry
        
        	An entry containing additional information for a particular process. This object deprecates  cpmProcessExtEntry
        	**type**\: list of    :py:class:`Cpmprocessextreventry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocessextrevtable.Cpmprocessextreventry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmprocessextrevtable, self).__init__()

            self.yang_name = "cpmProcessExtRevTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmProcessExtRevEntry" : ("cpmprocessextreventry", CISCOPROCESSMIB.Cpmprocessextrevtable.Cpmprocessextreventry)}

            self.cpmprocessextreventry = YList(self)
            self._segment_path = lambda: "cpmProcessExtRevTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmprocessextrevtable, [], name, value)


        class Cpmprocessextreventry(Entity):
            """
            An entry containing additional information for
            a particular process. This object deprecates 
            cpmProcessExtEntry.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmprocesspid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry>`
            
            .. attribute:: cpmprocessdatasegmentsize
            
            	This indicates the data segment of a process and all its shared objects
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessdatasegmentsizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessDataSegmentSize. This object needs to be supported only when the value of  cpmProcessDataSegmentSize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessdynamicmemorysize
            
            	This indicates the amount of dynamic memory being used by the process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessdynamicmemorysizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessDynamicMemorySize. This object needs to be supported only when the value of  cpmProcessDynamicMemorySize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshcdatasegmentsize
            
            	This indicates the data segment of a process and all its shared objects.. This object is a 64\-bit version of cpmProcessDataSegmentSize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshcdynamicmemorysize
            
            	This indicates the amount of dynamic memory being used by the process. This object is a 64\-bit version of cpmProcessDynamicMemorySize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshcstacksize
            
            	This indicates the amount of stack memory used by the process. This object is a 64\-bit version of cpmProcessStackSize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesshctextsegmentsize
            
            	This indicates the text memory of a process and all its shared objects. This object is a 64\-bit version of cpmProcessTextSegmentSize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesslastrestartuser
            
            	This indicate the user that has last restarted the process or has taken running coredump of the process
            	**type**\:  str
            
            .. attribute:: cpmprocessmemorycore
            
            	This indicates the part of process memory to be dumped when a process crashes. The process  memory is used for debugging purposes to trace the  root cause of the crash. sparse        \- Some operating systems support minimal                 dump of process core like register                 info, partial stack, partial memory                 pages especially for critical process                 to facilitate faster process restart
            	**type**\:   :py:class:`Cpmprocessmemorycore <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocessextrevtable.Cpmprocessextreventry.Cpmprocessmemorycore>`
            
            .. attribute:: cpmprocessrespawn
            
            	This indicates whether respawn of a process is enabled or not. If enabled the process in context repawns after it has crashed/stopped
            	**type**\:  int
            
            	**range:** 0..2
            
            .. attribute:: cpmprocessrespawnafterlastpatch
            
            	This indicates the number of times a process has restarted after the last patch is applied. This is to  determine the stability of the last patch
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessrespawncount
            
            	This indicates the number of times the process has respawned/restarted
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessstacksize
            
            	This indicates the amount of stack memory used by the process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocessstacksizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessStackSize. This object needs to be supported only when the value of cpmProcessStackSize exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesstextsegmentsize
            
            	This indicates the text memory of a process and all its shared objects
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesstextsegmentsizeovrflw
            
            	This object represents the upper 32\-bit of cpmProcessTextSegmentSize. This object needs to be supported only when the value of  cpmProcessTextSegmentSize exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: kilo-bytes
            
            .. attribute:: cpmprocesstype
            
            	This indicates the kind of process in context
            	**type**\:   :py:class:`Cpmprocesstype <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocessextrevtable.Cpmprocessextreventry.Cpmprocesstype>`
            
            .. attribute:: cpmprocexthcmemallocatedrev
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. This object is a 64\-bit version of cpmProcExtMemAllocatedRev
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cpmprocexthcmemfreedrev
            
            	The sum of all memory that this process has returned to the system. This object is a 64\-bit version of cpmProcExtMemFreedRev
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextinvokedrev
            
            	The number of times since cpmTimeCreated that the process has been invoked. This object  deprecates cpmProcExtInvoked
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocextmemallocatedrev
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. The sum of freed memory is provided by cpmProcExtMemFreedRev. This object deprecates cpmProcExtMemAllocated
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextmemallocatedrevovrflw
            
            	This object represents the upper 32\-bit of cpmProcExtMemAllocatedRev. This object needs to be supported only when the value of  cpmProcExtMemAllocatedRev exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextmemfreedrev
            
            	The sum of all memory that this process has returned to the system. This object  deprecates  cpmProcExtMemFreed
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextmemfreedrevovrflw
            
            	This object represents the upper 32\-bit of cpmProcExtMemFreedRev. This object needs to  be supported only when the value of cpmProcExtMemFreedRev exceeds 32\-bit,otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmprocextpriorityrev
            
            	The priority level at  which the process is running. This object deprecates  cpmProcExtPriority
            	**type**\:   :py:class:`Cpmprocextpriorityrev <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocessextrevtable.Cpmprocessextreventry.Cpmprocextpriorityrev>`
            
            .. attribute:: cpmprocextruntimerev
            
            	The amount of CPU time the process has used, in microseconds. This object deprecates cpmProcExtRuntime
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: cpmprocextutil1minrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 1  minute period. It is determined as a weighted  decaying average of the current idle time over the  longest idle time. Note that this information  should be used as an estimate only. This object  deprecates cpmProcExtUtil1Min and increases the value range to (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmprocextutil5minrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  minute period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object deprecates cpmProcExtUtil5Min and increases the value range to (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmprocextutil5secrev
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  second period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object deprecates cpmProcExtUtil5Sec and increases the  value range to (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmprocessextrevtable.Cpmprocessextreventry, self).__init__()

                self.yang_name = "cpmProcessExtRevEntry"
                self.yang_parent_name = "cpmProcessExtRevTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmprocesspid = YLeaf(YType.str, "cpmProcessPID")

                self.cpmprocessdatasegmentsize = YLeaf(YType.uint32, "cpmProcessDataSegmentSize")

                self.cpmprocessdatasegmentsizeovrflw = YLeaf(YType.uint32, "cpmProcessDataSegmentSizeOvrflw")

                self.cpmprocessdynamicmemorysize = YLeaf(YType.uint32, "cpmProcessDynamicMemorySize")

                self.cpmprocessdynamicmemorysizeovrflw = YLeaf(YType.uint32, "cpmProcessDynamicMemorySizeOvrflw")

                self.cpmprocesshcdatasegmentsize = YLeaf(YType.uint64, "cpmProcessHCDataSegmentSize")

                self.cpmprocesshcdynamicmemorysize = YLeaf(YType.uint64, "cpmProcessHCDynamicMemorySize")

                self.cpmprocesshcstacksize = YLeaf(YType.uint64, "cpmProcessHCStackSize")

                self.cpmprocesshctextsegmentsize = YLeaf(YType.uint64, "cpmProcessHCTextSegmentSize")

                self.cpmprocesslastrestartuser = YLeaf(YType.str, "cpmProcessLastRestartUser")

                self.cpmprocessmemorycore = YLeaf(YType.enumeration, "cpmProcessMemoryCore")

                self.cpmprocessrespawn = YLeaf(YType.uint32, "cpmProcessRespawn")

                self.cpmprocessrespawnafterlastpatch = YLeaf(YType.uint32, "cpmProcessRespawnAfterLastPatch")

                self.cpmprocessrespawncount = YLeaf(YType.uint32, "cpmProcessRespawnCount")

                self.cpmprocessstacksize = YLeaf(YType.uint32, "cpmProcessStackSize")

                self.cpmprocessstacksizeovrflw = YLeaf(YType.uint32, "cpmProcessStackSizeOvrflw")

                self.cpmprocesstextsegmentsize = YLeaf(YType.uint32, "cpmProcessTextSegmentSize")

                self.cpmprocesstextsegmentsizeovrflw = YLeaf(YType.uint32, "cpmProcessTextSegmentSizeOvrflw")

                self.cpmprocesstype = YLeaf(YType.enumeration, "cpmProcessType")

                self.cpmprocexthcmemallocatedrev = YLeaf(YType.uint64, "cpmProcExtHCMemAllocatedRev")

                self.cpmprocexthcmemfreedrev = YLeaf(YType.uint64, "cpmProcExtHCMemFreedRev")

                self.cpmprocextinvokedrev = YLeaf(YType.uint32, "cpmProcExtInvokedRev")

                self.cpmprocextmemallocatedrev = YLeaf(YType.uint32, "cpmProcExtMemAllocatedRev")

                self.cpmprocextmemallocatedrevovrflw = YLeaf(YType.uint32, "cpmProcExtMemAllocatedRevOvrflw")

                self.cpmprocextmemfreedrev = YLeaf(YType.uint32, "cpmProcExtMemFreedRev")

                self.cpmprocextmemfreedrevovrflw = YLeaf(YType.uint32, "cpmProcExtMemFreedRevOvrflw")

                self.cpmprocextpriorityrev = YLeaf(YType.enumeration, "cpmProcExtPriorityRev")

                self.cpmprocextruntimerev = YLeaf(YType.uint32, "cpmProcExtRuntimeRev")

                self.cpmprocextutil1minrev = YLeaf(YType.uint32, "cpmProcExtUtil1MinRev")

                self.cpmprocextutil5minrev = YLeaf(YType.uint32, "cpmProcExtUtil5MinRev")

                self.cpmprocextutil5secrev = YLeaf(YType.uint32, "cpmProcExtUtil5SecRev")
                self._segment_path = lambda: "cpmProcessExtRevEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmProcessExtRevTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmprocessextrevtable.Cpmprocessextreventry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmprocessdatasegmentsize', 'cpmprocessdatasegmentsizeovrflw', 'cpmprocessdynamicmemorysize', 'cpmprocessdynamicmemorysizeovrflw', 'cpmprocesshcdatasegmentsize', 'cpmprocesshcdynamicmemorysize', 'cpmprocesshcstacksize', 'cpmprocesshctextsegmentsize', 'cpmprocesslastrestartuser', 'cpmprocessmemorycore', 'cpmprocessrespawn', 'cpmprocessrespawnafterlastpatch', 'cpmprocessrespawncount', 'cpmprocessstacksize', 'cpmprocessstacksizeovrflw', 'cpmprocesstextsegmentsize', 'cpmprocesstextsegmentsizeovrflw', 'cpmprocesstype', 'cpmprocexthcmemallocatedrev', 'cpmprocexthcmemfreedrev', 'cpmprocextinvokedrev', 'cpmprocextmemallocatedrev', 'cpmprocextmemallocatedrevovrflw', 'cpmprocextmemfreedrev', 'cpmprocextmemfreedrevovrflw', 'cpmprocextpriorityrev', 'cpmprocextruntimerev', 'cpmprocextutil1minrev', 'cpmprocextutil5minrev', 'cpmprocextutil5secrev'], name, value)

            class Cpmprocessmemorycore(Enum):
                """
                Cpmprocessmemorycore

                This indicates the part of process memory to be

                dumped when a process crashes. The process 

                memory is used for debugging purposes to trace the 

                root cause of the crash.

                sparse        \- Some operating systems support minimal

                                dump of process core like register

                                info, partial stack, partial memory

                                pages especially for critical process

                                to facilitate faster process restart.

                .. data:: none = 0

                .. data:: other = 1

                .. data:: mainmem = 2

                .. data:: mainmemSharedmem = 3

                .. data:: mainmemText = 4

                .. data:: mainmemTextSharedmem = 5

                .. data:: sharedmem = 6

                .. data:: sparse = 7

                .. data:: off = 8

                """

                none = Enum.YLeaf(0, "none")

                other = Enum.YLeaf(1, "other")

                mainmem = Enum.YLeaf(2, "mainmem")

                mainmemSharedmem = Enum.YLeaf(3, "mainmemSharedmem")

                mainmemText = Enum.YLeaf(4, "mainmemText")

                mainmemTextSharedmem = Enum.YLeaf(5, "mainmemTextSharedmem")

                sharedmem = Enum.YLeaf(6, "sharedmem")

                sparse = Enum.YLeaf(7, "sparse")

                off = Enum.YLeaf(8, "off")


            class Cpmprocesstype(Enum):
                """
                Cpmprocesstype

                This indicates the kind of process in context.

                .. data:: none = 0

                .. data:: other = 1

                .. data:: posix = 2

                .. data:: ios = 3

                """

                none = Enum.YLeaf(0, "none")

                other = Enum.YLeaf(1, "other")

                posix = Enum.YLeaf(2, "posix")

                ios = Enum.YLeaf(3, "ios")


            class Cpmprocextpriorityrev(Enum):
                """
                Cpmprocextpriorityrev

                The priority level at  which the process is

                running. This object deprecates 

                cpmProcExtPriority.

                .. data:: critical = 1

                .. data:: high = 2

                .. data:: normal = 3

                .. data:: low = 4

                .. data:: notAssigned = 5

                """

                critical = Enum.YLeaf(1, "critical")

                high = Enum.YLeaf(2, "high")

                normal = Enum.YLeaf(3, "normal")

                low = Enum.YLeaf(4, "low")

                notAssigned = Enum.YLeaf(5, "notAssigned")



    class Cpmprocesstable(Entity):
        """
        A table of generic information on all active
        processes on this device.
        
        .. attribute:: cpmprocessentry
        
        	Generic information about an active process on this device. Entries in this table come and go as processes are  created and destroyed by the device
        	**type**\: list of    :py:class:`Cpmprocessentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmprocesstable, self).__init__()

            self.yang_name = "cpmProcessTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmProcessEntry" : ("cpmprocessentry", CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry)}

            self.cpmprocessentry = YList(self)
            self._segment_path = lambda: "cpmProcessTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmprocesstable, [], name, value)


        class Cpmprocessentry(Entity):
            """
            Generic information about an active process on this
            device. Entries in this table come and go as processes are 
            created and destroyed by the device.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmprocesspid  <key>
            
            	This object contains the process ID. cpmTimeCreated should be checked against the last time it was polled, and if it has changed the PID has been reused and the entire entry should be polled again
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessaverageusecs
            
            	Average elapsed CPU time in microseconds when the process was active. This object deprecates the object cpmProcessuSecs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: cpmprocessname
            
            	The name associated with this process. If the name is longer than 32 characters, it will be truncated to the first 31 characters, and a `\*' will be appended as the last character to imply this is a truncated process name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cpmprocesstimecreated
            
            	The time when the process was created. The process ID and the time when the process was created, uniquely  identifies a process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmprocessusecs
            
            	Average elapsed CPU time in microseconds when the process was active. This object is deprecated by cpmProcessAverageUSecs
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextinvoked
            
            	The number of times since cpmTimeCreated that the process has been invoked. This object is deprecated by cpmProcExtInvokedRev
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextmemallocated
            
            	The sum of all the dynamically allocated memory that this process has received from the system. This includes memory that may have been returned. The sum of freed memory is provided by cpmProcExtMemFreed. This object is deprecated by cpmProcExtMemAllocatedRev
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextmemfreed
            
            	The sum of all memory that this process has returned to the system. This object is deprecated by  cpmProcExtMemFreedRev
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextpriority
            
            	The priority level at which the process is running. This object is deprecated by cpmProcExtPriorityRev
            	**type**\:   :py:class:`Cpmprocextpriority <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry.Cpmprocextpriority>`
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextruntime
            
            	The amount of CPU time the process has used, in microseconds. This object is deprecated by cpmProcExtRuntimeRev
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextutil1min
            
            	This object provides a general idea of how busy a process caused the processor to be over a 1  minute period. It is determined as a weighted  decaying average of the current idle time over the  longest idle time. Note that this information  should be used as an estimate only. This object is  deprecated by cpmProcExtUtil1MinRev which has the changed range of value (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextutil5min
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  minute period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object is deprecated by cpmProcExtUtil5MinRev which has the changed range of value (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**status**\: deprecated
            
            .. attribute:: cpmprocextutil5sec
            
            	This object provides a general idea of how busy a process caused the processor to be over a 5  second period. It is determined as a weighted  decaying average of the current idle time over  the longest idle time. Note that this information  should be used as an estimate only. This object is  deprecated by cpmProcExtUtil5SecRev which has the  changed range of value (0..100)
            	**type**\:  int
            
            	**range:** 0..100
            
            	**status**\: deprecated
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry, self).__init__()

                self.yang_name = "cpmProcessEntry"
                self.yang_parent_name = "cpmProcessTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmprocesspid = YLeaf(YType.uint32, "cpmProcessPID")

                self.cpmprocessaverageusecs = YLeaf(YType.uint32, "cpmProcessAverageUSecs")

                self.cpmprocessname = YLeaf(YType.str, "cpmProcessName")

                self.cpmprocesstimecreated = YLeaf(YType.uint32, "cpmProcessTimeCreated")

                self.cpmprocessusecs = YLeaf(YType.uint32, "cpmProcessuSecs")

                self.cpmprocextinvoked = YLeaf(YType.uint32, "cpmProcExtInvoked")

                self.cpmprocextmemallocated = YLeaf(YType.uint32, "cpmProcExtMemAllocated")

                self.cpmprocextmemfreed = YLeaf(YType.uint32, "cpmProcExtMemFreed")

                self.cpmprocextpriority = YLeaf(YType.enumeration, "cpmProcExtPriority")

                self.cpmprocextruntime = YLeaf(YType.uint32, "cpmProcExtRuntime")

                self.cpmprocextutil1min = YLeaf(YType.uint32, "cpmProcExtUtil1Min")

                self.cpmprocextutil5min = YLeaf(YType.uint32, "cpmProcExtUtil5Min")

                self.cpmprocextutil5sec = YLeaf(YType.uint32, "cpmProcExtUtil5Sec")
                self._segment_path = lambda: "cpmProcessEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmProcessTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmprocessaverageusecs', 'cpmprocessname', 'cpmprocesstimecreated', 'cpmprocessusecs', 'cpmprocextinvoked', 'cpmprocextmemallocated', 'cpmprocextmemfreed', 'cpmprocextpriority', 'cpmprocextruntime', 'cpmprocextutil1min', 'cpmprocextutil5min', 'cpmprocextutil5sec'], name, value)

            class Cpmprocextpriority(Enum):
                """
                Cpmprocextpriority

                The priority level at which the process is

                running. This object is deprecated by

                cpmProcExtPriorityRev.

                .. data:: critical = 1

                .. data:: high = 2

                .. data:: normal = 3

                .. data:: low = 4

                .. data:: notAssigned = 5

                """

                critical = Enum.YLeaf(1, "critical")

                high = Enum.YLeaf(2, "high")

                normal = Enum.YLeaf(3, "normal")

                low = Enum.YLeaf(4, "low")

                notAssigned = Enum.YLeaf(5, "notAssigned")



    class Cpmthreadtable(Entity):
        """
        This table contains generic information about
        POSIX threads in the device.
        
        .. attribute:: cpmthreadentry
        
        	An entry containing the general statistics of a POSIX thread
        	**type**\: list of    :py:class:`Cpmthreadentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmthreadtable.Cpmthreadentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmthreadtable, self).__init__()

            self.yang_name = "cpmThreadTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmThreadEntry" : ("cpmthreadentry", CISCOPROCESSMIB.Cpmthreadtable.Cpmthreadentry)}

            self.cpmthreadentry = YList(self)
            self._segment_path = lambda: "cpmThreadTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmthreadtable, [], name, value)


        class Cpmthreadentry(Entity):
            """
            An entry containing the general statistics
            of a POSIX thread.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmprocesspid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry>`
            
            .. attribute:: cpmthreadid  <key>
            
            	This object contains the thread ID. ThreadID is Unique per process
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmthreadblockingprocess
            
            	This object identifies the process on which the current thread is blocked on. This points to the  cpmProcessTable of the process on which the thread  in context is blocked. This is valid only to threads which are either in send/reply states. For the  rest of the threads it is returned as 0.0
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cpmthreadcpuutilization
            
            	This object provides a general idea on how busy the thread in context caused the processor to be
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: milliseconds
            
            .. attribute:: cpmthreadhcstacksize
            
            	This object indicates the stack size allocated to the thread in context. This object is a 64\-bit version of cpmThreadStackSize
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cpmthreadname
            
            	This object represents the name of the thread. Thread names need not be unique. Hence statistics  should be analyzed against thread ID
            	**type**\:  str
            
            .. attribute:: cpmthreadpriority
            
            	This object indicates the priority of a POSIX thread. The higher the number, the higher the priority of the  thread over other threads
            	**type**\:  int
            
            	**range:** 0..63
            
            .. attribute:: cpmthreadstacksize
            
            	This object indicates the stack size allocated to the thread in context
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmthreadstacksizeovrflw
            
            	This object represents the upper 32\-bit of cpmThreadStackSize. This object needs to be supported only when the value of cpmThreadStackSize exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmthreadstate
            
            	This object indicates the current state of a thread. Running state means that the thread is actively  consumig CPU. All the other states are just waiting  states. The valid states are\: other         \- Any other state apart from the listed                  ones. dead          \- Kernel is waiting to release the                  thread's resources. running       \- Actively running on a CPU. ready         \- Not running on a CPU, but is ready to                  run (one or more higher or equal                  priority threads are running). stopped       \- Suspended (SIGSTOP signal). send          \- Waiting for a server to receive                  a message. receive       \- Waiting for a client to send a message. reply         \- Waiting for a server to reply to a                  message. stack         \- Waiting for more stack to be allocated. waitpage      \- Waiting for process manager to                  resolve a fault on a page. sigsuspend    \- Suspended for a signal. sigwaitinfo   \- Waiting for a signal. nanosleep     \- Sleeping for a period of time. mutex         \- Waiting to acquire a mutex condvar       \- Waiting for a condition variable to be                  signalled. join          \- Waiting for the completion of another                  thread. intr          \- Waiting for an interrupt. sem           \- Waiting to acquire a semaphore
            	**type**\:   :py:class:`Cpmthreadstate <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmthreadtable.Cpmthreadentry.Cpmthreadstate>`
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmthreadtable.Cpmthreadentry, self).__init__()

                self.yang_name = "cpmThreadEntry"
                self.yang_parent_name = "cpmThreadTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmprocesspid = YLeaf(YType.str, "cpmProcessPID")

                self.cpmthreadid = YLeaf(YType.uint32, "cpmThreadID")

                self.cpmthreadblockingprocess = YLeaf(YType.str, "cpmThreadBlockingProcess")

                self.cpmthreadcpuutilization = YLeaf(YType.uint32, "cpmThreadCpuUtilization")

                self.cpmthreadhcstacksize = YLeaf(YType.uint64, "cpmThreadHCStackSize")

                self.cpmthreadname = YLeaf(YType.str, "cpmThreadName")

                self.cpmthreadpriority = YLeaf(YType.uint32, "cpmThreadPriority")

                self.cpmthreadstacksize = YLeaf(YType.uint32, "cpmThreadStackSize")

                self.cpmthreadstacksizeovrflw = YLeaf(YType.uint32, "cpmThreadStackSizeOvrflw")

                self.cpmthreadstate = YLeaf(YType.enumeration, "cpmThreadState")
                self._segment_path = lambda: "cpmThreadEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']" + "[cpmThreadID='" + self.cpmthreadid.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmThreadTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmthreadtable.Cpmthreadentry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmthreadid', 'cpmthreadblockingprocess', 'cpmthreadcpuutilization', 'cpmthreadhcstacksize', 'cpmthreadname', 'cpmthreadpriority', 'cpmthreadstacksize', 'cpmthreadstacksizeovrflw', 'cpmthreadstate'], name, value)

            class Cpmthreadstate(Enum):
                """
                Cpmthreadstate

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

                .. data:: other = 1

                .. data:: dead = 2

                .. data:: running = 3

                .. data:: ready = 4

                .. data:: stopped = 5

                .. data:: send = 6

                .. data:: receive = 7

                .. data:: reply = 8

                .. data:: stack = 9

                .. data:: waitpage = 10

                .. data:: sigsuspend = 11

                .. data:: sigwaitinfo = 12

                .. data:: nanosleep = 13

                .. data:: mutex = 14

                .. data:: condvar = 15

                .. data:: join = 16

                .. data:: intr = 17

                .. data:: sem = 18

                """

                other = Enum.YLeaf(1, "other")

                dead = Enum.YLeaf(2, "dead")

                running = Enum.YLeaf(3, "running")

                ready = Enum.YLeaf(4, "ready")

                stopped = Enum.YLeaf(5, "stopped")

                send = Enum.YLeaf(6, "send")

                receive = Enum.YLeaf(7, "receive")

                reply = Enum.YLeaf(8, "reply")

                stack = Enum.YLeaf(9, "stack")

                waitpage = Enum.YLeaf(10, "waitpage")

                sigsuspend = Enum.YLeaf(11, "sigsuspend")

                sigwaitinfo = Enum.YLeaf(12, "sigwaitinfo")

                nanosleep = Enum.YLeaf(13, "nanosleep")

                mutex = Enum.YLeaf(14, "mutex")

                condvar = Enum.YLeaf(15, "condvar")

                join = Enum.YLeaf(16, "join")

                intr = Enum.YLeaf(17, "intr")

                sem = Enum.YLeaf(18, "sem")



    class Cpmvirtualprocesstable(Entity):
        """
        This table contains information about virtual
        processes in a virtual machine.
        
        .. attribute:: cpmvirtualprocessentry
        
        	An entry containing the general statistics of a virtual process in a virtual machine
        	**type**\: list of    :py:class:`Cpmvirtualprocessentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmvirtualprocesstable.Cpmvirtualprocessentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CISCOPROCESSMIB.Cpmvirtualprocesstable, self).__init__()

            self.yang_name = "cpmVirtualProcessTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self._child_container_classes = {}
            self._child_list_classes = {"cpmVirtualProcessEntry" : ("cpmvirtualprocessentry", CISCOPROCESSMIB.Cpmvirtualprocesstable.Cpmvirtualprocessentry)}

            self.cpmvirtualprocessentry = YList(self)
            self._segment_path = lambda: "cpmVirtualProcessTable"
            self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self._segment_path()

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOPROCESSMIB.Cpmvirtualprocesstable, [], name, value)


        class Cpmvirtualprocessentry(Entity):
            """
            An entry containing the general statistics of a
            virtual process in a virtual machine.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmprocesspid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CISCOPROCESSMIB.Cpmprocesstable.Cpmprocessentry>`
            
            .. attribute:: cpmvirtualprocessid  <key>
            
            	This object indicates the process ID of a virtual process. PID is unique only inside one address space. Virtual process PID should be considered along with  Parent process cpmProcessPID
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocesshcmemallocated
            
            	This object indicates the memory allocated by the virtual process inside the address space of a process running on Native OS. This object is a 64\-bit version of cpmVirtualProcessMemAllocated
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocesshcmemfreed
            
            	This object indicates the memory freed by the virtual process inside the address space of a process running on Native OS.This object is a 64\-bit version of cpmVirtualProcessMemAllocated
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessinvokecount
            
            	The number of times a virtual process is invoked
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cpmvirtualprocessmemallocated
            
            	This object indicates the memory allocated by the virtual process inside the address space of a  process running on Native OS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessmemallocatedovrflw
            
            	This object represents the upper 32\-bit of cpmVirtualProcessMemAllocated. This object  needs to be supported only when the value of cpmVirtualProcessMemAllocated exceeds 32\-bit, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessmemfreed
            
            	This object indicates the memory freed by the virtual process inside the address space of a process running  on Native OS
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessmemfreedovrflw
            
            	This object represents the upper 32\-bit of cpmVirtualProcessMemFreed. This object needs to be supported only when the value of  cpmVirtualProcessMemFreed exceeds 32\-bit,  otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cpmvirtualprocessname
            
            	This object indicates the name of a virtual process. If the name is longer than 32 characters, it will be truncated to the first 31 characters, and a `\*' will be appended as the last character to imply this is a truncated process name
            	**type**\:  str
            
            	**length:** 1..32
            
            .. attribute:: cpmvirtualprocessruntime
            
            	The amount of CPU time a virtual process has used in microseconds
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: microseconds
            
            .. attribute:: cpmvirtualprocessutil1min
            
            	This indicates an estimated CPU utilization by a virtual process over the last one minute
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmvirtualprocessutil5min
            
            	This indicates an estimated CPU utilization by a virtual process over the last 5 minutes
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            .. attribute:: cpmvirtualprocessutil5sec
            
            	This indicates an estimated CPU utilization by a virtual process over the last 5 seconds
            	**type**\:  int
            
            	**range:** 0..100
            
            	**units**\: percent
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CISCOPROCESSMIB.Cpmvirtualprocesstable.Cpmvirtualprocessentry, self).__init__()

                self.yang_name = "cpmVirtualProcessEntry"
                self.yang_parent_name = "cpmVirtualProcessTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self._child_container_classes = {}
                self._child_list_classes = {}

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmprocesspid = YLeaf(YType.str, "cpmProcessPID")

                self.cpmvirtualprocessid = YLeaf(YType.uint32, "cpmVirtualProcessID")

                self.cpmvirtualprocesshcmemallocated = YLeaf(YType.uint64, "cpmVirtualProcessHCMemAllocated")

                self.cpmvirtualprocesshcmemfreed = YLeaf(YType.uint64, "cpmVirtualProcessHCMemFreed")

                self.cpmvirtualprocessinvokecount = YLeaf(YType.uint32, "cpmVirtualProcessInvokeCount")

                self.cpmvirtualprocessmemallocated = YLeaf(YType.uint32, "cpmVirtualProcessMemAllocated")

                self.cpmvirtualprocessmemallocatedovrflw = YLeaf(YType.uint32, "cpmVirtualProcessMemAllocatedOvrflw")

                self.cpmvirtualprocessmemfreed = YLeaf(YType.uint32, "cpmVirtualProcessMemFreed")

                self.cpmvirtualprocessmemfreedovrflw = YLeaf(YType.uint32, "cpmVirtualProcessMemFreedOvrflw")

                self.cpmvirtualprocessname = YLeaf(YType.str, "cpmVirtualProcessName")

                self.cpmvirtualprocessruntime = YLeaf(YType.uint32, "cpmVirtualProcessRuntime")

                self.cpmvirtualprocessutil1min = YLeaf(YType.uint32, "cpmVirtualProcessUtil1Min")

                self.cpmvirtualprocessutil5min = YLeaf(YType.uint32, "cpmVirtualProcessUtil5Min")

                self.cpmvirtualprocessutil5sec = YLeaf(YType.uint32, "cpmVirtualProcessUtil5Sec")
                self._segment_path = lambda: "cpmVirtualProcessEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']" + "[cpmVirtualProcessID='" + self.cpmvirtualprocessid.get() + "']"
                self._absolute_path = lambda: "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmVirtualProcessTable/%s" % self._segment_path()

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOPROCESSMIB.Cpmvirtualprocesstable.Cpmvirtualprocessentry, ['cpmcputotalindex', 'cpmprocesspid', 'cpmvirtualprocessid', 'cpmvirtualprocesshcmemallocated', 'cpmvirtualprocesshcmemfreed', 'cpmvirtualprocessinvokecount', 'cpmvirtualprocessmemallocated', 'cpmvirtualprocessmemallocatedovrflw', 'cpmvirtualprocessmemfreed', 'cpmvirtualprocessmemfreedovrflw', 'cpmvirtualprocessname', 'cpmvirtualprocessruntime', 'cpmvirtualprocessutil1min', 'cpmvirtualprocessutil5min', 'cpmvirtualprocessutil5sec'], name, value)

    def clone_ptr(self):
        self._top_entity = CISCOPROCESSMIB()
        return self._top_entity

