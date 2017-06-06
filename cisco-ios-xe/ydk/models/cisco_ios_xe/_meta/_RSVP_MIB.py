


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'RsvpencapsulationEnum' : _MetaInfoEnum('RsvpencapsulationEnum', 'ydk.models.cisco_ios_xe.RSVP_MIB',
        {
            'ip':'ip',
            'udp':'udp',
            'both':'both',
        }, 'RSVP-MIB', _yang_ns._namespaces['RSVP-MIB']),
    'RsvpMib.Rsvpgenobjects' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpgenobjects',
            False, 
            [
            _MetaInfoClassMember('rsvpBadPackets', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This object	keeps a	count of the number of bad
                RSVP	packets	received.
                ''',
                'rsvpbadpackets',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdNewIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This  object  is  used  to	assign	values	to
                rsvpResvFwdNumber   as  described  in  'Textual
                Conventions for SNMPv2'.  The  network  manager
                reads  the  object,	and  then writes the value
                back	in the SET that	creates	a new instance	of
                rsvpResvFwdEntry.   If  the	SET fails with the
                code	'inconsistentValue', then the process must
                be  repeated;  If  the  SET	succeeds, then the
                object is incremented, and the new instance	is
                created according to	the manager's directions.
                ''',
                'rsvpresvfwdnewindex',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvNewIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This  object  is  used  to	assign	values	to
                rsvpResvNumber   as	 described   in	  'Textual
                Conventions for SNMPv2'.  The  network  manager
                reads  the  object,	and  then writes the value
                back	in the SET that	creates	a new instance	of
                rsvpResvEntry.   If the SET fails with the code
                'inconsistentValue',	then the process  must	be
                repeated;  If the SET succeeds, then	the object
                is incremented, and the new instance	is created
                according to	the manager's directions.
                ''',
                'rsvpresvnewindex',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderNewIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This  object  is  used  to	assign	values	to
                rsvpSenderNumber   as   described  in  'Textual
                Conventions for SNMPv2'.  The  network  manager
                reads  the  object,	and  then writes the value
                back	in the SET that	creates	a new instance	of
                rsvpSenderEntry.   If  the  SET  fails with the
                code	'inconsistentValue', then the process must
                be  repeated;  If  the  SET	succeeds, then the
                object is incremented, and the new instance	is
                created according to	the manager's directions.
                ''',
                'rsvpsendernewindex',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionNewIndex', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This  object  is  used  to	assign	values	to
                rsvpSessionNumber   as  described  in  'Textual
                Conventions for SNMPv2'.  The  network  manager
                reads  the  object,	and  then writes the value
                back	in the SET that	creates	a new instance	of
                rsvpSessionEntry.   If  the	SET fails with the
                code	'inconsistentValue', then the process must
                be  repeated;  If  the  SET	succeeds, then the
                object is incremented, and the new instance	is
                created according to	the manager's directions.
                ''',
                'rsvpsessionnewindex',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpGenObjects',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpsessiontable.Rsvpsessionentry' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpsessiontable.Rsvpsessionentry',
            False, 
            [
            _MetaInfoClassMember('rsvpSessionNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	number of this session.	 This is for  SNMP
                Indexing  purposes  only and	has no relation	to
                any protocol	value.
                ''',
                'rsvpsessionnumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpSessionDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	destination address used by all	senders	in
                this	 session.   This object	may not	be changed
                when	the  value  of	the  RowStatus	object	is
                'active'.
                ''',
                'rsvpsessiondestaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionDestAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The	CIDR prefix length of the session address,
                which   is	32  for	 IP4  host  and	 multicast
                addresses, and 128  for  IP6	 addresses.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpsessiondestaddrlength',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The	 UDP  or  TCP  port  number  used   as	 a
                destination	 port  for  all	 senders  in  this
                session.  If	the IP protocol	in use,	 specified
                by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH),
                this	 represents  a	virtual	 destination  port
                number.   A value of	zero indicates that the	IP
                protocol in use  does  not  have  ports.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpsessionport',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionProtocol', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	IP Protocol used by  this  session.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpsessionprotocol',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionReceivers', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	number of reservations being requested	of
                this	system for this	session.
                ''',
                'rsvpsessionreceivers',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	number of reservation requests this system
                is sending upstream for this	session.
                ''',
                'rsvpsessionrequests',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionSenders', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	number of distinct senders currently known
                to be part of this session.
                ''',
                'rsvpsessionsenders',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionType', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	type of	session	(IP4, IP6, IP6	with  flow
                information,	etc).
                ''',
                'rsvpsessiontype',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpSessionEntry',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpsessiontable' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpsessiontable',
            False, 
            [
            _MetaInfoClassMember('rsvpSessionEntry', REFERENCE_LIST, 'Rsvpsessionentry' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpsessiontable.Rsvpsessionentry', 
                [], [], 
                '''                A single session seen by a given system.
                ''',
                'rsvpsessionentry',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpSessionTable',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpsendertable.Rsvpsenderentry' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpsendertable.Rsvpsenderentry',
            False, 
            [
            _MetaInfoClassMember('rsvpSessionNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                ''',
                'rsvpsessionnumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpSenderNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	number of this sender.	This is	 for  SNMP
                Indexing  purposes  only and	has no relation	to
                any protocol	value.
                ''',
                'rsvpsendernumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpSenderAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	source address used by this sender in this
                session.   This  object may not be changed when
                the value of	the RowStatus object is	'active'.
                ''',
                'rsvpsenderaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The	length of the sender's	address	 in  bits.
                This	 is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpsenderaddrlength',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecBreak', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                The	global break bit general  characterization
                parameter  from  the	ADSPEC.	 If TRUE, at least
                one non-IS hop was detected in  the	path.	If
                FALSE, no non-IS hops were detected.
                ''',
                'rsvpsenderadspecbreak',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecCtrlLoadBreak', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, the Controlled Load Service  fragment
                has its 'break' bit set, indicating that one	or
                more	nodes along the	path do	 not  support  the
                controlled	load   service.	   If  FALSE,  and
                rsvpSenderAdspecCtrlLoadSvc	 is   TRUE,    the
                'break' bit is not set.
                
                If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this
                returns FALSE or noSuchValue.
                ''',
                'rsvpsenderadspecctrlloadbreak',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecCtrlLoadHopCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this
                is  the  service-specific  override	of the hop
                count general characterization  parameter  from
                the	ADSPEC.	  A  return of zero or noSuchValue
                indicates one of the	following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecctrlloadhopcount',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecCtrlLoadMinLatency', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this
                is the service-specific override of the minimum
                path	latency	general	characterization parameter
                from	  the	ADSPEC.	   A  return  of  zero	or
                noSuchValue	indicates  one	of  the	 following
                conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecctrlloadminlatency',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecCtrlLoadMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this
                is	the   service-specific	 override  of  the
                composed  Maximum  Transmission  Unit   general
                characterization  parameter from the	ADSPEC.	 A
                return of zero or noSuchValue indicates one	of
                the following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecctrlloadmtu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecCtrlLoadPathBw', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If rsvpSenderAdspecCtrlLoadSvc is  TRUE,  this
                is  the  service-specific  override of the path
                bandwidth  estimate	general	  characterization
                parameter from the ADSPEC.  A return	of zero	or
                noSuchValue	indicates  one	of  the	 following
                conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecCtrlLoadSvc is  FALSE,  this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecctrlloadpathbw',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecCtrlLoadSvc', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, the ADSPEC	contains a Controlled Load
                Service  fragment.	If  FALSE, the ADSPEC does
                not	 contain   a   Controlled   Load   Service
                fragment.
                ''',
                'rsvpsenderadspecctrlloadsvc',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedBreak', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, the Guaranteed Service  fragment  has
                its	'break'	 bit  set,  indicating that one	or
                more	nodes along the	path do	 not  support  the
                guaranteed	  service.     If    FALSE,    and
                rsvpSenderAdspecGuaranteedSvc  is   TRUE,   the
                'break' bit is not set.
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns FALSE or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteedbreak',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedCsum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is	the  composed  value  for  the	guaranteed
                service 'C' parameter since the last	 reshaping
                point.    A	 return	 of  zero  or  noSuchValue
                indicates one of the	following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteedcsum',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedCtot', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is	the  end-to-end	 composed  value  for  the
                guaranteed service 'C' parameter.  A	return	of
                zero	  or  noSuchValue  indicates  one  of  the
                following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteedctot',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedDsum', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is	the  composed  value  for  the	guaranteed
                service 'D' parameter since the last	 reshaping
                point.    A	 return	 of  zero  or  noSuchValue
                indicates one of the	following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteeddsum',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedDtot', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is	the  end-to-end	 composed  value  for  the
                guaranteed service 'D' parameter.  A	return	of
                zero	  or  noSuchValue  indicates  one  of  the
                following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteeddtot',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedHopCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is  the  service-specific  override	of the hop
                count general characterization  parameter  from
                the	ADSPEC.	  A  return of zero or noSuchValue
                indicates one of the	following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteedhopcount',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedMinLatency', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is the service-specific override of the minimum
                path	latency	general	characterization parameter
                from	  the	ADSPEC.	   A  return  of  zero	or
                noSuchValue	indicates  one	of  the	 following
                conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteedminlatency',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is	the   service-specific	 override  of  the
                composed  Maximum  Transmission  Unit   general
                characterization  parameter from the	ADSPEC.	 A
                return of zero or noSuchValue indicates one	of
                the following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteedmtu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedPathBw', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If rsvpSenderAdspecGuaranteedSvc is	TRUE, this
                is  the  service-specific  override of the path
                bandwidth  estimate	general	  characterization
                parameter from the ADSPEC.  A return	of zero	or
                noSuchValue	indicates  one	of  the	 following
                conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                
                If rsvpSenderAdspecGuaranteedSvc is FALSE, this
                returns zero	or noSuchValue.
                ''',
                'rsvpsenderadspecguaranteedpathbw',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecGuaranteedSvc', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE,  the  ADSPEC  contains  a	Guaranteed
                Service  fragment.	If  FALSE, the ADSPEC does
                not contain a Guaranteed Service fragment.
                ''',
                'rsvpsenderadspecguaranteedsvc',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecHopCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The	  hop	count	general	  characterization
                parameter from the ADSPEC.  A return	of zero	or
                noSuchValue	indicates  one	of  the	 following
                conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                ''',
                'rsvpsenderadspechopcount',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecMinLatency', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The	   minimum    path     latency	   general
                characterization  parameter from the	ADSPEC.	 A
                return of zero or noSuchValue indicates one	of
                the following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                ''',
                'rsvpsenderadspecminlatency',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecMtu', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                The	composed Maximum Transmission Unit general
                characterization  parameter from the	ADSPEC.	 A
                return of zero or noSuchValue indicates one	of
                the following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                ''',
                'rsvpsenderadspecmtu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderAdspecPathBw', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	  path	  bandwidth    estimate	   general
                characterization  parameter from the	ADSPEC.	 A
                return of zero or noSuchValue indicates one	of
                the following conditions:
                
                   the invalid bit was set
                   the parameter was	not present
                ''',
                'rsvpsenderadspecpathbw',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	destination address used by all	senders	in
                this	 session.   This object	may not	be changed
                when	the  value  of	the  RowStatus	object	is
                'active'.
                ''',
                'rsvpsenderdestaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderDestAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The	length of the destination address in bits.
                This	 is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpsenderdestaddrlength',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderDestPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The	 UDP  or  TCP  port  number  used   as	 a
                destination	 port  for  all	 senders  in  this
                session.  If	the IP protocol	in use,	 specified
                by  rsvpSenderProtocol, is 50 (ESP) or 51 (AH),
                this	 represents  a	virtual	 destination  port
                number.   A value of	zero indicates that the	IP
                protocol in use  does  not  have  ports.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpsenderdestport',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderFlowId', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                The	flow ID	that  this  sender  is	using,	if
                this	 is  an	IPv6 session.
                ''',
                'rsvpsenderflowid',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	address	used  by  the  previous	 RSVP  hop
                (which may be the original sender).
                ''',
                'rsvpsenderhopaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderHopLih', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The	 Logical  Interface  Handle  used  by  the
                previous  RSVP  hop	(which may be the original
                sender).
                ''',
                'rsvpsenderhoplih',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderInterface', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The	ifIndex	value of the  interface	 on  which
                this	PATH message was most recently received.
                ''',
                'rsvpsenderinterface',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	 interval  between  refresh  messages	as
                advertised by the Previous Hop.
                ''',
                'rsvpsenderinterval',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	time of	 the  last  change  in	this  PATH
                message;  This  is either the first time it was
                received or the time	of the most recent  change
                in parameters.
                ''',
                'rsvpsenderlastchange',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderPolicy', ATTRIBUTE, 'str' , None, None, 
                [(4, 65536)], [], 
                '''                The	contents of the	policy	object,	 displayed
                as an uninterpreted string of octets, including
                the object header.  In the absence of  such	an
                object, this	should be of zero length.
                ''',
                'rsvpsenderpolicy',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The	UDP or TCP port	number used  as	 a  source
                port	 for  this sender in this session.  If the
                IP	 protocol    in	   use,	   specified	by
                rsvpSenderProtocol is 50 (ESP) or 51	(AH), this
                represents a	generalized port identifier (GPI).
                A  value of zero indicates that the IP protocol
                in use does not have	ports.	 This  object  may
                not	be changed when	the value of the RowStatus
                object is 'active'.
                ''',
                'rsvpsenderport',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderProtocol', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	IP Protocol used by  this  session.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpsenderprotocol',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderRSVPHop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, the node believes that  the  previous
                IP  hop  is	an  RSVP  hop.	If FALSE, the node
                believes that the previous IP hop may not be	an
                RSVP	hop.
                ''',
                'rsvpsenderrsvphop',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' for all active PATH  messages.   This
                object  may	be  used  to  install  static PATH
                information or delete PATH information.
                ''',
                'rsvpsenderstatus',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderTSpecBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	size of	the largest  burst  expected  from
                the sender at a time.
                ''',
                'rsvpsendertspecburst',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderTSpecMaxTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	maximum	message	size for  this	flow.  The
                admission  algorithm	 will  reject TSpecs whose
                Maximum Transmission	Unit, plus  the	 interface
                headers, exceed the interface MTU.
                ''',
                'rsvpsendertspecmaxtu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderTSpecMinTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	minimum	message	size for  this	flow.  The
                policing  algorithm will treat smaller messages
                as though they are this size.
                ''',
                'rsvpsendertspecmintu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderTSpecPeakRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	Peak Bit Rate of the sender's data stream.
                Traffic  arrival is not expected to exceed this
                rate	at any time, apart  from  the  effects	of
                jitter in the network.  If not specified in the
                TSpec, this returns zero or noSuchValue.
                ''',
                'rsvpsendertspecpeakrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderTSpecRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	Average	Bit  Rate  of  the  sender's  data
                stream.    Within  a	 transmission  burst,  the
                arrival   rate    may    be	  as	fast	as
                rsvpSenderTSpecPeakRate  (if	 supported  by the
                service model); however, averaged across two	or
                more	 burst	intervals,  the	 rate  should  not
                exceed rsvpSenderTSpecRate.
                
                Note	that this is a prediction, often based	on
                the	general	 capability  of	a type of codec	or
                particular encoding;	the measured average  rate
                may be significantly	lower.
                ''',
                'rsvpsendertspecrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderTTL', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The	TTL value in the RSVP header that was last
                received.
                ''',
                'rsvpsenderttl',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderType', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	type of	session	(IP4, IP6, IP6	with  flow
                information,	etc).
                ''',
                'rsvpsendertype',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpSenderEntry',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpsendertable' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpsendertable',
            False, 
            [
            _MetaInfoClassMember('rsvpSenderEntry', REFERENCE_LIST, 'Rsvpsenderentry' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpsendertable.Rsvpsenderentry', 
                [], [], 
                '''                Information	describing the	state  information
                displayed by	a single sender's PATH message.
                ''',
                'rsvpsenderentry',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpSenderTable',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry',
            False, 
            [
            _MetaInfoClassMember('rsvpSessionNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                ''',
                'rsvpsessionnumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpSenderNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                ''',
                'rsvpsendernumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpSenderOutInterfaceStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' for all active PATH messages.
                ''',
                'rsvpsenderoutinterfacestatus',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpSenderOutInterfaceEntry',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpsenderoutinterfacetable' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpsenderoutinterfacetable',
            False, 
            [
            _MetaInfoClassMember('rsvpSenderOutInterfaceEntry', REFERENCE_LIST, 'Rsvpsenderoutinterfaceentry' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry', 
                [], [], 
                '''                List of outgoing interfaces	that a	particular
                PATH	message	has.
                ''',
                'rsvpsenderoutinterfaceentry',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpSenderOutInterfaceTable',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpresvtable.Rsvpresventry' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpresvtable.Rsvpresventry',
            False, 
            [
            _MetaInfoClassMember('rsvpSessionNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                ''',
                'rsvpsessionnumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpResvNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	number of this reservation request.   This
                is  for  SNMP Indexing purposes only	and has	no
                relation to any protocol value.
                ''',
                'rsvpresvnumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpResvDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	destination address used by all	senders	in
                this	 session.   This object	may not	be changed
                when	the  value  of	the  RowStatus	object	is
                'active'.
                ''',
                'rsvpresvdestaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvDestAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The	length of the destination address in bits.
                This	 is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvdestaddrlength',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvDestPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The	 UDP  or  TCP  port  number  used   as	 a
                destination	 port  for  all	 senders  in  this
                session.  If	the IP protocol	in use,	 specified
                by  rsvpResvProtocol,  is  50 (ESP) or 51 (AH),
                this	 represents  a	virtual	 destination  port
                number.   A value of	zero indicates that the	IP
                protocol in use  does  not  have  ports.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvdestport',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvExplicit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, individual	senders	are  listed  using
                Filter  Specifications.   If	FALSE, all senders
                are implicitly selected.  The Scope Object will
                contain  a list of senders that need	to receive
                this	reservation request  for  the  purpose	of
                routing the RESV message.
                ''',
                'rsvpresvexplicit',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFlowId', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                The	flow ID	that this receiver  is	using,	if
                this	 is  an	IPv6 session.
                ''',
                'rsvpresvflowid',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	address	used by	the next RSVP  hop  (which
                may be the ultimate receiver).
                ''',
                'rsvpresvhopaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvHopLih', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The	Logical	Interface Handle received from the
                previous  RSVP  hop	(which may be the ultimate
                receiver).
                ''',
                'rsvpresvhoplih',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvInterface', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The	ifIndex	value of the  interface	 on  which
                this	RESV message was most recently received.
                ''',
                'rsvpresvinterface',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	 interval  between  refresh  messages	as
                advertised by the Next Hop.
                ''',
                'rsvpresvinterval',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	 time  of  the	 last	change	 in   this
                reservation	request;  This is either the first
                time	it was received	or the time  of	 the  most
                recent change in parameters.
                ''',
                'rsvpresvlastchange',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvPolicy', ATTRIBUTE, 'str' , None, None, 
                [(0, 65536)], [], 
                '''                The	contents of the	policy	object,	 displayed
                as an uninterpreted string of octets, including
                the object header.  In the absence of  such	an
                object, this	should be of zero length.
                ''',
                'rsvpresvpolicy',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The	UDP or TCP port	number used  as	 a  source
                port	 for  this sender in this session.  If the
                IP	 protocol    in	   use,	   specified	by
                rsvpResvProtocol  is	 50 (ESP) or 51	(AH), this
                represents a	generalized port identifier (GPI).
                A  value of zero indicates that the IP protocol
                in use does not have	ports.	 This  object  may
                not	be changed when	the value of the RowStatus
                object is 'active'.
                ''',
                'rsvpresvport',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvProtocol', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	IP Protocol used by  this  session.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvprotocol',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvRSpecRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If the requested  service  is  Guaranteed,	as
                specified   by  rsvpResvService,  this  is  the
                clearing  rate   that   is	being	requested.
                Otherwise,  it is zero, or the agent	may return
                noSuchValue.
                ''',
                'rsvpresvrspecrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvRSpecSlack', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If the requested  service  is  Guaranteed,	as
                specified by	rsvpResvService, this is the delay
                slack.  Otherwise, it is zero, or the agent may
                return noSuchValue.
                ''',
                'rsvpresvrspecslack',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvRSVPHop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, the node believes that  the  previous
                IP  hop  is	an  RSVP  hop.	If FALSE, the node
                believes that the previous IP hop may not be	an
                RSVP	hop.
                ''',
                'rsvpresvrsvphop',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvScope', ATTRIBUTE, 'str' , None, None, 
                [(0, 65536)], [], 
                '''                The	contents of the	scope object, displayed	as
                an  uninterpreted  string  of octets, including
                the object header.  In the absence of  such	an
                object, this	should be of zero length.
                
                If the length  is  non-zero,	 this  contains	 a
                series of IP4 or IP6	addresses.
                ''',
                'rsvpresvscope',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvSenderAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	source address of the sender  selected	by
                this	 reservation.	The  value  of	all zeroes
                indicates 'all senders'.  This object  may  not
                be  changed	when  the  value  of the RowStatus
                object is 'active'.
                ''',
                'rsvpresvsenderaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvSenderAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The	length of the sender's	address	 in  bits.
                This	 is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvsenderaddrlength',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvService', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The	QoS Service  classification  requested	by
                the receiver.
                ''',
                'rsvpresvservice',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvShared', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, a reservation shared among	senders	is
                requested.  If FALSE, a reservation specific	to
                this	sender is requested.
                ''',
                'rsvpresvshared',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' for all active RESV  messages.   This
                object  may	be  used  to  install  static RESV
                information or delete RESV information.
                ''',
                'rsvpresvstatus',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvTSpecBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	size of	the largest  burst  expected  from
                the sender at a time.
                
                If this is less than	 the  sender's	advertised
                burst  size,	the receiver is	asking the network
                to provide flow pacing  beyond  what	 would	be
                provided   under   normal  circumstances.  Such
                pacing is at	the network's option.
                ''',
                'rsvpresvtspecburst',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvTSpecMaxTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	maximum	message	size for  this	flow.  The
                admission  algorithm	 will  reject TSpecs whose
                Maximum Transmission	Unit, plus  the	 interface
                headers, exceed the interface MTU.
                ''',
                'rsvpresvtspecmaxtu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvTSpecMinTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	minimum	message	size for  this	flow.  The
                policing  algorithm will treat smaller messages
                as though they are this size.
                ''',
                'rsvpresvtspecmintu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvTSpecPeakRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	Peak Bit Rate of the sender's data stream.
                Traffic  arrival is not expected to exceed this
                rate	at any time, apart  from  the  effects	of
                jitter in the network.  If not specified in the
                TSpec, this returns zero or noSuchValue.
                ''',
                'rsvpresvtspecpeakrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvTSpecRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	Average	Bit  Rate  of  the  sender's  data
                stream.    Within  a	 transmission  burst,  the
                arrival   rate    may    be	  as	fast	as
                rsvpResvTSpecPeakRate   (if	supported  by  the
                service model); however, averaged across two	or
                more	 burst	intervals,  the	 rate  should  not
                exceed rsvpResvTSpecRate.
                
                Note	that this is a prediction, often based	on
                the	general	 capability  of	a type of codec	or
                particular encoding;	the measured average  rate
                may be significantly	lower.
                ''',
                'rsvpresvtspecrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvTTL', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The	TTL value in the RSVP header that was last
                received.
                ''',
                'rsvpresvttl',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvType', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	type of	session	(IP4, IP6, IP6	with  flow
                information,	etc).
                ''',
                'rsvpresvtype',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpResvEntry',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpresvtable' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpresvtable',
            False, 
            [
            _MetaInfoClassMember('rsvpResvEntry', REFERENCE_LIST, 'Rsvpresventry' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpresvtable.Rsvpresventry', 
                [], [], 
                '''                Information	describing the	state  information
                displayed  by  a single receiver's RESV message
                concerning a	single sender.
                ''',
                'rsvpresventry',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpResvTable',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry',
            False, 
            [
            _MetaInfoClassMember('rsvpSessionNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                ''',
                'rsvpsessionnumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpResvFwdNumber', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	number of this reservation request.   This
                is  for  SNMP Indexing purposes only	and has	no
                relation to any protocol value.
                ''',
                'rsvpresvfwdnumber',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpResvFwdDestAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	destination address used by all	senders	in
                this	 session.   This object	may not	be changed
                when	the  value  of	the  RowStatus	object	is
                'active'.
                ''',
                'rsvpresvfwddestaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdDestAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The	length of the destination address in bits.
                This	 is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvfwddestaddrlength',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdDestPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The	 UDP  or  TCP  port  number  used   as	 a
                destination	 port  for  all	 senders  in  this
                session.  If	the IP protocol	in use,	 specified
                by rsvpResvFwdProtocol, is 50 (ESP) or 51 (AH),
                this	 represents  a	virtual	 destination  port
                number.   A value of	zero indicates that the	IP
                protocol in use  does  not  have  ports.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvfwddestport',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdExplicit', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, individual	senders	are  listed  using
                Filter  Specifications.   If	FALSE, all senders
                are implicitly selected.  The Scope Object will
                contain  a list of senders that need	to receive
                this	reservation request  for  the  purpose	of
                routing the RESV message.
                ''',
                'rsvpresvfwdexplicit',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdFlowId', ATTRIBUTE, 'int' , None, None, 
                [('0', '16777215')], [], 
                '''                The	flow ID	that this receiver  is	using,	if
                this	 is  an	IPv6 session.
                ''',
                'rsvpresvfwdflowid',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdHopAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	address	of the (previous) RSVP	that  will
                receive this	message.
                ''',
                'rsvpresvfwdhopaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdHopLih', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                The	 Logical  Interface  Handle  sent  to  the
                (previous)	RSVP   that   will   receive  this
                message.
                ''',
                'rsvpresvfwdhoplih',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdInterface', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                The	ifIndex	value of the  interface	 on  which
                this	RESV message was most recently sent.
                ''',
                'rsvpresvfwdinterface',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	  interval   between   refresh	  messages
                advertised to the Previous Hop.
                ''',
                'rsvpresvfwdinterval',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdLastChange', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	time of	the last change	in  this  request;
                This	 is  either  the first time it was sent	or
                the	time  of  the  most   recent   change	in
                parameters.
                ''',
                'rsvpresvfwdlastchange',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdPolicy', ATTRIBUTE, 'str' , None, None, 
                [(0, 65536)], [], 
                '''                The	contents of the	policy	object,	 displayed
                as an uninterpreted string of octets, including
                the object header.  In the absence of  such	an
                object, this	should be of zero length.
                ''',
                'rsvpresvfwdpolicy',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdPort', ATTRIBUTE, 'str' , None, None, 
                [(2, 4)], [], 
                '''                The	UDP or TCP port	number used  as	 a  source
                port	 for  this sender in this session.  If the
                IP	 protocol    in	   use,	   specified	by
                rsvpResvFwdProtocol	is  50	(ESP)  or 51 (AH),
                this	represents a generalized  port	identifier
                (GPI).   A  value of	zero indicates that the	IP
                protocol in use  does  not  have  ports.   This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvfwdport',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdProtocol', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	IP Protocol used by a session. for  secure
                sessions,  this  indicates  IP  Security.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvfwdprotocol',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdRSpecRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                If the requested  service  is  Guaranteed,	as
                specified   by  rsvpResvService,  this  is  the
                clearing  rate   that   is	being	requested.
                Otherwise,  it is zero, or the agent	may return
                noSuchValue.
                ''',
                'rsvpresvfwdrspecrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdRSpecSlack', ATTRIBUTE, 'int' , None, None, 
                [('-2147483648', '2147483647')], [], 
                '''                If the requested  service  is  Guaranteed,	as
                specified by	rsvpResvService, this is the delay
                slack.  Otherwise, it is zero, or the agent may
                return noSuchValue.
                ''',
                'rsvpresvfwdrspecslack',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdRSVPHop', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, the node believes that  the  next	IP
                hop	is  an	RSVP  hop.   If	 FALSE,	 the  node
                believes that the next IP hop  may  not  be	an
                RSVP	hop.
                ''',
                'rsvpresvfwdrsvphop',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdScope', ATTRIBUTE, 'str' , None, None, 
                [(0, 65536)], [], 
                '''                The	contents of the	scope object, displayed	as
                an  uninterpreted  string  of octets, including
                the object header.  In the absence of  such	an
                object, this	should be of zero length.
                ''',
                'rsvpresvfwdscope',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdSenderAddr', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	source address of the sender  selected	by
                this	 reservation.	The  value  of	all zeroes
                indicates 'all senders'.  This object  may  not
                be  changed	when  the  value  of the RowStatus
                object is 'active'.
                ''',
                'rsvpresvfwdsenderaddr',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdSenderAddrLength', ATTRIBUTE, 'int' , None, None, 
                [('0', '128')], [], 
                '''                The	length of the sender's	address	 in  bits.
                This	 is  the CIDR Prefix Length, which for IP4
                hosts and multicast addresses is 32 bits.  This
                object may not be changed when the value of the
                RowStatus object is 'active'.
                ''',
                'rsvpresvfwdsenderaddrlength',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdService', REFERENCE_ENUM_CLASS, 'QosserviceEnum' , 'ydk.models.cisco_ios_xe.INTEGRATED_SERVICES_MIB', 'QosserviceEnum', 
                [], [], 
                '''                The	QoS Service classification requested.
                ''',
                'rsvpresvfwdservice',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdShared', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, a reservation shared among	senders	is
                requested.  If FALSE, a reservation specific	to
                this	sender is requested.
                ''',
                'rsvpresvfwdshared',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' for all active RESV  messages.   This
                object may be used to delete	RESV information.
                ''',
                'rsvpresvfwdstatus',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdTSpecBurst', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	size of	the largest  burst  expected  from
                the sender at a time.
                
                If this is less than	 the  sender's	advertised
                burst  size,	the receiver is	asking the network
                to provide flow pacing  beyond  what	 would	be
                provided   under   normal  circumstances.  Such
                pacing is at	the network's option.
                ''',
                'rsvpresvfwdtspecburst',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdTSpecMaxTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	maximum	message	size for  this	flow.  The
                admission  algorithm	 will  reject TSpecs whose
                Maximum Transmission	Unit, plus  the	 interface
                headers, exceed the interface MTU.
                ''',
                'rsvpresvfwdtspecmaxtu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdTSpecMinTU', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	minimum	message	size for  this	flow.  The
                policing  algorithm will treat smaller messages
                as though they are this size.
                ''',
                'rsvpresvfwdtspecmintu',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdTSpecPeakRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	Peak Bit Rate of the sender's data  stream
                Traffic  arrival is not expected to exceed this
                rate	at any time, apart  from  the  effects	of
                jitter in the network.  If not specified in the
                TSpec, this returns zero or noSuchValue.
                ''',
                'rsvpresvfwdtspecpeakrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdTSpecRate', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	Average	Bit  Rate  of  the  sender's  data
                stream.    Within  a	 transmission  burst,  the
                arrival   rate    may    be	  as	fast	as
                rsvpResvFwdTSpecPeakRate  (if  supported by the
                service model); however, averaged across two	or
                more	 burst	intervals,  the	 rate  should  not
                exceed rsvpResvFwdTSpecRate.
                
                Note	that this is a prediction, often based	on
                the	general	 capability  of	a type of codec	or
                particular encoding;	the measured average  rate
                may be significantly	lower.
                ''',
                'rsvpresvfwdtspecrate',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdTTL', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The	TTL value in the RSVP header that was last
                received.
                ''',
                'rsvpresvfwdttl',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdType', ATTRIBUTE, 'int' , None, None, 
                [('1', '255')], [], 
                '''                The	type of	session	(IP4, IP6, IP6	with  flow
                information,	etc).
                ''',
                'rsvpresvfwdtype',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpResvFwdEntry',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpresvfwdtable' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpresvfwdtable',
            False, 
            [
            _MetaInfoClassMember('rsvpResvFwdEntry', REFERENCE_LIST, 'Rsvpresvfwdentry' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry', 
                [], [], 
                '''                Information	describing the	state  information
                displayed   upstream	  in   an   RESV   message
                concerning a	single sender.
                ''',
                'rsvpresvfwdentry',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpResvFwdTable',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpiftable.Rsvpifentry' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpiftable.Rsvpifentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpIfEnabled', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, RSVP is enabled  on  this	Interface.
                If	FALSE,	 RSVP	is  not	 enabled  on  this
                interface.
                ''',
                'rsvpifenabled',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfIpNbrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	number of neighbors perceived to be  using
                only	the RSVP IP Encapsulation.
                ''',
                'rsvpifipnbrs',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfNbrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	number of neighbors  currently	perceived;
                this	 will  exceed rsvpIfIpNbrs + rsvpIfUdpNbrs
                by  the  number   of	  neighbors   using   both
                encapsulations.
                ''',
                'rsvpifnbrs',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfRefreshBlockadeMultiple', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                The	value of the RSVP value	'Kb', Which is the
                minimum   number   of  refresh  intervals  that
                blockade state will last once entered.
                ''',
                'rsvpifrefreshblockademultiple',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfRefreshInterval', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	value of the RSVP value	'R', which is  the
                minimum period between refresh transmissions	of
                a given PATH	or RESV	message	on an interface.
                ''',
                'rsvpifrefreshinterval',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfRefreshMultiple', ATTRIBUTE, 'int' , None, None, 
                [('1', '65536')], [], 
                '''                The	value of the RSVP value	'K', which is  the
                number  of  refresh intervals which must elapse
                (minimum) before a PATH or RESV  message  which
                is not being	refreshed will be aged out.
                ''',
                'rsvpifrefreshmultiple',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfRouteDelay', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The	approximate period from	the time  a  route
                is  changed	to  the	 time  a resulting message
                appears on the interface.
                ''',
                'rsvpifroutedelay',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' on	interfaces that	are configured for
                RSVP.
                ''',
                'rsvpifstatus',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfTTL', ATTRIBUTE, 'int' , None, None, 
                [('0', '255')], [], 
                '''                The	value of SEND_TTL used on  this	 interface
                for	messages  this node originates.	 If set	to
                zero, the node determines  the  TTL	via  other
                means.
                ''',
                'rsvpifttl',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfUdpNbrs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The	number of neighbors perceived to be  using
                only	the RSVP UDP Encapsulation.
                ''',
                'rsvpifudpnbrs',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfUdpRequired', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                If TRUE, manual configuration forces  the  use
                of  UDP  encapsulation  on  the  interface.	If
                FALSE,  UDP	encapsulation  is  only	 used	if
                rsvpIfUdpNbrs is not	zero.
                ''',
                'rsvpifudprequired',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpIfEntry',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpiftable' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpiftable',
            False, 
            [
            _MetaInfoClassMember('rsvpIfEntry', REFERENCE_LIST, 'Rsvpifentry' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpiftable.Rsvpifentry', 
                [], [], 
                '''                The	RSVP-specific attributes of  the  a  given
                interface.
                ''',
                'rsvpifentry',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpIfTable',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpnbrtable.Rsvpnbrentry' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpnbrtable.Rsvpnbrentry',
            False, 
            [
            _MetaInfoClassMember('ifIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '2147483647')], [], 
                '''                ''',
                'ifindex',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpNbrAddress', ATTRIBUTE, 'str' , None, None, 
                [(4, 16)], [], 
                '''                The	IP4 or IP6 Address used	by this	 neighbor.
                This	 object	 may not be changed when the value
                of the RowStatus object is 'active'.
                ''',
                'rsvpnbraddress',
                'RSVP-MIB', True),
            _MetaInfoClassMember('rsvpNbrProtocol', REFERENCE_ENUM_CLASS, 'RsvpencapsulationEnum' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpencapsulationEnum', 
                [], [], 
                '''                The	  encapsulation	  being	  used	 by   this
                neighbor.
                ''',
                'rsvpnbrprotocol',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpNbrStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                'active' for all neighbors.	 This  object  may
                be	used   to  configure  neighbors.   In  the
                presence   of   configured	 neighbors,    the
                implementation  may	(but  is  not required to)
                limit the  set  of  valid  neighbors	 to  those
                configured.
                ''',
                'rsvpnbrstatus',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpNbrEntry',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib.Rsvpnbrtable' : {
        'meta_info' : _MetaInfoClass('RsvpMib.Rsvpnbrtable',
            False, 
            [
            _MetaInfoClassMember('rsvpNbrEntry', REFERENCE_LIST, 'Rsvpnbrentry' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpnbrtable.Rsvpnbrentry', 
                [], [], 
                '''                Information	  describing   a    single    RSVP
                Neighbor.
                ''',
                'rsvpnbrentry',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'rsvpNbrTable',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
    'RsvpMib' : {
        'meta_info' : _MetaInfoClass('RsvpMib',
            False, 
            [
            _MetaInfoClassMember('rsvpGenObjects', REFERENCE_CLASS, 'Rsvpgenobjects' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpgenobjects', 
                [], [], 
                '''                ''',
                'rsvpgenobjects',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpIfTable', REFERENCE_CLASS, 'Rsvpiftable' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpiftable', 
                [], [], 
                '''                The	RSVP-specific attributes of  the  system's
                interfaces.
                ''',
                'rsvpiftable',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpNbrTable', REFERENCE_CLASS, 'Rsvpnbrtable' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpnbrtable', 
                [], [], 
                '''                Information	describing  the	 Neighbors  of	an
                RSVP	system.
                ''',
                'rsvpnbrtable',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvFwdTable', REFERENCE_CLASS, 'Rsvpresvfwdtable' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpresvfwdtable', 
                [], [], 
                '''                Information	describing the	state  information
                displayed upstream in RESV messages.
                ''',
                'rsvpresvfwdtable',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpResvTable', REFERENCE_CLASS, 'Rsvpresvtable' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpresvtable', 
                [], [], 
                '''                Information	describing the	state  information
                displayed by	receivers in RESV messages.
                ''',
                'rsvpresvtable',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderOutInterfaceTable', REFERENCE_CLASS, 'Rsvpsenderoutinterfacetable' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpsenderoutinterfacetable', 
                [], [], 
                '''                List of outgoing interfaces	that PATH messages
                use.	 The  ifIndex  is the ifIndex value of the
                egress interface.
                ''',
                'rsvpsenderoutinterfacetable',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSenderTable', REFERENCE_CLASS, 'Rsvpsendertable' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpsendertable', 
                [], [], 
                '''                Information	describing the	state  information
                displayed by	senders	in PATH	messages.
                ''',
                'rsvpsendertable',
                'RSVP-MIB', False),
            _MetaInfoClassMember('rsvpSessionTable', REFERENCE_CLASS, 'Rsvpsessiontable' , 'ydk.models.cisco_ios_xe.RSVP_MIB', 'RsvpMib.Rsvpsessiontable', 
                [], [], 
                '''                A table  of	 all  sessions	seen  by  a  given
                system.
                ''',
                'rsvpsessiontable',
                'RSVP-MIB', False),
            ],
            'RSVP-MIB',
            'RSVP-MIB',
            _yang_ns._namespaces['RSVP-MIB'],
        'ydk.models.cisco_ios_xe.RSVP_MIB'
        ),
    },
}
_meta_table['RsvpMib.Rsvpsessiontable.Rsvpsessionentry']['meta_info'].parent =_meta_table['RsvpMib.Rsvpsessiontable']['meta_info']
_meta_table['RsvpMib.Rsvpsendertable.Rsvpsenderentry']['meta_info'].parent =_meta_table['RsvpMib.Rsvpsendertable']['meta_info']
_meta_table['RsvpMib.Rsvpsenderoutinterfacetable.Rsvpsenderoutinterfaceentry']['meta_info'].parent =_meta_table['RsvpMib.Rsvpsenderoutinterfacetable']['meta_info']
_meta_table['RsvpMib.Rsvpresvtable.Rsvpresventry']['meta_info'].parent =_meta_table['RsvpMib.Rsvpresvtable']['meta_info']
_meta_table['RsvpMib.Rsvpresvfwdtable.Rsvpresvfwdentry']['meta_info'].parent =_meta_table['RsvpMib.Rsvpresvfwdtable']['meta_info']
_meta_table['RsvpMib.Rsvpiftable.Rsvpifentry']['meta_info'].parent =_meta_table['RsvpMib.Rsvpiftable']['meta_info']
_meta_table['RsvpMib.Rsvpnbrtable.Rsvpnbrentry']['meta_info'].parent =_meta_table['RsvpMib.Rsvpnbrtable']['meta_info']
_meta_table['RsvpMib.Rsvpgenobjects']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
_meta_table['RsvpMib.Rsvpsessiontable']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
_meta_table['RsvpMib.Rsvpsendertable']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
_meta_table['RsvpMib.Rsvpsenderoutinterfacetable']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
_meta_table['RsvpMib.Rsvpresvtable']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
_meta_table['RsvpMib.Rsvpresvfwdtable']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
_meta_table['RsvpMib.Rsvpiftable']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
_meta_table['RsvpMib.Rsvpnbrtable']['meta_info'].parent =_meta_table['RsvpMib']['meta_info']
