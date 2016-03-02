


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum, _dm_validate_value
from ydk.types import Empty, YList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION

from ydk.errors import YPYError, YPYDataValidationError
from ydk.models import _yang_ns

_meta_table = {
    'EntryStatus_Enum' : _MetaInfoEnum('EntryStatus_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'valid':'VALID',
            'createRequest':'CREATEREQUEST',
            'underCreation':'UNDERCREATION',
            'invalid':'INVALID',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.AlarmTable.AlarmEntry.AlarmSampleType_Enum' : _MetaInfoEnum('AlarmSampleType_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'absoluteValue':'ABSOLUTEVALUE',
            'deltaValue':'DELTAVALUE',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.AlarmTable.AlarmEntry.AlarmStartupAlarm_Enum' : _MetaInfoEnum('AlarmStartupAlarm_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'risingAlarm':'RISINGALARM',
            'fallingAlarm':'FALLINGALARM',
            'risingOrFallingAlarm':'RISINGORFALLINGALARM',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.AlarmTable.AlarmEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.AlarmTable.AlarmEntry',
            False, 
            [
            _MetaInfoClassMember('alarmIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                alarm table.  Each such entry defines a
                diagnostic sample at a particular interval
                for an object on the device.
                ''',
                'alarmindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('alarmFallingEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The index of the eventEntry that is
                used when a falling threshold is crossed.  The
                eventEntry identified by a particular value of
                this index is the same as identified by the same value
                of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then
                no association exists.  In particular, if this value
                is zero, no associated event will be generated, as
                zero is not a valid event index.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmfallingeventindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmFallingThreshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                A threshold for the sampled statistic.  When the
                current sampled value is less than or equal to
                this threshold, and the value at the last sampling
                interval was greater than this threshold, a single
                event will be generated.
                A single event will also be generated if the first
                sample after this entry becomes valid is less than or
                equal to this threshold and the associated
                alarmStartupAlarm is equal to fallingAlarm(2) or
                risingOrFallingAlarm(3).
                
                After a falling event is generated, another such event
                will not be generated until the sampled value
                rises above this threshold and reaches the
                alarmRisingThreshold.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmfallingthreshold',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmInterval', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The interval in seconds over which the data is
                sampled and compared with the rising and falling
                thresholds.  When setting this variable, care
                should be given to ensure that the variable being
                monitored will not exceed 2^31 - 1 and roll
                over the alarmValue object during the interval.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarminterval',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'alarmowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmRisingEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The index of the eventEntry that is
                used when a rising threshold is crossed.  The
                eventEntry identified by a particular value of
                this index is the same as identified by the same value
                of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then
                no association exists.  In particular, if this value
                is zero, no associated event will be generated, as
                zero is not a valid event index.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmrisingeventindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmRisingThreshold', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                A threshold for the sampled statistic.  When the
                current sampled value is greater than or equal to
                this threshold, and the value at the last sampling
                interval was less than this threshold, a single
                event will be generated.
                A single event will also be generated if the first
                sample after this entry becomes valid is greater
                than or equal to this threshold and the associated
                alarmStartupAlarm is equal to risingAlarm(1) or
                risingOrFallingAlarm(3).
                
                After a rising event is generated, another such event
                will not be generated until the sampled value
                falls below this threshold and reaches the
                alarmFallingThreshold.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmrisingthreshold',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmSampleType', REFERENCE_ENUM_CLASS, 'AlarmSampleType_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.AlarmTable.AlarmEntry.AlarmSampleType_Enum', 
                [], [], 
                '''                The method of sampling the selected variable and
                calculating the value to be compared against the
                thresholds.  If the value of this object is
                absoluteValue(1), the value of the selected variable
                will be compared directly with the thresholds at the
                end of the sampling interval.  If the value of this
                object is deltaValue(2), the value of the selected
                variable at the last sample will be subtracted from
                the current value, and the difference compared with
                the thresholds.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmsampletype',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmStartupAlarm', REFERENCE_ENUM_CLASS, 'AlarmStartupAlarm_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.AlarmTable.AlarmEntry.AlarmStartupAlarm_Enum', 
                [], [], 
                '''                The alarm that may be sent when this entry is first
                set to valid.  If the first sample after this entry
                becomes valid is greater than or equal to the
                risingThreshold and alarmStartupAlarm is equal to
                risingAlarm(1) or risingOrFallingAlarm(3), then a
                single rising alarm will be generated.  If the first
                sample after this entry becomes valid is less than
                or equal to the fallingThreshold and
                alarmStartupAlarm is equal to fallingAlarm(2) or
                risingOrFallingAlarm(3), then a single falling
                alarm will be generated.
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmstartupalarm',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this alarm entry.
                ''',
                'alarmstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmValue', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The value of the statistic during the last sampling
                period.  The value during the current sampling period
                is not made available until the period is completed.
                ''',
                'alarmvalue',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('alarmVariable', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                The object identifier of the particular variable to
                be sampled.  Only variables that resolve to an ASN.1
                primitive type of INTEGER (INTEGER, Counter, Gauge,
                or TimeTicks) may be sampled.
                
                Because SNMP access control is articulated entirely
                in terms of the contents of MIB views, no access
                control mechanism exists that can restrict the value of
                this object to identify only those objects that exist
                in a particular MIB view.  Because there is thus no
                acceptable means of restricting the read access that
                could be obtained through the alarm mechanism, the
                probe must only grant write access to this object in
                those views that have read access to all objects on
                the probe.
                
                During a set operation, if the supplied variable
                name is not available in the selected MIB view, a
                badValue error must be returned.  If at any time
                the variable name of an established alarmEntry is
                no longer available in the selected MIB view, the
                probe must change the status of this alarmEntry
                to invalid(4).
                
                This object may not be modified if the associated
                alarmStatus object is equal to valid(1).
                ''',
                'alarmvariable',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'alarmEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.AlarmTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.AlarmTable',
            False, 
            [
            _MetaInfoClassMember('alarmEntry', REFERENCE_LIST, 'AlarmEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.AlarmTable.AlarmEntry', 
                [], [], 
                '''                A list of parameters that set up a periodic checking
                for alarm conditions.
                ''',
                'alarmentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'alarmTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullAction_Enum' : _MetaInfoEnum('BufferControlFullAction_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'lockWhenFull':'LOCKWHENFULL',
            'wrapWhenFull':'WRAPWHENFULL',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullStatus_Enum' : _MetaInfoEnum('BufferControlFullStatus_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'spaceAvailable':'SPACEAVAILABLE',
            'full':'FULL',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.BufferControlTable.BufferControlEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.BufferControlTable.BufferControlEntry',
            False, 
            [
            _MetaInfoClassMember('bufferControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry
                in the bufferControl table.  The value of this
                index shall never be zero.  Each such
                entry defines one set of packets that is
                captured and controlled by one or more filters.
                ''',
                'buffercontrolindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('bufferControlCapturedPackets', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of packets currently in this captureBuffer.
                ''',
                'buffercontrolcapturedpackets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlCaptureSliceSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum number of octets of each packet
                that will be saved in this capture buffer.
                For example, if a 1500 octet packet is received by
                the probe and this object is set to 500, then only
                500 octets of the packet will be stored in the
                associated capture buffer.  If this variable is set
                to 0, the capture buffer will save as many octets
                as is possible.
                
                This object may not be modified if the associated
                bufferControlStatus object is equal to valid(1).
                ''',
                'buffercontrolcaptureslicesize',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlChannelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that identifies the channel that is the
                source of packets for this bufferControl table.
                The channel identified by a particular value of this
                index is the same as identified by the same value of
                the channelIndex object.
                
                This object may not be modified if the associated
                bufferControlStatus object is equal to valid(1).
                ''',
                'buffercontrolchannelindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlDownloadOffset', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The offset of the first octet of each packet
                in this capture buffer that will be returned in
                an SNMP retrieval of that packet.  For example,
                if 500 octets of a packet have been stored in the
                associated capture buffer and this object is set to
                100, then the captureBufferPacket object that
                contains the packet will contain bytes starting
                100 octets into the packet.
                ''',
                'buffercontroldownloadoffset',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlDownloadSliceSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum number of octets of each packet
                in this capture buffer that will be returned in
                an SNMP retrieval of that packet.  For example,
                if 500 octets of a packet have been stored in the
                associated capture buffer, the associated
                bufferControlDownloadOffset is 0, and this
                object is set to 100, then the captureBufferPacket
                object that contains the packet will contain only
                the first 100 octets of the packet.
                
                A prudent manager will take into account possible
                interoperability or fragmentation problems that may
                occur if the download slice size is set too large.
                In particular, conformant SNMP implementations are not
                required to accept messages whose length exceeds 484
                octets, although they are encouraged to support larger
                datagrams whenever feasible.
                ''',
                'buffercontroldownloadslicesize',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlFullAction', REFERENCE_ENUM_CLASS, 'BufferControlFullAction_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullAction_Enum', 
                [], [], 
                '''                Controls the action of the buffer when it
                reaches the full status.  When in the lockWhenFull(1)
                state a packet is added to the buffer that
                fills the buffer, the bufferControlFullStatus will
                be set to full(2) and this buffer will stop capturing
                packets.
                ''',
                'buffercontrolfullaction',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlFullStatus', REFERENCE_ENUM_CLASS, 'BufferControlFullStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.BufferControlTable.BufferControlEntry.BufferControlFullStatus_Enum', 
                [], [], 
                '''                This object shows whether the buffer has room to
                accept new packets or if it is full.
                
                If the status is spaceAvailable(1), the buffer is
                accepting new packets normally.  If the status is
                full(2) and the associated bufferControlFullAction
                object is wrapWhenFull, the buffer is accepting new
                packets by deleting enough of the oldest packets
                to make room for new ones as they arrive.  Otherwise,
                if the status is full(2) and the
                bufferControlFullAction object is lockWhenFull,
                then the buffer has stopped collecting packets.
                
                When this object is set to full(2) the probe must
                not later set it to spaceAvailable(1) except in the
                case of a significant gain in resources such as
                an increase of bufferControlOctetsGranted.  In
                particular, the wrap-mode action of deleting old
                packets to make room for newly arrived packets
                must not affect the value of this object.
                ''',
                'buffercontrolfullstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlMaxOctetsGranted', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum number of octets that can be
                saved in this captureBuffer, including overhead.
                If this variable is -1, the capture buffer will save
                as many octets as possible.
                
                When the bufferControlMaxOctetsRequested object is
                created or modified, the probe should set this object
                as closely to the requested value as is possible for
                the particular probe implementation and available
                resources.  However, if the request object has the
                special value of -1, the probe must set this object
                to -1.  The probe must not lower this value except
                as a result of a modification to the associated
                bufferControlMaxOctetsRequested object.
                
                When this maximum number of octets is reached
                and a new packet is to be added to this
                capture buffer and the corresponding
                bufferControlFullAction is set to wrapWhenFull(2),
                enough of the oldest packets associated with this
                capture buffer shall be deleted by the agent so
                that the new packet can be added.  If the
                corresponding bufferControlFullAction is set to
                lockWhenFull(1), the new packet shall be discarded.
                In either case, the probe must set
                bufferControlFullStatus to full(2).
                
                When the value of this object changes to a value less
                than the current value, entries are deleted from
                the captureBufferTable associated with this
                bufferControlEntry.  Enough of the
                oldest of these captureBufferEntries shall be
                deleted by the agent so that the number of octets
                used remains less than or equal to the new value of
                this object.
                
                When the value of this object changes to a value greater
                than the current value, the number of associated
                captureBufferEntries may be allowed to grow.
                ''',
                'buffercontrolmaxoctetsgranted',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlMaxOctetsRequested', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The requested maximum number of octets to be
                saved in this captureBuffer, including any
                implementation-specific overhead. If this variable
                is set to -1, the capture buffer will save as many
                octets as is possible.
                
                When this object is created or modified, the probe
                should set bufferControlMaxOctetsGranted as closely
                to this object as is possible for the particular probe
                implementation and available resources.  However, if
                the object has the special value of -1, the probe
                must set bufferControlMaxOctetsGranted to -1.
                ''',
                'buffercontrolmaxoctetsrequested',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'buffercontrolowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this buffer Control Entry.
                ''',
                'buffercontrolstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlTurnOnTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this capture buffer was
                first turned on.
                ''',
                'buffercontrolturnontime',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'bufferControlEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.BufferControlTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.BufferControlTable',
            False, 
            [
            _MetaInfoClassMember('bufferControlEntry', REFERENCE_LIST, 'BufferControlEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.BufferControlTable.BufferControlEntry', 
                [], [], 
                '''                A set of parameters that control the collection of
                a stream of packets that have matched filters.
                ''',
                'buffercontrolentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'bufferControlTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.CaptureBufferTable.CaptureBufferEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.CaptureBufferTable.CaptureBufferEntry',
            False, 
            [
            _MetaInfoClassMember('captureBufferControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The index of the bufferControlEntry with which
                this packet is associated.
                ''',
                'capturebuffercontrolindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('captureBufferIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An index that uniquely identifies an entry
                in the captureBuffer table associated with a
                particular bufferControlEntry.  This index will
                start at 1 and increase by one for each new packet
                added with the same captureBufferControlIndex.
                ''',
                'capturebufferindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('captureBufferPacketData', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The data inside the packet, starting at the beginning
                of the packet plus any offset specified in the
                associated bufferControlDownloadOffset, including any
                link level headers.  The length of the data in this
                object is the minimum of the length of the captured
                packet minus the offset, the length of the associated
                bufferControlCaptureSliceSize minus the offset, and the
                associated bufferControlDownloadSliceSize.  If this
                minimum is less than zero, this object shall have a
                length of zero.
                ''',
                'capturebufferpacketdata',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('captureBufferPacketID', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An index that describes the order of packets
                that are received on a particular interface.
                The packetID of a packet captured on an
                interface is defined to be greater than the
                packetID's of all packets captured previously on
                the same interface.  As the captureBufferPacketID
                object has a maximum positive value of 2^31 - 1,
                any captureBufferPacketID object shall have the
                value of the associated packet's packetID mod 2^31.
                ''',
                'capturebufferpacketid',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('captureBufferPacketLength', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The actual length (off the wire) of the packet stored
                in this entry, including FCS octets.
                ''',
                'capturebufferpacketlength',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('captureBufferPacketStatus', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                A value which indicates the error status of this
                packet.
                
                The value of this object is defined in the same way as
                filterPacketStatus.  The value is a sum.  This sum
                initially takes the value zero.  Then, for each
                error, E, that has been discovered in this packet,
                2 raised to a value representing E is added to the sum.
                
                The errors defined for a packet captured off of an
                Ethernet interface are as follows:
                
                    bit #    Error
                        0    Packet is longer than 1518 octets
                        1    Packet is shorter than 64 octets
                        2    Packet experienced a CRC or Alignment
                             error
                        3    First packet in this capture buffer after
                             it was detected that some packets were
                             not processed correctly.
                
                For example, an Ethernet fragment would have a
                value of 6 (2^1 + 2^2).
                
                As this MIB is expanded to new media types, this object
                will have other media-specific errors defined.
                ''',
                'capturebufferpacketstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('captureBufferPacketTime', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of milliseconds that had passed since
                this capture buffer was first turned on when this
                packet was captured.
                ''',
                'capturebufferpackettime',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'captureBufferEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.CaptureBufferTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.CaptureBufferTable',
            False, 
            [
            _MetaInfoClassMember('captureBufferEntry', REFERENCE_LIST, 'CaptureBufferEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.CaptureBufferTable.CaptureBufferEntry', 
                [], [], 
                '''                A packet captured off of an attached network.
                ''',
                'capturebufferentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'captureBufferTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.ChannelTable.ChannelEntry.ChannelAcceptType_Enum' : _MetaInfoEnum('ChannelAcceptType_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'acceptMatched':'ACCEPTMATCHED',
            'acceptFailed':'ACCEPTFAILED',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.ChannelTable.ChannelEntry.ChannelDataControl_Enum' : _MetaInfoEnum('ChannelDataControl_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'on':'ON',
            'off':'OFF',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.ChannelTable.ChannelEntry.ChannelEventStatus_Enum' : _MetaInfoEnum('ChannelEventStatus_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'eventReady':'EVENTREADY',
            'eventFired':'EVENTFIRED',
            'eventAlwaysReady':'EVENTALWAYSREADY',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.ChannelTable.ChannelEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.ChannelTable.ChannelEntry',
            False, 
            [
            _MetaInfoClassMember('channelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry
                in the channel table.  Each such
                entry defines one channel, a logical data
                and event stream.
                ''',
                'channelindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('channelAcceptType', REFERENCE_ENUM_CLASS, 'ChannelAcceptType_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.ChannelTable.ChannelEntry.ChannelAcceptType_Enum', 
                [], [], 
                '''                This object controls the action of the filters
                associated with this channel.  If this object is equal
                to acceptMatched(1), packets will be accepted to this
                channel if they are accepted by both the packet data
                and packet status matches of an associated filter. If
                this object is equal to acceptFailed(2), packets will
                be accepted to this channel only if they fail either
                the packet data match or the packet status match of
                each of the associated filters.
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelaccepttype',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelDataControl', REFERENCE_ENUM_CLASS, 'ChannelDataControl_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.ChannelTable.ChannelEntry.ChannelDataControl_Enum', 
                [], [], 
                '''                This object controls the flow of data through this
                channel.  If this object is on(1), data, status and
                events flow through this channel.  If this object is
                off(2), data, status and events will not flow through
                this channel.
                ''',
                'channeldatacontrol',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                A comment describing this channel.
                ''',
                'channeldescription',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The value of this object identifies the event
                that is configured to be generated when the
                associated channelDataControl is on and a packet
                is matched.  The event identified by a particular value
                of this object is the same event as identified by the
                same value of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then no
                association exists.  In fact, if no event is intended
                for this channel, channelEventIndex must be
                set to zero, a non-existent event index.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channeleventindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelEventStatus', REFERENCE_ENUM_CLASS, 'ChannelEventStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.ChannelTable.ChannelEntry.ChannelEventStatus_Enum', 
                [], [], 
                '''                The event status of this channel.
                
                If this channel is configured to generate events
                when packets are matched, a means of controlling
                the flow of those events is often needed.  When
                this object is equal to eventReady(1), a single
                event may be generated, after which this object
                will be set by the probe to eventFired(2).  While
                in the eventFired(2) state, no events will be
                generated until the object is modified to
                eventReady(1) (or eventAlwaysReady(3)).  The
                management station can thus easily respond to a
                notification of an event by re-enabling this object.
                
                If the management station wishes to disable this
                flow control and allow events to be generated
                at will, this object may be set to
                eventAlwaysReady(3).  Disabling the flow control
                is discouraged as it can result in high network
                traffic or other performance problems.
                ''',
                'channeleventstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelIfIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of this object uniquely identifies the
                interface on this remote network monitoring device
                to which the associated filters are applied to allow
                data into this channel.  The interface identified by
                a particular value of this object is the same
                interface as identified by the same value of the
                ifIndex object, defined in [4,6].  The filters in
                this group are applied to all packets on the local
                network segment attached to the identified
                interface.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelifindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelMatches', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of times this channel has matched a packet.
                Note that this object is updated even when
                channelDataControl is set to off.
                ''',
                'channelmatches',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'channelowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this channel entry.
                ''',
                'channelstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelTurnOffEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The value of this object identifies the event
                that is configured to turn the associated
                channelDataControl from on to off when the event is
                generated.  The event identified by a particular value
                of this object is the same event as identified by the
                same value of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then no
                association exists.  In fact, if no event is intended
                for this channel, channelTurnOffEventIndex must be
                set to zero, a non-existent event index.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelturnoffeventindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelTurnOnEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(0, 65535)], [], 
                '''                The value of this object identifies the event
                that is configured to turn the associated
                channelDataControl from off to on when the event is
                generated.  The event identified by a particular value
                of this object is the same event as identified by the
                same value of the eventIndex object.  If there is no
                corresponding entry in the eventTable, then no
                association exists.  In fact, if no event is intended
                for this channel, channelTurnOnEventIndex must be
                set to zero, a non-existent event index.
                
                This object may not be modified if the associated
                channelStatus object is equal to valid(1).
                ''',
                'channelturnoneventindex',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'channelEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.ChannelTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.ChannelTable',
            False, 
            [
            _MetaInfoClassMember('channelEntry', REFERENCE_LIST, 'ChannelEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.ChannelTable.ChannelEntry', 
                [], [], 
                '''                A set of parameters for a packet channel applied on a
                particular interface.
                ''',
                'channelentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'channelTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.EtherHistoryTable.EtherHistoryEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.EtherHistoryTable.EtherHistoryEntry',
            False, 
            [
            _MetaInfoClassMember('etherHistoryIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The history of which this entry is a part.  The
                history identified by a particular value of this
                index is the same history as identified
                by the same value of historyControlIndex.
                ''',
                'etherhistoryindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('etherHistorySampleIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An index that uniquely identifies the particular
                sample this entry represents among all samples
                associated with the same historyControlEntry.
                This index starts at 1 and increases by one
                as each new sample is taken.
                ''',
                'etherhistorysampleindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('etherHistoryBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of good packets received during this
                sampling interval that were directed to the
                broadcast address.
                ''',
                'etherhistorybroadcastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryCollisions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The best estimate of the total number of collisions
                on this Ethernet segment during this interval.
                ''',
                'etherhistorycollisions',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryCRCAlignErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets received during this
                sampling interval that had a length (excluding
                framing bits but including FCS octets) between
                64 and 1518 octets, inclusive, but were not an
                integral number of octets in length or had a
                bad Frame Check Sequence (FCS).
                ''',
                'etherhistorycrcalignerrors',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryDropEvents', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of events in which packets
                were dropped by the probe due to lack of resources
                during this interval.  Note that this number is not
                necessarily the number of packets dropped, it is just
                the number of times this condition has been detected.
                ''',
                'etherhistorydropevents',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryFragments', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received during this
                sampling interval that were not an integral
                number of octets in length or that
                had a bad Frame Check Sequence (FCS), and
                were less than 64 octets in length (excluding
                framing bits but including FCS octets).
                ''',
                'etherhistoryfragments',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryIntervalStart', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the start of the interval
                over which this sample was measured.  If the probe
                keeps track of the time of day, it should start
                the first sample of the history at a time such that
                when the next hour of the day begins, a sample is
                started at that instant.  Note that following this
                rule may require the probe to delay collecting the
                first sample of the history, as each sample must be
                of the same interval.  Also note that the sample which
                is currently being collected is not accessible in this
                table until the end of its interval.
                ''',
                'etherhistoryintervalstart',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryJabbers', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets received during this
                interval that were longer than 1518 octets
                (excluding framing bits but including FCS octets),
                and were not an integral number of octets in
                length or had a bad Frame Check Sequence (FCS).
                ''',
                'etherhistoryjabbers',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of good packets received during this
                sampling interval that were directed to a
                multicast address.  Note that this number does not
                include packets addressed to the broadcast address.
                ''',
                'etherhistorymulticastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets of data (including
                those in bad packets) received on the
                network (excluding framing bits but including
                FCS octets).
                ''',
                'etherhistoryoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryOversizePkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets received during this
                interval that were longer than 1518 octets
                (excluding framing bits but including FCS
                octets) but were otherwise well formed.
                ''',
                'etherhistoryoversizepkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets (including error packets)
                received during this sampling interval.
                ''',
                'etherhistorypkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryUndersizePkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets received during this
                interval that were less than 64 octets long
                (excluding framing bits but including FCS
                octets) and were otherwise well formed.
                ''',
                'etherhistoryundersizepkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryUtilization', ATTRIBUTE, 'int' , None, None, 
                [(0, 10000)], [], 
                '''                The best estimate of the mean physical layer
                network utilization on this interface during this
                interval, in hundredths of a percent.
                ''',
                'etherhistoryutilization',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'etherHistoryEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.EtherHistoryTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.EtherHistoryTable',
            False, 
            [
            _MetaInfoClassMember('etherHistoryEntry', REFERENCE_LIST, 'EtherHistoryEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.EtherHistoryTable.EtherHistoryEntry', 
                [], [], 
                '''                An historical sample of Ethernet statistics on a
                particular Ethernet interface.  This sample is
                associated with the historyControlEntry which set
                up the parameters for a regular collection of these
                samples.
                ''',
                'etherhistoryentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'etherHistoryTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.EtherStatsTable.EtherStatsEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.EtherStatsTable.EtherStatsEntry',
            False, 
            [
            _MetaInfoClassMember('etherStatsIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The value of this object uniquely identifies this
                etherStats entry.
                ''',
                'etherstatsindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('etherStatsBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of good packets received that were
                directed to the broadcast address.
                ''',
                'etherstatsbroadcastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsCollisions', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The best estimate of the total number of collisions
                on this Ethernet segment.
                ''',
                'etherstatscollisions',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsCRCAlignErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received that
                had a length (excluding framing bits, but
                including FCS octets) of between 64 and 1518
                octets, inclusive, but were not an integral number
                of octets in length or had a bad Frame Check
                Sequence (FCS).
                ''',
                'etherstatscrcalignerrors',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data that
                this etherStats entry is configured to analyze.  This
                source can be any ethernet interface on this device.
                In order to identify a particular interface, this
                object shall identify the instance of the ifIndex
                object, defined in [4,6], for the desired interface.
                For example, if an entry were to receive data from
                interface #1, this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the
                identified interface.
                
                This object may not be modified if the associated
                etherStatsStatus object is equal to valid(1).
                ''',
                'etherstatsdatasource',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsDropEvents', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of events in which packets
                were dropped by the probe due to lack of resources.
                Note that this number is not necessarily the number of
                packets dropped; it is just the number of times this
                condition has been detected.
                ''',
                'etherstatsdropevents',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsFragments', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received that were not an
                integral number of octets in length or that had a bad
                Frame Check Sequence (FCS), and were less than 64
                octets in length (excluding framing bits but
                including FCS octets).
                ''',
                'etherstatsfragments',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsJabbers', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received that were
                longer than 1518 octets (excluding framing bits,
                but including FCS octets), and were not an
                integral number of octets in length or had
                a bad Frame Check Sequence (FCS).
                ''',
                'etherstatsjabbers',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of good packets received that were
                directed to a multicast address.  Note that this
                number does not include packets directed to the
                broadcast address.
                ''',
                'etherstatsmulticastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of octets of data (including
                those in bad packets) received on the
                network (excluding framing bits but including
                FCS octets).
                ''',
                'etherstatsoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsOversizePkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received that were
                longer than 1518 octets (excluding framing bits,
                but including FCS octets) and were otherwise
                well formed.
                ''',
                'etherstatsoversizepkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'etherstatsowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets (including error packets)
                received.
                ''',
                'etherstatspkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsPkts1024to1518Octets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets (including error
                packets) received that were between
                1024 and 1518 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts1024to1518octets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsPkts128to255Octets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets (including error
                packets) received that were between
                128 and 255 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts128to255octets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsPkts256to511Octets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets (including error
                packets) received that were between
                256 and 511 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts256to511octets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsPkts512to1023Octets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets (including error
                packets) received that were between
                512 and 1023 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts512to1023octets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsPkts64Octets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets (including error
                packets) received that were 64 octets in length
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts64octets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsPkts65to127Octets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets (including error
                packets) received that were between
                65 and 127 octets in length inclusive
                (excluding framing bits but including FCS octets).
                ''',
                'etherstatspkts65to127octets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this etherStats entry.
                ''',
                'etherstatsstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsUndersizePkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The total number of packets received that were
                less than 64 octets long (excluding framing bits,
                but including FCS octets) and were otherwise well
                formed.
                ''',
                'etherstatsundersizepkts',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'etherStatsEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.EtherStatsTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.EtherStatsTable',
            False, 
            [
            _MetaInfoClassMember('etherStatsEntry', REFERENCE_LIST, 'EtherStatsEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.EtherStatsTable.EtherStatsEntry', 
                [], [], 
                '''                A collection of statistics kept for a particular
                Ethernet interface.
                ''',
                'etherstatsentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'etherStatsTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.EventTable.EventEntry.EventType_Enum' : _MetaInfoEnum('EventType_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'none':'NONE',
            'log':'LOG',
            'snmp-trap':'SNMP_TRAP',
            'log-and-trap':'LOG_AND_TRAP',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.EventTable.EventEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.EventTable.EventEntry',
            False, 
            [
            _MetaInfoClassMember('eventIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                event table.  Each such entry defines one event that
                is to be generated when the appropriate conditions
                occur.
                ''',
                'eventindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('eventCommunity', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                If an SNMP trap is to be sent, it will be sent to
                the SNMP community specified by this octet string.
                In the future this table will be extended to include
                the party security mechanism.  This object shall be
                set to a string of length zero if it is intended that
                that mechanism be used to specify the destination of
                the trap.
                ''',
                'eventcommunity',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('eventDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 127)], [], 
                '''                A comment describing this event entry.
                ''',
                'eventdescription',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('eventLastTimeSent', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime at the time this event
                entry last generated an event.  If this entry has
                not generated any events, this value will be
                zero.
                ''',
                'eventlasttimesent',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('eventOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                
                If this object contains a string starting with 'monitor'
                and has associated entries in the log table, all
                connected management stations should retrieve those
                log entries, as they may have significance to all
                management stations connected to this device
                ''',
                'eventowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('eventStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this event entry.
                
                If this object is not equal to valid(1), all associated
                log entries shall be deleted by the agent.
                ''',
                'eventstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('eventType', REFERENCE_ENUM_CLASS, 'EventType_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.EventTable.EventEntry.EventType_Enum', 
                [], [], 
                '''                The type of notification that the probe will make
                about this event.  In the case of log, an entry is
                made in the log table for each event.  In the case of
                snmp-trap, an SNMP trap is sent to one or more
                management stations.
                ''',
                'eventtype',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'eventEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.EventTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.EventTable',
            False, 
            [
            _MetaInfoClassMember('eventEntry', REFERENCE_LIST, 'EventEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.EventTable.EventEntry', 
                [], [], 
                '''                A set of parameters that describe an event to be
                generated when certain conditions are met.
                ''',
                'evententry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'eventTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.FilterTable.FilterEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.FilterTable.FilterEntry',
            False, 
            [
            _MetaInfoClassMember('filterIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry
                in the filter table.  Each such entry defines
                one filter that is to be applied to every packet
                received on an interface.
                ''',
                'filterindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('filterChannelIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                This object identifies the channel of which this
                filter is a part.  The filters identified by a
                particular value of this object are associated
                with the same channel as identified by the same
                value of the channelIndex object.
                ''',
                'filterchannelindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'filterowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterPktData', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The data that is to be matched with the input packet.
                For each packet received, this filter and the
                accompanying filterPktDataMask and
                filterPktDataNotMask will be adjusted for the
                offset.  The only bits relevant to this
                match algorithm are those that have the corresponding
                filterPktDataMask bit equal to one.  The following
                three rules are then applied to every packet:
                
                (1) If the packet is too short and does not have data
                    corresponding to part of the filterPktData, the
                    packet will fail this data match.
                
                (2) For each relevant bit from the packet with the
                    corresponding filterPktDataNotMask bit set to
                    zero, if the bit from the packet is not equal to
                    the corresponding bit from the filterPktData,
                    then the packet will fail this data match.
                
                (3) If for every relevant bit from the packet with the
                    corresponding filterPktDataNotMask bit set to one,
                    the bit from the packet is equal to the
                    corresponding bit from the filterPktData, then
                    the packet will fail this data match.
                
                Any packets that have not failed any of the three
                matches above have passed this data match.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdata',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterPktDataMask', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The mask that is applied to the match process.
                After adjusting this mask for the offset, only those
                bits in the received packet that correspond to bits
                set in this mask are relevant for further processing
                by the match algorithm.  The offset is applied to
                filterPktDataMask in the same way it is applied to
                the filter.  For the purposes of the matching
                algorithm, if the associated filterPktData object
                is longer than this mask, this mask is conceptually
                extended with '1' bits until it reaches the
                length of the filterPktData object.
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdatamask',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterPktDataNotMask', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The inversion mask that is applied to the match
                process.  After adjusting this mask for the offset,
                those relevant bits in the received packet that
                correspond to bits cleared in this mask must all
                be equal to their corresponding bits in the
                filterPktData object for the packet to be accepted.
                In addition, at least one of those relevant
                bits in the received packet that correspond to bits
                set in this mask must be different to its
                corresponding bit in the filterPktData object.
                
                For the purposes of the matching algorithm, if
                the associated filterPktData object is longer than
                this mask, this mask is conceptually extended with
                '0' bits until it reaches the length of the
                filterPktData object.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdatanotmask',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterPktDataOffset', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The offset from the beginning of each packet where
                a match of packet data will be attempted.  This offset
                is measured from the point in the physical layer
                packet after the framing bits, if any.  For example,
                in an Ethernet frame, this point is at the beginning
                of the destination MAC address.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktdataoffset',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterPktStatus', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The status that is to be matched with the input
                packet.  The only bits relevant to this match
                algorithm are those that have the corresponding
                filterPktStatusMask bit equal to one.
                
                The following two rules are then applied to every
                packet:
                
                (1) For each relevant bit from the packet status
                    with the corresponding filterPktStatusNotMask
                    bit set to zero, if the bit from the packet
                    status is not equal to the corresponding bit
                    from the filterPktStatus, then the packet will
                    fail this status match.
                
                (2) If for every relevant bit from the packet status
                    with the corresponding filterPktStatusNotMask
                    bit set to one, the bit from the packet status
                    is equal to the corresponding bit from the
                    filterPktStatus, then the packet will fail
                    this status match.
                
                Any packets that have not failed either of the two
                matches above have passed this status match.
                
                The value of the packet status is a sum.  This sum
                initially takes the value zero.  Then, for each
                error, E, that has been discovered in this packet,
                2 raised to a value representing E is added to the sum.
                The errors and the bits that represent them are
                dependent on the media type of the interface that
                this channel is receiving packets from.
                
                The errors defined for a packet captured off of an
                Ethernet interface are as follows:
                
                    bit #    Error
                        0    Packet is longer than 1518 octets
                        1    Packet is shorter than 64 octets
                        2    Packet experienced a CRC or Alignment
                             error
                
                For example, an Ethernet fragment would have a
                value of 6 (2^1 + 2^2).
                
                As this MIB is expanded to new media types, this
                object will have other media-specific errors defined.
                
                For the purposes of this status matching algorithm, if
                the packet status is longer than this
                object, filterPktStatus this object is conceptually
                extended with '0' bits until it reaches the size of
                the packet status.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterPktStatusMask', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The mask that is applied to the status match process.
                Only those bits in the received packet that correspond
                to bits set in this mask are relevant for further
                processing by the status match algorithm.  For the
                purposes of the matching algorithm, if the
                associated filterPktStatus object is longer than
                this mask, this mask is conceptually extended with
                '1' bits until it reaches the size of the
                filterPktStatus.  In addition, if a packet status is
                longer than this mask, this mask is conceptually
                extended with '0' bits until it reaches the size of
                the packet status.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktstatusmask',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterPktStatusNotMask', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The inversion mask that is applied to the status match
                process.  Those relevant bits in the received packet
                status that correspond to bits cleared in this mask
                must all be equal to their corresponding bits in the
                filterPktStatus object for the packet to be accepted.
                In addition, at least one of those relevant bits in the
                received packet status that correspond to bits set in
                this mask must be different to its corresponding bit
                in the filterPktStatus object for the packet to be
                accepted.
                
                For the purposes of the matching algorithm, if the
                associated filterPktStatus object or a packet status
                is longer than this mask, this mask is conceptually
                extended with '0' bits until it reaches the longer of
                the lengths of the filterPktStatus object and the
                packet status.
                
                This object may not be modified if the associated
                filterStatus object is equal to valid(1).
                ''',
                'filterpktstatusnotmask',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this filter entry.
                ''',
                'filterstatus',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'filterEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.FilterTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.FilterTable',
            False, 
            [
            _MetaInfoClassMember('filterEntry', REFERENCE_LIST, 'FilterEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.FilterTable.FilterEntry', 
                [], [], 
                '''                A set of parameters for a packet filter applied on a
                particular interface.
                ''',
                'filterentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'filterTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HistoryControlTable.HistoryControlEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HistoryControlTable.HistoryControlEntry',
            False, 
            [
            _MetaInfoClassMember('historyControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                historyControl table.  Each such entry defines a
                set of samples at a particular interval for an
                interface on the device.
                ''',
                'historycontrolindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('historyControlBucketsGranted', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The number of discrete sampling intervals
                over which data shall be saved in the part of
                the media-specific table associated with this
                historyControl entry.
                
                When the associated historyControlBucketsRequested
                object is created or modified, the probe
                should set this object as closely to the requested
                value as is possible for the particular
                probe implementation and available resources.  The
                probe must not lower this value except as a result
                of a modification to the associated
                historyControlBucketsRequested object.
                
                There will be times when the actual number of
                buckets associated with this entry is less than
                the value of this object.  In this case, at the
                end of each sampling interval, a new bucket will
                be added to the media-specific table.
                
                When the number of buckets reaches the value of
                this object and a new bucket is to be added to the
                media-specific table, the oldest bucket associated
                with this historyControlEntry shall be deleted by
                the agent so that the new bucket can be added.
                
                When the value of this object changes to a value less
                than the current value, entries are deleted
                from the media-specific table associated with this
                historyControlEntry.  Enough of the oldest of these
                entries shall be deleted by the agent so that their
                number remains less than or equal to the new value of
                this object.
                
                When the value of this object changes to a value
                greater than the current value, the number of
                associated media-specific entries may be allowed
                to grow.
                ''',
                'historycontrolbucketsgranted',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('historyControlBucketsRequested', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The requested number of discrete time intervals
                over which data is to be saved in the part of the
                media-specific table associated with this
                historyControl entry.
                
                When this object is created or modified, the probe
                should set historyControlBucketsGranted as closely to
                this object as is possible for the particular probe
                implementation and available resources.
                ''',
                'historycontrolbucketsrequested',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('historyControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data for
                which historical data was collected and
                placed in a media-specific table on behalf of this
                historyControlEntry.  This source can be any
                interface on this device.  In order to identify
                a particular interface, this object shall identify
                the instance of the ifIndex object, defined
                in [4,6], for the desired interface.  For example,
                if an entry were to receive data from interface #1,
                this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the
                identified interface.
                
                This object may not be modified if the associated
                historyControlStatus object is equal to valid(1).
                ''',
                'historycontroldatasource',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('historyControlInterval', ATTRIBUTE, 'int' , None, None, 
                [(1, 3600)], [], 
                '''                The interval in seconds over which the data is
                sampled for each bucket in the part of the
                media-specific table associated with this
                historyControl entry.  This interval can
                be set to any number of seconds between 1 and
                3600 (1 hour).
                
                Because the counters in a bucket may overflow at their
                maximum value with no indication, a prudent manager
                will take into account the possibility of overflow
                in any of the associated counters.  It is important
                to consider the minimum time in which any counter
                could overflow on a particular media type and set
                the historyControlInterval object to a value less
                than this interval.  This is typically most
                important for the 'octets' counter in any
                media-specific table.  For example, on an Ethernet
                network, the etherHistoryOctets counter could overflow
                in about one hour at the Ethernet's maximum
                utilization.
                
                This object may not be modified if the associated
                historyControlStatus object is equal to valid(1).
                ''',
                'historycontrolinterval',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('historyControlOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is therefore
                using the resources assigned to it.
                ''',
                'historycontrolowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('historyControlStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this historyControl entry.
                
                Each instance of the media-specific table associated
                with this historyControlEntry will be deleted by the
                agent if this historyControlEntry is not equal to
                valid(1).
                ''',
                'historycontrolstatus',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'historyControlEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HistoryControlTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HistoryControlTable',
            False, 
            [
            _MetaInfoClassMember('historyControlEntry', REFERENCE_LIST, 'HistoryControlEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HistoryControlTable.HistoryControlEntry', 
                [], [], 
                '''                A list of parameters that set up a periodic
                sampling of statistics.
                ''',
                'historycontrolentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'historyControlTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostControlTable.HostControlEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostControlTable.HostControlEntry',
            False, 
            [
            _MetaInfoClassMember('hostControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                hostControl table.  Each such entry defines
                a function that discovers hosts on a particular
                interface and places statistics about them in the
                hostTable and the hostTimeTable on behalf of this
                hostControlEntry.
                ''',
                'hostcontrolindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of the data for
                this instance of the host function.  This source
                can be any interface on this device.  In order
                to identify a particular interface, this object shall
                identify the instance of the ifIndex object, defined
                in [4,6], for the desired interface.  For example,
                if an entry were to receive data from interface #1,
                this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the
                identified interface.
                
                This object may not be modified if the associated
                hostControlStatus object is equal to valid(1).
                ''',
                'hostcontroldatasource',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostControlLastDeleteTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the last entry
                was deleted from the portion of the hostTable
                associated with this hostControlEntry.  If no
                deletions have occurred, this value shall be zero.
                ''',
                'hostcontrollastdeletetime',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostControlOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'hostcontrolowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostControlStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this hostControl entry.
                
                If this object is not equal to valid(1), all
                associated entries in the hostTable,
                hostTimeTable, and the hostTopNTable shall be
                deleted by the agent.
                ''',
                'hostcontrolstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostControlTableSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of hostEntries in the hostTable and the
                hostTimeTable associated with this hostControlEntry.
                ''',
                'hostcontroltablesize',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostControlEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostControlTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostControlTable',
            False, 
            [
            _MetaInfoClassMember('hostControlEntry', REFERENCE_LIST, 'HostControlEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostControlTable.HostControlEntry', 
                [], [], 
                '''                A list of parameters that set up the discovery of
                hosts on a particular interface and the collection
                of statistics about these hosts.
                ''',
                'hostcontrolentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostControlTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTable.HostEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTable.HostEntry',
            False, 
            [
            _MetaInfoClassMember('hostAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The physical address of this host.
                ''',
                'hostaddress',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The set of collected host statistics of which
                this entry is a part.  The set of hosts
                identified by a particular value of this
                index is associated with the hostControlEntry
                as identified by the same value of hostControlIndex.
                ''',
                'hostindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostCreationOrder', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that defines the relative ordering of
                the creation time of hosts captured for a
                particular hostControlEntry.  This index shall
                be between 1 and N, where N is the value of
                the associated hostControlTableSize.  The ordering
                of the indexes is based on the order of each entry's
                insertion into the table, in which entries added
                earlier have a lower index value than entries added
                later.
                
                It is important to note that the order for a
                particular entry may change as an (earlier) entry
                is deleted from the table.  Because this order may
                change, management stations should make use of the
                hostControlLastDeleteTime variable in the
                hostControlEntry associated with the relevant
                portion of the hostTable.  By observing
                this variable, the management station may detect
                the circumstances where a previous association
                between a value of hostCreationOrder
                and a hostEntry may no longer hold.
                ''',
                'hostcreationorder',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted to this address
                since it was added to the hostTable (excluding
                framing bits but including FCS octets), except for
                those octets in packets that contained errors.
                ''',
                'hostinoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors transmitted to
                this address since it was added to the hostTable.
                ''',
                'hostinpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostOutBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of good packets transmitted by this
                address that were directed to the broadcast address
                since this host was added to the hostTable.
                ''',
                'hostoutbroadcastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostOutErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of error packets transmitted by this
                address since this host was added to the hostTable.
                ''',
                'hostouterrors',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostOutMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of good packets transmitted by this
                address that were directed to a multicast address
                since this host was added to the hostTable.
                Note that this number does not include packets
                directed to the broadcast address.
                ''',
                'hostoutmulticastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted by this address
                since it was added to the hostTable (excluding
                framing bits but including FCS octets), including
                those octets in packets that contained errors.
                ''',
                'hostoutoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets including errors transmitted
                by this address since it was added to the hostTable.
                ''',
                'hostoutpkts',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTable',
            False, 
            [
            _MetaInfoClassMember('hostEntry', REFERENCE_LIST, 'HostEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTable.HostEntry', 
                [], [], 
                '''                A collection of statistics for a particular host
                that has been discovered on an interface of this
                device.
                ''',
                'hostentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTimeTable.HostTimeEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTimeTable.HostTimeEntry',
            False, 
            [
            _MetaInfoClassMember('hostTimeCreationOrder', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in
                the hostTime table among those entries associated
                with the same hostControlEntry.  This index shall
                be between 1 and N, where N is the value of
                the associated hostControlTableSize.  The ordering
                of the indexes is based on the order of each entry's
                insertion into the table, in which entries added
                earlier have a lower index value than entries added
                later.  Thus the management station has the ability
                to learn of new entries added to this table without
                downloading the entire table.
                
                It is important to note that the index for a
                particular entry may change as an (earlier) entry
                is deleted from the table.  Because this order may
                change, management stations should make use of the
                hostControlLastDeleteTime variable in the
                hostControlEntry associated with the relevant
                portion of the hostTimeTable.  By observing
                this variable, the management station may detect
                the circumstances where a download of the table
                may have missed entries, and where a previous
                association between a value of hostTimeCreationOrder
                and a hostTimeEntry may no longer hold.
                ''',
                'hosttimecreationorder',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostTimeIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The set of collected host statistics of which
                this entry is a part.  The set of hosts
                identified by a particular value of this
                index is associated with the hostControlEntry
                as identified by the same value of hostControlIndex.
                ''',
                'hosttimeindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostTimeAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The physical address of this host.
                ''',
                'hosttimeaddress',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeInOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted to this address
                since it was added to the hostTimeTable (excluding
                framing bits but including FCS octets), except for
                those octets in packets that contained errors.
                ''',
                'hosttimeinoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeInPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets without errors transmitted to
                this address since it was added to the hostTimeTable.
                ''',
                'hosttimeinpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeOutBroadcastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of good packets transmitted by this
                address that were directed to the broadcast address
                since this host was added to the hostTimeTable.
                ''',
                'hosttimeoutbroadcastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeOutErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of error packets transmitted by this
                address since this host was added to the
                hostTimeTable.
                ''',
                'hosttimeouterrors',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeOutMulticastPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of good packets transmitted by this
                address that were directed to a multicast address
                since this host was added to the hostTimeTable.
                Note that this number does not include packets
                directed to the broadcast address.
                ''',
                'hosttimeoutmulticastpkts',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeOutOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets transmitted by this address since
                it was added to the hostTimeTable (excluding framing
                bits but including FCS octets), including those
                octets in packets that contained errors.
                ''',
                'hosttimeoutoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeOutPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets including errors transmitted
                by this address since it was added to the
                hostTimeTable.
                ''',
                'hosttimeoutpkts',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostTimeEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTimeTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTimeTable',
            False, 
            [
            _MetaInfoClassMember('hostTimeEntry', REFERENCE_LIST, 'HostTimeEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTimeTable.HostTimeEntry', 
                [], [], 
                '''                A collection of statistics for a particular host
                that has been discovered on an interface of this
                device.  This collection includes the relative
                ordering of the creation time of this object.
                ''',
                'hosttimeentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostTimeTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTopNControlTable.HostTopNControlEntry.HostTopNRateBase_Enum' : _MetaInfoEnum('HostTopNRateBase_Enum', 'ydk.models.rfc1271.RFC1271_MIB',
        {
            'hostTopNInPkts':'HOSTTOPNINPKTS',
            'hostTopNOutPkts':'HOSTTOPNOUTPKTS',
            'hostTopNInOctets':'HOSTTOPNINOCTETS',
            'hostTopNOutOctets':'HOSTTOPNOUTOCTETS',
            'hostTopNOutErrors':'HOSTTOPNOUTERRORS',
            'hostTopNOutBroadcastPkts':'HOSTTOPNOUTBROADCASTPKTS',
            'hostTopNOutMulticastPkts':'HOSTTOPNOUTMULTICASTPKTS',
        }, 'RFC1271-MIB', _yang_ns._namespaces['RFC1271-MIB']),
    'RFC1271MIB.HostTopNControlTable.HostTopNControlEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTopNControlTable.HostTopNControlEntry',
            False, 
            [
            _MetaInfoClassMember('hostTopNControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry
                in the hostTopNControl table.  Each such
                entry defines one top N report prepared for
                one interface.
                ''',
                'hosttopncontrolindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostTopNDuration', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of seconds that this report has collected
                during the last sampling interval, or if this
                report is currently being collected, the number
                of seconds that this report is being collected
                during this sampling interval.
                
                When the associated hostTopNTimeRemaining object is
                set, this object shall be set by the probe to the
                same value and shall not be modified until the next
                time the hostTopNTimeRemaining is set.
                
                This value shall be zero if no reports have been
                requested for this hostTopNControlEntry.
                ''',
                'hosttopnduration',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNGrantedSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum number of hosts in the top N table.
                
                When the associated hostTopNRequestedSize object is
                created or modified, the probe should set this
                object as closely to the requested value as is
                possible for the particular implementation and
                available resources. The probe must not lower this
                value except as a result of a set to the associated
                hostTopNRequestedSize object.
                
                Hosts with the highest value of hostTopNRate shall be
                placed in this table in decreasing order of this rate
                until there is no more room or until there are no more
                hosts.
                ''',
                'hosttopngrantedsize',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNHostIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The host table for which a top N report will be
                prepared on behalf of this entry.  The host table
                identified by a particular value of this index is
                associated with the same host table as identified
                by the same value of hostIndex.
                
                This object may not be modified if the associated
                hostTopNStatus object is equal to valid(1).
                ''',
                'hosttopnhostindex',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'hosttopnowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNRateBase', REFERENCE_ENUM_CLASS, 'HostTopNRateBase_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTopNControlTable.HostTopNControlEntry.HostTopNRateBase_Enum', 
                [], [], 
                '''                The variable for each host that the hostTopNRate
                variable is based upon.
                
                This object may not be modified if the associated
                hostTopNStatus object is equal to valid(1).
                ''',
                'hosttopnratebase',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNRequestedSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The maximum number of hosts requested for the top N
                table.
                
                When this object is created or modified, the probe
                should set hostTopNGrantedSize as closely to this
                object as is possible for the particular probe
                implementation and available resources.
                ''',
                'hosttopnrequestedsize',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNStartTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this top N report was
                last started.  In other words, this is the time that
                the associated hostTopNTimeRemaining object was
                modified to start the requested report.
                ''',
                'hosttopnstarttime',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this hostTopNControl entry.
                If this object is not equal to valid(1), all
                associated hostTopNEntries shall be deleted by
                the agent.
                ''',
                'hosttopnstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNTimeRemaining', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of seconds left in the report currently
                being collected.  When this object is modified by
                the management station, a new collection is started,
                possibly aborting a currently running report.  The
                new value is used as the requested duration of this
                report, which is loaded into the associated
                hostTopNDuration object.
                
                When this object is set to a non-zero value, any
                associated hostTopNEntries shall be made
                inaccessible by the monitor.  While the value of this
                object is non-zero, it decrements by one per second
                until it reaches zero.  During this time, all
                associated hostTopNEntries shall remain
                inaccessible.  At the time that this object
                decrements to zero, the report is made
                accessible in the hostTopNTable.  Thus, the hostTopN
                table needs to be created only at the end of the
                collection interval.
                ''',
                'hosttopntimeremaining',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostTopNControlEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTopNControlTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTopNControlTable',
            False, 
            [
            _MetaInfoClassMember('hostTopNControlEntry', REFERENCE_LIST, 'HostTopNControlEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTopNControlTable.HostTopNControlEntry', 
                [], [], 
                '''                A set of parameters that control the creation of a
                report of the top N hosts according to several
                metrics.
                ''',
                'hosttopncontrolentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostTopNControlTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTopNTable.HostTopNEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTopNTable.HostTopNEntry',
            False, 
            [
            _MetaInfoClassMember('hostTopNIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in
                the hostTopN table among those in the same report.
                This index is between 1 and N, where N is the
                number of entries in this table.  Increasing values
                of hostTopNIndex shall be assigned to entries with
                decreasing values of hostTopNRate until index N
                is assigned to the entry with the lowest value of
                hostTopNRate or there are no more hostTopNEntries.
                ''',
                'hosttopnindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostTopNReport', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                This object identifies the top N report of which
                this entry is a part.  The set of hosts
                identified by a particular value of this
                object is part of the same report as identified
                by the same value of the hostTopNControlIndex object.
                ''',
                'hosttopnreport',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('hostTopNAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The physical address of this host.
                ''',
                'hosttopnaddress',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNRate', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The amount of change in the selected variable
                during this sampling interval.  The selected
                variable is this host's instance of the object
                selected by hostTopNRateBase.
                ''',
                'hosttopnrate',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostTopNEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.HostTopNTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.HostTopNTable',
            False, 
            [
            _MetaInfoClassMember('hostTopNEntry', REFERENCE_LIST, 'HostTopNEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTopNTable.HostTopNEntry', 
                [], [], 
                '''                A set of statistics for a host that is part of a
                top N report.
                ''',
                'hosttopnentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'hostTopNTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.LogTable.LogEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.LogTable.LogEntry',
            False, 
            [
            _MetaInfoClassMember('logEventIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The event entry that generated this log
                entry.  The log identified by a particular
                value of this index is associated with the same
                eventEntry as identified by the same value
                of eventIndex.
                ''',
                'logeventindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('logIndex', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                An index that uniquely identifies an entry
                in the log table amongst those generated by the
                same eventEntries.  These indexes are
                assigned beginning with 1 and increase by one
                with each new log entry.  The association
                between values of logIndex and logEntries
                is fixed for the lifetime of each logEntry.
                The agent may choose to delete the oldest
                instances of logEntry as required because of
                lack of memory.  It is an implementation-specific
                matter as to when this deletion may occur.
                ''',
                'logindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('logDescription', ATTRIBUTE, 'str' , None, None, 
                [(0, 255)], [], 
                '''                An implementation dependent description of the
                event that activated this log entry.
                ''',
                'logdescription',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('logTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when this log entry was
                created.
                ''',
                'logtime',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'logEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.LogTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.LogTable',
            False, 
            [
            _MetaInfoClassMember('logEntry', REFERENCE_LIST, 'LogEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.LogTable.LogEntry', 
                [], [], 
                '''                A set of data describing an event that has been
                logged.
                ''',
                'logentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'logTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.MatrixControlTable.MatrixControlEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.MatrixControlTable.MatrixControlEntry',
            False, 
            [
            _MetaInfoClassMember('matrixControlIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                An index that uniquely identifies an entry in the
                matrixControl table.  Each such entry defines
                a function that discovers conversations on a particular
                interface and places statistics about them in the
                matrixSDTable and the matrixDSTable on behalf of this
                matrixControlEntry.
                ''',
                'matrixcontrolindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('matrixControlDataSource', ATTRIBUTE, 'str' , None, None, 
                [], ['(([0-1](\\.[1-3]?[0-9]))|(2\\.(0|([1-9]\\d*))))(\\.(0|([1-9]\\d*)))*'], 
                '''                This object identifies the source of
                the data from which this entry creates a traffic matrix.
                This source can be any interface on this device.  In
                order to identify a particular interface, this object
                shall identify the instance of the ifIndex object,
                defined in [4,6], for the desired interface.  For
                example, if an entry were to receive data from
                interface #1, this object would be set to ifIndex.1.
                
                The statistics in this group reflect all packets
                on the local network segment attached to the
                identified interface.
                
                This object may not be modified if the associated
                matrixControlStatus object is equal to valid(1).
                ''',
                'matrixcontroldatasource',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixControlLastDeleteTime', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The value of sysUpTime when the last entry
                was deleted from the portion of the matrixSDTable
                or matrixDSTable associated with this
                matrixControlEntry.
                If no deletions have occurred, this value shall be
                zero.
                ''',
                'matrixcontrollastdeletetime',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixControlOwner', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The entity that configured this entry and is
                therefore using the resources assigned to it.
                ''',
                'matrixcontrolowner',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixControlStatus', REFERENCE_ENUM_CLASS, 'EntryStatus_Enum' , 'ydk.models.rfc1271.RFC1271_MIB', 'EntryStatus_Enum', 
                [], [], 
                '''                The status of this matrixControl entry.
                
                If this object is not equal to valid(1), all
                associated entries in the matrixSDTable and the
                matrixDSTable shall be deleted by the agent.
                ''',
                'matrixcontrolstatus',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixControlTableSize', ATTRIBUTE, 'int' , None, None, 
                [(-2147483648, 2147483647)], [], 
                '''                The number of matrixSDEntries in the matrixSDTable
                for this interface.  This must also be the value of
                the number of entries in the matrixDSTable for this
                interface.
                ''',
                'matrixcontroltablesize',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'matrixControlEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.MatrixControlTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.MatrixControlTable',
            False, 
            [
            _MetaInfoClassMember('matrixControlEntry', REFERENCE_LIST, 'MatrixControlEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.MatrixControlTable.MatrixControlEntry', 
                [], [], 
                '''                Information about a traffic matrix on a
                particular interface.
                ''',
                'matrixcontrolentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'matrixControlTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.MatrixDSTable.MatrixDSEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.MatrixDSTable.MatrixDSEntry',
            False, 
            [
            _MetaInfoClassMember('matrixDSDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The destination physical address.
                ''',
                'matrixdsdestaddress',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('matrixDSIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The set of collected matrix statistics of which
                this entry is a part.  The set of matrix statistics
                identified by a particular value of this index
                is associated with the same matrixControlEntry
                as identified by the same value of matrixControlIndex.
                ''',
                'matrixdsindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('matrixDSSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The source physical address.
                ''',
                'matrixdssourceaddress',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('matrixDSErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of error packets transmitted from
                the source address to the destination address.
                ''',
                'matrixdserrors',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixDSOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets (excluding framing bits
                but including FCS octets) contained in all packets
                transmitted from the source address to the
                destination address.
                ''',
                'matrixdsoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixDSPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets transmitted from the source
                address to the destination address (this number
                includes error packets).
                ''',
                'matrixdspkts',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'matrixDSEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.MatrixDSTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.MatrixDSTable',
            False, 
            [
            _MetaInfoClassMember('matrixDSEntry', REFERENCE_LIST, 'MatrixDSEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.MatrixDSTable.MatrixDSEntry', 
                [], [], 
                '''                A collection of statistics for communications between
                two address on a particular interface.
                ''',
                'matrixdsentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'matrixDSTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.MatrixSDTable.MatrixSDEntry' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.MatrixSDTable.MatrixSDEntry',
            False, 
            [
            _MetaInfoClassMember('matrixSDDestAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The destination physical address.
                ''',
                'matrixsddestaddress',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('matrixSDIndex', ATTRIBUTE, 'int' , None, None, 
                [(1, 65535)], [], 
                '''                The set of collected matrix statistics of which
                this entry is a part.  The set of matrix statistics
                identified by a particular value of this index
                is associated with the same matrixControlEntry
                as identified by the same value of matrixControlIndex.
                ''',
                'matrixsdindex',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('matrixSDSourceAddress', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The source physical address.
                ''',
                'matrixsdsourceaddress',
                'RFC1271-MIB', True),
            _MetaInfoClassMember('matrixSDErrors', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of error packets transmitted from
                the source address to the destination address.
                ''',
                'matrixsderrors',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixSDOctets', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of octets (excluding framing bits but
                including FCS octets) contained in all packets
                transmitted from the source address to the
                destination address.
                ''',
                'matrixsdoctets',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixSDPkts', ATTRIBUTE, 'int' , None, None, 
                [(0, 4294967295)], [], 
                '''                The number of packets transmitted from the source
                address to the destination address (this number
                includes error packets).
                ''',
                'matrixsdpkts',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'matrixSDEntry',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB.MatrixSDTable' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB.MatrixSDTable',
            False, 
            [
            _MetaInfoClassMember('matrixSDEntry', REFERENCE_LIST, 'MatrixSDEntry' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.MatrixSDTable.MatrixSDEntry', 
                [], [], 
                '''                A collection of statistics for communications between
                two addresses on a particular interface.
                ''',
                'matrixsdentry',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'matrixSDTable',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
    'RFC1271MIB' : {
        'meta_info' : _MetaInfoClass('RFC1271MIB',
            False, 
            [
            _MetaInfoClassMember('alarmTable', REFERENCE_CLASS, 'AlarmTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.AlarmTable', 
                [], [], 
                '''                A list of alarm entries.
                ''',
                'alarmtable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('bufferControlTable', REFERENCE_CLASS, 'BufferControlTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.BufferControlTable', 
                [], [], 
                '''                A list of buffers control entries.
                ''',
                'buffercontroltable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('captureBufferTable', REFERENCE_CLASS, 'CaptureBufferTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.CaptureBufferTable', 
                [], [], 
                '''                A list of packets captured off of a channel.
                ''',
                'capturebuffertable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('channelTable', REFERENCE_CLASS, 'ChannelTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.ChannelTable', 
                [], [], 
                '''                A list of packet channel entries.
                ''',
                'channeltable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherHistoryTable', REFERENCE_CLASS, 'EtherHistoryTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.EtherHistoryTable', 
                [], [], 
                '''                A list of Ethernet history entries.
                ''',
                'etherhistorytable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('etherStatsTable', REFERENCE_CLASS, 'EtherStatsTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.EtherStatsTable', 
                [], [], 
                '''                A list of Ethernet statistics entries.
                ''',
                'etherstatstable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('eventTable', REFERENCE_CLASS, 'EventTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.EventTable', 
                [], [], 
                '''                A list of events to be generated.
                ''',
                'eventtable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('filterTable', REFERENCE_CLASS, 'FilterTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.FilterTable', 
                [], [], 
                '''                A list of packet filter entries.
                ''',
                'filtertable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('historyControlTable', REFERENCE_CLASS, 'HistoryControlTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HistoryControlTable', 
                [], [], 
                '''                A list of history control entries.
                ''',
                'historycontroltable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostControlTable', REFERENCE_CLASS, 'HostControlTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostControlTable', 
                [], [], 
                '''                A list of host table control entries.
                ''',
                'hostcontroltable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTable', REFERENCE_CLASS, 'HostTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTable', 
                [], [], 
                '''                A list of host entries.
                ''',
                'hosttable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTimeTable', REFERENCE_CLASS, 'HostTimeTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTimeTable', 
                [], [], 
                '''                A list of time-ordered host table entries.
                ''',
                'hosttimetable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNControlTable', REFERENCE_CLASS, 'HostTopNControlTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTopNControlTable', 
                [], [], 
                '''                A list of top N host control entries.
                ''',
                'hosttopncontroltable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('hostTopNTable', REFERENCE_CLASS, 'HostTopNTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.HostTopNTable', 
                [], [], 
                '''                A list of top N host entries.
                ''',
                'hosttopntable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('logTable', REFERENCE_CLASS, 'LogTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.LogTable', 
                [], [], 
                '''                A list of events that have been logged.
                ''',
                'logtable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixControlTable', REFERENCE_CLASS, 'MatrixControlTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.MatrixControlTable', 
                [], [], 
                '''                A list of information entries for the
                traffic matrix on each interface.
                ''',
                'matrixcontroltable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixDSTable', REFERENCE_CLASS, 'MatrixDSTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.MatrixDSTable', 
                [], [], 
                '''                A list of traffic matrix entries indexed by
                destination and source MAC address.
                ''',
                'matrixdstable',
                'RFC1271-MIB', False),
            _MetaInfoClassMember('matrixSDTable', REFERENCE_CLASS, 'MatrixSDTable' , 'ydk.models.rfc1271.RFC1271_MIB', 'RFC1271MIB.MatrixSDTable', 
                [], [], 
                '''                A list of traffic matrix entries indexed by
                source and destination MAC address.
                ''',
                'matrixsdtable',
                'RFC1271-MIB', False),
            ],
            'RFC1271-MIB',
            'RFC1271-MIB',
            _yang_ns._namespaces['RFC1271-MIB'],
        'ydk.models.rfc1271.RFC1271_MIB'
        ),
    },
}
_meta_table['RFC1271MIB.AlarmTable.AlarmEntry']['meta_info'].parent =_meta_table['RFC1271MIB.AlarmTable']['meta_info']
_meta_table['RFC1271MIB.BufferControlTable.BufferControlEntry']['meta_info'].parent =_meta_table['RFC1271MIB.BufferControlTable']['meta_info']
_meta_table['RFC1271MIB.CaptureBufferTable.CaptureBufferEntry']['meta_info'].parent =_meta_table['RFC1271MIB.CaptureBufferTable']['meta_info']
_meta_table['RFC1271MIB.ChannelTable.ChannelEntry']['meta_info'].parent =_meta_table['RFC1271MIB.ChannelTable']['meta_info']
_meta_table['RFC1271MIB.EtherHistoryTable.EtherHistoryEntry']['meta_info'].parent =_meta_table['RFC1271MIB.EtherHistoryTable']['meta_info']
_meta_table['RFC1271MIB.EtherStatsTable.EtherStatsEntry']['meta_info'].parent =_meta_table['RFC1271MIB.EtherStatsTable']['meta_info']
_meta_table['RFC1271MIB.EventTable.EventEntry']['meta_info'].parent =_meta_table['RFC1271MIB.EventTable']['meta_info']
_meta_table['RFC1271MIB.FilterTable.FilterEntry']['meta_info'].parent =_meta_table['RFC1271MIB.FilterTable']['meta_info']
_meta_table['RFC1271MIB.HistoryControlTable.HistoryControlEntry']['meta_info'].parent =_meta_table['RFC1271MIB.HistoryControlTable']['meta_info']
_meta_table['RFC1271MIB.HostControlTable.HostControlEntry']['meta_info'].parent =_meta_table['RFC1271MIB.HostControlTable']['meta_info']
_meta_table['RFC1271MIB.HostTable.HostEntry']['meta_info'].parent =_meta_table['RFC1271MIB.HostTable']['meta_info']
_meta_table['RFC1271MIB.HostTimeTable.HostTimeEntry']['meta_info'].parent =_meta_table['RFC1271MIB.HostTimeTable']['meta_info']
_meta_table['RFC1271MIB.HostTopNControlTable.HostTopNControlEntry']['meta_info'].parent =_meta_table['RFC1271MIB.HostTopNControlTable']['meta_info']
_meta_table['RFC1271MIB.HostTopNTable.HostTopNEntry']['meta_info'].parent =_meta_table['RFC1271MIB.HostTopNTable']['meta_info']
_meta_table['RFC1271MIB.LogTable.LogEntry']['meta_info'].parent =_meta_table['RFC1271MIB.LogTable']['meta_info']
_meta_table['RFC1271MIB.MatrixControlTable.MatrixControlEntry']['meta_info'].parent =_meta_table['RFC1271MIB.MatrixControlTable']['meta_info']
_meta_table['RFC1271MIB.MatrixDSTable.MatrixDSEntry']['meta_info'].parent =_meta_table['RFC1271MIB.MatrixDSTable']['meta_info']
_meta_table['RFC1271MIB.MatrixSDTable.MatrixSDEntry']['meta_info'].parent =_meta_table['RFC1271MIB.MatrixSDTable']['meta_info']
_meta_table['RFC1271MIB.AlarmTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.BufferControlTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.CaptureBufferTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.ChannelTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.EtherHistoryTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.EtherStatsTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.EventTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.FilterTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.HistoryControlTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.HostControlTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.HostTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.HostTimeTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.HostTopNControlTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.HostTopNTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.LogTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.MatrixControlTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.MatrixDSTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
_meta_table['RFC1271MIB.MatrixSDTable']['meta_info'].parent =_meta_table['RFC1271MIB']['meta_info']
