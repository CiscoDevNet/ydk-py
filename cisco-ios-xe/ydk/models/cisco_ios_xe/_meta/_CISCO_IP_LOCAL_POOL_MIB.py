


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoIpLocalPoolMib.Ciplocalpoolconfig' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolconfig',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolNotificationsEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether the notifications defined by the
                ciscoIpLocalPoolNotifGroup are enabled.
                ''',
                'ciplocalpoolnotificationsenable',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolConfig',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolName', ATTRIBUTE, 'str' , None, None, 
                [(1, 48)], [], 
                '''                An arbitrary non-empty string that uniquely identifies the IP
                local pool.  This name must be unique among all the local IP
                pools even when they belong to different pool groups.
                ''',
                'ciplocalpoolname',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the address type of cIpLocalPoolAddressLo
                and cIpLocalPoolAddressHi.
                ''',
                'ciplocalpooladdrtype',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolAddressLo', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the first IP address of the range of IP
                addresses contained by this pool entry.  The address type of
                this object is described by cIpLocalPoolAddrType.
                
                This address must be less than or equal to the address in
                cIpLocalPoolAddressHi.
                ''',
                'ciplocalpooladdresslo',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolAddressHi', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the last IP address of the range of IP
                addresses mapped by this pool entry.  The address type of this
                object is described by cIpLocalPoolAddrType.  If only a single
                address is being mapped, the value of this object is equal to
                the value of cIpLocalPoolAddressLo.
                ''',
                'ciplocalpooladdresshi',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolFreeAddrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP addresses available for use in the range of
                IP addresses.
                ''',
                'ciplocalpoolfreeaddrs',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolGroupContainedIn', ATTRIBUTE, 'str' , None, None, 
                [(0, 48)], [], 
                '''                This object relates an IP local pool to its IP pool group.
                
                A null string indicates this IP local pool is not contained in a
                named IP pool group, but that it is contained in the base IP
                pool group.  An IP local pool can only belong to one IP pool
                group.
                ''',
                'ciplocalpoolgroupcontainedin',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolInUseAddrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP addresses being used in the range of IP
                addresses.
                ''',
                'ciplocalpoolinuseaddrs',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolPriority', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                This object specifies priority of the IP local pool,
                where smaller value indicates the lower priority.
                The priority value is used in assigning IP Address 
                from local pools.
                ''',
                'ciplocalpoolpriority',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                This object facilitates the creation, or deletion of a
                conceptual row in this table.
                ''',
                'ciplocalpoolrowstatus',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolConfigEntry',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolconfigtable',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolConfigEntry', REFERENCE_LIST, 'Ciplocalpoolconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry', 
                [], [], 
                '''                Each entry provides information about a particular IP local
                pool, including the number of free and used addresses and its priority.
                ''',
                'ciplocalpoolconfigentry',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolConfigTable',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolGroupName', ATTRIBUTE, 'str' , None, None, 
                [(0, 48)], [], 
                '''                A unique group name that identifies the IP pool group.  The
                null string represents the base IP pool group.
                ''',
                'ciplocalpoolgroupname',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolChildIndex', ATTRIBUTE, 'str' , None, None, 
                [(1, 48)], [], 
                '''                The value of cIpLocalPoolName for the contained IP local pool.
                ''',
                'ciplocalpoolchildindex',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolGroupContainsEntry',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolGroupContainsEntry', REFERENCE_LIST, 'Ciplocalpoolgroupcontainsentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry', 
                [], [], 
                '''                Each entry describes single container/'containee'
                relationship.
                
                Pool names can only be associated with one group.  Pools carry
                implicit group identifiers because pool names can only be
                associated with one group.  An entry in this table describes
                such an association.
                ''',
                'ciplocalpoolgroupcontainsentry',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolGroupContainsTable',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolGroupName', ATTRIBUTE, 'str' , None, None, 
                [(0, 48)], [], 
                '''                ''',
                'ciplocalpoolgroupname',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolGroupFreeAddrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP addresses available for use in the IP pool
                group.
                ''',
                'ciplocalpoolgroupfreeaddrs',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolGroupInUseAddrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP addresses that have been allocated from the
                IP pool group.
                ''',
                'ciplocalpoolgroupinuseaddrs',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolGroupEntry',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolgrouptable' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolgrouptable',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolGroupEntry', REFERENCE_LIST, 'Ciplocalpoolgroupentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry', 
                [], [], 
                '''                Each entry provides information about a particular IP pool
                group and the number of free and used addresses in an IP pool
                group.
                ''',
                'ciplocalpoolgroupentry',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolGroupTable',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolName', ATTRIBUTE, 'str' , None, None, 
                [(1, 48)], [], 
                '''                ''',
                'ciplocalpoolname',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolPercentAddrThldHi', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                When the percentage of used addresses in an IP local pool
                is equal or exceeds this threshold value, a
                cilpPercentAddrUsedHiNotif notification will be generated. Once
                the notification is generated, it will be disarmed and it will
                not be generated again until the number of used addresses falls
                below the value indicated by cIpLocalPoolPercentAddrThldLo.
                
                The value of this object should never be smaller than the value
                of cIpLocalPoolPercentAddrThldLo.
                ''',
                'ciplocalpoolpercentaddrthldhi',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolPercentAddrThldLo', ATTRIBUTE, 'int' , None, None, 
                [('0', '100')], [], 
                '''                When the percentage of used addresses in an IP local pool
                falls below this threshold value, a cilpPercentAddrUsedLoNotif
                notification will be generated.  Once the notification is
                generated, it will be disarmed and it will not be generated
                again until the number of used addresses equals or exceeds the
                value indicated by cIpLocalPoolPercentAddrThldHi.
                
                The value of this object should never be greater than the value
                of cIpLocalPoolPercentAddrThldHi.
                ''',
                'ciplocalpoolpercentaddrthldlo',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolStatFreeAddrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP addresses available for use in this IP local
                pool.
                ''',
                'ciplocalpoolstatfreeaddrs',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolStatHiWaterUsedAddrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object contains the high water mark of used addresses
                in an IP local pool since pool creation, since the system was
                restarted, or since this object was reset, whichever occurred
                last.  This object can only be set to zero, and by doing so, it
                is reset to the value of cIpLocalPoolStatInUseAddrs.
                
                Since the number of addresses in a pool can be reduced (e.g. by
                deleting one of its ranges), the value of this object may be
                greater than the sum of cIpLocalPoolStatFreeAddrs and
                cIpLocalPoolStatInUseAddrs.
                ''',
                'ciplocalpoolstathiwaterusedaddrs',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolStatInUseAddrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of IP addresses being used in this IP local pool.
                ''',
                'ciplocalpoolstatinuseaddrs',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolStatInUseAddrThldHi', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the number of used addresses in an IP local pool
                is equal or exceeds this threshold value, a
                ciscoIpLocalPoolInUseAddrNoti notification will be generated.
                Once this notification is generated, it will be disarmed and it
                will not be generated again until the number of used address
                falls below the value indicated by
                cIpLocalPoolStatInUseAddrThldLo.
                
                The value of this object should never be smaller than the value
                of cIpLocalPoolStatInUseAddrThldLo.
                ''',
                'ciplocalpoolstatinuseaddrthldhi',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolStatInUseAddrThldLo', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                When the number of used addresses in an IP local pool falls
                below this threshold value, the ciscoIpLocalPoolInUseAddrNoti
                notification will be rearmed.
                
                The value of this object should never be greater than the value
                of cIpLocalPoolStatInUseAddrThldHi.
                ''',
                'ciplocalpoolstatinuseaddrthldlo',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolStatsEntry',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolstatstable' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolstatstable',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolStatsEntry', REFERENCE_LIST, 'Ciplocalpoolstatsentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry', 
                [], [], 
                '''                Each entry provides statistical information about a particular
                IP local pool, and the total number of free and used addresses
                of all the ranges in an IP local pool.
                ''',
                'ciplocalpoolstatsentry',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolStatsTable',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolName', ATTRIBUTE, 'str' , None, None, 
                [(1, 48)], [], 
                '''                ''',
                'ciplocalpoolname',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolAllocAddrType', REFERENCE_ENUM_CLASS, 'InetaddresstypeEnum' , 'ydk.models.cisco_ios_xe.INET_ADDRESS_MIB', 'InetaddresstypeEnum', 
                [], [], 
                '''                This object specifies the address type of
                cIpLocalPoolAllocAddr.
                ''',
                'ciplocalpoolallocaddrtype',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolAllocAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                This object specifies the allocated IP address.  The address
                type of this object is described by cIpLocalPoolAllocAddrType.
                ''',
                'ciplocalpoolallocaddr',
                'CISCO-IP-LOCAL-POOL-MIB', True),
            _MetaInfoClassMember('cIpLocalPoolAllocIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object indicates the interface from which the allocation
                message was sent.
                
                In the case that the interface can not be determined, the value
                of this object will be zero.
                ''',
                'ciplocalpoolallocifindex',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolAllocUser', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                This object indicates the user name of the person from whom the
                allocation message was sent.
                
                In the case that the user name can not be determined, the value
                of this object will the null string.
                ''',
                'ciplocalpoolallocuser',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolAllocEntry',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib.Ciplocalpoolalloctable' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib.Ciplocalpoolalloctable',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolAllocEntry', REFERENCE_LIST, 'Ciplocalpoolallocentry' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry', 
                [], [], 
                '''                Each entry refers to conceptual row that associates an IP
                addresses with the interface where the request was received, and
                the user that requested the address.
                ''',
                'ciplocalpoolallocentry',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'cIpLocalPoolAllocTable',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
    'CiscoIpLocalPoolMib' : {
        'meta_info' : _MetaInfoClass('CiscoIpLocalPoolMib',
            False, 
            [
            _MetaInfoClassMember('cIpLocalPoolAllocTable', REFERENCE_CLASS, 'Ciplocalpoolalloctable' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolalloctable', 
                [], [], 
                '''                This table lists all addresses that have been allocated out of
                an IP local pool.
                
                Entries in this table are created when a remote peer allocates
                an address from one of the IP local pools in the
                cIpLocalPoolConfigTable.
                
                Entries in this table are deleted when a remote peer deallocates
                an address from one of the IP local pool in the
                cIpLocalPoolConfigTable.
                
                Entries in this table are uniquely indexed by the name of the IP
                local pool, and the allocated address, together with its address
                type.
                ''',
                'ciplocalpoolalloctable',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolConfig', REFERENCE_CLASS, 'Ciplocalpoolconfig' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolconfig', 
                [], [], 
                '''                ''',
                'ciplocalpoolconfig',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolConfigTable', REFERENCE_CLASS, 'Ciplocalpoolconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolconfigtable', 
                [], [], 
                '''                This table manages the creation, modification, and deletion
                of IP local pools using the RowStatus textual convention.  An
                entry in this table defines an IP address range that is
                associated with an IP local pool.
                
                A conceptual row in this table can not be modified while
                cIpLocalPoolRowStatus is set to 'active'.
                
                Since IP local pool names are unique even when they belong to
                different groups, and addresses within a group can not overlap,
                a row in this table is uniquely indexed by the pool name, and by
                the low address of the IP local pool together with its address
                type.
                ''',
                'ciplocalpoolconfigtable',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolGroupContainsTable', REFERENCE_CLASS, 'Ciplocalpoolgroupcontainstable' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable', 
                [], [], 
                '''                A table which exposes the container/'containee' relationships
                between local IP pools and IP pool groups.
                
                Entries in this table are created or deleted as a by-product of
                creating or deleting entries in the cIpLocalPoolConfigTable.
                
                When an entry is created and activated in the
                cIpLocalPoolConfigTable table, an entry in this table will come
                into existence if it does not already exist.
                
                When an entry is deleted in the cIpLocalPoolConfigTable table,
                if there is no other entry existing in that table with the same
                cIpLocalPoolGroupContainedIn and cIpLocalPoolName, the entry in
                this table with the respective cIpLocalPoolGroupName and
                cIpLocalPoolName indices will be removed.
                ''',
                'ciplocalpoolgroupcontainstable',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolGroupTable', REFERENCE_CLASS, 'Ciplocalpoolgrouptable' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolgrouptable', 
                [], [], 
                '''                This table provides statistics for configured IP pool groups.
                
                Entries in this table are created as the result of adding a new
                IP pool group to the cIpLocalPoolConfigTable.
                
                Entries in this table are deleted as the result of removing all
                IP local pools that are contained in an IP pool group in the
                cIpLocalPoolConfigTable.
                
                An entry in this table is uniquely indexed by IP pool group
                name.
                ''',
                'ciplocalpoolgrouptable',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            _MetaInfoClassMember('cIpLocalPoolStatsTable', REFERENCE_CLASS, 'Ciplocalpoolstatstable' , 'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB', 'CiscoIpLocalPoolMib.Ciplocalpoolstatstable', 
                [], [], 
                '''                A table providing statistics for each IP local pool.
                
                Entries in this table are created as the result of adding a new
                IP local pool to the cIpLocalPoolConfigTable.
                
                Entries in this table are deleted as the result of removing all
                the address ranges that are contained in an IP local pool in the
                cIpLocalPoolConfigTable.
                
                Entries in this table are uniquely indexed by the name of the IP
                local pool.
                ''',
                'ciplocalpoolstatstable',
                'CISCO-IP-LOCAL-POOL-MIB', False),
            ],
            'CISCO-IP-LOCAL-POOL-MIB',
            'CISCO-IP-LOCAL-POOL-MIB',
            _yang_ns._namespaces['CISCO-IP-LOCAL-POOL-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_IP_LOCAL_POOL_MIB'
        ),
    },
}
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolconfigtable.Ciplocalpoolconfigentry']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolconfigtable']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable.Ciplocalpoolgroupcontainsentry']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolgrouptable.Ciplocalpoolgroupentry']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolgrouptable']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolstatstable.Ciplocalpoolstatsentry']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolstatstable']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolalloctable.Ciplocalpoolallocentry']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolalloctable']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolconfig']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolconfigtable']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolgroupcontainstable']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolgrouptable']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolstatstable']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib']['meta_info']
_meta_table['CiscoIpLocalPoolMib.Ciplocalpoolalloctable']['meta_info'].parent =_meta_table['CiscoIpLocalPoolMib']['meta_info']
