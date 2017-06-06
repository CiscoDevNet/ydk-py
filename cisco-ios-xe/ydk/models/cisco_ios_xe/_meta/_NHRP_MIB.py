


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NhrpMib.Nhrpgeneralobjects' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpgeneralobjects',
            False, 
            [
            _MetaInfoClassMember('nhrpNextIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This scalar is used for creating rows in the
                nhrpClientTable and the nhrpServerTable.
                The value of this variable is a currently unused value
                for nhrpClientIndex and nhrpServerIndex.
                
                
                
                
                The value returned when reading this variable must be
                unique for the NHC's and NHS's indices associated with
                this row. Subsequent attempts to read this variable
                must return different values.
                
                NOTE:  this object exists in the General Group because
                it is to be used in establishing rows in the
                nhrpClientTable and the nhrpServerTable.  In other words,
                the value retrieved from this object could become the
                value of nhrpClientIndex and nhprServerIndex.
                
                In the situation of an agent re-initialization the value
                of this object must be saved in non-volatile storage.
                
                This variable will return the special value 0 if no new
                rows can be created.
                ''',
                'nhrpnextindex',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpGeneralObjects',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpcachetable.Nhrpcacheentry.NhrpcachestateEnum' : _MetaInfoEnum('NhrpcachestateEnum', 'ydk.models.cisco_ios_xe.NHRP_MIB',
        {
            'incomplete':'incomplete',
            'ackReply':'ackReply',
            'nakReply':'nakReply',
        }, 'NHRP-MIB', _yang_ns._namespaces['NHRP-MIB']),
    'NhrpMib.Nhrpcachetable.Nhrpcacheentry.NhrpcachetypeEnum' : _MetaInfoEnum('NhrpcachetypeEnum', 'ydk.models.cisco_ios_xe.NHRP_MIB',
        {
            'other':'other',
            'register':'register',
            'resolveAuthoritative':'resolveAuthoritative',
            'resoveNonauthoritative':'resoveNonauthoritative',
            'transit':'transit',
            'administrativelyAdded':'administrativelyAdded',
            'atmarp':'atmarp',
            'scsp':'scsp',
        }, 'NHRP-MIB', _yang_ns._namespaces['NHRP-MIB']),
    'NhrpMib.Nhrpcachetable.Nhrpcacheentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpcachetable.Nhrpcacheentry',
            False, 
            [
            _MetaInfoClassMember('nhrpCacheInternetworkAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The internetwork layer address type of this Next Hop
                Resolution Cache entry. The value of this object indicates
                how to interpret the values of nhrpCacheInternetworkAddr
                and nhrpCacheNextHopInternetworkAddr.
                ''',
                'nhrpcacheinternetworkaddrtype',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpCacheInternetworkAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the internetwork address of the
                destination.
                ''',
                'nhrpcacheinternetworkaddr',
                'NHRP-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpCacheIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An identifier for this entry that has local
                significance within the scope of the General
                Group.  This identifier is used here to
                uniquely identify this row, and also used
                in the 'nhrpPurgeTable' for the value of
                the 'nhrpPurgeCacheIdentifier'.
                ''',
                'nhrpcacheindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpCacheHoldingTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If the value of 'nhrpCacheHoldingTimeValid is
                true(1) then this object represents the number
                of seconds that the cache entry will remain in this
                table.  When this value reaches 0 (zero) the row should
                be deleted.
                
                If the value of 'nhrpCacheHoldingTimeValid is
                false(2) then this object is undefined.
                ''',
                'nhrpcacheholdingtime',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheHoldingTimeValid', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                True(1) is returned if the value of
                'nhrpCacheType' is not
                'administrativelyAdded'.  Since the
                value of 'nhrpCacheType' was not
                configured by a user, the value of
                'nhrpCacheHoldingTime' is
                considered valid.  In other words, the value of
                'nhrpCacheHoldingTime' represents
                the Holding Time for the cache Entry.
                
                If 'nhrpCacheType has been configured by a
                user, (i.e. the value of 'nhrpCacheType' is
                'administrativelyAdded') then false(2) will be returned.
                This indicates that the value of
                'nhrpCacheHoldingTime' is undefined because this row
                could possibly be backed up in nonvolatile storage.
                ''',
                'nhrpcacheholdingtimevalid',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheNbmaAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the NBMA subnetwork address of the next
                hop.
                ''',
                'nhrpcachenbmaaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheNbmaAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The NBMA address type. The value of this
                object indicates how to interpret
                the values of nhrpCacheNbmaAddr and
                nhrpCacheNbmaSubaddr.
                ''',
                'nhrpcachenbmaaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheNbmaSubaddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the NBMA subaddress of the next hop. If
                there is no subaddress concept for the NBMA address
                family, this value will be a zero-length OCTET STRING.
                ''',
                'nhrpcachenbmasubaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheNegotiatedMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The maximum transmission unit (MTU) that was negotiated
                or registered for this entity. In other words, this is the
                actual MTU being used.
                ''',
                'nhrpcachenegotiatedmtu',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheNextHopInternetworkAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the internetwork address of the next hop.
                ''',
                'nhrpcachenexthopinternetworkaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCachePreference', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                An object which reflects the Preference value of the
                Client Information Entry (CIE).
                
                Zero or more Client Information Entries (CIEs) may be
                included in the NHRP Packet.  One of the fields in the
                CIE is the Preference.  For a complete description of
                the CIE, refer to Section 5.2.0.1 of  RFC 2332 [17].
                ''',
                'nhrpcachepreference',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCachePrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The number of bits that define the internetwork layer
                prefix associated with the nhrpCacheInternetworkAddr.
                ''',
                'nhrpcacheprefixlength',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                An object that allows entries in this table to be
                created and deleted using the RowStatus convention.
                ''',
                'nhrpcacherowstatus',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheState', REFERENCE_ENUM_CLASS, 'NhrpcachestateEnum' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpcachetable.Nhrpcacheentry.NhrpcachestateEnum', 
                [], [], 
                '''                An indication of the state of this entry. The values are:
                
                'incomplete(1)' The client has sent a NHRP Resolution
                                Request but has not yet received the
                                NHRP Resolution Reply.
                
                
                'ackReply(2)'   For a client or server, this is a
                                cached valid mapping.
                
                'nakReply(3)'   For a client or server, this is a
                                cached NAK mapping.
                ''',
                'nhrpcachestate',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This value only has meaning when the 'nhrpCacheType'
                has the value of 'administrativelyAdded'.
                
                When the row is created due to being
                'administrativelyAdded', this object reflects whether
                this row is kept in volatile storage
                and lost upon reboot or if this row is backed up by
                non-volatile or permanent storage.
                
                If the value of 'nhrpCacheType' has a value which
                is not 'administrativelyAdded, then the value of this
                object is 'other(1)'.
                ''',
                'nhrpcachestoragetype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpCacheType', REFERENCE_ENUM_CLASS, 'NhrpcachetypeEnum' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpcachetable.Nhrpcacheentry.NhrpcachetypeEnum', 
                [], [], 
                '''                An indication of how this cache entry
                was created. The values are:
                
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
                ''',
                'nhrpcachetype',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpCacheEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpcachetable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpcachetable',
            False, 
            [
            _MetaInfoClassMember('nhrpCacheEntry', REFERENCE_LIST, 'Nhrpcacheentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpcachetable.Nhrpcacheentry', 
                [], [], 
                '''                A cached mapping between an internetwork layer address
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
                ''',
                'nhrpcacheentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpCacheTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry',
            False, 
            [
            _MetaInfoClassMember('nhrpPurgeIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An index for this entry that has local significance
                within the scope of this table.
                ''',
                'nhrppurgeindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpPurgeCacheIdentifier', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                This object identifies which row in
                'nhrpCacheTable' is being purged.  This object
                should have the same value as the 'nhrpCacheIndex'
                in the 'nhrpCacheTable'.
                ''',
                'nhrppurgecacheidentifier',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpPurgePrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                In the case of NHRP Purge Requests, this specifies the
                equivalence class of addresses which match the first
                'Prefix Length' bit positions of the Client Protocol
                Address specified in the Client Information Entry (CIE).
                ''',
                'nhrppurgeprefixlength',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpPurgeReplyExpected', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether this Purge Request has the
                'N' Bit cleared (off).
                ''',
                'nhrppurgereplyexpected',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpPurgeRequestID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Request ID used in the purge request.
                ''',
                'nhrppurgerequestid',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpPurgeRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                An object that allows entries in this table to be
                created and deleted using the RowStatus convention.
                ''',
                'nhrppurgerowstatus',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpPurgeReqEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrppurgereqtable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrppurgereqtable',
            False, 
            [
            _MetaInfoClassMember('nhrpPurgeReqEntry', REFERENCE_LIST, 'Nhrppurgereqentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry', 
                [], [], 
                '''                Information regarding a Purge Request.
                ''',
                'nhrppurgereqentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpPurgeReqTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclienttable.Nhrpcliententry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclienttable.Nhrpcliententry',
            False, 
            [
            _MetaInfoClassMember('nhrpClientIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An identifier for the NHRP client that is unique within
                the scope of this agent.  The 'nhrpNextIndex' value
                should be consulted (read), prior to creating a row in
                this table, and the value returned from reading
                'nhrpNextIndex' should be used as this object's value.
                ''',
                'nhrpclientindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpClientDefaultMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The default maximum transmission unit (MTU) of the
                LIS/LAG which this client should use. This object
                will be initialized by the agent to the default MTU
                of the LIS/LAG (which is 9180) unless a different MTU
                value is specified during creation of this Client.
                ''',
                'nhrpclientdefaultmtu',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientHoldTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The hold time the client will register.
                ''',
                'nhrpclientholdtime',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientInitialRequestTimeout', ATTRIBUTE, 'int' , None, None, 
                [('1', '900')], [], 
                '''                The number of seconds that the client will wait before
                timing out an NHRP initial request.  This object only has
                meaning for the initial timeout period.
                ''',
                'nhrpclientinitialrequesttimeout',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientInternetworkAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the internetwork layer address of this
                client.
                ''',
                'nhrpclientinternetworkaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientInternetworkAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the internetwork layer address of this
                client. This object indicates how the value of
                nhrpClientInternetworkAddr is to be interpreted.
                ''',
                'nhrpclientinternetworkaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNbmaAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The NBMA subnetwork address of this client.
                ''',
                'nhrpclientnbmaaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNbmaAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the NBMA subnetwork address of this client.
                This object indicates how the values of
                nhrpClientNbmaAddr and nhrpClientNbmaSubaddr are to be
                interpreted.
                ''',
                'nhrpclientnbmaaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNbmaSubaddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The NBMA subaddress of this client. For NBMA address
                families without a subaddress concept, this will be a
                zero-length OCTET STRING.
                ''',
                'nhrpclientnbmasubaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientPurgeRequestRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of times the client will retry a purge request
                before failure. A value of 0 means don't retry. A value of
                65535 means retry forever.
                ''',
                'nhrpclientpurgerequestretries',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientRegistrationRequestRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of times the client will retry the
                registration request before failure. A value of
                0 means don't retry. A value of 65535 means
                retry forever.
                ''',
                'nhrpclientregistrationrequestretries',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientRequestID', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The Request ID used to register this client with its
                server. According to Section 5.2.3 of the NHRP
                Specification, RFC 2332 [17], the Request ID must
                be kept in non-volatile storage, so that if an NHC
                crashes and  re-initializes, it will use a different
                
                Request ID during the registration process
                when reregistering with the same NHS.
                ''',
                'nhrpclientrequestid',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientResolutionRequestRetries', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The number of times the client will retry the resolution
                request before failure. A value of 0 means don't retry.
                A value of 65535 means retry forever.
                ''',
                'nhrpclientresolutionrequestretries',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                An object that allows entries in this table to be
                created and deleted using the RowStatus convention.
                ''',
                'nhrpclientrowstatus',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This object defines whether this row is kept in
                volatile storage and lost upon a Client crash or
                reboot situation, or if this row is backed up by
                nonvolatile or permanent storage.
                ''',
                'nhrpclientstoragetype',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclienttable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclienttable',
            False, 
            [
            _MetaInfoClassMember('nhrpClientEntry', REFERENCE_LIST, 'Nhrpcliententry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclienttable.Nhrpcliententry', 
                [], [], 
                '''                Information about a single NHC.
                ''',
                'nhrpcliententry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry.NhrpclientregstateEnum' : _MetaInfoEnum('NhrpclientregstateEnum', 'ydk.models.cisco_ios_xe.NHRP_MIB',
        {
            'other':'other',
            'registering':'registering',
            'ackRegisterReply':'ackRegisterReply',
            'nakRegisterReply':'nakRegisterReply',
        }, 'NHRP-MIB', _yang_ns._namespaces['NHRP-MIB']),
    'NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry.NhrpclientreguniquenessEnum' : _MetaInfoEnum('NhrpclientreguniquenessEnum', 'ydk.models.cisco_ios_xe.NHRP_MIB',
        {
            'requestUnique':'requestUnique',
            'requestNotUnique':'requestNotUnique',
        }, 'NHRP-MIB', _yang_ns._namespaces['NHRP-MIB']),
    'NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry',
            False, 
            [
            _MetaInfoClassMember('nhrpClientIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'nhrpclientindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpClientRegIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An identifier for this entry such that it
                identifies a specific Registration Request from
                the NHC represented by the nhrpClientIndex.
                ''',
                'nhrpclientregindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpClientRegRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                An object that allows entries in this table to be
                created and deleted using the RowStatus convention.
                ''',
                'nhrpclientregrowstatus',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientRegState', REFERENCE_ENUM_CLASS, 'NhrpclientregstateEnum' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry.NhrpclientregstateEnum', 
                [], [], 
                '''                The registration state of this client. The values are:
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
                ''',
                'nhrpclientregstate',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientRegUniqueness', REFERENCE_ENUM_CLASS, 'NhrpclientreguniquenessEnum' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry.NhrpclientreguniquenessEnum', 
                [], [], 
                '''                The Uniqueness indicator for this Registration Request.
                If this object has the value of requestUnique(1), then
                the Uniqueness bit is set in the the NHRP Registration
                Request represented by this row.  The value cannot
                be changed once the row is created.
                ''',
                'nhrpclientreguniqueness',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientRegistrationEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclientregistrationtable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclientregistrationtable',
            False, 
            [
            _MetaInfoClassMember('nhrpClientRegistrationEntry', REFERENCE_LIST, 'Nhrpclientregistrationentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry', 
                [], [], 
                '''                An NHC needs to maintain registration request information
                between the NHC and the NHS.  An entry in this table
                represents information for a single registration request.
                ''',
                'nhrpclientregistrationentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientRegistrationTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry',
            False, 
            [
            _MetaInfoClassMember('nhrpClientIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'nhrpclientindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpClientNhsIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An identifier for an NHS available to an NHC.
                ''',
                'nhrpclientnhsindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpClientNhsInternetworkAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the destination internetwork layer
                address of the NHRP server represented by this
                
                
                
                entry.  If this value is not known, this will be
                a zero-length OCTET STRING.
                ''',
                'nhrpclientnhsinternetworkaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNhsInternetworkAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the internetwork layer address of the
                NHRP server represented in this entry. This object
                indicates how the value of
                nhrpClientNhsInternetworkAddr is to be interpreted.
                ''',
                'nhrpclientnhsinternetworkaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNhsInUse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether this NHS is in use by the NHC.
                ''',
                'nhrpclientnhsinuse',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNhsNbmaAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The NBMA subnetwork address of the NHS. The type of
                the address is indicated by the corresponding value of
                nhrpClientNhsNbmaAddrType.
                ''',
                'nhrpclientnhsnbmaaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNhsNbmaAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the NBMA subnetwork address of the NHRP
                Server represented by this entry. This object indicates
                how the values of nhrpClientNhsNbmaAddr and
                nhrpClientNhsNbmaSubaddr are to be interpreted.
                ''',
                'nhrpclientnhsnbmaaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNhsNbmaSubaddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The NBMA subaddress of the NHS. For NMBA address
                families that do not have the concept of subaddress,
                     this will be a zero-length OCTET STRING.
                ''',
                'nhrpclientnhsnbmasubaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNhsRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                An object that allows entries in this table to be
                created and deleted using the RowStatus convention.
                ''',
                'nhrpclientnhsrowstatus',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientNhsEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclientnhstable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclientnhstable',
            False, 
            [
            _MetaInfoClassMember('nhrpClientNhsEntry', REFERENCE_LIST, 'Nhrpclientnhsentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry', 
                [], [], 
                '''                An NHS that may be used by an NHC.
                ''',
                'nhrpclientnhsentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientNhsTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclientstattable.Nhrpclientstatentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclientstattable.Nhrpclientstatentry',
            False, 
            [
            _MetaInfoClassMember('nhrpClientIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'nhrpclientindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpClientStatDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at
                which any one or more of this Client's counters
                suffered a discontinuity.  If no such discontinuities
                have occurred since the last re-initialization of the
                local management subsystem or the NHRP Client
                re-initialization associated with this entry, then
                this object contains a zero value.
                ''',
                'nhrpclientstatdiscontinuitytime',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrAuthenticationFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code 'Authentication
                Failure'.
                
                
                
                
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrauthenticationfailure',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrHopCountExceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code 'Hop Count Exceeded'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrhopcountexceeded',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrInvalidExtension', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code 'Invalid Extension'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrinvalidextension',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrLoopDetected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code 'NHRP Loop Detected'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrloopdetected',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrProtoAddrUnreachable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code 'Protocol Address
                Unreachable'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrprotoaddrunreachable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrProtoError', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code 'Protocol Error'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrprotoerror',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrSduSizeExceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code 'NHRP SDU Size
                
                Exceeded'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrsdusizeexceeded',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxErrUnrecognizedExtension', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this client with the error code
                'Unrecognized Extension'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxerrunrecognizedextension',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxPurgeReply', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Replies received by this
                client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxpurgereply',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxPurgeReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Requests received by this
                client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxpurgereq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxRegisterAck', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of positively acknowledged NHRP Registration
                Replies received by this client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxregisterack',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxRegisterNakAlreadyReg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Registration Replies received
                by this client that contained the code indicating 'Unique
                Internetworking Layer Address Already Registered'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxregisternakalreadyreg',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxRegisterNakInsufResources', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Registration Replies received
                by this client that contained the code indicating
                'Insufficient Resources'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxregisternakinsufresources',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxRegisterNakProhibited', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Registration Replies received
                by this client that contained the code indicating
                'Administratively Prohibited'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxregisternakprohibited',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxResolveReplyAck', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of positively acknowledged NHRP Resolution
                Replies received by this client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxresolvereplyack',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxResolveReplyNakInsufResources', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies received
                by this client that contained the code indicating
                'Insufficient Resources'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxresolvereplynakinsufresources',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxResolveReplyNakNoBinding', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies received
                by this client that contained the code indicating
                'No Internetworking Layer Address to NBMA Address
                Binding Exists'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxresolvereplynaknobinding',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxResolveReplyNakNotUnique', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies received
                by this client that contained the code indicating
                'Binding Exists But Is Not Unique'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxresolvereplynaknotunique',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatRxResolveReplyNakProhibited', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies received
                by this client that contained the code indicating
                'Administratively Prohibited'.
                
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstatrxresolvereplynakprohibited',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatTxErrorIndication', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets transmitted
                by this client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstattxerrorindication',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatTxPurgeReply', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Replies transmitted by this
                client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstattxpurgereply',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatTxPurgeReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Requests transmitted by this
                client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstattxpurgereq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatTxRegisterReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Registration Requests transmitted
                by this client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstattxregisterreq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatTxResolveReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Resolution Requests transmitted
                by this client.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Client re-initialization and at
                other times as indicated by the value of
                nhrpClientStatDiscontinuityTime.
                ''',
                'nhrpclientstattxresolvereq',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientStatEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpclientstattable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpclientstattable',
            False, 
            [
            _MetaInfoClassMember('nhrpClientStatEntry', REFERENCE_LIST, 'Nhrpclientstatentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientstattable.Nhrpclientstatentry', 
                [], [], 
                '''                Statistics collected by a NHRP client.
                ''',
                'nhrpclientstatentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpClientStatTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpservertable.Nhrpserverentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpservertable.Nhrpserverentry',
            False, 
            [
            _MetaInfoClassMember('nhrpServerIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An identifier for the server that is unique within the
                scope of this agent.
                ''',
                'nhrpserverindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpServerInternetworkAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the internetwork layer address of this
                server.
                ''',
                'nhrpserverinternetworkaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerInternetworkAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the internetwork layer address of this
                server. This object is used to interpret the value of
                nhrpServerInternetworkAddr.
                ''',
                'nhrpserverinternetworkaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNbmaAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the NBMA subnetwork address of this
                server.
                ''',
                'nhrpservernbmaaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNbmaAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the NBMA subnetwork address of this server.
                This object is used to interpret the value of
                nhrpServerNbmaAddr.
                ''',
                'nhrpservernbmaaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNbmaSubaddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the NBMA subaddress of this server.
                For NBMA address families without a subaddress
                concept, this will be a zero-length OCTET STRING.
                ''',
                'nhrpservernbmasubaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                An object that allows entries in this table to be
                created and deleted using the RowStatus convention.
                ''',
                'nhrpserverrowstatus',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStorageType', REFERENCE_ENUM_CLASS, 'StoragetypeEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'StoragetypeEnum', 
                [], [], 
                '''                This object defines whether this row is kept in
                volatile storage and lost upon a Server crash or
                reboot situation, or if this row is backed up by
                nonvolatile or permanent storage.
                ''',
                'nhrpserverstoragetype',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpservertable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpservertable',
            False, 
            [
            _MetaInfoClassMember('nhrpServerEntry', REFERENCE_LIST, 'Nhrpserverentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpservertable.Nhrpserverentry', 
                [], [], 
                '''                Information about a single NHS.
                ''',
                'nhrpserverentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpservercachetable.Nhrpservercacheentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpservercachetable.Nhrpservercacheentry',
            False, 
            [
            _MetaInfoClassMember('nhrpCacheInternetworkAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                ''',
                'nhrpcacheinternetworkaddrtype',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpCacheInternetworkAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                ''',
                'nhrpcacheinternetworkaddr',
                'NHRP-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpCacheIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'nhrpcacheindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpServerCacheAuthoritative', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether this cache entry is
                authoritative, which means the entry was added because
                of a direct registration request with this server or
                by Server Cache Synchronization Protocol (SCSP) from
                an authoritative source.
                ''',
                'nhrpservercacheauthoritative',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerCacheUniqueness', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The Uniqueness indicator for this cache
                entry used in duplicate address detection. This value
                cannot be changed after the entry is active.
                ''',
                'nhrpservercacheuniqueness',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerCacheEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpservercachetable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpservercachetable',
            False, 
            [
            _MetaInfoClassMember('nhrpServerCacheEntry', REFERENCE_LIST, 'Nhrpservercacheentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpservercachetable.Nhrpservercacheentry', 
                [], [], 
                '''                Additional information kept by a NHS for a relevant
                Next Hop Resolution Cache entry.
                ''',
                'nhrpservercacheentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerCacheTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpservernhctable.Nhrpservernhcentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpservernhctable.Nhrpservernhcentry',
            False, 
            [
            _MetaInfoClassMember('nhrpServerIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'nhrpserverindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpServerNhcIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                An identifier for an NHC available to an NHS.
                ''',
                'nhrpservernhcindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpServerNhcInternetworkAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The value of the internetwork layer address of
                the NHRP Client represented by this entry.  If this
                value is not known, this will be a zero-length
                OCTET STRING.
                ''',
                'nhrpservernhcinternetworkaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcInternetworkAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the internetwork layer address of the
                NHRP Client represented in this entry. This object
                indicates how the value of nhrpServerNhcInternetworkAddr
                is to be interpreted.
                ''',
                'nhrpservernhcinternetworkaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcInUse', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                An indication of whether this NHC is in use by the NHS.
                ''',
                'nhrpservernhcinuse',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcNbmaAddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The NBMA subnetwork address of the NHC. The type of the
                address is indicated by the corresponding value of
                nhrpServerNbmaAddrType.
                ''',
                'nhrpservernhcnbmaaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcNbmaAddrType', REFERENCE_ENUM_CLASS, 'AddressfamilynumbersEnum' , 'ydk.models.cisco_ios_xe.IANA_ADDRESS_FAMILY_NUMBERS_MIB', 'AddressfamilynumbersEnum', 
                [], [], 
                '''                The type of the NBMA subnetwork address of the NHRP
                Client represented by this entry. This object indicates
                how the values of nhrpServerNhcNbmaAddr and
                nhrpServerNhcNbmaSubaddr are to be interpreted.
                ''',
                'nhrpservernhcnbmaaddrtype',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcNbmaSubaddr', ATTRIBUTE, 'str' , None, None, 
                [(0, 64)], [], 
                '''                The NBMA subaddress of the NHC. For NMBA address familes
                that do not have the concept of subaddress, this will
                be a zero-length OCTET STRING.
                ''',
                'nhrpservernhcnbmasubaddr',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcPrefixLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The number of bits that define the internetwork
                layer prefix associated with the
                nhrpServerNhcInternetworkAddr.
                ''',
                'nhrpservernhcprefixlength',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                An object that allows entries in this table to be
                created and deleted using the RowStatus convention.
                ''',
                'nhrpservernhcrowstatus',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerNhcEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpservernhctable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpservernhctable',
            False, 
            [
            _MetaInfoClassMember('nhrpServerNhcEntry', REFERENCE_LIST, 'Nhrpservernhcentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpservernhctable.Nhrpservernhcentry', 
                [], [], 
                '''                An NHC that may be used by an NHS.
                ''',
                'nhrpservernhcentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerNhcTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpserverstattable.Nhrpserverstatentry' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpserverstattable.Nhrpserverstatentry',
            False, 
            [
            _MetaInfoClassMember('nhrpServerIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                ''',
                'nhrpserverindex',
                'NHRP-MIB', True),
            _MetaInfoClassMember('nhrpServerStatDiscontinuityTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime on the most recent occasion at
                which any one or more of this Server's counters
                suffered a discontinuity.  If no such discontinuities
                have occurred since the last re-initialization of the
                
                
                
                local management subsystem or the NHRP Server
                re-initialization associated with this entry, then
                this object contains a zero value.
                ''',
                'nhrpserverstatdiscontinuitytime',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatFwErrorIndication', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets forwarded
                by this server acting as a transit NHS.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatfwerrorindication',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatFwPurgeReply', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Replies forwarded by this
                server acting as a transit NHS.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatfwpurgereply',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatFwPurgeReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Requests forwarded
                by this server acting as a transit NHS.
                
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatfwpurgereq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatFwRegisterReply', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Registration Replies forwarded
                by this server acting as a transit NHS.
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatfwregisterreply',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatFwRegisterReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Registration Requests forwarded
                by this server acting as a transit NHS.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatfwregisterreq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatFwResolveReply', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Resolution Replies forwarded
                by this server acting as a transit NHS.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatfwresolvereply',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatFwResolveReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Resolution Requests
                forwarded by this server acting as a transit NHS.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatfwresolvereq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrAuthenticationFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                received by this server with the error code
                'Authentication Failure'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrauthenticationfailure',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrHopCountExceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                received by this server with the error code
                'Hop Count Exceeded'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrhopcountexceeded',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrInvalidExtension', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this server with the error code 'Invalid Extension'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrinvalidextension',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrInvalidResReplyReceived', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this server with the error code 'Invalid Resolution
                Reply Received'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrinvalidresreplyreceived',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrLoopDetected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this server with the error code 'NHRP Loop Detected'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrloopdetected',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrProtoAddrUnreachable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this server with the error code 'Protocol Address
                Unreachable'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrprotoaddrunreachable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrProtoError', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this server with the error code 'Protocol Error'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrprotoerror',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrSduSizeExceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this server with the error code 'NHRP SDU Size
                Exceeded'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrsdusizeexceeded',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxErrUnrecognizedExtension', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets received
                by this server with the error code
                
                'Unrecognized Extension'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxerrunrecognizedextension',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxPurgeReply', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Replies received by this
                server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxpurgereply',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxPurgeReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Requests received by
                this server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxpurgereq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxRegisterReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Registration Requests received
                by this server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxregisterreq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatRxResolveReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Resolution Requests received by this
                server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstatrxresolvereq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrAuthenticationFailure', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error code
                'Authentication Failure'.
                
                
                
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrauthenticationfailure',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrHopCountExceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error
                code 'Hop Count Exceeded'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrhopcountexceeded',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrInvalidExtension', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error code
                
                'Invalid Extension'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrinvalidextension',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrLoopDetected', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error code
                'NHRP Loop Detected'.
                
                
                
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrloopdetected',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrProtoAddrUnreachable', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error code
                'Protocol Address Unreachable'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrprotoaddrunreachable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrProtoError', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error
                code 'Protocol Error'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrprotoerror',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrSduSizeExceeded', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error code
                'NHRP SDU Size Exceeded'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrsdusizeexceeded',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxErrUnrecognizedExtension', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Error Indication packets
                transmitted by this server with the error code
                'Unrecognized Extension'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxerrunrecognizedextension',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxPurgeReply', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Replies transmitted by
                this server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxpurgereply',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxPurgeReq', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NHRP Purge Requests transmitted by this
                server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxpurgereq',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxRegisterAck', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of positively acknowledged NHRP Registration
                Replies transmitted by this server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxregisterack',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxRegisterNakAlreadyReg', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Registration Replies
                transmitted by this server with the code
                'Unique Internetworking Layer Address Already
                Registered'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxregisternakalreadyreg',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxRegisterNakInsufResources', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Registration Replies
                transmitted by this server with the code
                'Insufficient Resources'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxregisternakinsufresources',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxRegisterNakProhibited', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Registration Replies
                transmitted by this server with the code
                'Administratively Prohibited'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxregisternakprohibited',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxResolveReplyAck', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of positively acknowledged NHRP
                Resolution Replies transmitted by this server.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxresolvereplyack',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxResolveReplyNakInsufResources', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies
                transmitted by this server with the code
                'Insufficient Resources'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxresolvereplynakinsufresources',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxResolveReplyNakNoBinding', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies
                transmitted by this server with the code
                'No Internetworking Layer Address to NBMA
                Address Binding Exists'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxresolvereplynaknobinding',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxResolveReplyNakNotUnique', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies
                transmitted by this server with the code
                'Binding Exists But Is Not Unique'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxresolvereplynaknotunique',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTxResolveReplyNakProhibited', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of NAKed NHRP Resolution Replies
                transmitted by this server with the code
                'Administratively Prohibited'.
                
                Discontinuities in the value of this counter can occur
                at re-initialization of the management system, at
                NHRP Server re-initialization and at
                other times as indicated by the value of
                nhrpServerStatDiscontinuityTime.
                ''',
                'nhrpserverstattxresolvereplynakprohibited',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerStatEntry',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib.Nhrpserverstattable' : {
        'meta_info' : _MetaInfoClass('NhrpMib.Nhrpserverstattable',
            False, 
            [
            _MetaInfoClassMember('nhrpServerStatEntry', REFERENCE_LIST, 'Nhrpserverstatentry' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpserverstattable.Nhrpserverstatentry', 
                [], [], 
                '''                Statistics for a particular NHS. The statistics are
                broken into received (Rx), transmitted (Tx)
                and forwarded (Fw).  Forwarded (Fw) would be done
                by a transit NHS.
                ''',
                'nhrpserverstatentry',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'nhrpServerStatTable',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
    'NhrpMib' : {
        'meta_info' : _MetaInfoClass('NhrpMib',
            False, 
            [
            _MetaInfoClassMember('nhrpCacheTable', REFERENCE_CLASS, 'Nhrpcachetable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpcachetable', 
                [], [], 
                '''                This table contains mappings between internetwork layer
                addresses and NBMA subnetwork layer addresses.
                ''',
                'nhrpcachetable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientNhsTable', REFERENCE_CLASS, 'Nhrpclientnhstable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientnhstable', 
                [], [], 
                '''                A table of NHSes that are available for use by this NHC
                (client). By default, the agent will add an entry to this
                table that corresponds to the client's default router.
                ''',
                'nhrpclientnhstable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientRegistrationTable', REFERENCE_CLASS, 'Nhrpclientregistrationtable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientregistrationtable', 
                [], [], 
                '''                A table of Registration Request Information that
                needs to be maintained by the NHCs (clients).
                ''',
                'nhrpclientregistrationtable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientStatTable', REFERENCE_CLASS, 'Nhrpclientstattable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclientstattable', 
                [], [], 
                '''                This table contains statistics collected by NHRP
                clients.
                ''',
                'nhrpclientstattable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpClientTable', REFERENCE_CLASS, 'Nhrpclienttable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpclienttable', 
                [], [], 
                '''                Information about NHRP clients (NHCs) managed by this
                agent.
                ''',
                'nhrpclienttable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpGeneralObjects', REFERENCE_CLASS, 'Nhrpgeneralobjects' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpgeneralobjects', 
                [], [], 
                '''                ''',
                'nhrpgeneralobjects',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpPurgeReqTable', REFERENCE_CLASS, 'Nhrppurgereqtable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrppurgereqtable', 
                [], [], 
                '''                This table will track Purge Request Information.
                ''',
                'nhrppurgereqtable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerCacheTable', REFERENCE_CLASS, 'Nhrpservercachetable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpservercachetable', 
                [], [], 
                '''                This table extends the nhrpCacheTable for
                NHSes.  If the nhrpCacheTable has a row added due to
                an NHS or based on information regarding an NHS then
                a row is also added in this table.
                
                The rows in this table will be created when rows in
                the nhrpCacheTable are created.  However, there may
                be rows created in the nhrpCacheTable which do not
                have corresponding rows in this table.  For example,
                if the nhrpCacheTable has a row added due to a Next
                Hop Client which is co-resident on the same device
                as the NHS, a row will not be added to this table.
                ''',
                'nhrpservercachetable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerNhcTable', REFERENCE_CLASS, 'Nhrpservernhctable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpservernhctable', 
                [], [], 
                '''                A table of NHCs that are available for use by this NHS
                (Server).
                ''',
                'nhrpservernhctable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerStatTable', REFERENCE_CLASS, 'Nhrpserverstattable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpserverstattable', 
                [], [], 
                '''                Statistics collected by Next Hop Servers.
                ''',
                'nhrpserverstattable',
                'NHRP-MIB', False),
            _MetaInfoClassMember('nhrpServerTable', REFERENCE_CLASS, 'Nhrpservertable' , 'ydk.models.cisco_ios_xe.NHRP_MIB', 'NhrpMib.Nhrpservertable', 
                [], [], 
                '''                This table contains information for a set of NHSes
                associated with this agent.
                ''',
                'nhrpservertable',
                'NHRP-MIB', False),
            ],
            'NHRP-MIB',
            'NHRP-MIB',
            _yang_ns._namespaces['NHRP-MIB'],
        'ydk.models.cisco_ios_xe.NHRP_MIB'
        ),
    },
}
_meta_table['NhrpMib.Nhrpcachetable.Nhrpcacheentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpcachetable']['meta_info']
_meta_table['NhrpMib.Nhrppurgereqtable.Nhrppurgereqentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrppurgereqtable']['meta_info']
_meta_table['NhrpMib.Nhrpclienttable.Nhrpcliententry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpclienttable']['meta_info']
_meta_table['NhrpMib.Nhrpclientregistrationtable.Nhrpclientregistrationentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpclientregistrationtable']['meta_info']
_meta_table['NhrpMib.Nhrpclientnhstable.Nhrpclientnhsentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpclientnhstable']['meta_info']
_meta_table['NhrpMib.Nhrpclientstattable.Nhrpclientstatentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpclientstattable']['meta_info']
_meta_table['NhrpMib.Nhrpservertable.Nhrpserverentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpservertable']['meta_info']
_meta_table['NhrpMib.Nhrpservercachetable.Nhrpservercacheentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpservercachetable']['meta_info']
_meta_table['NhrpMib.Nhrpservernhctable.Nhrpservernhcentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpservernhctable']['meta_info']
_meta_table['NhrpMib.Nhrpserverstattable.Nhrpserverstatentry']['meta_info'].parent =_meta_table['NhrpMib.Nhrpserverstattable']['meta_info']
_meta_table['NhrpMib.Nhrpgeneralobjects']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpcachetable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrppurgereqtable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpclienttable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpclientregistrationtable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpclientnhstable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpclientstattable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpservertable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpservercachetable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpservernhctable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
_meta_table['NhrpMib.Nhrpserverstattable']['meta_info'].parent =_meta_table['NhrpMib']['meta_info']
