


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'QosserviceEnum' : _MetaInfoEnum('QosserviceEnum', 'ydk.models.cisco_ios_xe.INT_SERV_MIB',
        {
            'bestEffort':'bestEffort',
            'guaranteedDelay':'guaranteedDelay',
            'controlledLoad':'controlledLoad',
        }, 'INT-SERV-MIB', _yang_ns._namespaces['INT-SERV-MIB']),
    'IntServMib.Intsrvgenobjects' : {
        'meta_info' : _MetaInfoClass('IntServMib.Intsrvgenobjects',
            False, 
            [
            _MetaInfoClassMember('intSrvFlowNewIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This  object  is  used  to  assign  values  to
                intSrvFlowNumber  as described in 'Textual Con-
                ventions  for  SNMPv2'.   The  network  manager
                reads  the  object,  and  then writes the value
                back in the SET that creates a new instance  of
                intSrvFlowEntry.   If  the  SET  fails with the
                code 'inconsistentValue', then the process must
                be  repeated; If the SET succeeds, then the ob-
                ject is incremented, and the  new  instance  is
                created according to the manager's directions.
                ''',
                'intsrvflownewindex',
                'INT-SERV-MIB', False),
            ],
            'INT-SERV-MIB',
            'intSrvGenObjects',
            _yang_ns._namespaces['INT-SERV-MIB'],
        'ydk.models.cisco_ios_xe.INT_SERV_MIB'
        ),
    },
    'IntServMib.Intsrvifattribtable.Intsrvifattribentry' : {
        'meta_info' : _MetaInfoClass('IntServMib.Intsrvifattribtable.Intsrvifattribentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'INT-SERV-MIB', True),
            _MetaInfoClassMember('intSrvIfAttribAllocatedBits', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of bits/second currently  allocated
                to reserved sessions on the interface.
                ''',
                'intsrvifattriballocatedbits',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvIfAttribAllocatedBuffer', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The amount of buffer space  required  to  hold
                the simultaneous burst of all reserved flows on
                the interface.
                ''',
                'intsrvifattriballocatedbuffer',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvIfAttribFlows', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of reserved flows currently  active
                on  this  interface.  A flow can be created ei-
                ther from a reservation protocol (such as  RSVP
                or ST-II) or via configuration information.
                ''',
                'intsrvifattribflows',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvIfAttribMaxAllocatedBits', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The maximum number of bits/second that may  be
                allocated  to  reserved  sessions on the inter-
                face.
                ''',
                'intsrvifattribmaxallocatedbits',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvIfAttribPropagationDelay', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The amount of propagation delay that this  in-
                terface  introduces  in addition to that intro-
                diced by bit propagation delays.
                ''',
                'intsrvifattribpropagationdelay',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvIfAttribStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' on interfaces that are configured for
                RSVP.
                ''',
                'intsrvifattribstatus',
                'INT-SERV-MIB', False),
            ],
            'INT-SERV-MIB',
            'intSrvIfAttribEntry',
            _yang_ns._namespaces['INT-SERV-MIB'],
        'ydk.models.cisco_ios_xe.INT_SERV_MIB'
        ),
    },
    'IntServMib.Intsrvifattribtable' : {
        'meta_info' : _MetaInfoClass('IntServMib.Intsrvifattribtable',
            False, 
            [
            _MetaInfoClassMember('intSrvIfAttribEntry', REFERENCE_LIST, 'Intsrvifattribentry' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'IntServMib.Intsrvifattribtable.Intsrvifattribentry', 
                [], [], 
                '''                The reservable attributes of  a  given  inter-
                face.
                ''',
                'intsrvifattribentry',
                'INT-SERV-MIB', False),
            ],
            'INT-SERV-MIB',
            'intSrvIfAttribTable',
            _yang_ns._namespaces['INT-SERV-MIB'],
        'ydk.models.cisco_ios_xe.INT_SERV_MIB'
        ),
    },
    'IntServMib.Intsrvflowtable.Intsrvflowentry.IntsrvflowownerEnum' : _MetaInfoEnum('IntsrvflowownerEnum', 'ydk.models.cisco_ios_xe.INT_SERV_MIB',
        {
            'other':'other',
            'rsvp':'rsvp',
            'management':'management',
        }, 'INT-SERV-MIB', _yang_ns._namespaces['INT-SERV-MIB']),
    'IntServMib.Intsrvflowtable.Intsrvflowentry' : {
        'meta_info' : _MetaInfoClass('IntServMib.Intsrvflowtable.Intsrvflowentry',
            False, 
            [
            _MetaInfoClassMember('intSrvFlowNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The number of this flow.  This is for SNMP In-
                dexing purposes only and has no relation to any
                protocol value.
                ''',
                'intsrvflownumber',
                'INT-SERV-MIB', True),
            _MetaInfoClassMember('intSrvFlowBestEffort', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets that  were  remanded  to
                best effort service.
                ''',
                'intsrvflowbesteffort',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The size of the largest  burst  expected  from
                the sender at a time.
                
                If this is less than  the  sender's  advertised
                burst  size, the receiver is asking the network
                to provide flow pacing  beyond  what  would  be
                provided  under normal circumstances. Such pac-
                ing is at the network's option.
                ''',
                'intsrvflowburst',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The destination address used by all senders in
                this  session.   This object may not be changed
                when the value of the RowStatus object is  'ac-
                tive'.
                ''',
                'intsrvflowdestaddr',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowDestAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The length of the destination address in bits.
                This  is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'intsrvflowdestaddrlength',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowDestPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The UDP or TCP port number used as a  destina-
                tion  port for all senders in this session.  If
                the  IP   protocol   in   use,   specified   by
                intSrvResvFwdProtocol,  is 50 (ESP) or 51 (AH),
                this  represents  a  virtual  destination  port
                number.   A value of zero indicates that the IP
                protocol in use does not have ports.  This  ob-
                ject  may  not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'intsrvflowdestport',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowDiscard', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If 'true', the flow  is  to  incur  loss  when
                traffic is policed.  If 'false', policed traff-
                ic is treated as best effort traffic.
                ''',
                'intsrvflowdiscard',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowFlowId', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                The flow ID that  this  sender  is  using,  if
                this  is  an IPv6 session.
                ''',
                'intsrvflowflowid',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowIfAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The IP Address on the ifEntry  on  which  this
                reservation  exists.  This is present primarily
                to support those interfaces which layer  multi-
                ple IP Addresses on the interface.
                ''',
                'intsrvflowifaddr',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowInterface', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The ifIndex value of the  interface  on  which
                this reservation exists.
                ''',
                'intsrvflowinterface',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowMaxTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The maximum datagram size for this  flow  that
                will conform to the traffic specification. This
                value cannot exceed the MTU of the interface.
                ''',
                'intsrvflowmaxtu',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowMinTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The minimum message size for  this  flow.  The
                policing  algorithm will treat smaller messages
                as though they are this size.
                ''',
                'intsrvflowmintu',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowOrder', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                In the event of ambiguity, the order in  which
                the  classifier  should  make  its comparisons.
                The row with intSrvFlowOrder=0 is tried  first,
                and  comparisons  proceed  in  the order of in-
                creasing value.  Non-serial implementations  of
                the classifier should emulate this behavior.
                ''',
                'intsrvfloworder',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowOwner', REFERENCE_ENUM_CLASS, 'IntsrvflowownerEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'IntServMib.Intsrvflowtable.Intsrvflowentry.IntsrvflowownerEnum', 
                [], [], 
                '''                The process that installed this  flow  in  the
                queue policy database.
                ''',
                'intsrvflowowner',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowPoliced', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number of packets policed since the incep-
                tion of the flow's service.
                ''',
                'intsrvflowpoliced',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The UDP or TCP port number used  as  a  source
                port  for  this sender in this session.  If the
                IP    protocol    in    use,    specified    by
                intSrvResvFwdProtocol  is  50 (ESP) or 51 (AH),
                this represents a generalized  port  identifier
                (GPI).   A  value of zero indicates that the IP
                protocol in use does not have ports.  This  ob-
                ject  may  not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'intsrvflowport',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowProtocol', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The IP Protocol used by a session.   This  ob-
                ject  may  not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'intsrvflowprotocol',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowQueue', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The number of the queue used by this  traffic.
                Note  that the interpretation of this object is
                implementation-specific,   as   implementations
                vary in their use of queue identifiers.
                ''',
                'intsrvflowqueue',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The Reserved Rate of the sender's data stream.
                If this is a Controlled Load service flow, this
                rate is derived from the Tspec  rate  parameter
                (r).   If  this  is  a Guaranteed service flow,
                this rate is derived from  the  Rspec  clearing
                rate parameter (R).
                ''',
                'intsrvflowrate',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowSenderAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The source address of the sender  selected  by
                this  reservation.  The value of all zeroes in-
                dicates 'all senders'.  This object may not  be
                changed  when the value of the RowStatus object
                is 'active'.
                ''',
                'intsrvflowsenderaddr',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowSenderAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The length of the sender's  address  in  bits.
                This  is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'intsrvflowsenderaddrlength',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowService', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The QoS service being applied to this flow.
                ''',
                'intsrvflowservice',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' for all active  flows.   This  object
                may be used to install static classifier infor-
                mation, delete classifier information,  or  au-
                thorize such.
                ''',
                'intsrvflowstatus',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowType', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The type of session (IP4, IP6, IP6  with  flow
                information, etc).
                ''',
                'intsrvflowtype',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvFlowWeight', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The weight used  to  prioritize  the  traffic.
                Note  that the interpretation of this object is
                implementation-specific,   as   implementations
                vary in their use of weighting procedures.
                ''',
                'intsrvflowweight',
                'INT-SERV-MIB', False),
            ],
            'INT-SERV-MIB',
            'intSrvFlowEntry',
            _yang_ns._namespaces['INT-SERV-MIB'],
        'ydk.models.cisco_ios_xe.INT_SERV_MIB'
        ),
    },
    'IntServMib.Intsrvflowtable' : {
        'meta_info' : _MetaInfoClass('IntServMib.Intsrvflowtable',
            False, 
            [
            _MetaInfoClassMember('intSrvFlowEntry', REFERENCE_LIST, 'Intsrvflowentry' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'IntServMib.Intsrvflowtable.Intsrvflowentry', 
                [], [], 
                '''                Information describing the use of a given  in-
                terface   by   a   given   flow.   The  counter
                intSrvFlowPoliced starts counting  at  the  in-
                stallation of the flow.
                ''',
                'intsrvflowentry',
                'INT-SERV-MIB', False),
            ],
            'INT-SERV-MIB',
            'intSrvFlowTable',
            _yang_ns._namespaces['INT-SERV-MIB'],
        'ydk.models.cisco_ios_xe.INT_SERV_MIB'
        ),
    },
    'IntServMib' : {
        'meta_info' : _MetaInfoClass('IntServMib',
            False, 
            [
            _MetaInfoClassMember('intSrvFlowTable', REFERENCE_CLASS, 'Intsrvflowtable' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'IntServMib.Intsrvflowtable', 
                [], [], 
                '''                Information describing the reserved flows  us-
                ing the system's interfaces.
                ''',
                'intsrvflowtable',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvGenObjects', REFERENCE_CLASS, 'Intsrvgenobjects' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'IntServMib.Intsrvgenobjects', 
                [], [], 
                '''                ''',
                'intsrvgenobjects',
                'INT-SERV-MIB', False),
            _MetaInfoClassMember('intSrvIfAttribTable', REFERENCE_CLASS, 'Intsrvifattribtable' , 'ydk.models.cisco_ios_xe.INT_SERV_MIB', 'IntServMib.Intsrvifattribtable', 
                [], [], 
                '''                The reservable attributes of the system's  in-
                terfaces.
                ''',
                'intsrvifattribtable',
                'INT-SERV-MIB', False),
            ],
            'INT-SERV-MIB',
            'INT-SERV-MIB',
            _yang_ns._namespaces['INT-SERV-MIB'],
        'ydk.models.cisco_ios_xe.INT_SERV_MIB'
        ),
    },
}
_meta_table['IntServMib.Intsrvifattribtable.Intsrvifattribentry']['meta_info'].parent =_meta_table['IntServMib.Intsrvifattribtable']['meta_info']
_meta_table['IntServMib.Intsrvflowtable.Intsrvflowentry']['meta_info'].parent =_meta_table['IntServMib.Intsrvflowtable']['meta_info']
_meta_table['IntServMib.Intsrvgenobjects']['meta_info'].parent =_meta_table['IntServMib']['meta_info']
_meta_table['IntServMib.Intsrvifattribtable']['meta_info'].parent =_meta_table['IntServMib']['meta_info']
_meta_table['IntServMib.Intsrvflowtable']['meta_info'].parent =_meta_table['IntServMib']['meta_info']
