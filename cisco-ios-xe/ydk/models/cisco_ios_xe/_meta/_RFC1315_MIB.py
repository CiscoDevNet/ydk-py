


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'Rfc1315Mib.FrameRelayGlobals.FrtrapstateEnum' : _MetaInfoEnum('FrtrapstateEnum', 'ydk.models.cisco_ios_xe.RFC1315_MIB',
        {
            'enabled':'enabled',
            'disabled':'disabled',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'Rfc1315Mib.FrameRelayGlobals' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib.FrameRelayGlobals',
            False, 
            [
            _MetaInfoClassMember('frTrapState', REFERENCE_ENUM_CLASS, 'FrtrapstateEnum' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.FrameRelayGlobals.FrtrapstateEnum', 
                [], [], 
                '''                This variable  indicates  whether  the  system
                produces the frDLCIStatusChange trap.
                ''',
                'frtrapstate',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frame-relay-globals',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
    'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum' : _MetaInfoEnum('FrdlcmiaddressEnum', 'ydk.models.cisco_ios_xe.RFC1315_MIB',
        {
            'q921':'q921',
            'q922March90':'q922March90',
            'q922November90':'q922November90',
            'q922':'q922',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum' : _MetaInfoEnum('FrdlcmiaddresslenEnum', 'ydk.models.cisco_ios_xe.RFC1315_MIB',
        {
            'two-octets':'two_octets',
            'three-octets':'three_octets',
            'four-octets':'four_octets',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum' : _MetaInfoEnum('FrdlcmimulticastEnum', 'ydk.models.cisco_ios_xe.RFC1315_MIB',
        {
            'nonBroadcast':'nonBroadcast',
            'broadcast':'broadcast',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum' : _MetaInfoEnum('FrdlcmistateEnum', 'ydk.models.cisco_ios_xe.RFC1315_MIB',
        {
            'noLmiConfigured':'noLmiConfigured',
            'lmiRev1':'lmiRev1',
            'ansiT1-617-D':'ansiT1_617_D',
            'ansiT1-617-B':'ansiT1_617_B',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'Rfc1315Mib.Frdlcmitable.Frdlcmientry' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib.Frdlcmitable.Frdlcmientry',
            False, 
            [
            _MetaInfoClassMember('frDlcmiIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The ifIndex value of the  corresponding  ifEn-
                try.
                ''',
                'frdlcmiifindex',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('frDlcmiAddress', REFERENCE_ENUM_CLASS, 'FrdlcmiaddressEnum' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddressEnum', 
                [], [], 
                '''                This variable states which address  format  is
                in use on the Frame Relay interface.
                ''',
                'frdlcmiaddress',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiAddressLen', REFERENCE_ENUM_CLASS, 'FrdlcmiaddresslenEnum' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmiaddresslenEnum', 
                [], [], 
                '''                This variable states which address  length  in
                octets.  In the case of Q922 format, the length
                indicates the entire length of the address  in-
                cluding the control portion.
                ''',
                'frdlcmiaddresslen',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiErrorThreshold', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This  is  the  maximum  number  of  unanswered
                Status Enquiries the equipment shall accept be-
                fore declaring the interface down.
                ''',
                'frdlcmierrorthreshold',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiFullEnquiryInterval', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                Number of status enquiry intervals  that  pass
                before  issuance  of a full status enquiry mes-
                sage.
                ''',
                'frdlcmifullenquiryinterval',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiMaxSupportedVCs', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The maximum number of Virtual Circuits allowed
                for  this  interface.   Usually dictated by the
                Frame Relay network.
                
                In response to a SET, if a value less than zero
                or  higher  than the agent's maximal capability
                is configured, the agent  should  respond  bad-
                Value
                ''',
                'frdlcmimaxsupportedvcs',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiMonitoredEvents', ATTRIBUTE, 'int' , None, None, 
                [('1', '10')], [], 
                '''                This is the number of status polling intervals
                over which the error threshold is counted.  For
                example, if within 'MonitoredEvents' number  of
                events  the  station  receives 'ErrorThreshold'
                number of errors, the interface  is  marked  as
                down.
                ''',
                'frdlcmimonitoredevents',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiMulticast', REFERENCE_ENUM_CLASS, 'FrdlcmimulticastEnum' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmimulticastEnum', 
                [], [], 
                '''                This indicates whether the Frame Relay  inter-
                face is using a multicast service.
                ''',
                'frdlcmimulticast',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiPollingInterval', ATTRIBUTE, 'int' , None, None, 
                [('5', '30')], [], 
                '''                This is the number of seconds between  succes-
                sive status enquiry messages.
                ''',
                'frdlcmipollinginterval',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiState', REFERENCE_ENUM_CLASS, 'FrdlcmistateEnum' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frdlcmitable.Frdlcmientry.FrdlcmistateEnum', 
                [], [], 
                '''                This variable states which Data  Link  Connec-
                tion Management scheme is active (and by impli-
                cation, what DLCI it uses) on the  Frame  Relay
                interface.
                ''',
                'frdlcmistate',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frDlcmiEntry',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
    'Rfc1315Mib.Frdlcmitable' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib.Frdlcmitable',
            False, 
            [
            _MetaInfoClassMember('frDlcmiEntry', REFERENCE_LIST, 'Frdlcmientry' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frdlcmitable.Frdlcmientry', 
                [], [], 
                '''                The Parameters for a particular Data Link Con-
                nection Management Interface.
                ''',
                'frdlcmientry',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frDlcmiTable',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
    'Rfc1315Mib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum' : _MetaInfoEnum('FrcircuitstateEnum', 'ydk.models.cisco_ios_xe.RFC1315_MIB',
        {
            'invalid':'invalid',
            'active':'active',
            'inactive':'inactive',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'Rfc1315Mib.Frcircuittable.Frcircuitentry' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib.Frcircuittable.Frcircuitentry',
            False, 
            [
            _MetaInfoClassMember('frCircuitIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The ifIndex Value of the ifEntry this  virtual
                circuit is layered onto.
                ''',
                'frcircuitifindex',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('frCircuitDlci', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The Data Link Connection Identifier  for  this
                virtual circuit.
                ''',
                'frcircuitdlci',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('frCircuitCommittedBurst', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This variable indicates the maximum amount  of
                data,  in  bits,  that  the  network  agrees to
                transfer under normal  conditions,  during  the
                measurement interval.
                ''',
                'frcircuitcommittedburst',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitCreationTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when the  virtual  cir-
                cuit was created, whether by the Data Link Con-
                nection Management Interface  or  by  a  SetRe-
                quest.
                ''',
                'frcircuitcreationtime',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitExcessBurst', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                This variable indicates the maximum amount  of
                uncommitted data bits that the network will at-
                tempt to deliver over the measurement interval.
                
                By default, if not configured when creating the
                entry, the Excess Information Burst Size is set
                to the value of ifSpeed.
                ''',
                'frcircuitexcessburst',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitLastTimeChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime when last there  was  a
                change in the virtual circuit state
                ''',
                'frcircuitlasttimechange',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedBECNs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames received from the network in-
                dicating  backward congestion since the virtual
                circuit was created.
                ''',
                'frcircuitreceivedbecns',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedFECNs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames received from the network in-
                dicating  forward  congestion since the virtual
                circuit was created.
                ''',
                'frcircuitreceivedfecns',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of frames received  over  this  virtual
                circuit since it was created.
                ''',
                'frcircuitreceivedframes',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitReceivedOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of octets received  over  this  virtual
                circuit since it was created.
                ''',
                'frcircuitreceivedoctets',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitSentFrames', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of frames sent  from  this  virtual
                circuit since it was created.
                ''',
                'frcircuitsentframes',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitSentOctets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of octets sent  from  this  virtual
                circuit since it was created.
                ''',
                'frcircuitsentoctets',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitState', REFERENCE_ENUM_CLASS, 'FrcircuitstateEnum' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frcircuittable.Frcircuitentry.FrcircuitstateEnum', 
                [], [], 
                '''                Indicates whether the particular virtual  cir-
                cuit  is operational.  In the absence of a Data
                Link Connection Management  Interface,  virtual
                circuit  entries  (rows) may be created by set-
                ting virtual  circuit  state  to  'active',  or
                deleted by changing Circuit state to 'invalid'.
                Whether or not the row actually  disappears  is
                left  to the implementation, so this object may
                actually read as 'invalid' for  some  arbitrary
                length  of  time.   It is also legal to set the
                state of a virtual  circuit  to  'inactive'  to
                temporarily disable a given circuit.
                ''',
                'frcircuitstate',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitThroughput', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                Throughput is the average number of 'Frame Re-
                lay  Information  Field'  bits  transferred per
                second across a user network interface  in  one
                direction, measured over the measurement inter-
                val.
                
                If the  configured  committed  burst  rate  and
                throughput  are  both non-zero, the measurement
                interval
                T=frCircuitCommittedBurst/frCircuitThroughput.
                
                If the  configured  committed  burst  rate  and
                throughput  are  both zero, the measurement in-
                terval
                       T=frCircuitExcessBurst/ifSpeed.
                ''',
                'frcircuitthroughput',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frCircuitEntry',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
    'Rfc1315Mib.Frcircuittable' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib.Frcircuittable',
            False, 
            [
            _MetaInfoClassMember('frCircuitEntry', REFERENCE_LIST, 'Frcircuitentry' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frcircuittable.Frcircuitentry', 
                [], [], 
                '''                The information regarding a single  Data  Link
                Connection Identifier.
                ''',
                'frcircuitentry',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frCircuitTable',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
    'Rfc1315Mib.Frerrtable.Frerrentry.FrerrtypeEnum' : _MetaInfoEnum('FrerrtypeEnum', 'ydk.models.cisco_ios_xe.RFC1315_MIB',
        {
            'unknownError':'unknownError',
            'receiveShort':'receiveShort',
            'receiveLong':'receiveLong',
            'illegalDLCI':'illegalDLCI',
            'unknownDLCI':'unknownDLCI',
            'dlcmiProtoErr':'dlcmiProtoErr',
            'dlcmiUnknownIE':'dlcmiUnknownIE',
            'dlcmiSequenceErr':'dlcmiSequenceErr',
            'dlcmiUnknownRpt':'dlcmiUnknownRpt',
            'noErrorSinceReset':'noErrorSinceReset',
        }, 'RFC1315-MIB', _yang_ns._namespaces['RFC1315-MIB']),
    'Rfc1315Mib.Frerrtable.Frerrentry' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib.Frerrtable.Frerrentry',
            False, 
            [
            _MetaInfoClassMember('frErrIfIndex', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The ifIndex Value of the  corresponding  ifEn-
                try.
                ''',
                'frerrifindex',
                'RFC1315-MIB', True),
            _MetaInfoClassMember('frErrData', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                An octet string containing as much of the  er-
                ror  packet as possible.  As a minimum, it must
                contain the Q.922 Address or  as  much  as  was
                delivered.   It is desirable to include all in-
                formation up to the PDU.
                ''',
                'frerrdata',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frErrTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The value of sysUpTime at which the error  was
                detected.
                ''',
                'frerrtime',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frErrType', REFERENCE_ENUM_CLASS, 'FrerrtypeEnum' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frerrtable.Frerrentry.FrerrtypeEnum', 
                [], [], 
                '''                The type of error that was last seen  on  this
                interface.
                ''',
                'frerrtype',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frErrEntry',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
    'Rfc1315Mib.Frerrtable' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib.Frerrtable',
            False, 
            [
            _MetaInfoClassMember('frErrEntry', REFERENCE_LIST, 'Frerrentry' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frerrtable.Frerrentry', 
                [], [], 
                '''                The error information for a single frame relay
                interface.
                ''',
                'frerrentry',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'frErrTable',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
    'Rfc1315Mib' : {
        'meta_info' : _MetaInfoClass('Rfc1315Mib',
            False, 
            [
            _MetaInfoClassMember('frame-relay-globals', REFERENCE_CLASS, 'FrameRelayGlobals' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.FrameRelayGlobals', 
                [], [], 
                '''                ''',
                'frame_relay_globals',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frCircuitTable', REFERENCE_CLASS, 'Frcircuittable' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frcircuittable', 
                [], [], 
                '''                A table containing information about specific Data
                Link Connection Identifiers and corresponding virtual
                circuits.
                ''',
                'frcircuittable',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frDlcmiTable', REFERENCE_CLASS, 'Frdlcmitable' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frdlcmitable', 
                [], [], 
                '''                The Parameters for the Data Link Connection Management
                Interface for the frame relay service on this
                interface.
                ''',
                'frdlcmitable',
                'RFC1315-MIB', False),
            _MetaInfoClassMember('frErrTable', REFERENCE_CLASS, 'Frerrtable' , 'ydk.models.cisco_ios_xe.RFC1315_MIB', 'Rfc1315Mib.Frerrtable', 
                [], [], 
                '''                A table containing information about Errors on the
                Frame Relay interface.
                ''',
                'frerrtable',
                'RFC1315-MIB', False),
            ],
            'RFC1315-MIB',
            'RFC1315-MIB',
            _yang_ns._namespaces['RFC1315-MIB'],
        'ydk.models.cisco_ios_xe.RFC1315_MIB'
        ),
    },
}
_meta_table['Rfc1315Mib.Frdlcmitable.Frdlcmientry']['meta_info'].parent =_meta_table['Rfc1315Mib.Frdlcmitable']['meta_info']
_meta_table['Rfc1315Mib.Frcircuittable.Frcircuitentry']['meta_info'].parent =_meta_table['Rfc1315Mib.Frcircuittable']['meta_info']
_meta_table['Rfc1315Mib.Frerrtable.Frerrentry']['meta_info'].parent =_meta_table['Rfc1315Mib.Frerrtable']['meta_info']
_meta_table['Rfc1315Mib.FrameRelayGlobals']['meta_info'].parent =_meta_table['Rfc1315Mib']['meta_info']
_meta_table['Rfc1315Mib.Frdlcmitable']['meta_info'].parent =_meta_table['Rfc1315Mib']['meta_info']
_meta_table['Rfc1315Mib.Frcircuittable']['meta_info'].parent =_meta_table['Rfc1315Mib']['meta_info']
_meta_table['Rfc1315Mib.Frerrtable']['meta_info'].parent =_meta_table['Rfc1315Mib']['meta_info']
