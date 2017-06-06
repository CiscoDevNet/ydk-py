


import re
import collections

from enum import Enum

from ydk._core._dm_meta_info import _MetaInfoClassMember, _MetaInfoClass, _MetaInfoEnum
from ydk.types import Empty, YList, YLeafList, DELETE, Decimal64, FixedBitsDict
from ydk._core._dm_meta_info import ATTRIBUTE, REFERENCE_CLASS, REFERENCE_LIST, REFERENCE_LEAFLIST,     REFERENCE_IDENTITY_CLASS, REFERENCE_ENUM_CLASS, REFERENCE_BITS, REFERENCE_UNION, ANYXML_CLASS

from ydk.errors import YPYError, YPYModelError
from ydk.providers._importer import _yang_ns
_meta_table = {
    'NetconfDatastoreTypeEnum' : _MetaInfoEnum('NetconfDatastoreTypeEnum', 'ydk.models.ietf.ietf_netconf_monitoring',
        {
            'running':'running',
            'candidate':'candidate',
            'startup':'startup',
        }, 'ietf-netconf-monitoring', _yang_ns._namespaces['ietf-netconf-monitoring']),
    'TransportIdentity' : {
        'meta_info' : _MetaInfoClass('TransportIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'transport',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'SchemaFormatIdentity' : {
        'meta_info' : _MetaInfoClass('SchemaFormatIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'schema-format',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Capabilities' : {
        'meta_info' : _MetaInfoClass('NetconfState.Capabilities',
            False, 
            [
            _MetaInfoClassMember('capability', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                List of NETCONF capabilities supported by the server.
                ''',
                'capability',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'capabilities',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Datastores.Datastore.Locks.GlobalLock' : {
        'meta_info' : _MetaInfoClass('NetconfState.Datastores.Datastore.Locks.GlobalLock',
            False, 
            [
            _MetaInfoClassMember('locked-by-session', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The session ID of the session that has locked
                this resource.  Both a global lock and a partial
                lock MUST contain the NETCONF session-id.
                
                If the lock is held by a session that is not managed
                by the NETCONF server (e.g., a CLI session), a session
                id of 0 (zero) is reported.
                ''',
                'locked_by_session',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('locked-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The date and time of when the resource was
                locked.
                ''',
                'locked_time',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'global-lock',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Datastores.Datastore.Locks.PartialLock' : {
        'meta_info' : _MetaInfoClass('NetconfState.Datastores.Datastore.Locks.PartialLock',
            False, 
            [
            _MetaInfoClassMember('lock-id', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                This is the lock id returned in the <partial-lock>
                response.
                ''',
                'lock_id',
                'ietf-netconf-monitoring', True),
            _MetaInfoClassMember('locked-by-session', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                The session ID of the session that has locked
                this resource.  Both a global lock and a partial
                lock MUST contain the NETCONF session-id.
                
                If the lock is held by a session that is not managed
                by the NETCONF server (e.g., a CLI session), a session
                id of 0 (zero) is reported.
                ''',
                'locked_by_session',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('locked-node', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                The list of instance-identifiers (i.e., the
                locked nodes).
                
                The scope of the partial lock is defined by the list
                of locked nodes.
                ''',
                'locked_node',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('locked-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                The date and time of when the resource was
                locked.
                ''',
                'locked_time',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('select', REFERENCE_LEAFLIST, 'str' , None, None, 
                [], [], 
                '''                The xpath expression that was used to request
                the lock.  The select expression indicates the
                original intended scope of the lock.
                ''',
                'select',
                'ietf-netconf-monitoring', False, min_elements=1),
            ],
            'ietf-netconf-monitoring',
            'partial-lock',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Datastores.Datastore.Locks' : {
        'meta_info' : _MetaInfoClass('NetconfState.Datastores.Datastore.Locks',
            False, 
            [
            _MetaInfoClassMember('global-lock', REFERENCE_CLASS, 'GlobalLock' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Datastores.Datastore.Locks.GlobalLock', 
                [], [], 
                '''                Present if the global lock is set.
                ''',
                'global_lock',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('partial-lock', REFERENCE_LIST, 'PartialLock' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Datastores.Datastore.Locks.PartialLock', 
                [], [], 
                '''                List of partial locks.
                ''',
                'partial_lock',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'locks',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Datastores.Datastore' : {
        'meta_info' : _MetaInfoClass('NetconfState.Datastores.Datastore',
            False, 
            [
            _MetaInfoClassMember('name', REFERENCE_ENUM_CLASS, 'NetconfDatastoreTypeEnum' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfDatastoreTypeEnum', 
                [], [], 
                '''                Name of the datastore associated with this list entry.
                ''',
                'name',
                'ietf-netconf-monitoring', True),
            _MetaInfoClassMember('locks', REFERENCE_CLASS, 'Locks' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Datastores.Datastore.Locks', 
                [], [], 
                '''                The NETCONF <lock> and <partial-lock> operations allow
                a client to lock specific resources in a datastore.  The
                NETCONF server will prevent changes to the locked
                resources by all sessions except the one that acquired
                the lock(s).
                
                Monitoring information is provided for each datastore
                entry including details such as the session that acquired
                the lock, the type of lock (global or partial) and the
                list of locked resources.  Multiple locks per datastore
                are supported.
                ''',
                'locks',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'datastore',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Datastores' : {
        'meta_info' : _MetaInfoClass('NetconfState.Datastores',
            False, 
            [
            _MetaInfoClassMember('datastore', REFERENCE_LIST, 'Datastore' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Datastores.Datastore', 
                [], [], 
                '''                List of NETCONF configuration datastores supported by
                the NETCONF server and related information.
                ''',
                'datastore',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'datastores',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Schemas.Schema.LocationEnum' : _MetaInfoEnum('LocationEnum', 'ydk.models.ietf.ietf_netconf_monitoring',
        {
            'NETCONF':'NETCONF',
        }, 'ietf-netconf-monitoring', _yang_ns._namespaces['ietf-netconf-monitoring']),
    'NetconfState.Schemas.Schema' : {
        'meta_info' : _MetaInfoClass('NetconfState.Schemas.Schema',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifier to uniquely reference the schema.  The
                identifier is used in the <get-schema> operation and may
                be used for other purposes such as file retrieval.
                
                For modeling languages that support or require a data
                model name (e.g., YANG module name) the identifier MUST
                match that name.  For YANG data models, the identifier is
                the name of the module or submodule.  In other cases, an
                identifier such as a filename MAY be used instead.
                ''',
                'identifier',
                'ietf-netconf-monitoring', True),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the schema supported.  Multiple versions MAY be
                supported simultaneously by a NETCONF server.  Each
                version MUST be reported individually in the schema list,
                i.e., with same identifier, possibly different location,
                but different version.
                
                For YANG data models, version is the value of the most
                recent YANG 'revision' statement in the module or
                submodule, or the empty string if no 'revision' statement
                is present.
                ''',
                'version',
                'ietf-netconf-monitoring', True),
            _MetaInfoClassMember('format', REFERENCE_IDENTITY_CLASS, 'SchemaFormatIdentity' , 'ydk.models.ietf.ietf_netconf_monitoring', 'SchemaFormatIdentity', 
                [], [], 
                '''                The data modeling language the schema is written
                in (currently xsd, yang, yin, rng, or rnc).
                For YANG data models, 'yang' format MUST be supported and
                'yin' format MAY also be provided.
                ''',
                'format',
                'ietf-netconf-monitoring', True),
            _MetaInfoClassMember('location', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                One or more locations from which the schema can be
                retrieved.  This list SHOULD contain at least one
                entry per schema.
                
                A schema entry may be located on a remote file system
                (e.g., reference to file system for ftp retrieval) or
                retrieved directly from a server supporting the
                <get-schema> operation (denoted by the value 'NETCONF').
                ''',
                'location',
                'ietf-netconf-monitoring', False, [
                    _MetaInfoClassMember('location', REFERENCE_LEAFLIST, 'NetconfState.Schemas.Schema.LocationEnum' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Schemas.Schema.LocationEnum', 
                        [], [], 
                        '''                        One or more locations from which the schema can be
                        retrieved.  This list SHOULD contain at least one
                        entry per schema.
                        
                        A schema entry may be located on a remote file system
                        (e.g., reference to file system for ftp retrieval) or
                        retrieved directly from a server supporting the
                        <get-schema> operation (denoted by the value 'NETCONF').
                        ''',
                        'location',
                        'ietf-netconf-monitoring', False),
                    _MetaInfoClassMember('location', REFERENCE_LEAFLIST, 'str' , None, None, 
                        [], [], 
                        '''                        One or more locations from which the schema can be
                        retrieved.  This list SHOULD contain at least one
                        entry per schema.
                        
                        A schema entry may be located on a remote file system
                        (e.g., reference to file system for ftp retrieval) or
                        retrieved directly from a server supporting the
                        <get-schema> operation (denoted by the value 'NETCONF').
                        ''',
                        'location',
                        'ietf-netconf-monitoring', False),
                ]),
            _MetaInfoClassMember('namespace', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The XML namespace defined by the data model.
                
                For YANG data models, this is the module's namespace.
                If the list entry describes a submodule, this field
                contains the namespace of the module to which the
                submodule belongs.
                ''',
                'namespace',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'schema',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Schemas' : {
        'meta_info' : _MetaInfoClass('NetconfState.Schemas',
            False, 
            [
            _MetaInfoClassMember('schema', REFERENCE_LIST, 'Schema' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Schemas.Schema', 
                [], [], 
                '''                List of data model schemas supported by the server.
                ''',
                'schema',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'schemas',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Sessions.Session' : {
        'meta_info' : _MetaInfoClass('NetconfState.Sessions.Session',
            False, 
            [
            _MetaInfoClassMember('session-id', ATTRIBUTE, 'int' , None, None, 
                [('1', '4294967295')], [], 
                '''                Unique identifier for the session.  This value is the
                NETCONF session identifier, as defined in RFC 4741.
                ''',
                'session_id',
                'ietf-netconf-monitoring', True),
            _MetaInfoClassMember('in-bad-rpcs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages received when an <rpc> message was expected,
                that were not correct <rpc> messages.  This includes XML parse
                errors and errors on the rpc layer.
                ''',
                'in_bad_rpcs',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('in-rpcs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of correct <rpc> messages received.
                ''',
                'in_rpcs',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('login-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Time at the server at which the session was established.
                ''',
                'login_time',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('out-notifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of <notification> messages sent.
                ''',
                'out_notifications',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('out-rpc-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of <rpc-reply> messages sent that contained an
                <rpc-error> element.
                ''',
                'out_rpc_errors',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('source-host', REFERENCE_UNION, 'str' , None, None, 
                [], [], 
                '''                Host identifier of the NETCONF client.  The value
                returned is implementation specific (e.g., hostname,
                IPv4 address, IPv6 address)
                ''',
                'source_host',
                'ietf-netconf-monitoring', False, [
                    _MetaInfoClassMember('source-host', REFERENCE_UNION, 'str' , None, None, 
                        [], [], 
                        '''                        Host identifier of the NETCONF client.  The value
                        returned is implementation specific (e.g., hostname,
                        IPv4 address, IPv6 address)
                        ''',
                        'source_host',
                        'ietf-netconf-monitoring', False, [
                            _MetaInfoClassMember('source-host', ATTRIBUTE, 'str' , None, None, 
                                [], [b'(([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\\.){3}([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Host identifier of the NETCONF client.  The value
                                returned is implementation specific (e.g., hostname,
                                IPv4 address, IPv6 address)
                                ''',
                                'source_host',
                                'ietf-netconf-monitoring', False),
                            _MetaInfoClassMember('source-host', ATTRIBUTE, 'str' , None, None, 
                                [], [b'((:|[0-9a-fA-F]{0,4}):)([0-9a-fA-F]{0,4}:){0,5}((([0-9a-fA-F]{0,4}:)?(:|[0-9a-fA-F]{0,4}))|(((25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])\\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9]?[0-9])))(%[\\p{N}\\p{L}]+)?'], 
                                '''                                Host identifier of the NETCONF client.  The value
                                returned is implementation specific (e.g., hostname,
                                IPv4 address, IPv6 address)
                                ''',
                                'source_host',
                                'ietf-netconf-monitoring', False),
                        ]),
                    _MetaInfoClassMember('source-host', ATTRIBUTE, 'str' , None, None, 
                        [], [b'((([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.)*([a-zA-Z0-9_]([a-zA-Z0-9\\-_]){0,61})?[a-zA-Z0-9]\\.?)|\\.'], 
                        '''                        Host identifier of the NETCONF client.  The value
                        returned is implementation specific (e.g., hostname,
                        IPv4 address, IPv6 address)
                        ''',
                        'source_host',
                        'ietf-netconf-monitoring', False),
                ]),
            _MetaInfoClassMember('transport', REFERENCE_IDENTITY_CLASS, 'TransportIdentity' , 'ydk.models.ietf.ietf_netconf_monitoring', 'TransportIdentity', 
                [], [], 
                '''                Identifies the transport for each session, e.g.,
                'netconf-ssh', 'netconf-soap', etc.
                ''',
                'transport',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('username', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                The username is the client identity that was authenticated
                by the NETCONF transport protocol.  The algorithm used to
                derive the username is NETCONF transport protocol specific
                and in addition specific to the authentication mechanism
                used by the NETCONF transport protocol.
                ''',
                'username',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'session',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Sessions' : {
        'meta_info' : _MetaInfoClass('NetconfState.Sessions',
            False, 
            [
            _MetaInfoClassMember('session', REFERENCE_LIST, 'Session' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Sessions.Session', 
                [], [], 
                '''                All NETCONF sessions managed by the NETCONF server
                MUST be reported in this list.
                ''',
                'session',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'sessions',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState.Statistics' : {
        'meta_info' : _MetaInfoClass('NetconfState.Statistics',
            False, 
            [
            _MetaInfoClassMember('dropped-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions that were abnormally terminated, e.g.,
                due to idle timeout or transport close.  This counter is not
                incremented when a session is properly closed by a
                <close-session> operation, or killed by a <kill-session>
                operation.
                ''',
                'dropped_sessions',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('in-bad-hellos', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions silently dropped because an
                invalid <hello> message was received.  This includes <hello>
                messages with a 'session-id' attribute, bad namespace, and
                bad capability declarations.
                ''',
                'in_bad_hellos',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('in-bad-rpcs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of messages received when an <rpc> message was expected,
                that were not correct <rpc> messages.  This includes XML parse
                errors and errors on the rpc layer.
                ''',
                'in_bad_rpcs',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('in-rpcs', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of correct <rpc> messages received.
                ''',
                'in_rpcs',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('in-sessions', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of sessions started.  This counter is incremented
                when a <hello> message with a <session-id> is sent.
                
                'in-sessions' - 'in-bad-hellos' =
                   'number of correctly started netconf sessions'
                ''',
                'in_sessions',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('netconf-start-time', ATTRIBUTE, 'str' , None, None, 
                [], [b'\\d{4}-\\d{2}-\\d{2}T\\d{2}:\\d{2}:\\d{2}(\\.\\d+)?(Z|[\\+\\-]\\d{2}:\\d{2})'], 
                '''                Date and time at which the management subsystem was
                started.
                ''',
                'netconf_start_time',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('out-notifications', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of <notification> messages sent.
                ''',
                'out_notifications',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('out-rpc-errors', ATTRIBUTE, 'int' , None, None, 
                [('0', '4294967295')], [], 
                '''                Number of <rpc-reply> messages sent that contained an
                <rpc-error> element.
                ''',
                'out_rpc_errors',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'statistics',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfState' : {
        'meta_info' : _MetaInfoClass('NetconfState',
            False, 
            [
            _MetaInfoClassMember('capabilities', REFERENCE_CLASS, 'Capabilities' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Capabilities', 
                [], [], 
                '''                Contains the list of NETCONF capabilities supported by the
                server.
                ''',
                'capabilities',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('datastores', REFERENCE_CLASS, 'Datastores' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Datastores', 
                [], [], 
                '''                Contains the list of NETCONF configuration datastores.
                ''',
                'datastores',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('schemas', REFERENCE_CLASS, 'Schemas' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Schemas', 
                [], [], 
                '''                Contains the list of data model schemas supported by the
                server.
                ''',
                'schemas',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('sessions', REFERENCE_CLASS, 'Sessions' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Sessions', 
                [], [], 
                '''                The sessions container includes session-specific data for
                NETCONF management sessions.  The session list MUST include
                all currently active NETCONF sessions.
                ''',
                'sessions',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('statistics', REFERENCE_CLASS, 'Statistics' , 'ydk.models.ietf.ietf_netconf_monitoring', 'NetconfState.Statistics', 
                [], [], 
                '''                Statistical data pertaining to the NETCONF server.
                ''',
                'statistics',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'netconf-state',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'GetSchemaRpc.Input' : {
        'meta_info' : _MetaInfoClass('GetSchemaRpc.Input',
            False, 
            [
            _MetaInfoClassMember('identifier', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Identifier for the schema list entry.
                ''',
                'identifier',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('version', ATTRIBUTE, 'str' , None, None, 
                [], [], 
                '''                Version of the schema requested.  If this parameter is not
                present, and more than one version of the schema exists on
                the server, a 'data-not-unique' error is returned, as
                described above.
                ''',
                'version',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('format', REFERENCE_IDENTITY_CLASS, 'SchemaFormatIdentity' , 'ydk.models.ietf.ietf_netconf_monitoring', 'SchemaFormatIdentity', 
                [], [], 
                '''                The data modeling language of the schema.  If this
                parameter is not present, and more than one formats of
                the schema exists on the server, a 'data-not-unique' error
                is returned, as described above.
                ''',
                'format',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'input',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'GetSchemaRpc.Output' : {
        'meta_info' : _MetaInfoClass('GetSchemaRpc.Output',
            False, 
            [
            _MetaInfoClassMember('data', ANYXML_CLASS, 'object' , None, None, 
                [], [], 
                '''                Contains the schema content.
                ''',
                'data',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'output',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'GetSchemaRpc' : {
        'meta_info' : _MetaInfoClass('GetSchemaRpc',
            False, 
            [
            _MetaInfoClassMember('input', REFERENCE_CLASS, 'Input' , 'ydk.models.ietf.ietf_netconf_monitoring', 'GetSchemaRpc.Input', 
                [], [], 
                '''                ''',
                'input',
                'ietf-netconf-monitoring', False),
            _MetaInfoClassMember('output', REFERENCE_CLASS, 'Output' , 'ydk.models.ietf.ietf_netconf_monitoring', 'GetSchemaRpc.Output', 
                [], [], 
                '''                ''',
                'output',
                'ietf-netconf-monitoring', False),
            ],
            'ietf-netconf-monitoring',
            'get-schema',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfBeepIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfBeepIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'netconf-beep',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'RngIdentity' : {
        'meta_info' : _MetaInfoClass('RngIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'rng',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'XsdIdentity' : {
        'meta_info' : _MetaInfoClass('XsdIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'xsd',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfSshIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfSshIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'netconf-ssh',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'RncIdentity' : {
        'meta_info' : _MetaInfoClass('RncIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'rnc',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'YinIdentity' : {
        'meta_info' : _MetaInfoClass('YinIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'yin',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'YangIdentity' : {
        'meta_info' : _MetaInfoClass('YangIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'yang',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfSoapOverHttpsIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfSoapOverHttpsIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'netconf-soap-over-https',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfSoapOverBeepIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfSoapOverBeepIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'netconf-soap-over-beep',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
    'NetconfTlsIdentity' : {
        'meta_info' : _MetaInfoClass('NetconfTlsIdentity',
            False, 
            [
            ],
            'ietf-netconf-monitoring',
            'netconf-tls',
            _yang_ns._namespaces['ietf-netconf-monitoring'],
        'ydk.models.ietf.ietf_netconf_monitoring'
        ),
    },
}
_meta_table['NetconfState.Datastores.Datastore.Locks.GlobalLock']['meta_info'].parent =_meta_table['NetconfState.Datastores.Datastore.Locks']['meta_info']
_meta_table['NetconfState.Datastores.Datastore.Locks.PartialLock']['meta_info'].parent =_meta_table['NetconfState.Datastores.Datastore.Locks']['meta_info']
_meta_table['NetconfState.Datastores.Datastore.Locks']['meta_info'].parent =_meta_table['NetconfState.Datastores.Datastore']['meta_info']
_meta_table['NetconfState.Datastores.Datastore']['meta_info'].parent =_meta_table['NetconfState.Datastores']['meta_info']
_meta_table['NetconfState.Schemas.Schema']['meta_info'].parent =_meta_table['NetconfState.Schemas']['meta_info']
_meta_table['NetconfState.Sessions.Session']['meta_info'].parent =_meta_table['NetconfState.Sessions']['meta_info']
_meta_table['NetconfState.Capabilities']['meta_info'].parent =_meta_table['NetconfState']['meta_info']
_meta_table['NetconfState.Datastores']['meta_info'].parent =_meta_table['NetconfState']['meta_info']
_meta_table['NetconfState.Schemas']['meta_info'].parent =_meta_table['NetconfState']['meta_info']
_meta_table['NetconfState.Sessions']['meta_info'].parent =_meta_table['NetconfState']['meta_info']
_meta_table['NetconfState.Statistics']['meta_info'].parent =_meta_table['NetconfState']['meta_info']
_meta_table['GetSchemaRpc.Input']['meta_info'].parent =_meta_table['GetSchemaRpc']['meta_info']
_meta_table['GetSchemaRpc.Output']['meta_info'].parent =_meta_table['GetSchemaRpc']['meta_info']
