""" CISCO_ENHANCED_MEMPOOL_MIB 

New MIB module for monitoring the memory pools
of all physical entities on a managed system.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYModelError



class CempmempooltypesEnum(Enum):
    """
    CempmempooltypesEnum

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

    other = 1

    processorMemory = 2

    ioMemory = 3

    pciMemory = 4

    fastMemory = 5

    multibusMemory = 6

    interruptStackMemory = 7

    processStackMemory = 8

    localExceptionMemory = 9

    virtualMemory = 10

    reservedMemory = 11

    imageMemory = 12

    asicMemory = 13

    posixMemory = 14


    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
        return meta._meta_table['CempmempooltypesEnum']



class CiscoEnhancedMempoolMib(object):
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
        self.cempmembuffercachepooltable = CiscoEnhancedMempoolMib.Cempmembuffercachepooltable()
        self.cempmembuffercachepooltable.parent = self
        self.cempmembufferpooltable = CiscoEnhancedMempoolMib.Cempmembufferpooltable()
        self.cempmembufferpooltable.parent = self
        self.cempmempooltable = CiscoEnhancedMempoolMib.Cempmempooltable()
        self.cempmempooltable.parent = self
        self.cempnotificationconfig = CiscoEnhancedMempoolMib.Cempnotificationconfig()
        self.cempnotificationconfig.parent = self


    class Cempnotificationconfig(object):
        """
        
        
        .. attribute:: cempmembuffernotifyenabled
        
        	This variable controls generation of the cempMemBufferNotify.  When this variable is 'true', generation of cempMemBufferNotify is enabled.  When this variable is 'false', generation of cempMemBufferNotify is disabled
        	**type**\:  bool
        
        

        """

        _prefix = 'CISCO-ENHANCED-MEMPOOL-MIB'
        _revision = '2008-12-05'

        def __init__(self):
            self.parent = None
            self.cempmembuffernotifyenabled = None

        @property
        def _common_path(self):

            return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/CISCO-ENHANCED-MEMPOOL-MIB:cempNotificationConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cempmembuffernotifyenabled is not None:
                return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
            return meta._meta_table['CiscoEnhancedMempoolMib.Cempnotificationconfig']['meta_info']


    class Cempmempooltable(object):
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
            self.parent = None
            self.cempmempoolentry = YList()
            self.cempmempoolentry.parent = self
            self.cempmempoolentry.name = 'cempmempoolentry'


        class Cempmempoolentry(object):
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
            	**type**\:   :py:class:`CempmempooltypesEnum <ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB.CempmempooltypesEnum>`
            
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
                self.parent = None
                self.entphysicalindex = None
                self.cempmempoolindex = None
                self.cempmempoolallochit = None
                self.cempmempoolallocmiss = None
                self.cempmempoolalternate = None
                self.cempmempoolfree = None
                self.cempmempoolfreehit = None
                self.cempmempoolfreemiss = None
                self.cempmempoolfreeovrflw = None
                self.cempmempoolhcfree = None
                self.cempmempoolhclargestfree = None
                self.cempmempoolhclowestfree = None
                self.cempmempoolhcshared = None
                self.cempmempoolhcused = None
                self.cempmempoolhcusedlowwatermark = None
                self.cempmempoollargestfree = None
                self.cempmempoollargestfreeovrflw = None
                self.cempmempoollowestfree = None
                self.cempmempoollowestfreeovrflw = None
                self.cempmempoolname = None
                self.cempmempoolplatformmemory = None
                self.cempmempoolshared = None
                self.cempmempoolsharedovrflw = None
                self.cempmempooltype = None
                self.cempmempoolused = None
                self.cempmempoolusedlowwatermark = None
                self.cempmempoolusedlowwatermarkovrflw = None
                self.cempmempoolusedovrflw = None
                self.cempmempoolvalid = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cempmempoolindex is None:
                    raise YPYModelError('Key property cempmempoolindex is None')

                return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/CISCO-ENHANCED-MEMPOOL-MIB:cempMemPoolTable/CISCO-ENHANCED-MEMPOOL-MIB:cempMemPoolEntry[CISCO-ENHANCED-MEMPOOL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENHANCED-MEMPOOL-MIB:cempMemPoolIndex = ' + str(self.cempmempoolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cempmempoolindex is not None:
                    return True

                if self.cempmempoolallochit is not None:
                    return True

                if self.cempmempoolallocmiss is not None:
                    return True

                if self.cempmempoolalternate is not None:
                    return True

                if self.cempmempoolfree is not None:
                    return True

                if self.cempmempoolfreehit is not None:
                    return True

                if self.cempmempoolfreemiss is not None:
                    return True

                if self.cempmempoolfreeovrflw is not None:
                    return True

                if self.cempmempoolhcfree is not None:
                    return True

                if self.cempmempoolhclargestfree is not None:
                    return True

                if self.cempmempoolhclowestfree is not None:
                    return True

                if self.cempmempoolhcshared is not None:
                    return True

                if self.cempmempoolhcused is not None:
                    return True

                if self.cempmempoolhcusedlowwatermark is not None:
                    return True

                if self.cempmempoollargestfree is not None:
                    return True

                if self.cempmempoollargestfreeovrflw is not None:
                    return True

                if self.cempmempoollowestfree is not None:
                    return True

                if self.cempmempoollowestfreeovrflw is not None:
                    return True

                if self.cempmempoolname is not None:
                    return True

                if self.cempmempoolplatformmemory is not None:
                    return True

                if self.cempmempoolshared is not None:
                    return True

                if self.cempmempoolsharedovrflw is not None:
                    return True

                if self.cempmempooltype is not None:
                    return True

                if self.cempmempoolused is not None:
                    return True

                if self.cempmempoolusedlowwatermark is not None:
                    return True

                if self.cempmempoolusedlowwatermarkovrflw is not None:
                    return True

                if self.cempmempoolusedovrflw is not None:
                    return True

                if self.cempmempoolvalid is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
                return meta._meta_table['CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/CISCO-ENHANCED-MEMPOOL-MIB:cempMemPoolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cempmempoolentry is not None:
                for child_ref in self.cempmempoolentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
            return meta._meta_table['CiscoEnhancedMempoolMib.Cempmempooltable']['meta_info']


    class Cempmembufferpooltable(object):
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
            self.parent = None
            self.cempmembufferpoolentry = YList()
            self.cempmembufferpoolentry.parent = self
            self.cempmembufferpoolentry.name = 'cempmembufferpoolentry'


        class Cempmembufferpoolentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cempmembufferpoolindex = None
                self.cempmembufferdynamic = None
                self.cempmembufferfailures = None
                self.cempmembufferfree = None
                self.cempmembufferfreehit = None
                self.cempmembufferfreemiss = None
                self.cempmembuffergrow = None
                self.cempmembufferhit = None
                self.cempmembuffermax = None
                self.cempmembuffermempoolindex = None
                self.cempmembuffermin = None
                self.cempmembuffermiss = None
                self.cempmembuffername = None
                self.cempmembuffernostorage = None
                self.cempmembufferpeak = None
                self.cempmembufferpeaktime = None
                self.cempmembufferpermanent = None
                self.cempmembufferpermchange = None
                self.cempmembuffersize = None
                self.cempmembuffertotal = None
                self.cempmembuffertransient = None
                self.cempmembuffertrim = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cempmembufferpoolindex is None:
                    raise YPYModelError('Key property cempmembufferpoolindex is None')

                return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferPoolTable/CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferPoolEntry[CISCO-ENHANCED-MEMPOOL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferPoolIndex = ' + str(self.cempmembufferpoolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cempmembufferpoolindex is not None:
                    return True

                if self.cempmembufferdynamic is not None:
                    return True

                if self.cempmembufferfailures is not None:
                    return True

                if self.cempmembufferfree is not None:
                    return True

                if self.cempmembufferfreehit is not None:
                    return True

                if self.cempmembufferfreemiss is not None:
                    return True

                if self.cempmembuffergrow is not None:
                    return True

                if self.cempmembufferhit is not None:
                    return True

                if self.cempmembuffermax is not None:
                    return True

                if self.cempmembuffermempoolindex is not None:
                    return True

                if self.cempmembuffermin is not None:
                    return True

                if self.cempmembuffermiss is not None:
                    return True

                if self.cempmembuffername is not None:
                    return True

                if self.cempmembuffernostorage is not None:
                    return True

                if self.cempmembufferpeak is not None:
                    return True

                if self.cempmembufferpeaktime is not None:
                    return True

                if self.cempmembufferpermanent is not None:
                    return True

                if self.cempmembufferpermchange is not None:
                    return True

                if self.cempmembuffersize is not None:
                    return True

                if self.cempmembuffertotal is not None:
                    return True

                if self.cempmembuffertransient is not None:
                    return True

                if self.cempmembuffertrim is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
                return meta._meta_table['CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferPoolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cempmembufferpoolentry is not None:
                for child_ref in self.cempmembufferpoolentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
            return meta._meta_table['CiscoEnhancedMempoolMib.Cempmembufferpooltable']['meta_info']


    class Cempmembuffercachepooltable(object):
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
            self.parent = None
            self.cempmembuffercachepoolentry = YList()
            self.cempmembuffercachepoolentry.parent = self
            self.cempmembuffercachepoolentry.name = 'cempmembuffercachepoolentry'


        class Cempmembuffercachepoolentry(object):
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
                self.parent = None
                self.entphysicalindex = None
                self.cempmembufferpoolindex = None
                self.cempmembuffercachehit = None
                self.cempmembuffercachemiss = None
                self.cempmembuffercachesize = None
                self.cempmembuffercachethreshold = None
                self.cempmembuffercachethresholdcount = None
                self.cempmembuffercachetotal = None
                self.cempmembuffercacheused = None

            @property
            def _common_path(self):
                if self.entphysicalindex is None:
                    raise YPYModelError('Key property entphysicalindex is None')
                if self.cempmembufferpoolindex is None:
                    raise YPYModelError('Key property cempmembufferpoolindex is None')

                return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferCachePoolTable/CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferCachePoolEntry[CISCO-ENHANCED-MEMPOOL-MIB:entPhysicalIndex = ' + str(self.entphysicalindex) + '][CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferPoolIndex = ' + str(self.cempmembufferpoolindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if self.entphysicalindex is not None:
                    return True

                if self.cempmembufferpoolindex is not None:
                    return True

                if self.cempmembuffercachehit is not None:
                    return True

                if self.cempmembuffercachemiss is not None:
                    return True

                if self.cempmembuffercachesize is not None:
                    return True

                if self.cempmembuffercachethreshold is not None:
                    return True

                if self.cempmembuffercachethresholdcount is not None:
                    return True

                if self.cempmembuffercachetotal is not None:
                    return True

                if self.cempmembuffercacheused is not None:
                    return True

                return False

            @staticmethod
            def _meta_info():
                from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
                return meta._meta_table['CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB/CISCO-ENHANCED-MEMPOOL-MIB:cempMemBufferCachePoolTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if self.cempmembuffercachepoolentry is not None:
                for child_ref in self.cempmembuffercachepoolentry:
                    if child_ref._has_data():
                        return True

            return False

        @staticmethod
        def _meta_info():
            from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
            return meta._meta_table['CiscoEnhancedMempoolMib.Cempmembuffercachepooltable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-ENHANCED-MEMPOOL-MIB:CISCO-ENHANCED-MEMPOOL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if self.cempmembuffercachepooltable is not None and self.cempmembuffercachepooltable._has_data():
            return True

        if self.cempmembufferpooltable is not None and self.cempmembufferpooltable._has_data():
            return True

        if self.cempmempooltable is not None and self.cempmempooltable._has_data():
            return True

        if self.cempnotificationconfig is not None and self.cempnotificationconfig._has_data():
            return True

        return False

    @staticmethod
    def _meta_info():
        from ydk.models.cisco_ios_xe._meta import _CISCO_ENHANCED_MEMPOOL_MIB as meta
        return meta._meta_table['CiscoEnhancedMempoolMib']['meta_info']


