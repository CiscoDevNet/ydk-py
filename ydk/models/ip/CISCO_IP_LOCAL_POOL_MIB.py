""" CISCO_IP_LOCAL_POOL_MIB 

This MIB defines the configuration and monitoring capabilities
relating to local IP pools.

Local IP pools have the following characteristics\:

\- An IP local pool consists of one or more IP address ranges.

\- An IP pool group consists of one or more IP local pools.

\- An IP local pool can only belong to one IP pool group.

\- IP local pools that belong to different groups can have
  overlapping addresses.

\- IP local pool names are unique even when they belong to
  different groups.

\- Addresses within an IP pool group can not overlap.

\- IP local pools without an explicit group name are considered
  members of the base system group.  In this MIB, the base
  system group is represented by a null IP pool group name.

This MIB defines objects that expose the relationship between
IP pool groups and IP local pools.  There exist other objects
that maintain statistics about the address usage of IP local
pools.

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.inet.INET_ADDRESS_MIB import InetAddressType_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum


class CISCOIPLOCALPOOLMIB(object):
    """
    
    
    .. attribute:: ciplocalpoolalloctable
    
    	This table lists all addresses that have been allocated out of an IP local pool.  Entries in this table are created when a remote peer allocates an address from one of the IP local pools in the cIpLocalPoolConfigTable.  Entries in this table are deleted when a remote peer deallocates an address from one of the IP local pool in the cIpLocalPoolConfigTable.  Entries in this table are uniquely indexed by the name of the IP local pool, and the allocated address, together with its address type
    	**type**\: :py:class:`CIpLocalPoolAllocTable <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolAllocTable>`
    
    .. attribute:: ciplocalpoolconfig
    
    	
    	**type**\: :py:class:`CIpLocalPoolConfig <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolConfig>`
    
    .. attribute:: ciplocalpoolconfigtable
    
    	This table manages the creation, modification, and deletion of IP local pools using the RowStatus textual convention.  An entry in this table defines an IP address range that is associated with an IP local pool.  A conceptual row in this table can not be modified while cIpLocalPoolRowStatus is set to 'active'.  Since IP local pool names are unique even when they belong to different groups, and addresses within a group can not overlap, a row in this table is uniquely indexed by the pool name, and by the low address of the IP local pool together with its address type
    	**type**\: :py:class:`CIpLocalPoolConfigTable <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolConfigTable>`
    
    .. attribute:: ciplocalpoolgroupcontainstable
    
    	A table which exposes the container/'containee' relationships between local IP pools and IP pool groups.  Entries in this table are created or deleted as a by\-product of creating or deleting entries in the cIpLocalPoolConfigTable.  When an entry is created and activated in the cIpLocalPoolConfigTable table, an entry in this table will come into existence if it does not already exist.  When an entry is deleted in the cIpLocalPoolConfigTable table, if there is no other entry existing in that table with the same cIpLocalPoolGroupContainedIn and cIpLocalPoolName, the entry in this table with the respective cIpLocalPoolGroupName and cIpLocalPoolName indices will be removed
    	**type**\: :py:class:`CIpLocalPoolGroupContainsTable <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupContainsTable>`
    
    .. attribute:: ciplocalpoolgrouptable
    
    	This table provides statistics for configured IP pool groups.  Entries in this table are created as the result of adding a new IP pool group to the cIpLocalPoolConfigTable.  Entries in this table are deleted as the result of removing all IP local pools that are contained in an IP pool group in the cIpLocalPoolConfigTable.  An entry in this table is uniquely indexed by IP pool group name
    	**type**\: :py:class:`CIpLocalPoolGroupTable <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupTable>`
    
    .. attribute:: ciplocalpoolstatstable
    
    	A table providing statistics for each IP local pool.  Entries in this table are created as the result of adding a new IP local pool to the cIpLocalPoolConfigTable.  Entries in this table are deleted as the result of removing all the address ranges that are contained in an IP local pool in the cIpLocalPoolConfigTable.  Entries in this table are uniquely indexed by the name of the IP local pool
    	**type**\: :py:class:`CIpLocalPoolStatsTable <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolStatsTable>`
    
    

    """

    _prefix = 'cisco-ip'
    _revision = '2007-11-12'

    def __init__(self):
        self.ciplocalpoolalloctable = CISCOIPLOCALPOOLMIB.CIpLocalPoolAllocTable()
        self.ciplocalpoolalloctable.parent = self
        self.ciplocalpoolconfig = CISCOIPLOCALPOOLMIB.CIpLocalPoolConfig()
        self.ciplocalpoolconfig.parent = self
        self.ciplocalpoolconfigtable = CISCOIPLOCALPOOLMIB.CIpLocalPoolConfigTable()
        self.ciplocalpoolconfigtable.parent = self
        self.ciplocalpoolgroupcontainstable = CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupContainsTable()
        self.ciplocalpoolgroupcontainstable.parent = self
        self.ciplocalpoolgrouptable = CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupTable()
        self.ciplocalpoolgrouptable.parent = self
        self.ciplocalpoolstatstable = CISCOIPLOCALPOOLMIB.CIpLocalPoolStatsTable()
        self.ciplocalpoolstatstable.parent = self


    class CIpLocalPoolAllocTable(object):
        """
        This table lists all addresses that have been allocated out of
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
        
        .. attribute:: ciplocalpoolallocentry
        
        	Each entry refers to conceptual row that associates an IP addresses with the interface where the request was received, and the user that requested the address
        	**type**\: list of :py:class:`CIpLocalPoolAllocEntry <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolAllocTable.CIpLocalPoolAllocEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2007-11-12'

        def __init__(self):
            self.parent = None
            self.ciplocalpoolallocentry = YList()
            self.ciplocalpoolallocentry.parent = self
            self.ciplocalpoolallocentry.name = 'ciplocalpoolallocentry'


        class CIpLocalPoolAllocEntry(object):
            """
            Each entry refers to conceptual row that associates an IP
            addresses with the interface where the request was received, and
            the user that requested the address.
            
            .. attribute:: ciplocalpoolallocaddr
            
            	This object specifies the allocated IP address.  The address type of this object is described by cIpLocalPoolAllocAddrType
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciplocalpoolallocaddrtype
            
            	This object specifies the address type of cIpLocalPoolAllocAddr
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciplocalpoolname
            
            	
            	**type**\: str
            
            	**range:** 1..48
            
            .. attribute:: ciplocalpoolallocifindex
            
            	This object indicates the interface from which the allocation message was sent.  In the case that the interface can not be determined, the value of this object will be zero
            	**type**\: int
            
            	**range:** 0..2147483647
            
            .. attribute:: ciplocalpoolallocuser
            
            	This object indicates the user name of the person from whom the allocation message was sent.  In the case that the user name can not be determined, the value of this object will the null string
            	**type**\: str
            
            	**range:** 0..255
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2007-11-12'

            def __init__(self):
                self.parent = None
                self.ciplocalpoolallocaddr = None
                self.ciplocalpoolallocaddrtype = None
                self.ciplocalpoolname = None
                self.ciplocalpoolallocifindex = None
                self.ciplocalpoolallocuser = None

            @property
            def _common_path(self):
                if self.ciplocalpoolallocaddr is None:
                    raise YPYDataValidationError('Key property ciplocalpoolallocaddr is None')
                if self.ciplocalpoolallocaddrtype is None:
                    raise YPYDataValidationError('Key property ciplocalpoolallocaddrtype is None')
                if self.ciplocalpoolname is None:
                    raise YPYDataValidationError('Key property ciplocalpoolname is None')

                return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolAllocTable/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolAllocEntry[CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolAllocAddr = ' + str(self.ciplocalpoolallocaddr) + '][CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolAllocAddrType = ' + str(self.ciplocalpoolallocaddrtype) + '][CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolName = ' + str(self.ciplocalpoolname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciplocalpoolallocaddr is not None:
                    return True

                if self.ciplocalpoolallocaddrtype is not None:
                    return True

                if self.ciplocalpoolname is not None:
                    return True

                if self.ciplocalpoolallocifindex is not None:
                    return True

                if self.ciplocalpoolallocuser is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
                return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolAllocTable.CIpLocalPoolAllocEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolAllocTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciplocalpoolallocentry is not None:
                for child_ref in self.ciplocalpoolallocentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
            return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolAllocTable']['meta_info']


    class CIpLocalPoolConfig(object):
        """
        
        
        .. attribute:: ciplocalpoolnotificationsenable
        
        	An indication of whether the notifications defined by the ciscoIpLocalPoolNotifGroup are enabled
        	**type**\: bool
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2007-11-12'

        def __init__(self):
            self.parent = None
            self.ciplocalpoolnotificationsenable = None

        @property
        def _common_path(self):

            return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolConfig'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciplocalpoolnotificationsenable is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
            return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolConfig']['meta_info']


    class CIpLocalPoolConfigTable(object):
        """
        This table manages the creation, modification, and deletion
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
        
        .. attribute:: ciplocalpoolconfigentry
        
        	Each entry provides information about a particular IP local pool, including the number of free and used addresses and its priority
        	**type**\: list of :py:class:`CIpLocalPoolConfigEntry <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolConfigTable.CIpLocalPoolConfigEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2007-11-12'

        def __init__(self):
            self.parent = None
            self.ciplocalpoolconfigentry = YList()
            self.ciplocalpoolconfigentry.parent = self
            self.ciplocalpoolconfigentry.name = 'ciplocalpoolconfigentry'


        class CIpLocalPoolConfigEntry(object):
            """
            Each entry provides information about a particular IP local
            pool, including the number of free and used addresses and its priority.
            
            .. attribute:: ciplocalpooladdresslo
            
            	This object specifies the first IP address of the range of IP addresses contained by this pool entry.  The address type of this object is described by cIpLocalPoolAddrType.  This address must be less than or equal to the address in cIpLocalPoolAddressHi
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciplocalpooladdrtype
            
            	This object specifies the address type of cIpLocalPoolAddressLo and cIpLocalPoolAddressHi
            	**type**\: :py:class:`InetAddressType_Enum <ydk.models.inet.INET_ADDRESS_MIB.InetAddressType_Enum>`
            
            .. attribute:: ciplocalpoolname
            
            	An arbitrary non\-empty string that uniquely identifies the IP local pool.  This name must be unique among all the local IP pools even when they belong to different pool groups
            	**type**\: str
            
            	**range:** 1..48
            
            .. attribute:: ciplocalpooladdresshi
            
            	This object specifies the last IP address of the range of IP addresses mapped by this pool entry.  The address type of this object is described by cIpLocalPoolAddrType.  If only a single address is being mapped, the value of this object is equal to the value of cIpLocalPoolAddressLo
            	**type**\: str
            
            	**range:** 0..255
            
            .. attribute:: ciplocalpoolfreeaddrs
            
            	The number of IP addresses available for use in the range of IP addresses
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolgroupcontainedin
            
            	This object relates an IP local pool to its IP pool group.  A null string indicates this IP local pool is not contained in a named IP pool group, but that it is contained in the base IP pool group.  An IP local pool can only belong to one IP pool group
            	**type**\: str
            
            	**range:** 0..48
            
            .. attribute:: ciplocalpoolinuseaddrs
            
            	The number of IP addresses being used in the range of IP addresses
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolpriority
            
            	This object specifies priority of the IP local pool, where smaller value indicates the lower priority. The priority value is used in assigning IP Address  from local pools
            	**type**\: int
            
            	**range:** 1..255
            
            .. attribute:: ciplocalpoolrowstatus
            
            	This object facilitates the creation, or deletion of a conceptual row in this table
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2007-11-12'

            def __init__(self):
                self.parent = None
                self.ciplocalpooladdresslo = None
                self.ciplocalpooladdrtype = None
                self.ciplocalpoolname = None
                self.ciplocalpooladdresshi = None
                self.ciplocalpoolfreeaddrs = None
                self.ciplocalpoolgroupcontainedin = None
                self.ciplocalpoolinuseaddrs = None
                self.ciplocalpoolpriority = None
                self.ciplocalpoolrowstatus = None

            @property
            def _common_path(self):
                if self.ciplocalpooladdresslo is None:
                    raise YPYDataValidationError('Key property ciplocalpooladdresslo is None')
                if self.ciplocalpooladdrtype is None:
                    raise YPYDataValidationError('Key property ciplocalpooladdrtype is None')
                if self.ciplocalpoolname is None:
                    raise YPYDataValidationError('Key property ciplocalpoolname is None')

                return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolConfigTable/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolConfigEntry[CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolAddressLo = ' + str(self.ciplocalpooladdresslo) + '][CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolAddrType = ' + str(self.ciplocalpooladdrtype) + '][CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolName = ' + str(self.ciplocalpoolname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciplocalpooladdresslo is not None:
                    return True

                if self.ciplocalpooladdrtype is not None:
                    return True

                if self.ciplocalpoolname is not None:
                    return True

                if self.ciplocalpooladdresshi is not None:
                    return True

                if self.ciplocalpoolfreeaddrs is not None:
                    return True

                if self.ciplocalpoolgroupcontainedin is not None:
                    return True

                if self.ciplocalpoolinuseaddrs is not None:
                    return True

                if self.ciplocalpoolpriority is not None:
                    return True

                if self.ciplocalpoolrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
                return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolConfigTable.CIpLocalPoolConfigEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolConfigTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciplocalpoolconfigentry is not None:
                for child_ref in self.ciplocalpoolconfigentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
            return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolConfigTable']['meta_info']


    class CIpLocalPoolGroupContainsTable(object):
        """
        A table which exposes the container/'containee' relationships
        between local IP pools and IP pool groups.
        
        Entries in this table are created or deleted as a by\-product of
        creating or deleting entries in the cIpLocalPoolConfigTable.
        
        When an entry is created and activated in the
        cIpLocalPoolConfigTable table, an entry in this table will come
        into existence if it does not already exist.
        
        When an entry is deleted in the cIpLocalPoolConfigTable table,
        if there is no other entry existing in that table with the same
        cIpLocalPoolGroupContainedIn and cIpLocalPoolName, the entry in
        this table with the respective cIpLocalPoolGroupName and
        cIpLocalPoolName indices will be removed.
        
        .. attribute:: ciplocalpoolgroupcontainsentry
        
        	Each entry describes single container/'containee' relationship.  Pool names can only be associated with one group.  Pools carry implicit group identifiers because pool names can only be associated with one group.  An entry in this table describes such an association
        	**type**\: list of :py:class:`CIpLocalPoolGroupContainsEntry <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupContainsTable.CIpLocalPoolGroupContainsEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2007-11-12'

        def __init__(self):
            self.parent = None
            self.ciplocalpoolgroupcontainsentry = YList()
            self.ciplocalpoolgroupcontainsentry.parent = self
            self.ciplocalpoolgroupcontainsentry.name = 'ciplocalpoolgroupcontainsentry'


        class CIpLocalPoolGroupContainsEntry(object):
            """
            Each entry describes single container/'containee'
            relationship.
            
            Pool names can only be associated with one group.  Pools carry
            implicit group identifiers because pool names can only be
            associated with one group.  An entry in this table describes
            such an association.
            
            .. attribute:: ciplocalpoolchildindex
            
            	The value of cIpLocalPoolName for the contained IP local pool
            	**type**\: str
            
            	**range:** 1..48
            
            .. attribute:: ciplocalpoolgroupname
            
            	A unique group name that identifies the IP pool group.  The null string represents the base IP pool group
            	**type**\: str
            
            	**range:** 0..48
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2007-11-12'

            def __init__(self):
                self.parent = None
                self.ciplocalpoolchildindex = None
                self.ciplocalpoolgroupname = None

            @property
            def _common_path(self):
                if self.ciplocalpoolchildindex is None:
                    raise YPYDataValidationError('Key property ciplocalpoolchildindex is None')
                if self.ciplocalpoolgroupname is None:
                    raise YPYDataValidationError('Key property ciplocalpoolgroupname is None')

                return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupContainsTable/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupContainsEntry[CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolChildIndex = ' + str(self.ciplocalpoolchildindex) + '][CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupName = ' + str(self.ciplocalpoolgroupname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciplocalpoolchildindex is not None:
                    return True

                if self.ciplocalpoolgroupname is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
                return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupContainsTable.CIpLocalPoolGroupContainsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupContainsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciplocalpoolgroupcontainsentry is not None:
                for child_ref in self.ciplocalpoolgroupcontainsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
            return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupContainsTable']['meta_info']


    class CIpLocalPoolGroupTable(object):
        """
        This table provides statistics for configured IP pool groups.
        
        Entries in this table are created as the result of adding a new
        IP pool group to the cIpLocalPoolConfigTable.
        
        Entries in this table are deleted as the result of removing all
        IP local pools that are contained in an IP pool group in the
        cIpLocalPoolConfigTable.
        
        An entry in this table is uniquely indexed by IP pool group
        name.
        
        .. attribute:: ciplocalpoolgroupentry
        
        	Each entry provides information about a particular IP pool group and the number of free and used addresses in an IP pool group
        	**type**\: list of :py:class:`CIpLocalPoolGroupEntry <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupTable.CIpLocalPoolGroupEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2007-11-12'

        def __init__(self):
            self.parent = None
            self.ciplocalpoolgroupentry = YList()
            self.ciplocalpoolgroupentry.parent = self
            self.ciplocalpoolgroupentry.name = 'ciplocalpoolgroupentry'


        class CIpLocalPoolGroupEntry(object):
            """
            Each entry provides information about a particular IP pool
            group and the number of free and used addresses in an IP pool
            group.
            
            .. attribute:: ciplocalpoolgroupname
            
            	
            	**type**\: str
            
            	**range:** 0..48
            
            .. attribute:: ciplocalpoolgroupfreeaddrs
            
            	The number of IP addresses available for use in the IP pool group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolgroupinuseaddrs
            
            	The number of IP addresses that have been allocated from the IP pool group
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2007-11-12'

            def __init__(self):
                self.parent = None
                self.ciplocalpoolgroupname = None
                self.ciplocalpoolgroupfreeaddrs = None
                self.ciplocalpoolgroupinuseaddrs = None

            @property
            def _common_path(self):
                if self.ciplocalpoolgroupname is None:
                    raise YPYDataValidationError('Key property ciplocalpoolgroupname is None')

                return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupTable/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupEntry[CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupName = ' + str(self.ciplocalpoolgroupname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciplocalpoolgroupname is not None:
                    return True

                if self.ciplocalpoolgroupfreeaddrs is not None:
                    return True

                if self.ciplocalpoolgroupinuseaddrs is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
                return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupTable.CIpLocalPoolGroupEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolGroupTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciplocalpoolgroupentry is not None:
                for child_ref in self.ciplocalpoolgroupentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
            return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolGroupTable']['meta_info']


    class CIpLocalPoolStatsTable(object):
        """
        A table providing statistics for each IP local pool.
        
        Entries in this table are created as the result of adding a new
        IP local pool to the cIpLocalPoolConfigTable.
        
        Entries in this table are deleted as the result of removing all
        the address ranges that are contained in an IP local pool in the
        cIpLocalPoolConfigTable.
        
        Entries in this table are uniquely indexed by the name of the IP
        local pool.
        
        .. attribute:: ciplocalpoolstatsentry
        
        	Each entry provides statistical information about a particular IP local pool, and the total number of free and used addresses of all the ranges in an IP local pool
        	**type**\: list of :py:class:`CIpLocalPoolStatsEntry <ydk.models.ip.CISCO_IP_LOCAL_POOL_MIB.CISCOIPLOCALPOOLMIB.CIpLocalPoolStatsTable.CIpLocalPoolStatsEntry>`
        
        

        """

        _prefix = 'cisco-ip'
        _revision = '2007-11-12'

        def __init__(self):
            self.parent = None
            self.ciplocalpoolstatsentry = YList()
            self.ciplocalpoolstatsentry.parent = self
            self.ciplocalpoolstatsentry.name = 'ciplocalpoolstatsentry'


        class CIpLocalPoolStatsEntry(object):
            """
            Each entry provides statistical information about a particular
            IP local pool, and the total number of free and used addresses
            of all the ranges in an IP local pool.
            
            .. attribute:: ciplocalpoolname
            
            	
            	**type**\: str
            
            	**range:** 1..48
            
            .. attribute:: ciplocalpoolpercentaddrthldhi
            
            	When the percentage of used addresses in an IP local pool is equal or exceeds this threshold value, a cilpPercentAddrUsedHiNotif notification will be generated. Once the notification is generated, it will be disarmed and it will not be generated again until the number of used addresses falls below the value indicated by cIpLocalPoolPercentAddrThldLo.  The value of this object should never be smaller than the value of cIpLocalPoolPercentAddrThldLo
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: ciplocalpoolpercentaddrthldlo
            
            	When the percentage of used addresses in an IP local pool falls below this threshold value, a cilpPercentAddrUsedLoNotif notification will be generated.  Once the notification is generated, it will be disarmed and it will not be generated again until the number of used addresses equals or exceeds the value indicated by cIpLocalPoolPercentAddrThldHi.  The value of this object should never be greater than the value of cIpLocalPoolPercentAddrThldHi
            	**type**\: int
            
            	**range:** 0..100
            
            .. attribute:: ciplocalpoolstatfreeaddrs
            
            	The number of IP addresses available for use in this IP local pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstathiwaterusedaddrs
            
            	This object contains the high water mark of used addresses in an IP local pool since pool creation, since the system was restarted, or since this object was reset, whichever occurred last.  This object can only be set to zero, and by doing so, it is reset to the value of cIpLocalPoolStatInUseAddrs.  Since the number of addresses in a pool can be reduced (e.g. by deleting one of its ranges), the value of this object may be greater than the sum of cIpLocalPoolStatFreeAddrs and cIpLocalPoolStatInUseAddrs
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrs
            
            	The number of IP addresses being used in this IP local pool
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrthldhi
            
            	When the number of used addresses in an IP local pool is equal or exceeds this threshold value, a ciscoIpLocalPoolInUseAddrNoti notification will be generated. Once this notification is generated, it will be disarmed and it will not be generated again until the number of used address falls below the value indicated by cIpLocalPoolStatInUseAddrThldLo.  The value of this object should never be smaller than the value of cIpLocalPoolStatInUseAddrThldLo
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: ciplocalpoolstatinuseaddrthldlo
            
            	When the number of used addresses in an IP local pool falls below this threshold value, the ciscoIpLocalPoolInUseAddrNoti notification will be rearmed.  The value of this object should never be greater than the value of cIpLocalPoolStatInUseAddrThldHi
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'cisco-ip'
            _revision = '2007-11-12'

            def __init__(self):
                self.parent = None
                self.ciplocalpoolname = None
                self.ciplocalpoolpercentaddrthldhi = None
                self.ciplocalpoolpercentaddrthldlo = None
                self.ciplocalpoolstatfreeaddrs = None
                self.ciplocalpoolstathiwaterusedaddrs = None
                self.ciplocalpoolstatinuseaddrs = None
                self.ciplocalpoolstatinuseaddrthldhi = None
                self.ciplocalpoolstatinuseaddrthldlo = None

            @property
            def _common_path(self):
                if self.ciplocalpoolname is None:
                    raise YPYDataValidationError('Key property ciplocalpoolname is None')

                return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolStatsTable/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolStatsEntry[CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolName = ' + str(self.ciplocalpoolname) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ciplocalpoolname is not None:
                    return True

                if self.ciplocalpoolpercentaddrthldhi is not None:
                    return True

                if self.ciplocalpoolpercentaddrthldlo is not None:
                    return True

                if self.ciplocalpoolstatfreeaddrs is not None:
                    return True

                if self.ciplocalpoolstathiwaterusedaddrs is not None:
                    return True

                if self.ciplocalpoolstatinuseaddrs is not None:
                    return True

                if self.ciplocalpoolstatinuseaddrthldhi is not None:
                    return True

                if self.ciplocalpoolstatinuseaddrthldlo is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
                return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolStatsTable.CIpLocalPoolStatsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB/CISCO-IP-LOCAL-POOL-MIB:cIpLocalPoolStatsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.ciplocalpoolstatsentry is not None:
                for child_ref in self.ciplocalpoolstatsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
            return meta._meta_table['CISCOIPLOCALPOOLMIB.CIpLocalPoolStatsTable']['meta_info']

    @property
    def _common_path(self):

        return '/CISCO-IP-LOCAL-POOL-MIB:CISCO-IP-LOCAL-POOL-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.ciplocalpoolalloctable is not None and self.ciplocalpoolalloctable._has_data():
            return True

        if self.ciplocalpoolalloctable is not None and self.ciplocalpoolalloctable.is_presence():
            return True

        if self.ciplocalpoolconfig is not None and self.ciplocalpoolconfig._has_data():
            return True

        if self.ciplocalpoolconfig is not None and self.ciplocalpoolconfig.is_presence():
            return True

        if self.ciplocalpoolconfigtable is not None and self.ciplocalpoolconfigtable._has_data():
            return True

        if self.ciplocalpoolconfigtable is not None and self.ciplocalpoolconfigtable.is_presence():
            return True

        if self.ciplocalpoolgroupcontainstable is not None and self.ciplocalpoolgroupcontainstable._has_data():
            return True

        if self.ciplocalpoolgroupcontainstable is not None and self.ciplocalpoolgroupcontainstable.is_presence():
            return True

        if self.ciplocalpoolgrouptable is not None and self.ciplocalpoolgrouptable._has_data():
            return True

        if self.ciplocalpoolgrouptable is not None and self.ciplocalpoolgrouptable.is_presence():
            return True

        if self.ciplocalpoolstatstable is not None and self.ciplocalpoolstatstable._has_data():
            return True

        if self.ciplocalpoolstatstable is not None and self.ciplocalpoolstatstable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.ip._meta import _CISCO_IP_LOCAL_POOL_MIB as meta
        return meta._meta_table['CISCOIPLOCALPOOLMIB']['meta_info']


