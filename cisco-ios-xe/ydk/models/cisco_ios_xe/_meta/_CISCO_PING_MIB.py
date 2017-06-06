


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoPingMib.Ciscopingtable.Ciscopingentry' : {
        'meta_info' : _MetaInfoClass('CiscoPingMib.Ciscopingtable.Ciscopingentry',
            False, 
            [
            _MetaInfoClassMember('ciscoPingSerialNumber', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Object which specifies a unique entry in the
                ciscoPingTable.  A management station wishing
                to initiate a ping operation should use a
                pseudo-random value for this object when creating
                or modifying an instance of a ciscoPingEntry.
                The RowStatus semantics of the ciscoPingEntryStatus
                object will prevent access conflicts.
                ''',
                'ciscopingserialnumber',
                'CISCO-PING-MIB', True),
            _MetaInfoClassMember('ciscoPingAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The address of the device to be pinged.
                An instance of this object cannot be created until the
                associated instance of ciscoPingProtocol is created.
                ''',
                'ciscopingaddress',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingAvgRtt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The average round trip time of all the packets that have
                been sent in this sequence.
                
                This object will not be created until the first ping
                response in a sequence is received.
                ''',
                'ciscopingavgrtt',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingCompleted', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Set to true when all the packets in this sequence have been
                either responded to or timed out.
                ''',
                'ciscopingcompleted',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                Specifies the minimum amount of time to wait before sending
                the next packet in a sequence after receiving a response or
                declaring a timeout for a previous packet.  The actual delay
                may be greater due to internal task scheduling.
                ''',
                'ciscopingdelay',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingEntryOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry.
                ''',
                'ciscopingentryowner',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingEntryStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this table entry.  Once the entry status is
                set to active, the associate entry cannot be modified until
                the sequence completes (ciscoPingCompleted is true).
                ''',
                'ciscopingentrystatus',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingMaxRtt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum round trip time of all the packets that have
                been sent in this sequence.
                
                This object will not be created until the first ping
                response in a sequence is received.
                ''',
                'ciscopingmaxrtt',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingMinRtt', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The minimum round trip time of all the packets that have
                been sent in this sequence.
                
                This object will not be created until the first ping
                response in a sequence is received.
                ''',
                'ciscopingminrtt',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingPacketCount', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                Specifies the number of ping packets to send to the target
                in this sequence.
                ''',
                'ciscopingpacketcount',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingPacketSize', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Specifies the size of ping packets to send to the target
                in this sequence.  The lower and upper boundaries of this
                object are protocol-dependent.
                An instance of this object cannot be modified unless the
                associated instance of ciscoPingProtocol has been created
                (so as to allow protocol-specific range checking on the
                new value).
                ''',
                'ciscopingpacketsize',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingPacketTimeout', ATTRIBUTE, 'int' , None, None, 
                [('0', '3600000')], [], 
                '''                Specifies the amount of time to wait for a response to a
                transmitted packet before declaring the packet 'dropped.'
                ''',
                'ciscopingpackettimeout',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingProtocol', REFERENCE_ENUM_CLASS, 'CisconetworkprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_TC', 'CisconetworkprotocolEnum', 
                [], [], 
                '''                The protocol to use.
                Once an instance of this object is created, its
                value can not be changed.
                ''',
                'ciscopingprotocol',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingReceivedPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ping packets that have been received from the
                target in this sequence.
                ''',
                'ciscopingreceivedpackets',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingSentPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of ping packets that have been sent to the target
                in this sequence.
                ''',
                'ciscopingsentpackets',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingTrapOnCompletion', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                Specifies whether or not a ciscoPingCompletion trap should
                be issued on completion of the sequence of pings.  If such a
                trap is desired, it is the responsibility of the management
                entity to ensure that the SNMP administrative model is
                configured in such a way as to allow the trap to be delivered.
                ''',
                'ciscopingtraponcompletion',
                'CISCO-PING-MIB', False),
            _MetaInfoClassMember('ciscoPingVrfName', ATTRIBUTE, 'str' , None, None, 
                [(0, 32)], [], 
                '''                This field is used to specify the VPN name in 
                which the ping will be used. For regular ping this
                field should not be configured. The agent will use
                this field to identify the VPN routing Table for 
                this ping. This is the same ascii string used in 
                the CLI to refer to this VPN. 
                ''',
                'ciscopingvrfname',
                'CISCO-PING-MIB', False),
            ],
            'CISCO-PING-MIB',
            'ciscoPingEntry',
            _yang_ns._namespaces['CISCO-PING-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PING_MIB'
        ),
    },
    'CiscoPingMib.Ciscopingtable' : {
        'meta_info' : _MetaInfoClass('CiscoPingMib.Ciscopingtable',
            False, 
            [
            _MetaInfoClassMember('ciscoPingEntry', REFERENCE_LIST, 'Ciscopingentry' , 'ydk.models.cisco_ios_xe.CISCO_PING_MIB', 'CiscoPingMib.Ciscopingtable.Ciscopingentry', 
                [], [], 
                '''                A ping request entry.
                
                A management station wishing to create an entry should
                first generate a pseudo-random serial number to be used
                as the index to this sparse table.  The station should
                then create the associated instance of the row status
                and row owner objects.  It must also, either in the same
                or in successive PDUs, create the associated instance of
                the protocol and address objects.  It should also modify
                the default values for the other configuration objects
                if the defaults are not appropriate.
                
                Once the appropriate instance of all the configuration
                objects have been created, either by an explicit SNMP
                set request or by default, the row status should be set
                to active to initiate the request.  Note that this entire
                procedure may be initiated via a single set request which
                specifies a row status of createAndGo as well as specifies
                valid values for the non-defaulted configuration objects.
                
                Once the ping sequence has been activated, it cannot be
                stopped -- it will run until the configured number of
                packets have been sent.
                
                Once the sequence completes, the management station should
                retrieve the values of the status objects of interest, and
                should then delete the entry.  In order to prevent old
                entries from clogging the table, entries will be aged out,
                but an entry will never be deleted within 5 minutes of
                completing.
                ''',
                'ciscopingentry',
                'CISCO-PING-MIB', False),
            ],
            'CISCO-PING-MIB',
            'ciscoPingTable',
            _yang_ns._namespaces['CISCO-PING-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PING_MIB'
        ),
    },
    'CiscoPingMib' : {
        'meta_info' : _MetaInfoClass('CiscoPingMib',
            False, 
            [
            _MetaInfoClassMember('ciscoPingTable', REFERENCE_CLASS, 'Ciscopingtable' , 'ydk.models.cisco_ios_xe.CISCO_PING_MIB', 'CiscoPingMib.Ciscopingtable', 
                [], [], 
                '''                A table of ping request entries.
                ''',
                'ciscopingtable',
                'CISCO-PING-MIB', False),
            ],
            'CISCO-PING-MIB',
            'CISCO-PING-MIB',
            _yang_ns._namespaces['CISCO-PING-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_PING_MIB'
        ),
    },
}
_meta_table['CiscoPingMib.Ciscopingtable.Ciscopingentry']['meta_info'].parent =_meta_table['CiscoPingMib.Ciscopingtable']['meta_info']
_meta_table['CiscoPingMib.Ciscopingtable']['meta_info'].parent =_meta_table['CiscoPingMib']['meta_info']
