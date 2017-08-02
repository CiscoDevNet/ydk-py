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
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CiscoProcessMib(Entity):
    """
    
    
    .. attribute:: cpmcoretable
    
    	A table of per\-Core statistics
    	**type**\:   :py:class:`Cpmcoretable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcoretable>`
    
    .. attribute:: cpmcpuhistory
    
    	
    	**type**\:   :py:class:`Cpmcpuhistory <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcpuhistory>`
    
    .. attribute:: cpmcpuhistorytable
    
    	A list of CPU utilization history entries
    	**type**\:   :py:class:`Cpmcpuhistorytable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcpuhistorytable>`
    
    .. attribute:: cpmcpuprocesshistorytable
    
    	A list of process history entries. This table contains CPU utilization of processes which crossed the  cpmCPUHistoryThreshold
    	**type**\:   :py:class:`Cpmcpuprocesshistorytable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcpuprocesshistorytable>`
    
    .. attribute:: cpmcputhresholdtable
    
    	This table contains the information about the thresholding values for CPU , configured by the user
    	**type**\:   :py:class:`Cpmcputhresholdtable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputhresholdtable>`
    
    .. attribute:: cpmcputotaltable
    
    	A table of overall CPU statistics
    	**type**\:   :py:class:`Cpmcputotaltable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable>`
    
    .. attribute:: cpmprocessextrevtable
    
    	This table contains information that may or may not be available on all cisco devices. It contains additional objects for the more general cpmProcessTable. This object deprecates  cpmProcessExtTable
    	**type**\:   :py:class:`Cpmprocessextrevtable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocessextrevtable>`
    
    .. attribute:: cpmprocesstable
    
    	A table of generic information on all active processes on this device
    	**type**\:   :py:class:`Cpmprocesstable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocesstable>`
    
    .. attribute:: cpmthreadtable
    
    	This table contains generic information about POSIX threads in the device
    	**type**\:   :py:class:`Cpmthreadtable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmthreadtable>`
    
    .. attribute:: cpmvirtualprocesstable
    
    	This table contains information about virtual processes in a virtual machine
    	**type**\:   :py:class:`Cpmvirtualprocesstable <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmvirtualprocesstable>`
    
    

    """

    _prefix = 'CISCO-PROCESS-MIB'
    _revision = '2011-06-23'

    def __init__(self):
        super(CiscoProcessMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-PROCESS-MIB"
        self.yang_parent_name = "CISCO-PROCESS-MIB"

        self.cpmcoretable = CiscoProcessMib.Cpmcoretable()
        self.cpmcoretable.parent = self
        self._children_name_map["cpmcoretable"] = "cpmCoreTable"
        self._children_yang_names.add("cpmCoreTable")

        self.cpmcpuhistory = CiscoProcessMib.Cpmcpuhistory()
        self.cpmcpuhistory.parent = self
        self._children_name_map["cpmcpuhistory"] = "cpmCPUHistory"
        self._children_yang_names.add("cpmCPUHistory")

        self.cpmcpuhistorytable = CiscoProcessMib.Cpmcpuhistorytable()
        self.cpmcpuhistorytable.parent = self
        self._children_name_map["cpmcpuhistorytable"] = "cpmCPUHistoryTable"
        self._children_yang_names.add("cpmCPUHistoryTable")

        self.cpmcpuprocesshistorytable = CiscoProcessMib.Cpmcpuprocesshistorytable()
        self.cpmcpuprocesshistorytable.parent = self
        self._children_name_map["cpmcpuprocesshistorytable"] = "cpmCPUProcessHistoryTable"
        self._children_yang_names.add("cpmCPUProcessHistoryTable")

        self.cpmcputhresholdtable = CiscoProcessMib.Cpmcputhresholdtable()
        self.cpmcputhresholdtable.parent = self
        self._children_name_map["cpmcputhresholdtable"] = "cpmCPUThresholdTable"
        self._children_yang_names.add("cpmCPUThresholdTable")

        self.cpmcputotaltable = CiscoProcessMib.Cpmcputotaltable()
        self.cpmcputotaltable.parent = self
        self._children_name_map["cpmcputotaltable"] = "cpmCPUTotalTable"
        self._children_yang_names.add("cpmCPUTotalTable")

        self.cpmprocessextrevtable = CiscoProcessMib.Cpmprocessextrevtable()
        self.cpmprocessextrevtable.parent = self
        self._children_name_map["cpmprocessextrevtable"] = "cpmProcessExtRevTable"
        self._children_yang_names.add("cpmProcessExtRevTable")

        self.cpmprocesstable = CiscoProcessMib.Cpmprocesstable()
        self.cpmprocesstable.parent = self
        self._children_name_map["cpmprocesstable"] = "cpmProcessTable"
        self._children_yang_names.add("cpmProcessTable")

        self.cpmthreadtable = CiscoProcessMib.Cpmthreadtable()
        self.cpmthreadtable.parent = self
        self._children_name_map["cpmthreadtable"] = "cpmThreadTable"
        self._children_yang_names.add("cpmThreadTable")

        self.cpmvirtualprocesstable = CiscoProcessMib.Cpmvirtualprocesstable()
        self.cpmvirtualprocesstable.parent = self
        self._children_name_map["cpmvirtualprocesstable"] = "cpmVirtualProcessTable"
        self._children_yang_names.add("cpmVirtualProcessTable")


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
            super(CiscoProcessMib.Cpmcpuhistory, self).__init__()

            self.yang_name = "cpmCPUHistory"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmcpuhistorysize = YLeaf(YType.uint32, "cpmCPUHistorySize")

            self.cpmcpuhistorythreshold = YLeaf(YType.uint32, "cpmCPUHistoryThreshold")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cpmcpuhistorysize",
                            "cpmcpuhistorythreshold") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmcpuhistory, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmcpuhistory, self).__setattr__(name, value)

        def has_data(self):
            return (
                self.cpmcpuhistorysize.is_set or
                self.cpmcpuhistorythreshold.is_set)

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cpmcpuhistorysize.yfilter != YFilter.not_set or
                self.cpmcpuhistorythreshold.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmCPUHistory" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cpmcpuhistorysize.is_set or self.cpmcpuhistorysize.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpmcpuhistorysize.get_name_leafdata())
            if (self.cpmcpuhistorythreshold.is_set or self.cpmcpuhistorythreshold.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cpmcpuhistorythreshold.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmCPUHistorySize" or name == "cpmCPUHistoryThreshold"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cpmCPUHistorySize"):
                self.cpmcpuhistorysize = value
                self.cpmcpuhistorysize.value_namespace = name_space
                self.cpmcpuhistorysize.value_namespace_prefix = name_space_prefix
            if(value_path == "cpmCPUHistoryThreshold"):
                self.cpmcpuhistorythreshold = value
                self.cpmcpuhistorythreshold.value_namespace = name_space
                self.cpmcpuhistorythreshold.value_namespace_prefix = name_space_prefix


    class Cpmcputotaltable(Entity):
        """
        A table of overall CPU statistics.
        
        .. attribute:: cpmcputotalentry
        
        	Overall information about the CPU load. Entries in this table come and go as CPUs are added and removed from the system
        	**type**\: list of    :py:class:`Cpmcputotalentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmcputotaltable, self).__init__()

            self.yang_name = "cpmCPUTotalTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmcputotalentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmcputotaltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmcputotaltable, self).__setattr__(name, value)


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
                super(CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry, self).__init__()

                self.yang_name = "cpmCPUTotalEntry"
                self.yang_parent_name = "cpmCPUTotalTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmcpuinterruptmonintervalvalue",
                                "cpmcpuloadavg15min",
                                "cpmcpuloadavg1min",
                                "cpmcpuloadavg5min",
                                "cpmcpumemorycommitted",
                                "cpmcpumemorycommittedovrflw",
                                "cpmcpumemoryfree",
                                "cpmcpumemoryfreeovrflw",
                                "cpmcpumemoryhccommitted",
                                "cpmcpumemoryhcfree",
                                "cpmcpumemoryhckernelreserved",
                                "cpmcpumemoryhclowest",
                                "cpmcpumemoryhcused",
                                "cpmcpumemorykernelreserved",
                                "cpmcpumemorykernelreservedovrflw",
                                "cpmcpumemorylowest",
                                "cpmcpumemorylowestovrflw",
                                "cpmcpumemoryused",
                                "cpmcpumemoryusedovrflw",
                                "cpmcpumoninterval",
                                "cpmcputotal1min",
                                "cpmcputotal1minrev",
                                "cpmcputotal5min",
                                "cpmcputotal5minrev",
                                "cpmcputotal5sec",
                                "cpmcputotal5secrev",
                                "cpmcputotalmonintervalvalue",
                                "cpmcputotalphysicalindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmcpuinterruptmonintervalvalue.is_set or
                    self.cpmcpuloadavg15min.is_set or
                    self.cpmcpuloadavg1min.is_set or
                    self.cpmcpuloadavg5min.is_set or
                    self.cpmcpumemorycommitted.is_set or
                    self.cpmcpumemorycommittedovrflw.is_set or
                    self.cpmcpumemoryfree.is_set or
                    self.cpmcpumemoryfreeovrflw.is_set or
                    self.cpmcpumemoryhccommitted.is_set or
                    self.cpmcpumemoryhcfree.is_set or
                    self.cpmcpumemoryhckernelreserved.is_set or
                    self.cpmcpumemoryhclowest.is_set or
                    self.cpmcpumemoryhcused.is_set or
                    self.cpmcpumemorykernelreserved.is_set or
                    self.cpmcpumemorykernelreservedovrflw.is_set or
                    self.cpmcpumemorylowest.is_set or
                    self.cpmcpumemorylowestovrflw.is_set or
                    self.cpmcpumemoryused.is_set or
                    self.cpmcpumemoryusedovrflw.is_set or
                    self.cpmcpumoninterval.is_set or
                    self.cpmcputotal1min.is_set or
                    self.cpmcputotal1minrev.is_set or
                    self.cpmcputotal5min.is_set or
                    self.cpmcputotal5minrev.is_set or
                    self.cpmcputotal5sec.is_set or
                    self.cpmcputotal5secrev.is_set or
                    self.cpmcputotalmonintervalvalue.is_set or
                    self.cpmcputotalphysicalindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmcpuinterruptmonintervalvalue.yfilter != YFilter.not_set or
                    self.cpmcpuloadavg15min.yfilter != YFilter.not_set or
                    self.cpmcpuloadavg1min.yfilter != YFilter.not_set or
                    self.cpmcpuloadavg5min.yfilter != YFilter.not_set or
                    self.cpmcpumemorycommitted.yfilter != YFilter.not_set or
                    self.cpmcpumemorycommittedovrflw.yfilter != YFilter.not_set or
                    self.cpmcpumemoryfree.yfilter != YFilter.not_set or
                    self.cpmcpumemoryfreeovrflw.yfilter != YFilter.not_set or
                    self.cpmcpumemoryhccommitted.yfilter != YFilter.not_set or
                    self.cpmcpumemoryhcfree.yfilter != YFilter.not_set or
                    self.cpmcpumemoryhckernelreserved.yfilter != YFilter.not_set or
                    self.cpmcpumemoryhclowest.yfilter != YFilter.not_set or
                    self.cpmcpumemoryhcused.yfilter != YFilter.not_set or
                    self.cpmcpumemorykernelreserved.yfilter != YFilter.not_set or
                    self.cpmcpumemorykernelreservedovrflw.yfilter != YFilter.not_set or
                    self.cpmcpumemorylowest.yfilter != YFilter.not_set or
                    self.cpmcpumemorylowestovrflw.yfilter != YFilter.not_set or
                    self.cpmcpumemoryused.yfilter != YFilter.not_set or
                    self.cpmcpumemoryusedovrflw.yfilter != YFilter.not_set or
                    self.cpmcpumoninterval.yfilter != YFilter.not_set or
                    self.cpmcputotal1min.yfilter != YFilter.not_set or
                    self.cpmcputotal1minrev.yfilter != YFilter.not_set or
                    self.cpmcputotal5min.yfilter != YFilter.not_set or
                    self.cpmcputotal5minrev.yfilter != YFilter.not_set or
                    self.cpmcputotal5sec.yfilter != YFilter.not_set or
                    self.cpmcputotal5secrev.yfilter != YFilter.not_set or
                    self.cpmcputotalmonintervalvalue.yfilter != YFilter.not_set or
                    self.cpmcputotalphysicalindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmCPUTotalEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUTotalTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmcpuinterruptmonintervalvalue.is_set or self.cpmcpuinterruptmonintervalvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuinterruptmonintervalvalue.get_name_leafdata())
                if (self.cpmcpuloadavg15min.is_set or self.cpmcpuloadavg15min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuloadavg15min.get_name_leafdata())
                if (self.cpmcpuloadavg1min.is_set or self.cpmcpuloadavg1min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuloadavg1min.get_name_leafdata())
                if (self.cpmcpuloadavg5min.is_set or self.cpmcpuloadavg5min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuloadavg5min.get_name_leafdata())
                if (self.cpmcpumemorycommitted.is_set or self.cpmcpumemorycommitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemorycommitted.get_name_leafdata())
                if (self.cpmcpumemorycommittedovrflw.is_set or self.cpmcpumemorycommittedovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemorycommittedovrflw.get_name_leafdata())
                if (self.cpmcpumemoryfree.is_set or self.cpmcpumemoryfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryfree.get_name_leafdata())
                if (self.cpmcpumemoryfreeovrflw.is_set or self.cpmcpumemoryfreeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryfreeovrflw.get_name_leafdata())
                if (self.cpmcpumemoryhccommitted.is_set or self.cpmcpumemoryhccommitted.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryhccommitted.get_name_leafdata())
                if (self.cpmcpumemoryhcfree.is_set or self.cpmcpumemoryhcfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryhcfree.get_name_leafdata())
                if (self.cpmcpumemoryhckernelreserved.is_set or self.cpmcpumemoryhckernelreserved.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryhckernelreserved.get_name_leafdata())
                if (self.cpmcpumemoryhclowest.is_set or self.cpmcpumemoryhclowest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryhclowest.get_name_leafdata())
                if (self.cpmcpumemoryhcused.is_set or self.cpmcpumemoryhcused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryhcused.get_name_leafdata())
                if (self.cpmcpumemorykernelreserved.is_set or self.cpmcpumemorykernelreserved.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemorykernelreserved.get_name_leafdata())
                if (self.cpmcpumemorykernelreservedovrflw.is_set or self.cpmcpumemorykernelreservedovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemorykernelreservedovrflw.get_name_leafdata())
                if (self.cpmcpumemorylowest.is_set or self.cpmcpumemorylowest.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemorylowest.get_name_leafdata())
                if (self.cpmcpumemorylowestovrflw.is_set or self.cpmcpumemorylowestovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemorylowestovrflw.get_name_leafdata())
                if (self.cpmcpumemoryused.is_set or self.cpmcpumemoryused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryused.get_name_leafdata())
                if (self.cpmcpumemoryusedovrflw.is_set or self.cpmcpumemoryusedovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumemoryusedovrflw.get_name_leafdata())
                if (self.cpmcpumoninterval.is_set or self.cpmcpumoninterval.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpumoninterval.get_name_leafdata())
                if (self.cpmcputotal1min.is_set or self.cpmcputotal1min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotal1min.get_name_leafdata())
                if (self.cpmcputotal1minrev.is_set or self.cpmcputotal1minrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotal1minrev.get_name_leafdata())
                if (self.cpmcputotal5min.is_set or self.cpmcputotal5min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotal5min.get_name_leafdata())
                if (self.cpmcputotal5minrev.is_set or self.cpmcputotal5minrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotal5minrev.get_name_leafdata())
                if (self.cpmcputotal5sec.is_set or self.cpmcputotal5sec.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotal5sec.get_name_leafdata())
                if (self.cpmcputotal5secrev.is_set or self.cpmcputotal5secrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotal5secrev.get_name_leafdata())
                if (self.cpmcputotalmonintervalvalue.is_set or self.cpmcputotalmonintervalvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalmonintervalvalue.get_name_leafdata())
                if (self.cpmcputotalphysicalindex.is_set or self.cpmcputotalphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalphysicalindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmCPUInterruptMonIntervalValue" or name == "cpmCPULoadAvg15min" or name == "cpmCPULoadAvg1min" or name == "cpmCPULoadAvg5min" or name == "cpmCPUMemoryCommitted" or name == "cpmCPUMemoryCommittedOvrflw" or name == "cpmCPUMemoryFree" or name == "cpmCPUMemoryFreeOvrflw" or name == "cpmCPUMemoryHCCommitted" or name == "cpmCPUMemoryHCFree" or name == "cpmCPUMemoryHCKernelReserved" or name == "cpmCPUMemoryHCLowest" or name == "cpmCPUMemoryHCUsed" or name == "cpmCPUMemoryKernelReserved" or name == "cpmCPUMemoryKernelReservedOvrflw" or name == "cpmCPUMemoryLowest" or name == "cpmCPUMemoryLowestOvrflw" or name == "cpmCPUMemoryUsed" or name == "cpmCPUMemoryUsedOvrflw" or name == "cpmCPUMonInterval" or name == "cpmCPUTotal1min" or name == "cpmCPUTotal1minRev" or name == "cpmCPUTotal5min" or name == "cpmCPUTotal5minRev" or name == "cpmCPUTotal5sec" or name == "cpmCPUTotal5secRev" or name == "cpmCPUTotalMonIntervalValue" or name == "cpmCPUTotalPhysicalIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUInterruptMonIntervalValue"):
                    self.cpmcpuinterruptmonintervalvalue = value
                    self.cpmcpuinterruptmonintervalvalue.value_namespace = name_space
                    self.cpmcpuinterruptmonintervalvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPULoadAvg15min"):
                    self.cpmcpuloadavg15min = value
                    self.cpmcpuloadavg15min.value_namespace = name_space
                    self.cpmcpuloadavg15min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPULoadAvg1min"):
                    self.cpmcpuloadavg1min = value
                    self.cpmcpuloadavg1min.value_namespace = name_space
                    self.cpmcpuloadavg1min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPULoadAvg5min"):
                    self.cpmcpuloadavg5min = value
                    self.cpmcpuloadavg5min.value_namespace = name_space
                    self.cpmcpuloadavg5min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryCommitted"):
                    self.cpmcpumemorycommitted = value
                    self.cpmcpumemorycommitted.value_namespace = name_space
                    self.cpmcpumemorycommitted.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryCommittedOvrflw"):
                    self.cpmcpumemorycommittedovrflw = value
                    self.cpmcpumemorycommittedovrflw.value_namespace = name_space
                    self.cpmcpumemorycommittedovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryFree"):
                    self.cpmcpumemoryfree = value
                    self.cpmcpumemoryfree.value_namespace = name_space
                    self.cpmcpumemoryfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryFreeOvrflw"):
                    self.cpmcpumemoryfreeovrflw = value
                    self.cpmcpumemoryfreeovrflw.value_namespace = name_space
                    self.cpmcpumemoryfreeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryHCCommitted"):
                    self.cpmcpumemoryhccommitted = value
                    self.cpmcpumemoryhccommitted.value_namespace = name_space
                    self.cpmcpumemoryhccommitted.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryHCFree"):
                    self.cpmcpumemoryhcfree = value
                    self.cpmcpumemoryhcfree.value_namespace = name_space
                    self.cpmcpumemoryhcfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryHCKernelReserved"):
                    self.cpmcpumemoryhckernelreserved = value
                    self.cpmcpumemoryhckernelreserved.value_namespace = name_space
                    self.cpmcpumemoryhckernelreserved.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryHCLowest"):
                    self.cpmcpumemoryhclowest = value
                    self.cpmcpumemoryhclowest.value_namespace = name_space
                    self.cpmcpumemoryhclowest.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryHCUsed"):
                    self.cpmcpumemoryhcused = value
                    self.cpmcpumemoryhcused.value_namespace = name_space
                    self.cpmcpumemoryhcused.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryKernelReserved"):
                    self.cpmcpumemorykernelreserved = value
                    self.cpmcpumemorykernelreserved.value_namespace = name_space
                    self.cpmcpumemorykernelreserved.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryKernelReservedOvrflw"):
                    self.cpmcpumemorykernelreservedovrflw = value
                    self.cpmcpumemorykernelreservedovrflw.value_namespace = name_space
                    self.cpmcpumemorykernelreservedovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryLowest"):
                    self.cpmcpumemorylowest = value
                    self.cpmcpumemorylowest.value_namespace = name_space
                    self.cpmcpumemorylowest.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryLowestOvrflw"):
                    self.cpmcpumemorylowestovrflw = value
                    self.cpmcpumemorylowestovrflw.value_namespace = name_space
                    self.cpmcpumemorylowestovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryUsed"):
                    self.cpmcpumemoryused = value
                    self.cpmcpumemoryused.value_namespace = name_space
                    self.cpmcpumemoryused.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMemoryUsedOvrflw"):
                    self.cpmcpumemoryusedovrflw = value
                    self.cpmcpumemoryusedovrflw.value_namespace = name_space
                    self.cpmcpumemoryusedovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUMonInterval"):
                    self.cpmcpumoninterval = value
                    self.cpmcpumoninterval.value_namespace = name_space
                    self.cpmcpumoninterval.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotal1min"):
                    self.cpmcputotal1min = value
                    self.cpmcputotal1min.value_namespace = name_space
                    self.cpmcputotal1min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotal1minRev"):
                    self.cpmcputotal1minrev = value
                    self.cpmcputotal1minrev.value_namespace = name_space
                    self.cpmcputotal1minrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotal5min"):
                    self.cpmcputotal5min = value
                    self.cpmcputotal5min.value_namespace = name_space
                    self.cpmcputotal5min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotal5minRev"):
                    self.cpmcputotal5minrev = value
                    self.cpmcputotal5minrev.value_namespace = name_space
                    self.cpmcputotal5minrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotal5sec"):
                    self.cpmcputotal5sec = value
                    self.cpmcputotal5sec.value_namespace = name_space
                    self.cpmcputotal5sec.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotal5secRev"):
                    self.cpmcputotal5secrev = value
                    self.cpmcputotal5secrev.value_namespace = name_space
                    self.cpmcputotal5secrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotalMonIntervalValue"):
                    self.cpmcputotalmonintervalvalue = value
                    self.cpmcputotalmonintervalvalue.value_namespace = name_space
                    self.cpmcputotalmonintervalvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUTotalPhysicalIndex"):
                    self.cpmcputotalphysicalindex = value
                    self.cpmcputotalphysicalindex.value_namespace = name_space
                    self.cpmcputotalphysicalindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmcputotalentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmcputotalentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmCPUTotalTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmCPUTotalEntry"):
                for c in self.cpmcputotalentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmcputotalentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmCPUTotalEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmcoretable(Entity):
        """
        A table of per\-Core statistics.
        
        .. attribute:: cpmcoreentry
        
        	Overall information about the Core load. Entries in this table could come and go as Cores go online or offline
        	**type**\: list of    :py:class:`Cpmcoreentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcoretable.Cpmcoreentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmcoretable, self).__init__()

            self.yang_name = "cpmCoreTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmcoreentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmcoretable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmcoretable, self).__setattr__(name, value)


        class Cpmcoreentry(Entity):
            """
            Overall information about the Core load. Entries in this
            table could come and go as Cores go online or offline.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
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
                super(CiscoProcessMib.Cpmcoretable.Cpmcoreentry, self).__init__()

                self.yang_name = "cpmCoreEntry"
                self.yang_parent_name = "cpmCoreTable"

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcoreindex = YLeaf(YType.uint32, "cpmCoreIndex")

                self.cpmcore1min = YLeaf(YType.uint32, "cpmCore1min")

                self.cpmcore5min = YLeaf(YType.uint32, "cpmCore5min")

                self.cpmcore5sec = YLeaf(YType.uint32, "cpmCore5sec")

                self.cpmcoreloadavg15min = YLeaf(YType.uint32, "cpmCoreLoadAvg15min")

                self.cpmcoreloadavg1min = YLeaf(YType.uint32, "cpmCoreLoadAvg1min")

                self.cpmcoreloadavg5min = YLeaf(YType.uint32, "cpmCoreLoadAvg5min")

                self.cpmcorephysicalindex = YLeaf(YType.int32, "cpmCorePhysicalIndex")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmcoreindex",
                                "cpmcore1min",
                                "cpmcore5min",
                                "cpmcore5sec",
                                "cpmcoreloadavg15min",
                                "cpmcoreloadavg1min",
                                "cpmcoreloadavg5min",
                                "cpmcorephysicalindex") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmcoretable.Cpmcoreentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmcoretable.Cpmcoreentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmcoreindex.is_set or
                    self.cpmcore1min.is_set or
                    self.cpmcore5min.is_set or
                    self.cpmcore5sec.is_set or
                    self.cpmcoreloadavg15min.is_set or
                    self.cpmcoreloadavg1min.is_set or
                    self.cpmcoreloadavg5min.is_set or
                    self.cpmcorephysicalindex.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmcoreindex.yfilter != YFilter.not_set or
                    self.cpmcore1min.yfilter != YFilter.not_set or
                    self.cpmcore5min.yfilter != YFilter.not_set or
                    self.cpmcore5sec.yfilter != YFilter.not_set or
                    self.cpmcoreloadavg15min.yfilter != YFilter.not_set or
                    self.cpmcoreloadavg1min.yfilter != YFilter.not_set or
                    self.cpmcoreloadavg5min.yfilter != YFilter.not_set or
                    self.cpmcorephysicalindex.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmCoreEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCoreIndex='" + self.cpmcoreindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCoreTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmcoreindex.is_set or self.cpmcoreindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcoreindex.get_name_leafdata())
                if (self.cpmcore1min.is_set or self.cpmcore1min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcore1min.get_name_leafdata())
                if (self.cpmcore5min.is_set or self.cpmcore5min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcore5min.get_name_leafdata())
                if (self.cpmcore5sec.is_set or self.cpmcore5sec.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcore5sec.get_name_leafdata())
                if (self.cpmcoreloadavg15min.is_set or self.cpmcoreloadavg15min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcoreloadavg15min.get_name_leafdata())
                if (self.cpmcoreloadavg1min.is_set or self.cpmcoreloadavg1min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcoreloadavg1min.get_name_leafdata())
                if (self.cpmcoreloadavg5min.is_set or self.cpmcoreloadavg5min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcoreloadavg5min.get_name_leafdata())
                if (self.cpmcorephysicalindex.is_set or self.cpmcorephysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcorephysicalindex.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmCoreIndex" or name == "cpmCore1min" or name == "cpmCore5min" or name == "cpmCore5sec" or name == "cpmCoreLoadAvg15min" or name == "cpmCoreLoadAvg1min" or name == "cpmCoreLoadAvg5min" or name == "cpmCorePhysicalIndex"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCoreIndex"):
                    self.cpmcoreindex = value
                    self.cpmcoreindex.value_namespace = name_space
                    self.cpmcoreindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCore1min"):
                    self.cpmcore1min = value
                    self.cpmcore1min.value_namespace = name_space
                    self.cpmcore1min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCore5min"):
                    self.cpmcore5min = value
                    self.cpmcore5min.value_namespace = name_space
                    self.cpmcore5min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCore5sec"):
                    self.cpmcore5sec = value
                    self.cpmcore5sec.value_namespace = name_space
                    self.cpmcore5sec.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCoreLoadAvg15min"):
                    self.cpmcoreloadavg15min = value
                    self.cpmcoreloadavg15min.value_namespace = name_space
                    self.cpmcoreloadavg15min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCoreLoadAvg1min"):
                    self.cpmcoreloadavg1min = value
                    self.cpmcoreloadavg1min.value_namespace = name_space
                    self.cpmcoreloadavg1min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCoreLoadAvg5min"):
                    self.cpmcoreloadavg5min = value
                    self.cpmcoreloadavg5min.value_namespace = name_space
                    self.cpmcoreloadavg5min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCorePhysicalIndex"):
                    self.cpmcorephysicalindex = value
                    self.cpmcorephysicalindex.value_namespace = name_space
                    self.cpmcorephysicalindex.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmcoreentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmcoreentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmCoreTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmCoreEntry"):
                for c in self.cpmcoreentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmcoretable.Cpmcoreentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmcoreentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmCoreEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmprocesstable(Entity):
        """
        A table of generic information on all active
        processes on this device.
        
        .. attribute:: cpmprocessentry
        
        	Generic information about an active process on this device. Entries in this table come and go as processes are  created and destroyed by the device
        	**type**\: list of    :py:class:`Cpmprocessentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocesstable.Cpmprocessentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmprocesstable, self).__init__()

            self.yang_name = "cpmProcessTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmprocessentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmprocesstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmprocesstable, self).__setattr__(name, value)


        class Cpmprocessentry(Entity):
            """
            Generic information about an active process on this
            device. Entries in this table come and go as processes are 
            created and destroyed by the device.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
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
            	**type**\:   :py:class:`Cpmprocextpriority <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocesstable.Cpmprocessentry.Cpmprocextpriority>`
            
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
                super(CiscoProcessMib.Cpmprocesstable.Cpmprocessentry, self).__init__()

                self.yang_name = "cpmProcessEntry"
                self.yang_parent_name = "cpmProcessTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmprocesspid",
                                "cpmprocessaverageusecs",
                                "cpmprocessname",
                                "cpmprocesstimecreated",
                                "cpmprocessusecs",
                                "cpmprocextinvoked",
                                "cpmprocextmemallocated",
                                "cpmprocextmemfreed",
                                "cpmprocextpriority",
                                "cpmprocextruntime",
                                "cpmprocextutil1min",
                                "cpmprocextutil5min",
                                "cpmprocextutil5sec") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmprocesstable.Cpmprocessentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmprocesstable.Cpmprocessentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmprocesspid.is_set or
                    self.cpmprocessaverageusecs.is_set or
                    self.cpmprocessname.is_set or
                    self.cpmprocesstimecreated.is_set or
                    self.cpmprocessusecs.is_set or
                    self.cpmprocextinvoked.is_set or
                    self.cpmprocextmemallocated.is_set or
                    self.cpmprocextmemfreed.is_set or
                    self.cpmprocextpriority.is_set or
                    self.cpmprocextruntime.is_set or
                    self.cpmprocextutil1min.is_set or
                    self.cpmprocextutil5min.is_set or
                    self.cpmprocextutil5sec.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmprocesspid.yfilter != YFilter.not_set or
                    self.cpmprocessaverageusecs.yfilter != YFilter.not_set or
                    self.cpmprocessname.yfilter != YFilter.not_set or
                    self.cpmprocesstimecreated.yfilter != YFilter.not_set or
                    self.cpmprocessusecs.yfilter != YFilter.not_set or
                    self.cpmprocextinvoked.yfilter != YFilter.not_set or
                    self.cpmprocextmemallocated.yfilter != YFilter.not_set or
                    self.cpmprocextmemfreed.yfilter != YFilter.not_set or
                    self.cpmprocextpriority.yfilter != YFilter.not_set or
                    self.cpmprocextruntime.yfilter != YFilter.not_set or
                    self.cpmprocextutil1min.yfilter != YFilter.not_set or
                    self.cpmprocextutil5min.yfilter != YFilter.not_set or
                    self.cpmprocextutil5sec.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmProcessEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmProcessTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmprocesspid.is_set or self.cpmprocesspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesspid.get_name_leafdata())
                if (self.cpmprocessaverageusecs.is_set or self.cpmprocessaverageusecs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessaverageusecs.get_name_leafdata())
                if (self.cpmprocessname.is_set or self.cpmprocessname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessname.get_name_leafdata())
                if (self.cpmprocesstimecreated.is_set or self.cpmprocesstimecreated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesstimecreated.get_name_leafdata())
                if (self.cpmprocessusecs.is_set or self.cpmprocessusecs.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessusecs.get_name_leafdata())
                if (self.cpmprocextinvoked.is_set or self.cpmprocextinvoked.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextinvoked.get_name_leafdata())
                if (self.cpmprocextmemallocated.is_set or self.cpmprocextmemallocated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextmemallocated.get_name_leafdata())
                if (self.cpmprocextmemfreed.is_set or self.cpmprocextmemfreed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextmemfreed.get_name_leafdata())
                if (self.cpmprocextpriority.is_set or self.cpmprocextpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextpriority.get_name_leafdata())
                if (self.cpmprocextruntime.is_set or self.cpmprocextruntime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextruntime.get_name_leafdata())
                if (self.cpmprocextutil1min.is_set or self.cpmprocextutil1min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextutil1min.get_name_leafdata())
                if (self.cpmprocextutil5min.is_set or self.cpmprocextutil5min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextutil5min.get_name_leafdata())
                if (self.cpmprocextutil5sec.is_set or self.cpmprocextutil5sec.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextutil5sec.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmProcessPID" or name == "cpmProcessAverageUSecs" or name == "cpmProcessName" or name == "cpmProcessTimeCreated" or name == "cpmProcessuSecs" or name == "cpmProcExtInvoked" or name == "cpmProcExtMemAllocated" or name == "cpmProcExtMemFreed" or name == "cpmProcExtPriority" or name == "cpmProcExtRuntime" or name == "cpmProcExtUtil1Min" or name == "cpmProcExtUtil5Min" or name == "cpmProcExtUtil5Sec"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessPID"):
                    self.cpmprocesspid = value
                    self.cpmprocesspid.value_namespace = name_space
                    self.cpmprocesspid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessAverageUSecs"):
                    self.cpmprocessaverageusecs = value
                    self.cpmprocessaverageusecs.value_namespace = name_space
                    self.cpmprocessaverageusecs.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessName"):
                    self.cpmprocessname = value
                    self.cpmprocessname.value_namespace = name_space
                    self.cpmprocessname.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessTimeCreated"):
                    self.cpmprocesstimecreated = value
                    self.cpmprocesstimecreated.value_namespace = name_space
                    self.cpmprocesstimecreated.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessuSecs"):
                    self.cpmprocessusecs = value
                    self.cpmprocessusecs.value_namespace = name_space
                    self.cpmprocessusecs.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtInvoked"):
                    self.cpmprocextinvoked = value
                    self.cpmprocextinvoked.value_namespace = name_space
                    self.cpmprocextinvoked.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtMemAllocated"):
                    self.cpmprocextmemallocated = value
                    self.cpmprocextmemallocated.value_namespace = name_space
                    self.cpmprocextmemallocated.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtMemFreed"):
                    self.cpmprocextmemfreed = value
                    self.cpmprocextmemfreed.value_namespace = name_space
                    self.cpmprocextmemfreed.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtPriority"):
                    self.cpmprocextpriority = value
                    self.cpmprocextpriority.value_namespace = name_space
                    self.cpmprocextpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtRuntime"):
                    self.cpmprocextruntime = value
                    self.cpmprocextruntime.value_namespace = name_space
                    self.cpmprocextruntime.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtUtil1Min"):
                    self.cpmprocextutil1min = value
                    self.cpmprocextutil1min.value_namespace = name_space
                    self.cpmprocextutil1min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtUtil5Min"):
                    self.cpmprocextutil5min = value
                    self.cpmprocextutil5min.value_namespace = name_space
                    self.cpmprocextutil5min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtUtil5Sec"):
                    self.cpmprocextutil5sec = value
                    self.cpmprocextutil5sec.value_namespace = name_space
                    self.cpmprocextutil5sec.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmprocessentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmprocessentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmProcessTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmProcessEntry"):
                for c in self.cpmprocessentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmprocesstable.Cpmprocessentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmprocessentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmProcessEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmprocessextrevtable(Entity):
        """
        This table contains information that may or may
        not be available on all cisco devices. It contains
        additional objects for the more general
        cpmProcessTable. This object deprecates 
        cpmProcessExtTable.
        
        .. attribute:: cpmprocessextreventry
        
        	An entry containing additional information for a particular process. This object deprecates  cpmProcessExtEntry
        	**type**\: list of    :py:class:`Cpmprocessextreventry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmprocessextrevtable, self).__init__()

            self.yang_name = "cpmProcessExtRevTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmprocessextreventry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmprocessextrevtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmprocessextrevtable, self).__setattr__(name, value)


        class Cpmprocessextreventry(Entity):
            """
            An entry containing additional information for
            a particular process. This object deprecates 
            cpmProcessExtEntry.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmprocesspid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocesstable.Cpmprocessentry>`
            
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
            	**type**\:   :py:class:`Cpmprocessmemorycore <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry.Cpmprocessmemorycore>`
            
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
            	**type**\:   :py:class:`Cpmprocesstype <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry.Cpmprocesstype>`
            
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
            	**type**\:   :py:class:`Cpmprocextpriorityrev <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry.Cpmprocextpriorityrev>`
            
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
                super(CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry, self).__init__()

                self.yang_name = "cpmProcessExtRevEntry"
                self.yang_parent_name = "cpmProcessExtRevTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmprocesspid",
                                "cpmprocessdatasegmentsize",
                                "cpmprocessdatasegmentsizeovrflw",
                                "cpmprocessdynamicmemorysize",
                                "cpmprocessdynamicmemorysizeovrflw",
                                "cpmprocesshcdatasegmentsize",
                                "cpmprocesshcdynamicmemorysize",
                                "cpmprocesshcstacksize",
                                "cpmprocesshctextsegmentsize",
                                "cpmprocesslastrestartuser",
                                "cpmprocessmemorycore",
                                "cpmprocessrespawn",
                                "cpmprocessrespawnafterlastpatch",
                                "cpmprocessrespawncount",
                                "cpmprocessstacksize",
                                "cpmprocessstacksizeovrflw",
                                "cpmprocesstextsegmentsize",
                                "cpmprocesstextsegmentsizeovrflw",
                                "cpmprocesstype",
                                "cpmprocexthcmemallocatedrev",
                                "cpmprocexthcmemfreedrev",
                                "cpmprocextinvokedrev",
                                "cpmprocextmemallocatedrev",
                                "cpmprocextmemallocatedrevovrflw",
                                "cpmprocextmemfreedrev",
                                "cpmprocextmemfreedrevovrflw",
                                "cpmprocextpriorityrev",
                                "cpmprocextruntimerev",
                                "cpmprocextutil1minrev",
                                "cpmprocextutil5minrev",
                                "cpmprocextutil5secrev") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmprocesspid.is_set or
                    self.cpmprocessdatasegmentsize.is_set or
                    self.cpmprocessdatasegmentsizeovrflw.is_set or
                    self.cpmprocessdynamicmemorysize.is_set or
                    self.cpmprocessdynamicmemorysizeovrflw.is_set or
                    self.cpmprocesshcdatasegmentsize.is_set or
                    self.cpmprocesshcdynamicmemorysize.is_set or
                    self.cpmprocesshcstacksize.is_set or
                    self.cpmprocesshctextsegmentsize.is_set or
                    self.cpmprocesslastrestartuser.is_set or
                    self.cpmprocessmemorycore.is_set or
                    self.cpmprocessrespawn.is_set or
                    self.cpmprocessrespawnafterlastpatch.is_set or
                    self.cpmprocessrespawncount.is_set or
                    self.cpmprocessstacksize.is_set or
                    self.cpmprocessstacksizeovrflw.is_set or
                    self.cpmprocesstextsegmentsize.is_set or
                    self.cpmprocesstextsegmentsizeovrflw.is_set or
                    self.cpmprocesstype.is_set or
                    self.cpmprocexthcmemallocatedrev.is_set or
                    self.cpmprocexthcmemfreedrev.is_set or
                    self.cpmprocextinvokedrev.is_set or
                    self.cpmprocextmemallocatedrev.is_set or
                    self.cpmprocextmemallocatedrevovrflw.is_set or
                    self.cpmprocextmemfreedrev.is_set or
                    self.cpmprocextmemfreedrevovrflw.is_set or
                    self.cpmprocextpriorityrev.is_set or
                    self.cpmprocextruntimerev.is_set or
                    self.cpmprocextutil1minrev.is_set or
                    self.cpmprocextutil5minrev.is_set or
                    self.cpmprocextutil5secrev.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmprocesspid.yfilter != YFilter.not_set or
                    self.cpmprocessdatasegmentsize.yfilter != YFilter.not_set or
                    self.cpmprocessdatasegmentsizeovrflw.yfilter != YFilter.not_set or
                    self.cpmprocessdynamicmemorysize.yfilter != YFilter.not_set or
                    self.cpmprocessdynamicmemorysizeovrflw.yfilter != YFilter.not_set or
                    self.cpmprocesshcdatasegmentsize.yfilter != YFilter.not_set or
                    self.cpmprocesshcdynamicmemorysize.yfilter != YFilter.not_set or
                    self.cpmprocesshcstacksize.yfilter != YFilter.not_set or
                    self.cpmprocesshctextsegmentsize.yfilter != YFilter.not_set or
                    self.cpmprocesslastrestartuser.yfilter != YFilter.not_set or
                    self.cpmprocessmemorycore.yfilter != YFilter.not_set or
                    self.cpmprocessrespawn.yfilter != YFilter.not_set or
                    self.cpmprocessrespawnafterlastpatch.yfilter != YFilter.not_set or
                    self.cpmprocessrespawncount.yfilter != YFilter.not_set or
                    self.cpmprocessstacksize.yfilter != YFilter.not_set or
                    self.cpmprocessstacksizeovrflw.yfilter != YFilter.not_set or
                    self.cpmprocesstextsegmentsize.yfilter != YFilter.not_set or
                    self.cpmprocesstextsegmentsizeovrflw.yfilter != YFilter.not_set or
                    self.cpmprocesstype.yfilter != YFilter.not_set or
                    self.cpmprocexthcmemallocatedrev.yfilter != YFilter.not_set or
                    self.cpmprocexthcmemfreedrev.yfilter != YFilter.not_set or
                    self.cpmprocextinvokedrev.yfilter != YFilter.not_set or
                    self.cpmprocextmemallocatedrev.yfilter != YFilter.not_set or
                    self.cpmprocextmemallocatedrevovrflw.yfilter != YFilter.not_set or
                    self.cpmprocextmemfreedrev.yfilter != YFilter.not_set or
                    self.cpmprocextmemfreedrevovrflw.yfilter != YFilter.not_set or
                    self.cpmprocextpriorityrev.yfilter != YFilter.not_set or
                    self.cpmprocextruntimerev.yfilter != YFilter.not_set or
                    self.cpmprocextutil1minrev.yfilter != YFilter.not_set or
                    self.cpmprocextutil5minrev.yfilter != YFilter.not_set or
                    self.cpmprocextutil5secrev.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmProcessExtRevEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmProcessExtRevTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmprocesspid.is_set or self.cpmprocesspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesspid.get_name_leafdata())
                if (self.cpmprocessdatasegmentsize.is_set or self.cpmprocessdatasegmentsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessdatasegmentsize.get_name_leafdata())
                if (self.cpmprocessdatasegmentsizeovrflw.is_set or self.cpmprocessdatasegmentsizeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessdatasegmentsizeovrflw.get_name_leafdata())
                if (self.cpmprocessdynamicmemorysize.is_set or self.cpmprocessdynamicmemorysize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessdynamicmemorysize.get_name_leafdata())
                if (self.cpmprocessdynamicmemorysizeovrflw.is_set or self.cpmprocessdynamicmemorysizeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessdynamicmemorysizeovrflw.get_name_leafdata())
                if (self.cpmprocesshcdatasegmentsize.is_set or self.cpmprocesshcdatasegmentsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesshcdatasegmentsize.get_name_leafdata())
                if (self.cpmprocesshcdynamicmemorysize.is_set or self.cpmprocesshcdynamicmemorysize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesshcdynamicmemorysize.get_name_leafdata())
                if (self.cpmprocesshcstacksize.is_set or self.cpmprocesshcstacksize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesshcstacksize.get_name_leafdata())
                if (self.cpmprocesshctextsegmentsize.is_set or self.cpmprocesshctextsegmentsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesshctextsegmentsize.get_name_leafdata())
                if (self.cpmprocesslastrestartuser.is_set or self.cpmprocesslastrestartuser.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesslastrestartuser.get_name_leafdata())
                if (self.cpmprocessmemorycore.is_set or self.cpmprocessmemorycore.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessmemorycore.get_name_leafdata())
                if (self.cpmprocessrespawn.is_set or self.cpmprocessrespawn.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessrespawn.get_name_leafdata())
                if (self.cpmprocessrespawnafterlastpatch.is_set or self.cpmprocessrespawnafterlastpatch.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessrespawnafterlastpatch.get_name_leafdata())
                if (self.cpmprocessrespawncount.is_set or self.cpmprocessrespawncount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessrespawncount.get_name_leafdata())
                if (self.cpmprocessstacksize.is_set or self.cpmprocessstacksize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessstacksize.get_name_leafdata())
                if (self.cpmprocessstacksizeovrflw.is_set or self.cpmprocessstacksizeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocessstacksizeovrflw.get_name_leafdata())
                if (self.cpmprocesstextsegmentsize.is_set or self.cpmprocesstextsegmentsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesstextsegmentsize.get_name_leafdata())
                if (self.cpmprocesstextsegmentsizeovrflw.is_set or self.cpmprocesstextsegmentsizeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesstextsegmentsizeovrflw.get_name_leafdata())
                if (self.cpmprocesstype.is_set or self.cpmprocesstype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesstype.get_name_leafdata())
                if (self.cpmprocexthcmemallocatedrev.is_set or self.cpmprocexthcmemallocatedrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocexthcmemallocatedrev.get_name_leafdata())
                if (self.cpmprocexthcmemfreedrev.is_set or self.cpmprocexthcmemfreedrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocexthcmemfreedrev.get_name_leafdata())
                if (self.cpmprocextinvokedrev.is_set or self.cpmprocextinvokedrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextinvokedrev.get_name_leafdata())
                if (self.cpmprocextmemallocatedrev.is_set or self.cpmprocextmemallocatedrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextmemallocatedrev.get_name_leafdata())
                if (self.cpmprocextmemallocatedrevovrflw.is_set or self.cpmprocextmemallocatedrevovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextmemallocatedrevovrflw.get_name_leafdata())
                if (self.cpmprocextmemfreedrev.is_set or self.cpmprocextmemfreedrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextmemfreedrev.get_name_leafdata())
                if (self.cpmprocextmemfreedrevovrflw.is_set or self.cpmprocextmemfreedrevovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextmemfreedrevovrflw.get_name_leafdata())
                if (self.cpmprocextpriorityrev.is_set or self.cpmprocextpriorityrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextpriorityrev.get_name_leafdata())
                if (self.cpmprocextruntimerev.is_set or self.cpmprocextruntimerev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextruntimerev.get_name_leafdata())
                if (self.cpmprocextutil1minrev.is_set or self.cpmprocextutil1minrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextutil1minrev.get_name_leafdata())
                if (self.cpmprocextutil5minrev.is_set or self.cpmprocextutil5minrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextutil5minrev.get_name_leafdata())
                if (self.cpmprocextutil5secrev.is_set or self.cpmprocextutil5secrev.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocextutil5secrev.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmProcessPID" or name == "cpmProcessDataSegmentSize" or name == "cpmProcessDataSegmentSizeOvrflw" or name == "cpmProcessDynamicMemorySize" or name == "cpmProcessDynamicMemorySizeOvrflw" or name == "cpmProcessHCDataSegmentSize" or name == "cpmProcessHCDynamicMemorySize" or name == "cpmProcessHCStackSize" or name == "cpmProcessHCTextSegmentSize" or name == "cpmProcessLastRestartUser" or name == "cpmProcessMemoryCore" or name == "cpmProcessRespawn" or name == "cpmProcessRespawnAfterLastPatch" or name == "cpmProcessRespawnCount" or name == "cpmProcessStackSize" or name == "cpmProcessStackSizeOvrflw" or name == "cpmProcessTextSegmentSize" or name == "cpmProcessTextSegmentSizeOvrflw" or name == "cpmProcessType" or name == "cpmProcExtHCMemAllocatedRev" or name == "cpmProcExtHCMemFreedRev" or name == "cpmProcExtInvokedRev" or name == "cpmProcExtMemAllocatedRev" or name == "cpmProcExtMemAllocatedRevOvrflw" or name == "cpmProcExtMemFreedRev" or name == "cpmProcExtMemFreedRevOvrflw" or name == "cpmProcExtPriorityRev" or name == "cpmProcExtRuntimeRev" or name == "cpmProcExtUtil1MinRev" or name == "cpmProcExtUtil5MinRev" or name == "cpmProcExtUtil5SecRev"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessPID"):
                    self.cpmprocesspid = value
                    self.cpmprocesspid.value_namespace = name_space
                    self.cpmprocesspid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessDataSegmentSize"):
                    self.cpmprocessdatasegmentsize = value
                    self.cpmprocessdatasegmentsize.value_namespace = name_space
                    self.cpmprocessdatasegmentsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessDataSegmentSizeOvrflw"):
                    self.cpmprocessdatasegmentsizeovrflw = value
                    self.cpmprocessdatasegmentsizeovrflw.value_namespace = name_space
                    self.cpmprocessdatasegmentsizeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessDynamicMemorySize"):
                    self.cpmprocessdynamicmemorysize = value
                    self.cpmprocessdynamicmemorysize.value_namespace = name_space
                    self.cpmprocessdynamicmemorysize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessDynamicMemorySizeOvrflw"):
                    self.cpmprocessdynamicmemorysizeovrflw = value
                    self.cpmprocessdynamicmemorysizeovrflw.value_namespace = name_space
                    self.cpmprocessdynamicmemorysizeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessHCDataSegmentSize"):
                    self.cpmprocesshcdatasegmentsize = value
                    self.cpmprocesshcdatasegmentsize.value_namespace = name_space
                    self.cpmprocesshcdatasegmentsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessHCDynamicMemorySize"):
                    self.cpmprocesshcdynamicmemorysize = value
                    self.cpmprocesshcdynamicmemorysize.value_namespace = name_space
                    self.cpmprocesshcdynamicmemorysize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessHCStackSize"):
                    self.cpmprocesshcstacksize = value
                    self.cpmprocesshcstacksize.value_namespace = name_space
                    self.cpmprocesshcstacksize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessHCTextSegmentSize"):
                    self.cpmprocesshctextsegmentsize = value
                    self.cpmprocesshctextsegmentsize.value_namespace = name_space
                    self.cpmprocesshctextsegmentsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessLastRestartUser"):
                    self.cpmprocesslastrestartuser = value
                    self.cpmprocesslastrestartuser.value_namespace = name_space
                    self.cpmprocesslastrestartuser.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessMemoryCore"):
                    self.cpmprocessmemorycore = value
                    self.cpmprocessmemorycore.value_namespace = name_space
                    self.cpmprocessmemorycore.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessRespawn"):
                    self.cpmprocessrespawn = value
                    self.cpmprocessrespawn.value_namespace = name_space
                    self.cpmprocessrespawn.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessRespawnAfterLastPatch"):
                    self.cpmprocessrespawnafterlastpatch = value
                    self.cpmprocessrespawnafterlastpatch.value_namespace = name_space
                    self.cpmprocessrespawnafterlastpatch.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessRespawnCount"):
                    self.cpmprocessrespawncount = value
                    self.cpmprocessrespawncount.value_namespace = name_space
                    self.cpmprocessrespawncount.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessStackSize"):
                    self.cpmprocessstacksize = value
                    self.cpmprocessstacksize.value_namespace = name_space
                    self.cpmprocessstacksize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessStackSizeOvrflw"):
                    self.cpmprocessstacksizeovrflw = value
                    self.cpmprocessstacksizeovrflw.value_namespace = name_space
                    self.cpmprocessstacksizeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessTextSegmentSize"):
                    self.cpmprocesstextsegmentsize = value
                    self.cpmprocesstextsegmentsize.value_namespace = name_space
                    self.cpmprocesstextsegmentsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessTextSegmentSizeOvrflw"):
                    self.cpmprocesstextsegmentsizeovrflw = value
                    self.cpmprocesstextsegmentsizeovrflw.value_namespace = name_space
                    self.cpmprocesstextsegmentsizeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessType"):
                    self.cpmprocesstype = value
                    self.cpmprocesstype.value_namespace = name_space
                    self.cpmprocesstype.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtHCMemAllocatedRev"):
                    self.cpmprocexthcmemallocatedrev = value
                    self.cpmprocexthcmemallocatedrev.value_namespace = name_space
                    self.cpmprocexthcmemallocatedrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtHCMemFreedRev"):
                    self.cpmprocexthcmemfreedrev = value
                    self.cpmprocexthcmemfreedrev.value_namespace = name_space
                    self.cpmprocexthcmemfreedrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtInvokedRev"):
                    self.cpmprocextinvokedrev = value
                    self.cpmprocextinvokedrev.value_namespace = name_space
                    self.cpmprocextinvokedrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtMemAllocatedRev"):
                    self.cpmprocextmemallocatedrev = value
                    self.cpmprocextmemallocatedrev.value_namespace = name_space
                    self.cpmprocextmemallocatedrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtMemAllocatedRevOvrflw"):
                    self.cpmprocextmemallocatedrevovrflw = value
                    self.cpmprocextmemallocatedrevovrflw.value_namespace = name_space
                    self.cpmprocextmemallocatedrevovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtMemFreedRev"):
                    self.cpmprocextmemfreedrev = value
                    self.cpmprocextmemfreedrev.value_namespace = name_space
                    self.cpmprocextmemfreedrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtMemFreedRevOvrflw"):
                    self.cpmprocextmemfreedrevovrflw = value
                    self.cpmprocextmemfreedrevovrflw.value_namespace = name_space
                    self.cpmprocextmemfreedrevovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtPriorityRev"):
                    self.cpmprocextpriorityrev = value
                    self.cpmprocextpriorityrev.value_namespace = name_space
                    self.cpmprocextpriorityrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtRuntimeRev"):
                    self.cpmprocextruntimerev = value
                    self.cpmprocextruntimerev.value_namespace = name_space
                    self.cpmprocextruntimerev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtUtil1MinRev"):
                    self.cpmprocextutil1minrev = value
                    self.cpmprocextutil1minrev.value_namespace = name_space
                    self.cpmprocextutil1minrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtUtil5MinRev"):
                    self.cpmprocextutil5minrev = value
                    self.cpmprocextutil5minrev.value_namespace = name_space
                    self.cpmprocextutil5minrev.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcExtUtil5SecRev"):
                    self.cpmprocextutil5secrev = value
                    self.cpmprocextutil5secrev.value_namespace = name_space
                    self.cpmprocextutil5secrev.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmprocessextreventry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmprocessextreventry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmProcessExtRevTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmProcessExtRevEntry"):
                for c in self.cpmprocessextreventry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmprocessextrevtable.Cpmprocessextreventry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmprocessextreventry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmProcessExtRevEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmcputhresholdtable(Entity):
        """
        This table contains the information about the
        thresholding values for CPU , configured by the user.
        
        .. attribute:: cpmcputhresholdentry
        
        	An entry containing information about CPU thresholding parameters. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this configuration applies
        	**type**\: list of    :py:class:`Cpmcputhresholdentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputhresholdtable.Cpmcputhresholdentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmcputhresholdtable, self).__init__()

            self.yang_name = "cpmCPUThresholdTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmcputhresholdentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmcputhresholdtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmcputhresholdtable, self).__setattr__(name, value)


        class Cpmcputhresholdentry(Entity):
            """
            An entry containing information about
            CPU thresholding parameters. cpmCPUTotalIndex
            identifies the CPU (or group of CPUs) for which this
            configuration applies.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmcputhresholdclass  <key>
            
            	Value of this object indicates the type of utilization, which is monitored. The total(1) indicates the total CPU utilization, interrupt(2) indicates the the CPU utilization in interrupt context and process(3) indicates the CPU utilization in the process level execution context
            	**type**\:   :py:class:`Cpmcputhresholdclass <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputhresholdtable.Cpmcputhresholdentry.Cpmcputhresholdclass>`
            
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
            	**type**\:   :py:class:`Rowstatus <ydk.models.cisco_ios_xe.SNMPv2_TC.Rowstatus>`
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CiscoProcessMib.Cpmcputhresholdtable.Cpmcputhresholdentry, self).__init__()

                self.yang_name = "cpmCPUThresholdEntry"
                self.yang_parent_name = "cpmCPUThresholdTable"

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcputhresholdclass = YLeaf(YType.enumeration, "cpmCPUThresholdClass")

                self.cpmcpufallingthresholdperiod = YLeaf(YType.uint32, "cpmCPUFallingThresholdPeriod")

                self.cpmcpufallingthresholdvalue = YLeaf(YType.uint32, "cpmCPUFallingThresholdValue")

                self.cpmcpurisingthresholdperiod = YLeaf(YType.uint32, "cpmCPURisingThresholdPeriod")

                self.cpmcpurisingthresholdvalue = YLeaf(YType.uint32, "cpmCPURisingThresholdValue")

                self.cpmcputhresholdentrystatus = YLeaf(YType.enumeration, "cpmCPUThresholdEntryStatus")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmcputhresholdclass",
                                "cpmcpufallingthresholdperiod",
                                "cpmcpufallingthresholdvalue",
                                "cpmcpurisingthresholdperiod",
                                "cpmcpurisingthresholdvalue",
                                "cpmcputhresholdentrystatus") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmcputhresholdtable.Cpmcputhresholdentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmcputhresholdtable.Cpmcputhresholdentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmcputhresholdclass.is_set or
                    self.cpmcpufallingthresholdperiod.is_set or
                    self.cpmcpufallingthresholdvalue.is_set or
                    self.cpmcpurisingthresholdperiod.is_set or
                    self.cpmcpurisingthresholdvalue.is_set or
                    self.cpmcputhresholdentrystatus.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmcputhresholdclass.yfilter != YFilter.not_set or
                    self.cpmcpufallingthresholdperiod.yfilter != YFilter.not_set or
                    self.cpmcpufallingthresholdvalue.yfilter != YFilter.not_set or
                    self.cpmcpurisingthresholdperiod.yfilter != YFilter.not_set or
                    self.cpmcpurisingthresholdvalue.yfilter != YFilter.not_set or
                    self.cpmcputhresholdentrystatus.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmCPUThresholdEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCPUThresholdClass='" + self.cpmcputhresholdclass.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUThresholdTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmcputhresholdclass.is_set or self.cpmcputhresholdclass.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputhresholdclass.get_name_leafdata())
                if (self.cpmcpufallingthresholdperiod.is_set or self.cpmcpufallingthresholdperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpufallingthresholdperiod.get_name_leafdata())
                if (self.cpmcpufallingthresholdvalue.is_set or self.cpmcpufallingthresholdvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpufallingthresholdvalue.get_name_leafdata())
                if (self.cpmcpurisingthresholdperiod.is_set or self.cpmcpurisingthresholdperiod.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpurisingthresholdperiod.get_name_leafdata())
                if (self.cpmcpurisingthresholdvalue.is_set or self.cpmcpurisingthresholdvalue.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpurisingthresholdvalue.get_name_leafdata())
                if (self.cpmcputhresholdentrystatus.is_set or self.cpmcputhresholdentrystatus.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputhresholdentrystatus.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmCPUThresholdClass" or name == "cpmCPUFallingThresholdPeriod" or name == "cpmCPUFallingThresholdValue" or name == "cpmCPURisingThresholdPeriod" or name == "cpmCPURisingThresholdValue" or name == "cpmCPUThresholdEntryStatus"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUThresholdClass"):
                    self.cpmcputhresholdclass = value
                    self.cpmcputhresholdclass.value_namespace = name_space
                    self.cpmcputhresholdclass.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUFallingThresholdPeriod"):
                    self.cpmcpufallingthresholdperiod = value
                    self.cpmcpufallingthresholdperiod.value_namespace = name_space
                    self.cpmcpufallingthresholdperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUFallingThresholdValue"):
                    self.cpmcpufallingthresholdvalue = value
                    self.cpmcpufallingthresholdvalue.value_namespace = name_space
                    self.cpmcpufallingthresholdvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPURisingThresholdPeriod"):
                    self.cpmcpurisingthresholdperiod = value
                    self.cpmcpurisingthresholdperiod.value_namespace = name_space
                    self.cpmcpurisingthresholdperiod.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPURisingThresholdValue"):
                    self.cpmcpurisingthresholdvalue = value
                    self.cpmcpurisingthresholdvalue.value_namespace = name_space
                    self.cpmcpurisingthresholdvalue.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUThresholdEntryStatus"):
                    self.cpmcputhresholdentrystatus = value
                    self.cpmcputhresholdentrystatus.value_namespace = name_space
                    self.cpmcputhresholdentrystatus.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmcputhresholdentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmcputhresholdentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmCPUThresholdTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmCPUThresholdEntry"):
                for c in self.cpmcputhresholdentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmcputhresholdtable.Cpmcputhresholdentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmcputhresholdentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmCPUThresholdEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmcpuhistorytable(Entity):
        """
        A list of CPU utilization history entries.
        
        .. attribute:: cpmcpuhistoryentry
        
        	A historical sample of CPU utilization statistics. cpmCPUTotalIndex identifies the CPU (or group of CPUs) for which this history is collected.  When the cpmCPUHistorySize is reached the least recent entry is lost
        	**type**\: list of    :py:class:`Cpmcpuhistoryentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcpuhistorytable.Cpmcpuhistoryentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmcpuhistorytable, self).__init__()

            self.yang_name = "cpmCPUHistoryTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmcpuhistoryentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmcpuhistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmcpuhistorytable, self).__setattr__(name, value)


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
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
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
                super(CiscoProcessMib.Cpmcpuhistorytable.Cpmcpuhistoryentry, self).__init__()

                self.yang_name = "cpmCPUHistoryEntry"
                self.yang_parent_name = "cpmCPUHistoryTable"

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcpuhistoryreportid = YLeaf(YType.uint32, "cpmCPUHistoryReportId")

                self.cpmcpuhistorycreatedtime = YLeaf(YType.uint32, "cpmCPUHistoryCreatedTime")

                self.cpmcpuhistoryinterruptutil = YLeaf(YType.uint32, "cpmCPUHistoryInterruptUtil")

                self.cpmcpuhistoryreportsize = YLeaf(YType.uint32, "cpmCPUHistoryReportSize")

                self.cpmcpuhistorytotalutil = YLeaf(YType.uint32, "cpmCPUHistoryTotalUtil")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmcpuhistoryreportid",
                                "cpmcpuhistorycreatedtime",
                                "cpmcpuhistoryinterruptutil",
                                "cpmcpuhistoryreportsize",
                                "cpmcpuhistorytotalutil") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmcpuhistorytable.Cpmcpuhistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmcpuhistorytable.Cpmcpuhistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmcpuhistoryreportid.is_set or
                    self.cpmcpuhistorycreatedtime.is_set or
                    self.cpmcpuhistoryinterruptutil.is_set or
                    self.cpmcpuhistoryreportsize.is_set or
                    self.cpmcpuhistorytotalutil.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryreportid.yfilter != YFilter.not_set or
                    self.cpmcpuhistorycreatedtime.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryinterruptutil.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryreportsize.yfilter != YFilter.not_set or
                    self.cpmcpuhistorytotalutil.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmCPUHistoryEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCPUHistoryReportId='" + self.cpmcpuhistoryreportid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmcpuhistoryreportid.is_set or self.cpmcpuhistoryreportid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryreportid.get_name_leafdata())
                if (self.cpmcpuhistorycreatedtime.is_set or self.cpmcpuhistorycreatedtime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistorycreatedtime.get_name_leafdata())
                if (self.cpmcpuhistoryinterruptutil.is_set or self.cpmcpuhistoryinterruptutil.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryinterruptutil.get_name_leafdata())
                if (self.cpmcpuhistoryreportsize.is_set or self.cpmcpuhistoryreportsize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryreportsize.get_name_leafdata())
                if (self.cpmcpuhistorytotalutil.is_set or self.cpmcpuhistorytotalutil.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistorytotalutil.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmCPUHistoryReportId" or name == "cpmCPUHistoryCreatedTime" or name == "cpmCPUHistoryInterruptUtil" or name == "cpmCPUHistoryReportSize" or name == "cpmCPUHistoryTotalUtil"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryReportId"):
                    self.cpmcpuhistoryreportid = value
                    self.cpmcpuhistoryreportid.value_namespace = name_space
                    self.cpmcpuhistoryreportid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryCreatedTime"):
                    self.cpmcpuhistorycreatedtime = value
                    self.cpmcpuhistorycreatedtime.value_namespace = name_space
                    self.cpmcpuhistorycreatedtime.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryInterruptUtil"):
                    self.cpmcpuhistoryinterruptutil = value
                    self.cpmcpuhistoryinterruptutil.value_namespace = name_space
                    self.cpmcpuhistoryinterruptutil.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryReportSize"):
                    self.cpmcpuhistoryreportsize = value
                    self.cpmcpuhistoryreportsize.value_namespace = name_space
                    self.cpmcpuhistoryreportsize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryTotalUtil"):
                    self.cpmcpuhistorytotalutil = value
                    self.cpmcpuhistorytotalutil.value_namespace = name_space
                    self.cpmcpuhistorytotalutil.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmcpuhistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmcpuhistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmCPUHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmCPUHistoryEntry"):
                for c in self.cpmcpuhistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmcpuhistorytable.Cpmcpuhistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmcpuhistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmCPUHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmcpuprocesshistorytable(Entity):
        """
        A list of process history entries. This table contains
        CPU utilization of processes which crossed the 
        cpmCPUHistoryThreshold.
        
        .. attribute:: cpmcpuprocesshistoryentry
        
        	A historical sample of process utilization statistics. The entries in this table will have corresponding entires in the cpmCPUHistoryTable. The entries in this table get deleted when the entry associated with this entry in the cpmCPUHistoryTable  gets deleted
        	**type**\: list of    :py:class:`Cpmcpuprocesshistoryentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmcpuprocesshistorytable, self).__init__()

            self.yang_name = "cpmCPUProcessHistoryTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmcpuprocesshistoryentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmcpuprocesshistorytable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmcpuprocesshistorytable, self).__setattr__(name, value)


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
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmcpuhistoryreportid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmcpuhistoryreportid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcpuhistorytable.Cpmcpuhistoryentry>`
            
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
                super(CiscoProcessMib.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry, self).__init__()

                self.yang_name = "cpmCPUProcessHistoryEntry"
                self.yang_parent_name = "cpmCPUProcessHistoryTable"

                self.cpmcputotalindex = YLeaf(YType.str, "cpmCPUTotalIndex")

                self.cpmcpuhistoryreportid = YLeaf(YType.str, "cpmCPUHistoryReportId")

                self.cpmcpuprocesshistoryindex = YLeaf(YType.uint32, "cpmCPUProcessHistoryIndex")

                self.cpmcpuhistoryproccreated = YLeaf(YType.uint32, "cpmCPUHistoryProcCreated")

                self.cpmcpuhistoryprocid = YLeaf(YType.uint32, "cpmCPUHistoryProcId")

                self.cpmcpuhistoryprocname = YLeaf(YType.str, "cpmCPUHistoryProcName")

                self.cpmcpuhistoryprocutil = YLeaf(YType.uint32, "cpmCPUHistoryProcUtil")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmcpuhistoryreportid",
                                "cpmcpuprocesshistoryindex",
                                "cpmcpuhistoryproccreated",
                                "cpmcpuhistoryprocid",
                                "cpmcpuhistoryprocname",
                                "cpmcpuhistoryprocutil") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmcpuhistoryreportid.is_set or
                    self.cpmcpuprocesshistoryindex.is_set or
                    self.cpmcpuhistoryproccreated.is_set or
                    self.cpmcpuhistoryprocid.is_set or
                    self.cpmcpuhistoryprocname.is_set or
                    self.cpmcpuhistoryprocutil.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryreportid.yfilter != YFilter.not_set or
                    self.cpmcpuprocesshistoryindex.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryproccreated.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryprocid.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryprocname.yfilter != YFilter.not_set or
                    self.cpmcpuhistoryprocutil.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmCPUProcessHistoryEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmCPUHistoryReportId='" + self.cpmcpuhistoryreportid.get() + "']" + "[cpmCPUProcessHistoryIndex='" + self.cpmcpuprocesshistoryindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmCPUProcessHistoryTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmcpuhistoryreportid.is_set or self.cpmcpuhistoryreportid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryreportid.get_name_leafdata())
                if (self.cpmcpuprocesshistoryindex.is_set or self.cpmcpuprocesshistoryindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuprocesshistoryindex.get_name_leafdata())
                if (self.cpmcpuhistoryproccreated.is_set or self.cpmcpuhistoryproccreated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryproccreated.get_name_leafdata())
                if (self.cpmcpuhistoryprocid.is_set or self.cpmcpuhistoryprocid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryprocid.get_name_leafdata())
                if (self.cpmcpuhistoryprocname.is_set or self.cpmcpuhistoryprocname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryprocname.get_name_leafdata())
                if (self.cpmcpuhistoryprocutil.is_set or self.cpmcpuhistoryprocutil.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcpuhistoryprocutil.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmCPUHistoryReportId" or name == "cpmCPUProcessHistoryIndex" or name == "cpmCPUHistoryProcCreated" or name == "cpmCPUHistoryProcId" or name == "cpmCPUHistoryProcName" or name == "cpmCPUHistoryProcUtil"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryReportId"):
                    self.cpmcpuhistoryreportid = value
                    self.cpmcpuhistoryreportid.value_namespace = name_space
                    self.cpmcpuhistoryreportid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUProcessHistoryIndex"):
                    self.cpmcpuprocesshistoryindex = value
                    self.cpmcpuprocesshistoryindex.value_namespace = name_space
                    self.cpmcpuprocesshistoryindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryProcCreated"):
                    self.cpmcpuhistoryproccreated = value
                    self.cpmcpuhistoryproccreated.value_namespace = name_space
                    self.cpmcpuhistoryproccreated.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryProcId"):
                    self.cpmcpuhistoryprocid = value
                    self.cpmcpuhistoryprocid.value_namespace = name_space
                    self.cpmcpuhistoryprocid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryProcName"):
                    self.cpmcpuhistoryprocname = value
                    self.cpmcpuhistoryprocname.value_namespace = name_space
                    self.cpmcpuhistoryprocname.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmCPUHistoryProcUtil"):
                    self.cpmcpuhistoryprocutil = value
                    self.cpmcpuhistoryprocutil.value_namespace = name_space
                    self.cpmcpuhistoryprocutil.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmcpuprocesshistoryentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmcpuprocesshistoryentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmCPUProcessHistoryTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmCPUProcessHistoryEntry"):
                for c in self.cpmcpuprocesshistoryentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmcpuprocesshistorytable.Cpmcpuprocesshistoryentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmcpuprocesshistoryentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmCPUProcessHistoryEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmthreadtable(Entity):
        """
        This table contains generic information about
        POSIX threads in the device.
        
        .. attribute:: cpmthreadentry
        
        	An entry containing the general statistics of a POSIX thread
        	**type**\: list of    :py:class:`Cpmthreadentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmthreadtable.Cpmthreadentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmthreadtable, self).__init__()

            self.yang_name = "cpmThreadTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmthreadentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmthreadtable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmthreadtable, self).__setattr__(name, value)


        class Cpmthreadentry(Entity):
            """
            An entry containing the general statistics
            of a POSIX thread.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmprocesspid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocesstable.Cpmprocessentry>`
            
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
            	**type**\:   :py:class:`Cpmthreadstate <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmthreadtable.Cpmthreadentry.Cpmthreadstate>`
            
            

            """

            _prefix = 'CISCO-PROCESS-MIB'
            _revision = '2011-06-23'

            def __init__(self):
                super(CiscoProcessMib.Cpmthreadtable.Cpmthreadentry, self).__init__()

                self.yang_name = "cpmThreadEntry"
                self.yang_parent_name = "cpmThreadTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmprocesspid",
                                "cpmthreadid",
                                "cpmthreadblockingprocess",
                                "cpmthreadcpuutilization",
                                "cpmthreadhcstacksize",
                                "cpmthreadname",
                                "cpmthreadpriority",
                                "cpmthreadstacksize",
                                "cpmthreadstacksizeovrflw",
                                "cpmthreadstate") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmthreadtable.Cpmthreadentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmthreadtable.Cpmthreadentry, self).__setattr__(name, value)

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


            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmprocesspid.is_set or
                    self.cpmthreadid.is_set or
                    self.cpmthreadblockingprocess.is_set or
                    self.cpmthreadcpuutilization.is_set or
                    self.cpmthreadhcstacksize.is_set or
                    self.cpmthreadname.is_set or
                    self.cpmthreadpriority.is_set or
                    self.cpmthreadstacksize.is_set or
                    self.cpmthreadstacksizeovrflw.is_set or
                    self.cpmthreadstate.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmprocesspid.yfilter != YFilter.not_set or
                    self.cpmthreadid.yfilter != YFilter.not_set or
                    self.cpmthreadblockingprocess.yfilter != YFilter.not_set or
                    self.cpmthreadcpuutilization.yfilter != YFilter.not_set or
                    self.cpmthreadhcstacksize.yfilter != YFilter.not_set or
                    self.cpmthreadname.yfilter != YFilter.not_set or
                    self.cpmthreadpriority.yfilter != YFilter.not_set or
                    self.cpmthreadstacksize.yfilter != YFilter.not_set or
                    self.cpmthreadstacksizeovrflw.yfilter != YFilter.not_set or
                    self.cpmthreadstate.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmThreadEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']" + "[cpmThreadID='" + self.cpmthreadid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmThreadTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmprocesspid.is_set or self.cpmprocesspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesspid.get_name_leafdata())
                if (self.cpmthreadid.is_set or self.cpmthreadid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadid.get_name_leafdata())
                if (self.cpmthreadblockingprocess.is_set or self.cpmthreadblockingprocess.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadblockingprocess.get_name_leafdata())
                if (self.cpmthreadcpuutilization.is_set or self.cpmthreadcpuutilization.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadcpuutilization.get_name_leafdata())
                if (self.cpmthreadhcstacksize.is_set or self.cpmthreadhcstacksize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadhcstacksize.get_name_leafdata())
                if (self.cpmthreadname.is_set or self.cpmthreadname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadname.get_name_leafdata())
                if (self.cpmthreadpriority.is_set or self.cpmthreadpriority.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadpriority.get_name_leafdata())
                if (self.cpmthreadstacksize.is_set or self.cpmthreadstacksize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadstacksize.get_name_leafdata())
                if (self.cpmthreadstacksizeovrflw.is_set or self.cpmthreadstacksizeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadstacksizeovrflw.get_name_leafdata())
                if (self.cpmthreadstate.is_set or self.cpmthreadstate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmthreadstate.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmProcessPID" or name == "cpmThreadID" or name == "cpmThreadBlockingProcess" or name == "cpmThreadCpuUtilization" or name == "cpmThreadHCStackSize" or name == "cpmThreadName" or name == "cpmThreadPriority" or name == "cpmThreadStackSize" or name == "cpmThreadStackSizeOvrflw" or name == "cpmThreadState"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessPID"):
                    self.cpmprocesspid = value
                    self.cpmprocesspid.value_namespace = name_space
                    self.cpmprocesspid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadID"):
                    self.cpmthreadid = value
                    self.cpmthreadid.value_namespace = name_space
                    self.cpmthreadid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadBlockingProcess"):
                    self.cpmthreadblockingprocess = value
                    self.cpmthreadblockingprocess.value_namespace = name_space
                    self.cpmthreadblockingprocess.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadCpuUtilization"):
                    self.cpmthreadcpuutilization = value
                    self.cpmthreadcpuutilization.value_namespace = name_space
                    self.cpmthreadcpuutilization.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadHCStackSize"):
                    self.cpmthreadhcstacksize = value
                    self.cpmthreadhcstacksize.value_namespace = name_space
                    self.cpmthreadhcstacksize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadName"):
                    self.cpmthreadname = value
                    self.cpmthreadname.value_namespace = name_space
                    self.cpmthreadname.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadPriority"):
                    self.cpmthreadpriority = value
                    self.cpmthreadpriority.value_namespace = name_space
                    self.cpmthreadpriority.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadStackSize"):
                    self.cpmthreadstacksize = value
                    self.cpmthreadstacksize.value_namespace = name_space
                    self.cpmthreadstacksize.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadStackSizeOvrflw"):
                    self.cpmthreadstacksizeovrflw = value
                    self.cpmthreadstacksizeovrflw.value_namespace = name_space
                    self.cpmthreadstacksizeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmThreadState"):
                    self.cpmthreadstate = value
                    self.cpmthreadstate.value_namespace = name_space
                    self.cpmthreadstate.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmthreadentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmthreadentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmThreadTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmThreadEntry"):
                for c in self.cpmthreadentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmthreadtable.Cpmthreadentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmthreadentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmThreadEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cpmvirtualprocesstable(Entity):
        """
        This table contains information about virtual
        processes in a virtual machine.
        
        .. attribute:: cpmvirtualprocessentry
        
        	An entry containing the general statistics of a virtual process in a virtual machine
        	**type**\: list of    :py:class:`Cpmvirtualprocessentry <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmvirtualprocesstable.Cpmvirtualprocessentry>`
        
        

        """

        _prefix = 'CISCO-PROCESS-MIB'
        _revision = '2011-06-23'

        def __init__(self):
            super(CiscoProcessMib.Cpmvirtualprocesstable, self).__init__()

            self.yang_name = "cpmVirtualProcessTable"
            self.yang_parent_name = "CISCO-PROCESS-MIB"

            self.cpmvirtualprocessentry = YList(self)

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in () and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoProcessMib.Cpmvirtualprocesstable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoProcessMib.Cpmvirtualprocesstable, self).__setattr__(name, value)


        class Cpmvirtualprocessentry(Entity):
            """
            An entry containing the general statistics of a
            virtual process in a virtual machine.
            
            .. attribute:: cpmcputotalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..4294967295
            
            	**refers to**\:  :py:class:`cpmcputotalindex <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmcputotaltable.Cpmcputotalentry>`
            
            .. attribute:: cpmprocesspid  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cpmprocesspid <ydk.models.cisco_ios_xe.CISCO_PROCESS_MIB.CiscoProcessMib.Cpmprocesstable.Cpmprocessentry>`
            
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
                super(CiscoProcessMib.Cpmvirtualprocesstable.Cpmvirtualprocessentry, self).__init__()

                self.yang_name = "cpmVirtualProcessEntry"
                self.yang_parent_name = "cpmVirtualProcessTable"

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

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("cpmcputotalindex",
                                "cpmprocesspid",
                                "cpmvirtualprocessid",
                                "cpmvirtualprocesshcmemallocated",
                                "cpmvirtualprocesshcmemfreed",
                                "cpmvirtualprocessinvokecount",
                                "cpmvirtualprocessmemallocated",
                                "cpmvirtualprocessmemallocatedovrflw",
                                "cpmvirtualprocessmemfreed",
                                "cpmvirtualprocessmemfreedovrflw",
                                "cpmvirtualprocessname",
                                "cpmvirtualprocessruntime",
                                "cpmvirtualprocessutil1min",
                                "cpmvirtualprocessutil5min",
                                "cpmvirtualprocessutil5sec") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoProcessMib.Cpmvirtualprocesstable.Cpmvirtualprocessentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoProcessMib.Cpmvirtualprocesstable.Cpmvirtualprocessentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.cpmcputotalindex.is_set or
                    self.cpmprocesspid.is_set or
                    self.cpmvirtualprocessid.is_set or
                    self.cpmvirtualprocesshcmemallocated.is_set or
                    self.cpmvirtualprocesshcmemfreed.is_set or
                    self.cpmvirtualprocessinvokecount.is_set or
                    self.cpmvirtualprocessmemallocated.is_set or
                    self.cpmvirtualprocessmemallocatedovrflw.is_set or
                    self.cpmvirtualprocessmemfreed.is_set or
                    self.cpmvirtualprocessmemfreedovrflw.is_set or
                    self.cpmvirtualprocessname.is_set or
                    self.cpmvirtualprocessruntime.is_set or
                    self.cpmvirtualprocessutil1min.is_set or
                    self.cpmvirtualprocessutil5min.is_set or
                    self.cpmvirtualprocessutil5sec.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.cpmcputotalindex.yfilter != YFilter.not_set or
                    self.cpmprocesspid.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessid.yfilter != YFilter.not_set or
                    self.cpmvirtualprocesshcmemallocated.yfilter != YFilter.not_set or
                    self.cpmvirtualprocesshcmemfreed.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessinvokecount.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessmemallocated.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessmemallocatedovrflw.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessmemfreed.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessmemfreedovrflw.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessname.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessruntime.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessutil1min.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessutil5min.yfilter != YFilter.not_set or
                    self.cpmvirtualprocessutil5sec.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cpmVirtualProcessEntry" + "[cpmCPUTotalIndex='" + self.cpmcputotalindex.get() + "']" + "[cpmProcessPID='" + self.cpmprocesspid.get() + "']" + "[cpmVirtualProcessID='" + self.cpmvirtualprocessid.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/cpmVirtualProcessTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.cpmcputotalindex.is_set or self.cpmcputotalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmcputotalindex.get_name_leafdata())
                if (self.cpmprocesspid.is_set or self.cpmprocesspid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmprocesspid.get_name_leafdata())
                if (self.cpmvirtualprocessid.is_set or self.cpmvirtualprocessid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessid.get_name_leafdata())
                if (self.cpmvirtualprocesshcmemallocated.is_set or self.cpmvirtualprocesshcmemallocated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocesshcmemallocated.get_name_leafdata())
                if (self.cpmvirtualprocesshcmemfreed.is_set or self.cpmvirtualprocesshcmemfreed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocesshcmemfreed.get_name_leafdata())
                if (self.cpmvirtualprocessinvokecount.is_set or self.cpmvirtualprocessinvokecount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessinvokecount.get_name_leafdata())
                if (self.cpmvirtualprocessmemallocated.is_set or self.cpmvirtualprocessmemallocated.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessmemallocated.get_name_leafdata())
                if (self.cpmvirtualprocessmemallocatedovrflw.is_set or self.cpmvirtualprocessmemallocatedovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessmemallocatedovrflw.get_name_leafdata())
                if (self.cpmvirtualprocessmemfreed.is_set or self.cpmvirtualprocessmemfreed.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessmemfreed.get_name_leafdata())
                if (self.cpmvirtualprocessmemfreedovrflw.is_set or self.cpmvirtualprocessmemfreedovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessmemfreedovrflw.get_name_leafdata())
                if (self.cpmvirtualprocessname.is_set or self.cpmvirtualprocessname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessname.get_name_leafdata())
                if (self.cpmvirtualprocessruntime.is_set or self.cpmvirtualprocessruntime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessruntime.get_name_leafdata())
                if (self.cpmvirtualprocessutil1min.is_set or self.cpmvirtualprocessutil1min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessutil1min.get_name_leafdata())
                if (self.cpmvirtualprocessutil5min.is_set or self.cpmvirtualprocessutil5min.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessutil5min.get_name_leafdata())
                if (self.cpmvirtualprocessutil5sec.is_set or self.cpmvirtualprocessutil5sec.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cpmvirtualprocessutil5sec.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "cpmCPUTotalIndex" or name == "cpmProcessPID" or name == "cpmVirtualProcessID" or name == "cpmVirtualProcessHCMemAllocated" or name == "cpmVirtualProcessHCMemFreed" or name == "cpmVirtualProcessInvokeCount" or name == "cpmVirtualProcessMemAllocated" or name == "cpmVirtualProcessMemAllocatedOvrflw" or name == "cpmVirtualProcessMemFreed" or name == "cpmVirtualProcessMemFreedOvrflw" or name == "cpmVirtualProcessName" or name == "cpmVirtualProcessRuntime" or name == "cpmVirtualProcessUtil1Min" or name == "cpmVirtualProcessUtil5Min" or name == "cpmVirtualProcessUtil5Sec"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "cpmCPUTotalIndex"):
                    self.cpmcputotalindex = value
                    self.cpmcputotalindex.value_namespace = name_space
                    self.cpmcputotalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmProcessPID"):
                    self.cpmprocesspid = value
                    self.cpmprocesspid.value_namespace = name_space
                    self.cpmprocesspid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessID"):
                    self.cpmvirtualprocessid = value
                    self.cpmvirtualprocessid.value_namespace = name_space
                    self.cpmvirtualprocessid.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessHCMemAllocated"):
                    self.cpmvirtualprocesshcmemallocated = value
                    self.cpmvirtualprocesshcmemallocated.value_namespace = name_space
                    self.cpmvirtualprocesshcmemallocated.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessHCMemFreed"):
                    self.cpmvirtualprocesshcmemfreed = value
                    self.cpmvirtualprocesshcmemfreed.value_namespace = name_space
                    self.cpmvirtualprocesshcmemfreed.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessInvokeCount"):
                    self.cpmvirtualprocessinvokecount = value
                    self.cpmvirtualprocessinvokecount.value_namespace = name_space
                    self.cpmvirtualprocessinvokecount.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessMemAllocated"):
                    self.cpmvirtualprocessmemallocated = value
                    self.cpmvirtualprocessmemallocated.value_namespace = name_space
                    self.cpmvirtualprocessmemallocated.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessMemAllocatedOvrflw"):
                    self.cpmvirtualprocessmemallocatedovrflw = value
                    self.cpmvirtualprocessmemallocatedovrflw.value_namespace = name_space
                    self.cpmvirtualprocessmemallocatedovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessMemFreed"):
                    self.cpmvirtualprocessmemfreed = value
                    self.cpmvirtualprocessmemfreed.value_namespace = name_space
                    self.cpmvirtualprocessmemfreed.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessMemFreedOvrflw"):
                    self.cpmvirtualprocessmemfreedovrflw = value
                    self.cpmvirtualprocessmemfreedovrflw.value_namespace = name_space
                    self.cpmvirtualprocessmemfreedovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessName"):
                    self.cpmvirtualprocessname = value
                    self.cpmvirtualprocessname.value_namespace = name_space
                    self.cpmvirtualprocessname.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessRuntime"):
                    self.cpmvirtualprocessruntime = value
                    self.cpmvirtualprocessruntime.value_namespace = name_space
                    self.cpmvirtualprocessruntime.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessUtil1Min"):
                    self.cpmvirtualprocessutil1min = value
                    self.cpmvirtualprocessutil1min.value_namespace = name_space
                    self.cpmvirtualprocessutil1min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessUtil5Min"):
                    self.cpmvirtualprocessutil5min = value
                    self.cpmvirtualprocessutil5min.value_namespace = name_space
                    self.cpmvirtualprocessutil5min.value_namespace_prefix = name_space_prefix
                if(value_path == "cpmVirtualProcessUtil5Sec"):
                    self.cpmvirtualprocessutil5sec = value
                    self.cpmvirtualprocessutil5sec.value_namespace = name_space
                    self.cpmvirtualprocessutil5sec.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cpmvirtualprocessentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cpmvirtualprocessentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cpmVirtualProcessTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cpmVirtualProcessEntry"):
                for c in self.cpmvirtualprocessentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoProcessMib.Cpmvirtualprocesstable.Cpmvirtualprocessentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cpmvirtualprocessentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cpmVirtualProcessEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cpmcoretable is not None and self.cpmcoretable.has_data()) or
            (self.cpmcpuhistory is not None and self.cpmcpuhistory.has_data()) or
            (self.cpmcpuhistorytable is not None and self.cpmcpuhistorytable.has_data()) or
            (self.cpmcpuprocesshistorytable is not None and self.cpmcpuprocesshistorytable.has_data()) or
            (self.cpmcputhresholdtable is not None and self.cpmcputhresholdtable.has_data()) or
            (self.cpmcputotaltable is not None and self.cpmcputotaltable.has_data()) or
            (self.cpmprocessextrevtable is not None and self.cpmprocessextrevtable.has_data()) or
            (self.cpmprocesstable is not None and self.cpmprocesstable.has_data()) or
            (self.cpmthreadtable is not None and self.cpmthreadtable.has_data()) or
            (self.cpmvirtualprocesstable is not None and self.cpmvirtualprocesstable.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cpmcoretable is not None and self.cpmcoretable.has_operation()) or
            (self.cpmcpuhistory is not None and self.cpmcpuhistory.has_operation()) or
            (self.cpmcpuhistorytable is not None and self.cpmcpuhistorytable.has_operation()) or
            (self.cpmcpuprocesshistorytable is not None and self.cpmcpuprocesshistorytable.has_operation()) or
            (self.cpmcputhresholdtable is not None and self.cpmcputhresholdtable.has_operation()) or
            (self.cpmcputotaltable is not None and self.cpmcputotaltable.has_operation()) or
            (self.cpmprocessextrevtable is not None and self.cpmprocessextrevtable.has_operation()) or
            (self.cpmprocesstable is not None and self.cpmprocesstable.has_operation()) or
            (self.cpmthreadtable is not None and self.cpmthreadtable.has_operation()) or
            (self.cpmvirtualprocesstable is not None and self.cpmvirtualprocesstable.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-PROCESS-MIB:CISCO-PROCESS-MIB" + path_buffer

        return path_buffer

    def get_entity_path(self, ancestor):
        path_buffer = ""
        if (not ancestor is None):
            raise YPYModelError("ancestor has to be None for top-level node")

        path_buffer = self.get_segment_path()
        leaf_name_data = LeafDataList()

        entity_path = EntityPath(path_buffer, leaf_name_data)
        return entity_path

    def get_child_by_name(self, child_yang_name, segment_path):
        child = self._get_child_by_seg_name([child_yang_name, segment_path])
        if child is not None:
            return child

        if (child_yang_name == "cpmCoreTable"):
            if (self.cpmcoretable is None):
                self.cpmcoretable = CiscoProcessMib.Cpmcoretable()
                self.cpmcoretable.parent = self
                self._children_name_map["cpmcoretable"] = "cpmCoreTable"
            return self.cpmcoretable

        if (child_yang_name == "cpmCPUHistory"):
            if (self.cpmcpuhistory is None):
                self.cpmcpuhistory = CiscoProcessMib.Cpmcpuhistory()
                self.cpmcpuhistory.parent = self
                self._children_name_map["cpmcpuhistory"] = "cpmCPUHistory"
            return self.cpmcpuhistory

        if (child_yang_name == "cpmCPUHistoryTable"):
            if (self.cpmcpuhistorytable is None):
                self.cpmcpuhistorytable = CiscoProcessMib.Cpmcpuhistorytable()
                self.cpmcpuhistorytable.parent = self
                self._children_name_map["cpmcpuhistorytable"] = "cpmCPUHistoryTable"
            return self.cpmcpuhistorytable

        if (child_yang_name == "cpmCPUProcessHistoryTable"):
            if (self.cpmcpuprocesshistorytable is None):
                self.cpmcpuprocesshistorytable = CiscoProcessMib.Cpmcpuprocesshistorytable()
                self.cpmcpuprocesshistorytable.parent = self
                self._children_name_map["cpmcpuprocesshistorytable"] = "cpmCPUProcessHistoryTable"
            return self.cpmcpuprocesshistorytable

        if (child_yang_name == "cpmCPUThresholdTable"):
            if (self.cpmcputhresholdtable is None):
                self.cpmcputhresholdtable = CiscoProcessMib.Cpmcputhresholdtable()
                self.cpmcputhresholdtable.parent = self
                self._children_name_map["cpmcputhresholdtable"] = "cpmCPUThresholdTable"
            return self.cpmcputhresholdtable

        if (child_yang_name == "cpmCPUTotalTable"):
            if (self.cpmcputotaltable is None):
                self.cpmcputotaltable = CiscoProcessMib.Cpmcputotaltable()
                self.cpmcputotaltable.parent = self
                self._children_name_map["cpmcputotaltable"] = "cpmCPUTotalTable"
            return self.cpmcputotaltable

        if (child_yang_name == "cpmProcessExtRevTable"):
            if (self.cpmprocessextrevtable is None):
                self.cpmprocessextrevtable = CiscoProcessMib.Cpmprocessextrevtable()
                self.cpmprocessextrevtable.parent = self
                self._children_name_map["cpmprocessextrevtable"] = "cpmProcessExtRevTable"
            return self.cpmprocessextrevtable

        if (child_yang_name == "cpmProcessTable"):
            if (self.cpmprocesstable is None):
                self.cpmprocesstable = CiscoProcessMib.Cpmprocesstable()
                self.cpmprocesstable.parent = self
                self._children_name_map["cpmprocesstable"] = "cpmProcessTable"
            return self.cpmprocesstable

        if (child_yang_name == "cpmThreadTable"):
            if (self.cpmthreadtable is None):
                self.cpmthreadtable = CiscoProcessMib.Cpmthreadtable()
                self.cpmthreadtable.parent = self
                self._children_name_map["cpmthreadtable"] = "cpmThreadTable"
            return self.cpmthreadtable

        if (child_yang_name == "cpmVirtualProcessTable"):
            if (self.cpmvirtualprocesstable is None):
                self.cpmvirtualprocesstable = CiscoProcessMib.Cpmvirtualprocesstable()
                self.cpmvirtualprocesstable.parent = self
                self._children_name_map["cpmvirtualprocesstable"] = "cpmVirtualProcessTable"
            return self.cpmvirtualprocesstable

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cpmCoreTable" or name == "cpmCPUHistory" or name == "cpmCPUHistoryTable" or name == "cpmCPUProcessHistoryTable" or name == "cpmCPUThresholdTable" or name == "cpmCPUTotalTable" or name == "cpmProcessExtRevTable" or name == "cpmProcessTable" or name == "cpmThreadTable" or name == "cpmVirtualProcessTable"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoProcessMib()
        return self._top_entity

