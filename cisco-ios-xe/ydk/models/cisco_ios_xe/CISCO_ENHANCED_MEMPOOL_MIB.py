""" CISCO_ENHANCED_MEMPOOL_MIB 

New MIB module for monitoring the memory pools
of all physical entities on a managed system.

"""
from ydk.entity_utils import get_relative_entity_path as _get_relative_entity_path
from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YPYError, YPYModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error


class Cempmempooltypes(Enum):
    """
    Cempmempooltypes

    Represents the different types of memory pools that

    may be present in a managed device. 

    Note that only the processor pool is required to be

    supported by all devices.  Support for other pool types

    is dependent on the device being managed.

    processorMemory \-

             processor associated heap memory.

    ioMemory \- 

             shared memory for buffer data and

             controller descriptor blocks.

    pciMemory \- 

             Peripheral Component Interconnect bus

             memory which is visible to all devices on 

             the PCI buses in a platform.

    fastMemory \- 

             memory defined by the particular platform 

             for speed critical applications.

    multibusMemory \- 

             memory present on some platforms that

             is used as a fallback pool.

    interruptStackMemory \- 

             memory for allocating interrupt stacks. 

             It is usually allocated from heap.

    processStackMemory \- 

             memory for allocating process stacks. 

             It is usually allocated from heap.

    localExceptionMemory \- 

             memory reserved for processing 

             a system core dump.

    virtualMemory \- 

             memory used to increase available RAM.

    reservedMemory \- 

             memory used for packet headers, 

             particle headers and particles. 

    imageMemory \- 

             memory which corresponds to the image 

             file system.

    asicMemory \- 

             Application Specific Integrated Circuit

             memory.

    posixMemory \-

              Heap memory associated with posix style

              processes in ion.

    .. data:: other = 1

    .. data:: processorMemory = 2

    .. data:: ioMemory = 3

    .. data:: pciMemory = 4

    .. data:: fastMemory = 5

    .. data:: multibusMemory = 6

    .. data:: interruptStackMemory = 7

    .. data:: processStackMemory = 8

    .. data:: localExceptionMemory = 9

    .. data:: virtualMemory = 10

    .. data:: reservedMemory = 11

    .. data:: imageMemory = 12

    .. data:: asicMemory = 13

    .. data:: posixMemory = 14

    """

    other = Enum.YLeaf(1, "other")

    processorMemory = Enum.YLeaf(2, "processorMemory")

    ioMemory = Enum.YLeaf(3, "ioMemory")

    pciMemory = Enum.YLeaf(4, "pciMemory")

    fastMemory = Enum.YLeaf(5, "fastMemory")

    multibusMemory = Enum.YLeaf(6, "multibusMemory")

    interruptStackMemory = Enum.YLeaf(7, "interruptStackMemory")

    processStackMemory = Enum.YLeaf(8, "processStackMemory")

    localExceptionMemory = Enum.YLeaf(9, "localExceptionMemory")

    virtualMemory = Enum.YLeaf(10, "virtualMemory")

    reservedMemory = Enum.YLeaf(11, "reservedMemory")

    imageMemory = Enum.YLeaf(12, "imageMemory")

    asicMemory = Enum.YLeaf(13, "asicMemory")

    posixMemory = Enum.YLeaf(14, "posixMemory")



class CiscoEnhancedMempoolMib(Entity):
    """
    
    
    .. attribute:: cempmembuffercachepooltable
    
    	A table that lists the cache buffer pools configured on a managed system.  1)To provide a noticeable performance boost,    Cache Pool can be used. A Cache Pool is effectively   a lookaside list of free buffers that can be    accessed quickly. Cache Pool is tied to Buffer Pool.  2)Cache pools can optionally have a threshold value   on the number of cache buffers used in a pool. This   can provide flow control management by having a    implementation specific approach such as invoking a   vector when pool cache rises above the optional    threshold set for it on creation
    	**type**\:   :py:class:`Cempmembuffercachepooltable <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempmembuffercachepooltable>`
    
    .. attribute:: cempmembufferpooltable
    
    	Entries in this table define entities (buffer pools in this case) which are contained in an entity  (memory pool) defined by an entry from cempMemPoolTable. \-\- Basic Pool Architecture \-\- 1)Pools are classified as being either Static or    Dynamic. Static pools make no attempt to increase    the number of buffers contained within them if the    number of free buffers (cempMemBufferFree) are less   than the number of minimum buffers (cempMemBufferMin).   With Dynamic pools, the pool attempts to meet the    demands of its users. 2)Buffers in a pool are classified as being either    Permanent or Temporary. Permanent buffers, as their   name suggests, are always in the pool and are never   destroyed unless the number of permanent buffers    (cempMemBufferPermanent) is changed. Temporary   buffers are transient buffers that are created in   dynamic pools whenever the free count    (cempMemBufferFree) of buffers in the pool drops    below the minimum (cempMemBufferMin). 3)Buffers pools are classified as either Public or    Private. Public pools are available for all users    to allocate buffers from. Private pools are   primarily used by interface drivers
    	**type**\:   :py:class:`Cempmembufferpooltable <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempmembufferpooltable>`
    
    .. attribute:: cempmempooltable
    
    	A table of memory pool monitoring entries for all physical entities on a managed system
    	**type**\:   :py:class:`Cempmempooltable <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempmempooltable>`
    
    .. attribute:: cempnotificationconfig
    
    	
    	**type**\:   :py:class:`Cempnotificationconfig <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempnotificationconfig>`
    
    

    """

    _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
    _revision = '2008-12-05'

    def __init__(self):
        super(CiscoEnhancedMempoolMib, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENHANCED-MEMPOOL-MIB"
        self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"

        self.cempmembuffercachepooltable = CiscoEnhancedMempoolMib.Cempmembuffercachepooltable()
        self.cempmembuffercachepooltable.parent = self
        self._children_name_map["cempmembuffercachepooltable"] = "cempMemBufferCachePoolTable"
        self._children_yang_names.add("cempMemBufferCachePoolTable")

        self.cempmembufferpooltable = CiscoEnhancedMempoolMib.Cempmembufferpooltable()
        self.cempmembufferpooltable.parent = self
        self._children_name_map["cempmembufferpooltable"] = "cempMemBufferPoolTable"
        self._children_yang_names.add("cempMemBufferPoolTable")

        self.cempmempooltable = CiscoEnhancedMempoolMib.Cempmempooltable()
        self.cempmempooltable.parent = self
        self._children_name_map["cempmempooltable"] = "cempMemPoolTable"
        self._children_yang_names.add("cempMemPoolTable")

        self.cempnotificationconfig = CiscoEnhancedMempoolMib.Cempnotificationconfig()
        self.cempnotificationconfig.parent = self
        self._children_name_map["cempnotificationconfig"] = "cempNotificationConfig"
        self._children_yang_names.add("cempNotificationConfig")


    class Cempnotificationconfig(Entity):
        """
        
        
        .. attribute:: cempmembuffernotifyenabled
        
        	This variable controls generation of the cempMemBufferNotify.  When this variable is 'true', generation of cempMemBufferNotify is enabled.  When this variable is 'false', generation of cempMemBufferNotify is disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CiscoEnhancedMempoolMib.Cempnotificationconfig, self).__init__()

            self.yang_name = "cempNotificationConfig"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"

            self.cempmembuffernotifyenabled = YLeaf(YType.boolean, "cempMemBufferNotifyEnabled")

        def __setattr__(self, name, value):
            self._check_monkey_patching_error(name, value)
            with _handle_type_error():
                if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                    raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                        "Please use list append or extend method."
                                        .format(value))
                if isinstance(value, Enum.YLeaf):
                    value = value.name
                if name in ("cempmembuffernotifyenabled") and name in self.__dict__:
                    if isinstance(value, YLeaf):
                        self.__dict__[name].set(value.get())
                    elif isinstance(value, YLeafList):
                        super(CiscoEnhancedMempoolMib.Cempnotificationconfig, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnhancedMempoolMib.Cempnotificationconfig, self).__setattr__(name, value)

        def has_data(self):
            return self.cempmembuffernotifyenabled.is_set

        def has_operation(self):
            return (
                self.yfilter != YFilter.not_set or
                self.cempmembuffernotifyenabled.yfilter != YFilter.not_set)

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cempNotificationConfig" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()
            if (self.cempmembuffernotifyenabled.is_set or self.cempmembuffernotifyenabled.yfilter != YFilter.not_set):
                leaf_name_data.append(self.cempmembuffernotifyenabled.get_name_leafdata())

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cempMemBufferNotifyEnabled"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            if(value_path == "cempMemBufferNotifyEnabled"):
                self.cempmembuffernotifyenabled = value
                self.cempmembuffernotifyenabled.value_namespace = name_space
                self.cempmembuffernotifyenabled.value_namespace_prefix = name_space_prefix


    class Cempmempooltable(Entity):
        """
        A table of memory pool monitoring entries for all
        physical entities on a managed system.
        
        .. attribute:: cempmempoolentry
        
        	An entry in the memory pool monitoring table
        	**type**\: list of    :py:class:`Cempmempoolentry <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry>`
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CiscoEnhancedMempoolMib.Cempmempooltable, self).__init__()

            self.yang_name = "cempMemPoolTable"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"

            self.cempmempoolentry = YList(self)

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
                        super(CiscoEnhancedMempoolMib.Cempmempooltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnhancedMempoolMib.Cempmempooltable, self).__setattr__(name, value)


        class Cempmempoolentry(Entity):
            """
            An entry in the memory pool monitoring table.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cempmempoolindex  <key>
            
            	Within each physical entity, the unique value greater than zero, used to represent each memory pool.   It is recommended that values are assigned contiguously starting from 1
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            .. attribute:: cempmempoolallochit
            
            	Indicates the number of successful allocations from the memory pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmempoolallocmiss
            
            	Indicates the number of unsuccessful allocations from the memory pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmempoolalternate
            
            	Indicates whether or not this memory pool has an alternate pool configured.  Alternate pools are used for fallback when the current pool runs out of memory.  If an instance of this object has a value of zero, then this pool does not have an alternate.  Otherwise the value of this object is the same as the value of cempMemPoolType of the alternate pool
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cempmempoolfree
            
            	Indicates the number of bytes from the memory pool that are currently unused on the physical entity.  Note that the sum of cempMemPoolUsed and cempMemPoolFree  is the total amount of memory in the pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolfreehit
            
            	Indicates the number of successful frees/ deallocations from the memory pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmempoolfreemiss
            
            	Indicates the number of unsuccessful attempts to free/deallocate memory from the memory pool. For example, this could be due to ownership errors  where the application that did not assign the  memory is trying to free it
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmempoolfreeovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolFree. This object needs to be supported only if the unused bytes in the memory pool exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcfree
            
            	Indicates the number of bytes from the memory pool that are currently unused on the physical entity. This object is a 64\-bit version of cempMemPoolFree
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhclargestfree
            
            	Indicates the largest number of contiguous bytes from the memory pool that are currently unused on the physical entity. This object is a 64\-bit version of cempMemPoolLargestFree
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhclowestfree
            
            	The lowest amount of available memory in the memory pool recorded at any time during the operation of the system. This object is a 64\-bit version of cempMemPoolLowestFree
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcshared
            
            	Indicates the number of bytes from the memory pool that are currently shared on the physical entity. This object is a 64\-bit version of cempMemPoolShared
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcused
            
            	Indicates the number of bytes from the memory pool that are currently in use by applications on the physical entity. This object is a 64\-bit version of cempMemPoolUsed
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcusedlowwatermark
            
            	Indicates the lowest number of bytes from the memory pool that have been used by applications on the physical entity since sysUpTime. This object is a 64\-bit version of cempMemPoolUsedLowWaterMark
            	**type**\:  int
            
            	**range:** 0..18446744073709551615
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollargestfree
            
            	Indicates the largest number of contiguous bytes from the memory pool that are currently unused on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollargestfreeovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolLargestFree. This object needs to  be supported only if the value of  cempMemPoolLargestFree exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollowestfree
            
            	The lowest amount of available memory in the memory pool recorded at any time during the operation of the system
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollowestfreeovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolLowestFree. This object needs to be supported only if the value of cempMemPoolLowestFree exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolname
            
            	A textual name assigned to the memory pool. This object is suitable for output to a human operator, and may also be used to distinguish among the various pool types
            	**type**\:  str
            
            .. attribute:: cempmempoolplatformmemory
            
            	An indication of the platform\-specific memory pool type. The associated instance of cempMemPoolType is used to indicate the general type of memory pool.  If no platform specific memory hardware type identifier exists for this physical entity, or the value is unknown by this agent, then the value { 0 0 } is returned
            	**type**\:  str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            .. attribute:: cempmempoolshared
            
            	Indicates the number of bytes from the memory pool that are currently shared on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolsharedovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolShared. This object needs to be supported only if the value of cempMemPoolShared exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempooltype
            
            	The type of memory pool for which this entry contains information
            	**type**\:   :py:class:`Cempmempooltypes <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.Cempmempooltypes>`
            
            .. attribute:: cempmempoolused
            
            	Indicates the number of bytes from the memory pool that are currently in use by applications on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolusedlowwatermark
            
            	Indicates the lowest number of bytes from the memory pool that have been used by applications on the physical entity since sysUpTime.Similarly,the Used High Watermark indicates the largest number of bytes from the memory pool that have been used by applications on the physical entity since sysUpTime.This can be derived as follows\: Used High Watermark = cempMemPoolUsed + cempMemPoolFree  \- cempMemPoolLowestFree
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmempoolusedlowwatermarkovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolUsedLowWaterMark. This object needs to be supported only if the value of cempMemPoolUsedLowWaterMark exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolusedovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolUsed. This object needs to be supported only if the used bytes in the memory pool exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolvalid
            
            	Indicates whether or not cempMemPoolUsed, cempMemPoolFree, cempMemPoolLargestFree and  cempMemPoolLowestFree in this entry contain accurate  data. If an instance of this object has the value  false (which in and of itself indicates an internal  error condition), the values of these objects in the conceptual row may contain inaccurate  information (specifically, the reported values may be  less than the actual values)
            	**type**\:  bool
            
            

            """

            _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
            _revision = '2008-12-05'

            def __init__(self):
                super(CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry, self).__init__()

                self.yang_name = "cempMemPoolEntry"
                self.yang_parent_name = "cempMemPoolTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cempmempoolindex = YLeaf(YType.int32, "cempMemPoolIndex")

                self.cempmempoolallochit = YLeaf(YType.uint32, "cempMemPoolAllocHit")

                self.cempmempoolallocmiss = YLeaf(YType.uint32, "cempMemPoolAllocMiss")

                self.cempmempoolalternate = YLeaf(YType.int32, "cempMemPoolAlternate")

                self.cempmempoolfree = YLeaf(YType.uint32, "cempMemPoolFree")

                self.cempmempoolfreehit = YLeaf(YType.uint32, "cempMemPoolFreeHit")

                self.cempmempoolfreemiss = YLeaf(YType.uint32, "cempMemPoolFreeMiss")

                self.cempmempoolfreeovrflw = YLeaf(YType.uint32, "cempMemPoolFreeOvrflw")

                self.cempmempoolhcfree = YLeaf(YType.uint64, "cempMemPoolHCFree")

                self.cempmempoolhclargestfree = YLeaf(YType.uint64, "cempMemPoolHCLargestFree")

                self.cempmempoolhclowestfree = YLeaf(YType.uint64, "cempMemPoolHCLowestFree")

                self.cempmempoolhcshared = YLeaf(YType.uint64, "cempMemPoolHCShared")

                self.cempmempoolhcused = YLeaf(YType.uint64, "cempMemPoolHCUsed")

                self.cempmempoolhcusedlowwatermark = YLeaf(YType.uint64, "cempMemPoolHCUsedLowWaterMark")

                self.cempmempoollargestfree = YLeaf(YType.uint32, "cempMemPoolLargestFree")

                self.cempmempoollargestfreeovrflw = YLeaf(YType.uint32, "cempMemPoolLargestFreeOvrflw")

                self.cempmempoollowestfree = YLeaf(YType.uint32, "cempMemPoolLowestFree")

                self.cempmempoollowestfreeovrflw = YLeaf(YType.uint32, "cempMemPoolLowestFreeOvrflw")

                self.cempmempoolname = YLeaf(YType.str, "cempMemPoolName")

                self.cempmempoolplatformmemory = YLeaf(YType.str, "cempMemPoolPlatformMemory")

                self.cempmempoolshared = YLeaf(YType.uint32, "cempMemPoolShared")

                self.cempmempoolsharedovrflw = YLeaf(YType.uint32, "cempMemPoolSharedOvrflw")

                self.cempmempooltype = YLeaf(YType.enumeration, "cempMemPoolType")

                self.cempmempoolused = YLeaf(YType.uint32, "cempMemPoolUsed")

                self.cempmempoolusedlowwatermark = YLeaf(YType.uint32, "cempMemPoolUsedLowWaterMark")

                self.cempmempoolusedlowwatermarkovrflw = YLeaf(YType.uint32, "cempMemPoolUsedLowWaterMarkOvrflw")

                self.cempmempoolusedovrflw = YLeaf(YType.uint32, "cempMemPoolUsedOvrflw")

                self.cempmempoolvalid = YLeaf(YType.boolean, "cempMemPoolValid")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cempmempoolindex",
                                "cempmempoolallochit",
                                "cempmempoolallocmiss",
                                "cempmempoolalternate",
                                "cempmempoolfree",
                                "cempmempoolfreehit",
                                "cempmempoolfreemiss",
                                "cempmempoolfreeovrflw",
                                "cempmempoolhcfree",
                                "cempmempoolhclargestfree",
                                "cempmempoolhclowestfree",
                                "cempmempoolhcshared",
                                "cempmempoolhcused",
                                "cempmempoolhcusedlowwatermark",
                                "cempmempoollargestfree",
                                "cempmempoollargestfreeovrflw",
                                "cempmempoollowestfree",
                                "cempmempoollowestfreeovrflw",
                                "cempmempoolname",
                                "cempmempoolplatformmemory",
                                "cempmempoolshared",
                                "cempmempoolsharedovrflw",
                                "cempmempooltype",
                                "cempmempoolused",
                                "cempmempoolusedlowwatermark",
                                "cempmempoolusedlowwatermarkovrflw",
                                "cempmempoolusedovrflw",
                                "cempmempoolvalid") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cempmempoolindex.is_set or
                    self.cempmempoolallochit.is_set or
                    self.cempmempoolallocmiss.is_set or
                    self.cempmempoolalternate.is_set or
                    self.cempmempoolfree.is_set or
                    self.cempmempoolfreehit.is_set or
                    self.cempmempoolfreemiss.is_set or
                    self.cempmempoolfreeovrflw.is_set or
                    self.cempmempoolhcfree.is_set or
                    self.cempmempoolhclargestfree.is_set or
                    self.cempmempoolhclowestfree.is_set or
                    self.cempmempoolhcshared.is_set or
                    self.cempmempoolhcused.is_set or
                    self.cempmempoolhcusedlowwatermark.is_set or
                    self.cempmempoollargestfree.is_set or
                    self.cempmempoollargestfreeovrflw.is_set or
                    self.cempmempoollowestfree.is_set or
                    self.cempmempoollowestfreeovrflw.is_set or
                    self.cempmempoolname.is_set or
                    self.cempmempoolplatformmemory.is_set or
                    self.cempmempoolshared.is_set or
                    self.cempmempoolsharedovrflw.is_set or
                    self.cempmempooltype.is_set or
                    self.cempmempoolused.is_set or
                    self.cempmempoolusedlowwatermark.is_set or
                    self.cempmempoolusedlowwatermarkovrflw.is_set or
                    self.cempmempoolusedovrflw.is_set or
                    self.cempmempoolvalid.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cempmempoolindex.yfilter != YFilter.not_set or
                    self.cempmempoolallochit.yfilter != YFilter.not_set or
                    self.cempmempoolallocmiss.yfilter != YFilter.not_set or
                    self.cempmempoolalternate.yfilter != YFilter.not_set or
                    self.cempmempoolfree.yfilter != YFilter.not_set or
                    self.cempmempoolfreehit.yfilter != YFilter.not_set or
                    self.cempmempoolfreemiss.yfilter != YFilter.not_set or
                    self.cempmempoolfreeovrflw.yfilter != YFilter.not_set or
                    self.cempmempoolhcfree.yfilter != YFilter.not_set or
                    self.cempmempoolhclargestfree.yfilter != YFilter.not_set or
                    self.cempmempoolhclowestfree.yfilter != YFilter.not_set or
                    self.cempmempoolhcshared.yfilter != YFilter.not_set or
                    self.cempmempoolhcused.yfilter != YFilter.not_set or
                    self.cempmempoolhcusedlowwatermark.yfilter != YFilter.not_set or
                    self.cempmempoollargestfree.yfilter != YFilter.not_set or
                    self.cempmempoollargestfreeovrflw.yfilter != YFilter.not_set or
                    self.cempmempoollowestfree.yfilter != YFilter.not_set or
                    self.cempmempoollowestfreeovrflw.yfilter != YFilter.not_set or
                    self.cempmempoolname.yfilter != YFilter.not_set or
                    self.cempmempoolplatformmemory.yfilter != YFilter.not_set or
                    self.cempmempoolshared.yfilter != YFilter.not_set or
                    self.cempmempoolsharedovrflw.yfilter != YFilter.not_set or
                    self.cempmempooltype.yfilter != YFilter.not_set or
                    self.cempmempoolused.yfilter != YFilter.not_set or
                    self.cempmempoolusedlowwatermark.yfilter != YFilter.not_set or
                    self.cempmempoolusedlowwatermarkovrflw.yfilter != YFilter.not_set or
                    self.cempmempoolusedovrflw.yfilter != YFilter.not_set or
                    self.cempmempoolvalid.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cempMemPoolEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cempMemPoolIndex='" + self.cempmempoolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/cempMemPoolTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cempmempoolindex.is_set or self.cempmempoolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolindex.get_name_leafdata())
                if (self.cempmempoolallochit.is_set or self.cempmempoolallochit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolallochit.get_name_leafdata())
                if (self.cempmempoolallocmiss.is_set or self.cempmempoolallocmiss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolallocmiss.get_name_leafdata())
                if (self.cempmempoolalternate.is_set or self.cempmempoolalternate.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolalternate.get_name_leafdata())
                if (self.cempmempoolfree.is_set or self.cempmempoolfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolfree.get_name_leafdata())
                if (self.cempmempoolfreehit.is_set or self.cempmempoolfreehit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolfreehit.get_name_leafdata())
                if (self.cempmempoolfreemiss.is_set or self.cempmempoolfreemiss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolfreemiss.get_name_leafdata())
                if (self.cempmempoolfreeovrflw.is_set or self.cempmempoolfreeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolfreeovrflw.get_name_leafdata())
                if (self.cempmempoolhcfree.is_set or self.cempmempoolhcfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolhcfree.get_name_leafdata())
                if (self.cempmempoolhclargestfree.is_set or self.cempmempoolhclargestfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolhclargestfree.get_name_leafdata())
                if (self.cempmempoolhclowestfree.is_set or self.cempmempoolhclowestfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolhclowestfree.get_name_leafdata())
                if (self.cempmempoolhcshared.is_set or self.cempmempoolhcshared.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolhcshared.get_name_leafdata())
                if (self.cempmempoolhcused.is_set or self.cempmempoolhcused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolhcused.get_name_leafdata())
                if (self.cempmempoolhcusedlowwatermark.is_set or self.cempmempoolhcusedlowwatermark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolhcusedlowwatermark.get_name_leafdata())
                if (self.cempmempoollargestfree.is_set or self.cempmempoollargestfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoollargestfree.get_name_leafdata())
                if (self.cempmempoollargestfreeovrflw.is_set or self.cempmempoollargestfreeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoollargestfreeovrflw.get_name_leafdata())
                if (self.cempmempoollowestfree.is_set or self.cempmempoollowestfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoollowestfree.get_name_leafdata())
                if (self.cempmempoollowestfreeovrflw.is_set or self.cempmempoollowestfreeovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoollowestfreeovrflw.get_name_leafdata())
                if (self.cempmempoolname.is_set or self.cempmempoolname.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolname.get_name_leafdata())
                if (self.cempmempoolplatformmemory.is_set or self.cempmempoolplatformmemory.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolplatformmemory.get_name_leafdata())
                if (self.cempmempoolshared.is_set or self.cempmempoolshared.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolshared.get_name_leafdata())
                if (self.cempmempoolsharedovrflw.is_set or self.cempmempoolsharedovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolsharedovrflw.get_name_leafdata())
                if (self.cempmempooltype.is_set or self.cempmempooltype.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempooltype.get_name_leafdata())
                if (self.cempmempoolused.is_set or self.cempmempoolused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolused.get_name_leafdata())
                if (self.cempmempoolusedlowwatermark.is_set or self.cempmempoolusedlowwatermark.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolusedlowwatermark.get_name_leafdata())
                if (self.cempmempoolusedlowwatermarkovrflw.is_set or self.cempmempoolusedlowwatermarkovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolusedlowwatermarkovrflw.get_name_leafdata())
                if (self.cempmempoolusedovrflw.is_set or self.cempmempoolusedovrflw.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolusedovrflw.get_name_leafdata())
                if (self.cempmempoolvalid.is_set or self.cempmempoolvalid.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmempoolvalid.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cempMemPoolIndex" or name == "cempMemPoolAllocHit" or name == "cempMemPoolAllocMiss" or name == "cempMemPoolAlternate" or name == "cempMemPoolFree" or name == "cempMemPoolFreeHit" or name == "cempMemPoolFreeMiss" or name == "cempMemPoolFreeOvrflw" or name == "cempMemPoolHCFree" or name == "cempMemPoolHCLargestFree" or name == "cempMemPoolHCLowestFree" or name == "cempMemPoolHCShared" or name == "cempMemPoolHCUsed" or name == "cempMemPoolHCUsedLowWaterMark" or name == "cempMemPoolLargestFree" or name == "cempMemPoolLargestFreeOvrflw" or name == "cempMemPoolLowestFree" or name == "cempMemPoolLowestFreeOvrflw" or name == "cempMemPoolName" or name == "cempMemPoolPlatformMemory" or name == "cempMemPoolShared" or name == "cempMemPoolSharedOvrflw" or name == "cempMemPoolType" or name == "cempMemPoolUsed" or name == "cempMemPoolUsedLowWaterMark" or name == "cempMemPoolUsedLowWaterMarkOvrflw" or name == "cempMemPoolUsedOvrflw" or name == "cempMemPoolValid"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolIndex"):
                    self.cempmempoolindex = value
                    self.cempmempoolindex.value_namespace = name_space
                    self.cempmempoolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolAllocHit"):
                    self.cempmempoolallochit = value
                    self.cempmempoolallochit.value_namespace = name_space
                    self.cempmempoolallochit.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolAllocMiss"):
                    self.cempmempoolallocmiss = value
                    self.cempmempoolallocmiss.value_namespace = name_space
                    self.cempmempoolallocmiss.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolAlternate"):
                    self.cempmempoolalternate = value
                    self.cempmempoolalternate.value_namespace = name_space
                    self.cempmempoolalternate.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolFree"):
                    self.cempmempoolfree = value
                    self.cempmempoolfree.value_namespace = name_space
                    self.cempmempoolfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolFreeHit"):
                    self.cempmempoolfreehit = value
                    self.cempmempoolfreehit.value_namespace = name_space
                    self.cempmempoolfreehit.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolFreeMiss"):
                    self.cempmempoolfreemiss = value
                    self.cempmempoolfreemiss.value_namespace = name_space
                    self.cempmempoolfreemiss.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolFreeOvrflw"):
                    self.cempmempoolfreeovrflw = value
                    self.cempmempoolfreeovrflw.value_namespace = name_space
                    self.cempmempoolfreeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolHCFree"):
                    self.cempmempoolhcfree = value
                    self.cempmempoolhcfree.value_namespace = name_space
                    self.cempmempoolhcfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolHCLargestFree"):
                    self.cempmempoolhclargestfree = value
                    self.cempmempoolhclargestfree.value_namespace = name_space
                    self.cempmempoolhclargestfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolHCLowestFree"):
                    self.cempmempoolhclowestfree = value
                    self.cempmempoolhclowestfree.value_namespace = name_space
                    self.cempmempoolhclowestfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolHCShared"):
                    self.cempmempoolhcshared = value
                    self.cempmempoolhcshared.value_namespace = name_space
                    self.cempmempoolhcshared.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolHCUsed"):
                    self.cempmempoolhcused = value
                    self.cempmempoolhcused.value_namespace = name_space
                    self.cempmempoolhcused.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolHCUsedLowWaterMark"):
                    self.cempmempoolhcusedlowwatermark = value
                    self.cempmempoolhcusedlowwatermark.value_namespace = name_space
                    self.cempmempoolhcusedlowwatermark.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolLargestFree"):
                    self.cempmempoollargestfree = value
                    self.cempmempoollargestfree.value_namespace = name_space
                    self.cempmempoollargestfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolLargestFreeOvrflw"):
                    self.cempmempoollargestfreeovrflw = value
                    self.cempmempoollargestfreeovrflw.value_namespace = name_space
                    self.cempmempoollargestfreeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolLowestFree"):
                    self.cempmempoollowestfree = value
                    self.cempmempoollowestfree.value_namespace = name_space
                    self.cempmempoollowestfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolLowestFreeOvrflw"):
                    self.cempmempoollowestfreeovrflw = value
                    self.cempmempoollowestfreeovrflw.value_namespace = name_space
                    self.cempmempoollowestfreeovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolName"):
                    self.cempmempoolname = value
                    self.cempmempoolname.value_namespace = name_space
                    self.cempmempoolname.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolPlatformMemory"):
                    self.cempmempoolplatformmemory = value
                    self.cempmempoolplatformmemory.value_namespace = name_space
                    self.cempmempoolplatformmemory.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolShared"):
                    self.cempmempoolshared = value
                    self.cempmempoolshared.value_namespace = name_space
                    self.cempmempoolshared.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolSharedOvrflw"):
                    self.cempmempoolsharedovrflw = value
                    self.cempmempoolsharedovrflw.value_namespace = name_space
                    self.cempmempoolsharedovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolType"):
                    self.cempmempooltype = value
                    self.cempmempooltype.value_namespace = name_space
                    self.cempmempooltype.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolUsed"):
                    self.cempmempoolused = value
                    self.cempmempoolused.value_namespace = name_space
                    self.cempmempoolused.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolUsedLowWaterMark"):
                    self.cempmempoolusedlowwatermark = value
                    self.cempmempoolusedlowwatermark.value_namespace = name_space
                    self.cempmempoolusedlowwatermark.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolUsedLowWaterMarkOvrflw"):
                    self.cempmempoolusedlowwatermarkovrflw = value
                    self.cempmempoolusedlowwatermarkovrflw.value_namespace = name_space
                    self.cempmempoolusedlowwatermarkovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolUsedOvrflw"):
                    self.cempmempoolusedovrflw = value
                    self.cempmempoolusedovrflw.value_namespace = name_space
                    self.cempmempoolusedovrflw.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemPoolValid"):
                    self.cempmempoolvalid = value
                    self.cempmempoolvalid.value_namespace = name_space
                    self.cempmempoolvalid.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cempmempoolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cempmempoolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cempMemPoolTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cempMemPoolEntry"):
                for c in self.cempmempoolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cempmempoolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cempMemPoolEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cempmembufferpooltable(Entity):
        """
        Entries in this table define entities (buffer pools
        in this case) which are contained in an entity 
        (memory pool) defined by an entry from
        cempMemPoolTable.
        \-\- Basic Pool Architecture \-\-
        1)Pools are classified as being either Static or 
          Dynamic. Static pools make no attempt to increase 
          the number of buffers contained within them if the 
          number of free buffers (cempMemBufferFree) are less
          than the number of minimum buffers (cempMemBufferMin).
          With Dynamic pools, the pool attempts to meet the 
          demands of its users.
        2)Buffers in a pool are classified as being either 
          Permanent or Temporary. Permanent buffers, as their
          name suggests, are always in the pool and are never
          destroyed unless the number of permanent buffers 
          (cempMemBufferPermanent) is changed. Temporary
          buffers are transient buffers that are created in
          dynamic pools whenever the free count 
          (cempMemBufferFree) of buffers in the pool drops 
          below the minimum (cempMemBufferMin).
        3)Buffers pools are classified as either Public or 
          Private. Public pools are available for all users 
          to allocate buffers from. Private pools are
          primarily used by interface drivers.
        
        .. attribute:: cempmembufferpoolentry
        
        	This contains all the memory buffer pool configurations object values. The  entPhysicalIndex identifies the entity on which memory buffer pools are present
        	**type**\: list of    :py:class:`Cempmembufferpoolentry <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry>`
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CiscoEnhancedMempoolMib.Cempmembufferpooltable, self).__init__()

            self.yang_name = "cempMemBufferPoolTable"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"

            self.cempmembufferpoolentry = YList(self)

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
                        super(CiscoEnhancedMempoolMib.Cempmembufferpooltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnhancedMempoolMib.Cempmembufferpooltable, self).__setattr__(name, value)


        class Cempmembufferpoolentry(Entity):
            """
            This contains all the memory buffer pool
            configurations object values. The 
            entPhysicalIndex identifies the entity on which
            memory buffer pools are present.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cempmembufferpoolindex  <key>
            
            	Within a physical entity, a unique value used to represent each buffer pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferdynamic
            
            	Boolean poolDynamic; if TRUE, the number of buffers in the pool is adjusted (adding more packet buffers  or deleting excesses) dynamically by the background  process. If FALSE, the number of buffers in the pool  is never adjusted, even if it falls below the minimum, or to zero
            	**type**\:  bool
            
            .. attribute:: cempmembufferfailures
            
            	The number of failures to grant a buffer to a requester due to reasons other than insufficient  memory. For example, in systems where there are  different execution contexts, it may be too expensive to create new buffers when running in certain contexts. In those cases it may be  preferable to fail the request
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferfree
            
            	Indicates the current number of free buffers in the buffer pool on the physical entity. Note that the cempMemBufferFree is less than or equal  to cempMemBufferTotal
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferfreehit
            
            	Indicates the number of successful frees/deallocations from the buffer pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferfreemiss
            
            	Indicates the number of unsuccessful attempts to free/deallocate a buffer from the buffer pool.  For example, this could be due to ownership errors where the application that did not assign the  buffer is trying to free it
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffergrow
            
            	The number of buffers that have been created in the pool when the number of free buffers(cempMemBufferFree) was less than minimum(cempMemBufferMix)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferhit
            
            	Indicates the number of buffers successfully allocated from the buffer pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffermax
            
            	Indicates the maximum number of free buffers allowed in the buffer pool or high\-water mark (hwm). For example of its usage \: If cempMemBufferFree > cempMemBufferMax & pool is  dynamic, then signal for trim of particular buffer pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffermempoolindex
            
            	This index corresponds to the memory pool (with cemMemPoolIndex as index in cempMemPoolTable)  from which buffers are allocated
            	**type**\:  int
            
            	**range:** 0..2147483647
            
            .. attribute:: cempmembuffermin
            
            	Indicates the minimum number of free buffers allowed in the buffer pool or low\-water mark (lwm).  For example of its usage \: If cempMemBufferFree < cempMemBufferMin & pool is  dynamic, then signal for growth of particular buffer pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffermiss
            
            	Indicates the number of times a buffer has been requested, but no buffers were available in the buffer pool, or when there were fewer than min  buffers(cempMemBufferMin) in the buffer pool. Note \: For interface pools, a miss is actually  a fall back to its corresponding public buffer pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffername
            
            	A textual name assigned to the buffer pool. This object is suitable for output to a human operator, and may also be used to distinguish among the various buffer types. For example\: 'Small', 'Big', 'Serial0/1' etc
            	**type**\:  str
            
            .. attribute:: cempmembuffernostorage
            
            	The number of times the system tried to create new buffers, but could not due to insufficient free  memory in the system
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferpeak
            
            	Indicates the peak number of buffers in pool on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferpeaktime
            
            	Indicates the time of most recent change in the peak number of buffers (cempMemBufferPeak object) in the pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferpermanent
            
            	Indicates the total number of permanent buffers in the pool on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembufferpermchange
            
            	This value is the difference of the desired number of permanent buffer & total number of permanent  buffers present in the pool. A positive value of  this object tells the number of buffers needed & a  negative value of the object tells the extra number  of buffers in the pool
            	**type**\:  int
            
            	**range:** \-2147483648..2147483647
            
            .. attribute:: cempmembuffersize
            
            	Indicates the size of buffer element in number of bytes on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**units**\: bytes
            
            .. attribute:: cempmembuffertotal
            
            	Indicates the total number of buffers (include allocated and free buffers) in the buffer pool on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffertransient
            
            	Indicates the initial number of temporary buffers in the pool on the physical entity. This object  instructs the system to create this many number of temporary extra buffers, just after a system restart.  A change in this object will be effective only after a system restart
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffertrim
            
            	The number of buffers that have been trimmed from the pool when the number of free buffers  (cempMemBufferFree) exceeded the number of max allowed buffers(cempMemBufferMax)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
            _revision = '2008-12-05'

            def __init__(self):
                super(CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry, self).__init__()

                self.yang_name = "cempMemBufferPoolEntry"
                self.yang_parent_name = "cempMemBufferPoolTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cempmembufferpoolindex = YLeaf(YType.uint32, "cempMemBufferPoolIndex")

                self.cempmembufferdynamic = YLeaf(YType.boolean, "cempMemBufferDynamic")

                self.cempmembufferfailures = YLeaf(YType.uint32, "cempMemBufferFailures")

                self.cempmembufferfree = YLeaf(YType.uint32, "cempMemBufferFree")

                self.cempmembufferfreehit = YLeaf(YType.uint32, "cempMemBufferFreeHit")

                self.cempmembufferfreemiss = YLeaf(YType.uint32, "cempMemBufferFreeMiss")

                self.cempmembuffergrow = YLeaf(YType.uint32, "cempMemBufferGrow")

                self.cempmembufferhit = YLeaf(YType.uint32, "cempMemBufferHit")

                self.cempmembuffermax = YLeaf(YType.uint32, "cempMemBufferMax")

                self.cempmembuffermempoolindex = YLeaf(YType.int32, "cempMemBufferMemPoolIndex")

                self.cempmembuffermin = YLeaf(YType.uint32, "cempMemBufferMin")

                self.cempmembuffermiss = YLeaf(YType.uint32, "cempMemBufferMiss")

                self.cempmembuffername = YLeaf(YType.str, "cempMemBufferName")

                self.cempmembuffernostorage = YLeaf(YType.uint32, "cempMemBufferNoStorage")

                self.cempmembufferpeak = YLeaf(YType.uint32, "cempMemBufferPeak")

                self.cempmembufferpeaktime = YLeaf(YType.uint32, "cempMemBufferPeakTime")

                self.cempmembufferpermanent = YLeaf(YType.uint32, "cempMemBufferPermanent")

                self.cempmembufferpermchange = YLeaf(YType.int32, "cempMemBufferPermChange")

                self.cempmembuffersize = YLeaf(YType.uint32, "cempMemBufferSize")

                self.cempmembuffertotal = YLeaf(YType.uint32, "cempMemBufferTotal")

                self.cempmembuffertransient = YLeaf(YType.uint32, "cempMemBufferTransient")

                self.cempmembuffertrim = YLeaf(YType.uint32, "cempMemBufferTrim")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cempmembufferpoolindex",
                                "cempmembufferdynamic",
                                "cempmembufferfailures",
                                "cempmembufferfree",
                                "cempmembufferfreehit",
                                "cempmembufferfreemiss",
                                "cempmembuffergrow",
                                "cempmembufferhit",
                                "cempmembuffermax",
                                "cempmembuffermempoolindex",
                                "cempmembuffermin",
                                "cempmembuffermiss",
                                "cempmembuffername",
                                "cempmembuffernostorage",
                                "cempmembufferpeak",
                                "cempmembufferpeaktime",
                                "cempmembufferpermanent",
                                "cempmembufferpermchange",
                                "cempmembuffersize",
                                "cempmembuffertotal",
                                "cempmembuffertransient",
                                "cempmembuffertrim") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cempmembufferpoolindex.is_set or
                    self.cempmembufferdynamic.is_set or
                    self.cempmembufferfailures.is_set or
                    self.cempmembufferfree.is_set or
                    self.cempmembufferfreehit.is_set or
                    self.cempmembufferfreemiss.is_set or
                    self.cempmembuffergrow.is_set or
                    self.cempmembufferhit.is_set or
                    self.cempmembuffermax.is_set or
                    self.cempmembuffermempoolindex.is_set or
                    self.cempmembuffermin.is_set or
                    self.cempmembuffermiss.is_set or
                    self.cempmembuffername.is_set or
                    self.cempmembuffernostorage.is_set or
                    self.cempmembufferpeak.is_set or
                    self.cempmembufferpeaktime.is_set or
                    self.cempmembufferpermanent.is_set or
                    self.cempmembufferpermchange.is_set or
                    self.cempmembuffersize.is_set or
                    self.cempmembuffertotal.is_set or
                    self.cempmembuffertransient.is_set or
                    self.cempmembuffertrim.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cempmembufferpoolindex.yfilter != YFilter.not_set or
                    self.cempmembufferdynamic.yfilter != YFilter.not_set or
                    self.cempmembufferfailures.yfilter != YFilter.not_set or
                    self.cempmembufferfree.yfilter != YFilter.not_set or
                    self.cempmembufferfreehit.yfilter != YFilter.not_set or
                    self.cempmembufferfreemiss.yfilter != YFilter.not_set or
                    self.cempmembuffergrow.yfilter != YFilter.not_set or
                    self.cempmembufferhit.yfilter != YFilter.not_set or
                    self.cempmembuffermax.yfilter != YFilter.not_set or
                    self.cempmembuffermempoolindex.yfilter != YFilter.not_set or
                    self.cempmembuffermin.yfilter != YFilter.not_set or
                    self.cempmembuffermiss.yfilter != YFilter.not_set or
                    self.cempmembuffername.yfilter != YFilter.not_set or
                    self.cempmembuffernostorage.yfilter != YFilter.not_set or
                    self.cempmembufferpeak.yfilter != YFilter.not_set or
                    self.cempmembufferpeaktime.yfilter != YFilter.not_set or
                    self.cempmembufferpermanent.yfilter != YFilter.not_set or
                    self.cempmembufferpermchange.yfilter != YFilter.not_set or
                    self.cempmembuffersize.yfilter != YFilter.not_set or
                    self.cempmembuffertotal.yfilter != YFilter.not_set or
                    self.cempmembuffertransient.yfilter != YFilter.not_set or
                    self.cempmembuffertrim.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cempMemBufferPoolEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cempMemBufferPoolIndex='" + self.cempmembufferpoolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/cempMemBufferPoolTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cempmembufferpoolindex.is_set or self.cempmembufferpoolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferpoolindex.get_name_leafdata())
                if (self.cempmembufferdynamic.is_set or self.cempmembufferdynamic.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferdynamic.get_name_leafdata())
                if (self.cempmembufferfailures.is_set or self.cempmembufferfailures.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferfailures.get_name_leafdata())
                if (self.cempmembufferfree.is_set or self.cempmembufferfree.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferfree.get_name_leafdata())
                if (self.cempmembufferfreehit.is_set or self.cempmembufferfreehit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferfreehit.get_name_leafdata())
                if (self.cempmembufferfreemiss.is_set or self.cempmembufferfreemiss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferfreemiss.get_name_leafdata())
                if (self.cempmembuffergrow.is_set or self.cempmembuffergrow.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffergrow.get_name_leafdata())
                if (self.cempmembufferhit.is_set or self.cempmembufferhit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferhit.get_name_leafdata())
                if (self.cempmembuffermax.is_set or self.cempmembuffermax.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffermax.get_name_leafdata())
                if (self.cempmembuffermempoolindex.is_set or self.cempmembuffermempoolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffermempoolindex.get_name_leafdata())
                if (self.cempmembuffermin.is_set or self.cempmembuffermin.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffermin.get_name_leafdata())
                if (self.cempmembuffermiss.is_set or self.cempmembuffermiss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffermiss.get_name_leafdata())
                if (self.cempmembuffername.is_set or self.cempmembuffername.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffername.get_name_leafdata())
                if (self.cempmembuffernostorage.is_set or self.cempmembuffernostorage.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffernostorage.get_name_leafdata())
                if (self.cempmembufferpeak.is_set or self.cempmembufferpeak.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferpeak.get_name_leafdata())
                if (self.cempmembufferpeaktime.is_set or self.cempmembufferpeaktime.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferpeaktime.get_name_leafdata())
                if (self.cempmembufferpermanent.is_set or self.cempmembufferpermanent.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferpermanent.get_name_leafdata())
                if (self.cempmembufferpermchange.is_set or self.cempmembufferpermchange.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferpermchange.get_name_leafdata())
                if (self.cempmembuffersize.is_set or self.cempmembuffersize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffersize.get_name_leafdata())
                if (self.cempmembuffertotal.is_set or self.cempmembuffertotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffertotal.get_name_leafdata())
                if (self.cempmembuffertransient.is_set or self.cempmembuffertransient.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffertransient.get_name_leafdata())
                if (self.cempmembuffertrim.is_set or self.cempmembuffertrim.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffertrim.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cempMemBufferPoolIndex" or name == "cempMemBufferDynamic" or name == "cempMemBufferFailures" or name == "cempMemBufferFree" or name == "cempMemBufferFreeHit" or name == "cempMemBufferFreeMiss" or name == "cempMemBufferGrow" or name == "cempMemBufferHit" or name == "cempMemBufferMax" or name == "cempMemBufferMemPoolIndex" or name == "cempMemBufferMin" or name == "cempMemBufferMiss" or name == "cempMemBufferName" or name == "cempMemBufferNoStorage" or name == "cempMemBufferPeak" or name == "cempMemBufferPeakTime" or name == "cempMemBufferPermanent" or name == "cempMemBufferPermChange" or name == "cempMemBufferSize" or name == "cempMemBufferTotal" or name == "cempMemBufferTransient" or name == "cempMemBufferTrim"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferPoolIndex"):
                    self.cempmembufferpoolindex = value
                    self.cempmembufferpoolindex.value_namespace = name_space
                    self.cempmembufferpoolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferDynamic"):
                    self.cempmembufferdynamic = value
                    self.cempmembufferdynamic.value_namespace = name_space
                    self.cempmembufferdynamic.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferFailures"):
                    self.cempmembufferfailures = value
                    self.cempmembufferfailures.value_namespace = name_space
                    self.cempmembufferfailures.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferFree"):
                    self.cempmembufferfree = value
                    self.cempmembufferfree.value_namespace = name_space
                    self.cempmembufferfree.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferFreeHit"):
                    self.cempmembufferfreehit = value
                    self.cempmembufferfreehit.value_namespace = name_space
                    self.cempmembufferfreehit.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferFreeMiss"):
                    self.cempmembufferfreemiss = value
                    self.cempmembufferfreemiss.value_namespace = name_space
                    self.cempmembufferfreemiss.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferGrow"):
                    self.cempmembuffergrow = value
                    self.cempmembuffergrow.value_namespace = name_space
                    self.cempmembuffergrow.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferHit"):
                    self.cempmembufferhit = value
                    self.cempmembufferhit.value_namespace = name_space
                    self.cempmembufferhit.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferMax"):
                    self.cempmembuffermax = value
                    self.cempmembuffermax.value_namespace = name_space
                    self.cempmembuffermax.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferMemPoolIndex"):
                    self.cempmembuffermempoolindex = value
                    self.cempmembuffermempoolindex.value_namespace = name_space
                    self.cempmembuffermempoolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferMin"):
                    self.cempmembuffermin = value
                    self.cempmembuffermin.value_namespace = name_space
                    self.cempmembuffermin.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferMiss"):
                    self.cempmembuffermiss = value
                    self.cempmembuffermiss.value_namespace = name_space
                    self.cempmembuffermiss.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferName"):
                    self.cempmembuffername = value
                    self.cempmembuffername.value_namespace = name_space
                    self.cempmembuffername.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferNoStorage"):
                    self.cempmembuffernostorage = value
                    self.cempmembuffernostorage.value_namespace = name_space
                    self.cempmembuffernostorage.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferPeak"):
                    self.cempmembufferpeak = value
                    self.cempmembufferpeak.value_namespace = name_space
                    self.cempmembufferpeak.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferPeakTime"):
                    self.cempmembufferpeaktime = value
                    self.cempmembufferpeaktime.value_namespace = name_space
                    self.cempmembufferpeaktime.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferPermanent"):
                    self.cempmembufferpermanent = value
                    self.cempmembufferpermanent.value_namespace = name_space
                    self.cempmembufferpermanent.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferPermChange"):
                    self.cempmembufferpermchange = value
                    self.cempmembufferpermchange.value_namespace = name_space
                    self.cempmembufferpermchange.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferSize"):
                    self.cempmembuffersize = value
                    self.cempmembuffersize.value_namespace = name_space
                    self.cempmembuffersize.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferTotal"):
                    self.cempmembuffertotal = value
                    self.cempmembuffertotal.value_namespace = name_space
                    self.cempmembuffertotal.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferTransient"):
                    self.cempmembuffertransient = value
                    self.cempmembuffertransient.value_namespace = name_space
                    self.cempmembuffertransient.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferTrim"):
                    self.cempmembuffertrim = value
                    self.cempmembuffertrim.value_namespace = name_space
                    self.cempmembuffertrim.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cempmembufferpoolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cempmembufferpoolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cempMemBufferPoolTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cempMemBufferPoolEntry"):
                for c in self.cempmembufferpoolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cempmembufferpoolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cempMemBufferPoolEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass


    class Cempmembuffercachepooltable(Entity):
        """
        A table that lists the cache buffer pools
        configured on a managed system. 
        1)To provide a noticeable performance boost, 
          Cache Pool can be used. A Cache Pool is effectively
          a lookaside list of free buffers that can be 
          accessed quickly. Cache Pool is tied to Buffer Pool. 
        2)Cache pools can optionally have a threshold value
          on the number of cache buffers used in a pool. This
          can provide flow control management by having a 
          implementation specific approach such as invoking a
          vector when pool cache rises above the optional 
          threshold set for it on creation.
        
        .. attribute:: cempmembuffercachepoolentry
        
        	Each entry represents one of the cache buffer pools available in the system and it contains the parameters configured for it. Note \: cempMemBufferCachePoolTable has a sparse dependency with cempMemBufferPoolTable (i.e all the entires in cempMemBufferPoolTable need not have an entry in cempMemBufferCachePoolTable
        	**type**\: list of    :py:class:`Cempmembuffercachepoolentry <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry>`
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CiscoEnhancedMempoolMib.Cempmembuffercachepooltable, self).__init__()

            self.yang_name = "cempMemBufferCachePoolTable"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"

            self.cempmembuffercachepoolentry = YList(self)

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
                        super(CiscoEnhancedMempoolMib.Cempmembuffercachepooltable, self).__setattr__(name, value)
                    else:
                        self.__dict__[name].set(value)
                else:
                    if hasattr(value, "parent") and name != "parent":
                        if hasattr(value, "is_presence_container") and value.is_presence_container:
                            value.parent = self
                        elif value.parent is None and value.yang_name in self._children_yang_names:
                            value.parent = self
                    super(CiscoEnhancedMempoolMib.Cempmembuffercachepooltable, self).__setattr__(name, value)


        class Cempmembuffercachepoolentry(Entity):
            """
            Each entry represents one of the cache buffer pools
            available in the system and it contains the
            parameters configured for it.
            Note \: cempMemBufferCachePoolTable has a sparse
            dependency with cempMemBufferPoolTable (i.e all the
            entires in cempMemBufferPoolTable need not have an
            entry in cempMemBufferCachePoolTable.
            
            .. attribute:: entphysicalindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.EntityMib.Entphysicaltable.Entphysicalentry>`
            
            .. attribute:: cempmembufferpoolindex  <key>
            
            	
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cempmembufferpoolindex <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry>`
            
            .. attribute:: cempmembuffercachehit
            
            	Indicates the number of buffers successfully allocated from the cache pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffercachemiss
            
            	Indicates the number of times a buffer has been requested, but no buffers were available in the cache pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffercachesize
            
            	Indicates the number of buffers in the cache pool on the physical entity
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffercachethreshold
            
            	Indicates the threshold limit for number of cache buffers used(cempMemBufferCacheUsed)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffercachethresholdcount
            
            	Indicates how many times the number of cache buffers used(cempMemBufferCacheUsed) has crossed the threshold value(cempMemBufferCacheThreshold)
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffercachetotal
            
            	Indicates the maximum number of free buffers allowed in the cache pool
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            .. attribute:: cempmembuffercacheused
            
            	Indicates the number of cache buffers from the pool that are currently used on the physical entity. Note that the cempMemBufferCacheUsed is less than or  equal to cempMemBufferCacheTotal
            	**type**\:  int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
            _revision = '2008-12-05'

            def __init__(self):
                super(CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry, self).__init__()

                self.yang_name = "cempMemBufferCachePoolEntry"
                self.yang_parent_name = "cempMemBufferCachePoolTable"

                self.entphysicalindex = YLeaf(YType.str, "entPhysicalIndex")

                self.cempmembufferpoolindex = YLeaf(YType.str, "cempMemBufferPoolIndex")

                self.cempmembuffercachehit = YLeaf(YType.uint32, "cempMemBufferCacheHit")

                self.cempmembuffercachemiss = YLeaf(YType.uint32, "cempMemBufferCacheMiss")

                self.cempmembuffercachesize = YLeaf(YType.uint32, "cempMemBufferCacheSize")

                self.cempmembuffercachethreshold = YLeaf(YType.uint32, "cempMemBufferCacheThreshold")

                self.cempmembuffercachethresholdcount = YLeaf(YType.uint32, "cempMemBufferCacheThresholdCount")

                self.cempmembuffercachetotal = YLeaf(YType.uint32, "cempMemBufferCacheTotal")

                self.cempmembuffercacheused = YLeaf(YType.uint32, "cempMemBufferCacheUsed")

            def __setattr__(self, name, value):
                self._check_monkey_patching_error(name, value)
                with _handle_type_error():
                    if name in self.__dict__ and isinstance(self.__dict__[name], YList):
                        raise YPYModelError("Attempt to assign value of '{}' to YList ldata. "
                                            "Please use list append or extend method."
                                            .format(value))
                    if isinstance(value, Enum.YLeaf):
                        value = value.name
                    if name in ("entphysicalindex",
                                "cempmembufferpoolindex",
                                "cempmembuffercachehit",
                                "cempmembuffercachemiss",
                                "cempmembuffercachesize",
                                "cempmembuffercachethreshold",
                                "cempmembuffercachethresholdcount",
                                "cempmembuffercachetotal",
                                "cempmembuffercacheused") and name in self.__dict__:
                        if isinstance(value, YLeaf):
                            self.__dict__[name].set(value.get())
                        elif isinstance(value, YLeafList):
                            super(CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry, self).__setattr__(name, value)
                        else:
                            self.__dict__[name].set(value)
                    else:
                        if hasattr(value, "parent") and name != "parent":
                            if hasattr(value, "is_presence_container") and value.is_presence_container:
                                value.parent = self
                            elif value.parent is None and value.yang_name in self._children_yang_names:
                                value.parent = self
                        super(CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry, self).__setattr__(name, value)

            def has_data(self):
                return (
                    self.entphysicalindex.is_set or
                    self.cempmembufferpoolindex.is_set or
                    self.cempmembuffercachehit.is_set or
                    self.cempmembuffercachemiss.is_set or
                    self.cempmembuffercachesize.is_set or
                    self.cempmembuffercachethreshold.is_set or
                    self.cempmembuffercachethresholdcount.is_set or
                    self.cempmembuffercachetotal.is_set or
                    self.cempmembuffercacheused.is_set)

            def has_operation(self):
                return (
                    self.yfilter != YFilter.not_set or
                    self.entphysicalindex.yfilter != YFilter.not_set or
                    self.cempmembufferpoolindex.yfilter != YFilter.not_set or
                    self.cempmembuffercachehit.yfilter != YFilter.not_set or
                    self.cempmembuffercachemiss.yfilter != YFilter.not_set or
                    self.cempmembuffercachesize.yfilter != YFilter.not_set or
                    self.cempmembuffercachethreshold.yfilter != YFilter.not_set or
                    self.cempmembuffercachethresholdcount.yfilter != YFilter.not_set or
                    self.cempmembuffercachetotal.yfilter != YFilter.not_set or
                    self.cempmembuffercacheused.yfilter != YFilter.not_set)

            def get_segment_path(self):
                path_buffer = ""
                path_buffer = "cempMemBufferCachePoolEntry" + "[entPhysicalIndex='" + self.entphysicalindex.get() + "']" + "[cempMemBufferPoolIndex='" + self.cempmembufferpoolindex.get() + "']" + path_buffer

                return path_buffer

            def get_entity_path(self, ancestor):
                path_buffer = ""
                if (ancestor is None):
                    path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/cempMemBufferCachePoolTable/%s" % self.get_segment_path()
                else:
                    path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

                leaf_name_data = LeafDataList()
                if (self.entphysicalindex.is_set or self.entphysicalindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.entphysicalindex.get_name_leafdata())
                if (self.cempmembufferpoolindex.is_set or self.cempmembufferpoolindex.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembufferpoolindex.get_name_leafdata())
                if (self.cempmembuffercachehit.is_set or self.cempmembuffercachehit.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffercachehit.get_name_leafdata())
                if (self.cempmembuffercachemiss.is_set or self.cempmembuffercachemiss.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffercachemiss.get_name_leafdata())
                if (self.cempmembuffercachesize.is_set or self.cempmembuffercachesize.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffercachesize.get_name_leafdata())
                if (self.cempmembuffercachethreshold.is_set or self.cempmembuffercachethreshold.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffercachethreshold.get_name_leafdata())
                if (self.cempmembuffercachethresholdcount.is_set or self.cempmembuffercachethresholdcount.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffercachethresholdcount.get_name_leafdata())
                if (self.cempmembuffercachetotal.is_set or self.cempmembuffercachetotal.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffercachetotal.get_name_leafdata())
                if (self.cempmembuffercacheused.is_set or self.cempmembuffercacheused.yfilter != YFilter.not_set):
                    leaf_name_data.append(self.cempmembuffercacheused.get_name_leafdata())

                entity_path = EntityPath(path_buffer, leaf_name_data)
                return entity_path

            def get_child_by_name(self, child_yang_name, segment_path):
                child = self._get_child_by_seg_name([child_yang_name, segment_path])
                if child is not None:
                    return child

                return None

            def has_leaf_or_child_of_name(self, name):
                if(name == "entPhysicalIndex" or name == "cempMemBufferPoolIndex" or name == "cempMemBufferCacheHit" or name == "cempMemBufferCacheMiss" or name == "cempMemBufferCacheSize" or name == "cempMemBufferCacheThreshold" or name == "cempMemBufferCacheThresholdCount" or name == "cempMemBufferCacheTotal" or name == "cempMemBufferCacheUsed"):
                    return True
                return False

            def set_value(self, value_path, value, name_space, name_space_prefix):
                if(value_path == "entPhysicalIndex"):
                    self.entphysicalindex = value
                    self.entphysicalindex.value_namespace = name_space
                    self.entphysicalindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferPoolIndex"):
                    self.cempmembufferpoolindex = value
                    self.cempmembufferpoolindex.value_namespace = name_space
                    self.cempmembufferpoolindex.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferCacheHit"):
                    self.cempmembuffercachehit = value
                    self.cempmembuffercachehit.value_namespace = name_space
                    self.cempmembuffercachehit.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferCacheMiss"):
                    self.cempmembuffercachemiss = value
                    self.cempmembuffercachemiss.value_namespace = name_space
                    self.cempmembuffercachemiss.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferCacheSize"):
                    self.cempmembuffercachesize = value
                    self.cempmembuffercachesize.value_namespace = name_space
                    self.cempmembuffercachesize.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferCacheThreshold"):
                    self.cempmembuffercachethreshold = value
                    self.cempmembuffercachethreshold.value_namespace = name_space
                    self.cempmembuffercachethreshold.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferCacheThresholdCount"):
                    self.cempmembuffercachethresholdcount = value
                    self.cempmembuffercachethresholdcount.value_namespace = name_space
                    self.cempmembuffercachethresholdcount.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferCacheTotal"):
                    self.cempmembuffercachetotal = value
                    self.cempmembuffercachetotal.value_namespace = name_space
                    self.cempmembuffercachetotal.value_namespace_prefix = name_space_prefix
                if(value_path == "cempMemBufferCacheUsed"):
                    self.cempmembuffercacheused = value
                    self.cempmembuffercacheused.value_namespace = name_space
                    self.cempmembuffercacheused.value_namespace_prefix = name_space_prefix

        def has_data(self):
            for c in self.cempmembuffercachepoolentry:
                if (c.has_data()):
                    return True
            return False

        def has_operation(self):
            for c in self.cempmembuffercachepoolentry:
                if (c.has_operation()):
                    return True
            return self.yfilter != YFilter.not_set

        def get_segment_path(self):
            path_buffer = ""
            path_buffer = "cempMemBufferCachePoolTable" + path_buffer

            return path_buffer

        def get_entity_path(self, ancestor):
            path_buffer = ""
            if (ancestor is None):
                path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self.get_segment_path()
            else:
                path_buffer = _get_relative_entity_path(self, ancestor, path_buffer)

            leaf_name_data = LeafDataList()

            entity_path = EntityPath(path_buffer, leaf_name_data)
            return entity_path

        def get_child_by_name(self, child_yang_name, segment_path):
            child = self._get_child_by_seg_name([child_yang_name, segment_path])
            if child is not None:
                return child

            if (child_yang_name == "cempMemBufferCachePoolEntry"):
                for c in self.cempmembuffercachepoolentry:
                    segment = c.get_segment_path()
                    if (segment_path == segment):
                        return c
                c = CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry()
                c.parent = self
                local_reference_key = "ydk::seg::%s" % segment_path
                self._local_refs[local_reference_key] = c
                self.cempmembuffercachepoolentry.append(c)
                return c

            return None

        def has_leaf_or_child_of_name(self, name):
            if(name == "cempMemBufferCachePoolEntry"):
                return True
            return False

        def set_value(self, value_path, value, name_space, name_space_prefix):
            pass

    def has_data(self):
        return (
            (self.cempmembuffercachepooltable is not None and self.cempmembuffercachepooltable.has_data()) or
            (self.cempmembufferpooltable is not None and self.cempmembufferpooltable.has_data()) or
            (self.cempmempooltable is not None and self.cempmempooltable.has_data()) or
            (self.cempnotificationconfig is not None and self.cempnotificationconfig.has_data()))

    def has_operation(self):
        return (
            self.yfilter != YFilter.not_set or
            (self.cempmembuffercachepooltable is not None and self.cempmembuffercachepooltable.has_operation()) or
            (self.cempmembufferpooltable is not None and self.cempmembufferpooltable.has_operation()) or
            (self.cempmempooltable is not None and self.cempmempooltable.has_operation()) or
            (self.cempnotificationconfig is not None and self.cempnotificationconfig.has_operation()))

    def get_segment_path(self):
        path_buffer = ""
        path_buffer = "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB" + path_buffer

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

        if (child_yang_name == "cempMemBufferCachePoolTable"):
            if (self.cempmembuffercachepooltable is None):
                self.cempmembuffercachepooltable = CiscoEnhancedMempoolMib.Cempmembuffercachepooltable()
                self.cempmembuffercachepooltable.parent = self
                self._children_name_map["cempmembuffercachepooltable"] = "cempMemBufferCachePoolTable"
            return self.cempmembuffercachepooltable

        if (child_yang_name == "cempMemBufferPoolTable"):
            if (self.cempmembufferpooltable is None):
                self.cempmembufferpooltable = CiscoEnhancedMempoolMib.Cempmembufferpooltable()
                self.cempmembufferpooltable.parent = self
                self._children_name_map["cempmembufferpooltable"] = "cempMemBufferPoolTable"
            return self.cempmembufferpooltable

        if (child_yang_name == "cempMemPoolTable"):
            if (self.cempmempooltable is None):
                self.cempmempooltable = CiscoEnhancedMempoolMib.Cempmempooltable()
                self.cempmempooltable.parent = self
                self._children_name_map["cempmempooltable"] = "cempMemPoolTable"
            return self.cempmempooltable

        if (child_yang_name == "cempNotificationConfig"):
            if (self.cempnotificationconfig is None):
                self.cempnotificationconfig = CiscoEnhancedMempoolMib.Cempnotificationconfig()
                self.cempnotificationconfig.parent = self
                self._children_name_map["cempnotificationconfig"] = "cempNotificationConfig"
            return self.cempnotificationconfig

        return None

    def has_leaf_or_child_of_name(self, name):
        if(name == "cempMemBufferCachePoolTable" or name == "cempMemBufferPoolTable" or name == "cempMemPoolTable" or name == "cempNotificationConfig"):
            return True
        return False

    def set_value(self, value_path, value, name_space, name_space_prefix):
        pass

    def clone_ptr(self):
        self._top_entity = CiscoEnhancedMempoolMib()
        return self._top_entity

