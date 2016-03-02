


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'RMON2MIB.AddressMap' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AddressMap',
            False, 
            [
            _MetaInfoClassMember('addressMapDeletes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an address mapping entry has been
                deleted from the addressMapTable (for any reason).  If
                an entry is deleted, then inserted, and then deleted, this
                counter will be incremented by 2.
                
                Note that the table size can be determined by subtracting
                addressMapDeletes from addressMapInserts.
                ''',
                'addressmapdeletes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapInserts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an address mapping entry has been
                inserted into the addressMapTable.  If an entry is inserted,
                then deleted, and then inserted, this counter will be
                incremented by 2.
                
                Note that the table size can be determined by subtracting
                addressMapDeletes from addressMapInserts.
                ''',
                'addressmapinserts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapMaxDesiredEntries', ATTRIBUTE, 'int' , None, None, 
                [(-1, 2147483647)], [], 
                '''                The maximum number of entries that are desired in the
                addressMapTable. The probe will not create more than
                this number of entries in the table, but may choose to create
                fewer entries in this table for any reason including the lack
                of resources.
                
                If this object is set to a value less than the current number
                of entries, enough entries are chosen in an
                implementation-dependent manner and deleted so that the number
                of entries in the table equals the value of this object.
                
                If this value is set to -1, the probe may create any number
                of entries in this table.
                
                This object may be used to control how resources are allocated
                on the probe for the various RMON functions.
                ''',
                'addressmapmaxdesiredentries',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'addressMap',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AddressMapControlTable.AddressMapControlEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AddressMapControlTable.AddressMapControlEntry',
            False, 
            [
            _MetaInfoClassMember('addressMapControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                A unique index for this entry in the addressMapControlTable.
                ''',
                'addressmapcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('addressMapControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The source of data for this addressMapControlEntry.
                ''',
                'addressmapcontroldatasource',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapControlDroppedFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of frames which were received by the probe
                and therefore not accounted for in the *StatsDropEvents, but
                for which the probe chose not to count for this entry for
                whatever reason.  Most often, this event occurs when the probe
                is out of some resources and decides to shed load from this
                collection.
                
                This count does not include packets that were not counted
                because they had MAC-layer errors.
                
                Note that, unlike the dropEvents counter, this number is the
                exact number of frames dropped.
                ''',
                'addressmapcontroldroppedframes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'addressmapcontrolowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapControlStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this addressMap control entry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                
                If this object is not equal to active(1), all associated
                entries in the addressMapTable shall be deleted.
                ''',
                'addressmapcontrolstatus',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'addressMapControlEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AddressMapControlTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AddressMapControlTable',
            False, 
            [
            _MetaInfoClassMember('addressMapControlEntry', REFERENCE_LIST, 'AddressMapControlEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AddressMapControlTable.AddressMapControlEntry', 
                [], [], 
                '''                A conceptual row in the addressMapControlTable.
                
                
                
                
                
                An example of the indexing of this entry is
                addressMapControlDroppedFrames.1
                ''',
                'addressmapcontrolentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'addressMapControlTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AddressMapTable.AddressMapEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AddressMapTable.AddressMapEntry',
            False, 
            [
            _MetaInfoClassMember('addressMapNetworkAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network address for this relation.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the protocolDirLocalIndex component of the
                index.
                
                For example, if the protocolDirLocalIndex indicates an
                encapsulation of ip, this object is encoded as a length
                octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'addressmapnetworkaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('addressMapSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The interface or port on which the associated network
                address was most recently seen.
                
                
                
                
                
                If this address mapping was discovered on an interface, this
                object shall identify the instance of the ifIndex
                object, defined in [3,5], for the desired interface.
                For example, if an entry were to receive data from
                interface #1, this object would be set to ifIndex.1.
                
                If this address mapping was discovered on a port, this
                object shall identify the instance of the rptrGroupPortIndex
                object, defined in [RFC1516], for the desired port.
                For example, if an entry were to receive data from
                group #1, port #1, this object would be set to
                rptrGroupPortIndex.1.1.
                
                Note that while the dataSource associated with this entry
                may only point to index objects, this object may at times
                point to repeater port objects. This situation occurs when
                the dataSource points to an interface which is a locally
                attached repeater and the agent has additional information
                about the source port of traffic seen on that repeater.
                ''',
                'addressmapsource',
                'RMON2-MIB', True),
            _MetaInfoClassMember('addressMapTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention to see how this works.
                ''',
                'addressmaptimemark',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('addressMapLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this entry was last
                created or the values of the physical address changed.
                
                This can be used to help detect duplicate address problems, in
                which case this object will be updated frequently.
                ''',
                'addressmaplastchange',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapPhysicalAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The last source physical address on which the associated
                network address was seen.  If the protocol of the associated
                network address was encapsulated inside of a network-level or
                higher protocol, this will be the address of the next-lower
                protocol with the addressRecognitionCapable bit enabled and
                will be formatted as specified for that protocol.
                ''',
                'addressmapphysicaladdress',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'addressMapEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AddressMapTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AddressMapTable',
            False, 
            [
            _MetaInfoClassMember('addressMapEntry', REFERENCE_LIST, 'AddressMapEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AddressMapTable.AddressMapEntry', 
                [], [], 
                '''                A conceptual row in the addressMapTable.
                The protocolDirLocalIndex in the index identifies the network
                layer protocol of the addressMapNetworkAddress.
                
                
                
                
                
                An example of the indexing of this entry is
                addressMapSource.783495.18.4.128.2.6.6.11.1.3.6.1.2.1.2.2.1.1.1
                ''',
                'addressmapentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'addressMapTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlHostTable.AlHostEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlHostTable.AlHostEntry',
            False, 
            [
            _MetaInfoClassMember('alHostTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention to see how this works.
                ''',
                'alhosttimemark',
                'RMON2-MIB', True),
            _MetaInfoClassMember('hlHostControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'hlhostcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlHostAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'nlhostaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex_2', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex_2',
                'RMON2-MIB', True),
            _MetaInfoClassMember('alHostCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this entry was last activated.
                This can be used by the management station to ensure that the
                entry has not been deleted and recreated between polls.
                ''',
                'alhostcreatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alHostInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted to this address
                of this protocol type since it was added to the
                alHostTable (excluding framing bits but including
                
                
                
                
                
                FCS octets), excluding those octets in packets that
                contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'alhostinoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alHostInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets of this protocol type without errors
                transmitted to this address since it was added to the
                alHostTable.  Note that this is the number of link-layer
                packets, so if a single network-layer packet is fragmented
                into several link-layer frames, this counter is incremented
                several times.
                ''',
                'alhostinpkts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alHostOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted by this address
                of this protocol type since it was added to the
                alHostTable (excluding framing bits but including
                FCS octets), excluding those octets in packets that
                contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'alhostoutoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alHostOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets of this protocol type without errors
                transmitted by this address since it was added to the
                alHostTable.  Note that this is the number of link-layer
                packets, so if a single network-layer packet is fragmented
                into several link-layer frames, this counter is incremented
                several times.
                ''',
                'alhostoutpkts',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alHostEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlHostTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlHostTable',
            False, 
            [
            _MetaInfoClassMember('alHostEntry', REFERENCE_LIST, 'AlHostEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlHostTable.AlHostEntry', 
                [], [], 
                '''                A conceptual row in the alHostTable.
                
                The hlHostControlIndex value in the index identifies the
                hlHostControlEntry on whose behalf this entry was created.
                The first protocolDirLocalIndex value in the index identifies
                the network layer protocol of the address.
                The nlHostAddress value in the index identifies the network
                layer address of this entry.
                The second protocolDirLocalIndex value in the index identifies
                the protocol that is counted by this entry.
                
                An example of the indexing in this entry is
                alHostOutPkts.1.783495.18.4.128.2.6.6.34
                ''',
                'alhostentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alHostTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixDSTable.AlMatrixDSEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixDSTable.AlMatrixDSEntry',
            False, 
            [
            _MetaInfoClassMember('alMatrixDSTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention to see how this works.
                ''',
                'almatrixdstimemark',
                'RMON2-MIB', True),
            _MetaInfoClassMember('hlMatrixControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'hlmatrixcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixDSDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'nlmatrixdsdestaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixDSSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'nlmatrixdssourceaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex_2', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex_2',
                'RMON2-MIB', True),
            _MetaInfoClassMember('alMatrixDSCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this entry was last activated.
                This can be used by the management station to ensure that the
                entry has not been deleted and recreated between polls.
                ''',
                'almatrixdscreatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixDSOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets in packets of this protocol type
                transmitted from the source address to the destination address
                since this entry was added to the alMatrixDSTable (excluding
                framing bits but including FCS octets), excluding those octets
                in packets that contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'almatrixdsoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixDSPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets of this protocol type without errors
                transmitted from the source address to the destination address
                since this entry was added to the alMatrixDSTable.  Note that
                this is the number of link-layer packets, so if a single
                network-layer packet is fragmented into several link-layer
                frames, this counter is incremented several times.
                ''',
                'almatrixdspkts',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixDSEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixDSTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixDSTable',
            False, 
            [
            _MetaInfoClassMember('alMatrixDSEntry', REFERENCE_LIST, 'AlMatrixDSEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixDSTable.AlMatrixDSEntry', 
                [], [], 
                '''                A conceptual row in the alMatrixDSTable.
                
                The hlMatrixControlIndex value in the index identifies the
                hlMatrixControlEntry on whose behalf this entry was created.
                The first protocolDirLocalIndex value in the index identifies
                the network layer protocol of the alMatrixDSSourceAddress and
                alMatrixDSDestAddress.
                
                
                
                
                
                The nlMatrixDSDestAddress value in the index identifies the
                network layer address of the destination host in this
                conversation.
                The nlMatrixDSSourceAddress value in the index identifies the
                network layer address of the source host in this conversation.
                The second protocolDirLocalIndex value in the index identifies
                the protocol that is counted by this entry.
                
                An example of the indexing of this entry is
                alMatrixDSPkts.1.783495.18.4.128.2.6.7.4.128.2.6.6.34
                ''',
                'almatrixdsentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixDSTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixSDTable.AlMatrixSDEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixSDTable.AlMatrixSDEntry',
            False, 
            [
            _MetaInfoClassMember('alMatrixSDTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention to see how this works.
                ''',
                'almatrixsdtimemark',
                'RMON2-MIB', True),
            _MetaInfoClassMember('hlMatrixControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'hlmatrixcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixSDDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'nlmatrixsddestaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixSDSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                ''',
                'nlmatrixsdsourceaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex_2', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex_2',
                'RMON2-MIB', True),
            _MetaInfoClassMember('alMatrixSDCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this entry was last activated.
                This can be used by the management station to ensure that the
                entry has not been deleted and recreated between polls.
                ''',
                'almatrixsdcreatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixSDOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets in packets of this protocol type
                transmitted from the source address to the destination address
                since this entry was added to the alMatrixSDTable (excluding
                framing bits but including FCS octets), excluding those octets
                in packets that contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'almatrixsdoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixSDPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets of this protocol type without errors
                transmitted from the source address to the destination address
                since this entry was added to the alMatrixSDTable.  Note that
                this is the number of link-layer packets, so if a single
                network-layer packet is fragmented into several link-layer
                frames, this counter is incremented several times.
                ''',
                'almatrixsdpkts',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixSDEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixSDTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixSDTable',
            False, 
            [
            _MetaInfoClassMember('alMatrixSDEntry', REFERENCE_LIST, 'AlMatrixSDEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixSDTable.AlMatrixSDEntry', 
                [], [], 
                '''                A conceptual row in the alMatrixSDTable.
                
                The hlMatrixControlIndex value in the index identifies the
                hlMatrixControlEntry on whose behalf this entry was created.
                The first protocolDirLocalIndex value in the index identifies
                the network layer protocol of the nlMatrixSDSourceAddress and
                nlMatrixSDDestAddress.
                The nlMatrixSDSourceAddress value in the index identifies the
                network layer address of the source host in this conversation.
                The nlMatrixSDDestAddress value in the index identifies the
                network layer address of the destination host in this
                conversation.
                The second protocolDirLocalIndex value in the index identifies
                the protocol that is counted by this entry.
                
                An example of the indexing of this entry is
                alMatrixSDPkts.1.783495.18.4.128.2.6.6.4.128.2.6.7.34
                ''',
                'almatrixsdentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixSDTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry.AlMatrixTopNControlRateBase_Enum' : _MetaInfoEnum('AlMatrixTopNControlRateBase_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'alMatrixTopNTerminalsPkts':'ALMATRIXTOPNTERMINALSPKTS',
            'alMatrixTopNTerminalsOctets':'ALMATRIXTOPNTERMINALSOCTETS',
            'alMatrixTopNAllPkts':'ALMATRIXTOPNALLPKTS',
            'alMatrixTopNAllOctets':'ALMATRIXTOPNALLOCTETS',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry',
            False, 
            [
            _MetaInfoClassMember('alMatrixTopNControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry
                in the alMatrixTopNControlTable.  Each such
                entry defines one top N report prepared for
                one interface.
                ''',
                'almatrixtopncontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('alMatrixTopNControlDuration', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of seconds that this report has collected
                during the last sampling interval.
                
                When the associated alMatrixTopNControlTimeRemaining object
                is set, this object shall be set by the probe to the
                same value and shall not be modified until the next
                time the alMatrixTopNControlTimeRemaining is set.
                
                This value shall be zero if no reports have been
                requested for this alMatrixTopNControlEntry.
                ''',
                'almatrixtopncontrolduration',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlGeneratedReports', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of reports that have been generated by this entry.
                ''',
                'almatrixtopncontrolgeneratedreports',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlGrantedSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The maximum number of matrix entries in this report.
                
                When the associated alMatrixTopNControlRequestedSize object
                is created or modified, the probe should set this
                
                
                
                
                
                object as closely to the requested value as is
                possible for the particular implementation and
                available resources. The probe must not lower this
                value except as a result of a set to the associated
                alMatrixTopNControlRequestedSize object.
                
                If the value of alMatrixTopNControlRateBase is equal to
                alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, when the
                next topN report is generated, matrix entries with the highest
                value of alMatrixTopNPktRate shall be placed in this table in
                decreasing order of this rate until there is no more room or
                until there are no more matrix entries.
                
                If the value of alMatrixTopNControlRateBase is equal to
                alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, when the
                next topN report is generated, matrix entries with the highest
                value of alMatrixTopNOctetRate shall be placed in this table
                in decreasing order of this rate until there is no more room
                or until there are no more matrix entries.
                
                It is an implementation-specific matter how entries with the
                same value of alMatrixTopNPktRate or alMatrixTopNOctetRate are
                sorted.  It is also an implementation-specific matter as to
                whether or not zero-valued entries are available.
                ''',
                'almatrixtopncontrolgrantedsize',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlMatrixIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The alMatrix[SD/DS] table for which a top N report will be
                prepared on behalf of this entry.  The alMatrix[SD/DS] table
                is identified by the value of the hlMatrixControlIndex
                for that table - that value is used here to identify the
                particular table.
                
                This object may not be modified if the associated
                alMatrixTopNControlStatus object is equal to active(1).
                ''',
                'almatrixtopncontrolmatrixindex',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'almatrixtopncontrolowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlRateBase', REFERENCE_ENUM_CLASS, 'AlMatrixTopNControlRateBase_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry.AlMatrixTopNControlRateBase_Enum', 
                [], [], 
                '''                The variable for each alMatrix[SD/DS] entry that the
                
                
                
                
                
                alMatrixTopNEntries are sorted by, as well as the
                selector of the view of the matrix table that will be
                used.
                
                The values alMatrixTopNTerminalsPkts and
                alMatrixTopNTerminalsOctets cause collection only from
                protocols that have no child protocols that are counted.  The
                values alMatrixTopNAllPkts and alMatrixTopNAllOctets cause
                collection from all alMatrix entries.
                
                This object may not be modified if the associated
                alMatrixTopNControlStatus object is equal to active(1).
                ''',
                'almatrixtopncontrolratebase',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlRequestedSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The maximum number of matrix entries requested for this report.
                
                When this object is created or modified, the probe
                should set alMatrixTopNControlGrantedSize as closely to this
                object as is possible for the particular probe
                implementation and available resources.
                ''',
                'almatrixtopncontrolrequestedsize',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlStartTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this top N report was
                last started.  In other words, this is the time that
                the associated alMatrixTopNControlTimeRemaining object
                was modified to start the requested report or the time
                the report was last automatically (re)started.
                
                This object may be used by the management station to
                determine if a report was missed or not.
                ''',
                'almatrixtopncontrolstarttime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this alMatrixTopNControlEntry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                
                If this object is not equal to active(1), all
                associated entries in the alMatrixTopNTable shall be
                deleted by the agent.
                ''',
                'almatrixtopncontrolstatus',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlTimeRemaining', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The number of seconds left in the report currently
                being collected.  When this object is modified by
                the management station, a new collection is started,
                possibly aborting a currently running report.  The
                new value is used as the requested duration of this
                report, and is immediately loaded into the associated
                alMatrixTopNControlDuration object.
                When the report finishes, the probe will automatically
                start another collection with the same initial value
                of alMatrixTopNControlTimeRemaining.  Thus the management
                station may simply read the resulting reports repeatedly,
                checking the startTime and duration each time to ensure that a
                report was not missed or that the report parameters were not
                changed.
                
                While the value of this object is non-zero, it decrements
                by one per second until it reaches zero.  At the time
                that this object decrements to zero, the report is made
                accessible in the alMatrixTopNTable, overwriting any report
                that may be there.
                
                When this object is modified by the management station, any
                associated entries in the alMatrixTopNTable shall be deleted.
                
                (Note that this is a different algorithm than the one used in
                the hostTopNTable).
                ''',
                'almatrixtopncontroltimeremaining',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixTopNControlEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixTopNControlTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixTopNControlTable',
            False, 
            [
            _MetaInfoClassMember('alMatrixTopNControlEntry', REFERENCE_LIST, 'AlMatrixTopNControlEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry', 
                [], [], 
                '''                A conceptual row in the alMatrixTopNControlTable.
                
                An example of the indexing of this table is
                alMatrixTopNControlDuration.3
                ''',
                'almatrixtopncontrolentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixTopNControlTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixTopNTable.AlMatrixTopNEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixTopNTable.AlMatrixTopNEntry',
            False, 
            [
            _MetaInfoClassMember('alMatrixTopNControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'almatrixtopncontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('alMatrixTopNIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in
                the alMatrixTopNTable among those in the same report.
                This index is between 1 and N, where N is the
                number of entries in this report.
                
                If the value of alMatrixTopNControlRateBase is equal to
                alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, increasing
                values of alMatrixTopNIndex shall be assigned to entries with
                decreasing values of alMatrixTopNPktRate until index N is
                assigned or there are no more alMatrixTopNEntries.
                
                If the value of alMatrixTopNControlRateBase is equal to
                alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets,
                increasing values of alMatrixTopNIndex shall be assigned to
                entries with decreasing values of alMatrixTopNOctetRate until
                index N is assigned or there are no more alMatrixTopNEntries.
                ''',
                'almatrixtopnindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('alMatrixTopNAppProtocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The type of the protocol counted by this matrix entry.
                ''',
                'almatrixtopnappprotocoldirlocalindex',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network layer address of the destination host in this
                conversation.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the associated alMatrixTopNProtocolDirLocalIndex.
                
                For example, if the alMatrixTopNProtocolDirLocalIndex
                indicates an encapsulation of ip, this object is encoded as a
                length octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'almatrixtopndestaddress',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNOctetRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets seen of this protocol from the source
                host to the destination host during this sampling interval,
                counted using the rules for counting the alMatrixSDOctets
                object.
                
                If the value of alMatrixTopNControlRateBase is
                alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, this
                variable will be used to sort this report.
                ''',
                'almatrixtopnoctetrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNPktRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets seen of this protocol from the source
                host to the destination host during this sampling interval,
                counted using the rules for counting the alMatrixSDPkts
                object.
                
                If the value of alMatrixTopNControlRateBase is
                alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, this
                variable will be used to sort this report.
                ''',
                'almatrixtopnpktrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNProtocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The protocolDirLocalIndex of the network layer protocol of
                this entry's network address.
                ''',
                'almatrixtopnprotocoldirlocalindex',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNReverseOctetRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets seen of this protocol from the
                destination host to the source host during this sampling
                interval, counted using the rules for counting the
                alMatrixDSOctets object  (note that the corresponding
                alMatrixSDOctets object selected is the one whose source
                address is equal to alMatrixTopNDestAddress and whose
                destination address is equal to alMatrixTopNSourceAddress.)
                
                Note that if the value of alMatrixTopNControlRateBase is equal
                
                
                
                
                
                to alMatrixTopNTerminalsOctets or alMatrixTopNAllOctets, the
                sort of topN entries is based entirely on
                alMatrixTopNOctetRate, and not on the value of this object.
                ''',
                'almatrixtopnreverseoctetrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNReversePktRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets seen of this protocol from the
                destination host to the source host during this sampling
                interval, counted using the rules for counting the
                alMatrixDSPkts object  (note that the corresponding
                alMatrixSDPkts object selected is the one whose source address
                is equal to alMatrixTopNDestAddress and whose destination
                address is equal to alMatrixTopNSourceAddress.)
                
                Note that if the value of alMatrixTopNControlRateBase is equal
                to alMatrixTopNTerminalsPkts or alMatrixTopNAllPkts, the sort
                of topN entries is based entirely on alMatrixTopNPktRate, and
                not on the value of this object.
                ''',
                'almatrixtopnreversepktrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network layer address of the source host in this
                conversation.
                This is represented as an octet string with
                specific semantics and length as identified
                
                
                
                
                
                by the associated alMatrixTopNProtocolDirLocalIndex.
                
                For example, if the alMatrixTopNProtocolDirLocalIndex
                indicates an encapsulation of ip, this object is encoded as a
                length octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'almatrixtopnsourceaddress',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixTopNEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.AlMatrixTopNTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.AlMatrixTopNTable',
            False, 
            [
            _MetaInfoClassMember('alMatrixTopNEntry', REFERENCE_LIST, 'AlMatrixTopNEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixTopNTable.AlMatrixTopNEntry', 
                [], [], 
                '''                A conceptual row in the alMatrixTopNTable.
                
                The alMatrixTopNControlIndex value in the index identifies
                the alMatrixTopNControlEntry on whose behalf this entry was
                created.
                
                An example of the indexing of this table is
                alMatrixTopNPktRate.3.10
                ''',
                'almatrixtopnentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'alMatrixTopNTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.HlHostControlTable.HlHostControlEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.HlHostControlTable.HlHostControlEntry',
            False, 
            [
            _MetaInfoClassMember('hlHostControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                hlHostControlTable.  Each such entry defines
                a function that discovers hosts on a particular
                interface and places statistics about them in the
                nlHostTable, and optionally in the alHostTable, on
                behalf of this hlHostControlEntry.
                ''',
                'hlhostcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('hlHostControlAlDeletes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an alHost entry has been
                deleted from the alHost table (for any reason).  If an entry
                is deleted, then inserted, and then deleted, this counter will
                be incremented by 2.
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                data structures for those short periods of time.
                
                Note that the table size can be determined by subtracting
                hlHostControlAlDeletes from hlHostControlAlInserts.
                ''',
                'hlhostcontrolaldeletes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlAlDroppedFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of frames which were received by the probe
                and therefore not accounted for in the *StatsDropEvents, but
                for which the probe chose not to count for the associated
                alHost entries for whatever reason.  Most often, this event
                occurs when the probe is out of some resources and decides to
                shed load from this collection.
                
                This count does not include packets that were not counted
                because they had MAC-layer errors.
                
                
                
                
                
                
                Note that if the alHostTable is not implemented or is inactive
                because no protocols are enabled in the protocol directory,
                this value should be 0.
                
                Note that, unlike the dropEvents counter, this number is the
                exact number of frames dropped.
                ''',
                'hlhostcontrolaldroppedframes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlAlInserts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an alHost entry has been
                inserted into the alHost table.  If an entry is inserted, then
                deleted, and then inserted, this counter will be incremented
                by 2.
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                data structures for those short periods of time.
                
                Note that the table size can be determined by subtracting
                hlHostControlAlDeletes from hlHostControlAlInserts.
                ''',
                'hlhostcontrolalinserts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlAlMaxDesiredEntries', ATTRIBUTE, 'int' , None, None, 
                [(-1, 2147483647)], [], 
                '''                The maximum number of entries that are desired in the alHost
                table on behalf of this control entry. The probe will not
                create more than this number of associated entries in the
                table, but may choose to create fewer entries in this table
                for any reason including the lack of resources.
                
                If this object is set to a value less than the current number
                of entries, enough entries are chosen in an
                implementation-dependent manner and deleted so that the number
                of entries in the table equals the value of this object.
                
                If this value is set to -1, the probe may create any number
                of entries in this table.  If the associated
                hlHostControlStatus object is equal to `active', this
                object may not be modified.
                
                This object may be used to control how resources are allocated
                on the probe for the various RMON functions.
                ''',
                'hlhostcontrolalmaxdesiredentries',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The source of data for the associated host tables.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the
                identified interface.
                
                This object may not be modified if the associated
                hlHostControlStatus object is equal to active(1).
                ''',
                'hlhostcontroldatasource',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlNlDeletes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an nlHost entry has been
                deleted from the nlHost table (for any reason).  If an entry
                is deleted, then inserted, and then deleted, this counter will
                be incremented by 2.
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                
                
                
                
                
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                data structures for those short periods of time.
                
                Note that the table size can be determined by subtracting
                hlHostControlNlDeletes from hlHostControlNlInserts.
                ''',
                'hlhostcontrolnldeletes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlNlDroppedFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of frames which were received by the probe
                and therefore not accounted for in the *StatsDropEvents, but
                for which the probe chose not to count for the associated
                
                
                
                
                
                nlHost entries for whatever reason.  Most often, this event
                occurs when the probe is out of some resources and decides to
                shed load from this collection.
                
                This count does not include packets that were not counted
                because they had MAC-layer errors.
                
                Note that if the nlHostTable is inactive because no protocols
                are enabled in the protocol directory, this value should be 0.
                
                Note that, unlike the dropEvents counter, this number is the
                exact number of frames dropped.
                ''',
                'hlhostcontrolnldroppedframes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlNlInserts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an nlHost entry has been
                inserted into the nlHost table.  If an entry is inserted, then
                deleted, and then inserted, this counter will be incremented
                by 2.
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                data structures for those short periods of time.
                
                Note that the table size can be determined by subtracting
                hlHostControlNlDeletes from hlHostControlNlInserts.
                ''',
                'hlhostcontrolnlinserts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlNlMaxDesiredEntries', ATTRIBUTE, 'int' , None, None, 
                [(-1, 2147483647)], [], 
                '''                The maximum number of entries that are desired in the
                nlHostTable on behalf of this control entry. The probe will
                not create more than this number of associated entries in the
                table, but may choose to create fewer entries in this table
                for any reason including the lack of resources.
                
                If this object is set to a value less than the current number
                of entries, enough entries are chosen in an
                implementation-dependent manner and deleted so that the number
                of entries in the table equals the value of this object.
                
                If this value is set to -1, the probe may create any number
                of entries in this table.  If the associated
                hlHostControlStatus object is equal to `active', this
                object may not be modified.
                
                This object may be used to control how resources are allocated
                on the probe for the various RMON functions.
                ''',
                'hlhostcontrolnlmaxdesiredentries',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'hlhostcontrolowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this hlHostControlEntry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                
                If this object is not equal to active(1), all associated
                entries in the nlHostTable and alHostTable shall be deleted.
                ''',
                'hlhostcontrolstatus',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'hlHostControlEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.HlHostControlTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.HlHostControlTable',
            False, 
            [
            _MetaInfoClassMember('hlHostControlEntry', REFERENCE_LIST, 'HlHostControlEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.HlHostControlTable.HlHostControlEntry', 
                [], [], 
                '''                A conceptual row in the hlHostControlTable.
                
                An example of the indexing of this entry is
                hlHostControlNlDroppedFrames.1
                ''',
                'hlhostcontrolentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'hlHostControlTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.HlMatrixControlTable.HlMatrixControlEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.HlMatrixControlTable.HlMatrixControlEntry',
            False, 
            [
            _MetaInfoClassMember('hlMatrixControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                hlMatrixControlTable.  Each such entry defines
                a function that discovers conversations on a particular
                interface and places statistics about them in the
                nlMatrixSDTable and the nlMatrixDSTable, and optionally the
                alMatrixSDTable and alMatrixDSTable, on behalf of this
                hlMatrixControlEntry.
                ''',
                'hlmatrixcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('hlMatrixControlAlDeletes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an alMatrix entry has been
                deleted from the alMatrix tables.  If an entry is deleted,
                then inserted, and then deleted, this counter will be
                incremented by 2.  The deletion of a conversation from both
                the alMatrixSDTable and alMatrixDSTable shall be counted as
                two deletions (even though every deletion from one table must
                be accompanied by a deletion from the other).
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                data structures for those short periods of time.
                
                Note that the table size can be determined by subtracting
                hlMatrixControlAlDeletes from hlMatrixControlAlInserts.
                ''',
                'hlmatrixcontrolaldeletes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlAlDroppedFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of frames which were received by the probe
                and therefore not accounted for in the *StatsDropEvents, but
                for which the probe chose not to count for this entry for
                whatever reason.  Most often, this event occurs when the probe
                is out of some resources and decides to shed load from this
                collection.
                
                This count does not include packets that were not counted
                because they had MAC-layer errors.
                
                Note that if the alMatrixTables are not implemented or are
                inactive because no protocols are enabled in the protocol
                directory, this value should be 0.
                
                Note that, unlike the dropEvents counter, this number is the
                exact number of frames dropped.
                ''',
                'hlmatrixcontrolaldroppedframes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlAlInserts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an alMatrix entry has been
                inserted into the alMatrix tables.  If an entry is inserted,
                then deleted, and then inserted, this counter will be
                incremented by 2.  The addition of a conversation into both
                the alMatrixSDTable and alMatrixDSTable shall be counted as
                two insertions (even though every addition into one table must
                be accompanied by an insertion into the other).
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                
                
                
                
                
                data structures for those short periods of time.
                
                Note that the table size can be determined by subtracting
                hlMatrixControlAlDeletes from hlMatrixControlAlInserts.
                ''',
                'hlmatrixcontrolalinserts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlAlMaxDesiredEntries', ATTRIBUTE, 'int' , None, None, 
                [(-1, 2147483647)], [], 
                '''                The maximum number of entries that are desired in the
                alMatrix tables on behalf of this control entry. The probe
                will not create more than this number of associated entries in
                the table, but may choose to create fewer entries in this
                table for any reason including the lack of resources.
                
                If this object is set to a value less than the current number
                of entries, enough entries are chosen in an
                implementation-dependent manner and deleted so that the number
                of entries in the table equals the value of this object.
                
                If this value is set to -1, the probe may create any number
                of entries in this table.  If the associated
                
                
                
                
                
                hlMatrixControlStatus object is equal to `active', this
                object may not be modified.
                
                This object may be used to control how resources are allocated
                on the probe for the various RMON functions.
                ''',
                'hlmatrixcontrolalmaxdesiredentries',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The source of the data for the associated matrix tables.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the
                
                
                
                
                
                identified interface.
                
                This object may not be modified if the associated
                hlMatrixControlStatus object is equal to active(1).
                ''',
                'hlmatrixcontroldatasource',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlNlDeletes', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an nlMatrix entry has been
                deleted from the nlMatrix tables (for any reason).  If an
                entry is deleted, then inserted, and then deleted, this
                counter will be incremented by 2.  The deletion of a
                conversation from both the nlMatrixSDTable and nlMatrixDSTable
                shall be counted as two deletions (even though every deletion
                from one table must be accompanied by a deletion from the
                other).
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                data structures for those short periods of time.
                
                Note that the table size can be determined by subtracting
                hlMatrixControlNlDeletes from hlMatrixControlNlInserts.
                ''',
                'hlmatrixcontrolnldeletes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlNlDroppedFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of frames which were received by the probe
                and therefore not accounted for in the *StatsDropEvents, but
                for which the probe chose not to count for this entry for
                whatever reason.  Most often, this event occurs when the probe
                is out of some resources and decides to shed load from this
                collection.
                
                This count does not include packets that were not counted
                because they had MAC-layer errors.
                
                Note that if the nlMatrixTables are inactive because no
                protocols are enabled in the protocol directory, this value
                should be 0.
                
                Note that, unlike the dropEvents counter, this number is the
                exact number of frames dropped.
                ''',
                'hlmatrixcontrolnldroppedframes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlNlInserts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times an nlMatrix entry has been
                inserted into the nlMatrix tables.  If an entry is inserted,
                then deleted, and then inserted, this counter will be
                incremented by 2.  The addition of a conversation into both
                the nlMatrixSDTable and nlMatrixDSTable shall be counted as
                two insertions (even though every addition into one table must
                be accompanied by an insertion into the other).
                
                To allow for efficient implementation strategies, agents may
                delay updating this object for short periods of time.  For
                example, an implementation strategy may allow internal
                data structures to differ from those visible via SNMP for
                short periods of time.  This counter may reflect the internal
                data structures for those short periods of time.
                
                
                
                
                
                Note that the sum of then nlMatrixSDTable and nlMatrixDSTable
                sizes can be determined by subtracting
                hlMatrixControlNlDeletes from hlMatrixControlNlInserts.
                ''',
                'hlmatrixcontrolnlinserts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlNlMaxDesiredEntries', ATTRIBUTE, 'int' , None, None, 
                [(-1, 2147483647)], [], 
                '''                The maximum number of entries that are desired in the
                nlMatrix tables on behalf of this control entry. The probe
                will not create more than this number of associated entries in
                the table, but may choose to create fewer entries in this
                table for any reason including the lack of resources.
                
                If this object is set to a value less than the current number
                of entries, enough entries are chosen in an
                implementation-dependent manner and deleted so that the number
                of entries in the table equals the value of this object.
                
                If this value is set to -1, the probe may create any number
                of entries in this table.  If the associated
                
                
                
                
                
                hlMatrixControlStatus object is equal to `active', this
                object may not be modified.
                
                This object may be used to control how resources are allocated
                on the probe for the various RMON functions.
                ''',
                'hlmatrixcontrolnlmaxdesiredentries',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'hlmatrixcontrolowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this hlMatrixControlEntry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                
                If this object is not equal to active(1), all
                associated entries in the nlMatrixSDTable,
                nlMatrixDSTable, alMatrixSDTable, and the alMatrixDSTable
                shall be deleted by the agent.
                ''',
                'hlmatrixcontrolstatus',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'hlMatrixControlEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.HlMatrixControlTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.HlMatrixControlTable',
            False, 
            [
            _MetaInfoClassMember('hlMatrixControlEntry', REFERENCE_LIST, 'HlMatrixControlEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.HlMatrixControlTable.HlMatrixControlEntry', 
                [], [], 
                '''                A conceptual row in the hlMatrixControlTable.
                
                An example of indexing of this entry is
                hlMatrixControlNlDroppedFrames.1
                ''',
                'hlmatrixcontrolentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'hlMatrixControlTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NetConfigTable.NetConfigEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NetConfigTable.NetConfigEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('netConfigIPAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of this Net interface.  The default value
                for this object is 0.0.0.0.  If either the netConfigIPAddress
                or netConfigSubnetMask are 0.0.0.0, then when the device
                boots, it may use BOOTP to try to figure out what these
                values should be. If BOOTP fails, before the device
                can talk on the network, this value must be configured
                (e.g., through a terminal attached to the device). If BOOTP is
                
                
                
                
                
                used, care should be taken to not send BOOTP broadcasts too
                frequently and to eventually send very infrequently if no
                replies are received.
                ''',
                'netconfigipaddress',
                'RMON2-MIB', False),
            _MetaInfoClassMember('netConfigStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this netConfigEntry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                ''',
                'netconfigstatus',
                'RMON2-MIB', False),
            _MetaInfoClassMember('netConfigSubnetMask', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The subnet mask of this Net interface.  The default value
                for this object is 0.0.0.0.  If either the netConfigIPAddress
                or netConfigSubnetMask are 0.0.0.0, then when the device
                boots, it may use BOOTP to try to figure out what these
                values should be. If BOOTP fails, before the device
                can talk on the network, this value must be configured
                (e.g., through a terminal attached to the device). If BOOTP is
                used, care should be taken to not send BOOTP broadcasts too
                frequently and to eventually send very infrequently if no
                replies are received.
                ''',
                'netconfigsubnetmask',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'netConfigEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NetConfigTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NetConfigTable',
            False, 
            [
            _MetaInfoClassMember('netConfigEntry', REFERENCE_LIST, 'NetConfigEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NetConfigTable.NetConfigEntry', 
                [], [], 
                '''                A set of configuration parameters for a particular
                network interface on this device. If the device has no network
                interface, this table is empty.
                
                The index is composed of the ifIndex assigned to the
                corresponding interface.
                ''',
                'netconfigentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'netConfigTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlHostTable.NlHostEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlHostTable.NlHostEntry',
            False, 
            [
            _MetaInfoClassMember('hlHostControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'hlhostcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlHostAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network address for this nlHostEntry.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the protocolDirLocalIndex component of the index.
                
                For example, if the protocolDirLocalIndex indicates an
                encapsulation of ip, this object is encoded as a length
                octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'nlhostaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlHostTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention to see how this works.
                ''',
                'nlhosttimemark',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlHostCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this entry was last activated.
                This can be used by the management station to ensure that the
                entry has not been deleted and recreated between polls.
                ''',
                'nlhostcreatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlHostInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted to this address
                since it was added to the nlHostTable (excluding
                framing bits but including FCS octets), excluding
                those octets in packets that contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'nlhostinoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlHostInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors transmitted to
                this address since it was added to the nlHostTable.  Note that
                this is the number of link-layer packets, so if a single
                network-layer packet is fragmented into several link-layer
                frames, this counter is incremented several times.
                ''',
                'nlhostinpkts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlHostOutMacNonUnicastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors transmitted by this
                address that were directed to any MAC broadcast addresses
                or to any MAC multicast addresses since this host was
                added to the nlHostTable. Note that this is the number of
                link-layer packets, so if a single network-layer packet is
                fragmented into several link-layer frames, this counter is
                incremented several times.
                ''',
                'nlhostoutmacnonunicastpkts',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlHostOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted by this address
                since it was added to the nlHostTable (excluding
                framing bits but including FCS octets), excluding
                those octets in packets that contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'nlhostoutoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlHostOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors transmitted by
                
                
                
                
                
                this address since it was added to the nlHostTable.  Note that
                this is the number of link-layer packets, so if a single
                network-layer packet is fragmented into several link-layer
                frames, this counter is incremented several times.
                ''',
                'nlhostoutpkts',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlHostEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlHostTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlHostTable',
            False, 
            [
            _MetaInfoClassMember('nlHostEntry', REFERENCE_LIST, 'NlHostEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlHostTable.NlHostEntry', 
                [], [], 
                '''                A conceptual row in the nlHostTable.
                
                The hlHostControlIndex value in the index identifies the
                hlHostControlEntry on whose behalf this entry was created.
                The protocolDirLocalIndex value in the index identifies the
                network layer protocol of the nlHostAddress.
                
                An example of the indexing of this entry is
                nlHostOutPkts.1.783495.18.4.128.2.6.6.
                ''',
                'nlhostentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlHostTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixDSTable.NlMatrixDSEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixDSTable.NlMatrixDSEntry',
            False, 
            [
            _MetaInfoClassMember('hlMatrixControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'hlmatrixcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixDSDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network destination address for this
                nlMatrixDSEntry.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the protocolDirLocalIndex component of the index.
                
                For example, if the protocolDirLocalIndex indicates an
                encapsulation of ip, this object is encoded as a length
                octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'nlmatrixdsdestaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixDSSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network source address for this nlMatrixDSEntry.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the protocolDirLocalIndex component of the index.
                
                For example, if the protocolDirLocalIndex indicates an
                encapsulation of ip, this object is encoded as a length
                octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'nlmatrixdssourceaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixDSTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention to see how this works.
                ''',
                'nlmatrixdstimemark',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixDSCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this entry was last activated.
                This can be used by the management station to ensure that the
                entry has not been deleted and recreated between polls.
                ''',
                'nlmatrixdscreatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixDSOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted from the source address
                to the destination address since this entry was added to the
                nlMatrixDSTable (excluding framing bits but
                including FCS octets), excluding those octets in packets that
                contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'nlmatrixdsoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixDSPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors transmitted from the
                source address to the destination address since this entry was
                added to the nlMatrixDSTable.  Note that this is the number of
                link-layer packets, so if a single network-layer packet is
                fragmented into several link-layer frames, this counter is
                incremented several times.
                ''',
                'nlmatrixdspkts',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixDSEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixDSTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixDSTable',
            False, 
            [
            _MetaInfoClassMember('nlMatrixDSEntry', REFERENCE_LIST, 'NlMatrixDSEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixDSTable.NlMatrixDSEntry', 
                [], [], 
                '''                A conceptual row in the nlMatrixDSTable.
                
                The hlMatrixControlIndex value in the index identifies the
                hlMatrixControlEntry on whose behalf this entry was created.
                The protocolDirLocalIndex value in the index identifies the
                network layer protocol of the nlMatrixDSSourceAddress and
                nlMatrixDSDestAddress.
                
                An example of the indexing of this table is
                nlMatrixDSPkts.1.783495.18.4.128.2.6.7.4.128.2.6.6
                ''',
                'nlmatrixdsentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixDSTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixSDTable.NlMatrixSDEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixSDTable.NlMatrixSDEntry',
            False, 
            [
            _MetaInfoClassMember('hlMatrixControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'hlmatrixcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixSDDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network destination address for this
                nlMatrixSDEntry.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the protocolDirLocalIndex component of the index.
                
                For example, if the protocolDirLocalIndex indicates an
                encapsulation of ip, this object is encoded as a length
                octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'nlmatrixsddestaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixSDSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network source address for this nlMatrixSDEntry.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the protocolDirLocalIndex component of the index.
                
                For example, if the protocolDirLocalIndex indicates an
                encapsulation of ip, this object is encoded as a length
                octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'nlmatrixsdsourceaddress',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixSDTimeMark', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                A TimeFilter for this entry.  See the TimeFilter textual
                convention to see how this works.
                ''',
                'nlmatrixsdtimemark',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixSDCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this entry was last activated.
                This can be used by the management station to ensure that the
                entry has not been deleted and recreated between polls.
                ''',
                'nlmatrixsdcreatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixSDOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted from the source address to
                the destination address since this entry was added to the
                nlMatrixSDTable (excluding framing bits but
                including FCS octets), excluding those octets in packets that
                contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'nlmatrixsdoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixSDPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors transmitted from the
                source address to the destination address since this entry was
                added to the nlMatrixSDTable.  Note that this is the number of
                link-layer packets, so if a single network-layer packet is
                fragmented into several link-layer frames, this counter is
                incremented several times.
                ''',
                'nlmatrixsdpkts',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixSDEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixSDTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixSDTable',
            False, 
            [
            _MetaInfoClassMember('nlMatrixSDEntry', REFERENCE_LIST, 'NlMatrixSDEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixSDTable.NlMatrixSDEntry', 
                [], [], 
                '''                A conceptual row in the nlMatrixSDTable.
                
                The hlMatrixControlIndex value in the index identifies the
                hlMatrixControlEntry on whose behalf this entry was created.
                The protocolDirLocalIndex value in the index identifies the
                network layer protocol of the nlMatrixSDSourceAddress and
                nlMatrixSDDestAddress.
                
                An example of the indexing of this table is
                nlMatrixSDPkts.1.783495.18.4.128.2.6.6.4.128.2.6.7
                ''',
                'nlmatrixsdentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixSDTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry.NlMatrixTopNControlRateBase_Enum' : _MetaInfoEnum('NlMatrixTopNControlRateBase_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'nlMatrixTopNPkts':'NLMATRIXTOPNPKTS',
            'nlMatrixTopNOctets':'NLMATRIXTOPNOCTETS',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry',
            False, 
            [
            _MetaInfoClassMember('nlMatrixTopNControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry
                in the nlMatrixTopNControlTable.  Each such
                entry defines one top N report prepared for
                one interface.
                ''',
                'nlmatrixtopncontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixTopNControlDuration', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of seconds that this report has collected
                during the last sampling interval.
                
                When the associated nlMatrixTopNControlTimeRemaining object is
                set, this object shall be set by the probe to the
                same value and shall not be modified until the next
                time the nlMatrixTopNControlTimeRemaining is set.
                This value shall be zero if no reports have been
                requested for this nlMatrixTopNControlEntry.
                ''',
                'nlmatrixtopncontrolduration',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlGeneratedReports', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of reports that have been generated by this entry.
                ''',
                'nlmatrixtopncontrolgeneratedreports',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlGrantedSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The maximum number of matrix entries in this report.
                
                When the associated nlMatrixTopNControlRequestedSize object is
                created or modified, the probe should set this
                object as closely to the requested value as is
                possible for the particular implementation and
                available resources. The probe must not lower this
                value except as a result of a set to the associated
                nlMatrixTopNControlRequestedSize object.
                
                If the value of nlMatrixTopNControlRateBase is equal to
                nlMatrixTopNPkts, when the next topN report is generated,
                matrix entries with the highest value of nlMatrixTopNPktRate
                shall be placed in this table in decreasing order of this rate
                until there is no more room or until there are no more
                
                
                
                
                
                matrix entries.
                
                If the value of nlMatrixTopNControlRateBase is equal to
                nlMatrixTopNOctets, when the next topN report is generated,
                matrix entries with the highest value of nlMatrixTopNOctetRate
                shall be placed in this table in decreasing order of this rate
                until there is no more room or until there are no more
                matrix entries.
                
                It is an implementation-specific matter how entries with the
                same value of nlMatrixTopNPktRate or nlMatrixTopNOctetRate are
                sorted.  It is also an implementation-specific matter as to
                whether or not zero-valued entries are available.
                ''',
                'nlmatrixtopncontrolgrantedsize',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlMatrixIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The nlMatrix[SD/DS] table for which a top N report will be
                prepared on behalf of this entry.  The nlMatrix[SD/DS] table
                is identified by the value of the hlMatrixControlIndex
                for that table - that value is used here to identify the
                particular table.
                
                This object may not be modified if the associated
                nlMatrixTopNControlStatus object is equal to active(1).
                ''',
                'nlmatrixtopncontrolmatrixindex',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'nlmatrixtopncontrolowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlRateBase', REFERENCE_ENUM_CLASS, 'NlMatrixTopNControlRateBase_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry.NlMatrixTopNControlRateBase_Enum', 
                [], [], 
                '''                The variable for each nlMatrix[SD/DS] entry that the
                nlMatrixTopNEntries are sorted by.
                
                
                
                
                
                This object may not be modified if the associated
                nlMatrixTopNControlStatus object is equal to active(1).
                ''',
                'nlmatrixtopncontrolratebase',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlRequestedSize', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The maximum number of matrix entries requested for this report.
                
                When this object is created or modified, the probe
                should set nlMatrixTopNControlGrantedSize as closely to this
                object as is possible for the particular probe
                implementation and available resources.
                ''',
                'nlmatrixtopncontrolrequestedsize',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlStartTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this top N report was
                last started.  In other words, this is the time that
                the associated nlMatrixTopNControlTimeRemaining object was
                modified to start the requested report or the time
                the report was last automatically (re)started.
                
                This object may be used by the management station to
                determine if a report was missed or not.
                ''',
                'nlmatrixtopncontrolstarttime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this nlMatrixTopNControlEntry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                
                
                
                
                
                If this object is not equal to active(1), all
                associated entries in the nlMatrixTopNTable shall be deleted
                by the agent.
                ''',
                'nlmatrixtopncontrolstatus',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlTimeRemaining', ATTRIBUTE, 'int' , None, None, 
                [(0, 2147483647)], [], 
                '''                The number of seconds left in the report currently
                being collected.  When this object is modified by
                the management station, a new collection is started,
                possibly aborting a currently running report.  The
                new value is used as the requested duration of this
                report, and is immediately loaded into the associated
                nlMatrixTopNControlDuration object.
                When the report finishes, the probe will automatically
                start another collection with the same initial value
                of nlMatrixTopNControlTimeRemaining.  Thus the management
                station may simply read the resulting reports repeatedly,
                checking the startTime and duration each time to ensure that a
                report was not missed or that the report parameters were not
                changed.
                
                While the value of this object is non-zero, it decrements
                by one per second until it reaches zero.  At the time
                that this object decrements to zero, the report is made
                accessible in the nlMatrixTopNTable, overwriting any report
                that may be there.
                
                When this object is modified by the management station, any
                associated entries in the nlMatrixTopNTable shall be deleted.
                
                (Note that this is a different algorithm than the one used in
                the hostTopNTable).
                ''',
                'nlmatrixtopncontroltimeremaining',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixTopNControlEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixTopNControlTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixTopNControlTable',
            False, 
            [
            _MetaInfoClassMember('nlMatrixTopNControlEntry', REFERENCE_LIST, 'NlMatrixTopNControlEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry', 
                [], [], 
                '''                A conceptual row in the nlMatrixTopNControlTable.
                
                An example of the indexing of this table is
                nlMatrixTopNControlDuration.3
                ''',
                'nlmatrixtopncontrolentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixTopNControlTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixTopNTable.NlMatrixTopNEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixTopNTable.NlMatrixTopNEntry',
            False, 
            [
            _MetaInfoClassMember('nlMatrixTopNControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'nlmatrixtopncontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixTopNIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in
                the nlMatrixTopNTable among those in the same report.
                
                
                
                
                
                This index is between 1 and N, where N is the
                number of entries in this report.
                
                If the value of nlMatrixTopNControlRateBase is equal to
                nlMatrixTopNPkts, increasing values of nlMatrixTopNIndex shall
                be assigned to entries with decreasing values of
                nlMatrixTopNPktRate until index N is assigned or there are no
                more nlMatrixTopNEntries.
                
                If the value of nlMatrixTopNControlRateBase is equal to
                nlMatrixTopNOctets, increasing values of nlMatrixTopNIndex
                shall be assigned to entries with decreasing values of
                nlMatrixTopNOctetRate until index N is assigned or there are
                no more nlMatrixTopNEntries.
                ''',
                'nlmatrixtopnindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('nlMatrixTopNDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network layer address of the destination host in this
                conversation.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the associated nlMatrixTopNProtocolDirLocalIndex.
                
                For example, if the nlMatrixTopNProtocolDirLocalIndex
                indicates an encapsulation of ip, this object is encoded as a
                length octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'nlmatrixtopndestaddress',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNOctetRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets seen from the source host
                to the destination host during this sampling interval, counted
                using the rules for counting the nlMatrixSDOctets object.  If
                the value of nlMatrixTopNControlRateBase is
                nlMatrixTopNOctets, this variable will be used to sort this
                report.
                ''',
                'nlmatrixtopnoctetrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNPktRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets seen from the source host
                to the destination host during this sampling interval, counted
                using the rules for counting the nlMatrixSDPkts object.
                If the value of nlMatrixTopNControlRateBase is
                nlMatrixTopNPkts, this variable will be used to sort this
                report.
                ''',
                'nlmatrixtopnpktrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNProtocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The protocolDirLocalIndex of the network layer protocol of
                this entry's network address.
                ''',
                'nlmatrixtopnprotocoldirlocalindex',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNReverseOctetRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets seen from the destination host to the
                source host during this sampling interval, counted
                using the rules for counting the nlMatrixDSOctets object (note
                that the corresponding nlMatrixSDOctets object selected is the
                one whose source address is equal to nlMatrixTopNDestAddress
                and whose destination address is equal to
                nlMatrixTopNSourceAddress.)
                
                Note that if the value of nlMatrixTopNControlRateBase is equal
                to nlMatrixTopNOctets, the sort of topN entries is based
                entirely on nlMatrixTopNOctetRate, and not on the value of
                this object.
                ''',
                'nlmatrixtopnreverseoctetrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNReversePktRate', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets seen from the destination host to the
                source host during this sampling interval, counted
                using the rules for counting the nlMatrixSDPkts object (note
                that the corresponding nlMatrixSDPkts object selected is the
                one whose source address is equal to nlMatrixTopNDestAddress
                and whose destination address is equal to
                nlMatrixTopNSourceAddress.)
                
                Note that if the value of nlMatrixTopNControlRateBase is equal
                to nlMatrixTopNPkts, the sort of topN entries is based
                entirely on nlMatrixTopNPktRate, and not on the value of this
                object.
                ''',
                'nlmatrixtopnreversepktrate',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The network layer address of the source host in this
                conversation.
                
                This is represented as an octet string with
                specific semantics and length as identified
                by the associated nlMatrixTopNProtocolDirLocalIndex.
                
                For example, if the protocolDirLocalIndex indicates an
                encapsulation of ip, this object is encoded as a length
                octet of 4, followed by the 4 octets of the ip address,
                in network byte order.
                ''',
                'nlmatrixtopnsourceaddress',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixTopNEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.NlMatrixTopNTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.NlMatrixTopNTable',
            False, 
            [
            _MetaInfoClassMember('nlMatrixTopNEntry', REFERENCE_LIST, 'NlMatrixTopNEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixTopNTable.NlMatrixTopNEntry', 
                [], [], 
                '''                A conceptual row in the nlMatrixTopNTable.
                
                The nlMatrixTopNControlIndex value in the index identifies the
                nlMatrixTopNControlEntry on whose behalf this entry was
                created.
                
                An example of the indexing of this table is
                nlMatrixTopNPktRate.3.10
                ''',
                'nlmatrixtopnentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'nlMatrixTopNTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProbeConfig.ProbeDownloadAction_Enum' : _MetaInfoEnum('ProbeDownloadAction_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'notDownloading':'NOTDOWNLOADING',
            'downloadToPROM':'DOWNLOADTOPROM',
            'downloadToRAM':'DOWNLOADTORAM',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.ProbeConfig.ProbeDownloadStatus_Enum' : _MetaInfoEnum('ProbeDownloadStatus_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'downloadSuccess':'DOWNLOADSUCCESS',
            'downloadStatusUnknown':'DOWNLOADSTATUSUNKNOWN',
            'downloadGeneralError':'DOWNLOADGENERALERROR',
            'downloadNoResponseFromServer':'DOWNLOADNORESPONSEFROMSERVER',
            'downloadChecksumError':'DOWNLOADCHECKSUMERROR',
            'downloadIncompatibleImage':'DOWNLOADINCOMPATIBLEIMAGE',
            'downloadTftpFileNotFound':'DOWNLOADTFTPFILENOTFOUND',
            'downloadTftpAccessViolation':'DOWNLOADTFTPACCESSVIOLATION',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.ProbeConfig.ProbeResetControl_Enum' : _MetaInfoEnum('ProbeResetControl_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'running':'RUNNING',
            'warmBoot':'WARMBOOT',
            'coldBoot':'COLDBOOT',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.ProbeConfig' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProbeConfig',
            False, 
            [
            _MetaInfoClassMember('netDefaultGateway', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP Address of the default gateway.  If this value is
                undefined or unknown, it shall have the value 0.0.0.0.
                ''',
                'netdefaultgateway',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeCapabilities', ATTRIBUTE, 'str' , None, None, 
                [(1, None)], [], 
                '''                An indication of the RMON MIB groups supported
                on at least one interface by this probe.
                ''',
                'probecapabilities',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeDateTime', ATTRIBUTE, 'str' , None, None, 
                [(0, None), (8, None), (11, None)], [], 
                '''                Probe's current date and time.
                
                field  octets  contents                  range
                -----  ------  --------                  -----
                  1      1-2   year                      0..65536
                  2       3    month                     1..12
                  3       4    day                       1..31
                  4       5    hour                      0..23
                  5       6    minutes                   0..59
                  6       7    seconds                   0..60
                                (use 60 for leap-second)
                  7       8    deci-seconds              0..9
                  8       9    direction from UTC        '+' / '-'
                  9      10    hours from UTC            0..11
                 10      11    minutes from UTC          0..59
                
                For example, Tuesday May 26, 1992 at 1:30:15 PM
                EDT would be displayed as:
                
                            1992-5-26,13:30:15.0,-4:0
                
                Note that if only local time is known, then
                timezone information (fields 8-10) is not
                present, and if no time information is known, the null
                string is returned.
                ''',
                'probedatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeDownloadAction', REFERENCE_ENUM_CLASS, 'ProbeDownloadAction_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProbeConfig.ProbeDownloadAction_Enum', 
                [], [], 
                '''                When this object is set to downloadToRAM(2) or
                downloadToPROM(3), the device will discontinue its
                normal operation and begin download of the image specified
                by probeDownloadFile from the server specified by
                probeDownloadTFTPServer using the TFTP protocol.  If
                downloadToRAM(2) is specified, the new image is copied
                to RAM only (the old image remains unaltered in the flash
                EPROM).  If downloadToPROM(3) is specified
                the new image is written to the flash EPROM
                memory after its checksum has been verified to be correct.
                When the download process is completed, the device will
                
                
                
                
                
                warm boot to restart the newly loaded application.
                When the device is not downloading, this object will have
                a value of notDownloading(1).
                ''',
                'probedownloadaction',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeDownloadFile', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The file name to be downloaded from the TFTP server when a
                download is next requested via this MIB.  This value is set to
                the zero length string when no file name has been specified.
                ''',
                'probedownloadfile',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeDownloadStatus', REFERENCE_ENUM_CLASS, 'ProbeDownloadStatus_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProbeConfig.ProbeDownloadStatus_Enum', 
                [], [], 
                '''                The status of the last download procedure, if any.  This
                object will have a value of downloadStatusUnknown(2) if no
                download process has been performed.
                ''',
                'probedownloadstatus',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeDownloadTFTPServer', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the TFTP server that contains the boot
                image to load when a download is next requested via this MIB.
                This value is set to `0.0.0.0' when no IP address has been
                specified.
                ''',
                'probedownloadtftpserver',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeHardwareRev', ATTRIBUTE, 'str' , None, None, 
                [(0, 31)], [], 
                '''                The hardware revision of this device.  This string will have
                a zero length if the revision is unknown.
                ''',
                'probehardwarerev',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeResetControl', REFERENCE_ENUM_CLASS, 'ProbeResetControl_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProbeConfig.ProbeResetControl_Enum', 
                [], [], 
                '''                Setting this object to warmBoot(2) causes the device to
                restart the application software with current configuration
                parameters saved in non-volatile memory.  Setting this
                object to coldBoot(3) causes the device to reinitialize
                configuration parameters in non-volatile memory to default
                values and restart the application software.  When the device
                is running normally, this variable has a value of
                running(1).
                ''',
                'proberesetcontrol',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeSoftwareRev', ATTRIBUTE, 'str' , None, None, 
                [(0, 15)], [], 
                '''                The software revision of this device.  This string will have
                a zero length if the revision is unknown.
                ''',
                'probesoftwarerev',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'probeConfig',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProtocolDir' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProtocolDir',
            False, 
            [
            _MetaInfoClassMember('protocolDirLastChange', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time the protocol directory
                was last modified, either through insertions or deletions,
                or through modifications of either the
                protocolDirAddressMapConfig, protocolDirHostConfig, or
                protocolDirMatrixConfig.
                ''',
                'protocoldirlastchange',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'protocolDir',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirAddressMapConfig_Enum' : _MetaInfoEnum('ProtocolDirAddressMapConfig_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'notSupported':'NOTSUPPORTED',
            'supportedOff':'SUPPORTEDOFF',
            'supportedOn':'SUPPORTEDON',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirHostConfig_Enum' : _MetaInfoEnum('ProtocolDirHostConfig_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'notSupported':'NOTSUPPORTED',
            'supportedOff':'SUPPORTEDOFF',
            'supportedOn':'SUPPORTEDON',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirMatrixConfig_Enum' : _MetaInfoEnum('ProtocolDirMatrixConfig_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'notSupported':'NOTSUPPORTED',
            'supportedOff':'SUPPORTEDOFF',
            'supportedOn':'SUPPORTEDON',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.ProtocolDirTable.ProtocolDirEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProtocolDirTable.ProtocolDirEntry',
            False, 
            [
            _MetaInfoClassMember('protocolDirID', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A unique identifier for a particular protocol.  Standard
                identifiers will be defined in a manner such that they
                can often be used as specifications for new protocols - i.e.
                a tree-structured assignment mechanism that matches the
                protocol encapsulation `tree' and which has algorithmic
                assignment mechanisms for certain subtrees. See RFC XXX for
                more details.
                
                Despite the algorithmic mechanism, the probe will only place
                entries in here for those protocols it chooses to collect.  In
                other words, it need not populate this table with all of the
                possible ethernet protocol types, nor need it create them on
                the fly when it sees them.  Whether or not it does these
                things is a matter of product definition (cost/benefit,
                usability), and is up to the designer of the product.
                
                If an entry is written to this table with a protocolDirID that
                the agent doesn't understand, either directly or
                algorithmically, the SET request will be rejected with an
                inconsistentName or badValue (for SNMPv1) error.
                ''',
                'protocoldirid',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirParameters', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                A set of parameters for the associated protocolDirID.
                See the associated RMON2 Protocol Identifiers document
                for a description of the possible parameters. There
                will be one octet in this string for each sub-identifier in
                the protocolDirID, and the parameters will appear here in the
                same order as the associated sub-identifiers appear in the
                protocolDirID.
                
                Every node in the protocolDirID tree has a different, optional
                set of parameters defined (that is, the definition of
                parameters for a node is optional).  The proper parameter
                value for each node is included in this string.  Note that the
                inclusion of a parameter value in this string for each node is
                not optional - what is optional is that a node may have no
                parameters defined, in which case the parameter field for that
                node will be zero.
                ''',
                'protocoldirparameters',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDirAddressMapConfig', REFERENCE_ENUM_CLASS, 'ProtocolDirAddressMapConfig_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirAddressMapConfig_Enum', 
                [], [], 
                '''                This object describes and configures the probe's support for
                address mapping for this protocol.  When the probe creates
                entries in this table for all protocols that it understands,
                it will set the entry to notSupported(1) if it doesn't have
                the capability to perform address mapping for the protocol or
                if this protocol is not a network-layer protocol.  When
                an entry is created in this table by a management operation as
                part of the limited extensibility feature, the probe must set
                this value to notSupported(1), because limited extensibility
                of the protocolDirTable does not extend to interpreting
                addresses of the extended protocols.
                
                If the value of this object is notSupported(1), the probe
                will not perform address mapping for this protocol and
                shall not allow this object to be changed to any other value.
                If the value of this object is supportedOn(3), the probe
                supports address mapping for this protocol and is configured
                to perform address mapping for this protocol for all
                addressMappingControlEntries and all interfaces.
                If the value of this object is supportedOff(2), the probe
                supports address mapping for this protocol but is configured
                to not perform address mapping for this protocol for any
                addressMappingControlEntries and all interfaces.
                Whenever this value changes from supportedOn(3) to
                supportedOff(2), the probe shall delete all related entries in
                the addressMappingTable.
                ''',
                'protocoldiraddressmapconfig',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirDescr', ATTRIBUTE, 'str' , None, None, 
                [(1, 64)], [], 
                '''                A textual description of the protocol encapsulation.
                A probe may choose to describe only a subset of the
                entire encapsulation (e.g. only the highest layer).
                
                This object is intended for human consumption only.
                
                This object may not be modified if the associated
                protocolDirStatus object is equal to active(1).
                ''',
                'protocoldirdescr',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirHostConfig', REFERENCE_ENUM_CLASS, 'ProtocolDirHostConfig_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirHostConfig_Enum', 
                [], [], 
                '''                This object describes and configures the probe's support for
                the network layer and application layer host tables for this
                protocol.  When the probe creates entries in this table for
                all protocols that it understands, it will set the entry to
                notSupported(1) if it doesn't have the capability to track the
                nlHostTable for this protocol or if the alHostTable is
                implemented but doesn't have the capability to track this
                protocol.  Note that if the alHostTable is implemented, the
                probe may only support a protocol if it is supported in both
                the nlHostTable and the alHostTable.
                
                
                
                
                
                If the associated protocolDirType object has the
                addressRecognitionCapable bit set, then this is a network
                layer protocol for which the probe recognizes addresses, and
                thus the probe will populate the nlHostTable and alHostTable
                with addresses it discovers for this protocol.
                
                If the value of this object is notSupported(1), the probe
                will not track the nlHostTable or alHostTable for this
                protocol and shall not allow this object to be changed to any
                other value. If the value of this object is supportedOn(3),
                the probe supports tracking of the nlHostTable and alHostTable
                for this protocol and is configured to track both tables
                for this protocol for all control entries and all interfaces.
                If the value of this object is supportedOff(2), the probe
                supports tracking of the nlHostTable and alHostTable for this
                protocol but is configured to not track these tables
                for any control entries or interfaces.
                Whenever this value changes from supportedOn(3) to
                supportedOff(2), the probe shall delete all related entries in
                the nlHostTable and alHostTable.
                
                Note that since each alHostEntry references 2 protocol
                directory entries, one for the network address and one for the
                type of the highest protocol recognized, that an entry will
                only be created in that table if this value is supportedOn(3)
                for both protocols.
                ''',
                'protocoldirhostconfig',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The locally arbitrary, but unique identifier associated
                with this protocolDir entry.
                
                The value for each supported protocol must remain constant at
                least from one re-initialization of the entity's network
                management system to the next re-initialization, except that
                if a protocol is deleted and re-created, it must be re-created
                with a new value that has not been used since the last
                re-initialization.
                
                The specific value is meaningful only within a given SNMP
                entity. A protocolDirLocalIndex must not be re-used until the
                next agent-restart in the event the protocol directory entry
                is deleted.
                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirMatrixConfig', REFERENCE_ENUM_CLASS, 'ProtocolDirMatrixConfig_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDirTable.ProtocolDirEntry.ProtocolDirMatrixConfig_Enum', 
                [], [], 
                '''                This object describes and configures the probe's support for
                the network layer and application layer matrix tables for this
                protocol.  When the probe creates entries in this table for
                all protocols that it understands, it will set the entry to
                notSupported(1) if it doesn't have the capability to track the
                nlMatrixTables for this protocol or if the alMatrixTables are
                implemented but don't have the capability to track this
                protocol.  Note that if the alMatrix tables are implemented,
                the probe may only support a protocol if it is supported in
                the the both of the nlMatrixTables and both of the
                alMatrixTables.
                
                
                
                
                
                If the associated protocolDirType object has the
                addressRecognitionCapable bit set, then this is a network
                layer protocol for which the probe recognizes addresses, and
                thus the probe will populate both of the nlMatrixTables and
                both of the alMatrixTables with addresses it discovers for
                this protocol.
                
                If the value of this object is notSupported(1), the probe
                will not track either of the nlMatrixTables or the
                alMatrixTables for this protocol and shall not allow this
                object to be changed to any other value. If the value of this
                object is supportedOn(3), the probe supports tracking of both
                of the nlMatrixTables and (if implemented) both of the
                alMatrixTables for this protocol and is configured to track
                these tables for this protocol for all control entries and all
                interfaces. If the value of this object is supportedOff(2),
                the probe supports tracking of both of the nlMatrixTables and
                (if implemented) both of the alMatrixTables for this protocol
                but is configured to not track these tables for this
                protocol for any control entries or interfaces.
                Whenever this value changes from supportedOn(3) to
                supportedOff(2), the probe shall delete all related entries in
                the nlMatrixTables and the alMatrixTables.
                
                Note that since each alMatrixEntry references 2 protocol
                directory entries, one for the network address and one for the
                type of the highest protocol recognized, that an entry will
                only be created in that table if this value is supportedOn(3)
                for both protocols.
                ''',
                'protocoldirmatrixconfig',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'protocoldirowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this protocol directory entry.
                
                An entry may not exist in the active state unless all
                
                
                
                
                
                objects in the entry have an appropriate value.
                
                If this object is not equal to active(1), all associated
                entries in the nlHostTable, nlMatrixSDTable, nlMatrixDSTable,
                alHostTable, alMatrixSDTable, and alMatrixDSTable shall be
                deleted.
                ''',
                'protocoldirstatus',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirType', ATTRIBUTE, 'str' , None, None, 
                [(1, None)], [], 
                '''                This object describes 2 attributes of this protocol
                directory entry.
                
                The presence or absence of the `extensible' bit describes
                whether or not this protocol directory entry can be extended
                
                
                
                
                
                by the user by creating protocol directory entries which are
                children of this protocol.
                
                An example of an entry that will often allow extensibility is
                `ip.udp'.  The probe may automatically populate some children
                of this node such as `ip.udp.snmp' and `ip.udp.dns'.
                A probe administrator or user may also populate additional
                children via remote SNMP requests that create entries in this
                table.  When a child node is added for a protocol for which the
                probe has no built in support, extending a parent node (for
                which the probe does have built in support),
                that child node is not extendible.  This is termed `limited
                extensibility'.
                
                When a child node is added through this extensibility
                mechanism, the values of protocolDirLocalIndex and
                protocolDirType shall be assigned by the agent.
                
                The other objects in the entry will be assigned by the
                manager who is creating the new entry.
                
                This object also describes whether or not this agent can
                recognize addresses for this protocol, should it be a network
                level protocol.  That is, while a probe may be able to
                recognize packets of a particular network layer protocol and
                count them, it takes additional logic to be able to recognize
                the addresses in this protocol and to populate network layer
                or application layer tables with the addresses in this
                protocol.  If this bit is set, the agent will recognize
                network layer addresses for this protoocl and populate the
                network and application layer host and matrix tables with
                these protocols.
                
                Note that when an entry is created, the agent will supply
                values for the bits that match the capabilities of the agent
                with respect to this protocol.  Note that since row creations
                usually exercise the limited extensibility feature, these
                bits will usually be set to zero.
                ''',
                'protocoldirtype',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'protocolDirEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProtocolDirTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProtocolDirTable',
            False, 
            [
            _MetaInfoClassMember('protocolDirEntry', REFERENCE_LIST, 'ProtocolDirEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDirTable.ProtocolDirEntry', 
                [], [], 
                '''                A conceptual row in the protocolDirTable.
                
                An example of the indexing of this entry is
                protocolDirLocalIndex.8.0.0.0.1.0.0.8.0.2.0.0, which is the
                encoding of a length of 8, followed by 8 subids encoding the
                protocolDirID of 1.2048, followed by a length of 2 and the
                2 subids encoding zero-valued parameters.
                ''',
                'protocoldirentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'protocolDirTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProtocolDistControlTable.ProtocolDistControlEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProtocolDistControlTable.ProtocolDistControlEntry',
            False, 
            [
            _MetaInfoClassMember('protocolDistControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                A unique index for this protocolDistControlEntry.
                ''',
                'protocoldistcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDistControlCreateTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this control entry was last
                activated. This can be used by the management station to
                ensure that the table has not been deleted and recreated
                between polls.
                ''',
                'protocoldistcontrolcreatetime',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDistControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The source of data for the this protocol distribution.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the
                identified interface.
                
                This object may not be modified if the associated
                protocolDistControlStatus object is equal to active(1).
                ''',
                'protocoldistcontroldatasource',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDistControlDroppedFrames', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of frames which were received by the probe
                and therefore not accounted for in the *StatsDropEvents, but
                for which the probe chose not to count for this entry for
                whatever reason.  Most often, this event occurs when the probe
                is out of some resources and decides to shed load from this
                collection.
                
                
                
                
                
                
                This count does not include packets that were not counted
                because they had MAC-layer errors.
                
                Note that, unlike the dropEvents counter, this number is the
                exact number of frames dropped.
                ''',
                'protocoldistcontroldroppedframes',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDistControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'protocoldistcontrolowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDistControlStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this row.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                
                If this object is not equal to active(1), all associated
                entries in the protocolDistStatsTable shall be deleted.
                ''',
                'protocoldistcontrolstatus',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'protocolDistControlEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProtocolDistControlTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProtocolDistControlTable',
            False, 
            [
            _MetaInfoClassMember('protocolDistControlEntry', REFERENCE_LIST, 'ProtocolDistControlEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDistControlTable.ProtocolDistControlEntry', 
                [], [], 
                '''                A conceptual row in the protocolDistControlTable.
                
                An example of the indexing of this entry is
                
                
                
                
                
                protocolDistControlDroppedFrames.7
                ''',
                'protocoldistcontrolentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'protocolDistControlTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProtocolDistStatsTable.ProtocolDistStatsEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProtocolDistStatsTable.ProtocolDistStatsEntry',
            False, 
            [
            _MetaInfoClassMember('protocolDirLocalIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                ''',
                'protocoldirlocalindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDistControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'protocoldistcontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('protocolDistStatsOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets in packets received of this protocol
                type since it was added to the protocolDistStatsTable
                (excluding framing bits but including FCS octets), except for
                those octets in packets that contained errors.
                
                Note this doesn't count just those octets in the particular
                protocol frames, but includes the entire packet that contained
                the protocol.
                ''',
                'protocoldiststatsoctets',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDistStatsPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors received of this
                protocol type.  Note that this is the number of link-layer
                packets, so if a single network-layer packet is fragmented
                into several link-layer frames, this counter is incremented
                several times.
                ''',
                'protocoldiststatspkts',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'protocolDistStatsEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.ProtocolDistStatsTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.ProtocolDistStatsTable',
            False, 
            [
            _MetaInfoClassMember('protocolDistStatsEntry', REFERENCE_LIST, 'ProtocolDistStatsEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDistStatsTable.ProtocolDistStatsEntry', 
                [], [], 
                '''                A conceptual row in the protocolDistStatsTable.
                
                The index is composed of the protocolDistControlIndex of the
                associated protocolDistControlEntry followed by the
                protocolDirLocalIndex of the associated protocol that this
                entry represents.  In other words, the index identifies the
                protocol distribution an entry is a part of as well as the
                particular protocol that it represents.
                
                An example of the indexing of this entry is
                protocolDistStatsPkts.1.18
                ''',
                'protocoldiststatsentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'protocolDistStatsTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialMode_Enum' : _MetaInfoEnum('SerialMode_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'direct':'DIRECT',
            'modem':'MODEM',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialProtocol_Enum' : _MetaInfoEnum('SerialProtocol_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'other':'OTHER',
            'slip':'SLIP',
            'ppp':'PPP',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.SerialConfigTable.SerialConfigEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.SerialConfigTable.SerialConfigEntry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                ''',
                'ifindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('serialDialoutTimeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                This timeout value is used when the probe initiates the
                serial connection with the intention of contacting a
                management station. This variable represents the number
                of seconds of inactivity allowed before terminating the
                connection on this serial interface.
                ''',
                'serialdialouttimeout',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialMode', REFERENCE_ENUM_CLASS, 'SerialMode_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialMode_Enum', 
                [], [], 
                '''                The type of incoming connection to expect on this serial
                interface.
                ''',
                'serialmode',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialModemConnectResp', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                An ASCII string containing substrings that describe the
                expected modem connection response code and associated bps
                rate.  The substrings are delimited by the first character
                in the string, for example:
                   /CONNECT/300/CONNECT 1200/1200/CONNECT 2400/2400/
                   CONNECT 4800/4800/CONNECT 9600/9600
                will be interpreted as:
                    response code    bps rate
                    CONNECT            300
                    CONNECT 1200      1200
                
                
                
                
                
                    CONNECT 2400      2400
                    CONNECT 4800      4800
                    CONNECT 9600      9600
                The agent will use the information in this string to adjust
                the bps rate of this serial interface once a modem connection
                is established.
                
                A value that is appropriate for a wide variety of modems is:
                '/CONNECT/300/CONNECT 1200/1200/CONNECT 2400/2400/
                 CONNECT 4800/4800/CONNECT 9600/9600/CONNECT 14400/14400/
                CONNECT 19200/19200/CONNECT 38400/38400/'.
                ''',
                'serialmodemconnectresp',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialModemHangUpString', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A control string which specifies how to disconnect a modem
                connection on this serial interface.  This object is only
                meaningful if the associated serialMode has the value
                of modem(2).
                A control string that is appropriate for a wide variety of
                modems is: '^d2^s+++^d2^sATH0^M^d2'.
                ''',
                'serialmodemhangupstring',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialModemInitString', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A control string which controls how a modem attached to this
                serial interface should be initialized.  The initialization
                is performed once during startup and again after each
                connection is terminated if the associated serialMode has the
                value of modem(2).
                
                A control string that is appropriate for a wide variety of
                modems is: '^s^MATE0Q0V1X4 S0=1 S2=43^M'.
                ''',
                'serialmodeminitstring',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialModemNoConnectResp', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                An ASCII string containing response codes that may be
                generated by a modem to report the reason why a connection
                attempt has failed.  The response codes are delimited by
                the first character in the string, for example:
                   /NO CARRIER/BUSY/NO DIALTONE/NO ANSWER/ERROR/
                If one of these response codes is received via this serial
                interface while attempting to make a modem connection,
                the agent will issue the hang up command as specified by
                serialModemHangUpString.
                
                A value that is appropriate for a wide variety of modems is:
                '/NO CARRIER/BUSY/NO DIALTONE/NO ANSWER/ERROR/'.
                ''',
                'serialmodemnoconnectresp',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialProtocol', REFERENCE_ENUM_CLASS, 'SerialProtocol_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.SerialConfigTable.SerialConfigEntry.SerialProtocol_Enum', 
                [], [], 
                '''                The type of data link encapsulation to be used on this
                serial interface.
                ''',
                'serialprotocol',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this serialConfigEntry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                ''',
                'serialstatus',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialTimeout', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                This timeout value is used when the Management Station has
                initiated the conversation over the serial link. This variable
                represents the number of seconds of inactivity allowed before
                terminating the connection on this serial interface. Use the
                
                
                
                
                
                serialDialoutTimeout in the case where the probe has initiated
                the connection for the purpose of sending a trap.
                ''',
                'serialtimeout',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'serialConfigEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.SerialConfigTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.SerialConfigTable',
            False, 
            [
            _MetaInfoClassMember('serialConfigEntry', REFERENCE_LIST, 'SerialConfigEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.SerialConfigTable.SerialConfigEntry', 
                [], [], 
                '''                A set of configuration parameters for a particular
                serial interface on this device. If the device has no serial
                interfaces, this table is empty.
                
                The index is composed of the ifIndex assigned to this serial
                line interface.
                ''',
                'serialconfigentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'serialConfigTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.SerialConnectionTable.SerialConnectionEntry.SerialConnectType_Enum' : _MetaInfoEnum('SerialConnectType_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'direct':'DIRECT',
            'modem':'MODEM',
            'switch':'SWITCH',
            'modemSwitch':'MODEMSWITCH',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.SerialConnectionTable.SerialConnectionEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.SerialConnectionTable.SerialConnectionEntry',
            False, 
            [
            _MetaInfoClassMember('serialConnectIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                A value that uniquely identifies this serialConnection
                entry.
                ''',
                'serialconnectindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('serialConnectDestIpAddress', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP Address that can be reached at the other end of this
                serial connection.
                This object may not be modified if the associated
                serialConnectStatus object is equal to active(1).
                ''',
                'serialconnectdestipaddress',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectDialString', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A control string which specifies how to dial the phone
                number in order to establish a modem connection.  The
                string should include dialing prefix and suffix.  For
                example: ``^s^MATD9,888-1234^M'' will instruct the Probe
                to send a carriage return followed by the dialing prefix
                ``ATD'', the phone number ``9,888-1234'', and a carriage
                return as the dialing suffix.
                This object may not be modified if the associated
                serialConnectStatus object is equal to active(1).
                ''',
                'serialconnectdialstring',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'serialconnectowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this serialConnectionEntry.
                
                If the manager attempts to set this object to active(1) when
                the serialConnectType is set to modem(2) or modem-switch(4)
                and the serialConnectDialString is a zero-length string or
                cannot be correctly parsed as a ConnectString, the set
                request will be rejected with badValue(3).
                
                If the manager attempts to set this object to active(1) when
                the serialConnectType is set to switch(3) or modem-switch(4)
                and the serialConnectSwitchConnectSeq,
                the serialConnectSwitchDisconnectSeq, or
                the serialConnectSwitchResetSeq are zero-length strings
                or cannot be correctly parsed as ConnectStrings, the set
                request will be rejected with badValue(3).
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                ''',
                'serialconnectstatus',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectSwitchConnectSeq', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A control string which specifies how to establish a
                data switch connection.
                This object may not be modified if the associated
                serialConnectStatus object is equal to active(1).
                ''',
                'serialconnectswitchconnectseq',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectSwitchDisconnectSeq', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A control string which specifies how to terminate a
                data switch connection.
                This object may not be modified if the associated
                
                
                
                
                
                serialConnectStatus object is equal to active(1).
                ''',
                'serialconnectswitchdisconnectseq',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectSwitchResetSeq', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                A control string which specifies how to reset a data
                switch in the event of a timeout.
                This object may not be modified if the associated
                serialConnectStatus object is equal to active(1).
                ''',
                'serialconnectswitchresetseq',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectType', REFERENCE_ENUM_CLASS, 'SerialConnectType_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.SerialConnectionTable.SerialConnectionEntry.SerialConnectType_Enum', 
                [], [], 
                '''                The type of outgoing connection to make.  If this object
                has the value direct(1), then a direct serial connection
                is assumed.  If this object has the value modem(2),
                then serialConnectDialString will be used to make a modem
                connection.  If this object has the value switch(3),
                
                
                
                
                
                then serialConnectSwitchConnectSeq will be used to establish
                the connection over a serial data switch, and
                serialConnectSwitchDisconnectSeq will be used to terminate
                the connection.  If this object has the value
                modem-switch(4), then a modem connection will be made first
                followed by the switch connection.
                
                This object may not be modified if the associated
                serialConnectStatus object is equal to active(1).
                ''',
                'serialconnecttype',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'serialConnectionEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.SerialConnectionTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.SerialConnectionTable',
            False, 
            [
            _MetaInfoClassMember('serialConnectionEntry', REFERENCE_LIST, 'SerialConnectionEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.SerialConnectionTable.SerialConnectionEntry', 
                [], [], 
                '''                Configuration for a SLIP link over a serial line.
                ''',
                'serialconnectionentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'serialConnectionTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.TrapDestTable.TrapDestEntry.TrapDestProtocol_Enum' : _MetaInfoEnum('TrapDestProtocol_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'ip':'IP',
            'ipx':'IPX',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.TrapDestTable.TrapDestEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.TrapDestTable.TrapDestEntry',
            False, 
            [
            _MetaInfoClassMember('trapDestIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                A value that uniquely identifies this trapDestEntry.
                ''',
                'trapdestindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('trapDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The address to send traps on behalf of this entry.
                
                If the associated trapDestProtocol object is equal to ip(1),
                the encoding of this object is the same as the snmpUDPAddress
                textual convention in [RFC1906]:
                  -- for a SnmpUDPAddress of length 6:
                  --
                  -- octets   contents        encoding
                  --  1-4     IP-address      network-byte order
                  --  5-6     UDP-port        network-byte order
                
                If the associated trapDestProtocol object is equal to ipx(2),
                the encoding of this object is the same as the snmpIPXAddress
                textual convention in [RFC1906]:
                  -- for a SnmpIPXAddress of length 12:
                  --
                  -- octets   contents            encoding
                  --  1-4     network-number      network-byte order
                  --  5-10    physical-address    network-byte order
                  -- 11-12    socket-number       network-byte order
                
                This object may not be modified if the associated
                
                
                
                
                
                trapDestStatus object is equal to active(1).
                ''',
                'trapdestaddress',
                'RMON2-MIB', False),
            _MetaInfoClassMember('trapDestCommunity', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                A community to which this destination address belongs.
                This entry is associated with any eventEntries in the RMON
                
                
                
                
                
                MIB whose value of eventCommunity is equal to the value of
                this object.  Every time an associated event entry sends a
                trap due to an event, that trap will be sent to each
                address in the trapDestTable with a trapDestCommunity equal to
                eventCommunity.
                
                This object may not be modified if the associated
                trapDestStatus object is equal to active(1).
                ''',
                'trapdestcommunity',
                'RMON2-MIB', False),
            _MetaInfoClassMember('trapDestOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'trapdestowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('trapDestProtocol', REFERENCE_ENUM_CLASS, 'TrapDestProtocol_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.TrapDestTable.TrapDestEntry.TrapDestProtocol_Enum', 
                [], [], 
                '''                The protocol with which to send this trap.
                ''',
                'trapdestprotocol',
                'RMON2-MIB', False),
            _MetaInfoClassMember('trapDestStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this trap destination entry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                ''',
                'trapdeststatus',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'trapDestEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.TrapDestTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.TrapDestTable',
            False, 
            [
            _MetaInfoClassMember('trapDestEntry', REFERENCE_LIST, 'TrapDestEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.TrapDestTable.TrapDestEntry', 
                [], [], 
                '''                This entry includes a destination IP address to which to send
                traps for this community.
                ''',
                'trapdestentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'trapDestTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.UsrHistoryControlTable.UsrHistoryControlEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.UsrHistoryControlTable.UsrHistoryControlEntry',
            False, 
            [
            _MetaInfoClassMember('usrHistoryControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                usrHistoryControlTable.  Each such entry defines a
                set of samples at a particular interval for a specified
                set of MIB instances available from the managed system.
                ''',
                'usrhistorycontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('usrHistoryControlBucketsGranted', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The number of discrete sampling intervals
                over which data shall be saved in the part of
                the usrHistoryTable associated with this
                usrHistoryControlEntry.
                
                When the associated usrHistoryControlBucketsRequested
                
                
                
                
                
                object is created or modified, the probe should set
                this object as closely to the requested value as is
                possible for the particular  probe implementation and
                available resources.  The probe must not lower this
                value except as a result of a modification to the associated
                usrHistoryControlBucketsRequested object.
                
                The associated usrHistoryControlBucketsRequested object
                should be set before or at the same time as this object
                to allow the probe to accurately estimate the resources
                required for this usrHistoryControlEntry.
                
                There will be times when the actual number of buckets
                associated with this entry is less than the value of
                this object.  In this case, at the end of each sampling
                interval, a new bucket will be added to the usrHistoryTable.
                
                When the number of buckets reaches the value of this object
                and a new bucket is to be added to the usrHistoryTable,
                the oldest bucket associated with this usrHistoryControlEntry
                shall be deleted by the agent so that the new bucket can be
                added.
                
                When the value of this object changes to a value less than
                the current value, entries are deleted from the
                usrHistoryTable associated with this usrHistoryControlEntry.
                Enough of the oldest of these entries shall be deleted by the
                agent so that their number remains less than or equal to the
                new value of this object.
                
                When the value of this object changes to a value greater
                than the current value, the number of associated usrHistory
                entries may be allowed to grow.
                ''',
                'usrhistorycontrolbucketsgranted',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryControlBucketsRequested', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The requested number of discrete time intervals
                over which data is to be saved in the part of the
                usrHistoryTable associated with this usrHistoryControlEntry.
                
                When this object is created or modified, the probe
                should set usrHistoryControlBucketsGranted as closely to
                this object as is possible for the particular probe
                implementation and available resources.
                ''',
                'usrhistorycontrolbucketsrequested',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryControlInterval', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                The interval in seconds over which the data is
                sampled for each bucket in the part of the usrHistory
                table associated with this usrHistoryControlEntry.
                
                Because the counters in a bucket may overflow at their
                maximum value with no indication, a prudent manager will
                take into account the possibility of overflow in any of
                
                
                
                
                
                the associated counters. It is important to consider the
                minimum time in which any counter could overflow on a
                particular media type and set the usrHistoryControlInterval
                object to a value less than this interval.
                
                This object may not be modified if the associated
                usrHistoryControlStatus object is equal to active(1).
                ''',
                'usrhistorycontrolinterval',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryControlObjects', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The number of MIB objects to be collected
                in the portion of usrHistoryTable associated with this
                usrHistoryControlEntry.
                
                This object may not be modified if the associated instance
                of usrHistoryControlStatus is equal to active(1).
                ''',
                'usrhistorycontrolobjects',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryControlOwner', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'usrhistorycontrolowner',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryControlStatus', REFERENCE_ENUM_CLASS, 'RowStatus_Enum' , 'ydk.models.snmpv2.SNMPv2_TC', 'RowStatus_Enum', 
                [], [], 
                '''                The status of this variable history control entry.
                
                An entry may not exist in the active state unless all
                objects in the entry have an appropriate value.
                
                If this object is not equal to active(1), all associated
                entries in the usrHistoryTable shall be deleted.
                ''',
                'usrhistorycontrolstatus',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'usrHistoryControlEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.UsrHistoryControlTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.UsrHistoryControlTable',
            False, 
            [
            _MetaInfoClassMember('usrHistoryControlEntry', REFERENCE_LIST, 'UsrHistoryControlEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryControlTable.UsrHistoryControlEntry', 
                [], [], 
                '''                A list of parameters that set up a group of user-defined
                MIB objects to be sampled periodically (called a
                bucket-group).
                
                For example, an instance of usrHistoryControlInterval
                might be named usrHistoryControlInterval.1
                ''',
                'usrhistorycontrolentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'usrHistoryControlTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry.UsrHistoryObjectSampleType_Enum' : _MetaInfoEnum('UsrHistoryObjectSampleType_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'absoluteValue':'ABSOLUTEVALUE',
            'deltaValue':'DELTAVALUE',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry',
            False, 
            [
            _MetaInfoClassMember('usrHistoryControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'usrhistorycontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('usrHistoryObjectIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index used to uniquely identify an entry in the
                usrHistoryObject table.  Each such entry defines a
                MIB instance to be collected periodically.
                ''',
                'usrhistoryobjectindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('usrHistoryObjectSampleType', REFERENCE_ENUM_CLASS, 'UsrHistoryObjectSampleType_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry.UsrHistoryObjectSampleType_Enum', 
                [], [], 
                '''                The method of sampling the selected variable for storage in
                the usrHistoryTable.
                
                If the value of this object is absoluteValue(1), the value of
                the selected variable will be copied directly into the history
                bucket.
                
                If the value of this object is deltaValue(2), the value of the
                selected variable at the last sample will be subtracted from
                the current value, and the difference will be stored in the
                history bucket. If the associated usrHistoryObjectVariable
                instance could not be obtained at the previous sample
                interval, then a delta sample is not possible, and the value
                of the associated usrHistoryValStatus object for this interval
                will be valueNotAvailable(1).
                
                This object may not be modified if the associated
                usrHistoryControlStatus object is equal to active(1).
                ''',
                'usrhistoryobjectsampletype',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryObjectVariable', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier of the particular variable to be
                sampled.
                
                Only variables that resolve to an ASN.1 primitive type of
                Integer32 (Integer32, Counter, Gauge, or TimeTicks) may be
                sampled.
                
                Because SNMP access control is articulated entirely in terms
                of the contents of MIB views, no access control mechanism
                exists that can restrict the value of this object to identify
                only those objects that exist in a particular MIB view.
                Because there is thus no acceptable means of restricting the
                read access that could be obtained through the user history
                
                
                
                
                
                mechanism, the probe must only grant write access to this
                object in those views that have read access to all objects on
                the probe.
                
                During a set operation, if the supplied variable name is not
                available in the selected MIB view, a badValue error must be
                returned.
                
                This object may not be modified if the associated
                usrHistoryControlStatus object is equal to active(1).
                ''',
                'usrhistoryobjectvariable',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'usrHistoryObjectEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.UsrHistoryObjectTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.UsrHistoryObjectTable',
            False, 
            [
            _MetaInfoClassMember('usrHistoryObjectEntry', REFERENCE_LIST, 'UsrHistoryObjectEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry', 
                [], [], 
                '''                A list of MIB instances to be sampled periodically.
                
                Entries in this table are created when an associated
                usrHistoryControlObjects object is created.
                
                The usrHistoryControlIndex value in the index is
                that of the associated usrHistoryControlEntry.
                
                For example, an instance of usrHistoryObjectVariable might be
                usrHistoryObjectVariable.1.3
                ''',
                'usrhistoryobjectentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'usrHistoryObjectTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.UsrHistoryTable.UsrHistoryEntry.UsrHistoryValStatus_Enum' : _MetaInfoEnum('UsrHistoryValStatus_Enum', 'ydk.models.rmon2.RMON2_MIB',
        {
            'valueNotAvailable':'VALUENOTAVAILABLE',
            'valuePositive':'VALUEPOSITIVE',
            'valueNegative':'VALUENEGATIVE',
        }, 'RMON2-MIB', _yang_ns._namespaces['RMON2-MIB']),
    'RMON2MIB.UsrHistoryTable.UsrHistoryEntry' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.UsrHistoryTable.UsrHistoryEntry',
            False, 
            [
            _MetaInfoClassMember('usrHistoryControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'usrhistorycontrolindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('usrHistoryObjectIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                ''',
                'usrhistoryobjectindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('usrHistorySampleIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 2147483647)], [], 
                '''                An index that uniquely identifies the particular sample this
                entry represents among all samples associated with the same
                usrHistoryControlEntry. This index starts at 1 and increases
                by one as each new sample is taken.
                ''',
                'usrhistorysampleindex',
                'RMON2-MIB', True),
            _MetaInfoClassMember('usrHistoryAbsValue', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The absolute value (i.e. unsigned value) of the
                user-specified statistic during the last sampling period. The
                value during the current sampling period is not made available
                until the period is completed.
                
                To obtain the true value for this sampling interval, the
                associated instance of usrHistoryValStatus must be checked,
                and usrHistoryAbsValue adjusted as necessary.
                
                If the MIB instance could not be accessed during the sampling
                interval, then this object will have a value of zero and the
                associated instance of usrHistoryValStatus will be set to
                'valueNotAvailable(1)'.
                ''',
                'usrhistoryabsvalue',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryIntervalEnd', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the end of the interval over which
                this sample was measured.
                ''',
                'usrhistoryintervalend',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryIntervalStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the start of the interval over
                which this sample was measured.  If the probe keeps track of
                the time of day, it should start the first sample of the
                history at a time such that when the next hour of the day
                begins, a sample is started at that instant.
                
                Note that following this rule may require the probe to delay
                collecting the first sample of the history, as each sample
                must be of the same interval. Also note that the sample which
                is currently being collected is not accessible in this table
                until the end of its interval.
                ''',
                'usrhistoryintervalstart',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryValStatus', REFERENCE_ENUM_CLASS, 'UsrHistoryValStatus_Enum' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryTable.UsrHistoryEntry.UsrHistoryValStatus_Enum', 
                [], [], 
                '''                This object indicates the validity and sign of the data in
                the associated instance of usrHistoryAbsValue.
                
                If the MIB instance could not be accessed during the sampling
                interval, then 'valueNotAvailable(1)' will be returned.
                
                If the sample is valid and actual value of the sample is
                greater than or equal to zero then 'valuePositive(2)' is
                returned.
                
                If the sample is valid and the actual value of the sample is
                less than zero, 'valueNegative(3)' will be returned. The
                associated instance of usrHistoryAbsValue should be multiplied
                by -1 to obtain the true sample value.
                ''',
                'usrhistoryvalstatus',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'usrHistoryEntry',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB.UsrHistoryTable' : {
        'meta_info' : _MetaInfoClass('RMON2MIB.UsrHistoryTable',
            False, 
            [
            _MetaInfoClassMember('usrHistoryEntry', REFERENCE_LIST, 'UsrHistoryEntry' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryTable.UsrHistoryEntry', 
                [], [], 
                '''                A historical sample of user-defined variables.  This sample
                is associated with the usrHistoryControlEntry which set up the
                parameters for a regular collection of these samples.
                
                The usrHistoryControlIndex value in the index identifies the
                usrHistoryControlEntry on whose behalf this entry was created.
                
                The usrHistoryObjectIndex value in the index identifies the
                usrHistoryObjectEntry on whose behalf this entry was created.
                
                For example, an instance of usrHistoryAbsValue, which represents
                the 14th sample of a variable collected as specified by
                usrHistoryControlEntry.1 and usrHistoryObjectEntry.1.5,
                would be named usrHistoryAbsValue.1.14.5
                ''',
                'usrhistoryentry',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'usrHistoryTable',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
    'RMON2MIB' : {
        'meta_info' : _MetaInfoClass('RMON2MIB',
            False, 
            [
            _MetaInfoClassMember('addressMap', REFERENCE_CLASS, 'AddressMap' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AddressMap', 
                [], [], 
                '''                ''',
                'addressmap',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapControlTable', REFERENCE_CLASS, 'AddressMapControlTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AddressMapControlTable', 
                [], [], 
                '''                A table to control the collection of network layer address to
                physical address to interface mappings.
                
                Note that this is not like the typical RMON
                controlTable and dataTable in which each entry creates
                its own data table.  Each entry in this table enables the
                discovery of addresses on a new interface and the placement
                of address mappings into the central addressMapTable.
                
                Implementations are encouraged to add an entry per monitored
                interface upon initialization so that a default collection
                of address mappings is available.
                ''',
                'addressmapcontroltable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('addressMapTable', REFERENCE_CLASS, 'AddressMapTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AddressMapTable', 
                [], [], 
                '''                A table of network layer address to physical address to
                interface mappings.
                
                The probe will add entries to this table based on the source
                MAC and network addresses seen in packets without MAC-level
                errors. The probe will populate this table for all protocols
                in the protocol directory table whose value of
                protocolDirAddressMapConfig is equal to supportedOn(3), and
                will delete any entries whose protocolDirEntry is deleted or
                has a protocolDirAddressMapConfig value of supportedOff(2).
                ''',
                'addressmaptable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alHostTable', REFERENCE_CLASS, 'AlHostTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlHostTable', 
                [], [], 
                '''                A collection of statistics for a particular protocol from a
                particular network address that has been discovered on an
                interface of this device.
                
                The probe will populate this table for all protocols in the
                protocol directory table whose value of
                protocolDirHostConfig is equal to supportedOn(3), and
                will delete any entries whose protocolDirEntry is deleted or
                has a protocolDirHostConfig value of supportedOff(2).
                
                The probe will add to this table all addresses
                seen as the source or destination address in all packets with
                no MAC errors, and will increment octet and packet counts in
                the table for all packets with no MAC errors.  Further,
                entries will only be added to this table if their address
                exists in the nlHostTable and will be deleted from this table
                if their address is deleted from the nlHostTable.
                ''',
                'alhosttable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixDSTable', REFERENCE_CLASS, 'AlMatrixDSTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixDSTable', 
                [], [], 
                '''                A list of application traffic matrix entries which collect
                statistics for conversations of a particular protocol between
                two network-level addresses.  This table is indexed first by
                the destination address and then by the source address to make
                it convenient to collect all statistics to a particular
                address.
                
                The probe will populate this table for all protocols in the
                protocol directory table whose value of
                protocolDirMatrixConfig is equal to supportedOn(3), and
                will delete any entries whose protocolDirEntry is deleted or
                has a protocolDirMatrixConfig value of supportedOff(2).
                
                The probe will add to this table all pairs of addresses for
                all protocols seen in all packets with no MAC errors, and will
                increment octet and packet counts in the table for all packets
                with no MAC errors.  Further, entries will only be added to
                this table if their address pair exists in the nlMatrixDSTable
                and will be deleted from this table if the address pair is
                deleted from the nlMatrixDSTable.
                ''',
                'almatrixdstable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixSDTable', REFERENCE_CLASS, 'AlMatrixSDTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixSDTable', 
                [], [], 
                '''                A list of application traffic matrix entries which collect
                
                
                
                
                
                statistics for conversations of a particular protocol between
                two network-level addresses.  This table is indexed first by
                the source address and then by the destination address to make
                it convenient to collect all statistics from a particular
                address.
                
                The probe will populate this table for all protocols in the
                protocol directory table whose value of
                protocolDirMatrixConfig is equal to supportedOn(3), and
                will delete any entries whose protocolDirEntry is deleted or
                has a protocolDirMatrixConfig value of supportedOff(2).
                
                The probe will add to this table all pairs of addresses for
                all protocols seen in all packets with no MAC errors, and will
                increment octet and packet counts in the table for all packets
                with no MAC errors.  Further, entries will only be added to
                this table if their address pair exists in the nlMatrixSDTable
                and will be deleted from this table if the address pair is
                deleted from the nlMatrixSDTable.
                ''',
                'almatrixsdtable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNControlTable', REFERENCE_CLASS, 'AlMatrixTopNControlTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixTopNControlTable', 
                [], [], 
                '''                A set of parameters that control the creation of a
                report of the top N matrix entries according to
                a selected metric.
                ''',
                'almatrixtopncontroltable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('alMatrixTopNTable', REFERENCE_CLASS, 'AlMatrixTopNTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.AlMatrixTopNTable', 
                [], [], 
                '''                A set of statistics for those application layer matrix
                entries that have counted the highest number of octets or
                packets.
                ''',
                'almatrixtopntable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlHostControlTable', REFERENCE_CLASS, 'HlHostControlTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.HlHostControlTable', 
                [], [], 
                '''                A list of higher layer (i.e. non-MAC) host table control entries.
                
                These entries will enable the collection of the network and
                application level host tables indexed by network addresses.
                Both the network and application level host tables are
                controlled by this table is so that they will both be created
                and deleted at the same time, further increasing the ease with
                which they can be implemented as a single datastore (note that
                if an implementation stores application layer host records in
                memory, it can derive network layer host records from them).
                
                Entries in the nlHostTable will be created on behalf of each
                entry in this table. Additionally, if this probe implements
                the alHostTable, entries in the alHostTable will be created on
                behalf of each entry in this table.
                
                Implementations are encouraged to add an entry per monitored
                interface upon initialization so that a default collection
                of host statistics is available.
                ''',
                'hlhostcontroltable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('hlMatrixControlTable', REFERENCE_CLASS, 'HlMatrixControlTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.HlMatrixControlTable', 
                [], [], 
                '''                A list of higher layer (i.e. non-MAC) matrix control entries.
                
                These entries will enable the collection of the network and
                application level matrix tables containing conversation
                statistics indexed by pairs of network addresses.
                Both the network and application level matrix tables are
                controlled by this table is so that they will both be created
                and deleted at the same time, further increasing the ease with
                which they can be implemented as a single datastore (note that
                if an implementation stores application layer matrix records
                in memory, it can derive network layer matrix records from
                them).
                
                Entries in the nlMatrixSDTable and nlMatrixDSTable will be
                created on behalf of each entry in this table.  Additionally,
                if this probe implements the alMatrix tables, entries in the
                alMatrix tables will be created on behalf of each entry in
                this table.
                ''',
                'hlmatrixcontroltable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('netConfigTable', REFERENCE_CLASS, 'NetConfigTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NetConfigTable', 
                [], [], 
                '''                A table of netConfigEntries.
                ''',
                'netconfigtable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlHostTable', REFERENCE_CLASS, 'NlHostTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlHostTable', 
                [], [], 
                '''                A collection of statistics for a particular network layer
                address that has been discovered on an interface of this
                device.
                
                The probe will populate this table for all network layer
                protocols in the protocol directory table whose value of
                protocolDirHostConfig is equal to supportedOn(3), and
                will delete any entries whose protocolDirEntry is deleted or
                has a protocolDirHostConfig value of supportedOff(2).
                
                The probe will add to this table all addresses seen
                as the source or destination address in all packets with no
                MAC errors, and will increment octet and packet counts in the
                table for all packets with no MAC errors.
                ''',
                'nlhosttable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixDSTable', REFERENCE_CLASS, 'NlMatrixDSTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixDSTable', 
                [], [], 
                '''                A list of traffic matrix entries which collect statistics for
                conversations between two network-level addresses.  This table
                is indexed first by the destination address and then by the
                source address to make it convenient to collect all
                conversations to a particular address.
                
                The probe will populate this table for all network layer
                protocols in the protocol directory table whose value of
                protocolDirMatrixConfig is equal to supportedOn(3), and
                will delete any entries whose protocolDirEntry is deleted or
                has a protocolDirMatrixConfig value of supportedOff(2).
                
                The probe will add to this table all pairs of addresses
                seen in all packets with no MAC errors, and will increment
                
                
                
                
                
                octet and packet counts in the table for all packets with no
                MAC errors.
                
                Further, this table will only contain entries that have a
                corresponding entry in the nlMatrixSDTable with the same
                source address and destination address.
                ''',
                'nlmatrixdstable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixSDTable', REFERENCE_CLASS, 'NlMatrixSDTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixSDTable', 
                [], [], 
                '''                A list of traffic matrix entries which collect statistics for
                conversations between two network-level addresses.  This table
                is indexed first by the source address and then by the
                destination address to make it convenient to collect all
                conversations from a particular address.
                
                The probe will populate this table for all network layer
                protocols in the protocol directory table whose value of
                protocolDirMatrixConfig is equal to supportedOn(3), and
                will delete any entries whose protocolDirEntry is deleted or
                has a protocolDirMatrixConfig value of supportedOff(2).
                
                
                
                
                
                The probe will add to this table all pairs of addresses
                seen in all packets with no MAC errors, and will increment
                octet and packet counts in the table for all packets with no
                MAC errors.
                
                Further, this table will only contain entries that have a
                corresponding entry in the nlMatrixDSTable with the same
                source address and destination address.
                ''',
                'nlmatrixsdtable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNControlTable', REFERENCE_CLASS, 'NlMatrixTopNControlTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixTopNControlTable', 
                [], [], 
                '''                A set of parameters that control the creation of a
                report of the top N matrix entries according to
                a selected metric.
                ''',
                'nlmatrixtopncontroltable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('nlMatrixTopNTable', REFERENCE_CLASS, 'NlMatrixTopNTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.NlMatrixTopNTable', 
                [], [], 
                '''                A set of statistics for those network layer matrix entries
                that have counted the highest number of octets or packets.
                ''',
                'nlmatrixtopntable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('probeConfig', REFERENCE_CLASS, 'ProbeConfig' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProbeConfig', 
                [], [], 
                '''                ''',
                'probeconfig',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDir', REFERENCE_CLASS, 'ProtocolDir' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDir', 
                [], [], 
                '''                ''',
                'protocoldir',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDirTable', REFERENCE_CLASS, 'ProtocolDirTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDirTable', 
                [], [], 
                '''                This table lists the protocols that this agent has the
                capability to decode and count.  There is one entry in this
                table for each such protocol.  These protocols represent
                different network layer, transport layer, and higher-layer
                protocols.  The agent should boot up with this table
                preconfigured with those protocols that it knows about and
                wishes to monitor.  Implementations are strongly encouraged to
                support protocols higher than the network layer (at least for
                the protocol distribution group), even for implementations
                that don't support the application layer groups.
                ''',
                'protocoldirtable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDistControlTable', REFERENCE_CLASS, 'ProtocolDistControlTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDistControlTable', 
                [], [], 
                '''                Controls the setup of protocol type distribution statistics
                tables.
                
                Implementations are encouraged to add an entry per monitored
                interface upon initialization so that a default collection
                of protocol statistics is available.
                
                Rationale:
                This table controls collection of very basic statistics
                for any or all of the protocols detected on a given interface.
                An NMS can use this table to quickly determine bandwidth
                allocation utilized by different protocols.
                
                A media-specific statistics collection could also
                be configured (e.g. etherStats, trPStats) to easily obtain
                total frame, octet, and droppedEvents for the same
                interface.
                ''',
                'protocoldistcontroltable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('protocolDistStatsTable', REFERENCE_CLASS, 'ProtocolDistStatsTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.ProtocolDistStatsTable', 
                [], [], 
                '''                An entry is made in this table for every protocol in the
                
                
                
                
                
                protocolDirTable which has been seen in at least one packet.
                Counters are updated in this table for every protocol type
                that is encountered when parsing a packet, but no counters are
                updated for packets with MAC-layer errors.
                
                Note that if a protocolDirEntry is deleted, all associated
                entries in this table are removed.
                ''',
                'protocoldiststatstable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConfigTable', REFERENCE_CLASS, 'SerialConfigTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.SerialConfigTable', 
                [], [], 
                '''                A table of serial interface configuration entries.  This data
                will be stored in non-volatile memory and preserved across
                probe resets or power loss.
                ''',
                'serialconfigtable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('serialConnectionTable', REFERENCE_CLASS, 'SerialConnectionTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.SerialConnectionTable', 
                [], [], 
                '''                A list of serialConnectionEntries.
                ''',
                'serialconnectiontable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('trapDestTable', REFERENCE_CLASS, 'TrapDestTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.TrapDestTable', 
                [], [], 
                '''                A list of trap destination entries.
                ''',
                'trapdesttable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryControlTable', REFERENCE_CLASS, 'UsrHistoryControlTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryControlTable', 
                [], [], 
                '''                A list of data-collection configuration entries.
                ''',
                'usrhistorycontroltable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryObjectTable', REFERENCE_CLASS, 'UsrHistoryObjectTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryObjectTable', 
                [], [], 
                '''                A list of data-collection configuration entries.
                ''',
                'usrhistoryobjecttable',
                'RMON2-MIB', False),
            _MetaInfoClassMember('usrHistoryTable', REFERENCE_CLASS, 'UsrHistoryTable' , 'ydk.models.rmon2.RMON2_MIB', 'RMON2MIB.UsrHistoryTable', 
                [], [], 
                '''                A list of user defined history entries.
                ''',
                'usrhistorytable',
                'RMON2-MIB', False),
            ],
            'RMON2-MIB',
            'RMON2-MIB',
            _yang_ns._namespaces['RMON2-MIB'],
        'ydk.models.rmon2.RMON2_MIB'
        ),
    },
}
_meta_table['RMON2MIB.AddressMapControlTable.AddressMapControlEntry']['meta_info'].parent =_meta_table['RMON2MIB.AddressMapControlTable']['meta_info']
_meta_table['RMON2MIB.AddressMapTable.AddressMapEntry']['meta_info'].parent =_meta_table['RMON2MIB.AddressMapTable']['meta_info']
_meta_table['RMON2MIB.AlHostTable.AlHostEntry']['meta_info'].parent =_meta_table['RMON2MIB.AlHostTable']['meta_info']
_meta_table['RMON2MIB.AlMatrixDSTable.AlMatrixDSEntry']['meta_info'].parent =_meta_table['RMON2MIB.AlMatrixDSTable']['meta_info']
_meta_table['RMON2MIB.AlMatrixSDTable.AlMatrixSDEntry']['meta_info'].parent =_meta_table['RMON2MIB.AlMatrixSDTable']['meta_info']
_meta_table['RMON2MIB.AlMatrixTopNControlTable.AlMatrixTopNControlEntry']['meta_info'].parent =_meta_table['RMON2MIB.AlMatrixTopNControlTable']['meta_info']
_meta_table['RMON2MIB.AlMatrixTopNTable.AlMatrixTopNEntry']['meta_info'].parent =_meta_table['RMON2MIB.AlMatrixTopNTable']['meta_info']
_meta_table['RMON2MIB.HlHostControlTable.HlHostControlEntry']['meta_info'].parent =_meta_table['RMON2MIB.HlHostControlTable']['meta_info']
_meta_table['RMON2MIB.HlMatrixControlTable.HlMatrixControlEntry']['meta_info'].parent =_meta_table['RMON2MIB.HlMatrixControlTable']['meta_info']
_meta_table['RMON2MIB.NetConfigTable.NetConfigEntry']['meta_info'].parent =_meta_table['RMON2MIB.NetConfigTable']['meta_info']
_meta_table['RMON2MIB.NlHostTable.NlHostEntry']['meta_info'].parent =_meta_table['RMON2MIB.NlHostTable']['meta_info']
_meta_table['RMON2MIB.NlMatrixDSTable.NlMatrixDSEntry']['meta_info'].parent =_meta_table['RMON2MIB.NlMatrixDSTable']['meta_info']
_meta_table['RMON2MIB.NlMatrixSDTable.NlMatrixSDEntry']['meta_info'].parent =_meta_table['RMON2MIB.NlMatrixSDTable']['meta_info']
_meta_table['RMON2MIB.NlMatrixTopNControlTable.NlMatrixTopNControlEntry']['meta_info'].parent =_meta_table['RMON2MIB.NlMatrixTopNControlTable']['meta_info']
_meta_table['RMON2MIB.NlMatrixTopNTable.NlMatrixTopNEntry']['meta_info'].parent =_meta_table['RMON2MIB.NlMatrixTopNTable']['meta_info']
_meta_table['RMON2MIB.ProtocolDirTable.ProtocolDirEntry']['meta_info'].parent =_meta_table['RMON2MIB.ProtocolDirTable']['meta_info']
_meta_table['RMON2MIB.ProtocolDistControlTable.ProtocolDistControlEntry']['meta_info'].parent =_meta_table['RMON2MIB.ProtocolDistControlTable']['meta_info']
_meta_table['RMON2MIB.ProtocolDistStatsTable.ProtocolDistStatsEntry']['meta_info'].parent =_meta_table['RMON2MIB.ProtocolDistStatsTable']['meta_info']
_meta_table['RMON2MIB.SerialConfigTable.SerialConfigEntry']['meta_info'].parent =_meta_table['RMON2MIB.SerialConfigTable']['meta_info']
_meta_table['RMON2MIB.SerialConnectionTable.SerialConnectionEntry']['meta_info'].parent =_meta_table['RMON2MIB.SerialConnectionTable']['meta_info']
_meta_table['RMON2MIB.TrapDestTable.TrapDestEntry']['meta_info'].parent =_meta_table['RMON2MIB.TrapDestTable']['meta_info']
_meta_table['RMON2MIB.UsrHistoryControlTable.UsrHistoryControlEntry']['meta_info'].parent =_meta_table['RMON2MIB.UsrHistoryControlTable']['meta_info']
_meta_table['RMON2MIB.UsrHistoryObjectTable.UsrHistoryObjectEntry']['meta_info'].parent =_meta_table['RMON2MIB.UsrHistoryObjectTable']['meta_info']
_meta_table['RMON2MIB.UsrHistoryTable.UsrHistoryEntry']['meta_info'].parent =_meta_table['RMON2MIB.UsrHistoryTable']['meta_info']
_meta_table['RMON2MIB.AddressMap']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.AddressMapControlTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.AddressMapTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.AlHostTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.AlMatrixDSTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.AlMatrixSDTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.AlMatrixTopNControlTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.AlMatrixTopNTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.HlHostControlTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.HlMatrixControlTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.NetConfigTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.NlHostTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.NlMatrixDSTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.NlMatrixSDTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.NlMatrixTopNControlTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.NlMatrixTopNTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.ProbeConfig']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.ProtocolDir']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.ProtocolDirTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.ProtocolDistControlTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.ProtocolDistStatsTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.SerialConfigTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.SerialConnectionTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.TrapDestTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.UsrHistoryControlTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.UsrHistoryObjectTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
_meta_table['RMON2MIB.UsrHistoryTable']['meta_info'].parent =_meta_table['RMON2MIB']['meta_info']
