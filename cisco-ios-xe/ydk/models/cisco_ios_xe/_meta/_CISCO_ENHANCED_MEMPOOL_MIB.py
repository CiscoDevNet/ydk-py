


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CempmempooltypesEnum' : _MetaInfoEnum('CempmempooltypesEnum', 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB',
        {
            'other':'other',
            'processorMemory':'processorMemory',
            'ioMemory':'ioMemory',
            'pciMemory':'pciMemory',
            'fastMemory':'fastMemory',
            'multibusMemory':'multibusMemory',
            'interruptStackMemory':'interruptStackMemory',
            'processStackMemory':'processStackMemory',
            'localExceptionMemory':'localExceptionMemory',
            'virtualMemory':'virtualMemory',
            'reservedMemory':'reservedMemory',
            'imageMemory':'imageMemory',
            'asicMemory':'asicMemory',
            'posixMemory':'posixMemory',
        }, 'CISCO-ENHANCED-MEMPOOL-MIB', _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB']),
    'CiscoEnhancedMempoolMib.Cempnotificationconfig' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib.Cempnotificationconfig',
            False, 
            [
            _MetaInfoClassMember('cempMemBufferNotifyEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable controls generation of the
                cempMemBufferNotify.
                
                When this variable is 'true', generation of
                cempMemBufferNotify is enabled.  When this variable
                is 'false', generation of cempMemBufferNotify
                is disabled.
                ''',
                'cempmembuffernotifyenabled',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'cempNotificationConfig',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
    'CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENHANCED-MEMPOOL-MIB', True),
            _MetaInfoClassMember('cempMemPoolIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Within each physical entity, the unique value
                greater than zero, used to represent each memory pool.  
                It is recommended that values are assigned
                contiguously starting from 1.
                ''',
                'cempmempoolindex',
                'CISCO-ENHANCED-MEMPOOL-MIB', True),
            _MetaInfoClassMember('cempMemPoolAllocHit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of successful allocations from
                the memory pool
                ''',
                'cempmempoolallochit',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolAllocMiss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of unsuccessful allocations from
                the memory pool
                ''',
                'cempmempoolallocmiss',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolAlternate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Indicates whether or not this memory pool has an
                alternate pool configured.  Alternate pools are
                used for fallback when the current pool runs out
                of memory.
                
                If an instance of this object has a value of zero,
                then this pool does not have an alternate.  Otherwise
                the value of this object is the same as the value of
                cempMemPoolType of the alternate pool.
                ''',
                'cempmempoolalternate',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of bytes from the memory pool
                that are currently unused on the physical entity.
                
                Note that the sum of cempMemPoolUsed and cempMemPoolFree 
                is the total amount of memory in the pool
                ''',
                'cempmempoolfree',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolFreeHit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of successful frees/
                deallocations from the memory pool
                ''',
                'cempmempoolfreehit',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolFreeMiss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of unsuccessful attempts
                to free/deallocate memory from the memory pool.
                For example, this could be due to ownership errors 
                where the application that did not assign the 
                memory is trying to free it.
                ''',
                'cempmempoolfreemiss',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolFreeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bits of cempMemPoolFree.
                This object needs to be supported only if the unused bytes in
                the memory pool exceeds 32-bits, otherwise this object value
                would be set to 0.
                ''',
                'cempmempoolfreeovrflw',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolHCFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Indicates the number of bytes from the memory pool
                that are currently unused on the physical entity.
                This object is a 64-bit version of cempMemPoolFree.
                ''',
                'cempmempoolhcfree',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolHCLargestFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Indicates the largest number of contiguous bytes from the
                memory pool that are currently unused on the physical entity.
                This object is a 64-bit version of cempMemPoolLargestFree.
                ''',
                'cempmempoolhclargestfree',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolHCLowestFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                The lowest amount of available memory in the memory pool
                recorded at any time during the operation of the system.
                This object is a 64-bit version of cempMemPoolLowestFree.
                ''',
                'cempmempoolhclowestfree',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolHCShared', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Indicates the number of bytes from the memory pool that are
                currently shared on the physical entity. This object is a
                64-bit version of cempMemPoolShared.
                ''',
                'cempmempoolhcshared',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolHCUsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Indicates the number of bytes from the memory pool
                that are currently in use by applications on the
                physical entity. This object is a 64-bit version of
                cempMemPoolUsed.
                ''',
                'cempmempoolhcused',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolHCUsedLowWaterMark', ATTRIBUTE, 'int' , None, None, 
                [('0', '18446744073709551615')], [], 
                '''                Indicates the lowest number of bytes from the memory
                pool that have been used by applications on the physical
                entity since sysUpTime. This object is a 64-bit version
                of cempMemPoolUsedLowWaterMark.
                ''',
                'cempmempoolhcusedlowwatermark',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolLargestFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the largest number of contiguous bytes
                from the memory pool that are currently unused on
                the physical entity.
                ''',
                'cempmempoollargestfree',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolLargestFreeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bits of
                cempMemPoolLargestFree. This object needs to 
                be supported only if the value of 
                cempMemPoolLargestFree exceeds 32-bits, otherwise
                this object value would be set to 0.
                ''',
                'cempmempoollargestfreeovrflw',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolLowestFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The lowest amount of available memory in the memory pool
                recorded at any time during the operation of the system.
                ''',
                'cempmempoollowestfree',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolLowestFreeOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bits of
                cempMemPoolLowestFree. This object needs to
                be supported only if the value of
                cempMemPoolLowestFree exceeds 32-bits, otherwise
                this object value would be set to 0.
                ''',
                'cempmempoollowestfreeovrflw',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual name assigned to the memory pool. This
                object is suitable for output to a human operator,
                and may also be used to distinguish among the various
                pool types.
                ''',
                'cempmempoolname',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolPlatformMemory', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                An indication of the platform-specific memory
                pool type. The associated instance of cempMemPoolType
                is used to indicate the general type of memory pool.
                
                If no platform specific memory hardware type
                identifier exists for this physical entity, or the
                value is unknown by this agent, then the value { 0 0 }
                is returned.
                ''',
                'cempmempoolplatformmemory',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolShared', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of bytes from the memory pool
                that are currently shared on the physical entity.
                ''',
                'cempmempoolshared',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolSharedOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bits of cempMemPoolShared.
                This object needs to be supported only if the value of
                cempMemPoolShared exceeds 32-bits, otherwise this object value
                would be set to 0.
                ''',
                'cempmempoolsharedovrflw',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolType', REFERENCE_ENUM_CLASS, 'CempmempooltypesEnum' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CempmempooltypesEnum', 
                [], [], 
                '''                The type of memory pool for which this entry
                contains information.
                ''',
                'cempmempooltype',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolUsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of bytes from the memory pool
                that are currently in use by applications on the
                physical entity.
                ''',
                'cempmempoolused',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolUsedLowWaterMark', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the lowest number of bytes from the memory pool
                that have been used by applications on the physical entity
                since sysUpTime.Similarly,the Used High
                Watermark indicates the largest number of bytes from
                the memory pool that have been used by applications on
                the physical entity since sysUpTime.This can be
                derived as follows:
                Used High Watermark = cempMemPoolUsed +
                cempMemPoolFree  - cempMemPoolLowestFree.
                ''',
                'cempmempoolusedlowwatermark',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolUsedLowWaterMarkOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bits of
                cempMemPoolUsedLowWaterMark. This object
                needs to be supported only if the value of
                cempMemPoolUsedLowWaterMark exceeds 32-bits,
                otherwise this object value would be set to 0.
                ''',
                'cempmempoolusedlowwatermarkovrflw',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolUsedOvrflw', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object represents the upper 32-bits of cempMemPoolUsed.
                This object needs to be supported only if the used bytes in the
                memory pool exceeds 32-bits, otherwise this object value would
                be set to 0.
                ''',
                'cempmempoolusedovrflw',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolValid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Indicates whether or not cempMemPoolUsed,
                cempMemPoolFree, cempMemPoolLargestFree and 
                cempMemPoolLowestFree in this entry contain accurate 
                data. If an instance of this object has the value 
                false (which in and of itself indicates an internal 
                error condition), the values of these objects
                in the conceptual row may contain inaccurate 
                information (specifically, the reported values may be 
                less than the actual values).
                ''',
                'cempmempoolvalid',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'cempMemPoolEntry',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
    'CiscoEnhancedMempoolMib.Cempmempooltable' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib.Cempmempooltable',
            False, 
            [
            _MetaInfoClassMember('cempMemPoolEntry', REFERENCE_LIST, 'Cempmempoolentry' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry', 
                [], [], 
                '''                An entry in the memory pool monitoring table.
                ''',
                'cempmempoolentry',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'cempMemPoolTable',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
    'CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENHANCED-MEMPOOL-MIB', True),
            _MetaInfoClassMember('cempMemBufferPoolIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Within a physical entity, a unique value used
                to represent each buffer pool.
                ''',
                'cempmembufferpoolindex',
                'CISCO-ENHANCED-MEMPOOL-MIB', True),
            _MetaInfoClassMember('cempMemBufferDynamic', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Boolean poolDynamic; if TRUE, the number of buffers
                in the pool is adjusted (adding more packet buffers 
                or deleting excesses) dynamically by the background 
                process. If FALSE, the number of buffers in the pool 
                is never adjusted, even if it falls below the minimum,
                or to zero.
                ''',
                'cempmembufferdynamic',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of failures to grant a buffer to a
                requester due to reasons other than insufficient 
                memory. For example, in systems where there are 
                different execution contexts, it may be too
                expensive to create new buffers when running in
                certain contexts. In those cases it may be 
                preferable to fail the request.
                ''',
                'cempmembufferfailures',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferFree', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the current number of free buffers in
                the buffer pool on the physical entity.
                Note that the cempMemBufferFree is less than or equal 
                to cempMemBufferTotal.
                ''',
                'cempmembufferfree',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferFreeHit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of successful frees/deallocations
                from the buffer pool.
                ''',
                'cempmembufferfreehit',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferFreeMiss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of unsuccessful attempts
                to free/deallocate a buffer from the buffer pool. 
                For example, this could be due to ownership errors
                where the application that did not assign the 
                buffer is trying to free it.
                ''',
                'cempmembufferfreemiss',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferGrow', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of buffers that have been created in the
                pool when the number of free buffers(cempMemBufferFree)
                was less than minimum(cempMemBufferMix).
                ''',
                'cempmembuffergrow',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferHit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of buffers successfully
                allocated from the buffer pool.
                ''',
                'cempmembufferhit',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferMax', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of free buffers
                allowed in the buffer pool or high-water mark (hwm).
                For example of its usage :
                If cempMemBufferFree > cempMemBufferMax & pool is 
                dynamic, then signal for trim of particular buffer
                pool.
                ''',
                'cempmembuffermax',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferMemPoolIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This index corresponds to the memory pool (with
                cemMemPoolIndex as index in cempMemPoolTable) 
                from which buffers are allocated.
                ''',
                'cempmembuffermempoolindex',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferMin', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the minimum number of free buffers
                allowed in the buffer pool or low-water mark (lwm). 
                For example of its usage :
                If cempMemBufferFree < cempMemBufferMin & pool is 
                dynamic, then signal for growth of particular buffer
                pool.
                ''',
                'cempmembuffermin',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferMiss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of times a buffer has been
                requested, but no buffers were available in the
                buffer pool, or when there were fewer than min 
                buffers(cempMemBufferMin) in the buffer pool.
                Note : For interface pools, a miss is actually 
                a fall back to its corresponding public buffer pool.
                ''',
                'cempmembuffermiss',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferName', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A textual name assigned to the buffer pool. This
                object is suitable for output to a human operator,
                and may also be used to distinguish among the various
                buffer types.
                For example: 'Small', 'Big', 'Serial0/1' etc.
                ''',
                'cempmembuffername',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferNoStorage', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of times the system tried to create new
                buffers, but could not due to insufficient free 
                memory in the system.
                ''',
                'cempmembuffernostorage',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferPeak', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the peak number of buffers in pool on the
                physical entity.
                ''',
                'cempmembufferpeak',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferPeakTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the time of most recent change in the peak
                number of buffers (cempMemBufferPeak object) in the pool.
                ''',
                'cempmembufferpeaktime',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferPermanent', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the total number of permanent buffers in the
                pool on the physical entity.
                ''',
                'cempmembufferpermanent',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferPermChange', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This value is the difference of the desired number
                of permanent buffer & total number of permanent 
                buffers present in the pool. A positive value of 
                this object tells the number of buffers needed & a 
                negative value of the object tells the extra number 
                of buffers in the pool.
                ''',
                'cempmembufferpermchange',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the size of buffer element in number of bytes
                on the physical entity.
                ''',
                'cempmembuffersize',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the total number of buffers
                (include allocated and free buffers) in the
                buffer pool on the physical entity.
                ''',
                'cempmembuffertotal',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferTransient', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the initial number of temporary buffers
                in the pool on the physical entity. This object 
                instructs the system to create this many number of
                temporary extra buffers, just after a system restart. 
                A change in this object will be effective only after
                a system restart.
                ''',
                'cempmembuffertransient',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferTrim', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of buffers that have been trimmed from the
                pool when the number of free buffers 
                (cempMemBufferFree) exceeded the number of max
                allowed buffers(cempMemBufferMax).
                ''',
                'cempmembuffertrim',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'cempMemBufferPoolEntry',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
    'CiscoEnhancedMempoolMib.Cempmembufferpooltable' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib.Cempmembufferpooltable',
            False, 
            [
            _MetaInfoClassMember('cempMemBufferPoolEntry', REFERENCE_LIST, 'Cempmembufferpoolentry' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry', 
                [], [], 
                '''                This contains all the memory buffer pool
                configurations object values. The 
                entPhysicalIndex identifies the entity on which
                memory buffer pools are present.
                ''',
                'cempmembufferpoolentry',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'cempMemBufferPoolTable',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
    'CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry',
            False, 
            [
            _MetaInfoClassMember('entPhysicalIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'entphysicalindex',
                'CISCO-ENHANCED-MEMPOOL-MIB', True),
            _MetaInfoClassMember('cempMemBufferPoolIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                ''',
                'cempmembufferpoolindex',
                'CISCO-ENHANCED-MEMPOOL-MIB', True),
            _MetaInfoClassMember('cempMemBufferCacheHit', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of buffers successfully
                allocated from the cache pool.
                ''',
                'cempmembuffercachehit',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferCacheMiss', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of times a buffer has been
                requested, but no buffers were available in the
                cache pool.
                ''',
                'cempmembuffercachemiss',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferCacheSize', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of buffers in the cache pool
                on the physical entity.
                ''',
                'cempmembuffercachesize',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferCacheThreshold', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the threshold limit for number of cache
                buffers used(cempMemBufferCacheUsed).
                ''',
                'cempmembuffercachethreshold',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferCacheThresholdCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates how many times the number of cache
                buffers used(cempMemBufferCacheUsed) has crossed the
                threshold value(cempMemBufferCacheThreshold).
                ''',
                'cempmembuffercachethresholdcount',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferCacheTotal', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the maximum number of free buffers
                allowed in the cache pool.
                ''',
                'cempmembuffercachetotal',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferCacheUsed', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Indicates the number of cache buffers from the
                pool that are currently used on the physical entity.
                Note that the cempMemBufferCacheUsed is less than or 
                equal to cempMemBufferCacheTotal.
                ''',
                'cempmembuffercacheused',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'cempMemBufferCachePoolEntry',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
    'CiscoEnhancedMempoolMib.Cempmembuffercachepooltable' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib.Cempmembuffercachepooltable',
            False, 
            [
            _MetaInfoClassMember('cempMemBufferCachePoolEntry', REFERENCE_LIST, 'Cempmembuffercachepoolentry' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry', 
                [], [], 
                '''                Each entry represents one of the cache buffer pools
                available in the system and it contains the
                parameters configured for it.
                Note : cempMemBufferCachePoolTable has a sparse
                dependency with cempMemBufferPoolTable (i.e all the
                entires in cempMemBufferPoolTable need not have an
                entry in cempMemBufferCachePoolTable.
                ''',
                'cempmembuffercachepoolentry',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'cempMemBufferCachePoolTable',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
    'CiscoEnhancedMempoolMib' : {
        'meta_info' : _MetaInfoClass('CiscoEnhancedMempoolMib',
            False, 
            [
            _MetaInfoClassMember('cempMemBufferCachePoolTable', REFERENCE_CLASS, 'Cempmembuffercachepooltable' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CiscoEnhancedMempoolMib.Cempmembuffercachepooltable', 
                [], [], 
                '''                A table that lists the cache buffer pools
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
                ''',
                'cempmembuffercachepooltable',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemBufferPoolTable', REFERENCE_CLASS, 'Cempmembufferpooltable' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CiscoEnhancedMempoolMib.Cempmembufferpooltable', 
                [], [], 
                '''                Entries in this table define entities (buffer pools
                in this case) which are contained in an entity 
                (memory pool) defined by an entry from
                cempMemPoolTable.
                -- Basic Pool Architecture --
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
                ''',
                'cempmembufferpooltable',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempMemPoolTable', REFERENCE_CLASS, 'Cempmempooltable' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CiscoEnhancedMempoolMib.Cempmempooltable', 
                [], [], 
                '''                A table of memory pool monitoring entries for all
                physical entities on a managed system.
                ''',
                'cempmempooltable',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            _MetaInfoClassMember('cempNotificationConfig', REFERENCE_CLASS, 'Cempnotificationconfig' , 'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB', 'CiscoEnhancedMempoolMib.Cempnotificationconfig', 
                [], [], 
                '''                ''',
                'cempnotificationconfig',
                'CISCO-ENHANCED-MEMPOOL-MIB', False),
            ],
            'CISCO-ENHANCED-MEMPOOL-MIB',
            'CISCO-ENHANCED-MEMPOOL-MIB',
            _yang_ns._namespaces['CISCO-ENHANCED-MEMPOOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_ENHANCED_MEMPOOL_MIB'
        ),
    },
}
_meta_table['CiscoEnhancedMempoolMib.Cempmempooltable.Cempmempoolentry']['meta_info'].parent =_meta_table['CiscoEnhancedMempoolMib.Cempmempooltable']['meta_info']
_meta_table['CiscoEnhancedMempoolMib.Cempmembufferpooltable.Cempmembufferpoolentry']['meta_info'].parent =_meta_table['CiscoEnhancedMempoolMib.Cempmembufferpooltable']['meta_info']
_meta_table['CiscoEnhancedMempoolMib.Cempmembuffercachepooltable.Cempmembuffercachepoolentry']['meta_info'].parent =_meta_table['CiscoEnhancedMempoolMib.Cempmembuffercachepooltable']['meta_info']
_meta_table['CiscoEnhancedMempoolMib.Cempnotificationconfig']['meta_info'].parent =_meta_table['CiscoEnhancedMempoolMib']['meta_info']
_meta_table['CiscoEnhancedMempoolMib.Cempmempooltable']['meta_info'].parent =_meta_table['CiscoEnhancedMempoolMib']['meta_info']
_meta_table['CiscoEnhancedMempoolMib.Cempmembufferpooltable']['meta_info'].parent =_meta_table['CiscoEnhancedMempoolMib']['meta_info']
_meta_table['CiscoEnhancedMempoolMib.Cempmembuffercachepooltable']['meta_info'].parent =_meta_table['CiscoEnhancedMempoolMib']['meta_info']
