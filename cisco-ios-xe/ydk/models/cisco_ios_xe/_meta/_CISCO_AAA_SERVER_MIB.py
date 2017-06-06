


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'CiscoaaaprotocolEnum' : _MetaInfoEnum('CiscoaaaprotocolEnum', 'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB',
        {
            'tacacsplus':'tacacsplus',
            'radius':'radius',
            'ldap':'ldap',
            'kerberos':'kerberos',
            'ntlm':'ntlm',
            'sdi':'sdi',
            'other':'other',
        }, 'CISCO-AAA-SERVER-MIB', _yang_ns._namespaces['CISCO-AAA-SERVER-MIB']),
    'CiscoAaaServerMib.Casconfig' : {
        'meta_info' : _MetaInfoClass('CiscoAaaServerMib.Casconfig',
            False, 
            [
            _MetaInfoClassMember('casServerStateChangeEnable', ATTRIBUTE, 'bool' , None, None, 
                [], [], 
                '''                This variable controls the	generation of
                casServerStateChange notification.
                
                When this variable	is true(1), generation of
                casServerStateChange notifications	is enabled.
                When this variable	is false(2), generation	of
                casServerStateChange notifications	is disabled.
                
                The default value is false(2).
                ''',
                'casserverstatechangeenable',
                'CISCO-AAA-SERVER-MIB', False),
            ],
            'CISCO-AAA-SERVER-MIB',
            'casConfig',
            _yang_ns._namespaces['CISCO-AAA-SERVER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB'
        ),
    },
    'CiscoAaaServerMib.Casconfigtable.Casconfigentry.CasstateEnum' : _MetaInfoEnum('CasstateEnum', 'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB',
        {
            'up':'up',
            'dead':'dead',
        }, 'CISCO-AAA-SERVER-MIB', _yang_ns._namespaces['CISCO-AAA-SERVER-MIB']),
    'CiscoAaaServerMib.Casconfigtable.Casconfigentry' : {
        'meta_info' : _MetaInfoClass('CiscoAaaServerMib.Casconfigtable.Casconfigentry',
            False, 
            [
            _MetaInfoClassMember('casProtocol', REFERENCE_ENUM_CLASS, 'CiscoaaaprotocolEnum' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB', 'CiscoaaaprotocolEnum', 
                [], [], 
                '''                The variable denotes the protocol used by the
                managed device with the AAA server corresponding to
                 this entry in the table.
                ''',
                'casprotocol',
                'CISCO-AAA-SERVER-MIB', True),
            _MetaInfoClassMember('casIndex', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A management station wishing to initiate a	new AAA	server
                configuration should use a	random value for this object
                when creating an instance of casConfigEntry.
                
                The RowStatus semantics of	the casConfigRowStatus object
                will prevent access conflicts.
                
                If	the randomly chosen casIndex value for row creation
                is	already	in use by an existing entry, snmp set to the
                casIndex value will fail.
                ''',
                'casindex',
                'CISCO-AAA-SERVER-MIB', True),
            _MetaInfoClassMember('casAcctIncorrectResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of accounting responses	which could not
                be	processed since	system re-initialization.
                
                Reasons include inability to decrypt the response,
                invalid fields, or	the response is	not valid based	on
                the request.
                ''',
                'casacctincorrectresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                UDP/TCP port used for accounting service in the configuration
                
                For TACACS+, the value of casAcctPort is ignored.
                casAuthenPort will	be used	instead.
                
                Default value is the IOS default for radius: 1646.
                ''',
                'casacctport',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of accounting requests sent to
                this server since system re-initialization.
                
                Retransmissions due to request timeouts are
                counted as	distinct requests.
                ''',
                'casacctrequests',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctRequestTimeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of accounting requests which have
                timed out since system re-initialization.
                
                A timeout results in a retransmission of the request
                If	the maximum number of attempts has been	reached,
                no	further	retransmissions	will be	attempted.
                ''',
                'casacctrequesttimeouts',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctResponseTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Average response time for accounting requests sent
                to	this server,, since system re-initialization
                excluding timeouts.
                ''',
                'casacctresponsetime',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctServerErrorResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of server ERROR	accounting responses received
                from this server since system re-initialization.
                
                These are responses indicating that the server itself
                has identified an error with its accounting
                operation.
                ''',
                'casacctservererrorresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctTransactionFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of accounting transactions with	this
                server which failed since system re-initialization.
                
                A transaction may include multiple	request
                retransmissions if	timeouts occur.
                
                A transaction failure occurs if maximum resends have
                been met or the server aborts the transaction.
                ''',
                'casaccttransactionfailures',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctTransactionSuccesses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of accounting transactions with	this
                server which succeeded since system re-initialization.
                
                A transaction may include multiple	request
                retransmissions if	timeouts occur.
                
                A transaction is successful if the	server responds
                with either an accounting pass or fail.
                ''',
                'casaccttransactionsuccesses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAcctUnexpectedResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of unexpected accounting responses received
                from this server since system re-initialization.
                
                An	example	is a delayed response to a request which had
                already timed out.
                ''',
                'casacctunexpectedresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAddress', ATTRIBUTE, 'str' , None, None, 
                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                '''                The IP address of the server.
                ''',
                'casaddress',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenIncorrectResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authentication responses which could	not
                be	processed since	it is made active.
                
                Reasons include inability to decrypt the response,
                invalid fields, or	the response is	not valid based	on
                the request.
                ''',
                'casauthenincorrectresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenPort', ATTRIBUTE, 'int' , None, None, 
                [('0', '65535')], [], 
                '''                UDP/TCP port used for authentication in the configuration
                
                For TACACS+, this object should be	explictly set.
                
                Default value is the IOS default for radius: 1645.
                ''',
                'casauthenport',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authentication requests sent	to
                this server since it is made active.
                
                Retransmissions due to request timeouts are
                counted as	distinct requests.
                ''',
                'casauthenrequests',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenRequestTimeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authentication requests which have
                timed out since it	is made	active.
                
                A timeout results in a retransmission of the request
                If	the maximum number of attempts has been	reached,
                no	further	retransmissions	will be	attempted.
                ''',
                'casauthenrequesttimeouts',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenResponseTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Average response time for authentication requests sent
                to	this server, excluding timeouts, since system
                re-initialization.
                ''',
                'casauthenresponsetime',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenServerErrorResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of server ERROR	authentication responses
                received from this	server since it	is made	active.
                
                These are responses indicating that the server itself
                has identified an error with its authentication
                operation.
                ''',
                'casauthenservererrorresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenTransactionFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authentication transactions with this
                server which failed since it is made active.
                
                A transaction may include multiple	request
                retransmissions if	timeouts occur.
                
                A transaction failure occurs if maximum resends have
                been met or the server aborts the transaction.
                ''',
                'casauthentransactionfailures',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenTransactionSuccesses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authentication transactions with this
                server which succeeded since it is	made active.
                
                A transaction may include multiple	request
                retransmissions if	timeouts occur.
                
                A transaction is successful if the	server responds
                with either an authentication pass	or fail.
                ''',
                'casauthentransactionsuccesses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthenUnexpectedResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of unexpected authentication responses received
                from this server since it is made active.
                
                An	example	is a delayed response to a request which had
                already timed out.
                ''',
                'casauthenunexpectedresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorIncorrectResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authorization responses which could not
                be	processed since	it is made active.
                
                Reasons include inability to decrypt the response,
                invalid fields, or	the response is	not valid based	on
                the request.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthorincorrectresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorRequests', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authorization requests sent to
                this server since it is made active.
                
                Retransmissions due to request timeouts are
                counted as	distinct requests.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthorrequests',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorRequestTimeouts', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authorization requests which	have
                timed out since it	is made	active.
                
                A timeout results in a retransmission of the request
                If	the maximum number of attempts has been	reached,
                no	further	retransmissions	will be	attempted.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthorrequesttimeouts',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorResponseTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                Average response time for authorization requests sent
                to	this server, excluding timeouts, since system
                re-initialization.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthorresponsetime',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorServerErrorResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of server ERROR	authorization responses
                received from this	server since it	is made	active.
                
                These are responses indicating that the server itself
                has identified an error with its authorization
                operation.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthorservererrorresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorTransactionFailures', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authorization transactions with this
                server which failed since it is made active.
                
                A transaction may include multiple	request
                retransmissions if	timeouts occur.
                
                A transaction failure occurs if maximum resends have
                been met or the server aborts the transaction.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthortransactionfailures',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorTransactionSuccesses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of authorization transactions with this
                server which succeeded since it is	made active.
                
                A transaction may include multiple	request
                retransmissions if	timeouts occur.
                
                A transaction is successful if the	server responds
                with either an authorization pass or fail.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthortransactionsuccesses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casAuthorUnexpectedResponses', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of unexpected authorization responses received
                from this server since it is made active.
                
                An	example	is a delayed response to a request which
                had already timed out.
                
                This object is not	instantiated for protocols which do
                not support a distinct authorization function.
                ''',
                'casauthorunexpectedresponses',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casConfigRowStatus', REFERENCE_ENUM_CLASS, 'RowstatusEnum' , 'ydk.models.cisco_ios_xe.SNMPv2_TC', 'RowstatusEnum', 
                [], [], 
                '''                The status of this table entry.  Once the entry status	is
                set to	active,	the associated entry cannot be modified
                except	destroyed by setting this object to destroy(6).
                ''',
                'casconfigrowstatus',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casCurrentStateDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object provides the elapsed time the server has
                been in its current state as shown	in casState.
                ''',
                'cascurrentstateduration',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casDeadCount', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The number	of times this server's casState	has
                transitioned to 'dead(2)' since system re-initialization.
                ''',
                'casdeadcount',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casKey', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The server key	to be used with	this server.
                
                Retrieving the	value of this object via SNMP will
                return	an empty string	for security reasons.
                ''',
                'caskey',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casPreviousStateDuration', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                This object provides the elapsed time the server was
                been in its previous state	prior to the most recent
                transistion of casState.
                
                This value	is zero	if the server has not changed state.
                ''',
                'caspreviousstateduration',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casPriority', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                A number that indicates the priority of the server	in
                this entry.  Lower	numbers	indicate higher	priority.
                ''',
                'caspriority',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casState', REFERENCE_ENUM_CLASS, 'CasstateEnum' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB', 'CiscoAaaServerMib.Casconfigtable.Casconfigentry.CasstateEnum', 
                [], [], 
                '''                Current state of this server.
                
                up(1)	 - Server responding to	requests
                
                dead(2) - Server failed to respond
                
                A server is marked	dead if	it does	not respond after
                maximum retransmissions.
                
                A server is marked	up again either	after a	waiting
                period or if some response	is received from it.
                
                The initial value of casState is 'up(1)' at system
                re-initialization.	This will only transistion to 'dead(2)'
                if	an attempt to communicate fails.
                ''',
                'casstate',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casTotalDeadTime', ATTRIBUTE, 'int' , None, None, 
                [('0', '2147483647')], [], 
                '''                The total elapsed time this server's casState has
                had the value 'dead(2)' since system re-initialization.
                ''',
                'castotaldeadtime',
                'CISCO-AAA-SERVER-MIB', False),
            ],
            'CISCO-AAA-SERVER-MIB',
            'casConfigEntry',
            _yang_ns._namespaces['CISCO-AAA-SERVER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB'
        ),
    },
    'CiscoAaaServerMib.Casconfigtable' : {
        'meta_info' : _MetaInfoClass('CiscoAaaServerMib.Casconfigtable',
            False, 
            [
            _MetaInfoClassMember('casConfigEntry', REFERENCE_LIST, 'Casconfigentry' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB', 'CiscoAaaServerMib.Casconfigtable.Casconfigentry', 
                [], [], 
                '''                An	AAA server configuration identified by its protocol
                and its index.
                
                An	entry is created/removed when a	server is defined
                or	undefined with IOS configuration commands via
                CLI or by issuing appropriate sets	to this	table
                using snmp.
                
                A management station wishing to create an entry should
                first generate a random number to be used as the index
                to	this sparse table.  The	station	should then create the
                associated	instance of the	row status and row index objects.
                It	must also, either in the same or in successive PDUs,
                create an instance	of casAddress where casAddress is the
                IP	address	of the server to be added.
                
                It	should also modify the default values for casAuthenPort,
                casAcctPort if the	defaults are not appropriate.
                
                If	casKey is a zero-length	string or is not explicitly set,
                then the global key will be used.	Otherwise, this	value
                is	used as	the key	for this server	instance.
                
                Once the appropriate instance of all the configuration
                objects have been created,	either by an explicit SNMP set
                request or	by default, the	row status should be set to
                active(1) to initiate the request.
                
                After the AAA server is made active, the entry can	not be
                modified -	the only allowed operation after this is to
                destroy the entry by setting casConfigRowStatus to	destroy(6).
                
                casPriority is automatically assigned once	the entry is
                made active and reflects the relative priority of the
                defined server with respect to already configured servers.
                Newly-created servers will	be assigned the	lowest priority.
                To	reassign server	priorities to existing server entries,
                it	may be necessary to destroy and	recreate entries in order
                of	priority.
                
                Entries in	this table with	casConfigRowStatus equal to
                active(1) remain in the table until destroyed.
                
                Entries in	this table with	casConfigRowStatus equal to
                values other than active(1) will be destroyed after timeout
                (5	minutes).
                
                If	a server address being created via SNMP	exists already
                in	another	active casConfigEntry, then a newly created row
                can not be	made active until the original row with	the
                with the same server address value	is destroyed.
                
                Upon reload, casIndex values may be changed, but the
                priorities	that were saved	before reload will be retained,
                with lowest priority number corresponding to the higher
                priority servers.
                ''',
                'casconfigentry',
                'CISCO-AAA-SERVER-MIB', False),
            ],
            'CISCO-AAA-SERVER-MIB',
            'casConfigTable',
            _yang_ns._namespaces['CISCO-AAA-SERVER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB'
        ),
    },
    'CiscoAaaServerMib' : {
        'meta_info' : _MetaInfoClass('CiscoAaaServerMib',
            False, 
            [
            _MetaInfoClassMember('casConfig', REFERENCE_CLASS, 'Casconfig' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB', 'CiscoAaaServerMib.Casconfig', 
                [], [], 
                '''                ''',
                'casconfig',
                'CISCO-AAA-SERVER-MIB', False),
            _MetaInfoClassMember('casConfigTable', REFERENCE_CLASS, 'Casconfigtable' , 'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB', 'CiscoAaaServerMib.Casconfigtable', 
                [], [], 
                '''                This table shows current configurations for each
                AAA server, allows existing servers to	be removed
                and new ones to be created.
                ''',
                'casconfigtable',
                'CISCO-AAA-SERVER-MIB', False),
            ],
            'CISCO-AAA-SERVER-MIB',
            'CISCO-AAA-SERVER-MIB',
            _yang_ns._namespaces['CISCO-AAA-SERVER-MIB'],
        'ydk.models.cisco_ios_xe.CISCO_AAA_SERVER_MIB'
        ),
    },
}
_meta_table['CiscoAaaServerMib.Casconfigtable.Casconfigentry']['meta_info'].parent =_meta_table['CiscoAaaServerMib.Casconfigtable']['meta_info']
_meta_table['CiscoAaaServerMib.Casconfig']['meta_info'].parent =_meta_table['CiscoAaaServerMib']['meta_info']
_meta_table['CiscoAaaServerMib.Casconfigtable']['meta_info'].parent =_meta_table['CiscoAaaServerMib']['meta_info']
