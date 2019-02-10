""" CISCO_ENHANCED_MEMPOOL_MIB 

New MIB module for monitoring the memory pools
of all physical entities on a managed system.

"""
from collections import OrderedDict

from ydk.types import Entity, EntityPath, Identity, Enum, YType, YLeaf, YLeafList, YList, LeafDataList, Bits, Empty, Decimal64
from ydk.filters import YFilter
from ydk.errors import YError, YModelError
from ydk.errors.error_handler import handle_type_error as _handle_type_error



class CempMemPoolTypes(Enum):
    """
    CempMemPoolTypes (Enum Class)

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



class CISCOENHANCEDMEMPOOLMIB(Entity):
    """
    
    
    .. attribute:: cempnotificationconfig
    
    	
    	**type**\:  :py:class:`CempNotificationConfig <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempNotificationConfig>`
    
    	**config**\: False
    
    .. attribute:: cempmempooltable
    
    	A table of memory pool monitoring entries for all physical entities on a managed system
    	**type**\:  :py:class:`CempMemPoolTable <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable>`
    
    	**config**\: False
    
    .. attribute:: cempmembufferpooltable
    
    	Entries in this table define entities (buffer pools in this case) which are contained in an entity  (memory pool) defined by an entry from cempMemPoolTable. \-\- Basic Pool Architecture \-\- 1)Pools are classified as being either Static or    Dynamic. Static pools make no attempt to increase    the number of buffers contained within them if the    number of free buffers (cempMemBufferFree) are less   than the number of minimum buffers (cempMemBufferMin).   With Dynamic pools, the pool attempts to meet the    demands of its users. 2)Buffers in a pool are classified as being either    Permanent or Temporary. Permanent buffers, as their   name suggests, are always in the pool and are never   destroyed unless the number of permanent buffers    (cempMemBufferPermanent) is changed. Temporary   buffers are transient buffers that are created in   dynamic pools whenever the free count    (cempMemBufferFree) of buffers in the pool drops    below the minimum (cempMemBufferMin). 3)Buffers pools are classified as either Public or    Private. Public pools are available for all users    to allocate buffers from. Private pools are   primarily used by interface drivers
    	**type**\:  :py:class:`CempMemBufferPoolTable <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable>`
    
    	**config**\: False
    
    .. attribute:: cempmembuffercachepooltable
    
    	A table that lists the cache buffer pools configured on a managed system.  1)To provide a noticeable performance boost,    Cache Pool can be used. A Cache Pool is effectively   a lookaside list of free buffers that can be    accessed quickly. Cache Pool is tied to Buffer Pool.  2)Cache pools can optionally have a threshold value   on the number of cache buffers used in a pool. This   can provide flow control management by having a    implementation specific approach such as invoking a   vector when pool cache rises above the optional    threshold set for it on creation
    	**type**\:  :py:class:`CempMemBufferCachePoolTable <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable>`
    
    	**config**\: False
    
    

    """

    _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
    _revision = '2008-12-05'

    def __init__(self):
        super(CISCOENHANCEDMEMPOOLMIB, self).__init__()
        self._top_entity = None

        self.yang_name = "CISCO-ENHANCED-MEMPOOL-MIB"
        self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"
        self.is_top_level_class = True
        self.has_list_ancestor = False
        self.ylist_key_names = []
        self._child_classes = OrderedDict([("cempNotificationConfig", ("cempnotificationconfig", CISCOENHANCEDMEMPOOLMIB.CempNotificationConfig)), ("cempMemPoolTable", ("cempmempooltable", CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable)), ("cempMemBufferPoolTable", ("cempmembufferpooltable", CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable)), ("cempMemBufferCachePoolTable", ("cempmembuffercachepooltable", CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable))])
        self._leafs = OrderedDict()

        self.cempnotificationconfig = CISCOENHANCEDMEMPOOLMIB.CempNotificationConfig()
        self.cempnotificationconfig.parent = self
        self._children_name_map["cempnotificationconfig"] = "cempNotificationConfig"

        self.cempmempooltable = CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable()
        self.cempmempooltable.parent = self
        self._children_name_map["cempmempooltable"] = "cempMemPoolTable"

        self.cempmembufferpooltable = CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable()
        self.cempmembufferpooltable.parent = self
        self._children_name_map["cempmembufferpooltable"] = "cempMemBufferPoolTable"

        self.cempmembuffercachepooltable = CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable()
        self.cempmembuffercachepooltable.parent = self
        self._children_name_map["cempmembuffercachepooltable"] = "cempMemBufferCachePoolTable"
        self._segment_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB"
        self._is_frozen = True

    def __setattr__(self, name, value):
        self._perform_setattr(CISCOENHANCEDMEMPOOLMIB, [], name, value)


    class CempNotificationConfig(Entity):
        """
        
        
        .. attribute:: cempmembuffernotifyenabled
        
        	This variable controls generation of the cempMemBufferNotify.  When this variable is 'true', generation of cempMemBufferNotify is enabled.  When this variable is 'false', generation of cempMemBufferNotify is disabled
        	**type**\: bool
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CISCOENHANCEDMEMPOOLMIB.CempNotificationConfig, self).__init__()

            self.yang_name = "cempNotificationConfig"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([])
            self._leafs = OrderedDict([
                ('cempmembuffernotifyenabled', (YLeaf(YType.boolean, 'cempMemBufferNotifyEnabled'), ['bool'])),
            ])
            self.cempmembuffernotifyenabled = None
            self._segment_path = lambda: "cempNotificationConfig"
            self._absolute_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENHANCEDMEMPOOLMIB.CempNotificationConfig, ['cempmembuffernotifyenabled'], name, value)



    class CempMemPoolTable(Entity):
        """
        A table of memory pool monitoring entries for all
        physical entities on a managed system.
        
        .. attribute:: cempmempoolentry
        
        	An entry in the memory pool monitoring table
        	**type**\: list of  		 :py:class:`CempMemPoolEntry <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable.CempMemPoolEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable, self).__init__()

            self.yang_name = "cempMemPoolTable"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cempMemPoolEntry", ("cempmempoolentry", CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable.CempMemPoolEntry))])
            self._leafs = OrderedDict()

            self.cempmempoolentry = YList(self)
            self._segment_path = lambda: "cempMemPoolTable"
            self._absolute_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable, [], name, value)


        class CempMemPoolEntry(Entity):
            """
            An entry in the memory pool monitoring table.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cempmempoolindex  (key)
            
            	Within each physical entity, the unique value greater than zero, used to represent each memory pool.   It is recommended that values are assigned contiguously starting from 1
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**config**\: False
            
            .. attribute:: cempmempooltype
            
            	The type of memory pool for which this entry contains information
            	**type**\:  :py:class:`CempMemPoolTypes <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CempMemPoolTypes>`
            
            	**config**\: False
            
            .. attribute:: cempmempoolname
            
            	A textual name assigned to the memory pool. This object is suitable for output to a human operator, and may also be used to distinguish among the various pool types
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cempmempoolplatformmemory
            
            	An indication of the platform\-specific memory pool type. The associated instance of cempMemPoolType is used to indicate the general type of memory pool.  If no platform specific memory hardware type identifier exists for this physical entity, or the value is unknown by this agent, then the value { 0 0 } is returned
            	**type**\: str
            
            	**pattern:** (([0\-1](\\.[1\-3]?[0\-9]))\|(2\\.(0\|([1\-9]\\d\*))))(\\.(0\|([1\-9]\\d\*)))\*
            
            	**config**\: False
            
            .. attribute:: cempmempoolalternate
            
            	Indicates whether or not this memory pool has an alternate pool configured.  Alternate pools are used for fallback when the current pool runs out of memory.  If an instance of this object has a value of zero, then this pool does not have an alternate.  Otherwise the value of this object is the same as the value of cempMemPoolType of the alternate pool
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cempmempoolvalid
            
            	Indicates whether or not cempMemPoolUsed, cempMemPoolFree, cempMemPoolLargestFree and  cempMemPoolLowestFree in this entry contain accurate  data. If an instance of this object has the value  false (which in and of itself indicates an internal  error condition), the values of these objects in the conceptual row may contain inaccurate  information (specifically, the reported values may be  less than the actual values)
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cempmempoolused
            
            	Indicates the number of bytes from the memory pool that are currently in use by applications on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolfree
            
            	Indicates the number of bytes from the memory pool that are currently unused on the physical entity.  Note that the sum of cempMemPoolUsed and cempMemPoolFree  is the total amount of memory in the pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollargestfree
            
            	Indicates the largest number of contiguous bytes from the memory pool that are currently unused on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollowestfree
            
            	The lowest amount of available memory in the memory pool recorded at any time during the operation of the system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolusedlowwatermark
            
            	Indicates the lowest number of bytes from the memory pool that have been used by applications on the physical entity since sysUpTime.Similarly,the Used High Watermark indicates the largest number of bytes from the memory pool that have been used by applications on the physical entity since sysUpTime.This can be derived as follows\: Used High Watermark = cempMemPoolUsed + cempMemPoolFree  \- cempMemPoolLowestFree
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmempoolallochit
            
            	Indicates the number of successful allocations from the memory pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmempoolallocmiss
            
            	Indicates the number of unsuccessful allocations from the memory pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmempoolfreehit
            
            	Indicates the number of successful frees/ deallocations from the memory pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmempoolfreemiss
            
            	Indicates the number of unsuccessful attempts to free/deallocate memory from the memory pool. For example, this could be due to ownership errors  where the application that did not assign the  memory is trying to free it
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmempoolshared
            
            	Indicates the number of bytes from the memory pool that are currently shared on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolusedovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolUsed. This object needs to be supported only if the used bytes in the memory pool exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcused
            
            	Indicates the number of bytes from the memory pool that are currently in use by applications on the physical entity. This object is a 64\-bit version of cempMemPoolUsed
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolfreeovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolFree. This object needs to be supported only if the unused bytes in the memory pool exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcfree
            
            	Indicates the number of bytes from the memory pool that are currently unused on the physical entity. This object is a 64\-bit version of cempMemPoolFree
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollargestfreeovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolLargestFree. This object needs to  be supported only if the value of  cempMemPoolLargestFree exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhclargestfree
            
            	Indicates the largest number of contiguous bytes from the memory pool that are currently unused on the physical entity. This object is a 64\-bit version of cempMemPoolLargestFree
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoollowestfreeovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolLowestFree. This object needs to be supported only if the value of cempMemPoolLowestFree exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhclowestfree
            
            	The lowest amount of available memory in the memory pool recorded at any time during the operation of the system. This object is a 64\-bit version of cempMemPoolLowestFree
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolusedlowwatermarkovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolUsedLowWaterMark. This object needs to be supported only if the value of cempMemPoolUsedLowWaterMark exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcusedlowwatermark
            
            	Indicates the lowest number of bytes from the memory pool that have been used by applications on the physical entity since sysUpTime. This object is a 64\-bit version of cempMemPoolUsedLowWaterMark
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolsharedovrflw
            
            	This object represents the upper 32\-bits of cempMemPoolShared. This object needs to be supported only if the value of cempMemPoolShared exceeds 32\-bits, otherwise this object value would be set to 0
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmempoolhcshared
            
            	Indicates the number of bytes from the memory pool that are currently shared on the physical entity. This object is a 64\-bit version of cempMemPoolShared
            	**type**\: int
            
            	**range:** 0..18446744073709551615
            
            	**config**\: False
            
            	**units**\: bytes
            
            

            """

            _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
            _revision = '2008-12-05'

            def __init__(self):
                super(CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable.CempMemPoolEntry, self).__init__()

                self.yang_name = "cempMemPoolEntry"
                self.yang_parent_name = "cempMemPoolTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cempmempoolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cempmempoolindex', (YLeaf(YType.int32, 'cempMemPoolIndex'), ['int'])),
                    ('cempmempooltype', (YLeaf(YType.enumeration, 'cempMemPoolType'), [('ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CempMemPoolTypes', '')])),
                    ('cempmempoolname', (YLeaf(YType.str, 'cempMemPoolName'), ['str'])),
                    ('cempmempoolplatformmemory', (YLeaf(YType.str, 'cempMemPoolPlatformMemory'), ['str'])),
                    ('cempmempoolalternate', (YLeaf(YType.int32, 'cempMemPoolAlternate'), ['int'])),
                    ('cempmempoolvalid', (YLeaf(YType.boolean, 'cempMemPoolValid'), ['bool'])),
                    ('cempmempoolused', (YLeaf(YType.uint32, 'cempMemPoolUsed'), ['int'])),
                    ('cempmempoolfree', (YLeaf(YType.uint32, 'cempMemPoolFree'), ['int'])),
                    ('cempmempoollargestfree', (YLeaf(YType.uint32, 'cempMemPoolLargestFree'), ['int'])),
                    ('cempmempoollowestfree', (YLeaf(YType.uint32, 'cempMemPoolLowestFree'), ['int'])),
                    ('cempmempoolusedlowwatermark', (YLeaf(YType.uint32, 'cempMemPoolUsedLowWaterMark'), ['int'])),
                    ('cempmempoolallochit', (YLeaf(YType.uint32, 'cempMemPoolAllocHit'), ['int'])),
                    ('cempmempoolallocmiss', (YLeaf(YType.uint32, 'cempMemPoolAllocMiss'), ['int'])),
                    ('cempmempoolfreehit', (YLeaf(YType.uint32, 'cempMemPoolFreeHit'), ['int'])),
                    ('cempmempoolfreemiss', (YLeaf(YType.uint32, 'cempMemPoolFreeMiss'), ['int'])),
                    ('cempmempoolshared', (YLeaf(YType.uint32, 'cempMemPoolShared'), ['int'])),
                    ('cempmempoolusedovrflw', (YLeaf(YType.uint32, 'cempMemPoolUsedOvrflw'), ['int'])),
                    ('cempmempoolhcused', (YLeaf(YType.uint64, 'cempMemPoolHCUsed'), ['int'])),
                    ('cempmempoolfreeovrflw', (YLeaf(YType.uint32, 'cempMemPoolFreeOvrflw'), ['int'])),
                    ('cempmempoolhcfree', (YLeaf(YType.uint64, 'cempMemPoolHCFree'), ['int'])),
                    ('cempmempoollargestfreeovrflw', (YLeaf(YType.uint32, 'cempMemPoolLargestFreeOvrflw'), ['int'])),
                    ('cempmempoolhclargestfree', (YLeaf(YType.uint64, 'cempMemPoolHCLargestFree'), ['int'])),
                    ('cempmempoollowestfreeovrflw', (YLeaf(YType.uint32, 'cempMemPoolLowestFreeOvrflw'), ['int'])),
                    ('cempmempoolhclowestfree', (YLeaf(YType.uint64, 'cempMemPoolHCLowestFree'), ['int'])),
                    ('cempmempoolusedlowwatermarkovrflw', (YLeaf(YType.uint32, 'cempMemPoolUsedLowWaterMarkOvrflw'), ['int'])),
                    ('cempmempoolhcusedlowwatermark', (YLeaf(YType.uint64, 'cempMemPoolHCUsedLowWaterMark'), ['int'])),
                    ('cempmempoolsharedovrflw', (YLeaf(YType.uint32, 'cempMemPoolSharedOvrflw'), ['int'])),
                    ('cempmempoolhcshared', (YLeaf(YType.uint64, 'cempMemPoolHCShared'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cempmempoolindex = None
                self.cempmempooltype = None
                self.cempmempoolname = None
                self.cempmempoolplatformmemory = None
                self.cempmempoolalternate = None
                self.cempmempoolvalid = None
                self.cempmempoolused = None
                self.cempmempoolfree = None
                self.cempmempoollargestfree = None
                self.cempmempoollowestfree = None
                self.cempmempoolusedlowwatermark = None
                self.cempmempoolallochit = None
                self.cempmempoolallocmiss = None
                self.cempmempoolfreehit = None
                self.cempmempoolfreemiss = None
                self.cempmempoolshared = None
                self.cempmempoolusedovrflw = None
                self.cempmempoolhcused = None
                self.cempmempoolfreeovrflw = None
                self.cempmempoolhcfree = None
                self.cempmempoollargestfreeovrflw = None
                self.cempmempoolhclargestfree = None
                self.cempmempoollowestfreeovrflw = None
                self.cempmempoolhclowestfree = None
                self.cempmempoolusedlowwatermarkovrflw = None
                self.cempmempoolhcusedlowwatermark = None
                self.cempmempoolsharedovrflw = None
                self.cempmempoolhcshared = None
                self._segment_path = lambda: "cempMemPoolEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cempMemPoolIndex='" + str(self.cempmempoolindex) + "']"
                self._absolute_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/cempMemPoolTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENHANCEDMEMPOOLMIB.CempMemPoolTable.CempMemPoolEntry, ['entphysicalindex', 'cempmempoolindex', 'cempmempooltype', 'cempmempoolname', 'cempmempoolplatformmemory', 'cempmempoolalternate', 'cempmempoolvalid', 'cempmempoolused', 'cempmempoolfree', 'cempmempoollargestfree', 'cempmempoollowestfree', 'cempmempoolusedlowwatermark', 'cempmempoolallochit', 'cempmempoolallocmiss', 'cempmempoolfreehit', 'cempmempoolfreemiss', 'cempmempoolshared', 'cempmempoolusedovrflw', 'cempmempoolhcused', 'cempmempoolfreeovrflw', 'cempmempoolhcfree', 'cempmempoollargestfreeovrflw', 'cempmempoolhclargestfree', 'cempmempoollowestfreeovrflw', 'cempmempoolhclowestfree', 'cempmempoolusedlowwatermarkovrflw', 'cempmempoolhcusedlowwatermark', 'cempmempoolsharedovrflw', 'cempmempoolhcshared'], name, value)




    class CempMemBufferPoolTable(Entity):
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
        	**type**\: list of  		 :py:class:`CempMemBufferPoolEntry <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable.CempMemBufferPoolEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable, self).__init__()

            self.yang_name = "cempMemBufferPoolTable"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cempMemBufferPoolEntry", ("cempmembufferpoolentry", CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable.CempMemBufferPoolEntry))])
            self._leafs = OrderedDict()

            self.cempmembufferpoolentry = YList(self)
            self._segment_path = lambda: "cempMemBufferPoolTable"
            self._absolute_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable, [], name, value)


        class CempMemBufferPoolEntry(Entity):
            """
            This contains all the memory buffer pool
            configurations object values. The 
            entPhysicalIndex identifies the entity on which
            memory buffer pools are present.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cempmembufferpoolindex  (key)
            
            	Within a physical entity, a unique value used to represent each buffer pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffermempoolindex
            
            	This index corresponds to the memory pool (with cemMemPoolIndex as index in cempMemPoolTable)  from which buffers are allocated
            	**type**\: int
            
            	**range:** 0..2147483647
            
            	**config**\: False
            
            .. attribute:: cempmembuffername
            
            	A textual name assigned to the buffer pool. This object is suitable for output to a human operator, and may also be used to distinguish among the various buffer types. For example\: 'Small', 'Big', 'Serial0/1' etc
            	**type**\: str
            
            	**config**\: False
            
            .. attribute:: cempmembufferdynamic
            
            	Boolean poolDynamic; if TRUE, the number of buffers in the pool is adjusted (adding more packet buffers  or deleting excesses) dynamically by the background  process. If FALSE, the number of buffers in the pool  is never adjusted, even if it falls below the minimum, or to zero
            	**type**\: bool
            
            	**config**\: False
            
            .. attribute:: cempmembuffersize
            
            	Indicates the size of buffer element in number of bytes on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            	**units**\: bytes
            
            .. attribute:: cempmembuffermin
            
            	Indicates the minimum number of free buffers allowed in the buffer pool or low\-water mark (lwm).  For example of its usage \: If cempMemBufferFree < cempMemBufferMin & pool is  dynamic, then signal for growth of particular buffer pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffermax
            
            	Indicates the maximum number of free buffers allowed in the buffer pool or high\-water mark (hwm). For example of its usage \: If cempMemBufferFree > cempMemBufferMax & pool is  dynamic, then signal for trim of particular buffer pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferpermanent
            
            	Indicates the total number of permanent buffers in the pool on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffertransient
            
            	Indicates the initial number of temporary buffers in the pool on the physical entity. This object  instructs the system to create this many number of temporary extra buffers, just after a system restart.  A change in this object will be effective only after a system restart
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffertotal
            
            	Indicates the total number of buffers (include allocated and free buffers) in the buffer pool on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferfree
            
            	Indicates the current number of free buffers in the buffer pool on the physical entity. Note that the cempMemBufferFree is less than or equal  to cempMemBufferTotal
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferhit
            
            	Indicates the number of buffers successfully allocated from the buffer pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffermiss
            
            	Indicates the number of times a buffer has been requested, but no buffers were available in the buffer pool, or when there were fewer than min  buffers(cempMemBufferMin) in the buffer pool. Note \: For interface pools, a miss is actually  a fall back to its corresponding public buffer pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferfreehit
            
            	Indicates the number of successful frees/deallocations from the buffer pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferfreemiss
            
            	Indicates the number of unsuccessful attempts to free/deallocate a buffer from the buffer pool.  For example, this could be due to ownership errors where the application that did not assign the  buffer is trying to free it
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferpermchange
            
            	This value is the difference of the desired number of permanent buffer & total number of permanent  buffers present in the pool. A positive value of  this object tells the number of buffers needed & a  negative value of the object tells the extra number  of buffers in the pool
            	**type**\: int
            
            	**range:** \-2147483648..2147483647
            
            	**config**\: False
            
            .. attribute:: cempmembufferpeak
            
            	Indicates the peak number of buffers in pool on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferpeaktime
            
            	Indicates the time of most recent change in the peak number of buffers (cempMemBufferPeak object) in the pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffertrim
            
            	The number of buffers that have been trimmed from the pool when the number of free buffers  (cempMemBufferFree) exceeded the number of max allowed buffers(cempMemBufferMax)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffergrow
            
            	The number of buffers that have been created in the pool when the number of free buffers(cempMemBufferFree) was less than minimum(cempMemBufferMix)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembufferfailures
            
            	The number of failures to grant a buffer to a requester due to reasons other than insufficient  memory. For example, in systems where there are  different execution contexts, it may be too expensive to create new buffers when running in certain contexts. In those cases it may be  preferable to fail the request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffernostorage
            
            	The number of times the system tried to create new buffers, but could not due to insufficient free  memory in the system
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
            _revision = '2008-12-05'

            def __init__(self):
                super(CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable.CempMemBufferPoolEntry, self).__init__()

                self.yang_name = "cempMemBufferPoolEntry"
                self.yang_parent_name = "cempMemBufferPoolTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cempmembufferpoolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cempmembufferpoolindex', (YLeaf(YType.uint32, 'cempMemBufferPoolIndex'), ['int'])),
                    ('cempmembuffermempoolindex', (YLeaf(YType.int32, 'cempMemBufferMemPoolIndex'), ['int'])),
                    ('cempmembuffername', (YLeaf(YType.str, 'cempMemBufferName'), ['str'])),
                    ('cempmembufferdynamic', (YLeaf(YType.boolean, 'cempMemBufferDynamic'), ['bool'])),
                    ('cempmembuffersize', (YLeaf(YType.uint32, 'cempMemBufferSize'), ['int'])),
                    ('cempmembuffermin', (YLeaf(YType.uint32, 'cempMemBufferMin'), ['int'])),
                    ('cempmembuffermax', (YLeaf(YType.uint32, 'cempMemBufferMax'), ['int'])),
                    ('cempmembufferpermanent', (YLeaf(YType.uint32, 'cempMemBufferPermanent'), ['int'])),
                    ('cempmembuffertransient', (YLeaf(YType.uint32, 'cempMemBufferTransient'), ['int'])),
                    ('cempmembuffertotal', (YLeaf(YType.uint32, 'cempMemBufferTotal'), ['int'])),
                    ('cempmembufferfree', (YLeaf(YType.uint32, 'cempMemBufferFree'), ['int'])),
                    ('cempmembufferhit', (YLeaf(YType.uint32, 'cempMemBufferHit'), ['int'])),
                    ('cempmembuffermiss', (YLeaf(YType.uint32, 'cempMemBufferMiss'), ['int'])),
                    ('cempmembufferfreehit', (YLeaf(YType.uint32, 'cempMemBufferFreeHit'), ['int'])),
                    ('cempmembufferfreemiss', (YLeaf(YType.uint32, 'cempMemBufferFreeMiss'), ['int'])),
                    ('cempmembufferpermchange', (YLeaf(YType.int32, 'cempMemBufferPermChange'), ['int'])),
                    ('cempmembufferpeak', (YLeaf(YType.uint32, 'cempMemBufferPeak'), ['int'])),
                    ('cempmembufferpeaktime', (YLeaf(YType.uint32, 'cempMemBufferPeakTime'), ['int'])),
                    ('cempmembuffertrim', (YLeaf(YType.uint32, 'cempMemBufferTrim'), ['int'])),
                    ('cempmembuffergrow', (YLeaf(YType.uint32, 'cempMemBufferGrow'), ['int'])),
                    ('cempmembufferfailures', (YLeaf(YType.uint32, 'cempMemBufferFailures'), ['int'])),
                    ('cempmembuffernostorage', (YLeaf(YType.uint32, 'cempMemBufferNoStorage'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cempmembufferpoolindex = None
                self.cempmembuffermempoolindex = None
                self.cempmembuffername = None
                self.cempmembufferdynamic = None
                self.cempmembuffersize = None
                self.cempmembuffermin = None
                self.cempmembuffermax = None
                self.cempmembufferpermanent = None
                self.cempmembuffertransient = None
                self.cempmembuffertotal = None
                self.cempmembufferfree = None
                self.cempmembufferhit = None
                self.cempmembuffermiss = None
                self.cempmembufferfreehit = None
                self.cempmembufferfreemiss = None
                self.cempmembufferpermchange = None
                self.cempmembufferpeak = None
                self.cempmembufferpeaktime = None
                self.cempmembuffertrim = None
                self.cempmembuffergrow = None
                self.cempmembufferfailures = None
                self.cempmembuffernostorage = None
                self._segment_path = lambda: "cempMemBufferPoolEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cempMemBufferPoolIndex='" + str(self.cempmembufferpoolindex) + "']"
                self._absolute_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/cempMemBufferPoolTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable.CempMemBufferPoolEntry, ['entphysicalindex', 'cempmembufferpoolindex', 'cempmembuffermempoolindex', 'cempmembuffername', 'cempmembufferdynamic', 'cempmembuffersize', 'cempmembuffermin', 'cempmembuffermax', 'cempmembufferpermanent', 'cempmembuffertransient', 'cempmembuffertotal', 'cempmembufferfree', 'cempmembufferhit', 'cempmembuffermiss', 'cempmembufferfreehit', 'cempmembufferfreemiss', 'cempmembufferpermchange', 'cempmembufferpeak', 'cempmembufferpeaktime', 'cempmembuffertrim', 'cempmembuffergrow', 'cempmembufferfailures', 'cempmembuffernostorage'], name, value)




    class CempMemBufferCachePoolTable(Entity):
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
        	**type**\: list of  		 :py:class:`CempMemBufferCachePoolEntry <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable.CempMemBufferCachePoolEntry>`
        
        	**config**\: False
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            super(CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable, self).__init__()

            self.yang_name = "cempMemBufferCachePoolTable"
            self.yang_parent_name = "CISCO-ENHANCED-MEMPOOL-MIB"
            self.is_top_level_class = False
            self.has_list_ancestor = False
            self.ylist_key_names = []
            self._child_classes = OrderedDict([("cempMemBufferCachePoolEntry", ("cempmembuffercachepoolentry", CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable.CempMemBufferCachePoolEntry))])
            self._leafs = OrderedDict()

            self.cempmembuffercachepoolentry = YList(self)
            self._segment_path = lambda: "cempMemBufferCachePoolTable"
            self._absolute_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/%s" % self._segment_path()
            self._is_frozen = True

        def __setattr__(self, name, value):
            self._perform_setattr(CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable, [], name, value)


        class CempMemBufferCachePoolEntry(Entity):
            """
            Each entry represents one of the cache buffer pools
            available in the system and it contains the
            parameters configured for it.
            Note \: cempMemBufferCachePoolTable has a sparse
            dependency with cempMemBufferPoolTable (i.e all the
            entires in cempMemBufferPoolTable need not have an
            entry in cempMemBufferCachePoolTable.
            
            .. attribute:: entphysicalindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            	**refers to**\:  :py:class:`entphysicalindex <ydk.models.cisco_ios_xe.ENTITY_MIB.ENTITYMIB.EntPhysicalTable.EntPhysicalEntry>`
            
            	**config**\: False
            
            .. attribute:: cempmembufferpoolindex  (key)
            
            	
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**refers to**\:  :py:class:`cempmembufferpoolindex <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CISCOENHANCEDMEMPOOLMIB.CempMemBufferPoolTable.CempMemBufferPoolEntry>`
            
            	**config**\: False
            
            .. attribute:: cempmembuffercachesize
            
            	Indicates the number of buffers in the cache pool on the physical entity
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffercachetotal
            
            	Indicates the maximum number of free buffers allowed in the cache pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffercacheused
            
            	Indicates the number of cache buffers from the pool that are currently used on the physical entity. Note that the cempMemBufferCacheUsed is less than or  equal to cempMemBufferCacheTotal
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffercachehit
            
            	Indicates the number of buffers successfully allocated from the cache pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffercachemiss
            
            	Indicates the number of times a buffer has been requested, but no buffers were available in the cache pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffercachethreshold
            
            	Indicates the threshold limit for number of cache buffers used(cempMemBufferCacheUsed)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            .. attribute:: cempmembuffercachethresholdcount
            
            	Indicates how many times the number of cache buffers used(cempMemBufferCacheUsed) has crossed the threshold value(cempMemBufferCacheThreshold)
            	**type**\: int
            
            	**range:** 0..4294967295
            
            	**config**\: False
            
            

            """

            _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
            _revision = '2008-12-05'

            def __init__(self):
                super(CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable.CempMemBufferCachePoolEntry, self).__init__()

                self.yang_name = "cempMemBufferCachePoolEntry"
                self.yang_parent_name = "cempMemBufferCachePoolTable"
                self.is_top_level_class = False
                self.has_list_ancestor = False
                self.ylist_key_names = ['entphysicalindex','cempmembufferpoolindex']
                self._child_classes = OrderedDict([])
                self._leafs = OrderedDict([
                    ('entphysicalindex', (YLeaf(YType.str, 'entPhysicalIndex'), ['int'])),
                    ('cempmembufferpoolindex', (YLeaf(YType.str, 'cempMemBufferPoolIndex'), ['int'])),
                    ('cempmembuffercachesize', (YLeaf(YType.uint32, 'cempMemBufferCacheSize'), ['int'])),
                    ('cempmembuffercachetotal', (YLeaf(YType.uint32, 'cempMemBufferCacheTotal'), ['int'])),
                    ('cempmembuffercacheused', (YLeaf(YType.uint32, 'cempMemBufferCacheUsed'), ['int'])),
                    ('cempmembuffercachehit', (YLeaf(YType.uint32, 'cempMemBufferCacheHit'), ['int'])),
                    ('cempmembuffercachemiss', (YLeaf(YType.uint32, 'cempMemBufferCacheMiss'), ['int'])),
                    ('cempmembuffercachethreshold', (YLeaf(YType.uint32, 'cempMemBufferCacheThreshold'), ['int'])),
                    ('cempmembuffercachethresholdcount', (YLeaf(YType.uint32, 'cempMemBufferCacheThresholdCount'), ['int'])),
                ])
                self.entphysicalindex = None
                self.cempmembufferpoolindex = None
                self.cempmembuffercachesize = None
                self.cempmembuffercachetotal = None
                self.cempmembuffercacheused = None
                self.cempmembuffercachehit = None
                self.cempmembuffercachemiss = None
                self.cempmembuffercachethreshold = None
                self.cempmembuffercachethresholdcount = None
                self._segment_path = lambda: "cempMemBufferCachePoolEntry" + "[entPhysicalIndex='" + str(self.entphysicalindex) + "']" + "[cempMemBufferPoolIndex='" + str(self.cempmembufferpoolindex) + "']"
                self._absolute_path = lambda: "CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/cempMemBufferCachePoolTable/%s" % self._segment_path()
                self._is_frozen = True

            def __setattr__(self, name, value):
                self._perform_setattr(CISCOENHANCEDMEMPOOLMIB.CempMemBufferCachePoolTable.CempMemBufferCachePoolEntry, ['entphysicalindex', 'cempmembufferpoolindex', 'cempmembuffercachesize', 'cempmembuffercachetotal', 'cempmembuffercacheused', 'cempmembuffercachehit', 'cempmembuffercachemiss', 'cempmembuffercachethreshold', 'cempmembuffercachethresholdcount'], name, value)



    def clone_ptr(self):
        self._top_entity = CISCOENHANCEDMEMPOOLMIB()
        return self._top_entity



