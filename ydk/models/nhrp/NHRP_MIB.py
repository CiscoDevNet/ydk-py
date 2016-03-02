""" NHRP_MIB 

This MIB contains managed object definitions for the Next
Hop Resolution Procol, NHRP, as defined in RFC 2332 [17].

"""


import re
import collections

from enum import Enum

from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict

from ydk.errors import YPYError, YPYDataValidationError


from ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB import AddressFamilyNumbers_Enum
from ydk.models.snmpv2.SNMPv2_TC import RowStatus_Enum
from ydk.models.snmpv2.SNMPv2_TC import StorageType_Enum


class NHRPMIB(object):
    """
    
    
    .. attribute:: nhrpcachetable
    
    	This table contains mappings between internetwork layer addresses and NBMA subnetwork layer addresses
    	**type**\: :py:class:`NhrpCacheTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpCacheTable>`
    
    .. attribute:: nhrpclientnhstable
    
    	A table of NHSes that are available for use by this NHC (client). By default, the agent will add an entry to this table that corresponds to the client's default router
    	**type**\: :py:class:`NhrpClientNhsTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientNhsTable>`
    
    .. attribute:: nhrpclientregistrationtable
    
    	A table of Registration Request Information that needs to be maintained by the NHCs (clients)
    	**type**\: :py:class:`NhrpClientRegistrationTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable>`
    
    .. attribute:: nhrpclientstattable
    
    	This table contains statistics collected by NHRP clients
    	**type**\: :py:class:`NhrpClientStatTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientStatTable>`
    
    .. attribute:: nhrpclienttable
    
    	Information about NHRP clients (NHCs) managed by this agent
    	**type**\: :py:class:`NhrpClientTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientTable>`
    
    .. attribute:: nhrpgeneralobjects
    
    	
    	**type**\: :py:class:`NhrpGeneralObjects <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpGeneralObjects>`
    
    .. attribute:: nhrppurgereqtable
    
    	This table will track Purge Request Information
    	**type**\: :py:class:`NhrpPurgeReqTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpPurgeReqTable>`
    
    .. attribute:: nhrpservercachetable
    
    	This table extends the nhrpCacheTable for NHSes.  If the nhrpCacheTable has a row added due to an NHS or based on information regarding an NHS then a row is also added in this table.  The rows in this table will be created when rows in the nhrpCacheTable are created.  However, there may be rows created in the nhrpCacheTable which do not have corresponding rows in this table.  For example, if the nhrpCacheTable has a row added due to a Next Hop Client which is co\-resident on the same device as the NHS, a row will not be added to this table
    	**type**\: :py:class:`NhrpServerCacheTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerCacheTable>`
    
    .. attribute:: nhrpservernhctable
    
    	A table of NHCs that are available for use by this NHS (Server)
    	**type**\: :py:class:`NhrpServerNhcTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerNhcTable>`
    
    .. attribute:: nhrpserverstattable
    
    	Statistics collected by Next Hop Servers
    	**type**\: :py:class:`NhrpServerStatTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerStatTable>`
    
    .. attribute:: nhrpservertable
    
    	This table contains information for a set of NHSes associated with this agent
    	**type**\: :py:class:`NhrpServerTable <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerTable>`
    
    

    """

    _prefix = 'nhrp-mib'
    _revision = '1999-08-26'

    def __init__(self):
        self.nhrpcachetable = NHRPMIB.NhrpCacheTable()
        self.nhrpcachetable.parent = self
        self.nhrpclientnhstable = NHRPMIB.NhrpClientNhsTable()
        self.nhrpclientnhstable.parent = self
        self.nhrpclientregistrationtable = NHRPMIB.NhrpClientRegistrationTable()
        self.nhrpclientregistrationtable.parent = self
        self.nhrpclientstattable = NHRPMIB.NhrpClientStatTable()
        self.nhrpclientstattable.parent = self
        self.nhrpclienttable = NHRPMIB.NhrpClientTable()
        self.nhrpclienttable.parent = self
        self.nhrpgeneralobjects = NHRPMIB.NhrpGeneralObjects()
        self.nhrpgeneralobjects.parent = self
        self.nhrppurgereqtable = NHRPMIB.NhrpPurgeReqTable()
        self.nhrppurgereqtable.parent = self
        self.nhrpservercachetable = NHRPMIB.NhrpServerCacheTable()
        self.nhrpservercachetable.parent = self
        self.nhrpservernhctable = NHRPMIB.NhrpServerNhcTable()
        self.nhrpservernhctable.parent = self
        self.nhrpserverstattable = NHRPMIB.NhrpServerStatTable()
        self.nhrpserverstattable.parent = self
        self.nhrpservertable = NHRPMIB.NhrpServerTable()
        self.nhrpservertable.parent = self


    class NhrpCacheTable(object):
        """
        This table contains mappings between internetwork layer
        addresses and NBMA subnetwork layer addresses.
        
        .. attribute:: nhrpcacheentry
        
        	A cached mapping between an internetwork layer address and an NBMA address. Entries can be created by the network administrator using the nhrpCacheRowStatus column, or they may be added dynamically based on protocol operation (including NHRP, SCSP, and others, such as ATMARP).  When created based by NHRP protocol operations this entry is largely based on contents contained in the Client Information Entry (CIE).  Zero or more Client Information Entries (CIEs) may be included in the NHRP Packet. For a complete description of the CIE, refer to Section 5.2.0.1 of RFC 2332 [17]
        	**type**\: list of :py:class:`NhrpCacheEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpcacheentry = YList()
            self.nhrpcacheentry.parent = self
            self.nhrpcacheentry.name = 'nhrpcacheentry'


        class NhrpCacheEntry(object):
            """
            A cached mapping between an internetwork layer address
            and an NBMA address. Entries can be created by the
            network administrator using the nhrpCacheRowStatus
            column, or they may be added dynamically based on
            protocol operation (including NHRP, SCSP, and others,
            such as ATMARP).
            
            When created based by NHRP protocol operations
            this entry is largely based on contents contained in
            the Client Information Entry (CIE).
            
            Zero or more Client Information Entries (CIEs) may be
            included in the NHRP Packet. For a complete description
            of the CIE, refer to Section 5.2.0.1 of
            RFC 2332 [17].
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: nhrpcacheindex
            
            	An identifier for this entry that has local significance within the scope of the General Group.  This identifier is used here to uniquely identify this row, and also used in the 'nhrpPurgeTable' for the value of the 'nhrpPurgeCacheIdentifier'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpcacheinternetworkaddr
            
            	The value of the internetwork address of the destination
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpcacheinternetworkaddrtype
            
            	The internetwork layer address type of this Next Hop Resolution Cache entry. The value of this object indicates how to interpret the values of nhrpCacheInternetworkAddr and nhrpCacheNextHopInternetworkAddr
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpcacheholdingtime
            
            	If the value of 'nhrpCacheHoldingTimeValid is true(1) then this object represents the number of seconds that the cache entry will remain in this table.  When this value reaches 0 (zero) the row should be deleted.  If the value of 'nhrpCacheHoldingTimeValid is false(2) then this object is undefined
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpcacheholdingtimevalid
            
            	True(1) is returned if the value of 'nhrpCacheType' is not 'administrativelyAdded'.  Since the value of 'nhrpCacheType' was not configured by a user, the value of 'nhrpCacheHoldingTime' is considered valid.  In other words, the value of 'nhrpCacheHoldingTime' represents the Holding Time for the cache Entry.  If 'nhrpCacheType has been configured by a user, (i.e. the value of 'nhrpCacheType' is 'administrativelyAdded') then false(2) will be returned. This indicates that the value of 'nhrpCacheHoldingTime' is undefined because this row could possibly be backed up in nonvolatile storage
            	**type**\: bool
            
            .. attribute:: nhrpcachenbmaaddr
            
            	The value of the NBMA subnetwork address of the next hop
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpcachenbmaaddrtype
            
            	The NBMA address type. The value of this object indicates how to interpret the values of nhrpCacheNbmaAddr and nhrpCacheNbmaSubaddr
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpcachenbmasubaddr
            
            	The value of the NBMA subaddress of the next hop. If there is no subaddress concept for the NBMA address family, this value will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpcachenegotiatedmtu
            
            	The maximum transmission unit (MTU) that was negotiated or registered for this entity. In other words, this is the actual MTU being used
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpcachenexthopinternetworkaddr
            
            	The value of the internetwork address of the next hop
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpcachepreference
            
            	An object which reflects the Preference value of the Client Information Entry (CIE).  Zero or more Client Information Entries (CIEs) may be included in the NHRP Packet.  One of the fields in the CIE is the Preference.  For a complete description of the CIE, refer to Section 5.2.0.1 of  RFC 2332 [17]
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: nhrpcacheprefixlength
            
            	The number of bits that define the internetwork layer prefix associated with the nhrpCacheInternetworkAddr
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: nhrpcacherowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: nhrpcachestate
            
            	An indication of the state of this entry. The values are\:  'incomplete(1)' The client has sent a NHRP Resolution                 Request but has not yet received the                 NHRP Resolution Reply.   'ackReply(2)'   For a client or server, this is a                 cached valid mapping.  'nakReply(3)'   For a client or server, this is a                 cached NAK mapping
            	**type**\: :py:class:`NhrpCacheState_Enum <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry.NhrpCacheState_Enum>`
            
            .. attribute:: nhrpcachestoragetype
            
            	This value only has meaning when the 'nhrpCacheType' has the value of 'administrativelyAdded'.  When the row is created due to being 'administrativelyAdded', this object reflects whether this row is kept in volatile storage and lost upon reboot or if this row is backed up by non\-volatile or permanent storage.  If the value of 'nhrpCacheType' has a value which is not 'administrativelyAdded, then the value of this object is 'other(1)'
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            .. attribute:: nhrpcachetype
            
            	An indication of how this cache entry was created. The values are\:  'other(1)'                   The entry was added by some                              other means.  'register(2)'                In a server, added based on a                              client registration.  'resolveAuthoritative(3)'    In a client, added based on                              receiving an Authoritative                              NHRP Resolution Reply.     'resolveNonauthoritative(4)' In a client, added based on                              receiving a Nonauthoritative                              NHRP Resolution Reply.  'transit(5)'                 In a transit server, added by                              examining a forwarded NHRP                              packet.  'administrativelyAdded(6)'   In a client or server,                              manually added by the                              administrator. The                              StorageType of this entry is                              reflected in                              'nhrpCacheStorageType'.  'atmarp(7)'                  The entry was added due to an                              ATMARP.  'scsp(8)'                    The entry was added due to                              SCSP.   When the entry is under creation using the nhrpCacheRowStatus column, the only value that can be specified by the administrator is 'administrativelyAdded'. Attempting to set any other value will cause an 'inconsistentValue' error.  The value cannot be modified once the entry is active
            	**type**\: :py:class:`NhrpCacheType_Enum <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpCacheTable.NhrpCacheEntry.NhrpCacheType_Enum>`
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.nhrpcacheindex = None
                self.nhrpcacheinternetworkaddr = None
                self.nhrpcacheinternetworkaddrtype = None
                self.nhrpcacheholdingtime = None
                self.nhrpcacheholdingtimevalid = None
                self.nhrpcachenbmaaddr = None
                self.nhrpcachenbmaaddrtype = None
                self.nhrpcachenbmasubaddr = None
                self.nhrpcachenegotiatedmtu = None
                self.nhrpcachenexthopinternetworkaddr = None
                self.nhrpcachepreference = None
                self.nhrpcacheprefixlength = None
                self.nhrpcacherowstatus = None
                self.nhrpcachestate = None
                self.nhrpcachestoragetype = None
                self.nhrpcachetype = None

            class NhrpCacheState_Enum(Enum):
                """
                NhrpCacheState_Enum

                An indication of the state of this entry. The values are\:
                
                'incomplete(1)' The client has sent a NHRP Resolution
                                Request but has not yet received the
                                NHRP Resolution Reply.
                
                
                'ackReply(2)'   For a client or server, this is a
                                cached valid mapping.
                
                'nakReply(3)'   For a client or server, this is a
                                cached NAK mapping.

                """

                INCOMPLETE = 1

                ACKREPLY = 2

                NAKREPLY = 3


                @staticmethod
                def _meta_info():
                    from ydk.models.nhrp._meta import _NHRP_MIB as meta
                    return meta._meta_table['NHRPMIB.NhrpCacheTable.NhrpCacheEntry.NhrpCacheState_Enum']


            class NhrpCacheType_Enum(Enum):
                """
                NhrpCacheType_Enum

                An indication of how this cache entry
                was created. The values are\:
                
                'other(1)'                   The entry was added by some
                                             other means.
                
                'register(2)'                In a server, added based on a
                                             client registration.
                
                'resolveAuthoritative(3)'    In a client, added based on
                                             receiving an Authoritative
                                             NHRP Resolution Reply.
                
                
                
                
                'resolveNonauthoritative(4)' In a client, added based on
                                             receiving a Nonauthoritative
                                             NHRP Resolution Reply.
                
                'transit(5)'                 In a transit server, added by
                                             examining a forwarded NHRP
                                             packet.
                
                'administrativelyAdded(6)'   In a client or server,
                                             manually added by the
                                             administrator. The
                                             StorageType of this entry is
                                             reflected in
                                             'nhrpCacheStorageType'.
                
                'atmarp(7)'                  The entry was added due to an
                                             ATMARP.
                
                'scsp(8)'                    The entry was added due to
                                             SCSP.
                
                
                When the entry is under creation using the
                nhrpCacheRowStatus column, the only value that can be
                specified by the administrator is 'administrativelyAdded'.
                Attempting to set any other value will cause an
                'inconsistentValue' error.
                
                The value cannot be modified once the entry is active.

                """

                OTHER = 1

                REGISTER = 2

                RESOLVEAUTHORITATIVE = 3

                RESOVENONAUTHORITATIVE = 4

                TRANSIT = 5

                ADMINISTRATIVELYADDED = 6

                ATMARP = 7

                SCSP = 8


                @staticmethod
                def _meta_info():
                    from ydk.models.nhrp._meta import _NHRP_MIB as meta
                    return meta._meta_table['NHRPMIB.NhrpCacheTable.NhrpCacheEntry.NhrpCacheType_Enum']


            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.nhrpcacheindex is None:
                    raise YPYDataValidationError('Key property nhrpcacheindex is None')
                if self.nhrpcacheinternetworkaddr is None:
                    raise YPYDataValidationError('Key property nhrpcacheinternetworkaddr is None')
                if self.nhrpcacheinternetworkaddrtype is None:
                    raise YPYDataValidationError('Key property nhrpcacheinternetworkaddrtype is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpCacheTable/NHRP-MIB:nhrpCacheEntry[NHRP-MIB:ifIndex = ' + str(self.ifindex) + '][NHRP-MIB:nhrpCacheIndex = ' + str(self.nhrpcacheindex) + '][NHRP-MIB:nhrpCacheInternetworkAddr = ' + str(self.nhrpcacheinternetworkaddr) + '][NHRP-MIB:nhrpCacheInternetworkAddrType = ' + str(self.nhrpcacheinternetworkaddrtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.nhrpcacheindex is not None:
                    return True

                if self.nhrpcacheinternetworkaddr is not None:
                    return True

                if self.nhrpcacheinternetworkaddrtype is not None:
                    return True

                if self.nhrpcacheholdingtime is not None:
                    return True

                if self.nhrpcacheholdingtimevalid is not None:
                    return True

                if self.nhrpcachenbmaaddr is not None:
                    return True

                if self.nhrpcachenbmaaddrtype is not None:
                    return True

                if self.nhrpcachenbmasubaddr is not None:
                    return True

                if self.nhrpcachenegotiatedmtu is not None:
                    return True

                if self.nhrpcachenexthopinternetworkaddr is not None:
                    return True

                if self.nhrpcachepreference is not None:
                    return True

                if self.nhrpcacheprefixlength is not None:
                    return True

                if self.nhrpcacherowstatus is not None:
                    return True

                if self.nhrpcachestate is not None:
                    return True

                if self.nhrpcachestoragetype is not None:
                    return True

                if self.nhrpcachetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpCacheTable.NhrpCacheEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpCacheTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpcacheentry is not None:
                for child_ref in self.nhrpcacheentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpCacheTable']['meta_info']


    class NhrpClientNhsTable(object):
        """
        A table of NHSes that are available for use by this NHC
        (client). By default, the agent will add an entry to this
        table that corresponds to the client's default router.
        
        .. attribute:: nhrpclientnhsentry
        
        	An NHS that may be used by an NHC
        	**type**\: list of :py:class:`NhrpClientNhsEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientNhsTable.NhrpClientNhsEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpclientnhsentry = YList()
            self.nhrpclientnhsentry.parent = self
            self.nhrpclientnhsentry.name = 'nhrpclientnhsentry'


        class NhrpClientNhsEntry(object):
            """
            An NHS that may be used by an NHC.
            
            .. attribute:: nhrpclientindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientnhsindex
            
            	An identifier for an NHS available to an NHC
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientnhsinternetworkaddr
            
            	The value of the destination internetwork layer address of the NHRP server represented by this    entry.  If this value is not known, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpclientnhsinternetworkaddrtype
            
            	The type of the internetwork layer address of the NHRP server represented in this entry. This object indicates how the value of nhrpClientNhsInternetworkAddr is to be interpreted
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpclientnhsinuse
            
            	An indication of whether this NHS is in use by the NHC
            	**type**\: bool
            
            .. attribute:: nhrpclientnhsnbmaaddr
            
            	The NBMA subnetwork address of the NHS. The type of the address is indicated by the corresponding value of nhrpClientNhsNbmaAddrType
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpclientnhsnbmaaddrtype
            
            	The type of the NBMA subnetwork address of the NHRP Server represented by this entry. This object indicates how the values of nhrpClientNhsNbmaAddr and nhrpClientNhsNbmaSubaddr are to be interpreted
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpclientnhsnbmasubaddr
            
            	The NBMA subaddress of the NHS. For NMBA address families that do not have the concept of subaddress,      this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpclientnhsrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrpclientindex = None
                self.nhrpclientnhsindex = None
                self.nhrpclientnhsinternetworkaddr = None
                self.nhrpclientnhsinternetworkaddrtype = None
                self.nhrpclientnhsinuse = None
                self.nhrpclientnhsnbmaaddr = None
                self.nhrpclientnhsnbmaaddrtype = None
                self.nhrpclientnhsnbmasubaddr = None
                self.nhrpclientnhsrowstatus = None

            @property
            def _common_path(self):
                if self.nhrpclientindex is None:
                    raise YPYDataValidationError('Key property nhrpclientindex is None')
                if self.nhrpclientnhsindex is None:
                    raise YPYDataValidationError('Key property nhrpclientnhsindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientNhsTable/NHRP-MIB:nhrpClientNhsEntry[NHRP-MIB:nhrpClientIndex = ' + str(self.nhrpclientindex) + '][NHRP-MIB:nhrpClientNhsIndex = ' + str(self.nhrpclientnhsindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrpclientindex is not None:
                    return True

                if self.nhrpclientnhsindex is not None:
                    return True

                if self.nhrpclientnhsinternetworkaddr is not None:
                    return True

                if self.nhrpclientnhsinternetworkaddrtype is not None:
                    return True

                if self.nhrpclientnhsinuse is not None:
                    return True

                if self.nhrpclientnhsnbmaaddr is not None:
                    return True

                if self.nhrpclientnhsnbmaaddrtype is not None:
                    return True

                if self.nhrpclientnhsnbmasubaddr is not None:
                    return True

                if self.nhrpclientnhsrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpClientNhsTable.NhrpClientNhsEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientNhsTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpclientnhsentry is not None:
                for child_ref in self.nhrpclientnhsentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpClientNhsTable']['meta_info']


    class NhrpClientRegistrationTable(object):
        """
        A table of Registration Request Information that
        needs to be maintained by the NHCs (clients).
        
        .. attribute:: nhrpclientregistrationentry
        
        	An NHC needs to maintain registration request information between the NHC and the NHS.  An entry in this table represents information for a single registration request
        	**type**\: list of :py:class:`NhrpClientRegistrationEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpclientregistrationentry = YList()
            self.nhrpclientregistrationentry.parent = self
            self.nhrpclientregistrationentry.name = 'nhrpclientregistrationentry'


        class NhrpClientRegistrationEntry(object):
            """
            An NHC needs to maintain registration request information
            between the NHC and the NHS.  An entry in this table
            represents information for a single registration request.
            
            .. attribute:: nhrpclientindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientregindex
            
            	An identifier for this entry such that it identifies a specific Registration Request from the NHC represented by the nhrpClientIndex
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientregrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: nhrpclientregstate
            
            	The registration state of this client. The values are\: 'other(1)'             The state of the registration                        request is not one of                        'registering',                        'ackRegisterReply' or                        'nakRegisterReply'.  'registering(2)'        A registration request has                         been issued and a registration                         reply is expected.  'ackRegisterReply(3)'   A positive registration reply                         has been received.  'nakRegisterReply(4)'   The client has received a                         negative registration                         reply (NAK)
            	**type**\: :py:class:`NhrpClientRegState_Enum <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegState_Enum>`
            
            .. attribute:: nhrpclientreguniqueness
            
            	The Uniqueness indicator for this Registration Request. If this object has the value of requestUnique(1), then the Uniqueness bit is set in the the NHRP Registration Request represented by this row.  The value cannot be changed once the row is created
            	**type**\: :py:class:`NhrpClientRegUniqueness_Enum <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegUniqueness_Enum>`
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrpclientindex = None
                self.nhrpclientregindex = None
                self.nhrpclientregrowstatus = None
                self.nhrpclientregstate = None
                self.nhrpclientreguniqueness = None

            class NhrpClientRegState_Enum(Enum):
                """
                NhrpClientRegState_Enum

                The registration state of this client. The values are\:
                'other(1)'             The state of the registration
                                       request is not one of
                                       'registering',
                                       'ackRegisterReply' or
                                       'nakRegisterReply'.
                
                'registering(2)'        A registration request has
                                        been issued and a registration
                                        reply is expected.
                
                'ackRegisterReply(3)'   A positive registration reply
                                        has been received.
                
                'nakRegisterReply(4)'   The client has received a
                                        negative registration
                                        reply (NAK).

                """

                OTHER = 1

                REGISTERING = 2

                ACKREGISTERREPLY = 3

                NAKREGISTERREPLY = 4


                @staticmethod
                def _meta_info():
                    from ydk.models.nhrp._meta import _NHRP_MIB as meta
                    return meta._meta_table['NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegState_Enum']


            class NhrpClientRegUniqueness_Enum(Enum):
                """
                NhrpClientRegUniqueness_Enum

                The Uniqueness indicator for this Registration Request.
                If this object has the value of requestUnique(1), then
                the Uniqueness bit is set in the the NHRP Registration
                Request represented by this row.  The value cannot
                be changed once the row is created.

                """

                REQUESTUNIQUE = 1

                REQUESTNOTUNIQUE = 2


                @staticmethod
                def _meta_info():
                    from ydk.models.nhrp._meta import _NHRP_MIB as meta
                    return meta._meta_table['NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry.NhrpClientRegUniqueness_Enum']


            @property
            def _common_path(self):
                if self.nhrpclientindex is None:
                    raise YPYDataValidationError('Key property nhrpclientindex is None')
                if self.nhrpclientregindex is None:
                    raise YPYDataValidationError('Key property nhrpclientregindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientRegistrationTable/NHRP-MIB:nhrpClientRegistrationEntry[NHRP-MIB:nhrpClientIndex = ' + str(self.nhrpclientindex) + '][NHRP-MIB:nhrpClientRegIndex = ' + str(self.nhrpclientregindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrpclientindex is not None:
                    return True

                if self.nhrpclientregindex is not None:
                    return True

                if self.nhrpclientregrowstatus is not None:
                    return True

                if self.nhrpclientregstate is not None:
                    return True

                if self.nhrpclientreguniqueness is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpClientRegistrationTable.NhrpClientRegistrationEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientRegistrationTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpclientregistrationentry is not None:
                for child_ref in self.nhrpclientregistrationentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpClientRegistrationTable']['meta_info']


    class NhrpClientStatTable(object):
        """
        This table contains statistics collected by NHRP
        clients.
        
        .. attribute:: nhrpclientstatentry
        
        	Statistics collected by a NHRP client
        	**type**\: list of :py:class:`NhrpClientStatEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientStatTable.NhrpClientStatEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpclientstatentry = YList()
            self.nhrpclientstatentry.parent = self
            self.nhrpclientstatentry.name = 'nhrpclientstatentry'


        class NhrpClientStatEntry(object):
            """
            Statistics collected by a NHRP client.
            
            .. attribute:: nhrpclientindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientstatdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this Client's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the local management subsystem or the NHRP Client re\-initialization associated with this entry, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Authentication Failure'.      Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrinvalidextension
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrloopdetected
            
            	The number of NHRP Error Indication packets received by this client with the error code 'NHRP Loop Detected'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrprotoerror
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets received by this client with the error code 'NHRP SDU Size  Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets received by this client with the error code 'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxpurgereply
            
            	The number of NHRP Purge Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxpurgereq
            
            	The number of NHRP Purge Requests received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisterack
            
            	The number of positively acknowledged NHRP Registration Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisternakalreadyreg
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Unique Internetworking Layer Address Already Registered'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisternakinsufresources
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxregisternakprohibited
            
            	The number of NAKed NHRP Registration Replies received by this client that contained the code indicating 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplyack
            
            	The number of positively acknowledged NHRP Resolution Replies received by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynakinsufresources
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynaknobinding
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'No Internetworking Layer Address to NBMA Address Binding Exists'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynaknotunique
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Binding Exists But Is Not Unique'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstatrxresolvereplynakprohibited
            
            	The number of NAKed NHRP Resolution Replies received by this client that contained the code indicating 'Administratively Prohibited'.   Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxerrorindication
            
            	The number of NHRP Error Indication packets transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxpurgereply
            
            	The number of NHRP Purge Replies transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxpurgereq
            
            	The number of NHRP Purge Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxregisterreq
            
            	The number of NHRP Registration Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientstattxresolvereq
            
            	The number of NHRP Resolution Requests transmitted by this client.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Client re\-initialization and at other times as indicated by the value of nhrpClientStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrpclientindex = None
                self.nhrpclientstatdiscontinuitytime = None
                self.nhrpclientstatrxerrauthenticationfailure = None
                self.nhrpclientstatrxerrhopcountexceeded = None
                self.nhrpclientstatrxerrinvalidextension = None
                self.nhrpclientstatrxerrloopdetected = None
                self.nhrpclientstatrxerrprotoaddrunreachable = None
                self.nhrpclientstatrxerrprotoerror = None
                self.nhrpclientstatrxerrsdusizeexceeded = None
                self.nhrpclientstatrxerrunrecognizedextension = None
                self.nhrpclientstatrxpurgereply = None
                self.nhrpclientstatrxpurgereq = None
                self.nhrpclientstatrxregisterack = None
                self.nhrpclientstatrxregisternakalreadyreg = None
                self.nhrpclientstatrxregisternakinsufresources = None
                self.nhrpclientstatrxregisternakprohibited = None
                self.nhrpclientstatrxresolvereplyack = None
                self.nhrpclientstatrxresolvereplynakinsufresources = None
                self.nhrpclientstatrxresolvereplynaknobinding = None
                self.nhrpclientstatrxresolvereplynaknotunique = None
                self.nhrpclientstatrxresolvereplynakprohibited = None
                self.nhrpclientstattxerrorindication = None
                self.nhrpclientstattxpurgereply = None
                self.nhrpclientstattxpurgereq = None
                self.nhrpclientstattxregisterreq = None
                self.nhrpclientstattxresolvereq = None

            @property
            def _common_path(self):
                if self.nhrpclientindex is None:
                    raise YPYDataValidationError('Key property nhrpclientindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientStatTable/NHRP-MIB:nhrpClientStatEntry[NHRP-MIB:nhrpClientIndex = ' + str(self.nhrpclientindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrpclientindex is not None:
                    return True

                if self.nhrpclientstatdiscontinuitytime is not None:
                    return True

                if self.nhrpclientstatrxerrauthenticationfailure is not None:
                    return True

                if self.nhrpclientstatrxerrhopcountexceeded is not None:
                    return True

                if self.nhrpclientstatrxerrinvalidextension is not None:
                    return True

                if self.nhrpclientstatrxerrloopdetected is not None:
                    return True

                if self.nhrpclientstatrxerrprotoaddrunreachable is not None:
                    return True

                if self.nhrpclientstatrxerrprotoerror is not None:
                    return True

                if self.nhrpclientstatrxerrsdusizeexceeded is not None:
                    return True

                if self.nhrpclientstatrxerrunrecognizedextension is not None:
                    return True

                if self.nhrpclientstatrxpurgereply is not None:
                    return True

                if self.nhrpclientstatrxpurgereq is not None:
                    return True

                if self.nhrpclientstatrxregisterack is not None:
                    return True

                if self.nhrpclientstatrxregisternakalreadyreg is not None:
                    return True

                if self.nhrpclientstatrxregisternakinsufresources is not None:
                    return True

                if self.nhrpclientstatrxregisternakprohibited is not None:
                    return True

                if self.nhrpclientstatrxresolvereplyack is not None:
                    return True

                if self.nhrpclientstatrxresolvereplynakinsufresources is not None:
                    return True

                if self.nhrpclientstatrxresolvereplynaknobinding is not None:
                    return True

                if self.nhrpclientstatrxresolvereplynaknotunique is not None:
                    return True

                if self.nhrpclientstatrxresolvereplynakprohibited is not None:
                    return True

                if self.nhrpclientstattxerrorindication is not None:
                    return True

                if self.nhrpclientstattxpurgereply is not None:
                    return True

                if self.nhrpclientstattxpurgereq is not None:
                    return True

                if self.nhrpclientstattxregisterreq is not None:
                    return True

                if self.nhrpclientstattxresolvereq is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpClientStatTable.NhrpClientStatEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientStatTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpclientstatentry is not None:
                for child_ref in self.nhrpclientstatentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpClientStatTable']['meta_info']


    class NhrpClientTable(object):
        """
        Information about NHRP clients (NHCs) managed by this
        agent.
        
        .. attribute:: nhrpcliententry
        
        	Information about a single NHC
        	**type**\: list of :py:class:`NhrpClientEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpClientTable.NhrpClientEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpcliententry = YList()
            self.nhrpcliententry.parent = self
            self.nhrpcliententry.name = 'nhrpcliententry'


        class NhrpClientEntry(object):
            """
            Information about a single NHC.
            
            .. attribute:: nhrpclientindex
            
            	An identifier for the NHRP client that is unique within the scope of this agent.  The 'nhrpNextIndex' value should be consulted (read), prior to creating a row in this table, and the value returned from reading 'nhrpNextIndex' should be used as this object's value
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpclientdefaultmtu
            
            	The default maximum transmission unit (MTU) of the LIS/LAG which this client should use. This object will be initialized by the agent to the default MTU of the LIS/LAG (which is 9180) unless a different MTU value is specified during creation of this Client
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientholdtime
            
            	The hold time the client will register
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientinitialrequesttimeout
            
            	The number of seconds that the client will wait before timing out an NHRP initial request.  This object only has meaning for the initial timeout period
            	**type**\: int
            
            	**range:** 1..900
            
            .. attribute:: nhrpclientinternetworkaddr
            
            	The value of the internetwork layer address of this client
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpclientinternetworkaddrtype
            
            	The type of the internetwork layer address of this client. This object indicates how the value of nhrpClientInternetworkAddr is to be interpreted
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpclientnbmaaddr
            
            	The NBMA subnetwork address of this client
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpclientnbmaaddrtype
            
            	The type of the NBMA subnetwork address of this client. This object indicates how the values of nhrpClientNbmaAddr and nhrpClientNbmaSubaddr are to be interpreted
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpclientnbmasubaddr
            
            	The NBMA subaddress of this client. For NBMA address families without a subaddress concept, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpclientpurgerequestretries
            
            	The number of times the client will retry a purge request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientregistrationrequestretries
            
            	The number of times the client will retry the registration request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientrequestid
            
            	The Request ID used to register this client with its server. According to Section 5.2.3 of the NHRP Specification, RFC 2332 [17], the Request ID must be kept in non\-volatile storage, so that if an NHC crashes and  re\-initializes, it will use a different  Request ID during the registration process when reregistering with the same NHS
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpclientresolutionrequestretries
            
            	The number of times the client will retry the resolution request before failure. A value of 0 means don't retry. A value of 65535 means retry forever
            	**type**\: int
            
            	**range:** 0..65535
            
            .. attribute:: nhrpclientrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: nhrpclientstoragetype
            
            	This object defines whether this row is kept in volatile storage and lost upon a Client crash or reboot situation, or if this row is backed up by nonvolatile or permanent storage
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrpclientindex = None
                self.nhrpclientdefaultmtu = None
                self.nhrpclientholdtime = None
                self.nhrpclientinitialrequesttimeout = None
                self.nhrpclientinternetworkaddr = None
                self.nhrpclientinternetworkaddrtype = None
                self.nhrpclientnbmaaddr = None
                self.nhrpclientnbmaaddrtype = None
                self.nhrpclientnbmasubaddr = None
                self.nhrpclientpurgerequestretries = None
                self.nhrpclientregistrationrequestretries = None
                self.nhrpclientrequestid = None
                self.nhrpclientresolutionrequestretries = None
                self.nhrpclientrowstatus = None
                self.nhrpclientstoragetype = None

            @property
            def _common_path(self):
                if self.nhrpclientindex is None:
                    raise YPYDataValidationError('Key property nhrpclientindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientTable/NHRP-MIB:nhrpClientEntry[NHRP-MIB:nhrpClientIndex = ' + str(self.nhrpclientindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrpclientindex is not None:
                    return True

                if self.nhrpclientdefaultmtu is not None:
                    return True

                if self.nhrpclientholdtime is not None:
                    return True

                if self.nhrpclientinitialrequesttimeout is not None:
                    return True

                if self.nhrpclientinternetworkaddr is not None:
                    return True

                if self.nhrpclientinternetworkaddrtype is not None:
                    return True

                if self.nhrpclientnbmaaddr is not None:
                    return True

                if self.nhrpclientnbmaaddrtype is not None:
                    return True

                if self.nhrpclientnbmasubaddr is not None:
                    return True

                if self.nhrpclientpurgerequestretries is not None:
                    return True

                if self.nhrpclientregistrationrequestretries is not None:
                    return True

                if self.nhrpclientrequestid is not None:
                    return True

                if self.nhrpclientresolutionrequestretries is not None:
                    return True

                if self.nhrpclientrowstatus is not None:
                    return True

                if self.nhrpclientstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpClientTable.NhrpClientEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpClientTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpcliententry is not None:
                for child_ref in self.nhrpcliententry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpClientTable']['meta_info']


    class NhrpGeneralObjects(object):
        """
        
        
        .. attribute:: nhrpnextindex
        
        	This scalar is used for creating rows in the nhrpClientTable and the nhrpServerTable. The value of this variable is a currently unused value for nhrpClientIndex and nhrpServerIndex.     The value returned when reading this variable must be unique for the NHC's and NHS's indices associated with this row. Subsequent attempts to read this variable must return different values.  NOTE\:  this object exists in the General Group because it is to be used in establishing rows in the nhrpClientTable and the nhrpServerTable.  In other words, the value retrieved from this object could become the value of nhrpClientIndex and nhprServerIndex.  In the situation of an agent re\-initialization the value of this object must be saved in non\-volatile storage.  This variable will return the special value 0 if no new rows can be created
        	**type**\: int
        
        	**range:** 0..4294967295
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpnextindex = None

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpGeneralObjects'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpnextindex is not None:
                return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpGeneralObjects']['meta_info']


    class NhrpPurgeReqTable(object):
        """
        This table will track Purge Request Information.
        
        .. attribute:: nhrppurgereqentry
        
        	Information regarding a Purge Request
        	**type**\: list of :py:class:`NhrpPurgeReqEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpPurgeReqTable.NhrpPurgeReqEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrppurgereqentry = YList()
            self.nhrppurgereqentry.parent = self
            self.nhrppurgereqentry.name = 'nhrppurgereqentry'


        class NhrpPurgeReqEntry(object):
            """
            Information regarding a Purge Request.
            
            .. attribute:: nhrppurgeindex
            
            	An index for this entry that has local significance within the scope of this table
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrppurgecacheidentifier
            
            	This object identifies which row in 'nhrpCacheTable' is being purged.  This object should have the same value as the 'nhrpCacheIndex' in the 'nhrpCacheTable'
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrppurgeprefixlength
            
            	In the case of NHRP Purge Requests, this specifies the equivalence class of addresses which match the first 'Prefix Length' bit positions of the Client Protocol Address specified in the Client Information Entry (CIE)
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: nhrppurgereplyexpected
            
            	An indication of whether this Purge Request has the 'N' Bit cleared (off)
            	**type**\: bool
            
            .. attribute:: nhrppurgerequestid
            
            	The Request ID used in the purge request
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrppurgerowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrppurgeindex = None
                self.nhrppurgecacheidentifier = None
                self.nhrppurgeprefixlength = None
                self.nhrppurgereplyexpected = None
                self.nhrppurgerequestid = None
                self.nhrppurgerowstatus = None

            @property
            def _common_path(self):
                if self.nhrppurgeindex is None:
                    raise YPYDataValidationError('Key property nhrppurgeindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpPurgeReqTable/NHRP-MIB:nhrpPurgeReqEntry[NHRP-MIB:nhrpPurgeIndex = ' + str(self.nhrppurgeindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrppurgeindex is not None:
                    return True

                if self.nhrppurgecacheidentifier is not None:
                    return True

                if self.nhrppurgeprefixlength is not None:
                    return True

                if self.nhrppurgereplyexpected is not None:
                    return True

                if self.nhrppurgerequestid is not None:
                    return True

                if self.nhrppurgerowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpPurgeReqTable.NhrpPurgeReqEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpPurgeReqTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrppurgereqentry is not None:
                for child_ref in self.nhrppurgereqentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpPurgeReqTable']['meta_info']


    class NhrpServerCacheTable(object):
        """
        This table extends the nhrpCacheTable for
        NHSes.  If the nhrpCacheTable has a row added due to
        an NHS or based on information regarding an NHS then
        a row is also added in this table.
        
        The rows in this table will be created when rows in
        the nhrpCacheTable are created.  However, there may
        be rows created in the nhrpCacheTable which do not
        have corresponding rows in this table.  For example,
        if the nhrpCacheTable has a row added due to a Next
        Hop Client which is co\-resident on the same device
        as the NHS, a row will not be added to this table.
        
        .. attribute:: nhrpservercacheentry
        
        	Additional information kept by a NHS for a relevant Next Hop Resolution Cache entry
        	**type**\: list of :py:class:`NhrpServerCacheEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerCacheTable.NhrpServerCacheEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpservercacheentry = YList()
            self.nhrpservercacheentry.parent = self
            self.nhrpservercacheentry.name = 'nhrpservercacheentry'


        class NhrpServerCacheEntry(object):
            """
            Additional information kept by a NHS for a relevant
            Next Hop Resolution Cache entry.
            
            .. attribute:: ifindex
            
            	
            	**type**\: int
            
            	**range:** 1..2147483647
            
            .. attribute:: nhrpcacheindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpcacheinternetworkaddr
            
            	
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpcacheinternetworkaddrtype
            
            	
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpservercacheauthoritative
            
            	An indication of whether this cache entry is authoritative, which means the entry was added because of a direct registration request with this server or by Server Cache Synchronization Protocol (SCSP) from an authoritative source
            	**type**\: bool
            
            .. attribute:: nhrpservercacheuniqueness
            
            	The Uniqueness indicator for this cache entry used in duplicate address detection. This value cannot be changed after the entry is active
            	**type**\: bool
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.ifindex = None
                self.nhrpcacheindex = None
                self.nhrpcacheinternetworkaddr = None
                self.nhrpcacheinternetworkaddrtype = None
                self.nhrpservercacheauthoritative = None
                self.nhrpservercacheuniqueness = None

            @property
            def _common_path(self):
                if self.ifindex is None:
                    raise YPYDataValidationError('Key property ifindex is None')
                if self.nhrpcacheindex is None:
                    raise YPYDataValidationError('Key property nhrpcacheindex is None')
                if self.nhrpcacheinternetworkaddr is None:
                    raise YPYDataValidationError('Key property nhrpcacheinternetworkaddr is None')
                if self.nhrpcacheinternetworkaddrtype is None:
                    raise YPYDataValidationError('Key property nhrpcacheinternetworkaddrtype is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerCacheTable/NHRP-MIB:nhrpServerCacheEntry[NHRP-MIB:ifIndex = ' + str(self.ifindex) + '][NHRP-MIB:nhrpCacheIndex = ' + str(self.nhrpcacheindex) + '][NHRP-MIB:nhrpCacheInternetworkAddr = ' + str(self.nhrpcacheinternetworkaddr) + '][NHRP-MIB:nhrpCacheInternetworkAddrType = ' + str(self.nhrpcacheinternetworkaddrtype) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.ifindex is not None:
                    return True

                if self.nhrpcacheindex is not None:
                    return True

                if self.nhrpcacheinternetworkaddr is not None:
                    return True

                if self.nhrpcacheinternetworkaddrtype is not None:
                    return True

                if self.nhrpservercacheauthoritative is not None:
                    return True

                if self.nhrpservercacheuniqueness is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpServerCacheTable.NhrpServerCacheEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerCacheTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpservercacheentry is not None:
                for child_ref in self.nhrpservercacheentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpServerCacheTable']['meta_info']


    class NhrpServerNhcTable(object):
        """
        A table of NHCs that are available for use by this NHS
        (Server).
        
        .. attribute:: nhrpservernhcentry
        
        	An NHC that may be used by an NHS
        	**type**\: list of :py:class:`NhrpServerNhcEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerNhcTable.NhrpServerNhcEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpservernhcentry = YList()
            self.nhrpservernhcentry.parent = self
            self.nhrpservernhcentry.name = 'nhrpservernhcentry'


        class NhrpServerNhcEntry(object):
            """
            An NHC that may be used by an NHS.
            
            .. attribute:: nhrpserverindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpservernhcindex
            
            	An identifier for an NHC available to an NHS
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpservernhcinternetworkaddr
            
            	The value of the internetwork layer address of the NHRP Client represented by this entry.  If this value is not known, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpservernhcinternetworkaddrtype
            
            	The type of the internetwork layer address of the NHRP Client represented in this entry. This object indicates how the value of nhrpServerNhcInternetworkAddr is to be interpreted
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpservernhcinuse
            
            	An indication of whether this NHC is in use by the NHS
            	**type**\: bool
            
            .. attribute:: nhrpservernhcnbmaaddr
            
            	The NBMA subnetwork address of the NHC. The type of the address is indicated by the corresponding value of nhrpServerNbmaAddrType
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpservernhcnbmaaddrtype
            
            	The type of the NBMA subnetwork address of the NHRP Client represented by this entry. This object indicates how the values of nhrpServerNhcNbmaAddr and nhrpServerNhcNbmaSubaddr are to be interpreted
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpservernhcnbmasubaddr
            
            	The NBMA subaddress of the NHC. For NMBA address familes that do not have the concept of subaddress, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpservernhcprefixlength
            
            	The number of bits that define the internetwork layer prefix associated with the nhrpServerNhcInternetworkAddr
            	**type**\: int
            
            	**range:** 0..255
            
            .. attribute:: nhrpservernhcrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrpserverindex = None
                self.nhrpservernhcindex = None
                self.nhrpservernhcinternetworkaddr = None
                self.nhrpservernhcinternetworkaddrtype = None
                self.nhrpservernhcinuse = None
                self.nhrpservernhcnbmaaddr = None
                self.nhrpservernhcnbmaaddrtype = None
                self.nhrpservernhcnbmasubaddr = None
                self.nhrpservernhcprefixlength = None
                self.nhrpservernhcrowstatus = None

            @property
            def _common_path(self):
                if self.nhrpserverindex is None:
                    raise YPYDataValidationError('Key property nhrpserverindex is None')
                if self.nhrpservernhcindex is None:
                    raise YPYDataValidationError('Key property nhrpservernhcindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerNhcTable/NHRP-MIB:nhrpServerNhcEntry[NHRP-MIB:nhrpServerIndex = ' + str(self.nhrpserverindex) + '][NHRP-MIB:nhrpServerNhcIndex = ' + str(self.nhrpservernhcindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrpserverindex is not None:
                    return True

                if self.nhrpservernhcindex is not None:
                    return True

                if self.nhrpservernhcinternetworkaddr is not None:
                    return True

                if self.nhrpservernhcinternetworkaddrtype is not None:
                    return True

                if self.nhrpservernhcinuse is not None:
                    return True

                if self.nhrpservernhcnbmaaddr is not None:
                    return True

                if self.nhrpservernhcnbmaaddrtype is not None:
                    return True

                if self.nhrpservernhcnbmasubaddr is not None:
                    return True

                if self.nhrpservernhcprefixlength is not None:
                    return True

                if self.nhrpservernhcrowstatus is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpServerNhcTable.NhrpServerNhcEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerNhcTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpservernhcentry is not None:
                for child_ref in self.nhrpservernhcentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpServerNhcTable']['meta_info']


    class NhrpServerStatTable(object):
        """
        Statistics collected by Next Hop Servers.
        
        .. attribute:: nhrpserverstatentry
        
        	Statistics for a particular NHS. The statistics are broken into received (Rx), transmitted (Tx) and forwarded (Fw).  Forwarded (Fw) would be done by a transit NHS
        	**type**\: list of :py:class:`NhrpServerStatEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerStatTable.NhrpServerStatEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpserverstatentry = YList()
            self.nhrpserverstatentry.parent = self
            self.nhrpserverstatentry.name = 'nhrpserverstatentry'


        class NhrpServerStatEntry(object):
            """
            Statistics for a particular NHS. The statistics are
            broken into received (Rx), transmitted (Tx)
            and forwarded (Fw).  Forwarded (Fw) would be done
            by a transit NHS.
            
            .. attribute:: nhrpserverindex
            
            	
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpserverstatdiscontinuitytime
            
            	The value of sysUpTime on the most recent occasion at which any one or more of this Server's counters suffered a discontinuity.  If no such discontinuities have occurred since the last re\-initialization of the    local management subsystem or the NHRP Server re\-initialization associated with this entry, then this object contains a zero value
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwerrorindication
            
            	The number of NHRP Error Indication packets forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwpurgereply
            
            	The number of NHRP Purge Replies forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwpurgereq
            
            	The number of NHRP Purge Requests forwarded by this server acting as a transit NHS.   Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwregisterreply
            
            	The number of NHRP Registration Replies forwarded by this server acting as a transit NHS. Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwregisterreq
            
            	The number of NHRP Registration Requests forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwresolvereply
            
            	The number of NHRP Resolution Replies forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatfwresolvereq
            
            	The number of NHRP Resolution Requests forwarded by this server acting as a transit NHS.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Authentication Failure'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrinvalidextension
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrinvalidresreplyreceived
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Invalid Resolution Reply Received'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrloopdetected
            
            	The number of NHRP Error Indication packets received by this server with the error code 'NHRP Loop Detected'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrprotoerror
            
            	The number of NHRP Error Indication packets received by this server with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets received by this server with the error code 'NHRP SDU Size Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets received by this server with the error code  'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxpurgereply
            
            	The number of NHRP Purge Replies received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxpurgereq
            
            	The number of NHRP Purge Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxregisterreq
            
            	The number of NHRP Registration Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstatrxresolvereq
            
            	The number of NHRP Resolution Requests received by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrauthenticationfailure
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Authentication Failure'.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrhopcountexceeded
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Hop Count Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrinvalidextension
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code  'Invalid Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrloopdetected
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'NHRP Loop Detected'.     Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrprotoaddrunreachable
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Protocol Address Unreachable'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrprotoerror
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Protocol Error'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrsdusizeexceeded
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'NHRP SDU Size Exceeded'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxerrunrecognizedextension
            
            	The number of NHRP Error Indication packets transmitted by this server with the error code 'Unrecognized Extension'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxpurgereply
            
            	The number of NHRP Purge Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxpurgereq
            
            	The number of NHRP Purge Requests transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisterack
            
            	The number of positively acknowledged NHRP Registration Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisternakalreadyreg
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Unique Internetworking Layer Address Already Registered'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisternakinsufresources
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxregisternakprohibited
            
            	The number of NAKed NHRP Registration Replies transmitted by this server with the code 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplyack
            
            	The number of positively acknowledged NHRP Resolution Replies transmitted by this server.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynakinsufresources
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Insufficient Resources'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynaknobinding
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'No Internetworking Layer Address to NBMA Address Binding Exists'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynaknotunique
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Binding Exists But Is Not Unique'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            .. attribute:: nhrpserverstattxresolvereplynakprohibited
            
            	The number of NAKed NHRP Resolution Replies transmitted by this server with the code 'Administratively Prohibited'.  Discontinuities in the value of this counter can occur at re\-initialization of the management system, at NHRP Server re\-initialization and at other times as indicated by the value of nhrpServerStatDiscontinuityTime
            	**type**\: int
            
            	**range:** 0..4294967295
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrpserverindex = None
                self.nhrpserverstatdiscontinuitytime = None
                self.nhrpserverstatfwerrorindication = None
                self.nhrpserverstatfwpurgereply = None
                self.nhrpserverstatfwpurgereq = None
                self.nhrpserverstatfwregisterreply = None
                self.nhrpserverstatfwregisterreq = None
                self.nhrpserverstatfwresolvereply = None
                self.nhrpserverstatfwresolvereq = None
                self.nhrpserverstatrxerrauthenticationfailure = None
                self.nhrpserverstatrxerrhopcountexceeded = None
                self.nhrpserverstatrxerrinvalidextension = None
                self.nhrpserverstatrxerrinvalidresreplyreceived = None
                self.nhrpserverstatrxerrloopdetected = None
                self.nhrpserverstatrxerrprotoaddrunreachable = None
                self.nhrpserverstatrxerrprotoerror = None
                self.nhrpserverstatrxerrsdusizeexceeded = None
                self.nhrpserverstatrxerrunrecognizedextension = None
                self.nhrpserverstatrxpurgereply = None
                self.nhrpserverstatrxpurgereq = None
                self.nhrpserverstatrxregisterreq = None
                self.nhrpserverstatrxresolvereq = None
                self.nhrpserverstattxerrauthenticationfailure = None
                self.nhrpserverstattxerrhopcountexceeded = None
                self.nhrpserverstattxerrinvalidextension = None
                self.nhrpserverstattxerrloopdetected = None
                self.nhrpserverstattxerrprotoaddrunreachable = None
                self.nhrpserverstattxerrprotoerror = None
                self.nhrpserverstattxerrsdusizeexceeded = None
                self.nhrpserverstattxerrunrecognizedextension = None
                self.nhrpserverstattxpurgereply = None
                self.nhrpserverstattxpurgereq = None
                self.nhrpserverstattxregisterack = None
                self.nhrpserverstattxregisternakalreadyreg = None
                self.nhrpserverstattxregisternakinsufresources = None
                self.nhrpserverstattxregisternakprohibited = None
                self.nhrpserverstattxresolvereplyack = None
                self.nhrpserverstattxresolvereplynakinsufresources = None
                self.nhrpserverstattxresolvereplynaknobinding = None
                self.nhrpserverstattxresolvereplynaknotunique = None
                self.nhrpserverstattxresolvereplynakprohibited = None

            @property
            def _common_path(self):
                if self.nhrpserverindex is None:
                    raise YPYDataValidationError('Key property nhrpserverindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerStatTable/NHRP-MIB:nhrpServerStatEntry[NHRP-MIB:nhrpServerIndex = ' + str(self.nhrpserverindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrpserverindex is not None:
                    return True

                if self.nhrpserverstatdiscontinuitytime is not None:
                    return True

                if self.nhrpserverstatfwerrorindication is not None:
                    return True

                if self.nhrpserverstatfwpurgereply is not None:
                    return True

                if self.nhrpserverstatfwpurgereq is not None:
                    return True

                if self.nhrpserverstatfwregisterreply is not None:
                    return True

                if self.nhrpserverstatfwregisterreq is not None:
                    return True

                if self.nhrpserverstatfwresolvereply is not None:
                    return True

                if self.nhrpserverstatfwresolvereq is not None:
                    return True

                if self.nhrpserverstatrxerrauthenticationfailure is not None:
                    return True

                if self.nhrpserverstatrxerrhopcountexceeded is not None:
                    return True

                if self.nhrpserverstatrxerrinvalidextension is not None:
                    return True

                if self.nhrpserverstatrxerrinvalidresreplyreceived is not None:
                    return True

                if self.nhrpserverstatrxerrloopdetected is not None:
                    return True

                if self.nhrpserverstatrxerrprotoaddrunreachable is not None:
                    return True

                if self.nhrpserverstatrxerrprotoerror is not None:
                    return True

                if self.nhrpserverstatrxerrsdusizeexceeded is not None:
                    return True

                if self.nhrpserverstatrxerrunrecognizedextension is not None:
                    return True

                if self.nhrpserverstatrxpurgereply is not None:
                    return True

                if self.nhrpserverstatrxpurgereq is not None:
                    return True

                if self.nhrpserverstatrxregisterreq is not None:
                    return True

                if self.nhrpserverstatrxresolvereq is not None:
                    return True

                if self.nhrpserverstattxerrauthenticationfailure is not None:
                    return True

                if self.nhrpserverstattxerrhopcountexceeded is not None:
                    return True

                if self.nhrpserverstattxerrinvalidextension is not None:
                    return True

                if self.nhrpserverstattxerrloopdetected is not None:
                    return True

                if self.nhrpserverstattxerrprotoaddrunreachable is not None:
                    return True

                if self.nhrpserverstattxerrprotoerror is not None:
                    return True

                if self.nhrpserverstattxerrsdusizeexceeded is not None:
                    return True

                if self.nhrpserverstattxerrunrecognizedextension is not None:
                    return True

                if self.nhrpserverstattxpurgereply is not None:
                    return True

                if self.nhrpserverstattxpurgereq is not None:
                    return True

                if self.nhrpserverstattxregisterack is not None:
                    return True

                if self.nhrpserverstattxregisternakalreadyreg is not None:
                    return True

                if self.nhrpserverstattxregisternakinsufresources is not None:
                    return True

                if self.nhrpserverstattxregisternakprohibited is not None:
                    return True

                if self.nhrpserverstattxresolvereplyack is not None:
                    return True

                if self.nhrpserverstattxresolvereplynakinsufresources is not None:
                    return True

                if self.nhrpserverstattxresolvereplynaknobinding is not None:
                    return True

                if self.nhrpserverstattxresolvereplynaknotunique is not None:
                    return True

                if self.nhrpserverstattxresolvereplynakprohibited is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpServerStatTable.NhrpServerStatEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerStatTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpserverstatentry is not None:
                for child_ref in self.nhrpserverstatentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpServerStatTable']['meta_info']


    class NhrpServerTable(object):
        """
        This table contains information for a set of NHSes
        associated with this agent.
        
        .. attribute:: nhrpserverentry
        
        	Information about a single NHS
        	**type**\: list of :py:class:`NhrpServerEntry <ydk.models.nhrp.NHRP_MIB.NHRPMIB.NhrpServerTable.NhrpServerEntry>`
        
        

        """

        _prefix = 'nhrp-mib'
        _revision = '1999-08-26'

        def __init__(self):
            self.parent = None
            self.nhrpserverentry = YList()
            self.nhrpserverentry.parent = self
            self.nhrpserverentry.name = 'nhrpserverentry'


        class NhrpServerEntry(object):
            """
            Information about a single NHS.
            
            .. attribute:: nhrpserverindex
            
            	An identifier for the server that is unique within the scope of this agent
            	**type**\: int
            
            	**range:** 1..4294967295
            
            .. attribute:: nhrpserverinternetworkaddr
            
            	The value of the internetwork layer address of this server
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpserverinternetworkaddrtype
            
            	The type of the internetwork layer address of this server. This object is used to interpret the value of nhrpServerInternetworkAddr
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpservernbmaaddr
            
            	The value of the NBMA subnetwork address of this server
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpservernbmaaddrtype
            
            	The type of the NBMA subnetwork address of this server. This object is used to interpret the value of nhrpServerNbmaAddr
            	**type**\: :py:class:`AddressFamilyNumbers_Enum <ydk.models.iana.IANA_ADDRESS_FAMILY_NUMBERS_MIB.AddressFamilyNumbers_Enum>`
            
            .. attribute:: nhrpservernbmasubaddr
            
            	The value of the NBMA subaddress of this server. For NBMA address families without a subaddress concept, this will be a zero\-length OCTET STRING
            	**type**\: str
            
            	**range:** 0..64
            
            .. attribute:: nhrpserverrowstatus
            
            	An object that allows entries in this table to be created and deleted using the RowStatus convention
            	**type**\: :py:class:`RowStatus_Enum <ydk.models.snmpv2.SNMPv2_TC.RowStatus_Enum>`
            
            .. attribute:: nhrpserverstoragetype
            
            	This object defines whether this row is kept in volatile storage and lost upon a Server crash or reboot situation, or if this row is backed up by nonvolatile or permanent storage
            	**type**\: :py:class:`StorageType_Enum <ydk.models.snmpv2.SNMPv2_TC.StorageType_Enum>`
            
            

            """

            _prefix = 'nhrp-mib'
            _revision = '1999-08-26'

            def __init__(self):
                self.parent = None
                self.nhrpserverindex = None
                self.nhrpserverinternetworkaddr = None
                self.nhrpserverinternetworkaddrtype = None
                self.nhrpservernbmaaddr = None
                self.nhrpservernbmaaddrtype = None
                self.nhrpservernbmasubaddr = None
                self.nhrpserverrowstatus = None
                self.nhrpserverstoragetype = None

            @property
            def _common_path(self):
                if self.nhrpserverindex is None:
                    raise YPYDataValidationError('Key property nhrpserverindex is None')

                return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerTable/NHRP-MIB:nhrpServerEntry[NHRP-MIB:nhrpServerIndex = ' + str(self.nhrpserverindex) + ']'

            def is_config(self):
                ''' Returns True if this instance represents config data else returns False '''
                return False

            def _has_data(self):
                if not self.is_config():
                    return False
                if self.is_presence():
                    return True
                if self.nhrpserverindex is not None:
                    return True

                if self.nhrpserverinternetworkaddr is not None:
                    return True

                if self.nhrpserverinternetworkaddrtype is not None:
                    return True

                if self.nhrpservernbmaaddr is not None:
                    return True

                if self.nhrpservernbmaaddrtype is not None:
                    return True

                if self.nhrpservernbmasubaddr is not None:
                    return True

                if self.nhrpserverrowstatus is not None:
                    return True

                if self.nhrpserverstoragetype is not None:
                    return True

                return False

            def is_presence(self):
                ''' Returns True if this instance represents presence container else returns False '''
                return False

            @staticmethod
            def _meta_info():
                from ydk.models.nhrp._meta import _NHRP_MIB as meta
                return meta._meta_table['NHRPMIB.NhrpServerTable.NhrpServerEntry']['meta_info']

        @property
        def _common_path(self):

            return '/NHRP-MIB:NHRP-MIB/NHRP-MIB:nhrpServerTable'

        def is_config(self):
            ''' Returns True if this instance represents config data else returns False '''
            return False

        def _has_data(self):
            if not self.is_config():
                return False
            if self.is_presence():
                return True
            if self.nhrpserverentry is not None:
                for child_ref in self.nhrpserverentry:
                    if child_ref._has_data():
                        return True

            return False

        def is_presence(self):
            ''' Returns True if this instance represents presence container else returns False '''
            return False

        @staticmethod
        def _meta_info():
            from ydk.models.nhrp._meta import _NHRP_MIB as meta
            return meta._meta_table['NHRPMIB.NhrpServerTable']['meta_info']

    @property
    def _common_path(self):

        return '/NHRP-MIB:NHRP-MIB'

    def is_config(self):
        ''' Returns True if this instance represents config data else returns False '''
        return False

    def _has_data(self):
        if not self.is_config():
            return False
        if self.is_presence():
            return True
        if self.nhrpcachetable is not None and self.nhrpcachetable._has_data():
            return True

        if self.nhrpcachetable is not None and self.nhrpcachetable.is_presence():
            return True

        if self.nhrpclientnhstable is not None and self.nhrpclientnhstable._has_data():
            return True

        if self.nhrpclientnhstable is not None and self.nhrpclientnhstable.is_presence():
            return True

        if self.nhrpclientregistrationtable is not None and self.nhrpclientregistrationtable._has_data():
            return True

        if self.nhrpclientregistrationtable is not None and self.nhrpclientregistrationtable.is_presence():
            return True

        if self.nhrpclientstattable is not None and self.nhrpclientstattable._has_data():
            return True

        if self.nhrpclientstattable is not None and self.nhrpclientstattable.is_presence():
            return True

        if self.nhrpclienttable is not None and self.nhrpclienttable._has_data():
            return True

        if self.nhrpclienttable is not None and self.nhrpclienttable.is_presence():
            return True

        if self.nhrpgeneralobjects is not None and self.nhrpgeneralobjects._has_data():
            return True

        if self.nhrpgeneralobjects is not None and self.nhrpgeneralobjects.is_presence():
            return True

        if self.nhrppurgereqtable is not None and self.nhrppurgereqtable._has_data():
            return True

        if self.nhrppurgereqtable is not None and self.nhrppurgereqtable.is_presence():
            return True

        if self.nhrpservercachetable is not None and self.nhrpservercachetable._has_data():
            return True

        if self.nhrpservercachetable is not None and self.nhrpservercachetable.is_presence():
            return True

        if self.nhrpservernhctable is not None and self.nhrpservernhctable._has_data():
            return True

        if self.nhrpservernhctable is not None and self.nhrpservernhctable.is_presence():
            return True

        if self.nhrpserverstattable is not None and self.nhrpserverstattable._has_data():
            return True

        if self.nhrpserverstattable is not None and self.nhrpserverstattable.is_presence():
            return True

        if self.nhrpservertable is not None and self.nhrpservertable._has_data():
            return True

        if self.nhrpservertable is not None and self.nhrpservertable.is_presence():
            return True

        return False

    def is_presence(self):
        ''' Returns True if this instance represents presence container else returns False '''
        return False

    @staticmethod
    def _meta_info():
        from ydk.models.nhrp._meta import _NHRP_MIB as meta
        return meta._meta_table['NHRPMIB']['meta_info']


